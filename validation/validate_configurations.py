#!/usr/bin/env python3
"""
Validation AUTOMATIQUE des CONFIGURATIONS extraites (valeurs numeriques), en
complement de la validation des entites (datasets, metrics, kge, ns...).

Principe : un SECOND LLM, INDEPENDANT du modele qui a peuple le KG (peuplement
= Claude, donc juge = GPT), joue le verificateur. Pour chaque article, il recoit :
  - les TABLEAUX bruts de l'article (load_md_tables_only, forme d'origine, non
    minimisee : chaque tableau a une forme differente, on ne prend pas le risque
    de la reecrire) ;
  - les CONFIGURATIONS extraites par la pipeline, sous forme MINIMALISTE
    deterministe (Task factorisee en tete de section ; le reste du tuple ecrit
    par ligne).

Le juge verifie le tuple COMPLET : Dataset + Metric + KGEModel + NSMethod + Task
+ valeur.
  - Dataset/Metric/KGEModel/valeur : doivent correspondre a une cellule reelle.
  - NSMethod/Task : les tableaux n'ont en general pas de colonne dediee ; on les
    infere des libelles de ligne / du modele propose / de la legende.
      * "Unknown" (NS non precise) = le tableau N'ATTRIBUE PAS de methode a cette
        ligne. C'est ACCEPTABLE, pas une erreur, tant que la cellule
        (dataset, metric, model, valeur) existe.
      * une NSMethod SPECIFIQUE doit etre coherente avec le tableau (ligne du
        modele propose, baseline nommee d'apres la methode...) ; on ne signale
        qu'une contradiction franche.

Sortie du juge = ANOMALIES SEULES (report-by-exception) : l'output scale avec le
nombre d'erreurs, pas avec les milliers de configs. [] => tout correct.

On NE mesure PAS le rappel (on sait que la pipeline n'extrait pas toutes les
lignes). Les regles Top-3 / couverture ne sont PAS traitees ici (hors scope).

Usage :
    python validate_configurations.py --list-models        # trouver l'id de Luna
    python validate_configurations.py --article adaptativens --model <id>
    python validate_configurations.py --all --model <id>
"""
import argparse
import glob
import json
import os
import sys

# --- chemins -----------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))          # /home/ilyes/POSTER
KG_DIR = os.path.join(ROOT, "ns4kge-kg", "per_article")
MD_DIR = os.path.join(ROOT, "liste_mds")
PIPELINE_SRC = os.path.join(ROOT, "ns4kge-extraction-pipeline", "src")
ENV_PATH = os.path.join(ROOT, "ns4kge-kg", ".env")
OUT_DIR = os.path.join(HERE, "reports_configurations")

# reutilise l'extracteur de tableaux DETERMINISTE de la pipeline (pas de reecriture)
sys.path.insert(0, PIPELINE_SRC)
from no_facts_pipeline.core import load_md_tables_only  # noqa: E402

DEFAULT_MODEL = "gpt-5.6-terra"  # Luna faisait des faux "tuple absent" sur les
                                 # en-tetes multi-niveaux ; Terra les lit correctement.


# --------------------------------------------------------------------------
# Chargement articles + mapping slug -> .md
# --------------------------------------------------------------------------
def md_index():
    return {os.path.basename(p)[:-3].lower(): p
            for p in glob.glob(os.path.join(MD_DIR, "*.md"))}


def load_article(slug, mds):
    data = json.load(open(os.path.join(KG_DIR, f"{slug}_merged.json"), encoding="utf-8"))
    cfgs = (data.get("Experimentation", {}) or {}).get("Configurations", []) or []
    md = mds.get(slug)
    if not md:
        raise FileNotFoundError(f"pas de .md pour {slug}")
    return {
        "slug": slug,
        "title": (data.get("Article", {}) or {}).get("title", slug),
        "tables": load_md_tables_only(md),
        "configs": cfgs,
    }


