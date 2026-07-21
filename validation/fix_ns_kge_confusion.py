#!/usr/bin/env python3
"""Post-traitement : corriger la confusion methode-NS / modele-KGE dans les JSON.

Le LLM tague parfois une METHODE de negative sampling comme si c'etait un modele
KGE. Ce sont des erreurs de categorie (une methode NS n'est pas un modele KGE).
Ce script sort ces noms des champs KGE (`proposedKGEModel`, `mentionedKGEModels`,
`Configurations[].KGEModel`) et les remet cote NS. Idempotent : on peut le
relancer, il ne change que ce qui n'est pas deja corrige.

Registre explicite et revu a la main (chaque entree est une methode NS attestee,
avec sa fiche dans liste_mds/). On NE reclasse PAS automatiquement les cas
ambigus (HaSa, RUGA, RAA-KGC, GraphGAN... qui sont aussi evalues comme modeles) :
ils sont juste signales en fin de run pour revue humaine.

Usage :
    python3 fix_ns_kge_confusion.py           # applique + affiche le journal
    python3 fix_ns_kge_confusion.py --check    # verifie seulement (exit!=0 si sale)
"""
import argparse
import glob
import json
import os
import sys

import validate_datasets as VD

# Methodes NS que le LLM a mal classees en KGE. Cle = nom, valeur = justification.
NS_NOT_KGE = {
    "KBGAN":     "GAN-based negative sampling (Cai & Wang 2018) — liste_mds/KBGAN.md",
    "CAKE":      "Commonsense-Aware NS framework (Niu et al. 2022) — liste_mds/CAKE.md",
    "ReasonKGE": "Ontology-reasoning negative sampling (Jain et al.) — liste_mds/ReasonKGE.md",
}
_NK = {VD.norm_key(k): k for k in NS_NOT_KGE}


def fix_file(path, check=False):
    d = json.load(open(path, encoding="utf-8"))
    changes = []

    # 1) proposedKGEModel : blanchir si c'est une methode NS
    if VD.norm_key(d.get("proposedKGEModel", "")) in _NK:
        changes.append(f"proposedKGEModel={d['proposedKGEModel']} -> ''")
        if not check:
            d["proposedKGEModel"] = ""

    # 2) mentionedKGEModels : retirer, garantir cote mentionedNSMethods
    mk = d.get("mentionedKGEModels") or []
    keep = [m for m in mk if VD.norm_key(m) not in _NK]
    for m in mk:
        if VD.norm_key(m) in _NK:
            changes.append(f"mentionedKGEModel={m} -> NS")
            ns = d.setdefault("mentionedNSMethods", [])
            if m not in ns and not check:
                ns.append(m)
    if not check:
        d["mentionedKGEModels"] = keep

    # 3) Configurations[].KGEModel : reclasser en NSMethod, vider KGEModel
    for c in (d.get("Experimentation", {}) or {}).get("Configurations", []) or []:
        if isinstance(c, dict) and VD.norm_key(c.get("KGEModel", "")) in _NK:
            name = c["KGEModel"]
            changes.append(f"Config.KGEModel={name} -> NSMethod")
            if not check:
                c["NSMethod"] = name
                c["KGEModel"] = ""

    if changes and not check:
        json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return changes


def report_candidates():
    """Signale (sans corriger) les noms presents a la fois en champ KGE et NS :
    incoherences a revoir manuellement avant d'etendre le registre."""
    kge, ns = {}, {}
    for p in glob.glob(os.path.join(VD.KG_DIR, "*_merged.json")):
        d = json.load(open(p, encoding="utf-8"))
        for m in ([d.get("proposedKGEModel")] + (d.get("mentionedKGEModels") or [])):
            if m and str(m).strip():
                kge.setdefault(VD.norm_key(m), str(m))
        for c in (d.get("Experimentation", {}) or {}).get("Configurations", []) or []:
            if isinstance(c, dict):
                if c.get("KGEModel"):
                    kge.setdefault(VD.norm_key(c["KGEModel"]), str(c["KGEModel"]))
                if c.get("NSMethod"):
                    ns.setdefault(VD.norm_key(c["NSMethod"]), str(c["NSMethod"]))
        for m in [d.get("proposedNSMethod")] + (d.get("mentionedNSMethods") or []):
            if m and str(m).strip():
                ns.setdefault(VD.norm_key(m), str(m))
    amb = sorted((kge[k] for k in (set(kge) & set(ns)) if k not in _NK), key=str.lower)
    return amb


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verifie sans modifier")
    args = ap.parse_args()

    total = 0
    for p in sorted(glob.glob(os.path.join(VD.KG_DIR, "*_merged.json"))):
        ch = fix_file(p, check=args.check)
        if ch:
            total += len(ch)
            print(f"{os.path.basename(p)}:")
            for c in ch:
                print(f"    {c}")

    if args.check:
        if total:
            print(f"\n[CHECK] {total} champ(s) KGE encore pollue(s) par une methode NS.")
            sys.exit(1)
        print("[CHECK] OK — aucun nom du registre NS ne traine dans un champ KGE.")
        return

    print(f"\n{total} correction(s) appliquee(s).")
    amb = report_candidates()
    if amb:
        print(f"\nA REVOIR (noms a la fois KGE et NS, non corriges) : {', '.join(amb)}")


if __name__ == "__main__":
    main()
