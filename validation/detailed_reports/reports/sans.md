# Validation — SANS.md

**Titre extrait :** Structure Aware Negative Sampling in Knowledge Graphs

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 14 |
| Extraites NON trouvees (FP -> erreur precision) | 5 |
| **Precision** | **73.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 26 |
| **Recall relatif (indicatif, a valider)** | **35.0%** |

## Datasets  —  precision 100% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K-237 | ✅ oui | proach on standard benchmarks, consisting of FB15K-237 (Bollacker et al., 2008), WN18 and WN18RR (M |
| WN18 | ✅ oui | sting of FB15K-237 (Bollacker et al., 2008), WN18 and WN18RR (Miller, 1995). From our experime |
| WN18RR | ✅ oui | FB15K-237 (Bollacker et al., 2008), WN18 and WN18RR (Miller, 1995). From our experiments we seek |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2009.11355v2 [cs.LG] 7 Oct 2020 # Structure |
| FB15k | proach on standard benchmarks, consisting of FB15K-237 (Bollacker et al., 2008), WN18 and WN18R |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | </th> <th>Algorithm</th> <th>Hit@10 (%)</th> <th>MRR</th> <th>Hi |
| MRR | ✅ oui | /th> <th>Hit@10 (%)</th> <th>MRR</th> <th>Hit@10 (%)</th> <th |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 55% · recall~ 26%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| KBGAN | ✅ oui | orm negative sampling (Bordes et al., 2013), KBGAN (Cai and Wang, 2018), and NSCaching (Zhang e |
| Noise Contrastive Estimation | ✅ oui | rgy landscape as simple random sampling—e.g. Noise Contrastive Estimation (NCE) (Gutmann and Hyvärinen, 2010)—produces |
| NSCaching | ✅ oui | er to train compared to GAN-based methods is NSCaching (Zhang et al., 2019), which involves using a |
| Random Walk Structure Aware Negative Sampling | ❌ NON | _(absent du texte)_ |
| Self-Adversarial Negative Sampling | ✅ oui | of easy negatives, Sun et al. (2019) propose Self-Adversarial negative sampling, which weighs each sampled negative accordin |
| Self-Adversarial Random Walk Structure Aware Negative Sampling | ❌ NON | _(absent du texte)_ |
| Self-Adversarial Structure Aware Negative Sampling | ❌ NON | _(absent du texte)_ |
| Structure Aware Negative Sampling | ✅ oui | arXiv:2009.11355v2 [cs.LG] 7 Oct 2020 # Structure Aware Negative Sampling in Knowledge Graphs **Kian Ahrabian\*,¹,³, |
| Uniform Negative Sampling | ✅ oui | SANS consistently leads to improvements upon uniform sampling and sophisticated Generative Adversarial Net |
| Uniform Random Walk Structure Aware Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Structure Aware Negative Sampling | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | se et al., 2018; Sun et al., 2019). However, adversarial negative sampling methods are computationally expensive, while |
| Dynamic Negative Sampling | negative sampling. We also experiment with a dynamic sampling scheme based on random walks to approximate |
| GAN | versarial Network (Goodfellow et al., 2014) (GAN) based approaches at a fraction of the compu |
| Importance Sampling | roximation of the partition function used in Importance Sampling (IS) (Bengio et al., 2003). **Non-Fixed Nega |
| Negative Sampling | 1355v2 [cs.LG] 7 Oct 2020 # Structure Aware Negative Sampling in Knowledge Graphs **Kian Ahrabian\*,¹,³, |
| Random Negative Sampling | le in shaping the energy landscape as simple random sampling—e.g. Noise Contrastive Estimation (NCE) (Gut |
| Random Sampling | le in shaping the energy landscape as simple random sampling—e.g. Noise Contrastive Estimation (NCE) (Gut |
| RW-SANS | s. To combat this inefficiency, we introduce RW-SANS in Alg. 1, which uses $\omega$ random walks |
| SANS | e propose Structure Aware Negative Sampling (SANS), an inexpensive negative sampling strategy |
| Self-Adv | efer to this technique as *Self-Adversarial (Self-Adv.) SANS*, whereas the former approach is refe |
| Self-Adv. RW-SANS | d>0.2249</td> </tr> <tr> <td>Self-Adv. RW-SANS (ours)</td> <td>50.04</td> < |
| Self-Adv. SANS | /strong></td> </tr> <tr> <td>Self-Adv. SANS (ours)</td> <td><strong>52.03</stron |
| Self-adversarial Sampling | of easy negatives, Sun et al. (2019) propose Self-Adversarial negative sampling, which weighs each sampled negative accordin |
| Subgraph-based Negative Sampling | N3(( )) N3 --- N4(( )) end subgraph Sampling ["negative triplets"] direction TB |
| Uniform RW-SANS | d>0.2254</td> </tr> <tr> <td>Uniform RW-SANS (ours)</td> <td><strong>48.50</stron |
| Uniform Sampling | SANS consistently leads to improvements upon uniform sampling and sophisticated Generative Adversarial Net |
| Uniform SANS | ereas the former approach is referred to as *Uniform SANS*. **Algorithm 1** Approximating the $k$-hop |

## KGE Models  —  precision 100% · recall~ 30%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DistMult | ✅ oui | ain KG embedding models based on the TransE, DistMult, and RotatE models for the task of KG comple |
| RotatE | ✅ oui | ng models based on the TransE, DistMult, and RotatE models for the task of KG completion*. We ev |
| TransE | ✅ oui | es to train KG embedding models based on the TransE, DistMult, and RotatE models for the task of |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ion answering over knowledge base with cross-attention combining global knowledge. In *Proceedings |
| ComplEx | selects a hard negative example through more complex negative sampling distribution, such as adve |
| DeepWalk | ozzi, Rami Al-Rfou, and Steven Skiena. 2014. Deepwalk: Online learning of social representations. |
| GAN | versarial Network (Goodfellow et al., 2014) (GAN) based approaches at a fraction of the compu |
| Random Walk | ment with a dynamic sampling scheme based on random walks to approximate a node's local neighborhood. |
| SimplE | ata. While earlier methods either employ too simple corruption distributions, i.e. uniform, yiel |
| TaKE | ory and allowing sparse tensor operations to take place, the appeal of incorporating graph st |
