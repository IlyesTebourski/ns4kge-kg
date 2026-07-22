# Task — GNS.md

**Titre :** Good negative sampling for triple classification

| Metrique | Valeur |
|---|---|
| Task extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 50% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 1 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — Task extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Triple Classification | ✅ oui | Good negative sampling for triple classification # Good negative sampling for triple cla |

## Recall — Task du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Link Prediction | ✅ faux positif (ignore) | Alias 'knowledge graph completion' employe comme terme-parapluie ; le papier evalue la Triple Classification (extraite). |