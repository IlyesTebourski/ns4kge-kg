#!/usr/bin/env python3
"""
Validation des OPTIMIZERS extraits par le KG.

Provenance (source unique) : prompt1 (prose). `TrainingProtocol.Optimizer`.
Le prompt NORMALISE vers le nom court standard : "Adam", "SGD", "AdaGrad"
(jamais "Adam Optimiser"). On valide donc la presence du nom court dans la prose.

Matcher GENERIQUE (non taille pour un article) : nom en mot-entier, insensible a
la casse, tirets/espaces souples ("AdamW", "Ada Grad"). Les ecarts (nom absent,
faux match sur un prenom "Adam", etc.) sont tranches en verification MANUELLE.

Sorties : validation/reports_optimizer/<slug>.md + _SUMMARY.md
"""
import os
import re

import validate_datasets as VD
import validate_common as C


# Alias DETERMINISTES et auditables par optimizer canonique (comme metrics MR=Mean
# Rank). Ce ne sont PAS du fuzzy : ce sont les expansions/graphies standard du meme
# nom (SGD = Stochastic Gradient Descent ; AdaGrad souvent ecrit "Ada-Grad").
ALIASES = {
    "adam":     r"adam|adaptive\s+moment\s+estimation",
    "adamw":    r"adam[\s\-]?w",
    "sgd":      r"sgd|stochastic\s+gradient\s+descent",
    "adagrad":  r"ada[\s\-]?grad|adaptive\s+(?:sub[\s\-]?)?gradient",
    "adadelta": r"ada[\s\-]?delta",
    "rmsprop":  r"rms[\s\-]?prop",
    "als":      r"als|alternating\s+least[\s\-]?squares",
    "momentum": r"momentum",
    "nadam":    r"nadam",
}


def _pattern(label):
    core = ALIASES.get(VD.norm_key(label))
    if core is None:                      # optimizer hors table -> match verbatim souple
        toks = re.findall(r"[A-Za-z0-9]+", label)
        if not toks:
            return None
        core = r"[\s\-_/.]*".join(re.escape(t) for t in toks)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + core + r")(?![A-Za-z0-9])", re.I)


class Optimizer(C.Entity):
    name = "Optimizer"
    out_dir = os.path.join(VD.HERE, "reports_optimizer")

    # Verdicts remplis apres lecture de la sortie automatique (voir _SUMMARY / rapports).
    prec_verdicts = {}
    recall_verdicts = {}

    def extract(self, data):
        out = {}
        tp = (data.get("Experimentation", {}) or {}).get("TrainingProtocol", {}) or {}
        opt = tp.get("Optimizer")
        for v in (opt if isinstance(opt, list) else [opt]):
            v = (str(v).strip() if v else "")
            if v:
                out.setdefault(VD.norm_key(v), v)
        return out

    def source_text(self, md_path, data):
        from no_facts_pipeline.core import load_md_no_tables
        return load_md_no_tables(md_path)

    def match(self, label, text, mode="precision"):
        pat = _pattern(label)
        return pat.search(text) if pat else None


if __name__ == "__main__":
    C.run(Optimizer())
