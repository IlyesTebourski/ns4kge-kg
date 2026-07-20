#!/usr/bin/env python3
"""
Validation des DATASETS extraits par le KG — version fidele au pipeline.

Point cle : dans le pipeline, les datasets ne sont extraits QUE des tableaux de
resultats (prompt2), dont l'unique entree est le sidecar produit par
`load_md_tables_only()` (les blocs <table> + leur caption). Le texte en prose
(prompt1) n'extrait aucun dataset.

=> On valide donc les datasets contre le `tables_only` de CHAQUE article, en
   reutilisant la fonction du repo (aucune divergence avec le pipeline).

PRECISION : chaque dataset extrait apparait-il dans les tableaux ?
RECALL    : quels datasets du vocabulaire global apparaissent dans les tableaux
            de l'article mais n'ont PAS ete extraits ? (candidats faux negatifs)
            On tague si le candidat est dans une table de RESULTATS (vrai
            candidat) ou seulement dans une table de STATS/ablation (que le
            prompt demande d'ignorer -> priorite basse).

Sorties : validation/reports_datasets/<slug>.md  + _SUMMARY.md
"""

import json
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_root(start):
    """Cherche en remontant le dossier contenant liste_mds + ns4kge-kg +
    ns4kge-extraction-pipeline. Rend le validateur robuste ou qu'il soit place
    (racine POSTER, ou deplace dans un des repos git)."""
    need = ("liste_mds", "ns4kge-kg", "ns4kge-extraction-pipeline")
    for cand in [start] + [os.path.abspath(os.path.join(start, *([".."] * n))) for n in range(1, 7)]:
        if all(os.path.isdir(os.path.join(cand, x)) for x in need):
            return cand
    return os.path.dirname(start)   # fallback


ROOT = _find_root(HERE)
MD_DIR = os.path.join(ROOT, "liste_mds")
KG_DIR = os.path.join(ROOT, "ns4kge-kg", "per_article")
PIPE_SRC = os.path.join(ROOT, "ns4kge-extraction-pipeline", "src")
OUT_DIR = os.path.join(HERE, "reports_datasets")

# On importe la fonction officielle du pipeline (fidelite garantie).
sys.path.insert(0, PIPE_SRC)
from no_facts_pipeline.core import load_md_tables_only  # noqa: E402

# Caption d'une table a ignorer selon le prompt (stats / ablation).
STATS_CAPTION = re.compile(r"(statistic|ablation|hyper.?parameter|dataset detail)", re.I)
# Meme regex de decoupage caption/table que core/loaders.py
TABLE_SPLIT = re.compile(r"(Table\s+\d+[^\n]*)?\s*(<table>[\s\S]*?</table>)\s*(Table\s+\d+[^\n]*)?")


# --------------------------------------------------------------------------
# Normalisation & matching (verbatim, mot-entier — datasets = noms canoniques)
# --------------------------------------------------------------------------

def tokens_of(entity: str):
    return re.findall(r"[a-z0-9]+", entity.lower())


def norm_key(entity: str) -> str:
    return "".join(tokens_of(entity))


# Frontiere : un nom de dataset ne doit pas etre un simple prefixe d'un code plus
# grand. On exclut donc aussi - _ / des frontieres, sinon "FB15k" matcherait
# l'interieur de "FB15k-237" (datasets DIFFERENTS).
BOUND = r"[A-Za-z0-9\-_/]"


def build_pattern(entity: str):
    toks = tokens_of(entity)
    if not toks:
        return None
    sep = r"[\s\-_/.@]*"
    core = sep.join(re.escape(t) for t in toks)
    return re.compile(r"(?<!" + BOUND + r")" + core + r"(?!" + BOUND + r")",
                      re.IGNORECASE)


def find_first(entity: str, text: str):
    pat = build_pattern(entity)
    if pat is None:
        return None
    return pat.search(text)


def snippet_around(text: str, m) -> str:
    s = max(0, m.start() - 40)
    e = min(len(text), m.end() + 40)
    return re.sub(r"\s+", " ", text[s:e].replace("\n", " ")).strip()


# --------------------------------------------------------------------------
# Chargement
# --------------------------------------------------------------------------

