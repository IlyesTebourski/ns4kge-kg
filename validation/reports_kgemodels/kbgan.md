# KGE Models — KBGAN.md

**Titre :** KBGAN: Adversarial Learning for Knowledge Graph Embeddings

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 4 |
| Modeles MENTIONNES seulement (hors tableaux) | 6 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 80% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | re considered in this paper. Except for COMPLEX, all boldface lower case letters repres |
| DistMult | ✅ oui | }\|$</td> </tr> <tr> <td>DISTMULT</td> <td>$\langle \mathbf{h}, \ |
| TransD | ✅ oui | }\|$</td> </tr> <tr> <td>TRANSD</td> <td>$\\|(\mathbf{I} + \math |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TRANSE</td> <td>$\\|\mathbf{h} + \mathb |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ConvE | ✅ oui | o combine the two entities in a triple. CONVE (Dettmers et al., 2017) uses a convolut |
| HolE | ✅ oui | iple as a manifold rather than a point. HOLE (Nickel et al., 2016) employs circular |
| ManifoldE | ✅ oui | ent models achieve strong performances. MANIFOLDE (Xiao et al., 2016) embeds a triple as |
| RESCAL | ✅ oui | graph embedding (KGE) techniques (e.g., RESCAL (Nickel et al., 2011), TRANSE (Bordes e |
| TransH | ✅ oui | ased embedding. Later variants, such as TRANSH (Wang et al., 2014), TRANSR (Lin et al. |
| TransR | ✅ oui | ts, such as TRANSH (Wang et al., 2014), TRANSR (Lin et al., 2015) and TRANSD (Ji et al |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose+table | Xiv:1711.04071v3 [cs.CL] 16 Apr 2018 # KBGAN: Adversarial Learning for Knowledge Gra |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._