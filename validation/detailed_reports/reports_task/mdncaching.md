# Task — MDNCaching.md

**Titre :** MDNCaching: A Strategy to Generate Quality Negatives for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Task extraits | 1 |
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

## Precision automatique — Task extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Link Prediction | ✅ oui | in knowledge acquisition tasks such as link prediction, triplet classification, and knowledge |

## Recall — Task du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Relation Prediction | ✅ faux positif (ignore) | Travaux futurs. |
| Triple Classification | ✅ faux positif (ignore) | Enumeration d'intro. |