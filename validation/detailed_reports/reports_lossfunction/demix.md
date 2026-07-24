# LossFunction — DeMix.md

**Titre :** Negative Sampling with Adaptive Denoising Mixup for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 2 |
| Recall BRUT (avant adjudication) | 33% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 2 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| cross-entropy loss | ✅ oui | tern}, \alpha)$ and $\ell(., .)$ is the cross-entropy loss. Movever, the probability distribu |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Negative Sampling loss | ✅ faux positif (ignore) | Related work (methodes precedentes). |
| Self-adversarial negative sampling loss | ✅ faux positif (ignore) | Related work (RotatE [18]). |