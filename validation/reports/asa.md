# Validation — ASA.md

**Titre extrait :** Relation-aware Graph Attention Model With Adaptive Self-adversarial Training

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 23 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **92.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 18 |
| **Recall relatif (indicatif, a valider)** | **56.1%** |

## Datasets  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Amazon | ✅ oui | blished heterogeneous graph datasets, namely Amazon and Youtube (Cen et al. 2019) which come wit |
| Company | ✅ oui | etary enterprise heterogeneous graph dataset Company concerning buy/sell transactions. Company in |
| Youtube | ✅ oui | erogeneous graph datasets, namely Amazon and Youtube (Cen et al. 2019) which come with standard v |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | 2021 Feb 14 [cs.LG] arXiv:2102.07186v1 # Relation-aware Graph Attenti |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AP | ✅ oui | among all. RelGNN achieves the best AUC and AP on the benchmarks and has the best F1 as wel |
| AUC | ✅ oui | not such combination holds. We report micro AUC (area under the curve) of ROC (receiver oper |
| F1 | ✅ oui | RC (precision-recall curve) as well as micro F1 with a fixed cutoff threshold. Second, to ev |
| Hits@1 | ✅ oui | thods</th> <th>MRR↑</th> <th>Hit@1↑</th> <th>Hit@10↑</th> <th>H |
| Hits@10 | ✅ oui | RR↑</th> <th>Hit@1↑</th> <th>Hit@10↑</th> <th>Hit@30↑</th> </tr> < |
| Hits@30 | ✅ oui | 1↑</th> <th>Hit@10↑</th> <th>Hit@30↑</th> </tr> </thead> <tbody> <tr |
| MRR | ✅ oui | iques for model training, we report filtered MRR (mean reciprocal rank) and Hit@k. These rank |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 71% · recall~ 42%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Adaptive Self-Adversarial Negative Sampling | ✅ oui | learning with relation-aware attention* and *adaptive self-adversarial negative sampling* for model training. ## 1 Introduction Mod |
| ASA₅₀₀ | ✅ oui | pling technique – adaptive self-adversarial (ASA) negative sampling. ASA reduces the false ne |
| GAN-based Negative Sampling | ❌ NON | _(absent du texte)_ |
| NSCaching | ✅ oui | self-adversarial negative sampling method **NSCaching** as the baseline. It provides some flexibil |
| Random Negative Sampling | ✅ oui | ially for link/relationship prediction task. Random negative sampling has been widely adopted for its simplicity a |
| Self-adversarial Negative Sampling | ✅ oui | with relation-aware attention* and *adaptive self-adversarial negative sampling* for model training. ## 1 Introduction Mod |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | relation-aware attention* and *adaptive self-adversarial negative sampling* for model training. ## 1 Introduction Mod |
| GAN | al. 2019b). Generative adversarial network (GAN) based solutions (Cai and Wang 2018; Wang, L |
| KBGAN | /1806.01261. Cai, L.; and Wang, W. Y. 2018. KBGAN: Adversarial Learning for Knowledge Graph Em |
| Negative Sampling | erogeneous graph representation learning and negative sampling. Existing message passing-based graph neural |
| Noise contrastive estimation | ing methods can be unified within a *sampled noise contrastive estimation* framework (Yang et al. 2020b), especially f |
| Random Sampling | ially for link/relationship prediction task. Random negative sampling has been widely adopted for its simplicity a |
| Self-adversarial Sampling | with relation-aware attention* and *adaptive self-adversarial negative sampling* for model training. ## 1 Introduction Mod |

## KGE Models  —  precision 100% · recall~ 44%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | unction is defined as a bilinear function. **ComplEx** (Hayashi and Shimbo 2017) extends this ide |
| ConvE | ✅ oui | tities and relations into a complex space. **ConvE** (Dettmers et al. 2018) utilizes 2-D convol |
| DistMult | ✅ oui | function. In this paper, we define $d_r$ as DistMult (Yang et al. 2015) factorization which can b |
| GATNE | ✅ oui | meta-path to model higher order proximity. **GATNE** (Cen et al. 2019) learns multiple embeddin |
| HAN | ✅ oui | d aggregation function for each edge type. **HAN** (Wang et al. 2019) utilizes meta-path to m |
| metapath2vec | ✅ oui | against a popular random walk-based method **metapath2vec** (Dong, Chawla, and Swami 2017). It utilize |
| R-GCN | ✅ oui | by aggregating the neighbors' information. **R-GCN** (Schlichtkrull et al. 2018) considers the |
| RelGNN | ✅ oui | . To address these issues, first, we propose RelGNN— a message passing-based heterogeneous graph |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ] arXiv:2102.07186v1 # Relation-aware Graph Attention Model With Adaptive Self-adversarial Trainin |
| GAN | al. 2019b). Generative adversarial network (GAN) based solutions (Cai and Wang 2018; Wang, L |
| GCN | aggregating the neighbors' information. **R-GCN** (Schlichtkrull et al. 2018) considers the |
| KBGAN | /1806.01261. Cai, L.; and Wang, W. Y. 2018. KBGAN: Adversarial Learning for Knowledge Graph Em |
| LINE | e generally difficult to train. Recently, a line of research exploits the model itself (Sun e |
| MLP | re 1(1) consists of a multilayer perceptron (MLP) network to process categorical attribute in |
| Random Walk | In particular, we compare against a popular random walk-based method **metapath2vec** (Dong, Chawla, |
| RatE | ive sampling. ASA reduces the false negative rate by leveraging positive relationships to effe |
| RotatE | n, Z.; Deng, Z.; Nie, J.; and Tang, J. 2019. RotatE: Knowledge Graph Embedding by Relational Rot |
| SimplE | the heterogeneity of the graphs failing the simple uniform thresholding approaches (Ying et al. |
