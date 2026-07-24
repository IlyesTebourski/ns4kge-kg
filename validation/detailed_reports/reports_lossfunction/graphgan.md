# LossFunction — GraphGAN.md

**Titre :** GraphGAN: Graph Representation Learning with Generative Adversarial Nets

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 0 |
| Trouves automatiquement (TP auto) | 0 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 0% |
| Recall — vrais oublis | 1 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (adjuge)** | **0%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| _(aucun LossFunction extrait)_ | — | — |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| policy gradient | ❌ vrai oubli | 'generator G is updated with policy gradient' : objectif d'entrainement du papier, extraits vides. |