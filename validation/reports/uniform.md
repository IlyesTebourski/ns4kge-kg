# Validation — Uniform.md

**Titre extrait :** Translating Embeddings for Modeling Multi-relational Data

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 10 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **76.9%** |
| Candidats faux negatifs (dans le texte, non extraits) | 14 |
| **Recall relatif (indicatif, a valider)** | **41.7%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | Numbers of parameters** and their values for FB15k (in millions). $n_e$ and $n_r$ are the nb. o |
| WN | ✅ oui | <tr> <th>DATA SET</th> <th>WN</th> <th>FB15K</th> <th>FB1M |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | rd in Theatrical Motion Pictures,<br/>Screen Actors Guild Award for Best Actor - Motion Picture< |
| Kinship | l can fail. For instance, on the small-scale Kinships data set [7], TransE does not achieve perfor |

## Metrics  —  precision 50% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | the *mean* of those predicted ranks and the *hits@10*, i.e. the proportion of correct entities ra |
| MR | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | ptions can lead to better trade-offs between accuracy and scalability. **Relationships as transla |

## NS Methods  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Unknown | ✅ oui | tructured is the best when no example of the unknown relationship is provided, because it does no |

_Aucun candidat faux negatif pour cette categorie._

## KGE Models  —  precision 75% · recall~ 35%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| LFM | ✅ oui | <td>1.06</td> </tr> <tr> <td>LFM [6]</td> <td>$O(n_e k + n_r k + 10k^ |
| Neural Tensor Model | ✅ oui | this point. Another related approach is the Neural Tensor Model [14]. A special case of this model correspon |
| RESCAL | ✅ oui | <td>0.75</td> </tr> <tr> <td>RESCAL [11]</td> <td>$O(n_e k + n_r k^2)$</ |
| SME(bilinear) | ❌ NON | _(absent du texte)_ |
| SME(linear) | ❌ NON | _(absent du texte)_ |
| Structured Embeddings | ✅ oui | he links between our model and those of [3] (Structured Embeddings or SE) and [14]. 3 Table 1: **Numbers of p |
| TransE | ✅ oui | p to very large databases. Hence, we propose TransE, a method which models relationships by inte |
| Unstructured | ✅ oui | r> </thead> <tbody> <tr> <td>Unstructured [2]</td> <td>$O(n_e k)$</td> |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| ComplEx | nt relationships. This suggests that even in complex and heterogeneous multi-relational domains s |
| HousE | er of Sam</em>, <em>Happy Feet</em>, <em>The House of Mirth</em>,<br/><em>Unfaithful</em>, <str |
| Neural Tensor Network | Learning new facts from knowledge bases with neural tensor networks and semantic word vectors. In *Advances in N |
| Neural Tensor Networks | Learning new facts from knowledge bases with neural tensor networks and semantic word vectors. In *Advances in N |
| RatE | aking a gradient step with constant learning rate. The algorithm is stopped based on its perfo |
| SE | l and those of [3] (Structured Embeddings or SE) and [14]. 3 Table 1: **Numbers of paramet |
| SimplE | t to single-relational data where ad-hoc but simple modeling assumptions can be made after some |
| SME | <td>7.47</td> </tr> <tr> <td>SME(LINEAR) [2]</td> <td>$O(n_e k + n_r |
| StAR | end on the entities, such as those who liked Star Wars IV also liked Star Wars V, but they may |
| Structured Embedding | he links between our model and those of [3] (Structured Embeddings or SE) and [14]. 3 Table 1: **Numbers of p |
| TaKE | tities and the relationships. The embeddings take values in $\mathbb{R}^k$ ($k$ is a model hyp |
