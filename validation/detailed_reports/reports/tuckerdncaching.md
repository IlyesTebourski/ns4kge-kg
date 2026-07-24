# Validation — TuckerDNCaching.md

**Titre extrait :** TuckerDNCaching: high-quality negative sampling with tucker decomposition

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 27 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **93.1%** |
| Candidats faux negatifs (dans le texte, non extraits) | 22 |
| **Recall relatif (indicatif, a valider)** | **55.1%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | (Miller, 1995), WN18RR (Wang et al., 2019), FB15K (Bollacker et al., 2008) and FB15K237 (Touta |
| FB15K237 | ✅ oui | s the training continues with TransE for the FB15K237 dataset. This result shows that the fixed di |
| WN18 | ✅ oui | d on four standard benchmark datasets, i.e., WN18 (Miller, 1995), WN18RR (Wang et al., 2019), |
| WN18RR | ✅ oui | nchmark datasets, i.e., WN18 (Miller, 1995), WN18RR (Wang et al., 2019), FB15K (Bollacker et al. |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | for the positive (*panorama*, *profession*, *actor*) following NSCaching (Zhang et al., 2019). |
| FB13 | analyzed the negative candidates sampled for FB13 as the triplets are more intuitive than WN18 |

## Metrics  —  precision 100% · recall~ 83%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | d>23</td> </tr> </tbody> </table> (b) Hits@1 with TransE <table> <thead> <tr> |
| Hits@10 | ✅ oui | d>43</td> </tr> </tbody> </table> (c) Hits@10 with TransE <table> <thead> <tr> |
| Hits@3 | ✅ oui | ink prediction task considering MRR, Hits@1, Hits@3, and Hits@10 for the WN18RR and FB15K237 dat |
| MR | ✅ oui | sis of the following metrics. * *Mean Rank (MR)* is the average of the obtained ranks, $MR |
| MRR | ✅ oui | nk is widely used. * *Mean Reciprocal Rank (MRR)* is the average of the inverse of the obtai |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | stated challenges in negative sampling, (b) accuracy in latent relation modeling, and (c) accurac |

## NS Methods  —  precision 92% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | gative fact (*Michelangelo, Gender, Male*). Bernoulli negative sampling (Wang et al., 2014) is introduced with the i |
| Entity Similarity-based Negative Sampling | ✅ oui | ts with large gradients in head/tail caches. Entity Similarity-based Negative Sampling (ESNS) (Yao et al., 2022) considers semantic |
| ExtremeSelectCaching | ✅ oui | hing negative sampling method. We called it "ExtremeSelectCaching" as it evaluates the importance of all candi |
| IGAN | ✅ oui | ., 2014) for modeling dynamic distributions, IGAN (Wang et al., 2018) and KBGAN (Cai et al., 2 |
| KBGAN | ✅ oui | distributions, IGAN (Wang et al., 2018) and KBGAN (Cai et al., 2018) were introduced as negati |
| KSGAN | ✅ oui | ng the embedding model as the discriminator. KSGAN (Hu et al., 2019) is an extension of KBGAN, |
| MDNCaching | ✅ oui | pling method by extending the previous work, MDNCaching (Madushanka et al., 2022) by introducing a r |
| NSCaching | ✅ oui | . With the aim of generating hard negatives, NSCaching (Zhang et al., 2019) introduces an approach |
| Self-Adversarial Negative Sampling | ❌ NON | _(absent du texte)_ |
| Structure Aware Negative Sampling | ✅ oui | that ignores non-semantic similar neighbors, Structure Aware Negative Sampling (SANS) (Ahrabian et al., 2020) shows better |
| TuckerDNCaching | ✅ oui | Check for updates](page_1_image_1_v2.jpg) # TuckerDNCaching: high-quality negative sampling with tucker |
| Uniform Negative Sampling | ✅ oui | its simplicity and efficiency. For example, Uniform negative sampling (Bordes et al., 2013) which constructs negat |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | gative fact (*Michelangelo, Gender, Male*). Bernoulli negative sampling (Wang et al., 2014) is introduced with the i |
| Dynamic Distribution Sampling | tes the false negatives suffered in previous dynamic distribution-based negative sampling methods. (2) The Tucker decomposition techni |
| Dynamic Negative Sampling | scratch with fewer parameters than previous dynamic negative sampling methods IGAN, KBGAN, and KSGAN. Even though |
| ESNS | . Entity Similarity-based Negative Sampling (ESNS) (Yao et al., 2022) considers semantic simil |
| GAN | E training. Generative adversarial networks (GAN) and self-adversarial methods have recently |
| Knowledge Selective Adversarial Network | 164–189. Hu, K., Liu, H., Hao, T., (2019) A knowledge selective adversarial network for link prediction in knowledge graph. In: |
| Negative Sampling | e_1_v2.jpg) # TuckerDNCaching: high-quality negative sampling with tucker decomposition Tiroshan Madushan |
| Probabilistic Negative Sampling | 17) Enhancing knowledge graph embedding with probabilistic negative sampling. In: Proceedings of International Conference |
| SANS | eighbors, Structure Aware Negative Sampling (SANS) (Ahrabian et al., 2020) shows better perfor |
| Self-Adv | et al., 2019) introduced a self-adversarial *Self-Adv* sampling approach based on a self-scoring f |
| Uniform Sampling | its simplicity and efficiency. For example, Uniform negative sampling (Bordes et al., 2013) which constructs negat |

## KGE Models  —  precision 88% · recall~ 47%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | ed KGE models (DistMult (Yang et al., 2015), ComplEx (Trouillon et al., 2016)). The discriminator |
| DistMult | ✅ oui | e of two semantic matching-based KGE models (DistMult (Yang et al., 2015), ComplEx (Trouillon et a |
| RESCAL | ❌ NON | _(absent du texte)_ |
| RotatE | ✅ oui | ng which has an impact on efficiency. Later, RotatE (Sun et al., 2019) introduced a self-adversa |
| TorusE | ✅ oui | translational distance-based models, such as TorusE (Ebisu et al., 2018), by addressing the regu |
| TransD | ✅ oui | ed KGE models (TransE (Bordes et al., 2013), TransD (Ji et al., 2015)). By replacing the probabi |
| TransE | ✅ oui | by addressing the regularization problem of TransE and incorporating techniques such as adaptiv |
| TuckER | ✅ oui | Caching: high-quality negative sampling with tucker decomposition Tiroshan Madushanka<sup>1,2</ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | (Chenchen et al., 2019) and the use of self-attention and position-aware embeddings (Siheng et al. |
| GAN | E training. Generative adversarial networks (GAN) and self-adversarial methods have recently |
| HAN | 653/v1/N18-1133 Chenchen, G., Chunhong, Z., Han, X., et al. (2019). AWML: adaptive weighted |
| HypER | with the Adam optimizer. First, we adjusted hyper-parameters referring to the Bernoulli sampli |
| LINE | d KGE model, ($\theta_E$) are initialized in line-1. Reflecting the steps in Section 3.4.2, th |
| Random Walk | r KGE models. By selecting negatives using a random walk approach that ignores non-semantic similar n |
| RatE | ion $d \in \{50, 100, 250, 1000\}$, learning rate $\eta \in \{0.0005, 0.005, 0.05, 0.5\}$, and |
| SimplE | iedel S, et al (2016) Complex embeddings for simple link prediction. In: Proceedings of Internat |
