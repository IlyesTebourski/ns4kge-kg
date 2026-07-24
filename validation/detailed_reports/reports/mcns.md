# Validation — MCNS.md

**Titre extrait :** Understanding Negative Sampling in Graph Representation Learning

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 25 |
| Extraites NON trouvees (FP -> erreur precision) | 0 |
| **Precision** | **100.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 27 |
| **Recall relatif (indicatif, a valider)** | **48.1%** |

## Datasets  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Alibaba | ✅ oui | inghua University <sup>‡</sup> DAMO Academy, Alibaba Group zheny2751@gmail.com, dm18@mails.tsing |
| Amazon | ✅ oui | <td>/</td> </tr> <tr> <td>Amazon</td> <td>255,404</td> <td>1, |
| Arxiv | ✅ oui | arXiv:2005.09863v2 [cs.LG] 25 Jun 2020 # Understa |
| BlogCatalog | ✅ oui | <td>Node Classification</td> <td>BlogCatalog</td> <td>10,312</td> <td>333 |
| MovieLens | ✅ oui | rowspan="3">Recommendation</td> <td>MovieLens</td> <td>2,625</td> <td>100, |

_Aucun candidat faux negatif pour cette categorie._

## Metrics  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AUC | ✅ oui | > <tbody> <tr> <td rowspan="9">AUC</td> <td>$Deg^{0.75}$</td> < |
| F1 | ✅ oui | talog dataset. Table 4 summarizes the Micro-F1 result on the BlogCatalog dataset. MCNS stab |
| Hits@30 | ✅ oui | > </tr> <tr> <td rowspan="9">Hits@30</td> <td>$Deg^{0.75}$</td> < |
| MRR | ✅ oui | , *Hits@k* [7] and mean reciprocal ranking (*MRR*) [30] serve as evaluation methodologies, wh |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | ch as recommendation or link prediction. **(Accuracy)** From the perspective of risk, we mainly c |
| Hits@10 | lability. Similar trends hold for Hits@5 and Hits@10. <table> <thead> <tr> <th>Al |
| Hits@5 | limited scalability. Similar trends hold for Hits@5 and Hits@10. <table> <thead> <tr> |
| NDCG | tr> <th>β</th> <th>MovieLens NDCG</th> <th>Amazon NDCG</th> <t |

