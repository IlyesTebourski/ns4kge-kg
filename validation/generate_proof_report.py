#!/usr/bin/env python3
"""
Genere un RAPPORT PREUVE factuel (datasets OU metrics), sans prose.
- definitions + methodo (minimal)
- resultats globaux
- analyse des erreurs (FP + candidats FN)
- LE gros tableau : 1 ligne par (article, entite extraite), validation + citation.

Usage : python3 generate_proof_report.py [datasets|metrics]   (defaut: datasets)
Sortie : validation/RAPPORT_PREUVE_<KIND>.md
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

KIND = (sys.argv[1] if len(sys.argv) > 1 else "datasets").lower()
if KIND == "datasets":
    import validate_datasets as V
    ENT, ENTS = "dataset", "datasets"
    SOURCE = "`Configurations[].Dataset`"
    METHODO = ("insensible à la casse ; séparateurs `-_/.@` tolérés ; frontières strictes "
               "(`FB15k` ≠ `FB15k-237`) ; recall cherché uniquement dans les blocs `<table>` ; "
               "tableaux classés *stats* vs *résultats* via leur caption.")
elif KIND == "metrics":
    import validate_metrics as V
    ENT, ENTS = "metric", "metrics"
    SOURCE = "`Configurations[].Metric`"
    METHODO = ("metrics normalisées par le prompt (ex. `Mean Rank`→`MR`, `Hit@10`→`Hits@10`, "
               "`Acc`→`Accuracy`) donc matching par **alias déterministes** ; `Hits@N`/`Hits@k` "
               "générique accepté en précision ; recall cherché dans les blocs `<table>` avec N littéral.")
else:
    sys.exit("kind inconnu (datasets|metrics)")

OUT = os.path.join(HERE, "detailed_reports", f"RAPPORT_PREUVE_{ENTS.upper()}.md")


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def clip(s, n=140):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n - 1] + "…"


def main():
    arts = V.load_articles()
    vocab = V.build_global_vocab(arts)

    rows, fps, cand_res, cand_stats = [], [], [], []
    TP = FP = REAL = STATS = 0
    for a in arts:
        prec, sus, tp, fp = V.validate(a, vocab)
        TP += tp; FP += fp
        for lab, found, cap, snip in prec:
            rows.append((a["md_name"], lab, found, cap or "—", clip(snip) if found else "—"))
            if not found:
                fps.append((a["md_name"], lab))
        for lab, cap, is_stats, snip in sus:
            if is_stats:
                STATS += 1; cand_stats.append((a["md_name"], lab, cap, clip(snip)))
            else:
                REAL += 1; cand_res.append((a["md_name"], lab, cap, clip(snip)))

    prec_micro = TP / (TP + FP) if (TP + FP) else 1.0
    rec_micro = TP / (TP + REAL) if (TP + REAL) else 1.0
    n_ok = sum(1 for r in rows if r[2])

    L = []
    L += [f"# Rapport-preuve — Validation des *{ENTS}* extraits (NS4KGE)", "",
          f"Corpus : **{len(arts)} articles** — Source : {SOURCE} (prompt2) — "
          "Validation contre `load_md_tables_only()` (tables uniquement).", ""]

    L += ["## 1. Définitions", "", "| Terme | Définition |", "|---|---|",
          f"| TP | {ENT} extrait par le KG ET présent dans les tableaux de l'article |",
          f"| FP | {ENT} extrait par le KG mais absent des tableaux |",
          f"| Candidat FN | {ENT} présent dans une cellule `<table>` mais non extrait |",
          "| Précision | TP / (TP + FP) |",
          "| Recall relatif | TP / (TP + candidats FN en table de résultats) |", "",
          f"**Méthodo (matching) :** {METHODO}", ""]

    L += ["## 2. Résultats globaux", "", "| Indicateur | Valeur |", "|---|---|",
          f"| {ENTS.capitalize()} extraits (lignes vérifiées) | {TP + FP} |",
          f"| Validés (TP) | {TP} |",
          f"| Non validés (FP) | {FP} |",
          f"| **Précision (micro)** | **{prec_micro:.1%}** |",
          f"| Candidats FN en table de résultats | {REAL} |",
          f"| Candidats FN en table de stats (ignorés par le prompt) | {STATS} |",
          f"| **Recall relatif (micro)** | **{rec_micro:.1%}** |",
          f"| Vocabulaire global de {ENTS} | {len(vocab)} |", ""]

    L += ["## 3. Analyse des erreurs", "",
          "### 3.1 Faux positifs (extraits mais absents des tableaux)", "",
          f"| Article | {ENT.capitalize()} extrait |", "|---|---|"]
    L += [f"| {esc(m)} | {esc(l)} |" for m, l in fps]
    L += ["", "### 3.2 Candidats faux négatifs — table de résultats", "",
          f"| Article | {ENT.capitalize()} | Table | Citation |", "|---|---|---|---|"]
    L += [f"| {esc(m)} | {esc(l)} | {esc(clip(c, 40))} | {esc(s)} |" for m, l, c, s in cand_res]
    L += ["", "### 3.3 Candidats faux négatifs — table de statistiques (priorité basse)", "",
          f"| Article | {ENT.capitalize()} | Table | Citation |", "|---|---|---|---|"]
    L += [f"| {esc(m)} | {esc(l)} | {esc(clip(c, 40))} | {esc(s)} |" for m, l, c, s in cand_stats]
    L += [""]

    L += [f"## 4. Preuve détaillée — {len(rows)} {ENTS} extraits ({n_ok} validés / "
          f"{len(rows) - n_ok} non)", "",
          f"| # | Article | {ENT.capitalize()} extrait | Validé | Table | Citation dans le texte |",
          "|---:|---|---|:---:|---|---|"]
    for i, (m, l, ok, cap, cite) in enumerate(rows, 1):
        mark = "✅" if ok else "❌"
        L.append(f"| {i} | {esc(m)} | {esc(l)} | {mark} | {esc(clip(cap, 40))} | {esc(cite)} |")
    L += [""]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Ecrit : {OUT}")
    print(f"{len(rows)} lignes de preuve ({n_ok} validees, {len(rows)-n_ok} non).")


if __name__ == "__main__":
    main()
