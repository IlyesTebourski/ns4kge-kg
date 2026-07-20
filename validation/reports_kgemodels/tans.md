# KGE Models — TANS.md

**Titre :** Unified Interpretation of Smoothing Methods for Negative Sampling Loss Functions in Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 6 |
| Modeles MENTIONNES seulement (hors tableaux) | 7 |
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
| ComplEx | ✅ oui | <td>FB15k-237</td> <td>ComplEx</td> <td>25.0</td> <td> |
| DistMult | ✅ oui | <td>FB15k-237</td> <td>DistMult</td> <td>24.0</td> <td> |
| HAKE | ✅ oui | <td>FB15k-237</td> <td>HAKE</td> <td>33.0</td> <td> |
| HousE | ✅ oui | <td>FB15k-237</td> <td>HousE</td> <td>33.5</td> <td> |
| RotatE | ✅ oui | <td>FB15k-237</td> <td>RotatE</td> <td>33.0</td> <td> |
| TransE | ✅ oui | <td>FB15k-237</td> <td>TransE</td> <td>33.0</td> <td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| BERT | ✅ oui | s, Clark et al. (2020a) indicate that a BERT (Devlin et al., 2019)-like model ELECTR |
| ELECTRA | ✅ oui | a BERT (Devlin et al., 2019)-like model ELECTRA (Clark et al., 2020b) uses the NS loss |
| GenKGC | ✅ oui | ods like KGT5 (Saxena et al., 2022) and GenKGC (Xie et al., 2022) are unique in direct |
| KEPLER | ✅ oui | guage model (PLM)-based approaches like KEPLER (Wang et al., 2021) and SimKGC (Wang et |
| KGT5 | ✅ oui | ning. Generation-based KGC methods like KGT5 (Saxena et al., 2022) and GenKGC (Xie e |
| SimKGC | ✅ oui | hes like KEPLER (Wang et al., 2021) and SimKGC (Wang et al., 2022) also have an import |
| word2vec | ✅ oui | n et al. (2019) import subsampling from word2vec (Mikolov et al., 2013) to KGE. Subsampl |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._