# LossFunction — LEMON.md

**Titre :** Language Model-driven Negative Sampling

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
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
| margin-based ranking loss | ✅ oui | iscriminator is trained to minimize the margin-based ranking loss, while the generator learns to sample h |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._