# Configurations — noigan

**Titre :** NoiGAN: Noise Aware Knowledge Graph Embedding with GAN

| Metrique | Valeur |
|---|---|
| Configs verifiees | 344 |
| Valeur existe dans les tables | 343/344 |
| **① Accuracy — valeur existe** | **99.7%** |
| Combinaison (dataset/metric/model/ns) correcte | 327/344 |
| **② Accuracy — combinaison correcte** | **95.1%** |
| **③ 🐤 Canari attrape** | **1/1 — ✅ fiable** |

## Configs fautives (combinaison incorrecte)

| # | Dataset | Metric | KGEModel | NS | Valeur | Valeur existe ? |
|---|---|---|---|---|---|:--:|
| 66 | FB15K-237 | MRR |  | KBGAN | 0.266 | ✅ oui (mal associee) |
| 67 | FB15K-237 | Hits@1 |  | KBGAN | 0.186 | ✅ oui (mal associee) |
| 68 | FB15K-237 | Hits@3 |  | KBGAN | 0.29 | ✅ oui (mal associee) |
| 69 | FB15K-237 | Hits@10 |  | KBGAN | 0.427 | ✅ oui (mal associee) |
| 70 | YAGO3-10 | MRR |  | KBGAN | 0.071 | ✅ oui (mal associee) |
| 71 | YAGO3-10 | Hits@1 |  | KBGAN | 0.041 | ✅ oui (mal associee) |
| 72 | YAGO3-10 | Hits@3 |  | KBGAN | 0.07 | ✅ oui (mal associee) |
| 73 | YAGO3-10 | Hits@10 |  | KBGAN | 0.124 | ✅ oui (mal associee) |
| 74 | WN18RR | MRR |  | KBGAN | 0.215 | ✅ oui (mal associee) |
| 75 | WN18RR | Hits@1 |  | KBGAN | 0.036 | ✅ oui (mal associee) |
| 76 | WN18RR | Hits@3 |  | KBGAN | 0.356 | ✅ oui (mal associee) |
| 77 | WN18RR | Hits@10 |  | KBGAN | 0.507 | ✅ oui (mal associee) |
| 78 | FB15K-237 | MRR | Attention | Unknown | 0.436 | ❌ non (absente) |
| 182 | FB15K-237 | MRR |  | KBGAN | 0.177 | ✅ oui (mal associee) |
| 183 | FB15K-237 | Hits@1 |  | KBGAN | 0.079 | ✅ oui (mal associee) |
| 184 | FB15K-237 | Hits@3 |  | KBGAN | 0.214 | ✅ oui (mal associee) |
| 185 | FB15K-237 | Hits@10 |  | KBGAN | 0.363 | ✅ oui (mal associee) |
