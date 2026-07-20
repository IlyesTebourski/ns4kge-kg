#!/usr/bin/env python3
"""
Rapport-preuve en PDF (paysage, tableau pagine), datasets OU metrics.
Usage : python3 generate_proof_pdf.py [datasets|metrics]   (defaut: datasets)
Sortie : validation/RAPPORT_PREUVE_<KIND>.pdf
"""
import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

HERE = os.path.dirname(os.path.abspath(__file__))

KIND = (sys.argv[1] if len(sys.argv) > 1 else "datasets").lower()
if KIND == "datasets":
    import validate_datasets as V
    ENT, ENTS = "dataset", "datasets"
    SOURCE = "Configurations[].Dataset"
    METHODO = ("insensible à la casse ; séparateurs -_/.@ tolérés ; frontières strictes "
               "(FB15k =/= FB15k-237, datasets distincts) ; recall cherché uniquement dans les "
               "blocs &lt;table&gt; ; tableaux classés stats vs résultats via leur caption.")
elif KIND == "metrics":
    import validate_metrics as V
    ENT, ENTS = "metric", "metrics"
    SOURCE = "Configurations[].Metric"
    METHODO = ("metrics normalisées par le prompt (Mean Rank-&gt;MR, Hit@10-&gt;Hits@10, "
               "Acc-&gt;Accuracy) donc matching par alias déterministes ; Hits@N / Hits@k "
               "générique accepté en précision ; recall dans les blocs &lt;table&gt; avec N littéral.")
else:
    sys.exit("kind inconnu (datasets|metrics)")

OUT = os.path.join(HERE, f"RAPPORT_PREUVE_{ENTS.upper()}.pdf")

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=15, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("BODY", parent=styles["Normal"], fontSize=8.5, leading=11)
CELL = ParagraphStyle("CELL", parent=styles["Normal"], fontSize=7, leading=8.5)
CELLC = ParagraphStyle("CELLC", parent=CELL, alignment=1)
MONO = ParagraphStyle("MONO", parent=styles["Normal"], fontName="Courier", fontSize=6.3, leading=7.5)


def clip(s, n=170):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n - 1] + "…"


def P(txt, style=CELL):
    return Paragraph((txt or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), style)


def PM(txt, style=CELL):
    return Paragraph(txt, style)


