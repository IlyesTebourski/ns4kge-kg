# Validation — NMiss.md

**Titre extrait :** Analysis of the Impact of Negative Sampling on Link Prediction in Knowledge Graphs

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 0 |
| **Precision** | **100.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 13 |
| **Recall relatif (indicatif, a valider)** | **59.4%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k | ✅ oui | mplEx – and evaluate on benchmark datasets – FB15k and WN18. We compare well known methods for |
| WN18 | ✅ oui | d evaluate on benchmark datasets – FB15k and WN18. We compare well known methods for negative |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:1708.06816v2 [cs.AI] 2 Mar 2018 # Analysis |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | ct to the negative samples. For FB15k we use hits@10, for WN18, hits@1. <sup>4</sup>https://gith |
| MRR | ✅ oui | ink prediction on FB15k and WN18 in terms of MRR in Figures 3 and 4 for $n_s \in \{1, 2, 5, 1 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Hits@1 | samples. For FB15k we use hits@10, for WN18, hits@1. <sup>4</sup>https://github.com/bhushank/kg |

## NS Methods  —  precision 100% · recall~ 69%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Corrupting Positive Instances | ✅ oui | straints in the following sections. ### 3.2 Corrupting positive instances : C We use a method described in [24] that |
| Importance Sampling | ✅ oui | gative sampling was first proposed in [1] as importance sampling. A sampling solution that was more stable th |
| Near Miss Sampling | ✅ oui | est neighbor sampling for 5 epochs. ### 3.6 Near Miss sampling : nmiss The nearest neighbor sampler genera |
| Nearest Neighbor Sampling | ✅ oui | a number $n_s$ of negative samples. ### 3.5 Nearest Neighbor sampling : NN Most negative sampling methods generat |
| Noise Contrastive Estimation | ✅ oui | was introduced by [16], who built upon the noise-contrastive estimation [10]. In these approaches negative samples a |
| Random Sampling | ✅ oui | aph completion, or link prediction. ### 3.1 Random sampling : R The simplest form of sampling negative |
| Relational Sampling | ✅ oui | predetermined types as in Freebase. ### 3.4 Relational Sampling : REL Although typed or corrupt relation sa |
| Typed Sampling | ✅ oui | randomly produced negative samples. ### 3.3 Typed Sampling : T Knowledge graphs such as FreeBase and N |
| Unknown | ✅ oui | of the KG, some of these candidates could be unknown positives. If we assume that source target p |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Nearest-neighbour Sampling | istMult perform well with both near miss and nearest neighbour sampling on FB15k. Rescal performs best with near mis |
| Negative Sampling | .AI] 2 Mar 2018 # Analysis of the Impact of Negative Sampling on Link Prediction in Knowledge Graphs Bhus |
| Random Negative Sampling | aph completion, or link prediction. ### 3.1 Random sampling : R The simplest form of sampling negative |
| Typed Negative Sampling | randomly produced negative samples. ### 3.3 Typed Sampling : T Knowledge graphs such as FreeBase and N |

## KGE Models  —  precision 100% · recall~ 46%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | dding methods – RESCAL, TransE, DistMult and ComplEx – and evaluate on benchmark datasets – FB15k |
| DistMult | ✅ oui | ge graph embedding methods – RESCAL, TransE, DistMult and ComplEx – and evaluate on benchmark data |
| HolE | ✅ oui | rforms as well as the Holographic Embedding (HolE) model, so HolE was not included<sup>1</sup> |
| Neural Tensor Networks | ✅ oui | lations. Methods such as **Rescal** [21] and Neural Tensor Networks [24] learn millions of parameters that makes |
| RESCAL | ✅ oui | -the-art knowledge graph embedding methods – RESCAL, TransE, DistMult and ComplEx – and evaluate |
| TransE | ✅ oui | knowledge graph embedding methods – RESCAL, TransE, DistMult and ComplEx – and evaluate on benc |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | terns from the KG have received considerable attention. They learn a representation of the graph in |
| HypER | tive sampling model (pre-trained model) as a hyper parameter. We found that the RESCAL model wo |
| LINE | ngeles, California USA ![Small multiples of line charts showing link prediction performance o |
| Neural Tensor Network | lations. Methods such as **Rescal** [21] and Neural Tensor Networks [24] learn millions of parameters that makes |
| RatE | addresses the problem of decreasing learning rate in AdaGrad. We ensure that entity embeddings |
| SimplE | $O(N^2)$) far outnumber the correct ones. A simple solution to the scalability problem is rando |
| StAR | <td><em>film</em></td> <td><em>star_wars_episode_IV</em></td> <td><em>pr |
