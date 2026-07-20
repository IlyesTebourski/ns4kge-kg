# Validation — BatchNS.md

**Titre extrait :** PyTorch-BigGraph: A Large-scale Graph Embedding System

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 18 |
| Extraites NON trouvees (FP -> erreur precision) | 5 |
| **Precision** | **78.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **52.9%** |

## Datasets  —  precision 100% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k | ✅ oui | s based on the validation split. Results for FB15k are reported on the separate test split. Al |
| LiveJournal | ✅ oui | ing System We evaluate PBG on the Freebase, LiveJournal and YouTube graphs and show that it matches |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Alibaba | ., 2015). The graph of users and products at Alibaba also consists of more than one billion users |
| Arxiv | arXiv:1903.12287v3 [cs.LG] 9 Apr 2019 # PYTORCH-B |
| Wikipedia | h that contains general facts extracted from Wikipedia, etc. The FB15k dataset consists of a subset |
| Youtube | valuate PBG on the Freebase, LiveJournal and YouTube graphs and show that it matches the performa |

## Metrics  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | <th>MRR</th> <th>MR</th> <th>Hits@10</th> <th>Memory</th> </tr> </t |
| MR | ✅ oui | Metric</th> <th>MRR</th> <th>MR</th> <th>Hits@10</th> <th>Me |
| MRR | ✅ oui | <tr> <th>Metric</th> <th>MRR</th> <th>MR</th> <th>Hits@10 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | ddings have nearly identical link prediction accuracy after 10 epochs of training with and without |
| F1 | r> <th>Metric</th> <th>Micro-F1</th> <th>Macro-F1</th> </tr> < |
| Hits@1 | n that we find that models can achieve > 50% hit@1 against 10,000 uniformly-sampled negatives, |

## NS Methods  —  precision 67% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Batched Negative Sampling | ✅ oui | an SGD. <sup>5</sup>In fact, our approach to batched negative sampling, described in Section 4.3 reduces the number |
| Uniform Negative Sampling | ✅ oui | 1 billion users vs. 1 million products. With uniform negative sampling over all nodes, the loss would be dominated |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | mbeddings for featurized nodes. * Efficient negative sampling for nodes that samples negative nodes both u |
| Uniform Sampling | 1 billion users vs. 1 million products. With uniform negative sampling over all nodes, the loss would be dominated |

## KGE Models  —  precision 73% · recall~ 61%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | lude linear transformation, translation, and complex multiplication. This combination of scoring |
| DeepWalk | ✅ oui | r> </thead> <tbody> <tr> <td>DeepWalk*</td> <td>0.691</td> <td>234 |
| DistMult | ✅ oui | lation operators allows PBG to train RESCAL, DistMult, TransE, and ComplEx models (Nickel et al., |
| HolE | ✅ oui | td>0.749</td> </tr> <tr> <td>HolE (Nickel et al., 2016b)</td> <td>0.23 |
| MILE (1 level) | ❌ NON | _(absent du texte)_ |
| MILE (5 levels) | ❌ NON | _(absent du texte)_ |
| PBG | ✅ oui | edding systems. We present PyTorch-BigGraph (PBG), an embedding system that incorporates seve |
| PBG (ComplEx) | ❌ NON | _(absent du texte)_ |
| PBG (TransE) | ❌ NON | _(absent du texte)_ |
| R-GCN+ | ✅ oui | td>0.840</td> </tr> <tr> <td>R-GCN+ (Schlichtkrull et al., 2018)</td> < |
| Reciprocal ComplEx-N3 | ✅ oui | td>0.838</td> </tr> <tr> <td>Reciprocal ComplEx-N3 (Lacroix et al., 2018)</td> <td>-</t |
| RESCAL | ✅ oui | s and relation operators allows PBG to train RESCAL, DistMult, TransE, and ComplEx models (Nicke |
| StarSpace | ✅ oui | td>0.842</td> </tr> <tr> <td>StarSpace (Wu et al., 2018)</td> <td>-</td> |
| TransE | ✅ oui | rators allows PBG to train RESCAL, DistMult, TransE, and ComplEx models (Nickel et al., 2011; Ya |
| word2vec | ✅ oui | gh in this literature are algorithms such as word2vec which allowed word embedding methods to scal |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GCN | ng et al., 2018). The problem studied by the GCN is different than the one solved by PBG (mos |
| RatE | best results from a grid search of learning rates from $0.001 - 0.1$, margins from $0.05 - 0.2 |
| SimplE | É., and Bouchard, G. Complex embeddings for simple link prediction. In *International Conferenc |
| Structured Embedding | , Collobert, R., Bengio, Y., et al. Learning structured embeddings of knowledge bases. In *AAAI*, volume 6, pp. |
| Structured Embeddings | , Collobert, R., Bengio, Y., et al. Learning structured embeddings of knowledge bases. In *AAAI*, volume 6, pp. |
| TaKE | e negative examples. In a typical setup, PBG takes a batch of $B = 1000$ positive edges from th |
| Tucker | Q. V., Mao, M. Z., Ranzato, M., Senior, A., Tucker, P., Yang, K., and Ng, A. Y. Large scale dis |
