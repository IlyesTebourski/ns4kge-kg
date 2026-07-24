# Validation — KBGAN.md

**Titre extrait :** KBGAN: Adversarial Learning for Knowledge Graph Embeddings

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 16 |
| Extraites NON trouvees (FP -> erreur precision) | 6 |
| **Precision** | **72.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 19 |
| **Recall relatif (indicatif, a valider)** | **45.7%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | ng three knowledge base completion datasets: FB15k-237, WN18 and WN18RR. Experimental results show |
| WN18 | ✅ oui | owledge base completion datasets: FB15k-237, WN18 and WN18RR. Experimental results show that a |
| WN18RR | ✅ oui | ase completion datasets: FB15k-237, WN18 and WN18RR. Experimental results show that adversarial |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | e *state* (which determines what actions the actor can take), $p_G(h', r, t'\|h, r, t)$ is the * |
| Arxiv | arXiv:1711.04071v3 [cs.CL] 16 Apr 2018 # KBGAN: A |
| FB15k | ng three knowledge base completion datasets: FB15k-237, WN18 and WN18RR. Experimental results s |

## Metrics  —  precision 50% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | two common metrics, mean reciprocal ranking (MRR) and hits at 10 (H@10). We only report score |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 29% · recall~ 20%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| KBGAN | ✅ oui | arXiv:1711.04071v3 [cs.CL] 16 Apr 2018 # KBGAN: Adversarial Learning for Knowledge Graph Em |
| KBGAN (ComplEx) | ❌ NON | _(absent du texte)_ |
| KBGAN (DistMult) | ❌ NON | _(absent du texte)_ |
| Type-constrained Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling | ✅ oui | function. However, most of these studies use uniform sampling to generate negative training examples (Bord |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | ples in a continuous space such as images. A GAN consists of two parts, the *generator* and t |
| IRGAN | ator using policy gradient and other tricks. IRGAN (Wang et al., 2017) is a recent work which c |
| Negative Sampling | use one knowledge graph embedding model as a negative sample generator to assist the training of our desi |
| Random Negative Sampling | <th>Positive fact</th> <th>Uniform random sample</th> <th>Trained generator</th> |
| Random Sampling | <th>Positive fact</th> <th>Uniform random sample</th> <th>Trained generator</th> |
| Uniform Random Negative Sampling | > <th>Positive fact</th> <th>Uniform random sample</th> <th>Trained generator</th> |
| Uniform Random Sampling | > <th>Positive fact</th> <th>Uniform random sample</th> <th>Trained generator</th> |
| Uniform Sampling | function. However, most of these studies use uniform sampling to generate negative training examples (Bord |

## KGE Models  —  precision 100% · recall~ 56%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | e two probability-based models, DISTMULT and COMPLEX. We evaluate the performances of KBGAN on th |
| ConvE | ✅ oui | cal{R}\|$</td> </tr> <tr> <td>CONVE</td> <td>$f(\text{vec}(f([\overline{ |
| DistMult | ✅ oui | rom one of the two probability-based models, DISTMULT and COMPLEX. We evaluate the performances of |
| HolE | ✅ oui | cal{R}\|$</td> </tr> <tr> <td>HOLE</td> <td>$\mathbf{r}^T(\mathbf{h} \s |
| ManifoldE | ✅ oui | cal{R}\|$</td> </tr> <tr> <td>MANIFOLDE (hyperplane)</td> <td>$\|(\mathbf{h} |
| RESCAL | ✅ oui | edge graph embedding (KGE) techniques (e.g., RESCAL (Nickel et al., 2011), TRANSE (Bordes et al. |
| TransD | ✅ oui | ain two translation-based models, TRANSE and TRANSD, each with assistance from one of the two pr |
| TransE | ✅ oui | sarially train two translation-based models, TRANSE and TRANSD, each with assistance from one of |
| TransH | ✅ oui | cal{R}\|$</td> </tr> <tr> <td>TRANSH</td> <td>$\\|(\mathbf{I} - \mathbf{r} |
| TransR | ✅ oui | cal{R}\|$</td> </tr> <tr> <td>TRANSR</td> <td>$\\|\mathbf{W}_r\mathbf{h} + |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| ANALOGY | t learning (RL), so we would like to draw an analogy between our model and an RL model. The gener |
| GAN | ples in a continuous space such as images. A GAN consists of two parts, the *generator* and t |
| HAN | earning. *Machine learning* 8(3-4):229–256. Han Xiao, Minlie Huang, and Xiaoyan Zhu. 2016. F |
| KBGAN | arXiv:1711.04071v3 [cs.CL] 16 Apr 2018 # KBGAN: Adversarial Learning for Knowledge Graph Em |
| LINE | g, there is still a common challenge in this line of research. For space efficiency, common kn |
| SimplE | ng step, so we cannot find its gradient with simple differentiation. We use a simple special cas |
| StAR | E</td> <td>$\mathbf{r}^T(\mathbf{h} \star \mathbf{t})$ ($\star$ is circular correlatio |
| TaKE | ly qualitatively. The marginal loss function takes the following form: $$L_m = \sum_{(h,r,t) \ |
