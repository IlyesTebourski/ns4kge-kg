# Validation — CCS.md

**Titre extrait :** Op-Trans: An Optimization Framework for Negative Sampling and Triplet-Mapping Properties in Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 35 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **97.2%** |
| Candidats faux negatifs (dans le texte, non extraits) | 26 |
| **Recall relatif (indicatif, a valider)** | **57.4%** |

## Datasets  —  precision 100% · recall~ 80%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | on four popular data sets, i.e., WN18 [33], FB15k [33], WN18RR [34], and FB15K237 [35]. The ex |
| FB15K237 | ✅ oui | .e., WN18 [33], FB15k [33], WN18RR [34], and FB15K237 [35]. The experiments show that our method i |
| WN18 | ✅ oui | experiments on four popular data sets, i.e., WN18 [33], FB15k [33], WN18RR [34], and FB15K237 |
| WN18RR | ✅ oui | ular data sets, i.e., WN18 [33], FB15k [33], WN18RR [34], and FB15K237 [35]. The experiments sho |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | ive approach for knowledge graph embedding. *arXiv* **2015**, arXiv:1509.05490, 2015. 28. Ji, S |

## Metrics  —  precision 100% · recall~ 83%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | <th>MR</th> <th>MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hit |
| Hits@10 | ✅ oui | <th>MR</th> <th>MRR</th> <th>Hits@10</th> <th>MR</th> <th>MRR</th |
| Hits@3 | ✅ oui | MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> </tr> </ |
| MR | ✅ oui | e field of knowledge graph completion, i.e., MR, MRR, Hits@N. Mean Rank (MR): It averages t |
| MRR | ✅ oui | eld of knowledge graph completion, i.e., MR, MRR, Hits@N. Mean Rank (MR): It averages the ra |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | he representation power of the model and the accuracy of predicting candidate entities. ![Diagram |

## NS Methods  —  precision 83% · recall~ 31%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | to model training. The TansH model uses the Bernoulli sampling method, which aims at reducing false negativ |
| Cluster-Cache Sampling | ✅ oui | ate high-quality negative triplets, based on cluster-cache sampling (CCS). It is a general negative sampling met |
| Kbgan Sampling | ✅ oui | pling methods, including Bernoulli sampling, Kbgan sampling, and NSCaching sampling as well as our propo |
| NSCaching Sampling | ✅ oui | ding Bernoulli sampling, Kbgan sampling, and NSCaching sampling as well as our proposed CCS sampling. Berno |
| Uniform Random Sampling | ✅ oui | pling works, such as the TransE model, use a uniform random sampling method to generate negative samples, Appl. |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | to model training. The TansH model uses the Bernoulli sampling method, which aims at reducing false negativ |
| Cache-based Negative Sampling | -quality negative triplets, based on cluster-cache sampling (CCS). It is a general negative sampling met |
| Dynamic Distribution Sampling | categories: fixed distribution sampling and dynamic distribution sampling [38]. The previous sampling works, such as t |
| GAN | pired by the generative adversarial network (GAN) [39], some works have attempted to generate |
| IGAN | ets using an adversarial training framework. IGAN [40] and Kbgan [41] both introduce GAN for n |
| KBGAN | dversarial training framework. IGAN [40] and Kbgan [41] both introduce GAN for negative samplin |
| Negative Sampling | e # Op-Trans: An Optimization Framework for Negative Sampling and Triplet-Mapping Properties in Knowledge |
| NSCaching | ng and increases the difficulty of training. NSCaching [38] has fewer parameters than both IGAN and |
| Random Negative Sampling | ized. The existing KGE models widely use the random sampling method, which generates negative samples by |
| Random Sampling | ized. The existing KGE models widely use the random sampling method, which generates negative samples by |
| Uniform Random Negative Sampling | pling works, such as the TransE model, use a uniform random sampling method to generate negative samples, Appl. |

## KGE Models  —  precision 100% · recall~ 62%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| HAKE | ✅ oui | otation translation of the vectors in space. HAKE [31] maps the entities into spatial polar co |
| NTN | ✅ oui | rgy (SME) [16] model, neural tensor network (NTN) [17] model, and matrix factorization (RESCA |
| Op-TransD | ✅ oui | d>0.4873</td> </tr> <tr> <td>Op-TransD</td> <td>3352</td> <td>0.290 |
| Op-TransE | ✅ oui | ns framework with the TransE model to obtain Op-TransE and give the training procedure of the compl |
| Op-TransH | ✅ oui | d>0.4852</td> </tr> <tr> <td>Op-TransH</td> <td>4404</td> <td>0.230 |
| Op-TransR | ✅ oui | d>0.4815</td> </tr> <tr> <td>Op-TransR</td> <td>3685</td> <td>0.241 |
| OTE | ✅ oui | the entities into spatial polar coordinates. OTE [32] exploits the orthogonality relation var |
| PTransE | ✅ oui | 5], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recently, RotatE [30] has changed |
| RESCAL | ✅ oui | (NTN) [17] model, and matrix factorization (RESCAL) [18] model. However, these KGE models have |
| RotatE | ✅ oui | , TransAt [28], PTransE [29], etc. Recently, RotatE [30] has changed the translation process of |
| SE | ✅ oui | ompletion, such as the structured embedding (SE) [15] model, semantic matching energy (SME) |
| SME | ✅ oui | g (SE) [15] model, semantic matching energy (SME) [16] model, neural tensor network (NTN) [17 |
| STransE | ✅ oui | , TransD [23], TransM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29 |
| TransA | ✅ oui | TransM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recen |
| TransAt | ✅ oui | TranSparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recently, RotatE [3 |
| TransD | ✅ oui | ily. These include TransH [21], TransR [22], TransD [23], TransM [24], TranSparse [25], STransE |
| TransE | ✅ oui | gradually become the mainstream in KGE. The TransE [19] model first proposed to use relations v |
| TransH | ✅ oui | ion Embedding Methods) family. These include TransH [21], TransR [22], TransD [23], TransM [24], |
| TransM | ✅ oui | clude TransH [21], TransR [22], TransD [23], TransM [24], TranSparse [25], STransE [26], TransA |
| TranSparse | ✅ oui | [21], TransR [22], TransD [23], TransM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28 |
| TransR | ✅ oui | Methods) family. These include TransH [21], TransR [22], TransD [23], TransM [24], TranSparse [ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | 20 ferent from previous models, we pay more attention to the different contributions of each tripl |
| ComplEx | ns many triplets that constitute a large and complex knowledge network graph. It organizes and st |
| GAN | pired by the generative adversarial network (GAN) [39], some works have attempted to generate |
| HAN | perties in Knowledge Graph Embedding Huixia Han ![ORCID logo](page_1_image_5_v2.jpg), Xinyue |
| HypER | gamma]_+$$ (3) where $\gamma$ is the margin hyper-parameter separating the positive and negati |
| Neural Tensor Network | , semantic matching energy (SME) [16] model, neural tensor network (NTN) [17] model, and matrix factorization ( |
| Neural Tensor Networks | en, D.; Manning, C.D.; Ng, A. Reasoning with Neural Tensor Networks for Knowledge Base Completion. In Proceeding |
| RatE | ng dimension $d = \{50, 80, 150\}$, learning rate $\eta = \{0.00001, 0.0001, 0.001\}$, the mar |
| SimplE | ph. It organizes and stores information in a simple and efficient way, which is very suitable fo |
| Structured Embedding | d of knowledge graph completion, such as the structured embedding (SE) [15] model, semantic matching energy (S |
| Structured Embeddings | ston, J.; Collobert, R.; Bengio, Y. Learning structured embeddings of knowledge based. In Proceedings of the AA |
| TaKE | better generalization performance because it takes into account that entities may have multiple |
| word2vec | bedding vector translation invariance of the word2vec model, Borders et al. proposed the first tra |
