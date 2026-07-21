# LossFunction — dans.md

**Titre :** Diversified and Adaptive Negative Sampling on Knowledge Graphs

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
| cross-entropy loss | ✅ oui | will be used to minimize the following cross-entropy loss: $$ -\sum_{\tau \in \mathcal{D}_{ |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Triplet loss | ⚠️ A VERIFIER | every method is standardized to use the triplet loss in Eqs.(2). Other baseline settings hav |