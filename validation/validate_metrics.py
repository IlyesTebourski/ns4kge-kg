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
OUT_DIR = os.path.join(VD.HERE, "detailed_reports", "reports_metrics")

# --------------------------------------------------------------------------
# Alias deterministes par metric canonique
# --------------------------------------------------------------------------
LB = r"(?<![A-Za-z0-9])"           # frontiere gauche
RB = r"(?![A-Za-z0-9])"            # frontiere droite

# metrics "epelables" : canonique -> alias (coeur de regex, sans frontieres).
# Regle de casse homogene (VD.tok_regex) appliquee aux alias : les ACRONYMES
# (MR, MRR, AUC, MAP, AP...) exigent leur casse exacte en RECALL (sinon "map"/
# "ap"/"mr" en prose genereraient des candidats) ; les expansions en mots restent
# insensibles via (?i:...). En PRECISION le pattern est compile avec re.I, ce qui
# neutralise la distinction (leniente, comportement inchange).
ALIASES = {
    "MR":       r"MR|(?i:mean\s*rank)",
    "MRR":      r"MRR|(?i:mean\s*reciprocal\s*rank(?:ing)?)",
    "Accuracy": r"(?i:accuracy|acc)",
    "AUC":      r"AUC",
    "AUROC":    r"AUROC|AUC[-\s]?ROC|ROC[-\s]?AUC",
    "AUPRC":    r"AUPRC|AUPR|AUC[-\s]?PR|PR[-\s]?AUC",
    "F1":       r"F1(?:[-\s]?(?i:score))?|(?i:F[-\s]?measure|F[-\s]?score)",
    "MAP":      r"MAP|(?i:mean\s*average\s*precision)",
    "AP":       r"AP|(?i:average\s*precision)",
    "NDCG":     r"[nN]?DCG",
    "Spe":      r"(?i:Spe|specificity)",
}

# Placeholder generique d'en-tete groupe : "Hits@N" / "Hits@k" couvre les N reels.
PLACEHOLDER = r"[nk]\b"


def metric_pattern(canonical: str, allow_placeholder: bool = True,
                   mode: str = "precision"):
    """Renvoie une regex compilee pour une metric canonique.

    allow_placeholder : si True (precision), un en-tete generique "Hits@N"/"Hits@k"
    couvre le N reel. Si False (recall), on exige le N litteral, sinon on
    sur-genererait des candidats des qu'un placeholder apparait.
    mode : "precision" -> compile re.I (leniente, inchangee) ; "recall" -> regle
    de casse homogene : les acronymes/tokens stylises exigent leur casse exacte
    (les groupes (?i:...) des ALIASES gardent les mots insensibles).
    """
    c = canonical.strip()
    flags = re.I if mode == "precision" else 0
    ph = (r"|" + PLACEHOLDER) if allow_placeholder else ""
    # Hits@N (N quelconque) : tolere Hit/Hits/H, @ optionnel, espaces
    m = re.match(r"(?i)hits?@(\d+)$", c)
    if m:
        n = m.group(1)
        return re.compile(LB + r"(?i:hits?|h)\s*@?\s*(?:" + n + r"(?![0-9])" + ph + r")", flags)
    # NDCG@N
    m = re.match(r"(?i)ndcg@(\d+)$", c)
    if m:
        n = m.group(1)
        return re.compile(LB + r"[nN]?DCG\s*@?\s*(?:" + n + r"(?![0-9])" + ph + r")", flags)
    # metrics epelables
    if c in ALIASES:
        return re.compile(LB + r"(?:" + ALIASES[c] + r")" + RB, flags)
    # fallback : mot-entier verbatim (recall : casse homogene par token)
    if mode == "recall":
        toks = re.findall(r"[A-Za-z0-9]+", c)
        if not toks:
            return None
        core = r"[\s\-_/.@]*".join(VD.tok_regex(t, True) for t in toks)
        return re.compile(LB + core + RB)
    return re.compile(LB + re.escape(c) + RB, re.I)


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

# Verdicts de verification MANUELLE (remplis apres coup ; vides = baseline honnete).
PREC_VERDICTS = {}
# Adjudication manuelle recall (2026-07-22, justifications completes :
# recall_checks/metrics_recall_check.csv). "fp" = faux flag ecarte, "miss" = vrai oubli.
RECALL_VERDICTS = {
    ("batchns", "F1"): ("miss", "Micro-F1/Macro-F1 rapportees en resultats, non extraites."),
    ("dans", "NDCG"): ("fp", "Matche 'NDCG@5' deja extraite (plus specifique)."),
    ("etruncateduns", "F1"): ("miss", "'Prec./Rec./F1-score' table resultats EA, non extraite."),
    ("mcns", "NDCG"): ("miss", "'MovieLens NDCG / Amazon NDCG' resultats, non extraite."),
    ("reasonkge", "Hits@3"): ("miss", "Table 6 resultats LP avec Hits@3, non extraite."),
    ("selfadv", "AUPRC"): ("fp", "'Countries (AUC-PR)' couverte par l'extraction generique AUC."),
    ("selfadv", "AUROC"): ("miss", "'Countries (AUC-ROC)' = 2e metrique AUC distincte ; "
                                   "le label generique AUC ne couvre que AUC-PR."),
    ("tuckerdncaching", "Accuracy"): ("miss", "Accuracy de relation prediction rapportee "
                                              "(cf. FN Task), non extraite."),
}


