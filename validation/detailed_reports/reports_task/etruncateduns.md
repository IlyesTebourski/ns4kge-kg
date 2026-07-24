# Task — eTruncatedUNS.md

**Titre :** Bootstrapping Entity Alignment with Knowledge Graph Embedding

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
| Entity Alignment | ✅ oui | Bootstrapping Entity Alignment with Knowledge Graph Embedding Proceedi |

## Recall — Task du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Link Prediction | ✅ faux positif (ignore) | Alias 'KG completion' dans le related work TransE ; papier d'Entity Alignment. |