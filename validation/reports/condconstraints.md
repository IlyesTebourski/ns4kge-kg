# Validation — CondConstraints.md

**Titre extrait :** Conditional Constraints for Knowledge Graph Embeddings

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 9 |
| Extraites NON trouvees (FP -> erreur precision) | 10 |
| **Precision** | **47.4%** |
| Candidats faux negatifs (dans le texte, non extraits) | 7 |
| **Recall relatif (indicatif, a valider)** | **56.2%** |

## Datasets  —  precision 50% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| MUTAG | ✅ oui | posed enhancements on two datasets (AIFB and MUTAG) that come supplied with elaborate schemas. |
| Table 1 Dataset | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | ling on link prediction in knowledge graphs. arXiv preprint arXiv:1708.06816 (2017) 7. Krompaß, |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | The metrics used to evaluate performance are Hits@10, Mean Rank (MR), and Mean Reciprocal Rank (M |
| MR | ✅ oui | evaluate performance are Hits@10, Mean Rank (MR), and Mean Reciprocal Rank (MRR), which are |
| MRR | ✅ oui | 0, Mean Rank (MR), and Mean Reciprocal Rank (MRR), which are standard when evaluating link pr |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 10% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| closed world constraints, neg_ratio=1 | ❌ NON | _(absent du texte)_ |
| closed world constraints, neg_ratio=5 | ❌ NON | _(absent du texte)_ |
| Conditional Constraint-Based Negative Sampling | ❌ NON | _(absent du texte)_ |
| Filtered Negative Sampling | ✅ oui | g so-called *filtered* negative samples [1]. Filtered negative samples are subjected to perturbation as per usual, |
| Locally Closed World Negative Sampling | ❌ NON | _(absent du texte)_ |
| no constraints, neg_ratio=1 | ❌ NON | _(absent du texte)_ |
| no constraints, neg_ratio=5 | ❌ NON | _(absent du texte)_ |
| open world constraints, neg_ratio=1 | ❌ NON | _(absent du texte)_ |
| open world constraints, neg_ratio=5 | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | pts were already made in the past to improve negative sampling by exploiting schematic domain and range con |
| Unknown | dictions about the existential likelihood of unknown facts [10]. In fact these two approaches to |

## KGE Models  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| RESCAL | ✅ oui | it only explores their applicability to the RESCAL model [2]. On the other hand, the work by To |
| TransE | ✅ oui | by Bordes et al. when they introduced their TransE embedding model: using so-called *filtered* |
| TransH | ✅ oui | ple scheme was introduced by Wang et al. for TransH and is sometimes called the Bernoulli trick |
| TRESCAL | ✅ oui | ly by exploiting type information [6]. While TRESCAL explicitly tries to make use of type constra |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| LINE | basic form of negative sampling takes a hard-line stance on the closed world assumption (CWA): |
| RatE | additional hyperparameter to tune the reject rate of an invalid triple. # 5 Evaluation To ev |
| SimplE | re actually valid. An early addition to this simple scheme was introduced by Wang et al. for Tra |
| TaKE | rk The most basic form of negative sampling takes a hard-line stance on the closed world assum |
