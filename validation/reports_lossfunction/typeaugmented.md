# LossFunction — TypeAugmented.md

**Titre :** A type-augmented knowledge graph embedding framework for knowledge graph completion

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
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
| cross-entropy loss | ✅ oui | weakened by prior knowledge. Since the cross entropy loss function has shown good performanc |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Negative Sampling loss | ⚠️ A VERIFIER | strategy and design a self-adversarial negative sampling loss as the optimization object. Other work |
| Self-adversarial negative sampling loss | ⚠️ A VERIFIER | negative sampling strategy and design a self-adversarial negative sampling loss as the optimization object. Other work |