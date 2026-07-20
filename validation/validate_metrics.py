#!/usr/bin/env python3
"""
Validation des METRICS extraites par le KG — meme principe que les datasets.

Source : Configurations[].Metric (prompt2) -> uniquement les tableaux de
resultats. On valide donc contre `load_md_tables_only()` (repo).

Difference vs datasets : le prompt NORMALISE les metrics (ex. "Mean Rank" -> MR,
"Hit@10" -> Hits@10, "Acc" -> Accuracy). Le matching utilise donc une couche
d'ALIAS explicites et deterministes par metric canonique.

PRECISION : chaque metric extraite apparait-elle (via ses alias) dans les tables ?
RECALL    : quelles metrics du vocab global apparaissent dans une cellule <table>
            mais n'ont pas ete extraites ? (candidats faux negatifs), en
            distinguant table de resultats vs table de stats (via caption).

Sorties : validation/reports_metrics/<slug>.md + _SUMMARY.md
"""
import json
import glob
import os
import re

import validate_datasets as VD  # reutilise split_tables / which_table / snippet / io

MD_DIR = VD.MD_DIR
KG_DIR = VD.KG_DIR
OUT_DIR = os.path.join(VD.HERE, "reports_metrics")

# --------------------------------------------------------------------------
# Alias deterministes par metric canonique
# --------------------------------------------------------------------------
LB = r"(?<![A-Za-z0-9])"           # frontiere gauche
RB = r"(?![A-Za-z0-9])"            # frontiere droite

# metrics "epelables" : canonique -> alias (coeur de regex, sans frontieres)
ALIASES = {
    "MR":       r"MR|mean\s*rank",
    "MRR":      r"MRR|mean\s*reciprocal\s*rank(?:ing)?",
    "Accuracy": r"accuracy|acc",
    "AUC":      r"AUC",
    "AUROC":    r"AUROC|AUC[-\s]?ROC|ROC[-\s]?AUC",
    "AUPRC":    r"AUPRC|AUPR|AUC[-\s]?PR|PR[-\s]?AUC",
    "F1":       r"F1(?:[-\s]?score)?|F[-\s]?measure|F[-\s]?score",
    "MAP":      r"MAP|mean\s*average\s*precision",
    "AP":       r"AP|average\s*precision",
    "NDCG":     r"n?DCG",
    "Spe":      r"Spe|specificity",
}

# Placeholder generique d'en-tete groupe : "Hits@N" / "Hits@k" couvre les N reels.
PLACEHOLDER = r"[nk]\b"


def metric_pattern(canonical: str, allow_placeholder: bool = True):
    """Renvoie une regex compilee (case-insensitive) pour une metric canonique.

    allow_placeholder : si True (precision), un en-tete generique "Hits@N"/"Hits@k"
    couvre le N reel. Si False (recall), on exige le N litteral, sinon on
    sur-genererait des candidats des qu'un placeholder apparait.
    """
    c = canonical.strip()
    ph = (r"|" + PLACEHOLDER) if allow_placeholder else ""
    # Hits@N (N quelconque) : tolere Hit/Hits/H, @ optionnel, espaces
    m = re.match(r"(?i)hits?@(\d+)$", c)
    if m:
        n = m.group(1)
        return re.compile(LB + r"(?:hits?|h)\s*@?\s*(?:" + n + r"(?![0-9])" + ph + r")", re.I)
    # NDCG@N
    m = re.match(r"(?i)ndcg@(\d+)$", c)
    if m:
        n = m.group(1)
        return re.compile(LB + r"n?dcg\s*@?\s*(?:" + n + r"(?![0-9])" + ph + r")", re.I)
    # metrics epelables
    if c in ALIASES:
        return re.compile(LB + r"(?:" + ALIASES[c] + r")" + RB, re.I)
    # fallback : mot-entier verbatim
    core = re.escape(c)
    return re.compile(LB + core + RB, re.I)


# --------------------------------------------------------------------------
# Chargement / extraction
# --------------------------------------------------------------------------

def extracted_metrics(data: dict):
    out = {}
    exp = data.get("Experimentation", {}) or {}
    for c in exp.get("Configurations", []) or []:
        if isinstance(c, dict):
            v = (c.get("Metric") or "").strip()
            if v:
                out.setdefault(v, v)   # cle = valeur canonique elle-meme
    return out


def load_articles():
    from no_facts_pipeline.core import load_md_tables_only
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            continue
        data = json.load(open(p, encoding="utf-8"))
        tables_text = load_md_tables_only(md)
        arts.append({
            "slug": slug,
            "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "tables_text": tables_text,
            "tables": VD.split_tables(tables_text),
            "metrics": extracted_metrics(data),
        })
    return arts


