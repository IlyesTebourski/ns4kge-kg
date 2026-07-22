# Task — TruncatedNS.md

**Titre :** Fusing Attribute Character Embeddings with Truncated Negative Sampling for Entity Alignment

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
| Entity Alignment | ✅ oui | gs with Truncated Negative Sampling for Entity Alignment ![electronics logo](page_1_image_2_v2.j |

## Recall — Task du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Link Prediction | ✅ faux positif (ignore) | 3 occurrences, toutes en related work (CrossE/TransE) ; papier d'Entity Alignment. |