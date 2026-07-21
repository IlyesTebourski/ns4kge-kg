# NS Methods — DMNS.md

**Titre :** Diffusion-based Negative Sampling on Graphs for Link Prediction

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 6 |
| Methodes MENTIONNEES seulement (prose) | 2 |
| Precision evalues | 83% | 
| Precision mentionnes | 100% |
| Recall evalues | 83% |
| Recall mentionnes | 67% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Conditional Diffusion-based Multi-level Negative Sampling | ✅ | name | om the latent space. Our method, called Conditional Diffusion-based Multi-level Negative Sampling (DMNS), leverages the |
| Dynamic Negative Sampling | ✅ | name | egative nodes, such as popularity [30], dynamic selections based on current predictions |
| KBGAN | ✅ | name | sampling. Among them, GraphGAN [46] and KBGAN [5] learns a distribution over negative |
| Markov Chain Monte Carlo Negative Sampling | ❌ |  | _(absent)_ |
| Popularity-based Negative Sampling | ✅ | name | to select hard negative nodes, such as popularity [30], dynamic selections based on curre |
| Uniform Negative Sampling | ✅ | name | ol the quality of negative nodes. While uniform negative sampling [14, 44] is simple, i |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| MixGCF | ✅ | name | ve examples from $k$-hop neighborhoods. MixGCF [20] synthesizes hard negative examples |
| Subgraph-based Negative Sampling | ✅ | name | ts the representations of the enclosing subgraphs. For example, SEAL [53] proposes the us |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| DMNS | prose+table | name | on-based Multi-level Negative Sampling (DMNS), leverages the Markov chain property o |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| SANS | prose | name | g high-variance samples [9]. On graphs, SANS [2] select negative examples from $k$-h |