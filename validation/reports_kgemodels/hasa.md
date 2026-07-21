# KGE Models — HaSa.md

**Titre :** HaSa: Hardness and Structure-Aware Contrastive Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 9 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **89%** |
| Precision (evalues, vs tableaux) | 89% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 89% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ❌ NON | _(absent des tableaux)_ |
| DistMult | ✅ oui | ng></td> </tr> <tr> <td>DistMult [36]</td> <td>7,000</td> |
| HaSa+ | ✅ oui | /tr> <tr> <td>$\mathcal{L}_{HaSa}$ (6)</td> <td><u>123</u></td> |
| KG-BERT | ✅ oui | KGE</td> </tr> <tr> <td>KGBERT [38]</td> <td>97</td> < |
| LASS | ✅ oui | 482</td> </tr> <tr> <td>LASS [25]</td> <td>55</td> < |
| RotatE | ✅ oui | 441</td> </tr> <tr> <td>RotatE [26]</td> <td>3,340</td> |
| sentence-BERT | ✅ oui | 6$). All methods use the pre-trained LM sentence-BERT as the initialization. Boldface is the |
| StAR | ✅ oui | 420</td> </tr> <tr> <td>StAR [30]</td> <td><strong>51</stron |
| TransE | ✅ oui | KGE</td> </tr> <tr> <td>TransE [3]</td> <td>2,300</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| BERT | prose+table | from the knowledge graph to propose KG-BERT. Shen et al. [25], Wang et al. [30] com |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._