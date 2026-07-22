# LossFunction — GHN.md

**Titre :** Improving Knowledge Graph Completion with Generative Hard Negative Mining

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
| Cross-entropy loss | ✅ oui | generator is optimized by minimizing a cross-entropy loss with the golden entity: $$ \mathc |
| InfoNCE | ✅ oui | r constructing the negative set, we use InfoNCE (Chen et al., 2020) loss to train the p |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._