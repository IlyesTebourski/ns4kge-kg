# Validation — RCWC.md

**Titre extrait :** KGBoost: A Classification-Based Knowledge Base Completion Method with Negative Sampling

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 20 |
| Extraites NON trouvees (FP -> erreur precision) | 8 |
| **Precision** | **71.4%** |
| Candidats faux negatifs (dans le texte, non extraits) | 12 |
| **Recall relatif (indicatif, a valider)** | **62.5%** |

## Datasets  —  precision 100% · recall~ 80%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | t al., 2013], WN18RR[Dettmers et al., 2018], FB15K[Bordes et al., 2013], FB15k-237[Toutanova an |
| FB15k-237 | ✅ oui | s et al., 2018], FB15K[Bordes et al., 2013], FB15k-237[Toutanova and Chen, 2015]. The statistics of |
| WN18 | ✅ oui | n four widely used link prediction datasets, WN18[Bordes et al., 2013], WN18RR[Dettmers et al. |
| WN18RR | ✅ oui | diction datasets, WN18[Bordes et al., 2013], WN18RR[Dettmers et al., 2018], FB15K[Bordes et al., |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2112.09340v1 [cs.LG] 17 Dec 2021 # KGBOOST: |

## Metrics  —  precision 40% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ❌ NON | _(absent du texte)_ |
| Hits@10 | ❌ NON | _(absent du texte)_ |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MR | ✅ oui | ion Metrics.** We evaluate the results using MR (Mean Rank), MRR (Mean Reciprocal Rank), and |
| MRR | ✅ oui | yper-parameters via grid search based on the MRR in the validation set with the following sea |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 29% · recall~ 25%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| GAN-based Negative Sampling | ✅ oui | _G(h', r, t')$, simultaneously. However, the GAN-based negative sample generator makes the original model more comp |
| Local-Closed World Assumption Negative Sampling | ❌ NON | _(absent du texte)_ |
| Naive Negative Sampling | ❌ NON | _(absent du texte)_ |
| Range-Constrained with Co-occurrence Negative Sampling | ❌ NON | _(absent du texte)_ |
| Self-Adversarial Negative Sampling | ✅ oui | and $p(h'_i, r, t'_i)$ is the coefficient in self-adversarial negative sampling [Sun et al., 2019]. ## 3.3 Training Relatio |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | p(h'_i, r, t'_i)$ is the coefficient in self-adversarial negative sampling [Sun et al., 2019]. ## 3.3 Training Relatio |
| GAN | _G(h', r, t')$, simultaneously. However, the GAN-based negative sample generator makes the or |
| KBGAN | 259, 2014. Liwei Cai and William Yang Wang. Kbgan: Adversarial learning for knowledge graph em |
| Local Closed-World Assumption | ompaß et al. [2015], where it was called the local-closed world assumption (LCWA). LCWA assumes that head and tail enti |
| Negative Sampling | -BASED KNOWLEDGE BASE COMPLETION METHOD WITH NEGATIVE SAMPLING **Yun-Cheng Wang** University of Southern C |
| Self-adversarial Sampling | and $p(h'_i, r, t'_i)$ is the coefficient in self-adversarial negative sampling [Sun et al., 2019]. ## 3.3 Training Relatio |

## KGE Models  —  precision 100% · recall~ 71%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | veness of embedding models, embedding in the complex space [Sun et al., 2019, Trouillon et al., 2 |
| ConvE | ✅ oui | l networks to increase model expressiveness. ConvE [Dettmers et al., 2018] predicts missing lin |
| DistMult | ✅ oui | instability caused by the relation matrices. DistMult [Yang et al., 2014] confines the relation ma |
| InteractE | ✅ oui | etworks over entity and relation embeddings. InteractE [Vashishth et al., 2020] improves the perfor |
| KGBoost-R | ✅ oui | with TransE as KGBoost-T and with RotatE as KGBoost-R. We assign an individual classifier to each |
| KGBoost-T | ✅ oui | and WN18RR. We denote KGBoost with TransE as KGBoost-T and with RotatE as KGBoost-R. We assign an i |
| RESCAL | ✅ oui | a matrix $M_r$ is used to model a relation. RESCAL [Nickel et al., 2011] suffers from model com |
| RotatE | ✅ oui | els such as TransE [Bordes et al., 2013] and RotatE [Sun et al., 2019] model relations as simple |
| SACN | ✅ oui | eature interactions in convolutional layers. SACN [Shang et al., 2019] adopts graph convolutio |
| TransE | ✅ oui | Motivation Some KG embedding models such as TransE [Bordes et al., 2013] and RotatE [Sun et al. |
| TransH | ✅ oui | since $r \approx 0$ for symmetric relations. TransH [Lin et al., 2015] and TransR [Lin et al., 2 |
| TransR | ✅ oui | ric relations. TransH [Lin et al., 2015] and TransR [Lin et al., 2015] model symmetric relations |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | _G(h', r, t')$, simultaneously. However, the GAN-based negative sample generator makes the or |
| HypER | **Training Details.** We determine optimal hyper-parameters via grid search based on the MRR |
| LINE | nd 2) effective negative samples. Along this line, we propose to incorporate inference pattern |
| RatE | * max depth: <u>3</u>, 5, 7, 10. * learning rate: 0.01, 0.05, **0.1**. Hyper-parameters to b |
| SimplE | RotatE [Sun et al., 2019] model relations as simple transformation from head entities to tail en |
