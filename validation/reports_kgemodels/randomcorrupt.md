# KGE Models — RandomCorrupt.md

**Titre :** Investigations on Knowledge Base Embedding for Relation Prediction and Extraction

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 8 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
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
| ComplEx | ✅ oui | modifications to adapt this task; (2) **ComplEx** achieves the best performance on all |
| DistMult | ✅ oui | ficantly and consistently outperforms **DistMult** which matches the observations for th |
| TransE | ✅ oui | of link prediction; (2) Surprisingly, **TransE** has competitive performance with **Co |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ConvE | ✅ oui | combine the two entities in a triple. **ConvE** (Dettmers et al., 2017) uses a convol |
| HOLE | ✅ oui | **DistMult** into the complex space. **HOLE** (Nickel et al., 2016) employs circula |
| ManifoldE | ✅ oui | tors of entities into various spaces. **ManifoldE** (Xiao et al., 2016) embeds a triple a |
| PTransE | ✅ oui | ), **TransR** (Lin et al., 2015b) and **PTransE** (Lin et al., 2015a). However, limited |
| RESCAL | ✅ oui | le as a manifold rather than a point. **RESCAL** (Nickel et al., 2011) is one of the e |
| TransD | ✅ oui | ), **TransR** (Lin et al., 2015b) and **TransD** (Ji et al., 2015), extend **TransE** |
| TransH | ✅ oui | ed embedding. Later variants, such as **TransH** (Wang et al., 2014), **TransR** (Lin |
| TransR | ✅ oui | ch as **TransH** (Wang et al., 2014), **TransR** (Lin et al., 2015b) and **TransD** (J |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._