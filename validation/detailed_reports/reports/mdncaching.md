# Validation — MDNCaching.md

**Titre extrait :** MDNCaching: A Strategy to Generate Quality Negatives for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 16 |
| Extraites NON trouvees (FP -> erreur precision) | 0 |
| **Precision** | **100.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 19 |
| **Recall relatif (indicatif, a valider)** | **45.7%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K237 | ✅ oui | td>3,134</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <td>237 |
| WN18RR | ✅ oui | r> </thead> <tbody> <tr> <td>WN18RR</td> <td>93,003</td> <td>11< |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| FB15k | e-duplicate relations from previous WN18 and FB15K datasets respectively. The experiments were |
| WN18 | ng inverse-duplicate relations from previous WN18 and FB15K datasets respectively. The experim |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | atasets with substantial improvements (i.e., Hits@10 by 4.40% and 10.91% for WN18RR and FB15K237 |
| MR | ✅ oui | ed on the following metrics, 1. *Mean Rank (MR)* is the average of the obtained ranks; $MR |
| MRR | ✅ oui | nka and R. Ichise 2. *Mean Reciprocal Rank (MRR)* is the average of the inverse of the obtai |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 100% · recall~ 41%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | s have introduced various strategies such as Bernoulli negative sampling to generate quality negatives that are hard |
| IGAN | ✅ oui | rks (GAN) based negative sampling strategies IGAN [12] and KBGAN [3] were introduced to genera |
| KBGAN | ✅ oui | d negative sampling strategies IGAN [12] and KBGAN [3] were introduced to generate negatives wi |
| Matrix Decomposed Negative Caching | ✅ oui | introduces a new strategy called MDNCaching (Matrix Decomposed Negative Caching), which generates negatives considering the |
| NSCaching | ✅ oui | e possibility of generating false negatives. NSCaching [17] was proposed to overcome the challenges |
| Structure Aware Negative Sampling | ✅ oui | e-trained, which adds extra costs. Recently, Structure Aware Negative Sampling (SANS) [1] strategy was introduced with a di |
| Uniform Negative Sampling | ✅ oui | g the existing negative sampling strategies, Uniform negative sampling is a widely used strategy due to its simplic |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | s have introduced various strategies such as Bernoulli negative sampling to generate quality negatives that are hard |
| Confidence-Aware Negative Sampling | . Shan, Y., Bu, C., Liu, X., Ji, S., Li, L.: Confidence-aware negative sampling method for noisy knowledge graph embedding. |
| Dynamic Distribution Sampling | ampling space. The proposed MDNCaching is a dynamic distribution-based negative sampling strategy that integrates a matrix decomposit |
| Dynamic Negative Sampling | ng gradients and false negatives. Later, the dynamic negative sampling techniques were introduced to overcome the v |
| GAN | 17]. Hence, Generative adversarial networks (GAN) based negative sampling strategies IGAN [12 |
| Importance Sampling | milarity scores and updating the cache using importance sampling. Despite this, NSCaching may produce false n |
| MDNCaching | Check for updates](page_1_image_1_v2.jpg) # MDNCaching: A Strategy to Generate Quality Negatives fo |
| Negative Sampling | roduced various strategies such as Bernoulli negative sampling to generate quality negatives that are hard |
| SANS | Recently, Structure Aware Negative Sampling (SANS) [1] strategy was introduced with a differen |
| Uniform Sampling | g the existing negative sampling strategies, Uniform negative sampling is a widely used strategy due to its simplic |

## KGE Models  —  precision 100% · recall~ 36%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | ransE [2], 880 T. Madushanka and R. Ichise ComplEx [11] and DistMult [16] use Uniform negative |
| DistMult | ✅ oui | . Madushanka and R. Ichise ComplEx [11] and DistMult [16] use Uniform negative sampling to genera |
| TransD | ✅ oui | bb{R}^n$</td> </tr> <tr> <td>TransD [6]</td> <td>$\left\\|h + w_r w_h^\to |
| TransE | ✅ oui | its simplicity and efficiency. For example, TransE [2], 880 T. Madushanka and R. Ichise Compl |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | , Neural network approaches have also gained attention in recent research work that utilizes the po |
| GAN | 17]. Hence, Generative adversarial networks (GAN) based negative sampling strategies IGAN [12 |
| HypER | ion with Adam optimizer, and first, we tuned hyper-parameters referring to Bernoulli sampling s |
| KBGAN | d negative sampling strategies IGAN [12] and KBGAN [3] were introduced to generate negatives wi |
| Random Walk | l did not include. We consider SANS with the random walk configuration. <table> <thead> <tr> |
| RatE | ion $d \in \{50, 100, 250, 1000\}$, learning rate $\eta \in \{0.0005, 0.005, 0.05, 0.5\}$, mar |
| SimplE | er, E., Bouchard, G.: Complex embeddings for simple link prediction. In: Proceedings of Internat |
