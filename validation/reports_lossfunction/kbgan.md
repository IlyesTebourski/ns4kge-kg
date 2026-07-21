# LossFunction — KBGAN.md

**Titre :** KBGAN: Adversarial Learning for Knowledge Graph Embeddings

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
| Log-softmax loss function | ✅ oui | {(h, r, t') \| t' \in \mathcal{E}\}$. **Log-softmax loss function** is commonly used by mod |
| Marginal loss function | ✅ oui | replaces the loss function in WGAN with marginal loss. Although originating from very di |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ⚠️ A VERIFIER | ative examples, and use distance-based, margin-loss embedding models as the discriminator t |
| marginal loss | ⚠️ A VERIFIER | ative examples, and use distance-based, margin-loss embedding models as the discriminator t |
| negative log-likelihood | ⚠️ A VERIFIER | f(h',r,t')}$. The loss function is the negative log-likelihood of this probabilistic model: $$L_l = \ |
| pairwise ranking loss | ⚠️ A VERIFIER | ative examples, and use distance-based, margin-loss embedding models as the discriminator t |
| policy gradient | ⚠️ A VERIFIER | learning—It trains the generator using policy gradient and other tricks. IRGAN (Wang et al., 2 |