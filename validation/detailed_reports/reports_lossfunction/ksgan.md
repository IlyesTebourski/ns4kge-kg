# LossFunction — KSGAN.md

**Titre :** A Knowledge Selective Adversarial Network for Link Prediction in Knowledge Graph

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 2 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 67% |
| Recall — vrais oublis | 1 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (adjuge)** | **67%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| logistic loss | ✅ oui | ection set is selected by selector. The logistic loss function used to train discriminat |
| margin-based ranking loss | ✅ oui | itive and negative triples. model with marginal loss function may cause zero loss problem. W |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| policy gradient | ❌ vrai oubli | 'policy gradient [24] with baseline b is used to tune... the generator' : non extrait. |