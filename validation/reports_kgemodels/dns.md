# KGE Models — DNS.md

**Titre :** Distributional Negative Sampling for Knowledge Base Completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 2 |
| Modeles MENTIONNES seulement (hors tableaux) | 4 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| RESCAL | ✅ oui | parameters. RNS results for TransE and RESCAL are borrowed from Nickel et al. [2016b] |
| TransE | ✅ oui | its default parameters. RNS results for TransE and RESCAL are borrowed from Nickel et |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | ued embeddings into their corresponding complex variants, and performs Hermitian dot pr |
| HolE | ✅ oui | teractions within the triples for their HolE system. Trouillon et al. [2016] represe |
| Neural Tensor Network | ✅ oui | h as *RESCAL* Nickel et al. [2011] and *Neural Tensor Network* Socher et al. [2013] employ higher ord |
| TransH | ✅ oui | Wang et al. [2014] define an algorithm *TransH* that behaves like *TransE* with a mino |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._