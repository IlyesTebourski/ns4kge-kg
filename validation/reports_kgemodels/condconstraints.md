# KGE Models — CondConstraints.md

**Titre :** Conditional Constraints for Knowledge Graph Embeddings

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 1 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
| **Precision globale** | **75%** |
| Precision (evalues, vs tableaux) | 0% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 0 |
| Recall BRUT evalues / mentionnes | 100% / 100% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| TransE | ❌ NON | _(absent des tableaux)_ |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| RESCAL | ✅ oui | nly explores their applicability to the RESCAL model [2]. On the other hand, the work |
| TransH | ✅ oui | cheme was introduced by Wang et al. for TransH and is sometimes called the Bernoulli t |
| TRESCAL | ✅ oui | exploiting type information [6]. While TRESCAL explicitly tries to make use of type co |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._