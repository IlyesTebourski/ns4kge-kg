#!/usr/bin/env python3
"""
Validation des KGE MODELS extraits par le KG, avec DISTINCTION DE PROVENANCE.

Les KGE models viennent de deux sources, que l'ontologie distingue :
- EVALUES  : Configurations[].KGEModel  -> prompt2 -> tables (modeles reellement
             testes dans les experiences de l'article).
- MENTIONNES/PROPOSES : proposedKGEModel + mentionedKGEModels -> prompt1 -> prose
             (modeles cites, related work... mais pas forcement evalues).

Cette validation EXPLICITE cette distinction : on valide separement
  (a) les modeles evalues, contre les tableaux (`load_md_tables_only`)
  (b) les modeles seulement mentionnes, contre la prose (`load_md_no_tables`)

Matching (hybride, deterministe) :
- PRECISION : insensible a la casse (ne pas rater ComplEx vs "Complex").
- RECALL    : sensible a la casse (les noms KGE sont stylises comme des mots
              anglais : RatE/SimplE/TaKE/LINE -> sinon bruit massif).

Sorties : validation/reports_kgemodels/<slug>.md + _SUMMARY.md
"""
import json
import glob
import os
import re

import validate_datasets as VD   # snippet_around, norm_key, dirs

MD_DIR = VD.MD_DIR
KG_DIR = VD.KG_DIR
OUT_DIR = os.path.join(VD.HERE, "reports_kgemodels")

# separateurs entre tokens : espaces, tirets, /, ., @, parentheses, crochets.
# (mais PAS '+' : "TransE+STC+TCE" doit rester non-matche = compound non splitte.)
SEP = r"[\s\-_/.@()\[\]]*"

# Termes que le LLM a parfois extraits comme "KGE model" mais qui n'en sont pas
# (frameworks / composants / techniques generiques). On les exclut du RECALL :
# la question "a-t-on rate un modele KGE ?" ne doit pas les considerer. Leur
# presence dans le vocab revele d'ailleurs une incoherence d'extraction (KG).
NON_KGE = {"gan", "mlp", "attention", "bert", "word2vec",
           "cnn", "rnn", "lstm", "transformer", "tucker"}


def toks_cs(label):
    """Tokens en conservant la casse (pour le matching sensible a la casse)."""
    return re.findall(r"[A-Za-z0-9]+", label)


def build_pattern(label, ci):
    toks = toks_cs(label)
    if not toks:
        return None
    core = SEP.join(re.escape(t) for t in toks)
    return re.compile(r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])",
                      re.I if ci else 0)


def found(label, text, ci):
    pat = build_pattern(label, ci)
    if pat is None:
        return None
    return pat.search(text)


# --------------------------------------------------------------------------
def load_articles():
    from no_facts_pipeline.core import load_md_tables_only, load_md_no_tables
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            continue
        data = json.load(open(p, encoding="utf-8"))
        models = {}   # {norm_key: {"label", "src":set}}

        def add(val, src):
            if not val or not str(val).strip():
                return
            val = str(val).strip()
            k = VD.norm_key(val)
            if k:
                models.setdefault(k, {"label": val, "src": set()})["src"].add(src)

        add(data.get("proposedKGEModel"), "prose")
        for m in data.get("mentionedKGEModels", []) or []:
            add(m, "prose")
        for c in data.get("Experimentation", {}).get("Configurations", []) or []:
            if isinstance(c, dict):
                add(c.get("KGEModel"), "table")

        arts.append({
            "slug": slug, "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "prose": load_md_no_tables(md), "tables": load_md_tables_only(md),
            "models": models,
        })
    return arts


def build_global_vocab(arts):
    vocab = {}
    for a in arts:
        for k, e in a["models"].items():
            vocab.setdefault(k, e["label"])
    return vocab


