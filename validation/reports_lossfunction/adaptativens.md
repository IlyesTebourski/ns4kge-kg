# LossFunction — AdaptativeNS.md

**Titre :** Knowledge Graph Embedding via Adaptive Negative Subsampling

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 0 |
| **Precision automatique** | **0%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 1 |
| **Precision verifiee** | **0%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| margin-based ranking loss | ❌ non | _(non trouve automatiquement)_ |

## Verification manuelle (adjudication precision)

Chaque ecart avec la source est verifie a la main. Un item non imputable au KG est reclasse **valide** ; une extraction fausse est **condamnee** (compte faux) ; les verdicts citent la source.

| Item | Verdict | Justification |
|---|:---:|---|
| margin-based ranking loss | ⚠️ A VERIFIER | _(non encore verifie)_ |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

_Aucun candidat._