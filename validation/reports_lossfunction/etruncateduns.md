# LossFunction — eTruncatedUNS.md

**Titre :** Bootstrapping Entity Alignment with Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 2 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 67% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 1 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| limit-based loss | ✅ oui | ent-oriented KG embedding, we propose a limit-based objective function, which expects |
| negative log-likelihood | ✅ oui | distribution, we minimize the following negative log-likelihood function to obtain the optimal embeddin |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ✅ faux positif (ignore) | Loss de TransE en related work ; l'objectif propre (limit-based loss) est extrait. |