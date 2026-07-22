# KGE Models — ConceptDriven.md

**Titre :** A Novel Concept-Driven Negative Sampling Mechanism for Enhancing Semanticity and Interpretability of Knowledge Graph Completion Task

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 6 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
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
| DistMult | ✅ oui | >81.4</td> <td>4.15</td> </tr> <tr> <td>DistMult [18]</td> <td>88.4</td> <td>86.1</td> < |
| DKRL | ✅ oui | d>44.5</td> <td>52.2</td> </tr><tr> <td>DKRL [16]</td> <td>26.0</td> <td>100.00</td> |
| RotatE | ✅ oui | d>43.2</td> <td>50.7</td> </tr><tr> <td>RotatE [17]</td> <td>47.6</td> <td>100.00</td> |
| TransE | ✅ oui | 0↑</th> </tr> </thead> <tbody> <tr> <td>TransE [3]</td> <td>24.3</td> <td>100.00</td> |
| TransH | ✅ oui | d>40.6</td> <td>47.6</td> </tr><tr> <td>TransH [14]</td> <td>23.1</td> <td>100.00</td> |
| TransR | ✅ oui | d>44.5</td> <td>52.2</td> </tr><tr> <td>TransR [15]</td> <td>23.2</td> <td>100.00</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._