def validate(article, vocab):
    prose, tables = article["prose"], article["tables"]
    evaluated, mentioned = [], []   # (label, found, snippet)
    te = fe = tm = fm = 0

    for k, e in sorted(article["models"].items(), key=lambda kv: kv[1]["label"].lower()):
        label, src = e["label"], e["src"]
        if "table" in src:                      # EVALUE -> valider vs tables
            m = found(label, tables, ci=True)
            evaluated.append((label, bool(m), VD.snippet_around(tables, m) if m else ""))
            te += bool(m); fe += (not m)
        else:                                   # MENTIONNE seul -> valider vs prose
            m = found(label, prose, ci=True)
            mentioned.append((label, bool(m), VD.snippet_around(prose, m) if m else ""))
            tm += bool(m); fm += (not m)

    # RECALL (sensible a la casse) : modele du vocab mentionne dans l'article
    # (prose OU tables) mais non extrait. On exclut les non-modeles KGE
    # (GAN/MLP/...) : ne pas les extraire est correct, ce ne sont pas des
    # instances de KGEModel -> sinon la mesure de recall serait biaisee.
    suspects = []
    for k, label in sorted(vocab.items(), key=lambda kv: kv[1].lower()):
        if k in article["models"] or k in NON_KGE:
            continue
        mp = found(label, prose, ci=False)
        mt = found(label, tables, ci=False)
        if mp or mt:
            where = "+".join(w for w, mm in (("prose", mp), ("table", mt)) if mm)
            m = mp or mt
            src_txt = prose if mp else tables
            suspects.append((label, where, VD.snippet_around(src_txt, m)))
    return evaluated, mentioned, suspects, (te, fe, tm, fm)


# --------------------------------------------------------------------------
def esc(s):
    return s.replace("|", "\\|")


def split_suspects(suspects):
    """Separe les candidats recall : dans un tableau (evaluation ratee) vs prose
    seulement (mention ratee)."""
    missed_eval = [(l, w, s) for l, w, s in suspects if "table" in w]
    missed_ment = [(l, w, s) for l, w, s in suspects if "table" not in w]
    return missed_eval, missed_ment


def render_article(a, evaluated, mentioned, suspects, counts):
    te, fe, tm, fm = counts
    tp, fp = te + tm, fe + fm
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    pe = te / (te + fe) if (te + fe) else 1.0
    pm = tm / (tm + fm) if (tm + fm) else 1.0
    miss_e, miss_m = split_suspects(suspects)
    re_e = te / (te + len(miss_e)) if (te + len(miss_e)) else 1.0
    re_m = tm / (tm + len(miss_m)) if (tm + len(miss_m)) else 1.0

    L = [f"# KGE Models — {a['md_name']}", "", f"**Titre :** {a['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Modeles EVALUES (dans les tableaux) | {te + fe} |",
         f"| Modeles MENTIONNES seulement (hors tableaux) | {tm + fm} |",
         f"| **Precision globale** | **{prec:.0%}** |",
         f"| Precision (evalues, vs tableaux) | {pe:.0%} |",
         f"| Precision (mentionnes, vs prose) | {pm:.0%} |",
         f"| Candidats evaluations ratees (en tableau, non extrait) | {len(miss_e)} |",
         f"| Candidats mentions ratees (en prose, non extrait) | {len(miss_m)} |",
         f"| Recall relatif *evalues* | {re_e:.0%} |",
         f"| Recall relatif *mentionnes* | {re_m:.0%} |", "",
         "## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)", "",
         "| Modele | Trouve dans les tableaux ? | Extrait |", "|---|:---:|---|"]
    for label, ok, snip in evaluated:
        L.append(f"| {esc(label)} | {'✅ oui' if ok else '❌ NON'} | {esc(snip) if ok else '_(absent des tableaux)_'} |")
    L += ["", "## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)", ""]
    if mentioned:
        L += ["| Modele | Trouve dans la prose ? | Extrait |", "|---|:---:|---|"]
        for label, ok, snip in mentioned:
            L.append(f"| {esc(label)} | {'✅ oui' if ok else '❌ NON'} | {esc(snip) if ok else '_(absent de la prose)_'} |")
    else:
        L.append("_Aucun modele mentionne hors tableaux._")

    L += ["", "## C1. Recall EVALUES — modeles dans un tableau mais NON extraits", ""]
    if miss_e:
        L += ["| Modele | Ou | Extrait |", "|---|---|---|"]
        L += [f"| {esc(l)} | {w} | {esc(s)} |" for l, w, s in miss_e]
    else:
        L.append("_Aucun._")
    L += ["", "## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits", ""]
    if miss_m:
        L += ["| Modele | Ou | Extrait |", "|---|---|---|"]
        L += [f"| {esc(l)} | {w} | {esc(s)} |" for l, w, s in miss_m]
    else:
        L.append("_Aucun._")
    return "\n".join(L), (te, fe, tm, fm, len(miss_e), len(miss_m), prec, re_e, re_m)


