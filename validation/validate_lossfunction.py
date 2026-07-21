#!/usr/bin/env python3
"""
Validation des LOSS FUNCTIONS extraites par le KG.

Provenance (source unique) : prompt1 (prose). `TrainingProtocol.LossFunction[]`.
Exemples : "margin-based ranking loss", "cross-entropy loss", "InfoNCE",
"logistic loss", "negative sampling loss".

Matcher GENERIQUE (non taille pour un article) : les tokens distinctifs du nom
doivent apparaitre dans l'ordre, insensible a la casse, avec des mots de liaison
OPTIONNELS ("loss", "function", "based", "the"...) — le texte ecrit souvent
"margin ranking loss" ou "margin-based loss" la ou le KG a "margin-based ranking
loss". Aucune liste noire ; les ecarts sont tranches en verification MANUELLE.

Sorties : validation/reports_lossfunction/<slug>.md + _SUMMARY.md
"""
import os
import re

import validate_datasets as VD
import validate_common as C

SEP = r"[\s\-_/.]*"
# Vrais mots de liaison OPTIONNELS (connecteurs).
CONNECTORS = {"function", "based", "the", "a", "of", "with"}
# Mot-CATEGORIE qui nomme la loss. NB : le traiter comme optionnel reduirait
# "Triplet loss" a "triplet" (match sur "invalid triplet"), "adversarial loss" a
# "adversarial" (match sur "adversarial training"), "Negative Sampling loss" a
# "negative sampling" (le sujet de tous les articles) -> bruit massif.
CATEGORY = {"loss"}

# PRECISION (leniente) : on fait confiance au label extrait, "loss" optionnel.
# RECALL (strict) : "loss" EXIGE, pour ne pas crier au faux negatif sur un simple
# mot de domaine (comme la dissymetrie precision/recall des validateurs KGE/NS).
FILLER = {"precision": CONNECTORS | CATEGORY, "recall": CONNECTORS}


# Famille max-margin : « margin-based ranking loss » = « margin-based loss » =
# « marginal loss » = « hinge loss » = « pairwise (ranking) loss ». Meme loss, autres
# graphies (synonymes de domaine, comme SGD=Stochastic Gradient Descent). On exige
# toujours le mot « loss »/« function » (pas de match sur un « margin » nu).
MARGIN_FAMILY = (r"margin(?:al|[\s\-]?based)?[\s\-]*(?:ranking[\s\-]*)?loss"
                 r"|hinge[\s\-]*(?:loss|function)"
                 r"|pairwise[\s\-]*(?:ranking[\s\-]*)?loss")
ALIASES = {k: MARGIN_FAMILY for k in (
    "marginbasedrankingloss", "marginbasedloss", "marginloss", "marginalloss",
    "marginrankingloss", "hingeloss", "pairwiseloss", "pairwiserankingloss",
    "rankingloss",
)}


def _tokens(label):
    return re.findall(r"[A-Za-z0-9]+", label)


def _content(label, mode):
    return [t for t in _tokens(label) if t.lower() not in FILLER[mode]]


def _pattern(label, mode):
    alias = ALIASES.get(VD.norm_key(label))
    if alias is not None:                 # famille de loss connue (synonymes)
        return re.compile(r"(?<![A-Za-z0-9])(?:" + alias + r")(?![A-Za-z0-9])", re.I)
    req = _content(label, mode) or _tokens(label)
    if not req:
        return None
    filler_alt = "|".join(sorted(FILLER[mode], key=len, reverse=True))
    gap = SEP + r"(?:(?:" + filler_alt + r")" + SEP + r")*"
    core = gap.join(re.escape(t) for t in req)
    return re.compile(r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])", re.I)


class LossFunction(C.Entity):
    name = "LossFunction"
    out_dir = os.path.join(VD.HERE, "reports_lossfunction")

    prec_verdicts = {}
    recall_verdicts = {}

    def extract(self, data):
        out = {}
        tp = (data.get("Experimentation", {}) or {}).get("TrainingProtocol", {}) or {}
        for v in (tp.get("LossFunction") or []):
            v = str(v).strip()
            if v:
                out.setdefault(VD.norm_key(v), v)
        return out

    def source_text(self, md_path, data):
        from no_facts_pipeline.core import load_md_no_tables
        return load_md_no_tables(md_path)

    def match(self, label, text, mode="precision"):
        pat = _pattern(label, mode)
        return pat.search(text) if pat else None

    def is_distinctive(self, label):
        # un nom reduit a un seul mot generique ("loss") ne sert pas au recall.
        return bool(_content(label, "recall"))


if __name__ == "__main__":
    C.run(LossFunction())