def precision_pass(article):
    """Precision + collecte des metrics VERIFIEES CORRECTES (pour le vocab)."""
    slug, tt = article["slug"], article["tables_text"]
    prec_rows = []
    verified = set()
    tp = fp = 0
    for lab in sorted(article["metrics"]):
        pat = metric_pattern(lab)
        m = pat.search(tt)
        v = PREC_VERDICTS.get((slug, lab))
        ok = bool(m) if not v else (v[0] == "valid" or (bool(m) and v[0] != "error"))
        if m:
            cap, _ = VD.which_table(m.start(), tt, article["tables"])
            prec_rows.append((lab, True, cap, VD.snippet_around(tt, m)))
            tp += 1
        else:
            prec_rows.append((lab, False, "", ""))
            fp += 1
        if ok:
            verified.add(lab)
    return prec_rows, verified, tp, fp


def recall_pass(article, vocab):
    """Recall : metric du vocab VERIFIE (N litteral exige) dans une cellule de table
    mais non extraite."""
    suspects = []
    for lab in sorted(vocab):
        if lab in article["metrics"]:
            continue
        pat = metric_pattern(lab, allow_placeholder=False, mode="recall")  # N litteral + casse homogene
        for caption, table, is_stats in article["tables"]:
            m = pat.search(table)
            if m:
                suspects.append((lab, caption or "(sans caption)", is_stats,
                                 VD.snippet_around(table, m)))
                break
    return suspects


# --------------------------------------------------------------------------
# Rendu (identique aux datasets)
# --------------------------------------------------------------------------

def esc(s):
    return s.replace("|", "\\|")


def render_article(a, prec_rows, suspects, tp, fp):
    real = [s for s in suspects if not s[2]]
    stats = [s for s in suspects if s[2]]
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    # BRUT (script seul) vs ADJUGE (verdicts manuels : "fp" ecarte, sinon oubli)
    miss = [s for s in real
            if RECALL_VERDICTS.get((a["slug"], s[0]), ("", ""))[0] != "fp"]
    rec_brut = tp / (tp + len(real)) if (tp + len(real)) else 1.0
    rec = tp / (tp + len(miss)) if (tp + len(miss)) else 1.0
    L = [f"# Metrics — {a['md_name']}", "", f"**Titre :** {a['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Metrics extraites trouvees dans les tables (TP) | {tp} |",
         f"| Extraites NON trouvees (FP) | {fp} |",
         f"| **Precision** | **{prec:.0%}** |",
         f"| Candidats faux negatifs (table resultats) | {len(real)} |",
         f"| Candidats en table de stats (priorite basse) | {len(stats)} |",
         f"| Recall BRUT (avant adjudication) | {rec_brut:.0%} |",
         f"| **Recall relatif (adjuge)** | **{rec:.0%}** |", "",
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
    return "\n".join(L), (tp, fp, len(real), len(stats), prec, rec, len(miss))


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

    # Phase 1 : precision -> vocab bati sur les metrics verifiees correctes
    prec = {}
    vocab = set()
    for a in arts:
        prec_rows, verified, tp, fp = precision_pass(a)
        prec[a["slug"]] = (prec_rows, tp, fp)
        vocab |= verified
    print(f"Vocab global metrics (items verifies corrects) = {len(vocab)} : {sorted(vocab)}")

    # Phase 2 : recall contre le vocab verifie
    rows = []
    TP = FP = REAL = STATS = MISS = 0
    for a in arts:
        prec_rows, tp, fp = prec[a["slug"]]
        suspects = recall_pass(a, vocab)
        report, (tp, fp, real, stats, prec_, rec, miss) = render_article(a, prec_rows, suspects, tp, fp)
        open(os.path.join(OUT_DIR, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        rows.append((a["md_name"], tp, fp, real, stats, prec_, rec))
        TP += tp; FP += fp; REAL += real; STATS += stats; MISS += miss
    open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(rows, TP, FP, REAL, STATS))
    print(f"{len(arts)} rapports -> {OUT_DIR}/")
    print(f"Precision micro = {TP/(TP+FP):.1%}   (cand resultats={REAL}, stats={STATS})")
    print(f"Recall BRUT   = {TP/(TP+REAL) if (TP+REAL) else 1.0:.1%} (candidats bruts={REAL})")
    print(f"Recall ADJUGE = {TP/(TP+MISS) if (TP+MISS) else 1.0:.1%} "
          f"(vrais FN={MISS}, FP ecartes={REAL-MISS})")


if __name__ == "__main__":
    main()
