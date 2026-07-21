# LossFunction — RAAKGC.md

**Titre :** Knowledge Graph Completion with Relation-Aware Anchor Enhancement

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
| InfoNCE | ✅ oui | he network is trained by minimizing the InfoNCE loss (Chen et al. 2020) over both class |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| contrastive loss | ⚠️ A VERIFIER | nd of the trade-off weight $\alpha$ for contrastive loss within the range {0.1, 0.2, 0.3, 0.4, 0 |