def split_tables(tables_text: str):
    """Renvoie [(caption, table_html, is_stats)] a partir du sidecar tables_only."""
    out = []
    for cap_b, table, cap_a in TABLE_SPLIT.findall(tables_text):
        caption = (cap_b or cap_a or "").strip()
        out.append((caption, table, bool(STATS_CAPTION.search(caption))))
    return out


def extracted_datasets(data: dict):
    """{norm_key: label} des datasets extraits (Configurations[].Dataset)."""
    out = {}
    exp = data.get("Experimentation", {}) or {}
    for c in exp.get("Configurations", []) or []:
        if isinstance(c, dict):
            v = (c.get("Dataset") or "").strip()
            if v:
                out.setdefault(norm_key(v), v)
    return out


def load_articles():
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            print(f"[WARN] pas de .md pour {slug}")
            continue
        data = json.load(open(p, encoding="utf-8"))
        tables_text = load_md_tables_only(md)
        arts.append({
            "slug": slug,
            "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "tables_text": tables_text,
            "tables": split_tables(tables_text),
            "datasets": extracted_datasets(data),
        })
    return arts


def build_global_vocab(arts):
    vocab = {}
    for a in arts:
        for k, lab in a["datasets"].items():
            vocab.setdefault(k, lab)
    return vocab


# --------------------------------------------------------------------------
# Validation d'un article
# --------------------------------------------------------------------------

def which_table(m_start, tables_text, tables):
    """Retrouve la caption/type de la table contenant l'offset m_start."""
    # positions des tables dans tables_text
    idx = 0
    for caption, table, is_stats in tables:
        pos = tables_text.find(table, idx)
        if pos == -1:
            continue
        idx = pos
        if pos <= m_start < pos + len(table):
            return caption or "(sans caption)", is_stats
    return "(hors table)", False


def validate(article, vocab):
    tt = article["tables_text"]
    prec_rows = []      # (label, found, caption, snippet)
    tp = fp = 0
    for k, lab in sorted(article["datasets"].items(), key=lambda kv: kv[1].lower()):
        m = find_first(lab, tt)
        if m:
            cap, _ = which_table(m.start(), tt, article["tables"])
            prec_rows.append((lab, True, cap, snippet_around(tt, m)))
            tp += 1
        else:
            prec_rows.append((lab, False, "", ""))
            fp += 1

    # Recall : datasets du vocab global presents dans une CELLULE de tableau
    # (bloc <table>) mais non extraits. On ignore les captions/prose : un
    # dataset doit apparaitre dans une ligne de tableau pour etre une config.
    suspects = []       # (label, caption, is_stats, snippet)
    for k, lab in sorted(vocab.items(), key=lambda kv: kv[1].lower()):
        if k in article["datasets"]:
            continue
        pat = build_pattern(lab)
        if pat is None:
            continue
        for caption, table, is_stats in article["tables"]:
            m = pat.search(table)
            if m:
                suspects.append((lab, caption or "(sans caption)", is_stats,
                                 snippet_around(table, m)))
                break
    return prec_rows, suspects, tp, fp


# --------------------------------------------------------------------------
# Rendu
# --------------------------------------------------------------------------

def esc(s):
    return s.replace("|", "\\|")


