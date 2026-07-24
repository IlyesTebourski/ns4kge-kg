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
# Regle de casse homogene (VD.tok_regex) appliquee aux alias : les acronymes
# tout-majuscules (SGD, ALS) exigent leur casse exacte en RECALL ; les noms en
# mots (Adam, AdaGrad — la litterature varie la stylisation, et aucune collision
# avec un mot anglais) restent insensibles via (?i:...). En PRECISION le pattern
# est compile avec re.I, ce qui neutralise la distinction (leniente, inchangee).
ALIASES = {
    "adam":     r"(?i:adam|adaptive\s+moment\s+estimation)",
    "adamw":    r"(?i:adam[\s\-]?w)",
    "sgd":      r"SGD|(?i:stochastic\s+gradient\s+descent)",
    "adagrad":  r"(?i:ada[\s\-]?grad|adaptive\s+(?:sub[\s\-]?)?gradient)",
    "adadelta": r"(?i:ada[\s\-]?delta)",
    "rmsprop":  r"(?i:rms[\s\-]?prop)",
    "als":      r"ALS|(?i:alternating\s+least[\s\-]?squares)",
    "momentum": r"(?i:momentum)",
    "nadam":    r"(?i:nadam)",
}


def _pattern(label, mode="precision"):
    core = ALIASES.get(VD.norm_key(label))
    if core is None:                      # optimizer hors table -> match verbatim souple
        toks = re.findall(r"[A-Za-z0-9]+", label)
        if not toks:
            return None
        core = r"[\s\-_/.]*".join(VD.tok_regex(t, mode == "recall") for t in toks)
    flags = re.I if mode == "precision" else 0
    return re.compile(r"(?<![A-Za-z0-9])(?:" + core + r")(?![A-Za-z0-9])", flags)


class Optimizer(C.Entity):
    name = "Optimizer"
    out_dir = os.path.join(VD.HERE, "detailed_reports", "reports_optimizer")

    # Verdicts remplis apres lecture de la sortie automatique (voir _SUMMARY / rapports).
    prec_verdicts = {}
    # Adjudication manuelle recall (2026-07-22, justifications completes :
    # recall_checks/optimizer_recall_check.csv).
    recall_verdicts = {
        ("asa", "SGD"): ("fp", "Description generale du principe des hard negatives."),
        ("batchns", "Adam"): ("fp", "'Adam Lerer'/'Adam Fisch' = prenoms d'auteurs."),
        ("batchns", "SGD"): ("fp", "SGD = cadre ; l'optimizer concret AdaGrad est extrait."),
        ("igan", "SGD"): ("fp", "'Adam SGD' : Adam extrait, SGD = parapluie."),
        ("localcognitive", "SGD"): ("fp", "'minibatch SGD with Adam optimizer' : Adam extrait."),
        ("nmiss", "AdaGrad"): ("fp", "AdaGrad cite comme repoussoir ('because it addresses "
                                     "the problem of decreasing learning rate in AdaGrad')."),
        ("nmiss", "SGD"): ("fp", "'Adam [13] SGD optimizer' : Adam extrait, SGD = cadre."),
        ("nscaching", "SGD"): ("fp", "Cadre generique + discussion convergence ; Adam extrait."),
        ("typeaugmented", "SGD"): ("miss",
            "'learning rate used for SGD lr in {0.1,0.5,1.0}', best config lr=0.5 : "
            "les modeles TaKE sont entraines par SGD, non extrait."),
        ("typeconstraints", "AdaGrad"): ("miss",
            "'optimized the cost function using mini-batch adaptive gradient descent' : "
            "AdaGrad utilise pour le modele neuronal, non extrait (KG n'a que ALS/SGD)."),
    }

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
        return VD.strip_references(load_md_no_tables(md_path))

    def match(self, label, text, mode="precision"):
        pat = _pattern(label, mode)
        return pat.search(text) if pat else None


if __name__ == "__main__":
    C.run(Optimizer())
