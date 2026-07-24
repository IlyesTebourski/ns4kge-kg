# Validation — SelfAdv.md

**Titre extrait :** RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 27 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **90.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **62.8%** |

## Datasets  —  precision 100% · recall~ 80%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Countries S1 | ✅ oui | <td>6</td> </tr> <tr> <td>Countries S1</td> <td>500</td> <td>512</t |
| Countries S2 | ✅ oui | <td>0.1</td> </tr> <tr> <td>Countries S2</td> <td>500</td> <td>512</t |
| Countries S3 | ✅ oui | <td>0.1</td> </tr> <tr> <td>Countries S3</td> <td>500</td> <td>512</t |
| FB15k | ✅ oui | knowledge graph benchmark datasets including FB15k (Bordes et al., 2013), WN18 (Bordes et al., |
| FB15k-237 | ✅ oui | s et al., 2013), WN18 (Bordes et al., 2013), FB15k-237 (Toutanova (Toutanova & Chen, 2015) and WN1 |
| WN18 | ✅ oui | asets including FB15k (Bordes et al., 2013), WN18 (Bordes et al., 2013), FB15k-237 (Toutanova |
| WN18RR | ✅ oui | 237 (Toutanova (Toutanova & Chen, 2015) and WN18RR (Dettmers et al., 2017). Experimental result |
| YAGO3-10 | ✅ oui | : Results of several models evaluated on the YAGO3-10 datasets. Other results are taken from (Dett |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | al learning for knowledge graph embeddings. *arXiv preprint arXiv:1711.04071*, 2017. Rajarshi |
| Wikipedia | k. Yago3: A knowledge base from multilingual wikipedias. In *CIDR*, 2013. 11 Published as a confer |

## Metrics  —  precision 67% · recall~ 80%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AUC | ✅ oui | <th></th> <th colspan="4">Countries (AUC-PR)</th> </tr> <tr> <th></th> |
| Hits@1 | ❌ NON | _(absent du texte)_ |
| Hits@10 | ✅ oui | h> <th colspan="4"><b>Prediction Head (Hits@10)</b></th> <th colspan="4"><b>Predictio |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MR | ✅ oui | ts: $(h', r, t)$ or $(h, r, t')$. Mean Rank (MR), Mean Reciprocal Rank (MRR) and Hits at N ( |
| MRR | ✅ oui | t')$. Mean Rank (MR), Mean Reciprocal Rank (MRR) and Hits at N (H@N) are standard evaluation |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | n patterns. Inspired by Euler’s identity, we map the head and tail entities $h, t$ to the com |

## NS Methods  —  precision 75% · recall~ 43%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| KBGAN | ✅ oui | <td>.915</td> </tr> <tr> <td>KBGAN (Cai & Wang, 2017)</td> <td>.278</td> |
| Self-Adversarial Negative Sampling | ✅ oui | ector space. In addition, we propose a novel self-adversarial negative sampling technique for efficiently and effectively tr |
| Uniform Negative Sampling | ✅ oui | e negative triplets in a uniform way. Such a uniform negative sampling suffers the problem of inefficiency since ma |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | space. In addition, we propose a novel self-adversarial negative sampling technique for efficiently and effectively tr |
| Negative Sampling | ddition, we propose a novel self-adversarial negative sampling technique for efficiently and effectively tr |
| Self-adversarial Sampling | ector space. In addition, we propose a novel self-adversarial negative sampling technique for efficiently and effectively tr |
| Uniform Sampling | e negative triplets in a uniform way. Such a uniform negative sampling suffers the problem of inefficiency since ma |

## KGE Models  —  precision 100% · recall~ 57%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | GE GRAPH EMBEDDING BY RELATIONAL ROTATION IN COMPLEX SPACE **Zhiqing Sun**<sup>1*</sup>, **Zhi-H |
| ConvE | ✅ oui | r, t \in R^k$</td> </tr> <tr> <td>ConvE (Dettmers et al., 2017)</td> <td>$\lan |
| DistMult | ✅ oui | r, t \in R^k$</td> </tr> <tr> <td>DistMult (Yang et al., 2014)</td> <td>$\langle |
| HolE | ✅ oui | r, t \in C^k$</td> </tr> <tr> <td>HolE (Nickel et al., 2016)</td> <td>$\langl |
| KG2E | ✅ oui | <td>.672</td> </tr> <tr> <td>KG2E_KL (bern)</td> <td>.923</td> <td |
| pRotatE | ✅ oui | ase information. We refer to the baseline as pRotatE. It is obvious to see that pRotatE can also |
| RotatE | ✅ oui | lished as a conference paper at ICLR 2019 # ROTATE: KNOWLEDGE GRAPH EMBEDDING BY RELATIONAL ROT |
| STransE | ✅ oui | al., 2014), TransR (Lin et al., 2015b), and STransE (Nguyen et al., 2016), where $g_{r,i}(\cdot) |
| TorusE | ✅ oui | evant and concurrent work to our work is the TorusE (Ebisu & Ichise, 2018) model, which defines |
| TransE | ✅ oui | ^{k \times k}$</td> </tr> <tr> <td>TransE (Bordes et al., 2013)</td> <td>$-\\|h + |
| TransH | ✅ oui | s a wide range of TransE’s variants, such as TransH (Wang et al., 2014), TransR (Lin et al., 201 |
| TransR | ✅ oui | ariants, such as TransH (Wang et al., 2014), TransR (Lin et al., 2015b), and STransE (Nguyen et |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ion answering over knowledge base with cross-attention combining global knowledge. In *Proceedings |
| DAT | 62*, 2015. Dai Quoc Nguyen, Tu Dinh Nguyen, Dat Quoc Nguyen, and Dinh Phung. A novel embeddi |
| KBGAN | <td>.915</td> </tr> <tr> <td>KBGAN (Cai & Wang, 2017)</td> <td>.278</td> |
| Random Walk | Ni Lao, Tom Mitchell, and William W Cohen. Random walk inference and learning in a large scale know |
| SE | /tr> </thead> <tbody> <tr> <td>SE (Bordes et al., 2011)</td> <td>$-\\|W_{ |
| SimplE | i\| = 1. \tag{1} $$ It turns out that such a simple operation can effectively model all the thre |
| Structured Embedding | an Collobert, Yoshua Bengio, et al. Learning structured embeddings of knowledge bases. In *AAAI*, volume 6, pp. |
| Structured Embeddings | an Collobert, Yoshua Bengio, et al. Learning structured embeddings of knowledge bases. In *AAAI*, volume 6, pp. |
| TaKE | ented as vectors, the score function usually takes the form $f_r(h, t)$, where $h$ and $t$ are |
