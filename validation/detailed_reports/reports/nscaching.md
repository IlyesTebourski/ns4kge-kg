# Validation — NSCaching.md

**Titre extrait :** NSCaching: Simple and Efficient Negative Sampling for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 26 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **89.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 24 |
| **Recall relatif (indicatif, a valider)** | **52.0%** |

## Datasets  —  precision 100% · recall~ 57%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | ts on four popular data sets, i.e., WN18 and FB15K, and their variants WN18RR and FB15K237. Exp |
| FB15K237 | ✅ oui | N18 and FB15K, and their variants WN18RR and FB15K237. Experimental results demonstrate that our m |
| WN18 | ✅ oui | experiments on four popular data sets, i.e., WN18 and FB15K, and their variants WN18RR and FB1 |
| WN18RR | ✅ oui | ts, i.e., WN18 and FB15K, and their variants WN18RR and FB15K237. Experimental results demonstra |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | datasets. We pick up (manorama, profession, actor) as the positive triplets, and the changes i |
| Arxiv | arXiv:1812.06410v2 [cs.AI] 18 Jan 2019 # NSCachin |
| FB13 | n Section III-C. Following [39], we also use FB13 here since its triplets are more interpretab |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | d according to maximizing the classification accuracy on the validation set. As shown in Table V, |
| Hits@10 | ✅ oui | hcal{S}\|\}$ is a set of ranking results; * Hit@10: It is the percentage of appearance in top-$ |
| MR | ✅ oui | )$ is the indicator function; * Mean rank (MR): It is computed by $\frac{1}{\|\mathcal{S}\|} |
| MRR | ✅ oui | owing metrics: * Mean reciprocal ranking (MRR): It is computed by average of the reciproca |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 67% · recall~ 35%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | performance. A better sampling scheme, i.e., Bernoulli sampling, is introduced in [42]. It improves uniform |
| IGAN | ✅ oui | cently, there are two pioneered works, i.e., IGAN [39] and KBGAN [9], attempting to address th |
| IGAN + scratch | ❌ NON | _(absent du texte)_ |
| KBGAN | ✅ oui | are two pioneered works, i.e., IGAN [39] and KBGAN [9], attempting to address these challenges. |
| KBGAN + scratch | ❌ NON | _(absent du texte)_ |
| NSCaching | ✅ oui | arXiv:1812.06410v2 [cs.AI] 18 Jan 2019 # NSCaching: Simple and Efficient Negative Sampling for |
| NSCaching + scratch | ❌ NON | _(absent du texte)_ |
| Self-paced GAN | ✅ oui | IGAN [39] and KBGAN [9] for KG embedding and self-paced GAN [12] for network embedding. # VI. CONCLUSIO |
| Uniform Negative Sampling | ✅ oui | tter. Due to its simplicity and efficiency, uniform sampling is broadly used in KG embedding [40]. Howeve |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | performance. A better sampling scheme, i.e., Bernoulli sampling, is introduced in [42]. It improves uniform |
| Cache-based Negative Sampling | vated to use a small amount of memory, which caches negative samples with large scores for each triplet in $\math |
| Dynamic Negative Sampling | though GAN provides a solution to model the dynamic negative sample distribution, it is famous for suffering fro |
| GAN | g. Recently, generative adversarial network (GAN), has been introduced in negative sampling. |
| Importance Sampling | negative triplets in cache, and then design importance sampling (IS) strategy to update the cache. The IS st |
| Negative Sampling | Jan 2019 # NSCaching: Simple and Efficient Negative Sampling for Knowledge Graph Embedding Yongqi Zhang< |
| Noise contrastive estimation | 77, 2017. [19] M. Gutmann and A. Hyvärinen. Noise-contrastive estimation: A new estimation principle for unnormalized |
| NSCaching Sampling | to sample negative triplets. Besides, since NSCaching samples negative triplets with larger scores, its gr |
| Random Negative Sampling | cache). These motivate us to use uniformly random sampling scheme in step 6. It is simple, efficient, a |
| Random Sampling | cache). These motivate us to use uniformly random sampling scheme in step 6. It is simple, efficient, a |
| Uniform Sampling | tter. Due to its simplicity and efficiency, uniform sampling is broadly used in KG embedding [40]. Howeve |

## KGE Models  —  precision 100% · recall~ 55%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ANALOGY | ✅ oui | 32], DistMult [46], HolE [31], ComplEx [38], ANALOGY [27], etc. All these methods are summarized |
| ComplEx | ✅ oui | ver, using GAN makes the original model more complex and hard to train, where reinforcement learn |
| DistMult | ✅ oui | simple and effective variants of RESCAL are DistMult [46], HolE [31] and ComplEx [38]. DistMult s |
| HolE | ✅ oui | ective variants of RESCAL are DistMult [46], HolE [31] and ComplEx [38]. DistMult simplifies R |
| ManifoldE | ✅ oui | , TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and semantic matching models RES |
| RESCAL | ✅ oui | re the plausibility of triplets $(h, r, t)$. RESCAL [32] is the most original model. The entity |
| TransD | ✅ oui | lem, variants like TransH [42], TransR [26], TransD [20] are introduced to project embeddings of |
| TransE | ✅ oui | presentative translational distance model is TransE [7]. Inspired from the word representation l |
| TransH | ✅ oui | tities. To solve this problem, variants like TransH [42], TransR [26], TransD [20] are introduce |
| TransM | ✅ oui | , TransR [26], TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and semantic mat |
| TranSparse | ✅ oui | [7], TransH [42], TransR [26], TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and |
| TransR | ✅ oui | lve this problem, variants like TransH [42], TransR [26], TransD [20] are introduced to project |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | Q. Song, H. Ge, J. Caverlee, and X. Hu. Self-attention generative adversarial networks. Technical r |
| GAN | g. Recently, generative adversarial network (GAN), has been introduced in negative sampling. |
| HypER | e comparison with state-of-the-arts methods. Hyper-parameters of *NSCaching* are studied in Sec |
| LINE | lets that satisfy $D \geq x$. The red dashed line shows where the margin $\gamma$ lies. (a) is |
| Node2vec | 2680, 2014. [17] A. Grover and J. Leskovec. node2vec: Scalable feature learning for networks. In |
| Random Walk | [25] N. Lao, T. Mitchell, and W. W. Cohen. Random walk inference and learning in a large scale know |
| RatE | nsion $d \in \{20, 50, 100, 200\}$, learning rate $\eta \in \{0.0001, 0.001, 0.01, 0.1\}$. For |
| SimplE | 12.06410v2 [cs.AI] 18 Jan 2019 # NSCaching: Simple and Efficient Negative Sampling for Knowledg |
| TaKE | fficiency of NSCaching. Furthermore, we also take good care of “exploration and exploitation”, |
| word2vec | 49–256, 2010. [15] Y. Goldberg and O. Levy. word2vec explained: deriving mikolov et al.’s negativ |
