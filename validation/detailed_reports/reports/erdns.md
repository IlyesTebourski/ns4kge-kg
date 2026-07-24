# Validation — ERDNS.md

**Titre extrait :** Entity-Relation Distribution-aware Negative Sampling for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 28 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **90.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 11 |
| **Recall relatif (indicatif, a valider)** | **71.8%** |

## Datasets  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K237 | ✅ oui | r> </thead> <tbody> <tr> <td>FB15K237</td> <td>0</td> <td>1000</td |
| WN18RR | ✅ oui | <td>1</td> </tr> <tr> <td>WN18RR</td> <td>0</td> <td>100</td> |
| YAGO3-10 | ✅ oui | <td>1</td> </tr> <tr> <td>YAGO3-10</td> <td>0</td> <td>10000</t |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Wikipedia | .: Yago3: A knowledge base from multilingual wikipedias. In: 7th biennial conference on innovative d |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | r> <tr> <th>MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hit |
| Hits@10 | ✅ oui | s@1</th> <th>Hits@3</th> <th>Hits@10</th> <th>MRR</th> <th>Hits@1 |
| Hits@3 | ✅ oui | MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> <th>MR |
| MRR | ✅ oui | ion metrics, including Mean Reciprocal Rank (MRR), and Hits@N (N=1, 3, 10). The evaluation is |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 100% · recall~ 62%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Sampling | ✅ oui | es on the performance of KGEs. For instance, Bernoulli sampling [29] assigns different probabilities to repl |
| Entity-Relation Distribution-aware Negative Sampling | ✅ oui | # Entity-Relation Distribution-aware Negative Sampling for Knowledge Graph Embedding Naimeng Yao<s |
| IGAN | ✅ oui | al language processing (NLP) [7]. KBGAN [3], IGAN [26], and NSCaching [34] create a negative c |
| KBGAN | ✅ oui | es in natural language processing (NLP) [7]. KBGAN [3], IGAN [26], and NSCaching [34] create a |
| Non-Sampling | ✅ oui | negative sampling (NS) loss function, and a Non-Sampling work [14] adds all of the negative instances |
| NSCaching | ✅ oui | cessing (NLP) [7]. KBGAN [3], IGAN [26], and NSCaching [34] create a negative candidate set $C_{(e, |
| SANS | ✅ oui | es in the loss function in Self-Adv [21] and SANS [1]. However, these approaches primarily ste |
| Self-Adv | ✅ oui | to negative samples in the loss function in Self-Adv [21] and SANS [1]. However, these approaches |
| Subsampling | ✅ oui | mprove the KGE performance. More recently, a Subsampling work [10] explores the hyperparameter tuning |
| Uniform Sampling | ✅ oui | ones. Simple negative sampling methods like uniform sampling [2] generate negative samples by randomly su |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Negative Sampling | es on the performance of KGEs. For instance, Bernoulli sampling [29] assigns different probabilities to repl |
| GAN | 26. Wang, P., Li, S., et al.: Incorporating gan for negative sampling in knowledge represent |
| Negative Sampling | # Entity-Relation Distribution-aware Negative Sampling for Knowledge Graph Embedding Naimeng Yao<s |
| Simple Negative Sampling | e triples and lower scores to negative ones. Simple negative sampling methods like uniform sampling [2] generate n |
| Structure-Aware Negative Sampling | A., Salehi, Y., Hamilton, W.L., Bose, A.J.: Structure aware negative sampling in knowledge graphs. In: Proceedings of the |
| Uniform Negative Sampling | ones. Simple negative sampling methods like uniform sampling [2] generate negative samples by randomly su |

## KGE Models  —  precision 79% · recall~ 73%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CompGCN | ✅ oui | B [18], ConvE [5], and InteractE [24], while CompGCN [5] is a generalized version of several exis |
| CompGCN (ConvE) | ❌ NON | _(absent du texte)_ |
| CompGCN (DistMult) | ❌ NON | _(absent du texte)_ |
| CompGCN (TransE) | ❌ NON | _(absent du texte)_ |
| ComplEx | ✅ oui | ile popular SM models include DistMult [30], ComplEx [23], and SimplE [11]. NN-based KGE models c |
| ConvE | ✅ oui | xamples of CNN-based models are ConvKB [18], ConvE [5], and InteractE [24], while CompGCN [5] i |
| ConvKB | ✅ oui | NN) models. Examples of CNN-based models are ConvKB [18], ConvE [5], and InteractE [24], while C |
| DistMult | ✅ oui | RotatE [21], while popular SM models include DistMult [30], ComplEx [23], and SimplE [11]. NN-base |
| InteractE | ✅ oui | based models are ConvKB [18], ConvE [5], and InteractE [24], while CompGCN [5] is a generalized ver |
| RotatE | ✅ oui | ude TransE [2], TransD [8], TransR [15], and RotatE [21], while popular SM models include DistMu |
| SimplE | ✅ oui | e triples and lower scores to negative ones. Simple negative sampling methods like uniform sampl |
| TransD | ✅ oui | s. Examples of TD models include TransE [2], TransD [8], TransR [15], and RotatE [21], while pop |
| TransE | ✅ oui | g (SM) models. Examples of TD models include TransE [2], TransD [8], TransR [15], and RotatE [21 |
| TransR | ✅ oui | of TD models include TransE [2], TransD [8], TransR [15], and RotatE [21], while popular SM mode |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | 26. Wang, P., Li, S., et al.: Incorporating gan for negative sampling in knowledge represent |
| KBGAN | es in natural language processing (NLP) [7]. KBGAN [3], IGAN [26], and NSCaching [34] create a |
| RatE | awback can negatively impact the convergence rate of the model, increase computational expense |
| TaKE | meters. For KBGAN and NSCaching, we directly take the results from their works because the bes |
