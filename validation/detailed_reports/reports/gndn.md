# Validation — GNDN.md

**Titre extrait :** A generative adversarial network for single and multi-hop distributional knowledge base completion

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 20 |
| Extraites NON trouvees (FP -> erreur precision) | 7 |
| **Precision** | **74.1%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **55.6%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | ype_of, part_of and has_part, etc. Freebase (FB15k) consists of predicates from the personal ID |
| WN18 | ✅ oui | n with the baseline studies [8–14]. Wordnet (WN18) is a collection of pairs of English diction |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | r learning and inference in knowledge bases, arXiv preprint arXiv:1412.6575, 2014.. [11] B. Sh |

## Metrics  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | as $(h, p, t) \geqslant T_R$. Classification accuracy is used to evaluate the performance of predi |
| Hits@10 | ✅ oui | on and belief prediction tasks using MRR and HIT@ 10, achieving best-in-class performance. © 202 |
| MRR | ✅ oui | prediction and belief prediction tasks using MRR and HIT@ 10, achieving best-in-class perform |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | iously alluded to, we shall employ an RNN to map the input sequence of relations $(r_1, \ r_2 |

## NS Methods  —  precision 75% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| KBGAN | ✅ oui | s hence a significant difference between the KBGAN model of [19] and KCGAN as proposed here; wh |
| Knowledge Completion GAN | ✅ oui | mulated by the GAN concept, we thus propose *Knowledge Completion GAN* (KCGAN), a novel framework leveraging both |
| Random Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ✅ oui | le communities for training because they are unknown beforehand [49]. To overcome the challenge, |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | o key challenges are addressed: 1) Classical GAN architectures’ inability to easily generate |
| Negative Sampling | native models that require both positive and negative samples to learn a decision boundary. KBs, by contra |

## KGE Models  —  precision 67% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ConvE | ✅ oui | interactions between entities and relations. ConvE [25] adopts a 2D-CNN to integrate entities a |
| ConvKB | ✅ oui | e ConvE, which models relationships locally, ConvKB [12] adopts a transitional modeling paradigm |
| DistMult | ✅ oui | entations over entities and relations, and a DistMult based decoder for factorization. The GCNs us |
| ELECTRA | ✅ oui | f a recently developed language model called ELECTRA [37], which is a compute-efficient GAN-based |
| HypER | ✅ oui | paradigm and reports better overall results. HypER [26] uses a 1D-relation-specific convolution |
| KCGAN | ✅ oui | novel framework, Knowledge Completion GANs (KCGANs), for competitively training generative link |
| KG-BERT | ✅ oui | ry transformer-based encoding models such as KG-BERT [35] are inspired by transformer-based langu |
| Knowledge Completion GAN | ✅ oui | mulated by the GAN concept, we thus propose *Knowledge Completion GAN* (KCGAN), a novel framework leveraging both |
| NTN | ✅ oui | ncoding models is the neural tensor network (NTN), in which interaction between entities is m |
| Path-KCGAN [2 hop] | ❌ NON | _(absent du texte)_ |
| Path-KCGAN [3 hop] | ❌ NON | _(absent du texte)_ |
| PathG-RNN [2 hop] | ❌ NON | _(absent du texte)_ |
| PathG-RNN [3 hop] | ❌ NON | _(absent du texte)_ |
| PTransE | ✅ oui | referred as PathG-RNNs. We also compare with PTransE which is a variant of TransE for integrating |
| PTransE [2 hop] | ❌ NON | _(absent du texte)_ |
| PTransE [3 hop] | ❌ NON | _(absent du texte)_ |
| TransE | ✅ oui | o compare with PTransE which is a variant of TransE for integrating relation paths for knowledge |
| TransG | ✅ oui | recently developed related methods including TransG [16] and ConvKB [12]. KCGAN results depict t |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | s not rely on a heavy-weight multi-head self-attention mechanism, it is significantly more compute- |
| BERT | transformer-based encoding models such as KG-BERT [35] are inspired by transformer-based langu |
| GAN | o key challenges are addressed: 1) Classical GAN architectures’ inability to easily generate |
| GCN | l consists of a Convolutional Graph Network (GCN) [39] based encoder for learning representat |
| GraphGAN | istics, vol. 1, 2016.. [17] H. Wang et al., Graphgan: Graph representation learning with generati |
| HAN | 2018.. [26] Chunhong Zhang, Miao Zhou, Xiao Han, Hu. Zheng, Yang Ji, Knowledge graph embeddi |
| LINE | ntation learning approach. The most relevant line of research to our work is consequently the |
| Neural Tensor Network | approach in NN-based encoding models is the neural tensor network (NTN), in which interaction between entities |
| Neural Tensor Networks | 11–33. [8] R. Socher et al., Reasoning with neural tensor networks for knowledge base completion, In Advances i |
| ProjE | :1412.6575, 2014.. [11] B. Shi, and W. Tim, ProjE: Embedding projection for knowledge graph co |
| SimplE | ttleneck of softmax [60,61], we here adopt a simple and effective approach known as independent |
| TaKE | ry different perspectives, it is possible to take a broader perspective on representation lear |
