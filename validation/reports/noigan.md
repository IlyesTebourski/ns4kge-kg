# Validation — NoiGAN.md

**Titre extrait :** NoiGAN: Noise Aware Knowledge Graph Embedding with GAN

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 22 |
| Extraites NON trouvees (FP -> erreur precision) | 22 |
| **Precision** | **50.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 14 |
| **Recall relatif (indicatif, a valider)** | **61.1%** |

## Datasets  —  precision 100% · recall~ 71%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | r> </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td>14,9 |
| FB15K-237 | ✅ oui | td>5,000</td> </tr> <tr> <td>FB15K-237</td> <td>237</td> <td>14,541 |
| WN18 | ✅ oui | d>59,071</td> </tr> <tr> <td>WN18</td> <td>18</td> <td>40,943< |
| WN18RR | ✅ oui | d>20,466</td> </tr> <tr> <td>WN18RR</td> <td>11</td> <td>40,943< |
| YAGO3-10 | ✅ oui | td>3,134</td> </tr> <tr> <td>YAGO3-10</td> <td>37</td> <td>123,182 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | <td>Positive</td> <td>(voice actor (filmmaking occupation),<br/>/people/profess |
| Arxiv | al learning for knowledge graph embeddings. *arXiv preprint arXiv:1711.04071*, 2017. Kathrin D |

## Metrics  —  precision 50% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AUC | ✅ oui | <th colspan="2">Metric</th> <th>AUC</th> <th>Spe</th> <th>AUC</t |
| Hits@1 | ❌ NON | _(absent du texte)_ |
| Hits@10 | ❌ NON | _(absent du texte)_ |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | /tr> <tr> <th> </th> <th>MRR</th> <th>H@1</th> <th>H@3</t |
| Spe | ✅ oui | Metric</th> <th>AUC</th> <th>Spe</th> <th>AUC</th> <th>Spe</t |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 17% · recall~ 44%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CKRL | ✅ oui | ., 2019)), (3) noise aware KGE models (e.g., CKRL (Xie et al., 2018)) and (4) KGE models with |
| CKRL (100%) | ❌ NON | _(absent du texte)_ |
| CKRL (20%) | ❌ NON | _(absent du texte)_ |
| CKRL (40%) | ❌ NON | _(absent du texte)_ |
| CKRL (70%) | ❌ NON | _(absent du texte)_ |
| KBGAN | ✅ oui | ., 2018)) and (4) KGE models with GAN (e.g., KBGAN (Cai & Wang, 2017)). In particular, there ar |
| KBGAN (40%) | ❌ NON | _(absent du texte)_ |
| NoiGAN | ✅ oui | review as a conference paper at ICLR 2020 # NOIGAN: NOISE AWARE KNOWLEDGE GRAPH EMBEDDING WITH |
| NoiGAN (hard) | ❌ NON | _(absent du texte)_ |
| NoiGAN (hard) (100%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (hard) (20%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (hard) (40%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (hard) (70%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (soft) | ❌ NON | _(absent du texte)_ |
| NoiGAN (soft) (100%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (soft) (20%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (soft) (40%) | ❌ NON | _(absent du texte)_ |
| NoiGAN (soft) (70%) | ❌ NON | _(absent du texte)_ |
| Random Negative Sampling | ✅ oui | guidance, the generator generates "noise" by random sampling. However, such "noise" is too easy for discr |
| Unknown | ❌ NON | _(absent du texte)_ |
| Unknown (100%) | ❌ NON | _(absent du texte)_ |
| Unknown (40%) | ❌ NON | _(absent du texte)_ |
| Unknown (70%) | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Confidence-Aware Negative Sampling | g Bu, Xiaojian Liu, Shengwei Ji, and Lei Li. Confidence-aware negative sampling method for noisy knowledge graph embedding. |
| GAN | : NOISE AWARE KNOWLEDGE GRAPH EMBEDDING WITH GAN **Anonymous authors** Paper under double-bl |
| IRGAN | Xu, Benyou Wang, Peng Zhang, and Dell Zhang. Irgan: A minimax game for unifying generative and |
| Negative Sampling | on et al., 2016). To optimize the KGE model, negative sampling is usually required to minimize the margin b |
| Random Sampling | guidance, the generator generates "noise" by random sampling. However, such "noise" is too easy for discr |

## KGE Models  —  precision 100% · recall~ 59%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Attention | ✅ oui | TRACT Knowledge graph has gained increasing attention in recent years for its successful applicati |
| CKRL | ✅ oui | ., 2019)), (3) noise aware KGE models (e.g., CKRL (Xie et al., 2018)) and (4) KGE models with |
| ComplEx | ✅ oui | al., 2011), DistMult (Yang et al., 2014) and ComplEx (Trouillon et al., 2016). To optimize the KG |
| DistMult | ✅ oui | models include RESCAL (Nickel et al., 2011), DistMult (Yang et al., 2014) and ComplEx (Trouillon e |
| KBGAN | ✅ oui | ., 2018)) and (4) KGE models with GAN (e.g., KBGAN (Cai & Wang, 2017)). In particular, there ar |
| RESCAL | ✅ oui | representations. The typical models include RESCAL (Nickel et al., 2011), DistMult (Yang et al. |
| RotatE | ✅ oui | lar observations on NoiGAN-TransE and NoiGAN-RotatE, we only report the experimental results w.r |
| TransE | ✅ oui | r a translation carried out by the relation. TransE (Bordes et al., 2013), TransH (Wang et al., |
| TransH | ✅ oui | the relation. TransE (Bordes et al., 2013), TransH (Wang et al., 2014) and TransR (Lin et al., |
| TransR | ✅ oui | t al., 2013), TransH (Wang et al., 2014) and TransR (Lin et al., 2015) are the representative ap |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | : NOISE AWARE KNOWLEDGE GRAPH EMBEDDING WITH GAN **Anonymous authors** Paper under double-bl |
| HAN | eads to the poor generalization performance (Han et al., 2018). Specifically, we take top 10% |
| MLP | $\mathcal{N}(h, r, t)$. In particular, this MLP uses ReLU as the activation function for the |
| RatE | NoiGAN becomes more significant as the noise rate in KGs rises. This further proves the robust |
| SimplE | ment both discriminator and the generator as simple two-layer fully connected neural networks. T |
| TaKE | . During the training, noise-aware KGE model takes the confidence score learned by GAN as guida |
| Unstructured | cting information as the form of triple from unstructured text using information extraction systems. E |
