# KGE Models — CAKE.md

**Titre :** CAKE: A Scalable Commonsense-Aware Framework For Multi-View Knowledge Graph Completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 5 |
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
| HAKE | ✅ oui | ng></td> </tr> <tr> <td>HAKE</td> <td>34</td> <td>0. |
| RotatE | ✅ oui | ng></td> </tr> <tr> <td>RotatE</td> <td>35</td> <td>0. |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>35</td> <td>0. |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | se together with the characteristics of complex relations. Furthermore, a multi-view li |
| DistMult | ✅ oui | osition-based** score function, such as DistMult (Yang et al., 2015): $$E(h, r, t) = \m |
| JOIE | ✅ oui | hand, although some KGE models such as JOIE (Hao et al., 2019) employ the ontology |
| RESCAL | ✅ oui | s such as TransE (Bordes et al., 2013), RESCAL (Nickel et al., 2011), ComplEx (Trouill |
| TransH | ✅ oui | amely 1-1, 1-N, N-1, and N-N defined in TransH (Wang et al., 2014) for negative sampli |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._