# Validation — DHNS.md

**Titre extrait :** Diffusion-based Hierarchical Negative Sampling for Multimodal Knowledge Graph Completion

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 36 |
| Extraites NON trouvees (FP -> erreur precision) | 4 |
| **Precision** | **90.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 21 |
| **Recall relatif (indicatif, a valider)** | **63.2%** |

## Datasets  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DB15K | ✅ oui | r> </thead> <tbody> <tr> <td>DB15K</td> <td>12842</td> <td>279< |
| MKG-W | ✅ oui | <td>9904</td> </tr> <tr> <td>MKG-W</td> <td>15000</td> <td>169< |
| MKG-Y | ✅ oui | <td>4274</td> </tr> <tr> <td>MKG-Y</td> <td>15000</td> <td>28</ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2501.15393v1 [cs.AI] 26 Jan 2025 # Diffusio |

## Metrics  —  precision 25% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ❌ NON | _(absent du texte)_ |
| Hits@10 | ❌ NON | _(absent du texte)_ |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | eciprocal rank of all the correct instances (MRR) and proportion of the correct instances ran |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 92% · recall~ 55%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | , leading to ambiguous training signals [4]. Bernoulli sampling [31] employs a Bernoulli distribution to rep |
| Diffusion-based Hierarchical Negative Sampling | ✅ oui | arXiv:2501.15393v1 [cs.AI] 26 Jan 2025 # Diffusion-based Hierarchical Negative Sampling for Multimodal Knowledge Graph Completion G |
| DMNS | ✅ oui | the original data. In graph-structured data, DMNS[21] employs DDPM to generate negative nodes |
| IGAN | ✅ oui | gher-quality negative triples. KBGAN [4] and IGAN [30] use Generative Adversarial Networks (GA |
| KBGAN | ✅ oui | to generate higher-quality negative triples. KBGAN [4] and IGAN [30] use Generative Adversarial |
| MANS | ✅ oui | challenging negatives from multimodal data. MANS [37] emphasizes modality-aware NS to align s |
| MMRNS | ✅ oui | ial for generating diverse negative triples. MMRNS [34] introduces a relation-enhanced NS mecha |
| NS-KGE | ✅ oui | SCaching (NSCach) [40], KBGAN [4], SANS [1], NS-KGE [13], MANS [37] and MMRNS [34]. **Implement |
| NSCaching | ✅ oui | or KGE models to distinguish from positives. NSCaching [40] utilizes additional memory to store and |
| SANS | ✅ oui | gh-quality negative triples during training. SANS [1] leverages graph structure information fo |
| Uniform Negative Sampling | ✅ oui | on both MMKGC and NS performances, including uniform sampling (Uniform) [3], Bernoulli sampling (Bern) [31 |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | ings. AdaMF [38] uses a generator to produce adversarial samples and a discriminator to measure their plausib |
| Bernoulli Sampling | , leading to ambiguous training signals [4]. Bernoulli sampling [31] employs a Bernoulli distribution to rep |
| GAN | 30. Wang, P., Li, S., Pan, R.: Incorporating gan for negative sampling in knowledge represent |
| Negative Sampling | 26 Jan 2025 # Diffusion-based Hierarchical Negative Sampling for Multimodal Knowledge Graph Completion G |
| Non-Sampling | , Y., Xu, S., Chen, C., Zhang, Y.: Efficient non-sampling knowledge graph embedding. In: Web Conferenc |
| Random Negative Sampling | g negative sampling (NS) strategies, such as random sampling and adversarial-based methods, face three ke |
| Random Sampling | g negative sampling (NS) strategies, such as random sampling and adversarial-based methods, face three ke |
| Structure-Aware Negative Sampling | A., Salehi, Y., Hamilton, W.L., Bose, A.J.: Structure aware negative sampling in knowledge graphs. In: EMNLP. pp. 6093–610 |
| Uniform Sampling | on both MMKGC and NS performances, including uniform sampling (Uniform) [3], Bernoulli sampling (Bern) [31 |

## KGE Models  —  precision 100% · recall~ 66%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AdaMF | ✅ oui | res are incorporated into entity embeddings. AdaMF [38] uses a generator to produce adversarial |
| ComplEx | ✅ oui | erations between entities. DistMult [35] and ComplEx [27] use bilinear models to capture both sym |
| DistMult | ✅ oui | as translation operations between entities. DistMult [35] and ComplEx [27] use bilinear models to |
| GC-OTE | ✅ oui | , ComplEx [27], RotatE [25], PairRE [7], and GC-OTE [26]. (2) **Multimodal KGC models:** we com |
| IKRL | ✅ oui | e plausibility of each triple. For instance, IKRL [33] extracts visual features using a pre-tr |
| KGDM | ✅ oui | considering the query node's context, while KGDM [16] applies DDPM to estimate the probabilis |
| LAFA | ✅ oui | bility in an adversarial training framework. LAFA [24] considers the relationships between ent |
| MMKRL | ✅ oui | cluding IKRL [33], TBKGC [20], TransAE [32], MMKRL [18], RSME [29], VBKGC [39], OTKGE [6] and A |
| OTKGE | ✅ oui | sAE [32], MMKRL [18], RSME [29], VBKGC [39], OTKGE [6] and AdaMF [38]. (3) **Negative sampling |
| PairRE | ✅ oui | ], DistMult [35], ComplEx [27], RotatE [25], PairRE [7], and GC-OTE [26]. (2) **Multimodal KGC |
| QuatE | ✅ oui | and antisymmetric relations. RotatE [25] and QuatE [36] introduce rotational and quaternion-bas |
| RESCAL | ✅ oui | ilinear interaction-based KGE models such as RESCAL [22] and DistMult [35], formulated as: $$C( |
| RotatE | ✅ oui | both symmetric and antisymmetric relations. RotatE [25] and QuatE [36] introduce rotational and |
| RSME | ✅ oui | grating both visual and textual information. RSME [29] employs a gate mechanism to ensure that |
| TBKGC | ✅ oui | he plausibility of triples. TransAE [32] and TBKGC [20] extend 4 G. Niu et al. IKRL by integr |
| TransAE | ✅ oui | ransE to assess the plausibility of triples. TransAE [32] and TBKGC [20] extend 4 G. Niu et al. |
| TransD | ✅ oui | s to evaluate triples, including TransE [3], TransD [10], DistMult [35], ComplEx [27], RotatE [2 |
| TransE | ✅ oui | ntinuous numerical spaces. Early models like TransE [3] propose a translational distance-based s |
| TransH | ✅ oui | tion-based KGE models such as TransE [3] and TransH [31], formulated as: $$C(\mathbf{x}_e, \mat |
| VBKGC | ✅ oui | C [20], TransAE [32], MMKRL [18], RSME [29], VBKGC [39], OTKGE [6] and AdaMF [38]. (3) **Negat |
| VISTA | ✅ oui | ware aggregation of multi-modal information. VISTA [11] designs three transformer-based encoder |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | mechanism using knowledge-guided cross-modal attention to generate more challenging negatives from |
| BERT | Bao, H., Dong, L., Piao, S., Wei, F.: BEiT: BERT pre-training of image ers. In: ICLR (2022) |
| GAN | 30. Wang, P., Li, S., Pan, R.: Incorporating gan for negative sampling in knowledge represent |
| HypER | {KGC}$ and $\mathcal{L}_{HA}$, weighted by a hyper-parameter $\lambda$ for a trade-off between |
| KBGAN | to generate higher-quality negative triples. KBGAN [4] and IGAN [30] use Generative Adversarial |
| MLP | , C(\mathbf{x}_e, \mathbf{x}_r)) = LayerNorm(MLP(\mathbf{x}_t, PE(t), C(\mathbf{x}_e, \mathbf |
| OTE | omplEx [27], RotatE [25], PairRE [7], and GC-OTE [26]. (2) **Multimodal KGC models:** we com |
| RatE | ng the Adam optimizer with separate learning rates to ensure stability. 8 G. Niu et al. The e |
| sentence-BERT | 9–816 (2011) 23. Reimers, N., Gurevych, I.: Sentence-BERT: Sentence embeddings using Siamese BERT-netw |
| SimplE | modalities** especially in MMKGs, leading to simple or invalid negative triples. Second, althoug |
| TaKE | structural, visual, and textual modalities. Take the generated negative triple via corrupting |
