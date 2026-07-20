# Validation — DomainNS.md

**Titre extrait :** An Interpretable Knowledge Transfer Model for Knowledge Base Completion

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **86.4%** |
| Candidats faux negatifs (dans le texte, non extraits) | 20 |
| **Recall relatif (indicatif, a valider)** | **48.7%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k | ✅ oui | e ITransF on two benchmark datasets—WN18 and FB15k for knowledge base completion and obtains im |
| WN18 | ✅ oui | e evaluate ITransF on two benchmark datasets—WN18 and FB15k for knowledge base completion and |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:1704.05908v2 [cs.CL] 3 May 2017 # An Interp |
| Wikipedia | , Multilingual Knowledge Base Extracted from Wikipedia. *Semantic Web* 6(2):167–195. Xiang Li, Tao |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | tains improvements on both the mean rank and Hits@10 metrics, over all baselines that do not use |
| MR | ✅ oui | 3">FB15k</th> </tr> <tr> <th>MR</th> <th>H10</th> <th>Time</ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | of the predicted ranks) and Hits@10 (top 10 accuracy). Lower mean rank or higher Hits@10 mean bet |

## NS Methods  —  precision 25% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Domain Sampling | ✅ oui | efer to the new proposed sampling method as "domain sampling". # 4 Experiments ## 4.1 Setup To evaluat |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Domain-based Negative Sampling | efer to the new proposed sampling method as "domain sampling". # 4 Experiments ## 4.1 Setup To evaluat |
| Negative Sampling | e define the probability $p_r$ to generate a negative sample from the same domain mentioned in Section 3. |

## KGE Models  —  precision 100% · recall~ 48%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CTransR | ✅ oui | <td>68.7</td> </tr> <tr> <td>CTransR (Lin et al., 2015b)</td> <td>No</td> |
| DISTMULT | ✅ oui | <td>41.4</td> </tr> <tr> <td>DISTMULT (Yang et al., 2015)</td> <td>No</td> |
| IRN | ✅ oui | Hits@10 than current state-of-the-art model IRN employing external information. We can see |
| ITransF | ✅ oui | teness. We propose a novel embedding model, *ITransF*, to perform knowledge base completion. Equi |
| NLFeat | ✅ oui | <td>84.6</td> </tr> <tr> <td>NLFeat (Toutanova and Chen, 2015)</td> <td> |
| PTransE | ✅ oui | <td>76.2</td> </tr> <tr> <td>PTransE (Lin et al., 2015a)</td> <td>Path</t |
| Random Walk | ✅ oui | <td>87.0</td> </tr> <tr> <td>Random Walk (Wei et al., 2016)</td> <td>Path</td |
| RTransE | ✅ oui | /strong></td> </tr> <tr> <td>RTransE (García-Durán et al., 2015)</td> <td |
| STransE | ✅ oui | s an effect of the projection. For instance, STransE (Nguyen et al., 2016b) utilizes two projecti |
| TATEC | ✅ oui | <td>77.3</td> </tr> <tr> <td>TATEC (García-Durán et al., 2016)</td> <td |
| TransD | ✅ oui | <td>74.0</td> </tr> <tr> <td>TransD (Ji et al., 2015)</td> <td>No</td> |
| TransE | ✅ oui | inal work, Bordes et al. (2013) proposes the TransE, which models the statistical regularities w |
| TransH | ✅ oui | <td>47.1</td> </tr> <tr> <td>TransH (Wang et al., 2014)</td> <td>No</td> |
| TransR | ✅ oui | elation-specific aspects of the same entity, TransR (Lin et al., 2015b) uses projection matrices |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | edge base completion. Equipped with a sparse attention mechanism, ITransF discovers hidden concepts |
| DAT | istics, Suntec, Singapore, pages 1003–1011. Dat Quoc Nguyen, Kairit Sirts, Lizhen Qu, and Ma |
| KG2E | <td>70.2</td> </tr> <tr> <td>KG2E (He et al., 2015)</td> <td>No</td> |
| LINE | of statistical regularities. Previously, a line of research makes use of external informatio |
| Neural Tensor Network | Manning, and Andrew Ng. 2013. Reasoning With Neural Tensor Networks for Knowledge Base Completion. In *Advances |
| Neural Tensor Networks | Manning, and Andrew Ng. 2013. Reasoning With Neural Tensor Networks for Knowledge Base Completion. In *Advances |
| NTN | <td>76.7</td> </tr> <tr> <td>NTN (Socher et al., 2013)</td> <td>No</t |
| RatE | 20 for WN18 and 1000 for FB15k. The learning rate is 0.01 on WN18 and 0.1 on FB15k. We use 30 |
| ScaLed | oting the number of matrices is not linearly scaled. dense attention model is acceptable<sup>3< |
| SE | r> </thead> <tbody> <tr> <td>SE (Bordes et al., 2011)</td> <td>No</t |
| SimplE | er inner loop to our algorithm, we turn to a simple but fast approximation method based on the f |
| Structured Embedding | Collobert, and Yoshua Bengio. 2011. Learning Structured Embeddings of Knowledge Bases. In *Proceedings of the T |
| Structured Embeddings | Collobert, and Yoshua Bengio. 2011. Learning Structured Embeddings of Knowledge Bases. In *Proceedings of the T |
| TaKE | <sup>3</sup>With 300 projection matrices, it takes 1h1m to run one epoch for a model with dense |
| Unstructured | <td>39.8</td> </tr> <tr> <td>Unstructured (Bordes et al., 2014)</td> <td>No</t |
