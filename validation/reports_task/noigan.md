# Task — NoiGAN.md

**Titre :** NoiGAN: Noise Aware Knowledge Graph Embedding with GAN

| Metrique | Valeur |
|---|---|
| Task extraits | 2 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **50%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 1 |
| **Precision verifiee** | **50%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — Task extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Link Prediction | ✅ oui | of-the-art algorithms both in regard to knowledge graph completion and error detection. ## 1 INTRODUCTION |
| Triple Classification | ❌ non | _(non trouve automatiquement)_ |

## Verification manuelle (adjudication precision)

Chaque ecart avec la source est verifie a la main. Un item non imputable au KG est reclasse **valide** ; une extraction fausse est **condamnee** (compte faux) ; les verdicts citent la source.

| Item | Verdict | Justification |
|---|:---:|---|
| Triple Classification | ⚠️ A VERIFIER | _(non encore verifie)_ |

## Recall — Task du vocab (verifie) present mais NON extrait

_Aucun candidat._