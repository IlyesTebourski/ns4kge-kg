# KGE Models — eTruncatedUNS.md

**Titre :** Bootstrapping Entity Alignment with Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 5 |
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
| AlignE | ✅ oui | 320</td> </tr> <tr> <td>AlignE</td> <td>47.18</td> <td |
| BootEA | ✅ oui | 707</td> </tr> <tr> <td>BootEA</td> <td><strong>62.94</strong> |
| IPTransE | ✅ oui | 334</td> </tr> <tr> <td>IPTransE</td> <td>40.59</td> <td |
| JAPE | ✅ oui | 386</td> </tr> <tr> <td>JAPE</td> <td>41.18</td> <td |
| MTransE | ✅ oui | </thead> <tbody> <tr> <td>MTransE</td> <td>30.83</td> <td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| KR-EAR | ✅ oui | tes reverse triples and relation paths. KR-EAR [Lin et al., 2016] introduces categoric |
| PTransE | ✅ oui | 2014], TransR [Lin et al., 2015b] and PTransE [Lin et al., 2015a]. Most existing KG |
| TransE | ✅ oui | nherent KG semantics. As an early work, TransE [Bordes et al., 2013] interprets a rela |
| TransH | ✅ oui | further improved by many works, such as TransH [Wang et al., 2014], TransR [Lin et al |
| TransR | ✅ oui | s, such as TransH [Wang et al., 2014], TransR [Lin et al., 2015b] and PTransE [Lin et |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._