# Hardware — BatchNS.md

**Titre :** PyTorch-BigGraph: A Large-scale Graph Embedding System

| Metrique | Valeur |
|---|---|
| Hardware extrait | 1 |
| Trouve automatiquement (TP auto) | 0 |
| Non trouve par l'algo (a verifier) | 1 |
| **Precision automatique** | **0%** |
| Ratés reclasses VALIDES apres verif manuelle | 0 |
| Vraies erreurs d'extraction | 1 |
| **Precision verifiee** | **0%** |
| Candidats faux negatifs recall (dans la prose, non extraits) | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — hardware extrait vs prose

| Hardware extrait | Trouve (algo) ? | Extrait de la prose |
|---|:---:|---|
| 24 Intel Xeon cores (two sockets) with two hyperthreads per core (48 virtual cores), 256 GB RAM | ❌ non | _(non trouve automatiquement)_ |

## Verification manuelle des ratés (adjudication)

Chaque hardware non retrouve par l'algo est verifie a la main contre la prose. Regle stricte : seules les **coquilles averees du papier** (ex. « Teals »->Tesla, « RTX 260 »->2060, modele inexistant) sont reclassees **valides** ; une **reformulation par le KG** ou un identifiant absent de la source compte comme **erreur**. Chaque verdict cite la source.

| Hardware | Verdict | Justification (source citee) |
|---|:---:|---|
| 24 Intel Xeon cores (two sockets) with two hyperthreads per core (48 virtual cores), 256 GB RAM | ❌ vraie erreur | Prose : « 24 Intel Xeon cores (two sockets) and two hyperthreads per core, for a total of 48 virtual cores, and 256 GB of RAM ». Meme machine, mais ce n'est PAS une coquille du papier (contrairement a Teals/RTX 260) : c'est le KG qui a REFORMULE le libelle (« and »->« with », « for a total of 48 »->« (48 »). Choix strict : on ne credite que le verbatim et les coquilles averees du papier -> comptee comme 1 erreur de precision. |

## Recall — hardware dans la prose mais NON extrait

_Aucun candidat._