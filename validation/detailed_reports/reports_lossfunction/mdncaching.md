# LossFunction — MDNCaching.md

**Titre :** MDNCaching: A Strategy to Generate Quality Negatives for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 0 |
| Trouves automatiquement (TP auto) | 0 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 2 |
| Recall BRUT (avant adjudication) | 0% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 2 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| _(aucun LossFunction extrait)_ | — | — |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ✅ faux positif (ignore) | Related work strategies GAN. |
| Marginal loss function | ✅ faux positif (ignore) | Meme passage related work. |