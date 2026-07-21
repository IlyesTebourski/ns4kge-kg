# LossFunction — PNS.md

**Titre :** Enhancing Knowledge Graph Embedding with Probabilistic Negative Sampling

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| margin-based ranking loss | ✅ oui | r + r \approx t_r$. Training phase uses margin-based ranking loss to encourage discrimination between gol |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._