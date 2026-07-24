# Validation — HaSa.md

**Titre extrait :** HaSa: Hardness and Structure-Aware Contrastive Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 21 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **91.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 14 |
| **Recall relatif (indicatif, a valider)** | **60.0%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | WN18RR datasets and competitive results for FB15k-237 datasets compared to both classic and pre-tr |
| WN18RR | ✅ oui | te-of-the-art results in several metrics for WN18RR datasets and competitive results for FB15k-2 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | 2023 Oct 15 [cs.AI] arXiv:2305.10563v2 # HaSa: Hardness and Structure |
| FB15k | WN18RR datasets and competitive results for FB15k-237 datasets compared to both classic and pr |

## Metrics  —  precision 100% · recall~ 71%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | rmance of the Simple InfoNCE in terms of the Hit@1 metric, as it compels Conference acronym ’X |
| Hits@10 | ✅ oui | @1↑</th> <th>Hit@3↑</th> <th>Hit@10↑</th> <th>MR↓</th> <th>MRR↑< |
| Hits@3 | ✅ oui | RR↑</th> <th>Hit@1↑</th> <th>Hit@3↑</th> <th>Hit@10↑</th> <th>M |
| MR | ✅ oui | head entities in a KG. We use the Mean Rank (MR) of correct entities, Mean Reciprocal Rank ( |
| MRR | ✅ oui | ) of correct entities, Mean Reciprocal Rank (MRR), and Hits at N (Hit@N) which means the prop |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | FB15K-237. Table 2 shows the link prediction accuracy after 10 epochs for WN18RR and after 5 epoch |
| MAP | \mathbb{R}^d$ [14, 33]; some KGE methods may map $r$ to a separate space from the entities. K |

## NS Methods  —  precision 71% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hard InfoNCE | ✅ oui | amples, lead to better performance [13, 15]. Hard InfoNCE samples negative tails from a distribution t |
| Hardness and Structure-Aware Contrastive Knowledge Graph Embedding | ✅ oui | 3 Oct 15 [cs.AI] arXiv:2305.10563v2 # HaSa: Hardness and Structure-Aware Contrastive Knowledge Graph Embedding **Honggen Zhang** University of Hawaii at M |
| KBGAN | ✅ oui | t]. \quad (4) $$ Similar to RotatE [26] and KBGAN [4], we use the following negative sample di |
| Noise contrastive estimation | ✅ oui | g loss proposed by [20], which is similar to noise contrastive estimation (NCE) [11]. More recently, InfoNCE loss [22] |
| Self-adversarial negative sampling | ❌ NON | _(absent du texte)_ |
| Simple InfoNCE | ✅ oui | nstead, we only generate $K$ negative tails. Simple InfoNCE[22] samples negative tails from a distributi |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Hard Negative Mixing | hilippe Weinzaepfel, and Diane Larlus. 2020. Hard negative mixing for contrastive learning. *Advances in Neura |
| Importance Sampling | e second expectation can be approximated via importance sampling. $$ \mathbb{E}_{t^- \sim p^-(t\|e_{hr}, \ell |
| Negative Sampling | ledge Graph Embedding, Contrastive Learning, Negative Sampling **ACM Reference Format:** Honggen Zhang, Ju |
| Simple Negative Sampling | $ produces far more false negatives than the simple negative sample distribution $p^-(t)$. ## 4.2 Shortest Path |
| Structure-Aware Negative Sampling | iam L Hamilton, and Avishek Joey Bose. 2020. Structure aware negative sampling in knowledge graphs. arXiv preprint arXiv:20 |

## KGE Models  —  precision 100% · recall~ 64%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | ge graph embedding by relational rotation in complex space. *arXiv preprint arXiv:1902.10197* (20 |
| DistMult | ✅ oui | /strong></td> </tr> <tr> <td>DistMult [36]</td> <td>7,000</td> <td |
| HaSa+ | ✅ oui | 2023 Oct 15 [cs.AI] arXiv:2305.10563v2 # HaSa: Hardness and Structure-Aware Contrastive Kn |
| KG-BERT | ✅ oui | ormation from the knowledge graph to propose KG-BERT. Shen et al. [25], Wang et al. [30] combined |
| LASS | ✅ oui | ed language-based methods such as StAR [30], LASS [25]. # 2 RELATED WORK Knowledge graph emb |
| RotatE | ✅ oui | KGE methods on both classic methods such as RotatE [26], ComplexE [29] and pre-trained language |
| sentence-BERT | ✅ oui | or the pre-trained LMs, we use BERT-base and sentence-BERT [23] (both pre-trained LMs have embedding sp |
| StAR | ✅ oui | d pre-trained language-based methods such as StAR [30], LASS [25]. # 2 RELATED WORK Knowledg |
| TransE | ✅ oui | ssic KGE</td> </tr> <tr> <td>TransE [3]</td> <td>2,300</td> <td> |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | g: Explainable conversational reasoning with attention-based walks over knowledge graphs. In *Proce |
| BERT | ation from the knowledge graph to propose KG-BERT. Shen et al. [25], Wang et al. [30] combined |
| RatE | on is done using PyTorch AdamW with learning rate $2 \times 10^{-5}$ and parameter penalty $1 |
| SimKGC | ei Zhao, Zhuoyu Wei, and Jingming Liu. 2022. SimKGC: Simple contrastive knowledge graph completi |
| SimplE | nstead, we only generate $K$ negative tails. Simple InfoNCE[22] samples negative tails from a di |