def build_global_vocab(arts):
    vocab = {}
    for a in arts:
        for k in a["metrics"]:
            vocab.setdefault(k, k)
    return vocab


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def validate(article, vocab):
    tt = article["tables_text"]
    prec_rows = []
    tp = fp = 0
    for lab in sorted(article["metrics"]):
        pat = metric_pattern(lab)
        m = pat.search(tt)
        if m:
            cap, _ = VD.which_table(m.start(), tt, article["tables"])
            prec_rows.append((lab, True, cap, VD.snippet_around(tt, m)))
            tp += 1
        else:
            prec_rows.append((lab, False, "", ""))
            fp += 1

    suspects = []
    for lab in sorted(vocab):
        if lab in article["metrics"]:
            continue
        pat = metric_pattern(lab, allow_placeholder=False)  # recall : N litteral exige
        for caption, table, is_stats in article["tables"]:
            m = pat.search(table)
            if m:
                suspects.append((lab, caption or "(sans caption)", is_stats,
                                 VD.snippet_around(table, m)))
                break
    return prec_rows, suspects, tp, fp


# --------------------------------------------------------------------------
# Rendu (identique aux datasets)
# --------------------------------------------------------------------------

def esc(s):
    return s.replace("|", "\\|")


def render_article(a, prec_rows, suspects, tp, fp):
    real = [s for s in suspects if not s[2]]
    stats = [s for s in suspects if s[2]]
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    rec = tp / (tp + len(real)) if (tp + len(real)) else 1.0
    L = [f"# Metrics — {a['md_name']}", "", f"**Titre :** {a['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Metrics extraites trouvees dans les tables (TP) | {tp} |",
         f"| Extraites NON trouvees (FP) | {fp} |",
         f"| **Precision** | **{prec:.0%}** |",
         f"| Candidats faux negatifs (table resultats) | {len(real)} |",
         f"| Candidats en table de stats (priorite basse) | {len(stats)} |",
         f"| **Recall relatif (indicatif)** | **{rec:.0%}** |", "",
         "## Precision — metrics extraites par le KG", "",
         "| Metric extraite | Dans les tables ? | Table | Extrait |", "|---|:---:|---|---|"]
    for lab, found, cap, snip in prec_rows:
        mark = "✅ oui" if found else "❌ NON"
        L.append(f"| {esc(lab)} | {mark} | {esc(cap)} | {esc(snip) if found else '_(absent)_'} |")
    L += ["", "## Recall — metrics dans les tables mais NON extraites", ""]
    if real:
        L += ["| Metric | Table | Extrait |", "|---|---|---|"]
        L += [f"| {esc(l)} | {esc(c)} | {esc(s)} |" for l, c, _, s in real]
    else:
        L.append("_Aucun candidat en table de resultats._")
    if stats:
        L += ["", "### Table de stats seulement", "", "| Metric | Table | Extrait |", "|---|---|---|"]
        L += [f"| {esc(l)} | {esc(c)} | {esc(s)} |" for l, c, _, s in stats]
    return "\n".join(L), (tp, fp, len(real), len(stats), prec, rec)


def render_summary(rows, TP, FP, REAL, STATS):
    mp = TP / (TP + FP) if (TP + FP) else 1.0
    mr = TP / (TP + REAL) if (TP + REAL) else 1.0
    Mp = sum(r[5] for r in rows) / len(rows)
    Mr = sum(r[6] for r in rows) / len(rows)
    L = ["# Recap validation METRICS (base sur les tables_only)", "",
         f"Articles : **{len(rows)}**", "",
         "| Article | TP | FP | Precision | Cand. resultats | Cand. stats | Recall~ |",
         "|---|---:|---:|:---:|---:|---:|:---:|"]
    for name, tp, fp, real, stats, prec, rec in rows:
        L.append(f"| {name} | {tp} | {fp} | {prec:.0%} | {real} | {stats} | {rec:.0%} |")
    L += ["", "## Totaux", "", "| Metrique | Valeur |", "|---|---|",
          f"| Total TP | {TP} |", f"| Total FP | {FP} |",
          f"| Total candidats (resultats) | {REAL} |",
          f"| Total candidats (stats) | {STATS} |",
          f"| **Precision micro** | **{mp:.1%}** |",
          f"| **Precision macro** | **{Mp:.1%}** |",
          f"| **Recall relatif micro (indicatif)** | **{mr:.1%}** |",
          f"| **Recall relatif macro (indicatif)** | **{Mr:.1%}** |"]
    return "\n".join(L)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    arts = load_articles()
    vocab = build_global_vocab(arts)
    print(f"Vocab global metrics = {len(vocab)} : {sorted(vocab)}")
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
    print(f"Precision micro = {TP/(TP+FP):.1%}   Recall relatif micro = {TP/(TP+REAL):.1%}   "
          f"(cand resultats={REAL}, stats={STATS})")


if __name__ == "__main__":
    main()
