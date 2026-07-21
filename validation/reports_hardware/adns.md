# Hardware — ADNS.md

**Titre :** Affinity Dependent Negative Sampling for Knowledge Graph Embeddings

| Metrique | Valeur |
|---|---|
| Hardware extrait | 2 |
| Trouve automatiquement (TP auto) | 1 |
| Non trouve par l'algo (a verifier) | 1 |
| **Precision automatique** | **50%** |
| Ratés reclasses VALIDES apres verif manuelle | 1 |
| Vraies erreurs d'extraction | 0 |
| **Precision verifiee** | **100%** |
| Candidats faux negatifs recall (dans la prose, non extraits) | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — hardware extrait vs prose

| Hardware extrait | Trouve (algo) ? | Extrait de la prose |
|---|:---:|---|
| i7 4770 | ✅ oui | achieved with a hardware of 16 GB ram, i7 4770 processor and Nvidia RTX 260 GPU. The e |
| Nvidia RTX 2060 | ❌ non | _(non trouve automatiquement)_ |

## Verification manuelle des ratés (adjudication)

Chaque hardware non retrouve par l'algo est verifie a la main contre la prose. Regle stricte : seules les **coquilles averees du papier** (ex. « Teals »->Tesla, « RTX 260 »->2060, modele inexistant) sont reclassees **valides** ; une **reformulation par le KG** ou un identifiant absent de la source compte comme **erreur**. Chaque verdict cite la source.

| Hardware | Verdict | Justification (source citee) |
|---|:---:|---|
| Nvidia RTX 2060 | ✅ valide (pas une erreur KG) | Le papier ecrit litteralement « i7 4770 processor and Nvidia RTX 260 GPU » — coquille du papier : la « RTX 260 » n'existe pas, il s'agit de la RTX 2060. Le KG a restitue le bon device. Ecart du a l'erreur du PAPIER, pas du KG. |

## Recall — hardware dans la prose mais NON extrait

_Aucun candidat._