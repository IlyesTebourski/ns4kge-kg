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
| Recall — candidats bruts (script) | 3 |
| Recall BRUT (avant adjudication) | 40% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 3 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| cross-entropy loss | ✅ oui | are sampled. In Algorithm 1, we use the cross-entropy loss to optimize the inner product wher |
| skewed hinge loss | ✅ oui | te the binary cross-entropy loss as a γ-skewed hinge loss, $$L = \max(0, E_\theta(v) \cdot |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| binary cross-entropy loss | ✅ faux positif (ignore) | Loss substituee ('we substitute the BCE as a gamma-skewed hinge loss'). |
| margin-based ranking loss | ✅ faux positif (ignore) | Matche la hinge deja extraite sous 'skewed hinge loss'. |
| mean squared error | ✅ faux positif (ignore) | Borne theorique ('aka risk'), pas une loss. |