# Validation — GibbsNS.md

**Titre extrait :** Link Prediction Based on Data Augmentation and Metric Learning Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 26 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **89.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 25 |
| **Recall relatif (indicatif, a valider)** | **51.0%** |

## Datasets  —  precision 100% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k | ✅ oui | on three link prediction benchmark datasets FB15k-237, WN11RR and FB15k. ![check for updates |
| FB15k-237 | ✅ oui | on three link prediction benchmark datasets FB15k-237, WN11RR and FB15k. ![check for updates logo |
| WN18RR | ✅ oui | test or validation sets under $(h, r_i, t)$. WN18RR, on the other hand, does not have this restr |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | aph embeddings via paired relation vectors. *arXiv* **2020**, arXiv:2011.03798. 11. He, M.; Du |
| WN11 | tions and duplicate relations from FB15k and WN11, respectively. By benchmarking the performan |

## Metrics  —  precision 80% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | ounced. However, our model excels in MRR and Hit@1 compared to all comparison models. It is wo |
| Hits@10 | ✅ oui | nducted the experiment on FB15k and show the Hit@10 results in the table. <table> <thead> |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MR | ✅ oui | worth mentioning that our model's Mean Rank (MR) performance on the FB15k-237 dataset signif |
| MRR | ✅ oui | ess pronounced. However, our model excels in MRR and Hit@1 compared to all comparison models. |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | in a knowledge graph enhances recommendation accuracy, Q&A answers, and semantic representations. |
| MAP | s as negative node pairs”. In the knowledge map embedding task, negative sampling is regarde |

## NS Methods  —  precision 83% · recall~ 31%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| EANS | ✅ oui | dom negative sampling, KBGAN, NSCaching, and EANS [40], were used to make comparisons with the |
| Gibbs Negative Sampling | ✅ oui | s research offers a unique strategy based on Gibbs sampling and connection embedding to improve the mode |
| KBGAN | ✅ oui | nalysis of static negative sampling methods, KBGAN [17] found that the majority of negative sam |
| NSCaching | ✅ oui | gative samples across various relationships. NSCaching [21] designed two modules: head entity cache |
| Uniform Random Negative Sampling | ✅ oui | ors. Four negative sampling methods, namely, uniform random negative sampling, KBGAN, NSCaching, and EANS [40], were used |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Entity Similarity-based Negative Sampling | oint relationship context negative sampling, entity similarity-based negative sampling, etc. As the performance of models encounter |
| Entity-Aware Negative Sampling | v* **2022**, arXiv:2203.02424. 40. Je, S.H. Entity Aware Negative Sampling with Auxiliary Loss of False Negative Predic |
| GAN | 19. Wang, P.; Li, S.; Pan, R. Incorporating GAN for Negative Sampling in Knowledge Represent |
| IGAN | e new distributions in the training process. IGAN [19] designed a generator and performed adva |
| Negative Sampling | ing is initially used to obtain high-quality negative samples. Following that, the triplet entities are ma |
| Random Negative Sampling | r negative sampling methods, namely, uniform random negative sampling, KBGAN, NSCaching, and EANS [40], were used |
| Random Sampling | r negative sampling methods, namely, uniform random negative sampling, KBGAN, NSCaching, and EANS [40], were used |
| Static Sampling | gative samples. After a detailed analysis of static negative sampling methods, KBGAN [17] found that the majority |
| Uniform Negative Sampling | ng problem is mitigated, this study used the uniform sampling method UNIFORM and the GNS method proposed i |
| Uniform Random Sampling | ors. Four negative sampling methods, namely, uniform random negative sampling, KBGAN, NSCaching, and EANS [40], were used |
| Uniform Sampling | ng problem is mitigated, this study used the uniform sampling method UNIFORM and the GNS method proposed i |

## KGE Models  —  precision 93% · recall~ 58%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | tion difficult, especially in the setting of complex relations. At the same time, current techniq |
| ConvE | ✅ oui | ng a holistic approach to semantic matching. ConvE [28] takes a unique perspective by separatel |
| DistMult | ✅ oui | have emerged to address these shortcomings. DistMult [25] simplifies the RESCAL model by constrai |
| InteractE | ✅ oui | its capability to handle complex relations. InteractE [29] identifies a limitation in previous mod |
| KG-BERT | ✅ oui | tilized pre-trained models to tackle issues. KG-BERT [14], for instance, is a BERT-based knowledg |
| KGE-EML | ✅ oui | Learning and Relationship Fusion modules as KGE-EML [11]. In knowledge graphs, there may be ins |
| KGE-EML+GNS | ❌ NON | _(absent du texte)_ |
| PairRE | ✅ oui | l’s capability to handle symmetry relations. PairRE, proposed by [10], leverages pairwise relati |
| PROCRUSTES | ✅ oui | td>0.528</td> </tr> <tr> <td>PROCRUSTES</td> <td>0.345</td> <td>0.24 |
| RESCAL | ✅ oui | cance. An eminent contender in this class is RESCAL proposed by Nickel et al. [24], which charac |
| RotatE | ✅ oui | des the transformation process. In contrast, RotatE, proposed by [23], utilizes rotation operati |
| TransD | ✅ oui | > </tr> <tr> <td rowspan="5">TransD</td> <td>Uniform</td> <td>18 |
| TransE | ✅ oui | ule that affects model performance. Take the TransE model [9] as an illustration; its objective |
| TransH | ✅ oui | a high similarity. To overcome challenges, TransH, introduced by [9], utilizes hyperplanes. In |
| TuckER | ✅ oui | e representation of non-symmetric relations. TuckER [27] employed a decomposition algorithm to b |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | the final embedded model. A knowledge-guided attention mechanism was introduced by [20], and they d |
| BERT | ized pre-trained models to tackle issues. KG-BERT [14], for instance, is a BERT-based knowledg |
| GAN | 19. Wang, P.; Li, S.; Pan, R. Incorporating GAN for Negative Sampling in Knowledge Represent |
| GCN | andewiele, G.; Ongenae, F.; Van Hoecke, S. R-GCN: The R could stand for random. *arXiv* **202 |
| HAN | ng Lijuan Duan <sup>1,2,3,*</sup>, Shengwen Han <sup>1,2,3</sup>, Wei Jiang <sup>4,*</sup>, |
| R-GCN | Vandewiele, G.; Ongenae, F.; Van Hoecke, S. R-GCN: The R could stand for random. *arXiv* **202 |
| SimplE | lfill the constraint $h + r \approx t$. This simple constraint yields a straightforward and effe |
| Structured Embedding | ston, J.; Collobert, R.; Bengio, Y. Learning structured embeddings of knowledge bases. In Proceedings of the AA |
| Structured Embeddings | ston, J.; Collobert, R.; Bengio, Y. Learning structured embeddings of knowledge bases. In Proceedings of the AA |
| TaKE | rtant module that affects model performance. Take the TransE model [9] as an illustration; its |
