# KGE Models — GHN.md

**Titre :** Improving Knowledge Graph Completion with Generative Hard Negative Mining

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 10 |
| Modeles MENTIONNES seulement (hors tableaux) | 2 |
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
| DistMult | ✅ oui | 4.1</td> </tr> <tr> <td>DistMult</td> <td>44.4</td> <td> |
| DKRL | ✅ oui | em></td> </tr> <tr> <td>DKRL</td> <td>16.0</td> <td> |
| KEPLER | ✅ oui | es$</td> </tr> <tr> <td>KEPLER</td> <td>21.0</td> <td> |
| KG-BERT | ✅ oui | ods</td> </tr> <tr> <td>KG-BERT</td> <td>21.6</td> <td> |
| MTL-KGC | ✅ oui | 2.0</td> </tr> <tr> <td>MTL-KGC</td> <td>33.1</td> <td> |
| RotatE | ✅ oui | 4.6</td> </tr> <tr> <td>RotatE</td> <td>47.6</td> <td> |
| SimKGC | ✅ oui | 8.2</td> </tr> <tr> <td>SimKGC</td> <td>66.6</td> <td> |
| StAR | ✅ oui | 5.8</td> </tr> <tr> <td>StAR</td> <td>40.1</td> <td> |
| TransE | ✅ oui | ods</td> </tr> <tr> <td>TransE</td> <td>24.3</td> <td> |
| Tucker | ✅ oui | 3.3</td> </tr> <tr> <td>TuckER</td> <td>47.0</td> <td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | al., 2013), TransH (Wang et al., 2014), Complex (Trouillon et al., 2016), and RotatE (S |
| TransH | ✅ oui | s include TransE (Bordes et al., 2013), TransH (Wang et al., 2014), Complex (Trouillon |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._