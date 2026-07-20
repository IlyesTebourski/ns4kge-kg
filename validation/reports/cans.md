# Validation — CANS.md

**Titre extrait :** Confidence-Aware Negative Sampling Method for Noisy Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 18 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **85.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **52.9%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K-N1 | ✅ oui | re, Xie et al. [9] generated three datasets (FB15K-N1, FB15K-N2, and FB15K-N3) based on FB15K with |
| FB15K-N2 | ✅ oui | al. [9] generated three datasets (FB15K-N1, FB15K-N2, and FB15K-N3) based on FB15K with different |
| FB15K-N3 | ✅ oui | ated three datasets (FB15K-N1, FB15K-N2, and FB15K-N3) based on FB15K with different noise rates ( |
| WN18-N1 | ✅ oui | % of positive triples, which were denoted as WN18-N1, WN18-N2, WN18-N3, respectively. The statist |
| WN18-N2 | ✅ oui | tive triples, which were denoted as WN18-N1, WN18-N2, WN18-N3, respectively. The statistics of WN |
| WN18-N3 | ✅ oui | les, which were denoted as WN18-N1, WN18-N2, WN18-N3, respectively. The statistics of WN18 and it |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| FB15k | ted our approach on two common KGE datasets (FB15K and WN18 [8]), with different noise ratios, |
| Wikipedia | in KGs [13]; DBpedia created its mappings to Wikipedia info boxes via a worldwide crowd-sourcing ef |
| WN18 | proach on two common KGE datasets (FB15K and WN18 [8]), with different noise ratios, and used |

## Metrics  —  precision 67% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | aw". The lower the Mean Rank, the better. * Hits@10 [8] indicated the proportion of correct answ |
| MR | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | ettings as well. * Mean reciprocal ranking (MRR), which has a range between (0, 1], can full |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | to low noise detection ability and undesired accuracy in embedding models. Furthermore, the defini |

## NS Methods  —  precision 50% · recall~ 25%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Confidence-Aware Negative Sampling | ✅ oui | International Conference on Big Knowledge # Confidence-Aware Negative Sampling Method for Noisy Knowledge Graph Embedding |
| Uniform Negative Sampling | ✅ oui | . Though effective at detecting noises, with uniform negative sampling methods, and a harsh triple quality function |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| CKRL | nce-aware knowledge representation learning (CKRL) framework was proposed, to incorporate trip |
| GAN | ] P. Wang, S. Li, and R. Pan, "Incorporating GAN for Negative Sampling in Knowledge Represent |
| Negative Sampling | ference on Big Knowledge # Confidence-Aware Negative Sampling Method for Noisy Knowledge Graph Embedding |
| Random Negative Sampling | ding models constructed negative triplets by random sampling, and were trained to separate the scores bet |
| Random Sampling | ding models constructed negative triplets by random sampling, and were trained to separate the scores bet |
| Uniform Sampling | . Though effective at detecting noises, with uniform negative sampling methods, and a harsh triple quality function |

## KGE Models  —  precision 100% · recall~ 57%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CKRL | ✅ oui | nce-aware knowledge representation learning (CKRL) framework was proposed, to incorporate trip |
| GTrans | ✅ oui | a triple as a manifold rather than a point. GTrans [20] used dynamic and static weighting strat |
| ManifoldE | ✅ oui | ng vectors of entities into various spaces. ManifoldE [19] embedded a triple as a manifold rather |
| puTransE | ✅ oui | educed the noise from other relation spaces. puTransE [21] generated multiple embedding spaces, th |
| TransD | ✅ oui | the same vector space. Then TransR [17], and TransD [18], extended TransE, by projecting the emb |
| TransE | ✅ oui | , thus becomes an important issue. To date, TransE [8] has been a representative KRL model. How |
| TransH | ✅ oui | al with 1-to-N, N-to-1, or N-to-N relations. TransH [10] proposed to project the entity to the r |
| TransR | ✅ oui | elations were in the same vector space. Then TransR [17], and TransD [18], extended TransE, by p |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ction, and has therefore quickly gained much attention. However, most conventional embedding models |
| ComplEx | information of the KG, while calculating the complex semantic associations between entities and r |
| GAN | ] P. Wang, S. Li, and R. Pan, "Incorporating GAN for Negative Sampling in Knowledge Represent |
| RatE | $\gamma$, embeddings dimension $k$, learning rate $\lambda$ **Output:** TransE model with nois |
| SimplE | er, and G. Bouchard, "Complex embeddings for simple link prediction," in *Proceedings of ICML*, |
| TaKE | d enhance the distinguishing ability, TransE takes a pairwise ranking loss function as its opti |