# --------------------------------------------------------------------------
# Forme minimaliste DETERMINISTE des configs (Task factorisee, reste par ligne)
# id = index dans le tableau JSON -> remap trivial des anomalies
# --------------------------------------------------------------------------
def make_canaries(cfgs, tables):
    """1 fausse config DETERMINISTE, indiscernable d'une vraie ligne, pour prouver
    PAR ARTICLE que le juge discrimine (ne tamponne pas un 100%). id SEQUENTIEL (n)
    -> invisible comme plant. Retourne [(id, cfg, kind)].

    Priorite : SWAP de dataset entre 2 lignes de meme (metric, model) mais dataset
    et valeur differents -> la valeur reste une VRAIE valeur du tableau, placee a la
    MAUVAISE cellule. Teste la metrique "combinaison correcte" (localisation), la
    plus importante. Garanti faux (les 2 valeurs different).

    Fallback (si aucune paire) : valeur bidon (vraie x 0.7) -> valeur absente."""
    if not cfgs:
        return []
    n = len(cfgs)
    groups = {}
    for i, c in enumerate(cfgs):
        groups.setdefault((c.get("Metric"), c.get("KGEModel")), []).append(i)
    for idxs in groups.values():
        for a in idxs:
            for b in idxs:
                if (a != b and cfgs[a].get("Dataset") != cfgs[b].get("Dataset")
                        and str(cfgs[a].get("result")) != str(cfgs[b].get("result"))):
                    c = dict(cfgs[a])
                    c["Dataset"] = cfgs[b]["Dataset"]      # valeur reelle, mauvaise cellule
                    return [(n, c, "swap")]
    a = dict(cfgs[0])                                       # fallback : valeur bidon
    try:
        v = float(a.get("result"))
        a["result"] = round(v * 0.7, 4) if v else 0.333
    except (TypeError, ValueError):
        a["result"] = 0.333
    if str(a["result"]) == str(cfgs[0].get("result")):
        a["result"] = 0.333
    return [(n, a, "fake")]


def build_config_block(indexed_cfgs):
    """indexed_cfgs : liste de (id, cfg). id = index JSON reel, ou id sentinelle
    pour un canari. Task factorisee en tete de section."""
    by_task = {}
    for i, c in indexed_cfgs:
        by_task.setdefault(c.get("Task", "Unknown"), []).append((i, c))
    lines = []
    for task in sorted(by_task):
        lines.append(f"== task: {task} ==")
        lines.append("id|dataset|metric|model|ns|val")
        for i, c in by_task[task]:
            lines.append("|".join([
                str(i),
                str(c.get("Dataset", "")),
                str(c.get("Metric", "")),
                str(c.get("KGEModel", "")),
                str(c.get("NSMethod", "")),
                str(c.get("result", "")),
            ]))
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Prompt
# --------------------------------------------------------------------------
SYSTEM = (
    "You are an INDEPENDENT verifier of a scientific extraction pipeline. "
    "You receive the RAW results tables of a paper and a list of configurations "
    "the pipeline extracted from them. Verify each configuration ONLY against the "
    "tables. Be strict but fair with numeric formatting."
)

