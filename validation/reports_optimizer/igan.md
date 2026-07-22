# Optimizer — IGAN.md

**Titre :** Incorporating GAN for Negative Sampling in Knowledge Representation Learning

| Metrique | Valeur |
|---|---|
| Optimizer extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 50% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 1 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — Optimizer extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Adam | ✅ oui | criminator and generator are trained by Adam stochastic optimization (Kingma and Ba |

## Recall — Optimizer du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| SGD | ✅ faux positif (ignore) | 'Adam SGD' : Adam extrait, SGD = parapluie. |