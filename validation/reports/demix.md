# Validation — DeMix.md

**Titre extrait :** Negative Sampling with Adaptive Denoising Mixup for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 23 |
| Extraites NON trouvees (FP -> erreur precision) | 0 |
| **Precision** | **100.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 30 |
| **Recall relatif (indicatif, a valider)** | **43.4%** |

## Datasets  —  precision 100% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K237 | ✅ oui | <tr> <th>Epoch</th> <th>FB15k237-normal</th> <th>FB15k237-leakage</th |
| WN18RR | ✅ oui | <th>FB15k237-leakage</th> <th>WN18RR-normal</th> <th>WN18RR-leakage</th> |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Alibaba | NSF (LR21F020004), the NSFC (No. 62272411), Alibaba-Zhejiang University Joint Research Institute |
| Arxiv | arXiv:2310.09781v1 [cs.AI] 15 Oct 2023 # Negative |
| FB15k | deleted. Similarly, FB15k237 is a subset of FB15K [4], which comes Title Suppressed Due to Ex |
| WN18 | 10] and FB15K237 [20]. WN18RR is a subset of WN18 [4], where inverse relations are deleted. Si |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | @10</th> <th>Hits@3</th> <th>Hits@1</th> <th>MRR</th> <th>Hits@1 |
| Hits@10 | ✅ oui | <th> </th> <th>MRR</th> <th>Hits@10</th> <th>MRR</th> <th>Hits@1 |
| Hits@3 | ✅ oui | RR</th> <th>Hits@10</th> <th>Hits@3</th> <th>Hits@1</th> <th>MRR |
| MRR | ✅ oui | sampling false-negative triples. (b) Testing MRR performance v.s. Epoch based on RotatE. Norm |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | time on additional parameters. **Estimation Accuracy** In order to investigate whether the MPNE m |
| MAP | t.** Knowledge graph embedding (KGE) aims to map entities and relations of a knowledge graph |

## NS Methods  —  precision 100% · recall~ 44%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Adaptive Denoising Mixup | ✅ oui | cs.AI] 15 Oct 2023 # Negative Sampling with Adaptive Denoising Mixup for Knowledge Graph Embedding Xiangnan Chen |
| Bernoulli Sampling | ✅ oui | ive triples from a uniform distribution. - *Bernoulli Sampling* [24]. which sample negative triples from a |
| CANS | ✅ oui | orhood by utilizing the graph structure. - *CANS* [16]. The CANS is a component of CAKE [16] |
| ESNS | ✅ oui | we mainly compare CANS instead of CAKE. - *ESNS* [29]. It takes semantic similarities among |
| IGAN | ✅ oui | with high scores. For example, KBGAN[6] and IGAN[23] introduce a generative adversarial netwo |
| KBGAN | ✅ oui | stent triples with high scores. For example, KBGAN[6] and IGAN[23] introduce a generative adver |
| MixKG | ✅ oui | rate harder negative triples for KGE such as MixKG [8]. Different from existing methods, DeMix |
| NSCaching | ✅ oui | erate negative triples with high scores, and NSCaching[31] introduces a caching mechanism to store |
| RW-SANS | ✅ oui | ccording to the current embedding model. - *RW-SANS* [1]. It samples negative triples from the k |
| Self-adversarial Sampling | ✅ oui | nce v.s. Epoch based on RotatE. Normal means self-adversarial negative sampling. Leakage means ensuring sampled negative tri |
| Uniform Sampling | ✅ oui | we show the training objectives based on the uniform negative sampling [4] and self-adversarial sampling [18]. The |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | .s. Epoch based on RotatE. Normal means self-adversarial negative sampling. Leakage means ensuring sampled negative tri |
| Bernoulli Negative Sampling | ive triples from a uniform distribution. - *Bernoulli Sampling* [24]. which sample negative triples from a |
| CAKE | . - *CANS* [16]. The CANS is a component of CAKE [16] responsible for solving the invalid neg |
| Entity Similarity-based Negative Sampling | Yao, N., Liu, Q., Li, X., Yang, Y., Bai, Q.: Entity similarity-based negative sampling for knowledge graph embedding. In: Proceedin |
| GAN | introduce a generative adversarial network (GAN)[11] to generate negative triples with high |
| MixGCF | the generalization and robustness of models. MixGCF [13] integrates multiple negative samples to |
| Negative Sampling | arXiv:2310.09781v1 [cs.AI] 15 Oct 2023 # Negative Sampling with Adaptive Denoising Mixup for Knowledge |
| Random Negative Sampling | e denoising mixup mechanism. In specific, we random sample an input $(h, r)$ pattern from FB15K237, nam |
| Random Sampling | e denoising mixup mechanism. In specific, we random sample an input $(h, r)$ pattern from FB15K237, nam |
| SANS | rding to the current embedding model. - *RW-SANS* [1]. It samples negative triples from the k |
| Self-Adv | ></td> </tr> <tr> <td>TransE+Self-Adv</td> <td>0.215<sup>Δ</sup></td> |
| Self-adversarial Negative Sampling | nce v.s. Epoch based on RotatE. Normal means self-adversarial negative sampling. Leakage means ensuring sampled negative tri |
| Structure-Aware Negative Sampling | A., Salehi, Y., Hamilton, W.L., Bose, A.J.: Structure aware negative sampling in knowledge graphs. In: Proceedings of the |
| Uniform Negative Sampling | we show the training objectives based on the uniform negative sampling [4] and self-adversarial sampling [18]. The |

## KGE Models  —  precision 100% · recall~ 38%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | Notably, inspired by the characteristics of complex relations in KG, namely 1-N, N-1, 1-1, and N |
| DistMult | ✅ oui | tween vectors, such as the score function of DistMult [27]: $$ f(h, r, t) = \mathbf{h}^\top diag( |
| HAKE | ✅ oui | /strong></td> </tr> <tr> <td>HAKE+Uniform<sup>Δ</sup></td> <td>0.493</ |
| RotatE | ✅ oui | Testing MRR performance v.s. Epoch based on RotatE. Normal means self-adversarial negative samp |
| TransE | ✅ oui | Triples</td> </tr> <tr> <td>TransE+Uniform</td> <td>0.175*</td> |
| TransH | ✅ oui | KG, namely 1-N, N-1, 1-1, and N-N defined in TransH [24], we record the num of positive triples |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ion answering over knowledge base with cross-attention combining global knowledge. In: Proceedings |
| CAKE | . - *CANS* [16]. The CANS is a component of CAKE [16] responsible for solving the invalid neg |
| GAN | introduce a generative adversarial network (GAN)[11] to generate negative triples with high |
| HypER | nimum and mean value of $X$. $\delta_T$ is a hyper-parameter controlling the estimation range a |
| KBGAN | stent triples with high scores. For example, KBGAN[6] and IGAN[23] introduce a generative adver |
| RatE | 1\}$, $\mu$ from $\{1, 3, 5\}$. The learning rate is tuned from 0.00001 to 0.01. The margin is |
| SimplE | of our work are as follows: - We propose a simple and efficient denoising framework, named **D |
| Structured Embedding | ton, J., Collobert, R., Bengio, Y.: Learning structured embeddings of knowledge bases. In: Proceedings of the A |
| Structured Embeddings | ton, J., Collobert, R., Bengio, Y.: Learning structured embeddings of knowledge bases. In: Proceedings of the A |
| TaKE | $ to generate a partially positive triple to take more precise supervision to the KGE model. B |