INSTRUCTIONS = """\
For EACH configuration line, run TWO checks against the TABLES only.

  (A) VALUE EXISTS — does the number `val` appear ANYWHERE in the tables (any cell)?
  (B) COMBINATION CORRECT — is `val` at the RIGHT place: does the cell at
      (dataset, metric, kgemodel) exist AND equal `val`, with ns consistent?

A config is FULLY CORRECT iff (B) holds (then (A) necessarily holds too). A config
can have (A) true but (B) false: the value is real but attached to the WRONG
combination (e.g. right number, wrong dataset).

READING THE TABLES (headers are messy):
  * Multi-level headers: a dataset header with colspan spans several metric
    sub-columns. Map each cell to (dataset = top-level group, metric = sub-column).
    Count columns carefully across colspans.
  * Abbreviations / typos — match SEMANTICALLY, not by identical spelling:
      metrics "H@1"=="Hits@1", "H@10"=="Hits@10", "MR" != "MRR";
      datasets "WN8RR"=="WN18RR", "FB15k237"=="FB15k-237"; models "MuRp"=="MuRP".
  * Numeric equality is lenient: strip a trailing % (26.96 == "26.96%"; do NOT
    rescale otherwise), ignore trailing zeros / rounding (0.43 == 0.430).
  * ns == "Unknown" is ALWAYS acceptable (tables have no ns column). A SPECIFIC ns
    is wrong only if the table clearly contradicts it. `task` -> ignore entirely.

  * PROPOSED-METHOD ROW: the paper's own method is often a row labelled "Proposed",
    "Ours", "Our", "Our method", or the paper's acronym — NOT by the base-model name.
    A config whose ns is the paper's proposed sampling method (kgemodel = the base
    model) refers to THAT row, not the same-named baseline row. When several rows
    share the same base model, use ns to pick the right one:
      - ns == a specific proposed method -> the "Proposed"/"Ours"/acronym row;
      - ns == "Unknown" -> the plain baseline row named after the model.
  * NESTED ROWSPAN: a model cell may span (rowspan) several sub-rows, one per ns
    method (e.g. Bernoulli, KBGAN, NSCaching, ...). Match (kgemodel, ns) to the
    correct SUB-ROW; do not collapse them to the first row of the group.

Report ONLY configs where (B) FAILS, as a JSON array:
  {"id": <int>, "exists": true|false}
  - "exists" is the result of check (A): is `val` present somewhere in the tables?
      true  = the value is real but mis-associated (right number, wrong combination);
      false = the value is not in the tables at all (hallucinated / plain wrong number).
A config ABSENT from the array = fully correct (both checks pass).
Output STRICTLY the JSON array and nothing else. [] if every config is fully correct.
"""


def build_prompt(article, canaries):
    indexed = list(enumerate(article["configs"])) + [(cid, c) for cid, c, _ in canaries]
    return (
        f"{INSTRUCTIONS}\n"
        f"=== TABLES (raw, verbatim from the paper) ===\n{article['tables']}\n\n"
        f"=== CONFIGURATIONS TO VERIFY ===\n{build_config_block(indexed)}\n"
    )


# --------------------------------------------------------------------------
# Appel LLM
# --------------------------------------------------------------------------
def make_client():
    from dotenv import load_dotenv
    load_dotenv(ENV_PATH)
    from openai import OpenAI
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        sys.exit(f"[ERREUR] OPENAI_API_KEY absente. Mets-la dans {ENV_PATH}")
    return OpenAI(api_key=key)


def list_models(client):
    ms = sorted(m.id for m in client.models.list())
    hit = [m for m in ms if any(k in m.lower() for k in ("luna", "5.6", "5-6", "terra", "sol"))]
    print("Modeles pertinents (luna/5.6/terra/sol) :")
    for m in hit:
        print("  ", m)
    print(f"\n({len(ms)} modeles au total)")


def call_judge(client, model, prompt):
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content


def parse_anomalies(txt):
    s = txt.strip()
    if s.startswith("```"):
        s = s.strip("`")
        s = s[s.find("["):]
    a = s.find("["); b = s.rfind("]")
    if a == -1 or b == -1:
        raise ValueError(f"reponse non-JSON: {txt[:200]}")
    return json.loads(s[a:b + 1])


# --------------------------------------------------------------------------
# Stats
# --------------------------------------------------------------------------
def stats_for(article, anomalies):
    n = len(article["configs"])
    by_id = {a["id"]: a for a in anomalies if isinstance(a.get("id"), int)}
    combo_wrong = len(by_id)                                 # (B) echoue
    val_absent = sum(1 for a in by_id.values() if not a.get("exists", False))  # (A) echoue
    return {
        "n": n,
        "combo_ok": n - combo_wrong,          # combinaison correcte
        "val_exists_ok": n - val_absent,      # valeur presente dans les tables
        "acc_combo": (n - combo_wrong) / n if n else 1.0,
        "acc_val_exists": (n - val_absent) / n if n else 1.0,
    }


