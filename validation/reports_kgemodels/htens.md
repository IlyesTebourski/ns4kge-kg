# KGE Models — HTENS.md

**Titre :** Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 4 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 80% |
| Recall relatif *mentionnes* | 0% |

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

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose+table | The GAN-based sampling methods, such as KBGAN[3] and IGAN[13], set the KGE model to b |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| TKRL | prose | <sup>1</sup>https://github.com/thunlp/TKRL SIGIR ’23, July 23–27, 2023, Taipei, T |