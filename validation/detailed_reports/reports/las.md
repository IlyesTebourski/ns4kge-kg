# Validation — LAS.md

**Titre extrait :** Adversarial Knowledge Representation Learning without External Model

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 42 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **95.5%** |
| Candidats faux negatifs (dans le texte, non extraits) | 25 |
| **Recall relatif (indicatif, a valider)** | **62.7%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k237 | ✅ oui | GURE 1. Ratio of zero loss cases in training FB15k237 by TransE with uniform random negative tripl |
| WN18 | ✅ oui | s are conducted on three datasets, FB15k237, WN18 and WN18RR. FB15k237 is a difficult subset o |
| WN18RR | ✅ oui | er state-of-the-art models over FB15k237 and WN18RR. 2) Second, we verify the reward is necessa |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| FB15k | nd WN18RR. FB15k237 is a difficult subset of FB15k which inverse relations are removed [23], wh |
| Table 1 Dataset | e statistics of them are listed in Table 1. TABLE 1. Dataset statistics. <table> <thead> <tr> |
| Wikipedia | , multilingual knowledge base extracted from wikipedia," Semantic Web J., vol. 6, no. 2, pp. 167–19 |

## Metrics  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | reciprocal rank of the correct entities. 3) Hits@10 (H@10), the proportion of the correct entiti |
| MR | ✅ oui | edge representation learning: 1) Mean Rank (MR), the mean rank of the correct entities. 2) |
| MRR | ✅ oui | rrect entities. 2) Mean Reciprocal Ranking (MRR), the mean value of reciprocal rank of the c |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | r the ComplEx model, and a trade-off between accuracy and training time are also considered in [20 |

## NS Methods  —  precision 82% · recall~ 39%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Domain Sampling | ✅ oui | diction tasks. Furthermore, [16] proposes a "domain sampling" mechanism to define a Bernoulli distributio |
| GAN-pretrain | ✅ oui | roaches, such as KBGAN [25] and GAN-scratch (GAN-pretrain) [24], have been proposed. In these approach |
| GAN-scratch | ✅ oui | sampling approaches, such as KBGAN [25] and GAN-scratch (GAN-pretrain) [24], have been proposed. In |
| KBGAN | ✅ oui | proach outperforms GAN-based sampling method KBGAN. **INDEX TERMS** Knowledge graph, knowledge |
| Loss Adaptive Sampling | ✅ oui | ial knowledge representation learning, named loss adaptive sampling (LAS) mechanism, which is efficient without |
| Near-miss Sampling | ✅ oui | discriminator, and it can be regarded as the near miss sampling in [26]. In this part of experiments, we use |
| Nearest-neighbour Sampling | ✅ oui | n [26], the static negative sampling models, nearest-neighbour sampling and near-miss sampling, are proposed for neg |
| Type-constrained Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Random Negative Sampling | ✅ oui | ative sampling models by comparing them with uniform random sampling approach. In this paper, we exploit the los |
| Unknown | ✅ oui | candidate set on account of compute cost and unknown false negative cases. ## B. OVER-TRAINED FA |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adaptive Negative Sampling | nowledge representation learning, named loss adaptive sampling (LAS) mechanism, which is efficient without |
| Adversarial Negative Sampling | . In this paper, LAS is a simple but strong adversarial negative sampling approach without an external sampling model. |
| Domain-based Negative Sampling | diction tasks. Furthermore, [16] proposes a "domain sampling" mechanism to define a Bernoulli distributio |
| GAN | representation learning approach outperforms GAN-based sampling method KBGAN. **INDEX TERMS* |
| GAN-based Negative Sampling | representation learning approach outperforms GAN-based sampling method KBGAN. **INDEX TERMS** Knowledge gra |
| Kbgan Sampling | -.->\|Reward\| B ``` FIGURE 3. An overview of KBGAN negative sampling framework. In the training stage, the gener |
| Local Closed-World Assumption | e the filtering by this restriction. Unlike local closed-world assumption in [37] and [16], we consider the domain of |
| Negative Sampling | this paper, we introduce a simple but strong negative sampling approach for adversarial knowledge represent |
| Random Negative Sampling | oes on, as is illustrated in Figure 1. Thus, random negative sampling would cause very slow convergence and even f |
| Random Sampling | oes on, as is illustrated in Figure 1. Thus, random negative sampling would cause very slow convergence and even f |
| Static Sampling | h LAS get competitive results. In [26], the static negative sampling models, nearest-neighbour sampling and near- |
| Uniform Negative Sampling | lets by gradient descent of loss, but unlike uniform sampling, LAS sample corrupted triplets with differen |
| Uniform Random Sampling | ative sampling models by comparing them with uniform random sampling approach. In this paper, we exploit the los |
| Uniform Sampling | lets by gradient descent of loss, but unlike uniform sampling, LAS sample corrupted triplets with differen |

## KGE Models  —  precision 100% · recall~ 79%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ANALOGY | ✅ oui | r probability-based models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good resul |
| ComplEx | ✅ oui | e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx [20], and ConvE [23] etc), are another group |
| ConvE | ✅ oui | DistMult [18], HolE [19], ComplEx [20], and ConvE [23] etc), are another group of efficient em |
| DistMult | ✅ oui | Probability-based models (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx [20], and ConvE [23 |
| DKRL | ✅ oui | E [32] exploit relation paths, TEKE [33] and DKRL [34] embed knowledge graph with textual info |
| HolE | ✅ oui | ed models (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx [20], and ConvE [23] etc), are |
| ITransF | ✅ oui | ransG [13], STransE [14], puTransE [15], and ITransF [16]) define an energy function according to |
| KALE | ✅ oui | ed knowledge graph with textual information, KALE [35] and RUGE [36] utilize logical rules. I |
| KG2E | ✅ oui | nsE [6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [ |
| ProjE | ✅ oui | . Many other probability-based models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achi |
| PTransE | ✅ oui | [29] and TKRL [30] consider the entity type, PTransE [31] and RTransE [32] exploit relation paths |
| puTransE | ✅ oui | TranSparse [12], TransG [13], STransE [14], puTransE [15], and ITransF [16]) define an energy fun |
| R-GCN | ✅ oui | ed models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good results for link pre |
| RESCAL | ✅ oui | ased models Probability-based models (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx [20] |
| RTransE | ✅ oui | ] consider the entity type, PTransE [31] and RTransE [32] exploit relation paths, TEKE [33] and D |
| RUGE | ✅ oui | raph with textual information, KALE [35] and RUGE [36] utilize logical rules. In this paper, |
| SSE | ✅ oui | on to further improve the task. For example, SSE [29] and TKRL [30] consider the entity type, |
| STransE | ✅ oui | , TransA [11], TranSparse [12], TransG [13], STransE [14], puTransE [15], and ITransF [16]) defin |
| TEKE | ✅ oui | 31] and RTransE [32] exploit relation paths, TEKE [33] and DKRL [34] embed knowledge graph wit |
| TKRL | ✅ oui | improve the task. For example, SSE [29] and TKRL [30] consider the entity type, PTransE [31] |
| TransA | ✅ oui | ansH [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STransE |
| TransD* | ✅ oui | s (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12] |
| TransE | ✅ oui | on, since the first translation-based model (TransE [6]) proposed. Currently, translation-based |
| TransG | ✅ oui | 9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STransE [14], puTransE [15], and ITran |
| TransH | ✅ oui | translation-based models (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], Tran |
| TranSparse | ✅ oui | nsR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STransE [14], puTransE [1 |
| TransR | ✅ oui | -based models (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11], Tra |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | dge representation learning has gained great attention, since the first translation-based model (Tr |
| GAN | representation learning approach outperforms GAN-based sampling method KBGAN. **INDEX TERMS* |
| GCN | models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good results for link pre |
| HypER | by projecting entities on relation-specific hyper-planes. TransR [8] directly models entities |
| KBGAN | proach outperforms GAN-based sampling method KBGAN. **INDEX TERMS** Knowledge graph, knowledge |
| SimplE | se approaches. In this paper, we introduce a simple but strong negative sampling approach for ad |
| TaKE | nslation-based models, TransE and TransD, to take the role of discriminator $\mathbf{D}$. The |
