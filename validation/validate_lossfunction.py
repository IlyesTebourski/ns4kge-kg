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
    # Regle de casse homogene : en recall, un token stylise (InfoNCE) exige sa casse
    # exacte (VD.tok_regex) ; les alias (familles en mots) restent insensibles (?i:).
    # En precision tout est compile re.I (leniente, inchangee).
    flags = re.I if mode == "precision" else 0
    alias = ALIASES.get(VD.norm_key(label))
    if alias is not None:                 # famille de loss connue (synonymes)
        return re.compile(r"(?<![A-Za-z0-9])(?i:" + alias + r")(?![A-Za-z0-9])", flags)
    req = _content(label, mode) or _tokens(label)
    if not req:
        return None
    filler_alt = "|".join(sorted(FILLER[mode], key=len, reverse=True))
    gap = SEP + r"(?:(?i:" + filler_alt + r")" + SEP + r")*"
    core = gap.join(VD.tok_regex(t, mode == "recall") for t in req)
    return re.compile(r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])", flags)


class LossFunction(C.Entity):
    name = "LossFunction"
    out_dir = os.path.join(VD.HERE, "reports_lossfunction")

    prec_verdicts = {}
    # Adjudication manuelle recall (2026-07-22, justifications completes :
    # recall_checks/lossfunction_recall_check.csv).
    recall_verdicts = {
        ("batchns", "binary cross-entropy loss"): ("fp", "Footnote hypothetique ('if we were using...')."),
        ("batchns", "cross-entropy"): ("fp", "Meme footnote hypothetique."),
        ("batchns", "cross-entropy loss"): ("fp", "Meme footnote hypothetique."),
        ("dans", "Triplet loss"): ("miss",
            "'every method is standardized to use the triplet loss in Eqs.(2)' : loss "
            "d'entrainement standardisee des experiences, non extraite."),
        ("demix", "Negative Sampling loss"): ("fp", "Related work (methodes precedentes)."),
        ("demix", "Self-adversarial negative sampling loss"): ("fp", "Related work (RotatE [18])."),
        ("etruncateduns", "margin-based ranking loss"): ("fp",
            "Loss de TransE en related work ; l'objectif propre (limit-based loss) est extrait."),
        ("gibbsns", "cross-entropy loss"): ("fp",
            "Variante deja capturee par 'binary cross-entropy loss' extraite."),
        ("gibbsns", "Triplet loss"): ("fp", "Historique face recognition (Ref. [32])."),
        ("graphgan", "policy gradient"): ("miss",
            "'generator G is updated with policy gradient' : objectif d'entrainement du "
            "papier, extraits vides."),
        ("hasa", "contrastive loss"): ("fp", "Related work ; loss propres extraites (InfoNCE...)."),
        ("igan", "policy gradient"): ("miss",
            "'we use policy gradient based reinforcement learning' + eq.(17) : "
            "entrainement du generateur, non extrait."),
        ("kbgan", "margin-based ranking loss"): ("fp",
            "Deja extraite sous 'Marginal loss function' (graphie hors alias famille)."),
        ("kbgan", "negative log-likelihood"): ("fp",
            "Definition de la loss log-softmax deja extraite."),
        ("kbgan", "policy gradient"): ("miss",
            "'our framework relies on policy gradient to train the generator' : non extrait."),
        ("ksgan", "policy gradient"): ("miss",
            "'policy gradient [24] with baseline b is used to tune... the generator' : non extrait."),
        ("las", "policy gradient"): ("fp",
            "Description des policy gradients des baselines (GAN-scratch/KBGAN)."),
        ("localcognitive", "adversarial loss"): ("fp",
            "Abrege de la 'Self-adversarial negative sampling loss' deja extraite."),
        ("localcognitive", "self adversarial loss"): ("fp", "Meme phrase ; loss deja extraite."),
        ("mcns", "binary cross-entropy loss"): ("fp",
            "Loss substituee ('we substitute the BCE as a gamma-skewed hinge loss')."),
        ("mcns", "margin-based ranking loss"): ("fp",
            "Matche la hinge deja extraite sous 'skewed hinge loss'."),
        ("mcns", "mean squared error"): ("fp", "Borne theorique ('aka risk'), pas une loss."),
        ("mdncaching", "margin-based ranking loss"): ("fp", "Related work strategies GAN."),
        ("mdncaching", "Marginal loss function"): ("fp", "Meme passage related work."),
        ("noigan", "margin-based ranking loss"): ("fp",
            "Background generique ('usually required to minimize...')."),
        ("noigan", "policy gradient"): ("miss",
            "Le papier definit SON entrainement du generateur par policy gradient "
            "(reward du discriminateur), non extrait."),
        ("raakgc", "contrastive loss"): ("fp",
            "'trade-off weight for contrastive loss' = le terme InfoNCE deja extrait."),
        ("ruga", "negative log-likelihood"): ("fp", "Definition de la log-softmax deja extraite."),
        ("ruga", "policy gradient"): ("miss",
            "'We use a simple special case of Policy Gradient Theorem' : non extrait."),
        ("tans", "cross-entropy"): ("fp", "Historique de la NS loss (Mikolov)."),
        ("tans", "cross-entropy loss"): ("fp", "Meme passage historique."),
        ("tuckerdncaching", "logistic loss"): ("fp",
            "Loss d'ESNS (related work) ; le papier est loss-agnostique, marginal loss extraite."),
        ("typeaugmented", "Negative Sampling loss"): ("fp", "Related work (Sun et al.)."),
        ("typeaugmented", "Self-adversarial negative sampling loss"): ("fp", "Meme passage."),
    }

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
        return VD.strip_references(load_md_no_tables(md_path))

    def match(self, label, text, mode="precision"):
        pat = _pattern(label, mode)
        return pat.search(text) if pat else None

    def is_distinctive(self, label):
        # un nom reduit a un seul mot generique ("loss") ne sert pas au recall.
        return bool(_content(label, "recall"))

    def family_key(self, label):
        # meme equivalence que la precision : toutes les graphies de la famille
        # margin (margin-based ranking / marginal / pairwise / hinge...) = 1 famille.
        k = VD.norm_key(label)
        return "margin-family" if k in ALIASES else k


if __name__ == "__main__":
    C.run(LossFunction())
