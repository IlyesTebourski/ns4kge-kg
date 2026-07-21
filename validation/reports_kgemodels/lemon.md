# KGE Models — LEMON.md

**Titre :** Language Model-driven Negative Sampling

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 2 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 2 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 0% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| RotatE | ✅ oui | tbody> <tr> <td rowspan="4">RotatE</td> <td>Uniform</td> < |
| TransE | ✅ oui | </tr> <tr> <td rowspan="4">TransE</td> <td>Uniform</td> < |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| BERT | prose | of the entities. We employed Sentence-BERT [13] to obtain the contextual represent |
| GAN | prose | cently, Generative Adversarial Network (GAN) [9] has been explored for negative sam |