# KGE Models — SelfAdv.md

**Titre :** RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 7 |
| Modeles MENTIONNES seulement (hors tableaux) | 5 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 88% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | \overline{\cdot}$ denotes conjugate for complex vectors, and 2D reshaping for real vect |
| ConvE | ✅ oui | s, and 2D reshaping for real vectors in ConvE model. TransX represents a wide range o |
| DistMult | ✅ oui | \in R^k$</td> </tr> <tr> <td>DistMult (Yang et al., 2014)</td> <td>$\la |
| HolE | ✅ oui | \in C^k$</td> </tr> <tr> <td>HolE (Nickel et al., 2016)</td> <td>$\ |
| pRotatE | ✅ oui | <td>.956</td> </tr> <tr> <td>pRotatE</td> <td>43</td> <td><b>.79 |
| RotatE | ✅ oui | \in R^k$</td> </tr> <tr> <td>RotatE</td> <td>$-\\|h \circ r - t\\|^2$</ |
| TransE | ✅ oui | odel. TransX represents a wide range of TransE’s variants, such as TransH (Wang et al. |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| KG2E | ✅ oui | We also compare an additional approach KG2E_KL (He et al., 2015), which is a probab |
| STransE | ✅ oui | 2014), TransR (Lin et al., 2015b), and STransE (Nguyen et al., 2016), where $g_{r,i}(\ |
| TorusE | ✅ oui | and concurrent work to our work is the TorusE (Ebisu & Ichise, 2018) model, which def |
| TransH | ✅ oui | ide range of TransE’s variants, such as TransH (Wang et al., 2014), TransR (Lin et al. |
| TransR | ✅ oui | ts, such as TransH (Wang et al., 2014), TransR (Lin et al., 2015b), and STransE (Nguye |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| SE | table | </thead> <tbody> <tr> <td>SE (Bordes et al., 2011)</td> <td>$- |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._