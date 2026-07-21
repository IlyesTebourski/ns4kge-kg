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
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| limit-based loss | ✅ oui | ent-oriented KG embedding, we propose a limit-based objective function, which expects |
| negative log-likelihood | ✅ oui | distribution, we minimize the following negative log-likelihood function to obtain the optimal embeddin |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ⚠️ A VERIFIER | e $\tau = (h, r, t)$. They optimize the margin-based ranking loss to make the scores of positive triples |
| marginal loss | ⚠️ A VERIFIER | e $\tau = (h, r, t)$. They optimize the margin-based ranking loss to make the scores of positive triples |
| pairwise ranking loss | ⚠️ A VERIFIER | e $\tau = (h, r, t)$. They optimize the margin-based ranking loss to make the scores of positive triples |