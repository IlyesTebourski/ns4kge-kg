# Validation — RUGA.md

**Titre extrait :** Improving Knowledge Graph Completion Using Soft Rules and Adversarial Learning

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 4 |
| **Precision** | **82.6%** |
| Candidats faux negatifs (dans le texte, non extraits) | 9 |
| **Recall relatif (indicatif, a valider)** | **67.9%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | # 1) Datasets This paper uses two datasets: FB15K and YAGO37. FB15K is a subgraph of Freebase, |
| YAGO37 | ✅ oui | ets This paper uses two datasets: FB15K and YAGO37. FB15K is a subgraph of Freebase, which cont |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | tions in vector space”, available at https://arxiv.org/abs/1301.3781, 2013-9-7. [8] Bordes A, |

## Metrics  —  precision 43% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | s correct or not. In this paper, the average accuracy (graph) is selected as the evaluation index |
| Hits@1 | ✅ oui | e best performance baseline ComplEx, the MRR/hits@1 of FB15K is increased by 8%/19% and YAGO37 b |
| Hits@10 | ❌ NON | _(absent du texte)_ |
| Hits@3 | ❌ NON | _(absent du texte)_ |
| Hits@5 | ❌ NON | _(absent du texte)_ |
| MR | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | t ($e_j$) given ($r_k, e_j$). In this paper, MRR, MED and HITS@N were selected for experiment |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| KBGAN | ✅ oui | ng. Therefore, Liwei Cai et al.[16] proposed KBGAN to solve the problem that negative samples g |
| soft Rules and graph adversarial learning | ✅ oui | o improve the completion of knowledge graph: soft Rules and graph adversarial learning (RUGA). Firstly, the traditional knowledge g |
| Uniform Negative Sampling | ✅ oui | space of positive examples. The traditional uniform negative sampling method fixed the ratio of the number of posi |
| Unknown | ✅ oui | negative example distribution above all the unknown facts. Such a sampling space is very large, |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | role of logic rules and the effect of false negative samples on knowledge embedding. Based on the logic r |
| Uniform Sampling | space of positive examples. The traditional uniform negative sampling method fixed the ratio of the number of posi |

## KGE Models  —  precision 100% · recall~ 62%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | le 1-1 relationship. However, there are also complex 1-n, n-1, n-n relationships in the knowledge |
| DistMult | ✅ oui | ypical models include RESCAL<sup>[13]</sup>, DistMult<sup>[14]</sup>, ComplEx<sup>[10]</sup>, *etc |
| HolE | ✅ oui | ansE<sup>[8]</sup>, DistMult<sup>[18]</sup>, Hole<sup>[22]</sup> and ComplEx<sup>[13]</sup>. T |
| RESCAL | ✅ oui | of scoring function. Typical models include RESCAL<sup>[13]</sup>, DistMult<sup>[14]</sup>, Com |
| RUGA | ✅ oui | : soft Rules and graph adversarial learning (RUGA). Firstly, the traditional knowledge graph e |
| RUGE | ✅ oui | et al.[14] proposed a Rule-guided embedding (RUGE), which is a new iterative guidance method b |
| TransD | ✅ oui | TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD<sup>[11]</sup> and so on. As shown in Fig.2, |
| TransE | ✅ oui | oposed a representative model of translation–TransE<sup>[8]</sup>. The model considers the relat |
| TransH | ✅ oui | as done to expand and apply TranE, including TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD |
| TransR | ✅ oui | apply TranE, including TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD<sup>[11]</sup> and so |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ge acquisition and reasoning. More and more attention has been paid to the combination of embedded |
| LINE | }$ in batch processing. The fifth to seventh lines of the algorithm are the two stages of soft |
| RatE | \alpha$ in 1, 2, 5, 10, the initial learning rate $\gamma$ in 0.01, 0.05, 0.1, 0.5, 1.0, and t |
| SimplE | eld of knowledge graph. The model can handle simple 1-1 relationship. However, there are also co |
| TaKE | wledge graph embedding method does not fully take into account the role of logic rules and the |
| word2vec | on invariance exists in vector space through word2vec. Thus, Bordes et al. proposed a representati |
