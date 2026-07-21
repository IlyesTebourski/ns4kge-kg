# LossFunction — BatchNS.md

**Titre :** PyTorch-BigGraph: A Large-scale Graph Embedding System

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 3 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **67%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 1 |
| **Precision verifiee** | **67%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| logistic loss | ✅ oui | ze, nor are they prone to overfitting. Logistic and softmax loss functions may also be |
| margin-based ranking loss | ❌ non | _(non trouve automatiquement)_ |
| softmax loss | ✅ oui | hey prone to overfitting. Logistic and softmax loss functions may also be used instead |

## Verification manuelle (adjudication precision)

Chaque ecart avec la source est verifie a la main. Un item non imputable au KG est reclasse **valide** ; une extraction fausse est **condamnee** (compte faux) ; les verdicts citent la source.

| Item | Verdict | Justification |
|---|:---:|---|
| margin-based ranking loss | ⚠️ A VERIFIER | _(non encore verifie)_ |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| binary cross-entropy loss | ⚠️ A VERIFIER | oss for positives and negatives, e.g. a binary cross-entropy loss <sup>3</sup>The slower convergence may |
| cross-entropy | ⚠️ A VERIFIER | positives and negatives, e.g. a binary cross-entropy loss <sup>3</sup>The slower convergence |
| cross-entropy loss | ⚠️ A VERIFIER | positives and negatives, e.g. a binary cross-entropy loss <sup>3</sup>The slower convergence may |