# --------------------------------------------------------------------------
# Rendu markdown (deterministe) — transforme la reponse minimaliste du LLM
# en tableau propre : 2 chiffres (valeur existe / combinaison correcte) + canari.
# --------------------------------------------------------------------------
def _esc(s):
    return str(s).replace("|", "\\|")


def render_markdown(article, anomalies, st):
    n = st["n"]
    L = [f"# Configurations — {article['slug']}", "",
         f"**Titre :** {article['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Configs verifiees | {n} |",
         f"| Valeur existe dans les tables | {st['val_exists_ok']}/{n} |",
         f"| **① Accuracy — valeur existe** | **{st['acc_val_exists']:.1%}** |",
         f"| Combinaison (dataset/metric/model/ns) correcte | {st['combo_ok']}/{n} |",
         f"| **② Accuracy — combinaison correcte** | **{st['acc_combo']:.1%}** |"]
    ct = st.get("canary_total", 0)
    if ct:
        ok = st["canary_caught"] == ct
        L.append(f"| **③ 🐤 Canari attrape** | **{st['canary_caught']}/{ct} "
                 f"— {'✅ fiable' if ok else '⚠️ PEU FIABLE'}** |")
    L.append("")

    L += ["## Configs fautives (combinaison incorrecte)", ""]
    if anomalies:
        L += ["| # | Dataset | Metric | KGEModel | NS | Valeur | Valeur existe ? |",
              "|---|---|---|---|---|---|:--:|"]
        for a in sorted(anomalies, key=lambda x: x.get("id", -1)):
            i = a.get("id")
            c = article["configs"][i] if isinstance(i, int) and i < n else {}
            exists = "✅ oui (mal associee)" if a.get("exists") else "❌ non (absente)"
            L.append(f"| {i} | {_esc(c.get('Dataset',''))} | {_esc(c.get('Metric',''))} "
                     f"| {_esc(c.get('KGEModel',''))} | {_esc(c.get('NSMethod',''))} "
                     f"| {_esc(c.get('result',''))} | {exists} |")
    else:
        L.append("_Aucune config fautive — combinaison correcte partout._")
    L.append("")
    return "\n".join(L)


def render_summary(rows):
    N = sum(s["n"] for _, s in rows)
    VEX = sum(s["val_exists_ok"] for _, s in rows)
    CMB = sum(s["combo_ok"] for _, s in rows)
    CAN_OK = sum(s.get("canary_caught", 0) for _, s in rows)
    CAN_TOT = sum(s.get("canary_total", 0) for _, s in rows)
    L = ["# Recap validation CONFIGURATIONS (juge LLM independant)", "",
         "3 chiffres par article : ① valeur existe, ② combinaison correcte, ③ canari.", "",
         "| Article | Configs | ① valeur existe | ② combinaison correcte | ③ 🐤 |",
         "|---|---:|:--:|:--:|:--:|"]
    for name, s in rows:
        ct = s.get("canary_total", 0)
        can = f"{s.get('canary_caught',0)}/{ct}" if ct else "—"
        flag = "" if s.get("canary_caught", 0) == ct else " ⚠️"
        L.append(f"| {name} | {s['n']} | {s['acc_val_exists']:.1%} "
                 f"| {s['acc_combo']:.1%} | {can}{flag} |")
    L += ["", "## Totaux (micro)", "", "| Metrique | Valeur |", "|---|---|",
          f"| Configs verifiees | {N} |",
          f"| Valeur existe dans les tables | {VEX}/{N} |",
          f"| **① Accuracy — valeur existe** | **{VEX/N if N else 1.0:.1%}** |",
          f"| Combinaison correcte | {CMB}/{N} |",
          f"| **② Accuracy — combinaison correcte** | **{CMB/N if N else 1.0:.1%}** |",
          f"| **③ 🐤 Canaris attrapes (sanity)** | **{CAN_OK}/{CAN_TOT}** |", ""]
    return "\n".join(L)


