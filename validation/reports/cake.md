# Validation — CAKE.md

**Titre extrait :** CAKE: A Scalable Commonsense-Aware Framework For Multi-View Knowledge Graph Completion

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 26 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **96.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 24 |
| **Recall relatif (indicatif, a valider)** | **52.0%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DBpedia-242 | ✅ oui | d>15,838</td> </tr> <tr> <td>DBpedia-242</td> <td>298</td> <td>99,744 |
| FB15K | ✅ oui | r> </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td>14,9 |
| FB15K237 | ✅ oui | d>59,071</td> </tr> <tr> <td>FB15K237</td> <td>237</td> <td>14,505 |
| NELL-995 | ✅ oui | N-1 relation by our designed CANS module on NELL-995. ## 3.3 Commonsense-Aware Negative Sampling |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2202.13785v3 [cs.AI] 17 Apr 2022 # CAKE: A |
| Wikipedia | , multilingual knowledge base extracted from wikipedia. *Semantic Web*, 6(2):167–195. Zelong Li, J |

## Metrics  —  precision 100% · recall~ 83%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | @10</th> <th>Hits@3</th> <th>Hits@1</th> <th>MR</th> <th>MRR</th |
| Hits@10 | ✅ oui | <th>MR</th> <th>MRR</th> <th>Hits@10</th> <th>Hits@3</th> <th>Hit |
| Hits@3 | ✅ oui | RR</th> <th>Hits@10</th> <th>Hits@3</th> <th>Hits@1</th> <th>MR< |
| MR | ✅ oui | /tr> <tr> <th> </th> <th>MR</th> <th>MRR</th> <th>Hits@1 |
| MRR | ✅ oui | <th> </th> <th>MR</th> <th>MRR</th> <th>Hits@10</th> <th>Hi |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | o the symbolic representations, limiting the accuracy of KGC. Take the tail entity prediction (*Da |

## NS Methods  —  precision 89% · recall~ 38%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CAKE | ✅ oui | arXiv:2202.13785v3 [cs.AI] 17 Apr 2022 # CAKE: A Scalable Commonsense-Aware Framework For |
| Commonsense-Aware Negative Sampling | ✅ oui | iples and entity concepts. * We develop a **commonsense-aware negative sampling** strategy for generating valid and high-qua |
| Domain-based Negative Sampling | ✅ oui | lf-scoring function without a generator. (3) Domain-based sampling: domain-based NS (Wang et al., 2019b) and ty |
| MVLP | ✅ oui | ) module and the multi-view link prediction (MVLP) module. Firstly, the ACG module extracts th |
| None Sampling | ✅ oui | s to improve the efficiency of sampling. (5) None-sampling: NS-KGE (Li et al., 2021) eliminates the NS |
| NSCaching | ✅ oui | the correct domain. (4) Efficient sampling: NSCaching (Zhang et al., 2019b) employs cache containi |
| Self-Adversarial Negative Sampling | ✅ oui | riples in an adversarial training framework. Self-adversarial sampling (Sun et al., 2019) performs similar to KBGAN |
| Type-Constrained Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling | ✅ oui | th various types of NS techniques, including uniform sampling (Bordes et al., 2013), none sampling (Li et |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | niform distribution (Wang et al., 2014). (2) Adversarial-based sampling: KBGAN (Cai and Wang, 2018) integrates the K |
| CANS | le, the commonsense-aware negative sampling (CANS) module and the multi-view link prediction ( |
| Domain Sampling | lf-scoring function without a generator. (3) Domain-based sampling: domain-based NS (Wang et al., 2019b) and ty |
| GAN | introduces generative adversarial networks (GAN) in the NS framework, making the original mo |
| KBGAN | al., 2014). (2) Adversarial-based sampling: KBGAN (Cai and Wang, 2018) integrates the KGE mode |
| Local Closed-World Assumption | 2.2 Negative Sampling of KGE Following the local closed-world assumption (Dong et al., 2014), the existing NS techniq |
| Negative Sampling | bedding (KGE) techniques suffer from invalid negative sampling and the uncertainty of fact-view link predic |
| Non-Sampling | ng Chen, and Yongfeng Zhang. 2021. Efficient non-sampling knowledge graph embedding. In *Proceedings o |
| NS-KGE | e efficiency of sampling. (5) None-sampling: NS-KGE (Li et al., 2021) eliminates the NS procedur |
| Random Negative Sampling | action technique from KGs. Then, contrary to random sampling, we **purposefully** generate the high-quali |
| Random Sampling | action technique from KGs. Then, contrary to random sampling, we **purposefully** generate the high-quali |
| Self-adversarial Sampling | riples in an adversarial training framework. Self-adversarial sampling (Sun et al., 2019) performs similar to KBGAN |
| Uniform Sampling | th various types of NS techniques, including uniform sampling (Bordes et al., 2013), none sampling (Li et |

## KGE Models  —  precision 100% · recall~ 53%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | onsense together with the characteristics of complex relations. Furthermore, a multi-view link pr |
| DistMult | ✅ oui | ecomposition-based** score function, such as DistMult (Yang et al., 2015): $$E(h, r, t) = \mathbf |
| HAKE | ✅ oui | et al., 2016), RotatE (Sun et al., 2019) and HAKE (Zhang et al., 2020) learn the embeddings of |
| JOIE | ✅ oui | other hand, although some KGE models such as JOIE (Hao et al., 2019) employ the ontology built |
| KBGAN | ✅ oui | al., 2014). (2) Adversarial-based sampling: KBGAN (Cai and Wang, 2018) integrates the KGE mode |
| RESCAL | ✅ oui | models such as TransE (Bordes et al., 2013), RESCAL (Nickel et al., 2011), ComplEx (Trouillon et |
| RotatE | ✅ oui | l., 2011), ComplEx (Trouillon et al., 2016), RotatE (Sun et al., 2019) and HAKE (Zhang et al., 2 |
| TransE | ✅ oui | multi-hop reasoning. (3) KGE models such as TransE (Bordes et al., 2013) and its variants (Sun |
| TransH | ✅ oui | ns, namely 1-1, 1-N, N-1, and N-N defined in TransH (Wang et al., 2014) for negative sampling, w |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | and Sonia Chernova. 2020. Path ranking with attention to type hierarchies. In *Proceedings of the |
| CAKE | arXiv:2202.13785v3 [cs.AI] 17 Apr 2022 # CAKE: A Scalable Commonsense-Aware Framework For |
| GAN | introduces generative adversarial networks (GAN) in the NS framework, making the original mo |
| HypER | Adam optimizer for the training and tune the hyper-parameters of our model by grid search on th |
| Random Walk | o, Tom Mitchell, and William W. Cohen. 2011. Random walk inference and learning in a large scale know |
| RatE | is set as 2 for all the models. The learning rate is chosen from 0.0001 to 0.01. The margin is |
| SimplE | laume Bouchard. 2016. Complex embeddings for simple link prediction. In *Proceedings of the 33rd |
| TaKE | presentations, limiting the accuracy of KGC. Take the tail entity prediction (*David, National |
