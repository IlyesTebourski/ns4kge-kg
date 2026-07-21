# LossFunction — NoiGAN.md

**Titre :** NoiGAN: Noise Aware Knowledge Graph Embedding with GAN

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
| cross-entropy loss | ✅ oui | formulated as minimizing the following cross entropy loss: $$ \mathcal{L}_D = - \sum_{(h,r, |
| negative sampling loss | ✅ oui | al., 2016). To optimize the KGE model, negative sampling is usually required to minimize the mar |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ⚠️ A VERIFIER | ing is usually required to minimize the margin based ranking loss. A conventional method to construct neg |
| marginal loss | ⚠️ A VERIFIER | ing is usually required to minimize the margin based ranking loss. A conventional method to construct neg |
| pairwise ranking loss | ⚠️ A VERIFIER | ing is usually required to minimize the margin based ranking loss. A conventional method to construct neg |
| policy gradient | ⚠️ A VERIFIER | lity issue. A common solution is to use policy gradient based reinforcement learning instead (W |