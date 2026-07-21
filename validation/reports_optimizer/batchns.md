# Optimizer — BatchNS.md

**Titre :** PyTorch-BigGraph: A Large-scale Graph Embedding System

| Metrique | Valeur |
|---|---|
| Optimizer extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (indicatif)** | **100%** |

## Precision automatique — Optimizer extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| AdaGrad | ✅ oui | stic gradient descent (SGD). We use the Adagrad optimizer, and sum the accumulated grad |

## Recall — Optimizer du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Adam | ⚠️ A VERIFIER | : A LARGE-SCALE GRAPH EMBEDDING SYSTEM Adam Lerer <sup>1</sup> Ledell Wu <sup>1</su |
| SGD | ⚠️ A VERIFIER | parameters are performed via minibatch stochastic gradient descent (SGD). We use the Adagrad optimizer, an |