# Optimizer — TypeConstraints.md

**Titre :** Type-Constrained Representation Learning in Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Optimizer extraits | 2 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 67% |
| Recall — vrais oublis | 1 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (adjuge)** | **67%** |

## Precision automatique — Optimizer extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| ALS | ✅ oui | ion can be minimized via very efficient Alternating Least-Squares (ALS) that effectively exploits data sp |
| SGD | ✅ oui | f observed training triples $T$ through Stochastic Gradient Descent (SGD), where $\gamma > 0$. The "corrupt |

## Recall — Optimizer du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| AdaGrad | ❌ vrai oubli | 'optimized the cost function using mini-batch adaptive gradient descent' : AdaGrad utilise pour le modele neuronal, non extrait (KG n'a que ALS/SGD). |