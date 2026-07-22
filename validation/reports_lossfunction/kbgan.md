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
| Recall — candidats bruts (script) | 3 |
| Recall BRUT (avant adjudication) | 40% |
| Recall — vrais oublis | 1 |
| Recall — faux positifs ecartes | 2 |
| **Recall relatif (adjuge)** | **67%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Log-softmax loss function | ✅ oui | {(h, r, t') \| t' \in \mathcal{E}\}$. **Log-softmax loss function** is commonly used by mod |
| Marginal loss function | ✅ oui | replaces the loss function in WGAN with marginal loss. Although originating from very di |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ✅ faux positif (ignore) | Deja extraite sous 'Marginal loss function' (graphie hors alias famille). |
| negative log-likelihood | ✅ faux positif (ignore) | Definition de la loss log-softmax deja extraite. |
| policy gradient | ❌ vrai oubli | 'our framework relies on policy gradient to train the generator' : non extrait. |