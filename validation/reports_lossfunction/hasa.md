# LossFunction — HaSa.md

**Titre :** HaSa: Hardness and Structure-Aware Contrastive Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 6 |
| Trouves automatiquement (TP auto) | 6 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 86% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 1 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Cross-entropy loss | ✅ oui | ttmers et al. [8], Yao et al. [38] used cross-entropy loss. More recent works such as Shen et |
| HaSa loss | ✅ oui | 23 Oct 15 [cs.AI] arXiv:2305.10563v2 # HaSa: Hardness and Structure-Aware Contrasti |
| InfoNCE | ✅ oui | to knowledge graph embedding (KGE) via InfoNCE. For KGE, efficient learning relies on |
| Negative log-likelihood | ✅ oui | uillon et al. [29], Xu and Li [35] used negative log-likelihood while Dettmers et al. [8], Yao et al. [ |
| Negative sampling loss | ✅ oui | Graph Embedding, Contrastive Learning, Negative Sampling **ACM Reference Format:** Honggen Zhan |
| Triplet loss | ✅ oui | Lin et al. [18], Yang et al. [36] used triplet loss, by assigning higher scores to pos |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| contrastive loss | ✅ faux positif (ignore) | Related work ; loss propres extraites (InfoNCE...). |