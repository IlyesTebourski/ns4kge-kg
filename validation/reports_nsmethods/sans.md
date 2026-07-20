# NS Methods — SANS.md

**Titre :** Structure Aware Negative Sampling in Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 8 |
| Methodes MENTIONNEES seulement (prose) | 3 |
| Precision evalues | 50% | 
| Precision mentionnes | 67% |
| Recall evalues | 40% |
| Recall mentionnes | 67% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| KBGAN | ✅ | name | egative sampling (Bordes et al., 2013), KBGAN (Cai and Wang, 2018), and NSCaching (Zh |
| NSCaching | ✅ | name | train compared to GAN-based methods is NSCaching (Zhang et al., 2019), which involves us |
| Self-Adversarial Negative Sampling | ✅ | name | sy negatives, Sun et al. (2019) propose Self-Adversarial negative sampling, which weighs each sa |
| Self-Adversarial Random Walk Structure Aware Negative Sampling | ❌ |  | _(absent)_ |
| Self-Adversarial Structure Aware Negative Sampling | ❌ |  | _(absent)_ |
| Uniform Negative Sampling | ✅ | name | o simple corruption distributions, i.e. uniform, yielding easy uninformative negatives |
| Uniform Random Walk Structure Aware Negative Sampling | ❌ |  | _(absent)_ |
| Uniform Structure Aware Negative Sampling | ❌ |  | _(absent)_ |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Noise Contrastive Estimation | ✅ | name | andscape as simple random sampling—e.g. Noise Contrastive Estimation (NCE) (Gutmann and Hyvärinen, 2010)—pro |
| Random Walk Structure Aware Negative Sampling | ❌ |  | _(absent)_ |
| Structure Aware Negative Sampling | ✅ | name | rXiv:2009.11355v2 [cs.LG] 7 Oct 2020 # Structure Aware Negative Sampling in Knowledge Graphs |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| RW-SANS | prose+table | name | combat this inefficiency, we introduce RW-SANS in Alg. 1, which uses $\omega$ random w |
| SANS | prose+table | name | pose Structure Aware Negative Sampling (SANS), an inexpensive negative sampling stra |
| Self-Adv | prose+table | name | to this technique as *Self-Adversarial (Self-Adv.) SANS*, whereas the former approach is |
| Self-Adv. RW-SANS | prose+table | name | ted in Table 2 under Self-Adv. SANS and Self-Adv. RW-SANS, both of which reweigh the negative tri |
| Self-Adv. SANS | table | name | ng></td> </tr> <tr> <td>Self-Adv. SANS (ours)</td> <td><strong>52.03</ |
| Uniform SANS | prose+table | name | the former approach is referred to as *Uniform SANS*. **Algorithm 1** Approximating the $k |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Uniform RW-SANS | prose | name | heme. Figure 2: The performance of Uniform RW-SANS with TransE on FB15K-237 using differen |