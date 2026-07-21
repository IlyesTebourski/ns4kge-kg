# Optimizer — NSCaching.md

**Titre :** NSCaching: Simple and Efficient Negative Sampling for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Optimizer extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — Optimizer extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Adam | ✅ oui | n$ $\{0.001, 0.01, 0.1\}$ [38]. We use Adam [22], which is a popular variant of SGD |

## Recall — Optimizer du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| SGD | ⚠️ A VERIFIER | wo objectives can be optimized by using stochastic gradient descent in an unified framework (Algorithm 1). |