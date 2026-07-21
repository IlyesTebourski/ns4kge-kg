# NS Methods — DHNS.md

**Titre :** Diffusion-based Hierarchical Negative Sampling for Multimodal Knowledge Graph Completion

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 8 |
| Methodes MENTIONNEES seulement (prose) | 3 |
| Precision evalues | 100% | 
| Precision mentionnes | 100% |
| Recall evalues | 89% |
| Recall mentionnes | 43% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Bernoulli Negative Sampling | ✅ | name | ding to ambiguous training signals [4]. Bernoulli sampling [31] employs a Bernoulli distr |
| Diffusion-based Hierarchical Negative Sampling | ✅ | name | Xiv:2501.15393v1 [cs.AI] 26 Jan 2025 # Diffusion-based Hierarchical Negative Sampling for Multimodal Knowle |
| KBGAN | ✅ | name | nerate higher-quality negative triples. KBGAN [4] and IGAN [30] use Generative Advers |
| MANS | ✅ | name | lenging negatives from multimodal data. MANS [37] emphasizes modality-aware NS to al |
| MMRNS | ✅ | name | or generating diverse negative triples. MMRNS [34] introduces a relation-enhanced NS |
| NSCaching | ✅ | name | E models to distinguish from positives. NSCaching [40] utilizes additional memory to stor |
| SANS | ✅ | name | ality negative triples during training. SANS [1] leverages graph structure informati |
| Uniform Negative Sampling | ✅ | name | th MMKGC and NS performances, including uniform sampling (Uniform) [3], Bernoulli sampl |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| DMNS | ✅ | name | riginal data. In graph-structured data, DMNS[21] employs DDPM to generate negative n |
| IGAN | ✅ | name | quality negative triples. KBGAN [4] and IGAN [30] use Generative Adversarial Network |
| NS-KGE | ✅ | name | ing (NSCach) [40], KBGAN [4], SANS [1], NS-KGE [13], MANS [37] and MMRNS [34]. **Impl |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Self-adversarial Negative Sampling | prose+table | acro | ality negative triples during training. SANS [1] leverages graph structure informati |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Adaptive Negative Sampling | prose | name | rthermore, we develop a Negative Triple-Adaptive Training (NTAT) strategy that dynamical |
| Adversarial Negative Sampling | prose | name | KBGAN [4] and IGAN [30] use Generative Adversarial Networks (GANs) to select harder negati |
| GAN-based Negative Sampling | prose | name | sed on generative adversarial networks (GANs) [4] or self-adversarial strategies [25 |
| Probabilistic Negative Sampling | prose | name | s, particularly the Denoising Diffusion Probabilistic Model (DDPM) [9], have become pivotal i |