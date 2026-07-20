# Validation — IGAN.md

**Titre extrait :** Incorporating GAN for Negative Sampling in Knowledge Representation Learning

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 17 |
| Extraites NON trouvees (FP -> erreur precision) | 7 |
| **Precision** | **70.8%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **51.5%** |

## Datasets  —  precision 100% · recall~ 80%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB13 | ✅ oui | y are FB15K used in (Bordes et al. 2013) and FB13 used in (Socher et al. 2013). Wordnet provid |
| FB15K | ✅ oui | and we use two subsets of Freebase. They are FB15K used in (Bordes et al. 2013) and FB13 used i |
| WN11 | ✅ oui | we also use two subsets of Wordnet. They are WN11 used in (Socher et al. 2013) and WN18 used i |
| WN18 | ✅ oui | ey are WN11 used in (Socher et al. 2013) and WN18 used in (Bordes et al. 2013). The statistics |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | 2018 Sep 23 [cs.AI] arXiv:1809.11017v1 # Incorporating GAN for Negati |

## Metrics  —  precision 67% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | e 3: Evaluation results about classification accuracy on triplets classification(%). <table> < |
| Hits@10 | ✅ oui | </th> <th>Mean Rank</th> <th>Hits@10 (%)</th> <th>Mean Rank</th> |
| MR | ❌ NON | _(absent du texte)_ |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 43% · recall~ 43%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| GAN-based Negative Sampling | ❌ NON | _(absent du texte)_ |
| GAN-pretrain | ✅ oui | he whole model is trained from scratch. * **GAN-pretrain** We firstly train the original models with |
| GAN-scratch | ✅ oui | ning settings are conducted as follows. * **GAN-scratch** The parameters of the discriminator and ge |
| Random Negative Sampling | ✅ oui | sampled from the whole entities set. Such a random sampling method is effective at the beginning of the |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | [cs.AI] arXiv:1809.11017v1 # Incorporating GAN for Negative Sampling in Knowledge Represent |
| IRGAN | Y.; Wang, B.; Zhang, P.; and Zhang, D. 2017. Irgan: A minimax game for unifying generative and |
| Negative Sampling | arXiv:1809.11017v1 # Incorporating GAN for Negative Sampling in Knowledge Representation Learning **Peif |
| Random Sampling | sampled from the whole entities set. Such a random sampling method is effective at the beginning of the |

## KGE Models  —  precision 80% · recall~ 42%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Neural Tensor Network | ✅ oui | ), \tag{8}$$ where g() is tanh function. **Neural Tensor Network** (Socher et al. 2013) extends Single Layer |
| Single Layer Model | ✅ oui | - \mathbf{M}_{r,t} \mathbf{t}\|. \tag{7}$$ **Single Layer Model** (Socher et al. 2013) improves Structured E |
| SME(Bilinear) | ❌ NON | _(absent du texte)_ |
| Structured Embedding | ✅ oui | t) = \|\mathbf{h} - \mathbf{t}\|. \tag{6}$$ **Structured Embedding** (Bordes et al. 2011) uses two projection m |
| TransD | ✅ oui | athbf{M}_r \mathbf{t}\|_{L1/L2}. \tag{4}$$ **TransD** (Ji et al. 2015) argues that the project m |
| TransE | ✅ oui | d **r** for entities h, t and relation r. **TransE** (Bordes et al. 2013) starts the line of tr |
| TransE + A-LSTM | ❌ NON | _(absent du texte)_ |
| TransH | ✅ oui | le for 1-to-N, N-to-1 or N-to-N relations, **TransH** (Wang et al. 2014) proposes to project the |
| TransR | ✅ oui | lations are in the same vector space, thus **TransR** (Lin et al. 2015) proposes to use a relati |
| Unstructured Model | ✅ oui | nd images (Xie et al. 2016a) of entities. **Unstructured Model** (Bordes et al. 2012; Bordes et al. 2014) i |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | [cs.AI] arXiv:1809.11017v1 # Incorporating GAN for Negative Sampling in Knowledge Represent |
| HypER | f $x$, and $\gamma$ is a fixed margin set as hyper parameter. The score function $f_r(h, t)$ ha |
| LINE | **TransE** (Bordes et al. 2013) starts the line of translation based knowledge embedding mod |
| Neural Tensor Networks | ning, C. D.; and Ng, A. 2013. Reasoning with neural tensor networks for knowledge base completion. In *Advances |
| RatE | relations among {20, 50, 100, 200}, learning rate $\lambda$ for SGD among {0.01, 0.001, 0.0001 |
| SE | /strong></td> </tr> <tr> <td>SE (Bordes et al. 2011)</td> <td><stron |
| SimplE | onstrates the effectiveness of our method on simple models. Simple models generalize well to tes |
| SME | /strong></td> </tr> <tr> <td>SME(Bilinear) (Bordes et al. 2012)</td> |
| Structured Embeddings | obert, R.; Bengio, Y.; et al. 2011. Learning structured embeddings of knowledge bases. In *AAAI*, volume 6, 6. |
| TaKE | works (GAN). In this GAN-based framework, we take advantage of a generator to obtain high-qual |
| Unstructured | nd images (Xie et al. 2016a) of entities. **Unstructured Model** (Bordes et al. 2012; Bordes et al. 2 |