def render_article(article, prec_rows, suspects, tp, fp):
    real_sus = [s for s in suspects if not s[2]]        # dans table de resultats
    stats_sus = [s for s in suspects if s[2]]           # seulement dans table de stats
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    rec = tp / (tp + len(real_sus)) if (tp + len(real_sus)) else 1.0

    L = [f"# Datasets — {article['md_name']}", "",
         f"**Titre :** {article['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Datasets extraits trouves dans les tables (TP) | {tp} |",
         f"| Extraits NON trouves (FP -> erreur precision) | {fp} |",
         f"| **Precision** | **{prec:.0%}** |",
         f"| Candidats faux negatifs (table de resultats) | {len(real_sus)} |",
         f"| Candidats en table de stats seulement (priorite basse) | {len(stats_sus)} |",
         f"| **Recall relatif (indicatif)** | **{rec:.0%}** |", ""]

    L += ["## Precision — datasets extraits par le KG", "",
          "| Dataset extrait | Dans les tables ? | Table | Extrait |",
          "|---|:---:|---|---|"]
    for lab, found, cap, snip in prec_rows:
        mark = "✅ oui" if found else "❌ NON"
        L.append(f"| {esc(lab)} | {mark} | {esc(cap)} | {esc(snip) if found else '_(absent des tables)_'} |")
    L.append("")

    L += ["## Recall — datasets dans les tables mais NON extraits", ""]
    if real_sus:
        L += ["### ⚠️ Candidats en table de resultats (a revoir en priorite)", "",
              "| Dataset | Table | Extrait |", "|---|---|---|"]
        for lab, cap, _, snip in real_sus:
            L.append(f"| {esc(lab)} | {esc(cap)} | {esc(snip)} |")
        L.append("")
    else:
        L += ["_Aucun candidat en table de resultats._", ""]
    if stats_sus:
        L += ["### Candidats en table de STATS seulement (le prompt les ignore)", "",
              "| Dataset | Table | Extrait |", "|---|---|---|"]
        for lab, cap, _, snip in stats_sus:
            L.append(f"| {esc(lab)} | {esc(cap)} | {esc(snip)} |")
        L.append("")
    return "\n".join(L), (tp, fp, len(real_sus), len(stats_sus), prec, rec)


def render_summary(rows, TP, FP, REAL, STATS):
    micro_p = TP / (TP + FP) if (TP + FP) else 1.0
    micro_r = TP / (TP + REAL) if (TP + REAL) else 1.0
    macro_p = sum(r[5] for r in rows) / len(rows)
    macro_r = sum(r[6] for r in rows) / len(rows)
    L = ["# Recap validation DATASETS (base sur les tables_only)", "",
         f"Articles : **{len(rows)}**", "",
         "| Article | TP | FP | Precision | Cand. resultats | Cand. stats | Recall~ |",
         "|---|---:|---:|:---:|---:|---:|:---:|"]
    for name, tp, fp, real, stats, prec, rec in rows:
        L.append(f"| {name} | {tp} | {fp} | {prec:.0%} | {real} | {stats} | {rec:.0%} |")
    L += ["", "## Totaux", "", "| Metrique | Valeur |", "|---|---|",
          f"| Total TP | {TP} |",
          f"| Total FP (extraits absents des tables) | {FP} |",
          f"| Total candidats faux negatifs (tables resultats) | {REAL} |",
          f"| Total candidats en tables stats seulement | {STATS} |",
          f"| **Precision micro** | **{micro_p:.1%}** |",
          f"| **Precision macro** | **{macro_p:.1%}** |",
          f"| **Recall relatif micro (indicatif)** | **{micro_r:.1%}** |",
          f"| **Recall relatif macro (indicatif)** | **{macro_r:.1%}** |", "",
          "> Recall **indicatif** : les candidats 'table de resultats' sont des "
          "datasets presents dans un tableau de resultats mais non extraits — a "
          "verifier a la main. Les candidats 'table de stats' sont volontairement "
          "ignores par le prompt (tables de statistiques/ablation)."]
    return "\n".join(L)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    arts = load_articles()
    vocab = build_global_vocab(arts)
    print(f"Vocab global datasets = {len(vocab)}")

    rows = []
    TP = FP = REAL = STATS = 0
    for a in arts:
        prec_rows, suspects, tp, fp = validate(a, vocab)
        report, (tp, fp, real, stats, prec, rec) = render_article(a, prec_rows, suspects, tp, fp)
        open(os.path.join(OUT_DIR, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        rows.append((a["md_name"], tp, fp, real, stats, prec, rec))
        TP += tp; FP += fp; REAL += real; STATS += stats

    open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(rows, TP, FP, REAL, STATS))
    print(f"{len(arts)} rapports -> {OUT_DIR}/")
    print(f"Precision micro = {TP/(TP+FP):.1%}   "
          f"Recall relatif micro = {TP/(TP+REAL):.1%}   "
          f"(candidats resultats={REAL}, stats={STATS})")


if __name__ == "__main__":
    main()