def styled(tbl_data, col_widths, header_bg=colors.HexColor("#2c3e50")):
    t = Table(tbl_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 7.5),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b0b8c0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f5f8")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


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
            (cand_stats if is_stats else cand_res).append((a["md_name"], lab, cap, clip(snip)))
        STATS += sum(1 for x in sus if x[2]); REAL += sum(1 for x in sus if not x[2])

    prec_micro = TP / (TP + FP) if (TP + FP) else 1.0
    rec_micro = TP / (TP + REAL) if (TP + REAL) else 1.0
    n_ok = sum(1 for r in rows if r[2])

    doc = SimpleDocTemplate(OUT, pagesize=landscape(A4),
                            leftMargin=12 * mm, rightMargin=12 * mm,
                            topMargin=12 * mm, bottomMargin=12 * mm,
                            title=f"Rapport-preuve {ENTS} NS4KGE")
    story = []
    story.append(Paragraph(f"Rapport-preuve — Validation des <i>{ENTS}</i> extraits (NS4KGE)", H1))
    story.append(Paragraph(
        f"Corpus : <b>{len(arts)} articles</b> — Source : {SOURCE} (prompt2) — "
        "Validation contre <font face='Courier'>load_md_tables_only()</font> (tables uniquement).", BODY))

    story.append(Paragraph("1. Définitions &amp; méthodologie", H2))
    defs = [[P("Terme", CELLC), P("Définition", CELL)],
            [P("TP", CELLC), P(f"{ENT} extrait par le KG ET présent dans les tableaux de l'article", CELL)],
            [P("FP", CELLC), P(f"{ENT} extrait par le KG mais absent des tableaux", CELL)],
            [P("Candidat FN", CELLC), P(f"{ENT} présent dans une cellule <table> mais non extrait", CELL)],
            [P("Précision", CELLC), P("TP / (TP + FP)", CELL)],
            [P("Recall relatif", CELLC), P("TP / (TP + candidats FN en table de résultats)", CELL)]]
    story.append(styled(defs, [35 * mm, 220 * mm]))
    story.append(Spacer(1, 3))
    story.append(PM(f"<b>Matching :</b> {METHODO}", BODY))

    story.append(Paragraph("2. Résultats globaux", H2))
    glob = [[P("Indicateur", CELLC), P("Valeur", CELLC)],
            [P(f"{ENTS.capitalize()} extraits (lignes vérifiées)", CELL), P(str(TP + FP), CELLC)],
            [P("Validés (TP)", CELL), P(str(TP), CELLC)],
            [P("Non validés (FP)", CELL), P(str(FP), CELLC)],
            [PM("<b>Précision (micro)</b>", CELL), PM(f"<b>{prec_micro:.1%}</b>", CELLC)],
            [P("Candidats FN en table de résultats", CELL), P(str(REAL), CELLC)],
            [P("Candidats FN en table de stats (ignorés par le prompt)", CELL), P(str(STATS), CELLC)],
            [PM("<b>Recall relatif (micro)</b>", CELL), PM(f"<b>{rec_micro:.1%}</b>", CELLC)],
            [P(f"Vocabulaire global de {ENTS}", CELL), P(str(len(vocab)), CELLC)]]
    story.append(styled(glob, [140 * mm, 40 * mm]))

    story.append(Paragraph("3. Analyse des erreurs", H2))
    story.append(PM("3.1 Faux positifs (extraits mais absents des tableaux)", BODY))
    fpt = [[P("Article", CELLC), P(f"{ENT.capitalize()} extrait", CELLC)]] + \
          [[P(m, CELL), P(l, CELL)] for m, l in fps]
    story.append(styled(fpt, [50 * mm, 80 * mm]))
    story.append(Spacer(1, 4))
    story.append(PM("3.2 Candidats faux négatifs — table de résultats", BODY))
    crt = [[P("Article", CELLC), P(ENT.capitalize(), CELLC), P("Table", CELLC), P("Citation", CELLC)]] + \
          [[P(m, CELL), P(l, CELL), P(clip(c, 40), CELL), P(clip(s, 90), MONO)] for m, l, c, s in cand_res]
    story.append(styled(crt, [35 * mm, 25 * mm, 55 * mm, 155 * mm]))
    story.append(Spacer(1, 4))
    story.append(PM("3.3 Candidats faux négatifs — table de statistiques (priorité basse)", BODY))
    cst = [[P("Article", CELLC), P(ENT.capitalize(), CELLC), P("Table", CELLC), P("Citation", CELLC)]] + \
          ([[P(m, CELL), P(l, CELL), P(clip(c, 40), CELL), P(clip(s, 90), MONO)] for m, l, c, s in cand_stats]
           or [[P("—", CELL), P("—", CELL), P("—", CELL), P("aucun", CELL)]])
    story.append(styled(cst, [35 * mm, 25 * mm, 55 * mm, 155 * mm]))

    story.append(Paragraph(
        f"4. Preuve détaillée — {len(rows)} {ENTS} extraits "
        f"({n_ok} validés / {len(rows) - n_ok} non)", H2))
    head = [P("#", CELLC), P("Article", CELLC), P(f"{ENT.capitalize()} extrait", CELLC),
            P("OK", CELLC), P("Table", CELLC), P("Citation dans le texte", CELLC)]
    data = [head]
    for i, (m, l, ok, cap, cite) in enumerate(rows, 1):
        data.append([P(str(i), CELLC), P(m, CELL), P(l, CELL),
                     PM("<b>oui</b>" if ok else "<b>non</b>", CELLC), P(clip(cap, 40), CELL), P(cite, MONO)])
    big = styled(data, [10 * mm, 34 * mm, 40 * mm, 9 * mm, 48 * mm, 132 * mm])
    st = [("TEXTCOLOR", (3, i), (3, i),
           colors.HexColor("#1a7f37") if rows[i - 1][2] else colors.HexColor("#c0392b"))
          for i in range(1, len(rows) + 1)]
    big.setStyle(TableStyle(st))
    story.append(big)

    doc.build(story)
    print(f"PDF ecrit : {OUT}  ({len(rows)} lignes de preuve)")


if __name__ == "__main__":
    main()
