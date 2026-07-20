# Validation — PNS.md

**Titre extrait :** Enhancing Knowledge Graph Embedding with Probabilistic Negative Sampling

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 8 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **72.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 4 |
| **Recall relatif (indicatif, a valider)** | **66.7%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | bases such as Word-net (WN18) and Freebase (FB15K) have been proven to be very useful as train |
| WN18 | ✅ oui | on space. Knowledge bases such as Word-net (WN18) and Freebase (FB15K) have been proven to be |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Citeseer | on hyperplanes. In *AAAI*, pages 1112–1119. Citeseer, 2014. [3] Y. Lin, Z. Liu, M. Sun, Y. Liu, |

## Metrics  —  precision 50% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | correct entities in top-10 ranked entities (Hits@10). Ranking is decided by score function $f_r$ |
| MR | ❌ NON | _(absent du texte)_ |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 33% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Probabilistic Negative Sampling | ✅ oui | # Enhancing Knowledge Graph Embedding with Probabilistic Negative Sampling Citation in BibTeX format **VIBHOR KANOJIA |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | Knowledge Graph Embedding with Probabilistic Negative Sampling Citation in BibTeX format **VIBHOR KANOJIA |

## KGE Models  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| TransE | ✅ oui | series of translation-based models such as *TransE*[1], *TransH*[2], and *TransR*[3]. This pape |
| TransG | ✅ oui | ied to the current state-of-the-art approach TransG[4] to further improve its performance. # 6. |
| TransH | ✅ oui | anslation-based models such as *TransE*[1], *TransH*[2], and *TransR*[3]. This paper proposes mo |
| TransR | ✅ oui | odels such as *TransE*[1], *TransH*[2], and *TransR*[3]. This paper proposes modifications in th |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| ComplEx | s use of hyperplanes to address the issue of complex relation embedding. Entities are projected i |
| RatE | we used Adam Optimiser with initial learning rate $\lambda = 0.001$, batch size = 256, dimensi |
