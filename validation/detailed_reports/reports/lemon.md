# Validation — LEMON.md

**Titre extrait :** Language Model-driven Negative Sampling

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 17 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **85.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 20 |
| **Recall relatif (indicatif, a valider)** | **45.9%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| WN18 | ✅ oui | used two publicly available datasets, namely WN18, and WN18RR. Since our approach is model ind |
| WN18RR | ✅ oui | ublicly available datasets, namely WN18, and WN18RR. Since our approach is model independent, we |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2203.04703v1 [cs.AI] 9 Mar 2022 # Language |
| UMLS | ng technique. For this analysis we have used UMLs dataset due to its exclusivity. 'manufacture |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | hes are re-used from SANS [2]. task. We use Hit@10 and Mean Reciprocal Rank (MRR) as the perfor |
| MRR | ✅ oui | ask. We use Hit@10 and Mean Reciprocal Rank (MRR) as the performance metrics. MRR represents |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | e ∈ E do dict{key : e, value : c} ← map({e}⊆ EZ, c ∈ C) // map the matching entities |

## NS Methods  —  precision 79% · recall~ 58%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Adversarial Language Model-driven Negative Sampling | ❌ NON | _(absent du texte)_ |
| Adversarial Negative Sampling | ✅ oui | , adversarial temperature (for training with adversarial negative sampling) $\tau = 0.5$, learning rate $\alpha = 0.000 |
| Adversarial Uniform Negative Sampling | ✅ oui | $, and hop size $\mathcal{H} = 3$. Using non adversarial/uniform negative sampling the number of negative sample is $\mathcal{N |
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Generative Adversarial Network-based Negative Sampling | ❌ NON | _(absent du texte)_ |
| KBGAN | ✅ oui | l{O}(1)$</td> </tr> <tr> <td>KBGAN [6]</td> <td>$\mathcal{O}(t)$</td> |
| Language Model-driven Negative Sampling | ✅ oui | arXiv:2203.04703v1 [cs.AI] 9 Mar 2022 # Language Model-driven Negative Sampling **Mirza Mohtashim Alam² , Md Rashad Al Hasa |
| NSCaching | ✅ oui | l{O}(t)$</td> </tr> <tr> <td>NSCaching [22]</td> <td>$\mathcal{O}(1)$</td> |
| Self-Adv. RW-SANS | ✅ oui | al{V}\|)$</td> </tr> <tr> <td>Self-Adv. RW-SANS [2]</td> <td>$\mathcal{O}(r\mathcal{ |
| Self-Adv. SANS | ✅ oui | {V}\|^2)$</td> </tr> <tr> <td>Self-Adv. SANS [2]</td> <td>$\mathcal{O}(\|\mathcal{ |
| Structure-aware Negative Sampling | ✅ oui | ructure-aware Approaches.** More recently, a structure-aware negative sampling technique (SANS) was proposed [2] to conside |
| Uniform Negative Sampling | ✅ oui | ize $\mathcal{H} = 3$. Using non adversarial/uniform negative sampling the number of negative sample is $\mathcal{N |
| Uniform RW-SANS | ✅ oui | {V}\|^2)$</td> </tr> <tr> <td>Uniform RW-SANS [2]</td> <td>$\mathcal{O}(r\mathcal{ |
| Uniform SANS | ✅ oui | cal{E}\|$</td> </tr> <tr> <td>Uniform SANS [2]</td> <td>$\mathcal{O}(\|\mathcal{ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Affinity Dependent Negative Sampling | li, M.; Mohiuddin, K.; and Lehmann, J. 2020. Affinity dependent negative sampling for knowledge graph embeddings. In *DL4KG@ES |
| Distributional Negative Sampling | *, 767–776. Dash, S., and Gliozzo, A. 2019. Distributional negative sampling for knowledge base completion. *Applied Scie |
| GAN | ** Recently, Generative Adversarial Network (GAN) [9] has been explored for negative sampling |
| Negative Sampling | [cs.AI] 9 Mar 2022 # Language Model-driven Negative Sampling **Mirza Mohtashim Alam² , Md Rashad Al Hasa |
| RW-SANS | </td> </tr> <tr> <td>Uniform RW-SANS [2]</td> <td>$\mathcal{O}(r\mathcal{ |
| SANS | structure-aware negative sampling technique (SANS) was proposed [2] to consider the neighbourh |
| Self-Adv | al{V}\|)$</td> </tr> <tr> <td>Self-Adv. [15]</td> <td>$\mathcal{O}(\|\mathca |
| Uniform Sampling | ize $\mathcal{H} = 3$. Using non adversarial/uniform negative sampling the number of negative sample is $\mathcal{N |

## KGE Models  —  precision 100% · recall~ 18%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| RotatE | ✅ oui | ely used KGEs in the case of TransE [5], and RotatE [15]. Our proposed method achieves state-of- |
| TransE | ✅ oui | ng method on widely used KGEs in the case of TransE [5], and RotatE [15]. Our proposed method ac |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| BERT | ities of the entities. We employed Sentence-BERT [13] to obtain the contextual representation |
| ComplEx | ge graph embedding by relational rotation in complex space. In *International Conference on Learn |
| GAN | ** Recently, Generative Adversarial Network (GAN) [9] has been explored for negative sampling |
| HypER | experimental set up including the datasets, hyper-parameters, and the chosen KGE models. In or |
| LINE | ities labeled h=0, h=1, h=2, and h=3. Dotted lines represent distances d=1, d=2, and d=3 betwee |
| Random Walk | \mathcal{H}$ is used for hops count, $r$ for randomwalks count, and $\mathcal{Z}$ for PCA dimensional |
| RatE | al negative sampling) $\tau = 0.5$, learning rate $\alpha = 0.0001$, batch size $\mathcal{B} = |
| sentence-BERT | e similarities of the entities. We employed Sentence-BERT [13] to obtain the contextual representation |
| SimplE | Q.; Shao, Y.; and Chen, L. 2019. Nscaching: Simple and efficient negative sampling for knowledg |