def render_summary(rows, TE, FE, TM, FM, SUS_E, SUS_M):
    TP, FP = TE + TM, FE + FM
    mp = TP / (TP + FP) if (TP + FP) else 1.0
    pe = TE / (TE + FE) if (TE + FE) else 1.0
    pm = TM / (TM + FM) if (TM + FM) else 1.0
    re_e = TE / (TE + SUS_E) if (TE + SUS_E) else 1.0
    re_m = TM / (TM + SUS_M) if (TM + SUS_M) else 1.0
    L = ["# Recap validation KGE MODELS (provenance explicite)", "",
         f"Articles : **{len(rows)}**", "",
         "| Article | Eval. | Ment. | Prec.eval | Prec.ment | Prec.glob | Manq.eval | Manq.ment |",
         "|---|---:|---:|:---:|:---:|:---:|---:|---:|"]
    for name, te, fe, tm, fm, nse, nsm, prec, r_e, r_m in rows:
        pe_ = te / (te + fe) if (te + fe) else 1.0
        pm_ = tm / (tm + fm) if (tm + fm) else 1.0
        L.append(f"| {name} | {te+fe} | {tm+fm} | {pe_:.0%} | {pm_:.0%} | {prec:.0%} | {nse} | {nsm} |")
    L += ["", "## Totaux", "", "| Metrique | Valeur |", "|---|---|",
          f"| Modeles EVALUES (tableaux) | {TE + FE} |",
          f"| Modeles MENTIONNES seulement | {TM + FM} |",
          f"| **Precision globale (micro)** | **{mp:.1%}** |",
          f"| Precision modeles evalues | {pe:.1%} |",
          f"| Precision modeles mentionnes | {pm:.1%} |",
          f"| Candidats evaluations ratees (en tableau) | {SUS_E} |",
          f"| Candidats mentions ratees (en prose) | {SUS_M} |",
          f"| **Recall relatif evalues (indicatif)** | **{re_e:.1%}** |",
          f"| **Recall relatif mentionnes (indicatif)** | **{re_m:.1%}** |", "",
          "> La distinction *evalue* (dans un tableau de resultats) vs *mentionne seulement* "
          "(cite en prose / related work) est precisement ce que l'ontologie rend explicite : "
          "un modele peut etre discute sans etre experimentalement evalue dans l'article. "
          "Le recall est lui aussi separe : evaluation ratee (modele d'un tableau non extrait) "
          "vs mention ratee (modele cite en prose non extrait)."]
    return "\n".join(L)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    arts = load_articles()
    vocab = build_global_vocab(arts)
    print(f"Vocab global KGE models = {len(vocab)}")
    rows = []
    TE = FE = TM = FM = SUS_E = SUS_M = 0
    for a in arts:
        ev, me, sus, counts = validate(a, vocab)
        report, (te, fe, tm, fm, nse, nsm, prec, r_e, r_m) = render_article(a, ev, me, sus, counts)
        open(os.path.join(OUT_DIR, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        rows.append((a["md_name"], te, fe, tm, fm, nse, nsm, prec, r_e, r_m))
        TE += te; FE += fe; TM += tm; FM += fm; SUS_E += nse; SUS_M += nsm
    open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(rows, TE, FE, TM, FM, SUS_E, SUS_M))
    TP, FP = TE + TM, FE + FM
    print(f"{len(arts)} rapports -> {OUT_DIR}/")
    print(f"Evalues={TE+FE} (prec {TE/(TE+FE):.1%})   Mentionnes={TM+FM} (prec {TM/(TM+FM):.1%})")
    print(f"Precision globale = {TP/(TP+FP):.1%}")
    print(f"Recall evalues = {TE/(TE+SUS_E):.1%} (manques={SUS_E})   "
          f"Recall mentionnes = {TM/(TM+SUS_M):.1%} (manques={SUS_M})")


if __name__ == "__main__":
    main()
