# LossFunction — MCNS.md

**Titre :** Understanding Negative Sampling in Graph Representation Learning

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
| cross-entropy loss | ✅ oui | are sampled. In Algorithm 1, we use the cross-entropy loss to optimize the inner product wher |
| skewed hinge loss | ✅ oui | te the binary cross-entropy loss as a γ-skewed hinge loss, $$L = \max(0, E_\theta(v) \cdot |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| binary cross-entropy loss | ⚠️ A VERIFIER | defined margin. Thus, we substitute the binary cross-entropy loss as a γ-skewed hinge loss, $$L = \max(0 |
| margin-based ranking loss | ⚠️ A VERIFIER | k nodes with 1/2 probability each. The hinge loss pulls positive node pairs closer and pu |
| marginal loss | ⚠️ A VERIFIER | k nodes with 1/2 probability each. The hinge loss pulls positive node pairs closer and pu |
| mean squared error | ⚠️ A VERIFIER | $\square$ According to Theorem 2, the mean squared error, aka risk, of $\vec{u}^\top \vec{v}$ is |
| pairwise ranking loss | ⚠️ A VERIFIER | k nodes with 1/2 probability each. The hinge loss pulls positive node pairs closer and pu |