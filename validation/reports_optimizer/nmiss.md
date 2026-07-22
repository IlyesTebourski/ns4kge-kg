# Optimizer — NMiss.md

**Titre :** Analysis of the Impact of Negative Sampling on Link Prediction in Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Optimizer extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 2 |
| Recall BRUT (avant adjudication) | 33% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 2 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — Optimizer extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Adam | ✅ oui | edding size (100), and data. We use the Adam [13] SGD optimizer for training because |

## Recall — Optimizer du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| AdaGrad | ✅ faux positif (ignore) | AdaGrad cite comme repoussoir ('because it addresses the problem of decreasing learning rate in AdaGrad'). |
| SGD | ✅ faux positif (ignore) | 'Adam [13] SGD optimizer' : Adam extrait, SGD = cadre. |