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


def _pattern(label, mode="precision"):
    # Regle de casse homogene : les alias (mots banals, "link prediction") restent
    # insensibles (?i:) dans les deux modes ; seul un token stylise d'une valeur
    # hors enum exigerait sa casse exacte en recall (VD.tok_regex).
    flags = re.I if mode == "precision" else 0
    core = ALIASES.get(label.strip())
    if core is not None:
        core = r"(?i:" + core + r")"
    else:                                 # valeur hors enum -> match verbatim souple
        toks = re.findall(r"[A-Za-z0-9]+", label)
        if not toks:
            return None
        core = r"[\s\-_/.]*".join(VD.tok_regex(t, mode == "recall") for t in toks)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + core + r")(?![A-Za-z0-9])", flags)


class Task(C.Entity):
    name = "Task"
    out_dir = os.path.join(VD.HERE, "detailed_reports", "reports_task")

    prec_verdicts = {}
    # Adjudication manuelle des candidats recall (2026-07-22, voir
    # recall_checks/task_recall_check.csv pour les justifications completes).
    recall_verdicts = {
        ("asa", "Relation Prediction"): ("miss",
            "Task PRINCIPALE du papier ('end-to-end solution for the relationship "
            "prediction task', resultats SOTA dessus) ; configs = Link Prediction."),
        ("lts", "Triple Classification"): ("miss",
            "TABLE V. TERNARY CLASSIFICATION EXPERIMENTAL RESULT + conclusion "
            "revendiquant des gains en triplet classification."),
        ("nscaching", "Relation Prediction"): ("miss",
            "TABLE V COMPARISON ... ON TASKS OF RELATION PREDICTION AND TRIPLET "
            "CLASSIFICATION : vraie experience d'appendice non extraite."),
        ("tuckerdncaching", "Relation Prediction"): ("miss",
            "Bar charts 'Relation Prediction Accuracy (%)' pour LEUR modele."),
        ("ccs", "Relation Prediction"): ("fp",
            "Decoupage 1-to-1/1-to-N des resultats de LINK prediction."),
        ("demix", "Triple Classification"): ("fp", "Enumeration citee en related work."),
        ("eans", "Entity Alignment"): ("fp", "Limitation/travaux futurs."),
        ("etruncateduns", "Link Prediction"): ("fp",
            "Alias 'KG completion' dans le related work TransE ; papier d'Entity Alignment."),
        ("gibbsns", "Relation Prediction"): ("fp",
            "Caption de figure pedagogique illustrant la task de LINK prediction."),
        ("gns", "Link Prediction"): ("fp",
            "Alias 'knowledge graph completion' employe comme terme-parapluie ; "
            "le papier evalue la Triple Classification (extraite)."),
        ("ksgan", "Triple Classification"): ("fp",
            "Description de l'usage du dataset FB15k-237."),
        ("m2ixkg", "Triple Classification"): ("fp", "Enumeration citee en intro."),
        ("mdncaching", "Relation Prediction"): ("fp", "Travaux futurs."),
        ("mdncaching", "Triple Classification"): ("fp", "Enumeration d'intro."),
        ("raakgc", "Relation Prediction"): ("fp", "Taxonomie de related work citee."),
        ("raakgc", "Triple Classification"): ("fp", "Meme phrase de taxonomie."),
        ("randomcorrupt", "Link Prediction"): ("fp",
            "Papier de RELATION prediction (extraite) ; LP cite pour comparer aux "
            "observations de la litterature."),
        ("stc", "Entity Alignment"): ("fp",
            "Contexte sur la construction des infos de type via Wikipedia."),
        ("truncatedns", "Link Prediction"): ("fp",
            "3 occurrences, toutes en related work (CrossE/TransE) ; papier d'Entity Alignment."),
        ("tuckerdncaching", "Triple Classification"): ("fp", "Enumeration d'intro."),
    }

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
        return "\n".join([title, VD.strip_references(load_md_no_tables(md_path)), load_md_tables_only(md_path)])

    def match(self, label, text, mode="precision"):
        pat = _pattern(label, mode)
        return pat.search(text) if pat else None


if __name__ == "__main__":
    C.run(Task())
