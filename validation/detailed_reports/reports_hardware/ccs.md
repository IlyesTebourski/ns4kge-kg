# Hardware — CCS.md

**Titre :** Op-Trans: An Optimization Framework for Negative Sampling and Triplet-Mapping Properties in Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Hardware extrait | 1 |
| Trouve automatiquement (TP auto) | 0 |
| Non trouve par l'algo (a verifier) | 1 |
| **Precision automatique** | **0%** |
| Ratés reclasses VALIDES apres verif manuelle | 1 |
| Vraies erreurs d'extraction | 0 |
| **Precision verifiee** | **100%** |
| Candidats faux negatifs recall (dans la prose, non extraits) | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — hardware extrait vs prose

| Hardware extrait | Trouve (algo) ? | Extrait de la prose |
|---|:---:|---|
| Tesla P100 GPU 16GB RAM | ❌ non | _(non trouve automatiquement)_ |

## Verification manuelle des ratés (adjudication)

Chaque hardware non retrouve par l'algo est verifie a la main contre la prose. Regle stricte : seules les **coquilles averees du papier** (ex. « Teals »->Tesla, « RTX 260 »->2060, modele inexistant) sont reclassees **valides** ; une **reformulation par le KG** ou un identifiant absent de la source compte comme **erreur**. Chaque verdict cite la source.

| Hardware | Verdict | Justification (source citee) |
|---|:---:|---|
| Tesla P100 GPU 16GB RAM | ✅ valide (pas une erreur KG) | Le papier ecrit « ran on a single Teals P100 GPU with 16 GB RAM » — coquille vendeur « Teals » pour « Tesla ». Le modele (P100) et la RAM (16 GB) sont corrects et presents verbatim. Ecart du a la coquille du PAPIER, pas du KG. |

## Recall — hardware dans la prose mais NON extrait

_Aucun candidat._