# KGE Models — ERDNS.md

**Titre :** Entity-Relation Distribution-aware Negative Sampling for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 8 |
| Modeles MENTIONNES seulement (hors tableaux) | 6 |
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
| CompGCN (ConvE) | ✅ oui | </tr> <tr> <td rowspan="3">CompGCN (ConvE)</td> <td>unif</td> <td |
| CompGCN (DistMult) | ✅ oui | </tr> <tr> <td rowspan="3">CompGCN (DistMult)</td> <td>unif</td> <td |
| CompGCN (TransE) | ✅ oui | </tr> <tr> <td rowspan="3">CompGCN (TransE)</td> <td>unif</td> <td |
| ComplEx | ✅ oui | 3. Performance comparison on DistMult, ComplEx, TransE and RotatE. <table> <thead> |
| ConvE | ✅ oui | le> Table 4. Performance comparison on ConvE and CompGCN. <table> <thead> <tr> |
| DistMult | ✅ oui | le> Table 3. Performance comparison on DistMult, ComplEx, TransE and RotatE. <table> |
| RotatE | ✅ oui | arison on DistMult, ComplEx, TransE and RotatE. <table> <thead> <tr> <th |
| TransE | ✅ oui | rmance comparison on DistMult, ComplEx, TransE and RotatE. <table> <thead> <tr> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| CompGCN | ✅ oui | ], ConvE [5], and InteractE [24], while CompGCN [5] is a generalized version of several |
| ConvKB | ✅ oui | odels. Examples of CNN-based models are ConvKB [18], ConvE [5], and InteractE [24], wh |
| InteractE | ✅ oui | models are ConvKB [18], ConvE [5], and InteractE [24], while CompGCN [5] is a generalize |
| SimplE | ✅ oui | ples and lower scores to negative ones. Simple negative sampling methods like uniform |
| TransD | ✅ oui | amples of TD models include TransE [2], TransD [8], TransR [15], and RotatE [21], whil |
| TransR | ✅ oui | models include TransE [2], TransD [8], TransR [15], and RotatE [21], while popular SM |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._