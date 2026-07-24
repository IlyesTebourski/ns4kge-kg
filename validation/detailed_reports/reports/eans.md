# Validation — EANS.md

**Titre extrait :** Entity Aware Negative Sampling with Auxiliary Loss of False Negative Prediction for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **90.5%** |
| Candidats faux negatifs (dans le texte, non extraits) | 24 |
| **Recall relatif (indicatif, a valider)** | **44.2%** |

## Datasets  —  precision 100% · recall~ 40%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K237 | ✅ oui | r> </thead> <tbody> <tr> <td>FB15K237</td> <td>14,541</td> <td>237 |
| WN18RR | ✅ oui | d>20,466</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <td>11< |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2210.06242v1 [cs.LG] 12 Oct 2022 # Entity A |
| FB15k | </tbody> </table> Table 1: Statistics of FB15K-237 and WN18RR datasets. be formalized as, |
| WN18 | es et al., 2013; Bollacker et al., 2008) and WN18 (Bordes et al., 2013; Miller, 1995), respec |

## Metrics  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | <th>MR</th> <th>MRR</th> <th>Hit@10</th> <th>MR</th> <th>MRR</th |
| MR | ✅ oui | ">WN18RR</th> </tr> <tr> <th>MR</th> <th>MRR</th> <th>Hit@10 |
| MRR | ✅ oui | tr> <tr> <th>MR</th> <th>MRR</th> <th>Hit@10</th> <th>MR< |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | le are updated. The index mapping table that map the virtual indices and the real entity indi |

## NS Methods  —  precision 75% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Entity Aware Negative Sampling | ✅ oui | arXiv:2210.06242v1 [cs.LG] 12 Oct 2022 # Entity Aware Negative Sampling with Auxiliary Loss of False Negative Predic |
| Entity Aware Negative Sampling + Self-Adversarial Negative Sampling | ❌ NON | _(absent du texte)_ |
| KB-GAN | ✅ oui | td>0.501</td> </tr> <tr> <td>KBGAN(Cai and Wang, 2017)<sup>††</sup></td> |
| NS-Caching | ✅ oui | td>0.432</td> </tr> <tr> <td>NSCaching(Zhang et al., 2019)</td> <td>186</td |
| SANS | ✅ oui | td>0.530</td> </tr> <tr> <td>SANS + Self-adv.(Ahrabian et al., 2020)</td> |
| SANS + Self-Adversarial Negative Sampling | ❌ NON | _(absent du texte)_ |
| Self-Adversarial Negative Sampling | ✅ oui | od in the graph. (Sun et al., 2019) proposed self-adversarial negative sampling, which give difference weights to each sampl |
| Uniform Negative Sampling | ✅ oui | ive and negative samples of various steps on uniform sampling method and EANS with TransE on FB15K-237. # |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | the graph. (Sun et al., 2019) proposed self-adversarial negative sampling, which give difference weights to each sampl |
| EANS | ethod called Entity Aware Negative Sampling (EANS), which is able to sample negative entities |
| GAN | 017) proposed Generative Adversarial Network(GAN) (Goodfellow et al., 2014) based architectur |
| Negative Sampling | .06242v1 [cs.LG] 12 Oct 2022 # Entity Aware Negative Sampling with Auxiliary Loss of False Negative Predic |
| Random Negative Sampling | ed because of its efficiency. Such a uniform random sampling method can be effective at the beginning of |
| Random Sampling | ed because of its efficiency. Such a uniform random sampling method can be effective at the beginning of |
| Self-Adv | td>0.478</td> </tr> <tr> <td>Self-adv.(Sun et al., 2019)</td> <td><u>172</ |
| Self-adversarial Sampling | od in the graph. (Sun et al., 2019) proposed self-adversarial negative sampling, which give difference weights to each sampl |
| Structure-Aware Negative Sampling | iam L Hamilton, and Avishek Joey Bose. 2020. Structure aware negative sampling in knowledge graphs. *arXiv preprint arXiv:2 |
| Uniform Random Negative Sampling | idely used because of its efficiency. Such a uniform random sampling method can be effective at the beginning of |
| Uniform Random Sampling | idely used because of its efficiency. Such a uniform random sampling method can be effective at the beginning of |
| Uniform Sampling | ive and negative samples of various steps on uniform sampling method and EANS with TransE on FB15K-237. # |

## KGE Models  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | l., 2011), DistMult (Yang et al., 2014), and ComplEx (Trouillon et al., 2016) is the most represe |
| DistMult | ✅ oui | rious spaces. RESCAL (Nickel et al., 2011), DistMult (Yang et al., 2014), and ComplEx (Trouillon |
| RESCAL | ✅ oui | y and relation vectors into various spaces. RESCAL (Nickel et al., 2011), DistMult (Yang et al. |
| RotatE | ✅ oui | > </tr> <tr> <td rowspan="5">RotatE<br/>(Sun et al., 2019)</td> <td>Unif |
| TransD | ✅ oui | et al., 2014), TransR (Lin et al., 2015) and TransD (Ji et al., 2015), increase their expressive |
| TransE | ✅ oui | and the other for semantic matching models. TransE (Bordes et al., 2013) is the first proposed |
| TransH | ✅ oui | model. Various extensions of TransE, such as TransH (Wang et al., 2014), TransR (Lin et al., 201 |
| TransR | ✅ oui | TransE, such as TransH (Wang et al., 2014), TransR (Lin et al., 2015) and TransD (Ji et al., 20 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | d Tat-Seng Chua. 2019. Kgat: Knowledge graph attention network for recommendation. In *Proceedings |
| DAT | 11):39–41. Dai Quoc Nguyen, Tu Dinh Nguyen, Dat Quoc Nguyen, and Dinh Phung. 2017. A novel e |
| GAN | 017) proposed Generative Adversarial Network(GAN) (Goodfellow et al., 2014) based architectur |
| InteractE | , Nilesh Agrawal, and Partha Talukdar. 2020. Interacte: Improving convolution-based knowledge graph |
| LINE | </tbody> </table> Figure 3: Hit@10(solid line) and MRR(dashed line) of TransE and ComplEx |
| RatE | gative sample size, $lr$ is initial learning rate, $\gamma$ is fixed margin, and $\alpha$ is s |
| SimplE | laume Bouchard. 2016. Complex embeddings for simple link prediction. In *International conferenc |
| TaKE | selected cluster and the remaining clusters, take the nearest cluster as the next cluster to a |
