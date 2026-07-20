# Validation — ConceptDriven.md

**Titre extrait :** A Novel Concept-Driven Negative Sampling Mechanism for Enhancing Semanticity and Interpretability of Knowledge Graph Completion Task

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 14 |
| Extraites NON trouvees (FP -> erreur precision) | 5 |
| **Precision** | **73.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 19 |
| **Recall relatif (indicatif, a valider)** | **42.4%** |

## Datasets  —  precision 100% · recall~ 40%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | \|/k$, trad-off parameter $\lambda = 0.5$, on FB15K-237 dataset. We train the model until convergenc |
| WN18RR | ✅ oui | /2k$, trad-off parameter $\lambda = 0.4$, on WN18RR dataset; $\epsilon = 2.5e-5$, dropout rate i |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | benchmark for knowledge graph completion,” *ArXiv*, vol. abs/2108.01387, 2021. [7] J. Devlin, |
| FB15k | \|/k$, trad-off parameter $\lambda = 0.5$, on FB15K-237 dataset. We train the model until conver |
| WN | . <table> <thead> <tr> <th>Method</th> <th>WN.↑</th> <th>FB.↑</th> <th>AVG.↑</th> <th>AVG. |

## Metrics  —  precision 40% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | entities ranked among the top-$n$; and (iii) Accuracy. ### D. Performance Summary Entity Predict |
| Hits@1 | ❌ NON | _(absent du texte)_ |
| Hits@10 | ❌ NON | _(absent du texte)_ |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | valuation metrics: (i) Mean Reciprocal Rank (MRR), indicating the average reciprocal rank of |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 67% · recall~ 36%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Commonsense-Aware Negative Sampling | ✅ oui | tomatic commonsense generation (ACG) module, commonsense-aware negative sampling (CANS) module and the multi-view link predic |
| Concept Domain Negative Sampling | ✅ oui | nstructive constraints. E.g., [4] proposes a concept domain negative sampling (CDNS) strategy, which samples corrupted hea |
| Concept-Driven Negative Sampling | ✅ oui | DOI: 10.1109/DSC59305.2023.00047 # A Novel Concept-Driven Negative Sampling Mechanism for Enhancing Semanticity and Inte |
| Entity-Aware Negative Sampling | ✅ oui | Machine Learning*, 2022. [21] S. hyun Je, “Entity aware negative sampling with auxiliary loss of false negative predic |
| Reinforcement Learning Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| CAKE | hable Commonsense-Aware Knowledge Embedding (CAKE) framework, which consists of automatic comm |
| CANS | module, commonsense-aware negative sampling (CANS) module and the multi-view link prediction ( |
| Domain Sampling | ve constraints. E.g., [4] proposes a concept domain negative sampling (CDNS) strategy, which samples corrupted hea |
| Domain-based Negative Sampling | ve constraints. E.g., [4] proposes a concept domain negative sampling (CDNS) strategy, which samples corrupted hea |
| MVLP | ) module and the multi-view link prediction (MVLP) module, wherein CANS is comparable with our |
| Negative Sampling | C59305.2023.00047 # A Novel Concept-Driven Negative Sampling Mechanism for Enhancing Semanticity and Inte |
| Reinforced Negative Sampling | Xu, X. He, Y. Cao, M. Wang, and T.-S. Chua, “Reinforced negative sampling over knowledge graph for recommendation,” *P |

## KGE Models  —  precision 100% · recall~ 40%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DistMult | ✅ oui | > <td>81.4</td> <td>4.15</td> </tr> <tr> <td>DistMult [18]</td> <td>88.4</td> <td>86.1</td> <td>87 |
| DKRL | ✅ oui | as TransE [3], TransH [14], TransR [15] and DKRL [16]), and when takeing the representative T |
| RotatE | ✅ oui | $; (ii) Rotation-based KGC models, including RotatE [17] and its corresponding Hardmard-product- |
| TransE | ✅ oui | s: (i) Translation-based KGC models (such as TransE [3], TransH [14], TransR [15] and DKRL [16]) |
| TransH | ✅ oui | lation-based KGC models (such as TransE [3], TransH [14], TransR [15] and DKRL [16]), and when t |
| TransR | ✅ oui | KGC models (such as TransE [3], TransH [14], TransR [15] and DKRL [16]), and when takeing the re |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| BERT | lin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep bidirectional transfor |
| CAKE | hable Commonsense-Aware Knowledge Embedding (CAKE) framework, which consists of automatic comm |
| ComplEx | task has achieved higher improvement on more complex and more challenging dataset FB15k-237, comp |
| HypER | etically analyzes NS’s loss to contribute to hyper-parameter tuning and understand the better u |
| LINE | n [12], [13]. Among them, three most typical lines of KGC models are described as follows: (i) |
| RatE | ations are summarized below: Adam's learning rate $\epsilon = 2e-5$, dropout rate is 0.1, vect |
| SimKGC | [8] L. Wang, W. Zhao, Z. Wei, and J. Liu, “Simkgc: Simple contrastive knowledge graph completi |
| SimplE | that of $C_e$. Although, this method is very simple and effective, it unfortunately *neglects* t |
| TransT | . Ma, J. Ding, W. Jia, K. Wang, and M. Guo, “Transt: Type-based multiple embedding representatio |
