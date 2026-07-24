# Validation — SparseNSG.md

**Titre extrait :** A Novel Negative Sampling Based on Frequency of Relational Association Entities for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 22 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **91.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 5 |
| **Recall relatif (indicatif, a valider)** | **81.5%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | ults on two commonly used datasets, WN18 and FB15K, show that the proposed method improves enti |
| WN18 | ✅ oui | ental results on two commonly used datasets, WN18 and FB15K, show that the proposed method imp |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | approach for knowledge graph embedding’, in arXiv:1509.05490, 2015. [17] S. He, K. Liu, G. Ji |
| Table 1 Dataset | ote as no result in the original paper. The Table 1 Datasets used in the experiment <table> <thead> |

## Metrics  —  precision 80% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | nt replacing relationships lead to different accuracy of the prediction results. This paper develo |
| Hits@10 | ✅ oui | sing from the triple. Therefore, in Table 3, hit@10 is A Novel Negative Sampling Based on Frequ |
| Hits@3 | ✅ oui | an="2">MeanRank</th> <th colspan="2">Hit@3(%)</th> <th colspan="2">MeanRank</th |
| MR | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | > <th> </th> <th colspan="2">MRR</th> <th colspan="2">MeanRank</th> |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 67% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Negative Sampling Based on Frequency of Relational Association Entities | ✅ oui | # A Novel Negative Sampling Based on Frequency of Relational Association Entities for Knowledge Graph Embedding Yi Zhang<sup> |
| Unknown | ✅ oui | n efficient way to automatically predict the unknown relational facts, knowledge representation l |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | # A Novel Negative Sampling Based on Frequency of Relational Association |

## KGE Models  —  precision 100% · recall~ 88%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ANALOGY | ✅ oui | ch as TransE, TransH, DistMult, ComplEx, and Analogy. And both the evaluation criteria of relatio |
| ComplEx | ✅ oui | ng models, such as TransE, TransH, DistMult, ComplEx, and Analogy. And both the evaluation criter |
| DistMult | ✅ oui | ph embedding models, such as TransE, TransH, DistMult, ComplEx, and Analogy. And both the evaluati |
| NTN | ✅ oui | and other kinds of models, such as SE, SME, NTN. However, a practical knowledge graph is oft |
| SE | ✅ oui | nsD [15], and other kinds of models, such as SE, SME, NTN. However, a practical knowledge gr |
| SME | ✅ oui | e latter contains, Semantic Matching Energy (SME) [10], Semantically Smooth Embedding (SSE) [ |
| SSE | ✅ oui | y (SME) [10], Semantically Smooth Embedding (SSE) [11], and translation-based methods [12–19] |
| TransA | ✅ oui | r missing, some presentation models, such as TransA [16], TransG [19], replace the relation of a |
| TransD | ✅ oui | models, such as TransE, TransH, TransR, and TransD [15], and other kinds of models, such as SE, |
| TransE | ✅ oui | rt knowledge graph embedding models, such as TransE, TransH, DistMult, ComplEx, and Analogy. And |
| TransG | ✅ oui | me presentation models, such as TransA [16], TransG [19], replace the relation of a triplet to c |
| TransH | ✅ oui | edge graph embedding models, such as TransE, TransH, DistMult, ComplEx, and Analogy. And both th |
| TranSparse | ✅ oui | provement, widely used in TransR, TransD and TranSparse [18], can effectively reduce the probability |
| TransR | ✅ oui | ethods, such as TransE [12], TransH [13] and TransR [14], are the most used knowledge graphs emb |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| LINE | politan_transit/transit_service_type/transit_lines*, only two entities related with it: Entity |
| SimplE | e graph is often far from complete, and this simple randomly replacing method may introduce many |
