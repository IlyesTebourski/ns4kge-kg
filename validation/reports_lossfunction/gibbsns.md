# LossFunction — GibbsNS.md

**Titre :** Link Prediction Based on Data Augmentation and Metric Learning Knowledge Graph Embedding

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
| binary cross-entropy loss | ✅ oui | })}}$$ (6) Finally, the model utilizes binary cross-entropy as the loss function for optimization, |
| contrastive loss | ✅ oui | h dimensions. Ref. [31] introduced the Contrastive Loss function, which trains the model t |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| cross-entropy loss | ⚠️ A VERIFIER | istance models, as most of them utilize cross-entropy loss. In this paper, we also adopt such loss |
| Triplet loss | ⚠️ A VERIFIER | r samples apart. Ref. [32] proposed the Triplet Loss function as an improvement, where each |