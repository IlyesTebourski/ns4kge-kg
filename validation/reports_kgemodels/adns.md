# KGE Models — ADNS.md

**Titre :** Affinity Dependent Negative Sampling for Knowledge Graph Embeddings

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 2 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
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
| DistMult | ✅ oui | e 3. Evaluation of Negative Sampling on DistMult <table> <thead> <tr> <th> |
| TransE | ✅ oui | 2.** Evaluation of Negative Sampling on TransE <table> <thead> <tr> <th> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | t years. e.g, TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost |
| RotatE | ✅ oui | , DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all of these models dep |
| TransH | ✅ oui | , TransE [2], DistMult [3], Complex[4], TransH [5], RotatE [6] etc. Almost all of thes |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._