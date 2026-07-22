# KGE Models — M2ixKG.md

**Titre :** MixKG: Mixing for harder negative samples in knowledge graph

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
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | ct, $\bar{\cdot}$ denotes conjugate for complex vectors <table> <thead> <tr> |
| DistMult | ✅ oui | ="2">semantic matching</td> <td>DistMult</td> <td>$\langle \mathbf{r}, \ |
| RotatE | ✅ oui | \\|$</td> </tr> <tr> <td>RotatE</td> <td>$\\|\mathbf{h} \odot \m |
| TransE | ✅ oui | translational distance</td> <td>TransE</td> <td>$\\|\mathbf{h} + \mathb |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | izes cached-based mechanism to pay more attention to high-quality negative samples. Diffe |