# NS Methods — ReasonKGE.md

**Titre :** Improving Knowledge Graph Embeddings with Ontological Reasoning

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 3 |
| Methodes MENTIONNEES seulement (prose) | 6 |
| Precision evalues | 100% | 
| Precision mentionnes | 100% |
| Recall evalues | 100% |
| Recall mentionnes | 50% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Random Negative Sampling | ✅ | name | ve triples is done either completely at random [9], relying on the (local) closed worl |
| ReasonKGE | ✅ | name | we present a novel iterative approach *ReasonKGE* that identifies dynamically via symbol |
| Static Sampling | ✅ | name | Therefore, instead of pre–computing a static set of negative examples, we propose to |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Distributional Negative Sampling | ✅ | name | d assumption [27]. Alternatives include Distributional Negative Sampling (DNS) [12] and its va |
| Near Miss Sampling | ✅ | name | approach [30]. *Nearest Neighbor* and *Near Miss sampling* [21] resp. exploit a pre-trai |
| Nearest Neighbor Sampling | ✅ | name | n or triple corruption approach [30]. *Nearest Neighbor* and *Near Miss sampling* [21] resp. ex |
| NSCaching | ✅ | name | samples from a node’s neighborhood. The NSCaching sampling method [40] suggests to sample |
| Structure-Aware Negative Sampling | ✅ | name | egative sampling. The work [1] presents structure-aware negative sampling (SANS), which utilize |
| Type-Constrained Negative Sampling | ✅ | name | nother related method is concerned with type-constrained negative sampling [22]. Given a triple |

## C1. Recall EVALUES — dans un tableau mais non extrait

_Aucun._

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Adversarial Negative Sampling | prose | name | ction concerns making use of Generative Adversarial Networks (GANs) [39,35,10] for negative |
| Domain-based Negative Sampling | prose | name | they utilized such ontology axioms as *Domain*, *Range*, *Functional*, and *Disjointn |
| GAN-based Negative Sampling | prose | name | use of Generative Adversarial Networks (GANs) [39,35,10] for negative sampling. The |
| Iterative Negative Sampling | prose | name | nutshell # 3 Ontological Reasoning for Iterative Negative Sampling While a variety of e |
| SANS | prose | name | ents structure-aware negative sampling (SANS), which utilizes the graph structure by |
| Local-Closed World Assumption Negative Sampling | prose | acro | on the (local) closed world assumption (LCWA). Based on CWA all triples not present |