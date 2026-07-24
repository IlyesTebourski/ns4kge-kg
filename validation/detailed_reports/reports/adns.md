# Validation — ADNS.md

**Titre extrait :** Affinity Dependent Negative Sampling for Knowledge Graph Embeddings

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 22 |
| Extraites NON trouvees (FP -> erreur precision) | 0 |
| **Precision** | **100.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 13 |
| **Recall relatif (indicatif, a valider)** | **62.9%** |

## Datasets  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Kinship | ✅ oui | es and relations. We have used nations [12], kinship [13], and UMLS [14] dataset. These datasets |
| Nations | ✅ oui | pecific entities and relations. We have used nations [12], kinship [13], and UMLS [14] dataset. T |
| UMLS | ✅ oui | We have used nations [12], kinship [13], and UMLS [14] dataset. These datasets are not very bi |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | nal semantics using neural-embedding models. arXiv preprint arXiv:1411.4072. 4. Trouillon, T., |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | mean rank (MR), mean reciprocal rank (MRR), Hit@1, Hit@3, Hit@5, and Hit@10. # 6 Discussion a |
| Hits@10 | ✅ oui | iprocal rank (MRR), Hit@1, Hit@3, Hit@5, and Hit@10. # 6 Discussion and Result Comparing with |
| Hits@3 | ✅ oui | ank (MR), mean reciprocal rank (MRR), Hit@1, Hit@3, Hit@5, and Hit@10. # 6 Discussion and Resu |
| Hits@5 | ✅ oui | ), mean reciprocal rank (MRR), Hit@1, Hit@3, Hit@5, and Hit@10. # 6 Discussion and Result Com |
| MR | ✅ oui | used in our researches which are mean rank (MR), mean reciprocal rank (MRR), Hit@1, Hit@3, |
| MRR | ✅ oui | ch are mean rank (MR), mean reciprocal rank (MRR), Hit@1, Hit@3, Hit@5, and Hit@10. # 6 Disc |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 100% · recall~ 62%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Affinity Dependent Negative Sampling | ✅ oui | CEUR-WS.org/Vol-2635/paper8.pdf # Affinity Dependent Negative Sampling for Knowledge Graph Embeddings* Mirza Mohta |
| Bernoulli Negative Sampling | ✅ oui | $C$ negative samples. In the training phase, Bernoulli sampling [10] is used to decide if the head (subject) |
| Distributional Negative Sampling | ✅ oui | prominent candidate as replaceable entity is Distributional Negative Sampling [9]. This approach does not require any pre- |
| Near Miss Sampling | ✅ oui | ational Sampling, Nearest Neighbor sampling, Near Miss sampling. Nearest Neighbor sampling and Near Miss sam |
| Nearest Neighbor Sampling | ✅ oui | es discussed in [7] are Relational Sampling, Nearest Neighbor sampling, Near Miss sampling. Nearest Neighbor sampli |
| Random Negative Sampling | ✅ oui | ethod with distributed negative sampling and random negative sampling and the results have been found comparable a |
| Relational Sampling | ✅ oui | . Some other approaches discussed in [7] are Relational Sampling, Nearest Neighbor sampling, Near Miss sampli |
| Typed Sampling | ✅ oui | ient pool to corrupt positive instances [7]. Typed Sampling is the negative sampling based on entity and |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | $C$ negative samples. In the training phase, Bernoulli sampling [10] is used to decide if the head (subject) |
| Negative Sampling | rg/Vol-2635/paper8.pdf # Affinity Dependent Negative Sampling for Knowledge Graph Embeddings* Mirza Mohta |
| Random Sampling | ethod with distributed negative sampling and random negative sampling and the results have been found comparable a |
| Typed Negative Sampling | ient pool to corrupt positive instances [7]. Typed Sampling is the negative sampling based on entity and |
| Unknown | idered false, but it can only be labelled as unknown. On the other hand, similar to most of the m |

## KGE Models  —  precision 100% · recall~ 42%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | recent years. e.g, TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all o |
| DistMult | ✅ oui | rature in the recent years. e.g, TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. |
| RotatE | ✅ oui | E [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all of these models depend o |
| TransE | ✅ oui | in the literature in the recent years. e.g, TransE [2], DistMult [3], Complex[4], TransH [5], R |
| TransH | ✅ oui | . e.g, TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all of these mod |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| HypER | 5.3 Hyperparameters For TransE the optimal hyper parameters were: learning rate = 0.1, gamma |
| LINE | this algorithm, similar to [9] in first few lines the main aim is to, perform head or tail cor |
| Neural Tensor Network | ning, C. D., & Ng, A. (2013). Reasoning with neural tensor networks for knowledge base completion. In Advances i |
| Neural Tensor Networks | ning, C. D., & Ng, A. (2013). Reasoning with neural tensor networks for knowledge base completion. In Advances i |
| RatE | the optimal hyper parameters were: learning rate = 0.1, gamma = 14 (for kinship, nations data |
| SimplE | Bouchard, G. (2016). Complex embeddings for simple link prediction. International Conference on |
| TaKE | dings 7 replaceable entities at once (which takes fairly less amount of time). This function G |
