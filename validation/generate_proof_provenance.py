#!/usr/bin/env python3
"""Rapport-preuve pour KGE models / NS methods (structure evalue/mentionne).
Usage: python3 generate_proof_provenance.py [kgemodels|nsmethods]
Sortie: RAPPORT_PREUVE_<KIND>.md  (a convertir en PDF via md2pdf.py)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
KIND = (sys.argv[1] if len(sys.argv) > 1 else "kgemodels").lower()
if KIND == "kgemodels":
    import validate_kgemodels as V
    TITLE = "KGE Models"
elif KIND == "nsmethods":
    import validate_nsmethods as V
    TITLE = "NS Methods"
else:
    sys.exit("kind: kgemodels|nsmethods")
OUT = os.path.join(HERE, f"RAPPORT_PREUVE_{KIND.upper()}.md")


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def clip(s, n=120):
    s = " ".join(str(s).split()); return s if len(s) <= n else s[:n-1] + "…"


def get(row, idx, default=""):
    return row[idx] if len(row) > idx else default


def main():
    arts = V.load_articles(); vocab = V.build_global_vocab(arts)
    TE = FE = TM = FM = 0
    ev_rows, me_rows, c1, c2 = [], [], [], []
    for a in arts:
        evaluated, mentioned, suspects, counts = V.validate(a, vocab)
        te, fe, tm, fm = counts; TE += te; FE += fe; TM += tm; FM += fm
        for r in evaluated:
            label, ok = r[0], r[1]; snip = r[-1]
            ev_rows.append((a["md_name"], label, ok, clip(snip) if ok else "—"))
        for r in mentioned:
            label, ok = r[0], r[1]; snip = r[-1]
            me_rows.append((a["md_name"], label, ok, clip(snip) if ok else "—"))
        me_, mm_ = V.split_suspects(suspects)
        for r in me_:
            c1.append((a["md_name"], r[0], get(r, 1), clip(r[-1])))
        for r in mm_:
            c2.append((a["md_name"], r[0], get(r, 1), clip(r[-1])))

    pe = TE/(TE+FE) if TE+FE else 1.0
    pm = TM/(TM+FM) if TM+FM else 1.0
    re_e = TE/(TE+len(c1)) if TE+len(c1) else 1.0
    re_m = TM/(TM+len(c2)) if TM+len(c2) else 1.0

    L = [f"# Rapport-preuve — {TITLE} (provenance : évalué vs mentionné)", "",
         f"Corpus : **{len(arts)} articles**. Évalués validés vs `tables_only`, "
         "mentionnés vs `no_tables` (prose). Matching déterministe.", "",
         "## Scores", "", "| Score | Valeur |", "|---|---|",
         f"| Précision évalués | **{pe:.1%}** |",
         f"| Précision mentionnés | **{pm:.1%}** |",
         f"| Recall évalués (indicatif) | **{re_e:.1%}** |",
         f"| Recall mentionnés (indicatif) | **{re_m:.1%}** |",
         f"| Évalués vérifiés / mentionnés vérifiés | {TE+FE} / {TM+FM} |", ""]

    L += [f"## A. Preuve — modèles/méthodes ÉVALUÉS ({len(ev_rows)})", "",
          "| Article | Entité | Trouvé | Extrait (tableau) |", "|---|---|:---:|---|"]
    for m, l, ok, s in ev_rows:
        L.append(f"| {esc(m)} | {esc(l)} | {'oui' if ok else '**NON**'} | {esc(s)} |")

    L += ["", f"## B. Preuve — MENTIONNÉS seulement ({len(me_rows)})", "",
          "| Article | Entité | Trouvé | Extrait (prose) |", "|---|---|:---:|---|"]
    for m, l, ok, s in me_rows:
        L.append(f"| {esc(m)} | {esc(l)} | {'oui' if ok else '**NON**'} | {esc(s)} |")

    L += ["", f"## C1. Candidats faux négatifs — ÉVALUÉS ({len(c1)})", "",
          "| Article | Entité | Où | Extrait |", "|---|---|:---:|---|"]
    for m, l, w, s in c1:
        L.append(f"| {esc(m)} | {esc(l)} | {esc(w)} | {esc(s)} |")

    L += ["", f"## C2. Candidats faux négatifs — MENTIONNÉS ({len(c2)})", "",
          "| Article | Entité | Où | Extrait |", "|---|---|:---:|---|"]
    for m, l, w, s in c2:
        L.append(f"| {esc(m)} | {esc(l)} | {esc(w)} | {esc(s)} |")

    open(OUT, "w", encoding="utf-8").write("\n".join(L))
    print("Ecrit:", OUT, "| A=%d B=%d C1=%d C2=%d" % (len(ev_rows), len(me_rows), len(c1), len(c2)))


if __name__ == "__main__":
    main()
