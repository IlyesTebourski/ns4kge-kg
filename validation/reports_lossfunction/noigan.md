# LossFunction — NoiGAN.md

**Titre :** NoiGAN: Noise Aware Knowledge Graph Embedding with GAN

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 2 |
| Trouves automatiquement (TP auto) | 2 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 2 |
| Recall BRUT (avant adjudication) | 50% |
| Recall — vrais oublis | 1 |
| Recall — faux positifs ecartes | 1 |
| **Recall relatif (adjuge)** | **67%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| cross-entropy loss | ✅ oui | formulated as minimizing the following cross entropy loss: $$ \mathcal{L}_D = - \sum_{(h,r, |
| negative sampling loss | ✅ oui | al., 2016). To optimize the KGE model, negative sampling is usually required to minimize the mar |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| margin-based ranking loss | ✅ faux positif (ignore) | Background generique ('usually required to minimize...'). |
| policy gradient | ❌ vrai oubli | Le papier definit SON entrainement du generateur par policy gradient (reward du discriminateur), non extrait. |