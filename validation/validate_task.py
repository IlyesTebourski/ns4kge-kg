#!/usr/bin/env python3
"""
Validation des TASKS extraites par le KG.

Provenance : prompt2 (tables/Configurations). `Configurations[].Task`, un ENUM
contraint : "Link Prediction", "Triple Classification", "Entity Alignment",
"Relation Prediction". Regle du prompt : DEFAUT "Link Prediction" sauf si le titre,
les sections, les captions ou le contexte indiquent explicitement une autre task.

Comme la task est determinee par le CONTEXTE (titre / sections / captions), on
valide l'ensemble des tasks DISTINCTES d'un article contre : titre + prose + tables
(captions comprises). Le cas "Link Prediction" par DEFAUT est particulier : s'il
n'apparait pas litteralement, ce n'est pas forcement une erreur (defaut legitime en
l'absence d'un autre signal de task) -> tranche en verification MANUELLE.

Matcher GENERIQUE : libelle de la task + quelques alias standards, insensible a la
casse. Aucune liste noire ; les ecarts sont adjuges a la main.

Sorties : validation/reports_task/<slug>.md + _SUMMARY.md
"""
import os
import re

import validate_datasets as VD
import validate_common as C

# Alias standards par valeur d'enum (coeur de regex, insensible a la casse).
ALIASES = {
    "Link Prediction":       r"link\s*prediction|knowledge\s*graph\s*completion|kg\s*completion|entity\s*prediction",
    "Triple Classification": r"tri(?:ple|plet)\s*classification",
    "Entity Alignment":      r"entity\s*alignment",
    "Relation Prediction":   r"relation(?:ship)?\s*prediction",
}


def _pattern(label):
    core = ALIASES.get(label.strip())
    if core is None:                      # valeur hors enum -> match verbatim souple
        toks = re.findall(r"[A-Za-z0-9]+", label)
        if not toks:
            return None
        core = r"[\s\-_/.]*".join(re.escape(t) for t in toks)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + core + r")(?![A-Za-z0-9])", re.I)


class Task(C.Entity):
    name = "Task"
    out_dir = os.path.join(VD.HERE, "reports_task")

    prec_verdicts = {}
    recall_verdicts = {}

    def extract(self, data):
        # ensemble des tasks DISTINCTES (les 6567 configs se reduisent a peu de valeurs)
        out = {}
        exp = data.get("Experimentation", {}) or {}
        for c in (exp.get("Configurations") or []):
            if isinstance(c, dict):
                v = (c.get("Task") or "").strip()
                if v:
                    out.setdefault(VD.norm_key(v), v)
        return out

    def source_text(self, md_path, data):
        from no_facts_pipeline.core import load_md_no_tables, load_md_tables_only
        title = (data.get("Article", {}) or {}).get("title", "") or ""
        return "\n".join([title, load_md_no_tables(md_path), load_md_tables_only(md_path)])

    def match(self, label, text, mode="precision"):
        pat = _pattern(label)
        return pat.search(text) if pat else None


if __name__ == "__main__":
    C.run(Task())
