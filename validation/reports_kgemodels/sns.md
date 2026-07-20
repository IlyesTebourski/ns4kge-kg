# KGE Models — SNS.md

**Titre :** Simple negative sampling for link prediction in knowledge graphs

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 2 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 67% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| DistMult | ✅ oui | ^2$</td> </tr> <tr> <td>DistMult [12]</td> <td>$\mathbf{h}^d, \m |
| TransH | ✅ oui | </thead> <tbody> <tr> <td>TransH [11]</td> <td>$\mathbf{h}^d, \m |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose+table | trained to learn embeddings. IGAN [8], KBGAN [3], KSGAN [7] are three existing GAN-b |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._