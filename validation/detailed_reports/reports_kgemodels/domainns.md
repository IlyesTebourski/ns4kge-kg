# KGE Models — DomainNS.md

**Titre :** An Interpretable Knowledge Transfer Model for Knowledge Base Completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 14 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 5 |
| Candidats mentions ratees (bruts) | 0 |
| Recall BRUT evalues / mentionnes | 74% / 100% |
| Vrais oublis (adjuges) evalues / mentionnes | 4 / 0 |
| Recall ADJUGE *evalues* | 78% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| CTransR | ✅ oui | 8.7</td> </tr> <tr> <td>CTransR (Lin et al., 2015b)</td> <td>No |
| DISTMULT | ✅ oui | 1.4</td> </tr> <tr> <td>DISTMULT (Yang et al., 2015)</td> <td>No |
| IRN | ✅ oui | 4.7</td> </tr> <tr> <td>IRN (Shen et al., 2016)</td> <td>Ex |
| ITransF | ✅ oui | </tr> <tr> <td><strong>ITransF</strong></td> <td>No</td> |
| NLFeat | ✅ oui | 4.6</td> </tr> <tr> <td>NLFeat (Toutanova and Chen, 2015)</td> |
| PTransE | ✅ oui | 6.2</td> </tr> <tr> <td>PTransE (Lin et al., 2015a)</td> <td>Pa |
| Random Walk | ✅ oui | 7.0</td> </tr> <tr> <td>Random Walk (Wei et al., 2016)</td> <td>Pat |
| RTransE | ✅ oui | ng></td> </tr> <tr> <td>RTransE (García-Durán et al., 2015)</td> |
| STransE | ✅ oui | the brackets are another set of results STransE reported. <table> <thead> <tr> |
| TATEC | ✅ oui | 7.3</td> </tr> <tr> <td>TATEC (García-Durán et al., 2016)</td> |
| TransD | ✅ oui | 4.0</td> </tr> <tr> <td>TransD (Ji et al., 2015)</td> <td>No</ |
| TransE | ✅ oui | 6.3</td> </tr> <tr> <td>TransE (Bordes et al., 2013)</td> <td> |
| TransH | ✅ oui | 7.1</td> </tr> <tr> <td>TransH (Wang et al., 2014)</td> <td>No |
| TransR | ✅ oui | 4.4</td> </tr> <tr> <td>TransR (Lin et al., 2015b)</td> <td>No |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose+table | base completion. Equipped with a sparse attention mechanism, ITransF discovers hidden con |
| KG2E | table | 0.2</td> </tr> <tr> <td>KG2E (He et al., 2015)</td> <td>No</ |
| NTN | table | 6.7</td> </tr> <tr> <td>NTN (Socher et al., 2013)</td> <td> |
| SE | table | </thead> <tbody> <tr> <td>SE (Bordes et al., 2011)</td> <td> |
| Unstructured | table | 9.8</td> </tr> <tr> <td>Unstructured (Bordes et al., 2014)</td> <td> |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._