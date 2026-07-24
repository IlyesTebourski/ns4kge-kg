# LossFunction — TypeConstraints.md

**Titre :** Type-Constrained Representation Learning in Knowledge Graphs

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 3 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **67%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 1 |
| **Precision verifiee** | **67%** |
| Recall — candidats bruts (script) | 0 |
| Recall BRUT (avant adjudication) | 100% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Bernoulli cross-entropy loss | ❌ non | _(non trouve automatiquement)_ |
| max-margin-based ranking loss | ✅ oui | mbeddings are learned by minimizing the max-margin-based ranking cost function $$ \mathcal{L}_{TransE} |
| regularized least-squares | ✅ oui | mbeddings are learned by minimizing the regularized least-squares function $$ \mathcal{L}_{RESCAL} = \su |

## Verification manuelle (adjudication precision)

Chaque ecart avec la source est verifie a la main. Un item non imputable au KG est reclasse **valide** ; une extraction fausse est **condamnee** (compte faux) ; les verdicts citent la source.

| Item | Verdict | Justification |
|---|:---:|---|
| Bernoulli cross-entropy loss | ⚠️ A VERIFIER | _(non encore verifie)_ |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._