def print_report(article, anomalies, st):
    n = st["n"]
    print(f"\n=== {article['slug']}  ({article['title'][:60]}) ===")
    print(f"configs verifiees            : {n}")
    print(f"① valeur existe              : {st['acc_val_exists']:.1%}  ({st['val_exists_ok']}/{n})")
    print(f"② combinaison correcte       : {st['acc_combo']:.1%}  ({st['combo_ok']}/{n})")
    ct = st.get("canary_total", 0)
    if ct:
        ok = st["canary_caught"] == ct
        print(f"③ canari attrape             : {st['canary_caught']}/{ct} "
              f"{'✅' if ok else '⚠️ JUGE PEU FIABLE POUR CET ARTICLE'}")
    if anomalies:
        print("\nConfigs fautives (combinaison incorrecte) :")
        for a in sorted(anomalies, key=lambda x: x.get("id", -1)):
            c = article["configs"][a["id"]] if isinstance(a.get("id"), int) and a["id"] < n else {}
            ex = "valeur existe (mal associee)" if a.get("exists") else "valeur absente"
            print(f"  #{a.get('id')} {c.get('Dataset','?')}/{c.get('Metric','?')}"
                  f"/{c.get('KGEModel','?')}/ns={c.get('NSMethod','?')}={c.get('result','?')}"
                  f"  -> {ex}")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--article", help="slug d'un article (ex: adaptativens)")
    ap.add_argument("--all", action="store_true", help="tous les articles")
    ap.add_argument("--limit", type=int, help="avec --all : ne traiter que les N premiers")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--dump-prompt", action="store_true",
                    help="affiche le prompt sans appeler le LLM (debug/tokens)")
    args = ap.parse_args()

    mds = md_index()

    if args.dump_prompt:
        art = load_article(args.article, mds)
        print(build_prompt(art, make_canaries(art["configs"], art["tables"])))
        return

    client = make_client()
    if args.list_models:
        list_models(client)
        return

    slugs = ([os.path.basename(p)[:-len("_merged.json")]
              for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json")))]
             if args.all else [args.article])
    if not slugs or slugs == [None]:
        sys.exit("Precise --article <slug> ou --all")
    if args.limit:
        slugs = slugs[:args.limit]

    os.makedirs(OUT_DIR, exist_ok=True)
    summary_rows = []
    for slug in slugs:
        art = load_article(slug, mds)
        if not art["configs"]:
            print(f"[skip] {slug} : 0 config")
            continue
        canaries = make_canaries(art["configs"], art["tables"])
        raw = call_judge(client, args.model, build_prompt(art, canaries))
        all_anomalies = parse_anomalies(raw)

        # separer canaris des vraies anomalies via l'ensemble d'ids (cote Python,
        # invisible au juge) ; un canari est "attrape" s'il ressort comme
        # combinaison incorrecte (il l'est par construction : valeur mal placee).
        expect_ids = {cid for cid, _, _ in canaries}
        caught = {a["id"] for a in all_anomalies if a.get("id") in expect_ids}
        anomalies = [a for a in all_anomalies if a.get("id") not in expect_ids]

        st = stats_for(art, anomalies)
        st["canary_caught"] = len(caught)
        st["canary_total"] = len(canaries)
        print_report(art, anomalies, st)
        json.dump({"slug": slug, "stats": st, "anomalies": anomalies,
                   "canary": {"caught": sorted(caught), "ids": sorted(expect_ids)}},
                  open(os.path.join(OUT_DIR, f"{slug}.json"), "w"), indent=2)
        open(os.path.join(OUT_DIR, f"{slug}.md"), "w", encoding="utf-8").write(
            render_markdown(art, anomalies, st))
        summary_rows.append((slug, st))

    if summary_rows:
        open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
            render_summary(summary_rows))
        print(f"\nRapports -> {OUT_DIR}/  (par article .md/.json + _SUMMARY.md)")


if __name__ == "__main__":
    main()
