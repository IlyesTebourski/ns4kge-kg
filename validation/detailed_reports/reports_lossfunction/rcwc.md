# LossFunction — RCWC.md

**Titre :** KGBoost: A Classification-Based Knowledge Base Completion Method with Negative Sampling

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 2 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 0 |
| Recall BRUT (avant adjudication) | 100% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| binary cross entropy loss | ✅ oui | n at the $k$-th iteration. We adopt the binary cross entropy loss commonly used in logistic regressi |
| negative log likelihood loss | ✅ oui | ty embeddings are then trained with the negative log likelihood loss as in [Sun et al., 2019]: $$ \beg |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._