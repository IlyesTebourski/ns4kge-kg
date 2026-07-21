# LossFunction — TANS.md

**Titre :** Unified Interpretation of Smoothing Methods for Negative Sampling Loss Functions in Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 3 |
| Trouves automatiquement (TP auto) | 3 |
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
| Negative Sampling loss | ✅ oui | Interpretation of Smoothing Methods for Negative Sampling Loss Functions in Knowledge Graph Embed |
| Self-Adversarial Negative Sampling loss | ✅ oui | in KGE relies on smoothing methods like Self-Adversarial Negative Sampling (SANS) and subsampling. However, it is |
| Triplet Adaptive Negative Sampling loss | ✅ oui | loss in KGE and induces a new NS loss, Triplet Adaptive Negative Sampling (TANS), that can cover the characterist |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| cross-entropy | ⚠️ A VERIFIER | loss is proposed to approximate softmax cross-entropy loss to reduce computational costs by s |
| cross-entropy loss | ⚠️ A VERIFIER | loss is proposed to approximate softmax cross-entropy loss to reduce computational costs by sampli |