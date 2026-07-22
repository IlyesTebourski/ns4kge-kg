# Optimizer — ASA.md

**Titre :** Relation-aware Graph Attention Model With Adaptive Self-adversarial Training

| Metrique | Valeur |
|---|---|
| Optimizer extraits | 0 |
| Trouves automatiquement (TP auto) | 0 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 0% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 1 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — Optimizer extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| _(aucun Optimizer extrait)_ | — | — |

## Recall — Optimizer du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| SGD | ✅ faux positif (ignore) | Description generale du principe des hard negatives. |