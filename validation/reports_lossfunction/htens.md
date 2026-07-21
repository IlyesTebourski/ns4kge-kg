# LossFunction — HTENS.md

**Titre :** Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 3 |
| Trouves automatiquement (TP auto) | 3 |
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
| Kullback-Leibler divergence loss | ✅ oui | h'_j, r, t'_j)}. \tag{11}$$ We use the Kullback-Leibler divergence loss to train the sampler, $$L_{kl}(p_ |
| log-softmax loss | ✅ oui | s a triple is more likely to exist. The log-softmax loss function is used to train these mo |
| marginal loss | ✅ oui | s a triple is more likely to exist. The marginal loss function is used to train these models. |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._