# KGE Models — TypeConstraints.md

**Titre :** Type-Constrained Representation Learning in Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 3 |
| Recall BRUT evalues / mentionnes | 100% / 50% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| mwNN | ✅ oui | omparison of AUPRC and AUROC result for mwNN [8] with and without exploiting prior k |
| RESCAL | ✅ oui | omparison of AUPRC and AUROC result for RESCAL with and without exploiting prior knowl |
| TransE | ✅ oui | omparison of AUPRC and AUROC result for TransE with and without exploiting prior knowl |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| Neural Tensor Network | ✅ oui | deling of KGs. [20] recently proposed a neural tensor network, which we did not consider in our study |
| TransH | ✅ oui | network proposed in [20]. [23] proposed TransH which improves TransE’s capability to m |
| TransR | ✅ oui | further extended in [14] by introducing TransR which separates representations of enti |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | ariable models have increasingly gained attention for the statistical modeling of knowled |
| SME | prose | sup>9</sup> https://github.com/glorotxa/SME <sup>10</sup> Mainly caused by the rank |
| Unstructured | prose | posed to support triple extraction from unstructured web documents. The confidence value $\t |