# KGE Models — GNS.md

**Titre :** Good negative sampling for triple classification

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 1 |
| Modeles MENTIONNES seulement (hors tableaux) | 7 |
| **Precision globale** | **88%** |
| Precision (evalues, vs tableaux) | 0% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| KG-BERT | ❌ NON | _(absent des tableaux)_ |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| BERT | ✅ oui | state-of-the-art embedding method - KG-BERT for triple classification task - on a b |
| ComplEx | ✅ oui | n KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BERT [21], a |
| DistMult | ✅ oui | TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BERT [21], and all these me |
| ReasonKGE | ✅ oui | o pick head or tail entity to corrupt. ReasonKGE [9] with its Iterative Negative Samplin |
| Rescal | ✅ oui | embeddings in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and K |
| TransE | ✅ oui | and relation embeddings in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMul |
| TransOWL | ✅ oui | e sampling for triple classification 5 TransOWL [7] leverages ontology axioms in order |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._