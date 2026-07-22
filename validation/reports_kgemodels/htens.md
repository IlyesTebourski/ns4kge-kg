# KGE Models — HTENS.md

**Titre :** Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 4 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 1 |
| Recall BRUT evalues / mentionnes | 100% / 0% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 1 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 0% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | )d$</td> </tr> <tr> <td>ComplEx</td> <td>$&lt; \mathbf{h}, \mat |
| DistMult | ✅ oui | )d$</td> </tr> <tr> <td>DistMult</td> <td>$&lt; \mathbf{h}, \mat |
| TransD | ✅ oui | )d$</td> </tr> <tr> <td>TransD</td> <td>$\\| (\mathbf{I} + \mat |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>$\\| \mathbf{h} + \math |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| TKRL | prose | <sup>1</sup>https://github.com/thunlp/TKRL SIGIR ’23, July 23–27, 2023, Taipei, T |