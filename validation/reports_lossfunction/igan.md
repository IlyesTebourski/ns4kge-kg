# LossFunction — IGAN.md

**Titre :** Incorporating GAN for Negative Sampling in Knowledge Representation Learning

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
| margin-based ranking loss | ✅ oui | ng need negative sampling to minimize a margin-based ranking loss. However, those works construct negativ |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| policy gradient | ⚠️ A VERIFIER | a discrete index of the entity, we use policy gradient based reinforcement learning (Williams |