# LossFunction — DMNS.md

**Titre :** Diffusion-based Negative Sampling on Graphs for Link Prediction

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
| log-sigmoid loss | ✅ oui | **Link prediction loss.** We adopt the log-sigmoid loss [14] for the link prediction task. |
| mean squared error | ✅ oui | ction. **Diffusion loss.** We employ a mean squared error (MSE) between sampled noises from the f |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._