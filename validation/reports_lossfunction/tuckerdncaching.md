# LossFunction — TuckerDNCaching.md

**Titre :** TuckerDNCaching: high-quality negative sampling with tucker decomposition

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
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
| marginal loss | ✅ oui | to the discriminator that minimizes the marginal loss between positive and negative samples t |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| logistic loss | ⚠️ A VERIFIER | ng negatives and utilizes a shift-based logistic loss function. Despite addressing the proble |