## NS Methods  —  precision 100% · recall~ 45%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bayesian Personalized Ranking | ✅ oui | been studied extensively in recommendation. Bayesian Personalized Ranking [29] proposes uniform sampling for negative |
| Dynamic Negative Sampling | ✅ oui | uniform sampling for negative samples. Then, dynamic negative sampling (DNS) [41] is proposed to sample informativ |
| IRGAN | ✅ oui | GE [40]). * **GAN-based Negative Sampling.** IRGAN [35] trains generative adversarial nets (GAN |
| KBGAN | ✅ oui | o adaptively generate hard negative samples. KBGAN [3] employs a sampling-based adaptation of I |
| Markov chain Monte Carlo Negative Sampling | ✅ oui | e and scalable negative sampling strategy, **Markov chain Monte Carlo Negative Sampling** (MCNS), which applies our theory with an a |
| PinSAGE | ✅ oui | ng-max (DNS [41]) and personalized PageRank (PinSAGE [40]). * **GAN-based Negative Sampling.** IR |
| Power of Degree | ✅ oui | ampling distribution proportional to the 3/4 power of degree by tuning the power parameter. Most later wo |
| Random Negative Sampling | ✅ oui | negative sampling schemes, including Uniform Random Sampling (RNS), Item-Oriented Sampling (ItemPop), Use |
| Weighted Approximate-Rank Pairwise | ✅ oui | K hard negative items. * **WARP** [38, 44]. Weighted Approximate-Rank Pairwise (WARP) utilizes SGD and a novel sampling tri |
| Weighted Regularized Matrix Factorization | ✅ oui | setting as a baseline. * **WRMF** [15, 26]. Weighted Regularized Matrix Factorization is an implicit MF model, which adapts a weig |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | on retrieval models. The generator generates adversarial negative samples to fool the discriminator while the discrimi |
| GAN | olution layers [17] to attention-based [34], GAN-based [8], sampled aggregator [13] and WL ke |
| GAN-based Negative Sampling | nd personalized PageRank (PinSAGE [40]). * **GAN-based Negative Sampling.** IRGAN [35] trains generative adversarial |
| Importance Sampling | eceptive field expansion. FastGCN [5] adopts importance sampling in each layer. **Negative Sampling.** Nega |
| Negative Sampling | 09863v2 [cs.LG] 25 Jun 2020 # Understanding Negative Sampling in Graph Representation Learning Zhen Yang< |
| Noise contrastive estimation | on learning can be unified within a *Sampled Noise Contrastive Estimation* (SampledNCE) framework (§ 2), comprising of |
| NSCaching | nming Yao, Yingxia Shao, and Lei Chen. 2019. NSCaching: Simple and Efficient Negative Sampling for |
| Random Sampling | negative sampling schemes, including Uniform Random Sampling (RNS), Item-Oriented Sampling (ItemPop), Use |
| Uniform Negative Sampling | rgence rate. Our q(y\|x) is defined by mixing uniform sampling and sampling from the nearest k nodes with 1 |
| Uniform Random Negative Sampling | s three negative sampling schemes, including Uniform Random Sampling (RNS), Item-Oriented Sampling (ItemPop), Use |
| Uniform Random Sampling | s three negative sampling schemes, including Uniform Random Sampling (RNS), Item-Oriented Sampling (ItemPop), Use |
| Uniform Sampling | rgence rate. Our q(y\|x) is defined by mixing uniform sampling and sampling from the nearest k nodes with 1 |

## KGE Models  —  precision 100% · recall~ 35%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DeepWalk | ✅ oui | traditional Network Embedding methods (e.g. DeepWalk [27], LINE [32]) and Graph Neural Networks ( |
| FastGCN | ✅ oui | to alleviate the receptive field expansion. FastGCN [5] adopts importance sampling in each layer |
| GCN | ✅ oui | , LINE [32]) and Graph Neural Networks (e.g. GCN [17], GraphSAGE [13]), although the latter s |
| GraphSAGE | ✅ oui | ]) and Graph Neural Networks (e.g. GCN [17], GraphSAGE [13]), although the latter sometimes are tra |
| LINE | ✅ oui | twork Embedding methods (e.g. DeepWalk [27], LINE [32]) and Graph Neural Networks (e.g. GCN [1 |
| node2vec | ✅ oui | rithms, such as DeepWalk [27], LINE [32] and node2vec [11], actually assign each node two embeddin |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | from basic graph convolution layers [17] to attention-based [34], GAN-based [8], sampled aggregato |
| ComplEx | ge graph embedding by relational rotation in complex space. *arXiv preprint arXiv:1902.10197* (20 |
| GAN | olution layers [17] to attention-based [34], GAN-based [8], sampled aggregator [13] and WL ke |
| HAN | NIPS'14*. 2177–2185. [20] Qimai Li, Zhichao Han, and Xiao-Ming Wu. 2018. Deeper insights int |
| MEI | ngzhe Wang, Ming Zhang, Jun Yan, and Qiaozhu Mei. 2015. Line: Large-scale information network |
| Random Walk | ia to sample positive node pairs, such as by random walk [27], the second-order proximity [32], commu |
| RatE | sal distribution also influences convergence rate. Our q(y\|x) is defined by mixing uniform sam |
| RotatE | ong Deng, Jian-Yun Nie, and Jian Tang. 2019. Rotate: Knowledge graph embedding by relational rot |
| SimplE | ned embedding deviates from the optimum). A simple solution is to sample negative nodes positiv |
| TaKE | er> <sup>2</sup>For bipartite graphs, always take nodes from V part as central node and sample |
| word2vec | d distribution to accelerate the training of word2vec. Mikolov et al. [24] set the negative sampli |
