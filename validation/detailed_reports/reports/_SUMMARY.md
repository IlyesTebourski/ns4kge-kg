# Recap global de validation KG vs articles

Articles valides : **55**

## Par article

| Article | TP | FP | Precision | Candidats FN | Recall~ |
|---|---:|---:|:---:|---:|:---:|
| AdaptativeNS.md | 24 | 2 | 92% | 15 | 62% |
| ADNS.md | 22 | 0 | 100% | 13 | 63% |
| ASA.md | 23 | 2 | 92% | 18 | 56% |
| BatchNS.md | 18 | 5 | 78% | 16 | 53% |
| CAKE.md | 26 | 1 | 96% | 24 | 52% |
| CANS.md | 18 | 3 | 86% | 16 | 53% |
| CCS.md | 35 | 1 | 97% | 27 | 56% |
| ConceptDriven.md | 14 | 5 | 74% | 19 | 42% |
| CondConstraints.md | 9 | 10 | 47% | 7 | 56% |
| dans.md | 22 | 2 | 92% | 35 | 39% |
| DeMix.md | 23 | 0 | 100% | 30 | 43% |
| DHNS.md | 36 | 4 | 90% | 21 | 63% |
| DMNS.md | 19 | 4 | 83% | 23 | 45% |
| DNS.md | 18 | 0 | 100% | 20 | 47% |
| DomainNS.md | 19 | 3 | 86% | 20 | 49% |
| EANS.md | 19 | 2 | 90% | 25 | 43% |
| ERDNS.md | 28 | 3 | 90% | 11 | 72% |
| eTruncatedUNS.md | 19 | 2 | 90% | 14 | 58% |
| GHN.md | 28 | 2 | 93% | 11 | 72% |
| GibbsNS.md | 26 | 3 | 90% | 26 | 50% |
| GNDN.md | 20 | 7 | 74% | 17 | 54% |
| GNS.md | 15 | 1 | 94% | 17 | 47% |
| GraphGAN.md | 14 | 1 | 93% | 16 | 47% |
| HaSa.md | 22 | 2 | 92% | 14 | 61% |
| HTENS.md | 15 | 3 | 83% | 17 | 47% |
| IGAN.md | 17 | 7 | 71% | 16 | 52% |
| KBGAN.md | 16 | 6 | 73% | 19 | 46% |
| KSGAN.md | 23 | 5 | 82% | 12 | 66% |
| LAS.md | 42 | 2 | 95% | 25 | 63% |
| LEMON.md | 17 | 3 | 85% | 21 | 45% |
| Localcognitive.md | 25 | 4 | 86% | 13 | 66% |
| LTS.md | 21 | 5 | 81% | 11 | 66% |
| M2ixKG.md | 16 | 2 | 89% | 24 | 40% |
| MCNS.md | 25 | 0 | 100% | 28 | 47% |
| MDNCaching.md | 16 | 0 | 100% | 19 | 46% |
| NMiss.md | 19 | 0 | 100% | 13 | 59% |
| NoiGAN.md | 22 | 22 | 50% | 14 | 61% |
| NSCaching.md | 26 | 3 | 90% | 25 | 51% |
| PNS.md | 8 | 3 | 73% | 4 | 67% |
| RAAKGC.md | 42 | 1 | 98% | 16 | 72% |
| RandomCorrupt.md | 18 | 1 | 95% | 5 | 78% |
| RCWC.md | 20 | 8 | 71% | 13 | 61% |
| ReasonKGE.md | 17 | 1 | 94% | 24 | 41% |
| RUGA.md | 19 | 4 | 83% | 10 | 66% |
| SANS.md | 14 | 5 | 74% | 27 | 34% |
| SelfAdv.md | 27 | 3 | 90% | 16 | 63% |
| SNS.md | 19 | 0 | 100% | 16 | 54% |
| SparseNSG.md | 22 | 2 | 92% | 5 | 81% |
| STC.md | 16 | 16 | 50% | 14 | 53% |
| TANS.md | 27 | 11 | 71% | 13 | 68% |
| TruncatedNS.md | 29 | 1 | 97% | 11 | 72% |
| TuckerDNCaching.md | 27 | 2 | 93% | 23 | 54% |
| TypeAugmented.md | 35 | 2 | 95% | 15 | 70% |
| TypeConstraints.md | 12 | 2 | 86% | 14 | 46% |
| Uniform.md | 10 | 3 | 77% | 14 | 42% |

## Totaux

| Metrique | Valeur |
|---|---|
| Total TP (extraites & trouvees) | 1179 |
| Total FP (extraites & absentes) | 192 |
| Total candidats faux negatifs | 952 |
| **Precision micro** (toutes entites confondues) | **86.0%** |
| **Precision macro** (moyenne des articles) | **86.2%** |
| **Recall relatif micro** (indicatif) | **55.3%** |
| **Recall relatif macro** (indicatif) | **55.6%** |

> Le recall est **indicatif** : les 'candidats faux negatifs' sont des entites du vocabulaire global presentes dans le texte mais non extraites pour cet article. Certaines sont de vrais oublis, d'autres de simples mentions (related work, etc.) — a valider a la main.