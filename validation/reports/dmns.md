# Validation — DMNS.md

**Titre extrait :** Diffusion-based Negative Sampling on Graphs for Link Prediction

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 4 |
| **Precision** | **82.6%** |
| Candidats faux negatifs (dans le texte, non extraits) | 23 |
| **Recall relatif (indicatif, a valider)** | **45.2%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Actor | ✅ oui | ime steps on Cora, Citeseer, Coauthor-CS and Actor are 80.14%, 81.62%, 81.65% and 84.31%, respe |
| Citeseer | ✅ oui | aged over samples from 4 time steps on Cora, Citeseer, Coauthor-CS and Actor are 80.14%, 81.62%, 8 |
| Coauthor-CS | ✅ oui | samples from 4 time steps on Cora, Citeseer, Coauthor-CS and Actor are 80.14%, 81.62%, 81.65% and 84. |
| Cora | ✅ oui | $ averaged over samples from 4 time steps on Cora, Citeseer, Coauthor-CS and Actor are 80.14%, |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | 2024 Mar 25 [cs.LG] arXiv:2403.17259v1 # Diffusion-based Negative Sam |
| Wikipedia | nnects two actors both occurring on the same Wikipedia page. **Baselines.** We employ a comprehens |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| MAP | ✅ oui | /tr> <tr> <th> </th> <th>MAP</th> <th>NDCG</th> <th>MAP</ |
| NDCG | ✅ oui | <th> </th> <th>MAP</th> <th>NDCG</th> <th>MAP</th> <th>NDCG</ |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 50% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Conditional Diffusion-based Multi-level Negative Sampling | ✅ oui | ls from the latent space. Our method, called Conditional Diffusion-based Multi-level Negative Sampling (DMNS), leverages the Markov chain property |
| Dynamic Negative Sampling | ❌ NON | _(absent du texte)_ |
| Markov Chain Monte Carlo Negative Sampling | ❌ NON | _(absent du texte)_ |
| MixGCF | ✅ oui | egative examples from $k$-hop neighborhoods. MixGCF [20] synthesizes hard negative examples by h |
| Popularity-based Negative Sampling | ❌ NON | _(absent du texte)_ |
| Subgraph-based Negative Sampling | ✅ oui | SEAL by utilizing random walks for efficient subgraphs sampling. For other base GNN encoders, GAT [45] empl |
| Uniform Negative Sampling | ✅ oui | control the quality of negative nodes. While uniform negative sampling [14, 44] is simple, it ignores the quality o |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| DMNS | ffusion-based Multi-level Negative Sampling (DMNS), leverages the Markov chain property of dif |
| GAN | ularly in visual applications [8, 17]. While GAN-based models are successful in generating hi |
| KBGAN | tive sampling. Among them, GraphGAN [46] and KBGAN [5] learns a distribution over negative cand |
| Negative Sampling | cs.LG] arXiv:2403.17259v1 # Diffusion-based Negative Sampling on Graphs for Link Prediction Trung-Kien Ng |
| Noise contrastive estimation | ion learning methods [14, 44, 50] follow the noise contrastive estimation approach [13], which resorts to sampling a s |
| SANS | ecting high-variance samples [9]. On graphs, SANS [2] select negative examples from $k$-hop ne |
| Structure-Aware Negative Sampling | iam L Hamilton, and Avishek Joey Bose. 2020. Structure aware negative sampling in knowledge graphs. *arXiv preprint arXiv:2 |
| Uniform Sampling | control the quality of negative nodes. While uniform negative sampling [14, 44] is simple, it ignores the quality o |

## KGE Models  —  precision 100% · recall~ 41%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ARVGA | ✅ oui | nerative adversarial methods: GraphGAN [46], ARVGA [35] and \*Code & data at https://github.co |
| GAT | ✅ oui | r> </thead> <tbody> <tr> <td>GAT</td> <td>.766 ± .006</td> <t |
| GCN | ✅ oui | the complexity of DMNS for one node. Taking GCN as base encoder, the neighborhood aggregatio |
| GraphGAN | ✅ oui | for automatic negative sampling. Among them, GraphGAN [46] and KBGAN [5] learns a distribution ove |
| GVAE | ✅ oui | 4 ± .003</td> </tr> <tr> <td>GVAE</td> <td><u>.783 ± .003</u></td> |
| KBGAN | ✅ oui | tive sampling. Among them, GraphGAN [46] and KBGAN [5] learns a distribution over negative cand |
| SAGE | ✅ oui | /strong></td> </tr> <tr> <td>SAGE</td> <td>.598 ± .014</td> <t |
| ScaLed | ✅ oui | gamma$-decaying heuristic theory. Meanwhile, ScaLED [27] utilizes random walks to efficiently sa |
| SEAL | ✅ oui | ons of the enclosing subgraphs. For example, SEAL [53] proposes the usage of local subgraphs b |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ion function such as mean-pooling [23], self-attention [45] or concatenation [14], $\sigma$ is an a |
| ComplEx | an Lü and Tao Zhou. 2011. Link prediction in complex networks: A survey. *Physica A: statistical |
| GAN | ularly in visual applications [8, 17]. While GAN-based models are successful in generating hi |
| GraphSAGE | also conduct experiments using GAT [45] and GraphSAGE (SAGE) [14]. For GCN, we employ two layers w |
| LINE | oposed sub-linear positivity theory. Another line of research utilizes generative adversarial |
| MEI | ngzhe Wang, Ming Zhang, Jun Yan, and Qiaozhu Mei. 2015. Line: Large-scale information network |
| MLP | _h}})$, followed by a multilayer perceptron (MLP). $\tau(\cdot; \theta)$ is a learnable trans |
| Node2vec | [12] Aditya Grover and Jure Leskovec. 2016. node2vec: Scalable feature learning for networks. In |
| Random Walk | stic theory. Meanwhile, ScaLED [27] utilizes random walks to efficiently sample subgraphs for large-sc |
| RatE | diction. For our model DMNS, we set learning rate as 0.01, dropout ratio as 0.1. For each quer |
| SimplE | While uniform negative sampling [14, 44] is simple, it ignores the quality of negative examples |
| TaKE | ayer dimension. Thus, the diffusion training takes $N$ iterations has complexity $O(N L_1 L_2 d |
| word2vec | stic negative sampling*: PNS is adopted from word2vec [30], where the distribution for negative sa |
