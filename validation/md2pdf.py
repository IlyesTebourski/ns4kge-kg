#!/usr/bin/env python3
"""Convertit un rapport Markdown en PDF (titres, paragraphes, gras, code,
listes, tableaux, blockquotes). Usage: python3 md2pdf.py <in.md> [out.pdf]"""
import sys, os, re
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, Preformatted, HRFlowable)

src = sys.argv[1] if len(sys.argv) > 1 else "RAPPORT_VALIDATION_COMPLET.md"
out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"

S = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=S["Heading1"], fontSize=17, spaceBefore=8, spaceAfter=8, textColor=colors.HexColor("#1a2b45"))
H2 = ParagraphStyle("H2", parent=S["Heading2"], fontSize=13, spaceBefore=12, spaceAfter=5, textColor=colors.HexColor("#22406a"))
H3 = ParagraphStyle("H3", parent=S["Heading3"], fontSize=11, spaceBefore=8, spaceAfter=3, textColor=colors.HexColor("#2c3e50"))
BODY = ParagraphStyle("BODY", parent=S["Normal"], fontSize=9.5, leading=13, spaceAfter=4, alignment=4)
LI = ParagraphStyle("LI", parent=BODY, leftIndent=12, spaceAfter=2)
QUOTE = ParagraphStyle("QUOTE", parent=BODY, leftIndent=10, textColor=colors.HexColor("#555"), fontSize=9)
CELL = ParagraphStyle("CELL", parent=S["Normal"], fontSize=8, leading=10)
CELLH = ParagraphStyle("CELLH", parent=CELL, textColor=colors.white, fontName="Helvetica-Bold")


def sanitize(t):
    for a, b in [("→", "->"), ("≠", "!="), ("≥", ">="), ("≤", "<="), ("×", "x"),
                 ("⭐", "*"), ("→", "->"), ("’", "'"), ("–", "-"), ("—", "-")]:
        t = t.replace(a, b)
    return t


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    t = sanitize(t)
    codes = []
    def stash(m):
        codes.append(m.group(1)); return f"\x00{len(codes)-1}\x00"
    t = re.sub(r"`(.+?)`", stash, t)          # protege le code d'abord
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(?!\s)([^*]+?)(?<!\s)\*", r"<i>\1</i>", t)   # italique sur
    t = re.sub(r"\x00(\d+)\x00",                                # ... du texte
               lambda m: f'<font face="Courier">{esc(codes[int(m.group(1))])}</font>', t)
    return t


def cell(t, hdr=False):
    return Paragraph(inline(t.strip()), CELLH if hdr else CELL)


story, lines, i = [], open(src, encoding="utf-8").read().splitlines(), 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith("```"):
        buf = []
        i += 1
        while i < len(lines) and not lines[i].startswith("```"):
            buf.append(sanitize(lines[i])); i += 1
        story.append(Preformatted("\n".join(buf), ParagraphStyle("code", parent=S["Code"], fontSize=8, leading=10, backColor=colors.HexColor("#f2f4f7"))))
        story.append(Spacer(1, 4))
    elif ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1]):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            if not re.match(r"^\|[\s:\-|]+\|$", lines[i]):
                rows.append([c for c in lines[i].strip().strip("|").split("|")])
            i += 1
        data = [[cell(c, hdr=(r == 0)) for c in row] for r, row in enumerate(rows)]
        t = Table(data, repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b0b8c0")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f2f5f8")]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        story.append(t); story.append(Spacer(1, 6)); continue
    elif ln.startswith("### "):
        story.append(Paragraph(inline(ln[4:]), H3))
    elif ln.startswith("## "):
        story.append(Paragraph(inline(ln[3:]), H2))
    elif ln.startswith("# "):
        story.append(Paragraph(inline(ln[2:]), H1))
    elif ln.strip() == "---":
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#ccc"), spaceBefore=4, spaceAfter=4))
    elif ln.startswith("> "):
        story.append(Paragraph(inline(ln[2:]), QUOTE))
    elif re.match(r"^\s*[-*] ", ln):
        story.append(Paragraph("• " + inline(re.sub(r"^\s*[-*] ", "", ln)), LI))
    elif ln.strip() == "":
        story.append(Spacer(1, 3))
    else:
        story.append(Paragraph(inline(ln), BODY))
    i += 1

SimpleDocTemplate(out, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                  topMargin=16 * mm, bottomMargin=16 * mm,
                  title=os.path.basename(out)).build(story)
print("PDF ecrit:", out)
