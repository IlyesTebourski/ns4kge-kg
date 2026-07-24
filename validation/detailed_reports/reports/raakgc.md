# Validation — RAAKGC.md

**Titre extrait :** Knowledge Graph Completion with Relation-Aware Anchor Enhancement

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 42 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **97.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **72.4%** |

## Datasets  —  precision 100% · recall~ 79%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | <td>3134</td> </tr> <tr> <td>FB15k-237</td> <td>272,115</td> <td>17 |
| FB15k-237_v1 | ✅ oui | n="2">WN18RR_v1</th> <th colspan="2">FB15k-237_v1</th> </tr> <tr> <th>MRR</th> |
| FB15k-237_v2 | ✅ oui | 18RR_v2, WN18RR_v3, WN18RR_v4, FB15k-237_v1, FB15k-237_v2, FB15k-237_v3, and FB15k-237_v4. The eight d |
| FB15k-237_v3 | ✅ oui | R_v3, WN18RR_v4, FB15k-237_v1, FB15k-237_v2, FB15k-237_v3, and FB15k-237_v4. The eight datasets were e |
| FB15k-237_v4 | ✅ oui | B15k-237_v1, FB15k-237_v2, FB15k-237_v3, and FB15k-237_v4. The eight datasets were extracted by Teru e |
| Wikidata5M-Trans | ✅ oui | d>20,466</td> </tr> <tr> <td>Wikidata5M-Trans</td> <td>20,614,279</td> <td |
| WN18RR | ✅ oui | Figure. 1, we illustrate a sub-graph of the WN18RR dataset as an example. In this subgraph, *ru |
| WN18RR_v1 | ✅ oui | line models w./w.o. our RAA framework on the WN18RR_v1 dataset (Teru, Denis, and Hamilton 2020). As |
| WN18RR_v2 | ✅ oui | ting. The texted datasets include WN18RR_v1, WN18RR_v2, WN18RR_v3, WN18RR_v4, FB15k-237_v1, FB15k-2 |
| WN18RR_v3 | ✅ oui | exted datasets include WN18RR_v1, WN18RR_v2, WN18RR_v3, WN18RR_v4, FB15k-237_v1, FB15k-237_v2, FB15 |
| WN18RR_v4 | ✅ oui | ets include WN18RR_v1, WN18RR_v2, WN18RR_v3, WN18RR_v4, FB15k-237_v1, FB15k-237_v2, FB15k-237_v3, a |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2504.06129v1 [cs.IR] 8 Apr 2025 # Knowledge |
| FB15k | <td>3134</td> </tr> <tr> <td>FB15k-237</td> <td>272,115</td> <t |
| Wikidata5M | d>20,466</td> </tr> <tr> <td>Wikidata5M-Trans</td> <td>20,614,279</td> |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | he WN18RR dataset, it improves MRR by 4.43%, Hit@1 by 5.61%, Hit@3 by 3.44%, and Hit@10 by 2.36 |
| Hits@10 | ✅ oui | y 4.43%, Hit@1 by 5.61%, Hit@3 by 3.44%, and Hit@10 by 2.36% compared to SimKGC. Second, we obse |
| Hits@3 | ✅ oui | t, it improves MRR by 4.43%, Hit@1 by 5.61%, Hit@3 by 3.44%, and Hit@10 by 2.36% compared to Si |
| MRR | ✅ oui | ed evaluation metrics: Mean Reciprocal Rank (MRR) and Hit@k(k=1,3,10). **Compared Baselines* |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | entity descriptions for improved predictive accuracy, have garnered escalating interest in recent |
| MAP | descriptions. Typical methods in this branch map an input query (textual descriptions associa |

## NS Methods  —  precision 80% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| In-Batch Negative Sampling | ✅ oui | mples are the self-negative samples (SN) and in-batch negative samples (IBN) (Wang et al. 2022a). Moreover, differe |
| In-Batch-Relation Negative Sampling | ✅ oui | is the same. Therefore, we also incorporate in-batch-relation negative samples (IBRN). This ![Framework illustration of th |
| Relation-Aware Anchor Enhancement | ✅ oui | Apr 2025 # Knowledge Graph Completion with Relation-Aware Anchor Enhancement Duanyang Yuan¹\*, Sihang Zhou¹\*, Xiaoshu C |
| Self-Negative Sampling | ✅ oui | ples in KG, and the negative samples are the self-negative samples (SN) and in-batch negative samples (IBN) (Wa |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Hardness and Structure-Aware Contrastive Knowledge Graph Embedding | , H.; Zhang, J.; and Molybog, I. 2024. HaSa: Hardness and Structure-Aware Contrastive Knowledge Graph Embedding. In Proceedings of the ACM on Web Conference |
| Negative Sampling | problem, the existing methods design various negative sampling algorithms to enable the learned network to |
| Random Negative Sampling | ..., k\}, t_i \in \mathcal{T}\}$, $k$ is the random sampling size. Given an input query (europe, has par |
| Random Sampling | ..., k\}, t_i \in \mathcal{T}\}$, $k$ is the random sampling size. Given an input query (europe, has par |

## KGE Models  —  precision 100% · recall~ 77%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| BERTRL | ✅ oui | he relation-aware neighborhood of the query. BERTRL (Zha, Chen, and Yan 2022) collects possible |
| ComplEx | ✅ oui | port results of TransE (Bordes et al. 2013), ComplEx (Trouillon and Bouchard 2017), DistMult (Yan |
| ConKGC | ✅ oui | of the query as extra context to the model. ConKGC (Shang et al. 2023) introduces a sampling st |
| ConvE | ✅ oui | Bouchard 2017), DistMult (Yang et al. 2015), ConvE (Dettmers et al. 2018), RGCN (Schlichtkrull |
| DistMult | ✅ oui | 013), ComplEx (Trouillon and Bouchard 2017), DistMult (Yang et al. 2015), ConvE (Dettmers et al. 2 |
| DKRL | ✅ oui | et al. 2024). The pioneer text-based method, DKRL (Xie et al. 2016), initially integrates text |
| GenKGC | ✅ oui | pervision. Besides the mentioned algorithms, GenKGC (Xie et al. 2022) and KICGPT (Wei et al. 202 |
| HaSa | ✅ oui | al. 2021a), SimKGC (Wang et al. 2022a), and HaSa (Zhang, Zhang, and Molybog 2024). Note that |
| InsKGC | ✅ oui | 7). As for the text-based methods, we choose InsKGC (Jiang, Drummond, and Cohn 2023) and SimKGC |
| KEPLER | ✅ oui | cluding KG-BERT (Yao, Mao, and Luo 2019) and KEPLER (Wang et al. 2021b), utilize a Pre-trained L |
| KG-BERT | ✅ oui | eural network. Subsequent studies, including KG-BERT (Yao, Mao, and Luo 2019) and KEPLER (Wang et |
| KG-S2S | ✅ oui | ver, KGT5-context (Kochsiek et al. 2023) and KG-S2S (Chen et al. 2022a) model the link predictio |
| KGT5-context | ✅ oui | M) for encoding text descriptions. Moreover, KGT5-context (Kochsiek et al. 2023) and KG-S2S (Chen et a |
| KICGPT | ✅ oui | ned algorithms, GenKGC (Xie et al. 2022) and KICGPT (Wei et al. 2023) go beyond the neighborhood |
| LMKE | ✅ oui | ctions by the decoder directly. Furthermore, LMKE (Wang et al. 2022b) introduces a contrastive |
| MTL-KGC | ✅ oui | we include KG-BERT (Yao, Mao, and Luo 2019), MTL-KGC (Kim et al. 2020), StAR (Wang et al. 2021a), |
| QuatE | ✅ oui | et al. 2018), RotatE (Sun et al. 2019), and QuatE (Li et al. 2023b). For text-based methods, w |
| RAA-KGC | ✅ oui | enhanced knowledge graph completion method (RAA-KGC). Specifically, in our method, to provide a |
| RGCN | ✅ oui | et al. 2015), ConvE (Dettmers et al. 2018), RGCN (Schlichtkrull et al. 2018), RotatE (Sun et |
| RotatE | ✅ oui | al. 2018), RGCN (Schlichtkrull et al. 2018), RotatE (Sun et al. 2019), and QuatE (Li et al. 2023 |
| SimKGC | ✅ oui | result. Following the approach presented in SimKGC (Wang et al. 2022a), we use the inverse trip |
| StAR | ✅ oui | o, and Luo 2019), MTL-KGC (Kim et al. 2020), StAR (Wang et al. 2021a), SimKGC (Wang et al. 202 |
| TransE | ✅ oui | r triple-based methods, we report results of TransE (Bordes et al. 2013), ComplEx (Trouillon and |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | gaining promising performance and increasing attention for the rapid development of large language |
| BERT | al network. Subsequent studies, including KG-BERT (Yao, Mao, and Luo 2019) and KEPLER (Wang et |
| HAN | hen, Y.; Yu, S.; Yan, Y.; Liu, Z.; Wang, S.; Han, X.; Liu, Z.; and Sun, M. 2024. KBAda: Effic |
| KGT5 | M) for encoding text descriptions. Moreover, KGT5-context (Kochsiek et al. 2023) and KG-S2S (C |
| ScaLed | $e_{hrt_a}^{avg}$ can be further rotated and scaled, thereby bringing the target entity embeddin |
| SimplE | ### Training and Inference We formulate a simple yet effective contrastive learning loss func |
| TaKE | ext-based knowledge graph completion methods take advantage of pre-trained language models (PL |
