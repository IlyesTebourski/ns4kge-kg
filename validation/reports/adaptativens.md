# Validation — AdaptativeNS.md

**Titre extrait :** Knowledge Graph Embedding via Adaptive Negative Subsampling

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 24 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **92.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 15 |
| **Recall relatif (indicatif, a valider)** | **61.5%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | ach on three commonly used datasets (WN18RR, FB15k-237, and YAGO3-10). The experimental results dem |
| WN18RR | ✅ oui | ur approach on three commonly used datasets (WN18RR, FB15k-237, and YAGO3-10). The experimental |
| YAGO3-10 | ✅ oui | mmonly used datasets (WN18RR, FB15k-237, and YAGO3-10). The experimental results demonstrate a sig |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| FB15k | ach on three commonly used datasets (WN18RR, FB15k-237, and YAGO3-10). The experimental results |
| Wikipedia | k. YAGO3: A knowledge base from multilingual wikipedias. In *CIDR*. www.cidrdb.org, 2015. [9] Tomas |
| WN18 | 18RR, FB15k-237, and YAGO3-10 are subsets of WN18 [3], FB15k [4], and YAGO3 [8], respectively. |

## Metrics  —  precision 75% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | onspicuously lags behind other models in the Hits@1 metric. This discrepancy suggests that the m |
| Hits@10 | ✅ oui | 10 dataset showing the best results. MRR and Hits@10, being the most commonly used evaluation met |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | ing. We utilize the mean reciprocal ranking (MRR) and the click-through rate (H@N) 41 Author |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | es for model training, thereby enhancing the accuracy and efficiency of knowledge graph representa |
| MAP | wledge graph representation learning aims to map entities and relationships from the knowledg |

## NS Methods  —  precision 80% · recall~ 57%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Adaptive Negative Sampling | ✅ oui | er classical models. In this study, we apply adaptive negative sampling to the classical knowledge graph embedding m |
| Adversarial Negative Sampling | ✅ oui | d patterns in the data. Another approach is adversarial negative sampling, where a discriminator network is trained to |
| Frequency-based Negative Sampling | ✅ oui | ormative negative samples [9]. For instance, frequency-based negative sampling considers the frequency distribution of enti |
| Random Negative Sampling | ✅ oui | formance, conventional methods have employed random negative sampling to augment the model's learning capabilities |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | cal models. In this study, we apply adaptive negative sampling to the classical knowledge graph embedding m |
| Random Sampling | formance, conventional methods have employed random negative sampling to augment the model's learning capabilities |
| Subsampling | wledge Graph Embedding via Adaptive Negative Subsampling Dong Zhu\*, Haonan Tan\*, Le Wang\*\u2021, |

## KGE Models  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | is approach enables a better modeling of the complex relationships between entities and relations |
| ConvE | ✅ oui | epresentation of entities and relationships. ConvE [4] is a convolutional neural network-based |
| DistMult | ✅ oui | ng upon the foundations laid by RESCAL, the DistMult [19] model was introduced. This bilinear mod |
| HAKE | ✅ oui | rsion relationships in knowledge graphs. The HAKE [20] model is designed for graph embedding, |
| MEI | ✅ oui | inherent intricacies of the knowledge graph. MEI [13] and MEIM [14] partition each embedding |
| MEIM | ✅ oui | icacies of the knowledge graph. MEI [13] and MEIM [14] partition each embedding into multiple |
| MuRP | ✅ oui | es. Some surface embedding methods, such as MuRP [1], embed knowledge graphs in curved spaces |
| RESCAL | ✅ oui | s expressed in vector space representations. RESCAL [10] introduced a tensor factorization appro |
| RotatE | ✅ oui | rmance hierarchical semantic embeddings. The RotatE [11] model is a knowledge graph embedding mo |
| TransD | ✅ oui | hips between entities and relationships. The TransD [18] model further improves upon TransR by d |
| TransE | ✅ oui | he classical knowledge graph embedding model transE. We have performed optimization on the loss |
| TransG | ✅ oui | ties and relationships more effectively. The TransG [17] model proposes a solution to the challe |
| TransH | ✅ oui | e-to-many and many-to-one relationships, the TransH [16] model extends it by introducing relatio |
| TransR | ✅ oui | overcomes the shortcomings of TransE. In the TransR [7] model, a relation mapping matrix is intr |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | aph completion, which has received extensive attention and research in recent years. However, some |
| HAN | I*, pages 1112–1119. AAAI Press, 2014. [17] Han Xiao, Minlie Huang, and Xiaoyan Zhu. Transg |
| LINE | ch pursuits. ## D. Impact of dimension The line charts in Figure 2 illustrate the performanc |
| RatE | or performance [9]. Furthermore, a learning rate decay method has been incorporated into the |
| SimplE | provement achieved by our method, enabling a simple model to achieve results close to the state- |
| TaKE | g methods have been developed. These methods take into account the characteristics of the know |
| Tucker | ns. Local interactions are modeled using the Tucker tensor format, while the complete interactio |
