# Validation croisée par LLM-juge des configurations expérimentales

**Projet :** ns4kge — Knowledge Graph d'articles sur le Negative Sampling pour les KGE
**Objet :** vérification automatique indépendante des 6 567 configurations numériques extraites
**Juge :** GPT‑5.6 Terra (OpenAI) — indépendant du modèle de peuplement (Claude)
**Périmètre :** 55 articles · 6 567 configurations · vérification 100 % automatique

---

## 1. Résumé exécutif

Un **second LLM, indépendant** du pipeline d'extraction, vérifie chaque configuration
extraite (croisement *dataset × metric × KGE model × NS method → valeur*) directement
contre les **tableaux bruts** de l'article. Sur les 6 567 configurations :

| Métrique | Résultat (micro, global) |
|---|---|
| ① La valeur existe dans les tableaux | **99.9 %** (6 562 / 6 567) |
| ② La combinaison est correctement associée à la valeur | **99.5 %** (6 533 / 6 567) — *brut* |
| ② après adjudication manuelle des écarts | **99.92 %** (6 562 / 6 567) |
| ③ Canaris (sanity anti-tamponnage) attrapés | **54 / 55 articles** |

Le chiffre brut de 99.5 % signale **34 configurations**. Leur adjudication montre que
**5 seulement sont de vraies imprécisions d'extraction** ; les **29 autres sont des faux
positifs du juge**, dus à ses limites de localisation dans des tableaux à structure
complexe (lignes labellisées par méthode, rowspan imbriqués). La précision réelle du
pipeline sur l'association *combinaison → valeur* est donc de **99.92 %**.

> Un score inférieur à 100 % est ici un **gage de crédibilité** : le validateur détecte
> réellement des écarts (il ne tamponne pas), et le canari indépendant confirme article
> par article qu'il sait attraper une erreur injectée.

---

## 2. Contexte et objectif

Le pipeline extrait, pour chaque article, un ensemble de **configurations
expérimentales**. Chaque configuration associe cinq descripteurs à une valeur numérique :

```
{ Dataset, Task, Metric, KGEModel, NSMethod }  →  result
```

Une première validation (par entité : datasets, metrics, KGE models, NS methods…) contrôle
la **justesse des entités** extraites. Elle ne dit rien sur la **cohérence des tuples ni des
valeurs numériques**. La présente validation comble ce trou : elle vérifie que chaque
valeur numérique est **réelle** et **correctement associée** à sa combinaison de descripteurs,
telle qu'imprimée dans les tableaux de résultats du papier.

**Le rappel n'est volontairement pas mesuré** : le pipeline n'extrait pas toutes les lignes
de tous les tableaux, par conception. On mesure la **précision** de ce qui a été extrait.

---

## 3. Méthodologie

### 3.1 Principe : un juge indépendant

Le peuplement du graphe a été réalisé avec **Claude**. Pour éviter qu'un modèle valide ses
propres angles morts, le vérificateur est d'une **famille différente** : **GPT‑5.6 Terra**
(OpenAI). Le juge ne reçoit **que** les tableaux et les configurations — jamais le
raisonnement du pipeline.

### 3.2 Choix du modèle

- **Indépendance** : extraction = Claude → juge = GPT (non‑Claude).
- **GPT‑4o** n'est plus disponible via l'API (retiré le 16/02/2026) ; la gamme actuelle est
  la famille GPT‑5.6 (Luna / Terra / Sol).
- **Luna** (le tier économique) produisait des **faux « tuple absent »** sur les en‑têtes
  multi‑niveaux. Le passage à **Terra** (tier équilibré) les a supprimés. Coût total du run
  complet : de l'ordre de **1 $**.

### 3.3 Entrées

- **Source = les JSON `*_merged.json`** (jamais les TTL). La normalisation des pourcentages
  vers [0,1] a lieu **au passage JSON→TTL** (déterministe, hors périmètre) ; le JSON conserve
  la valeur **verbatim** du tableau, ce qui permet une comparaison directe.
- **Tableaux = extraits bruts** des articles (blocs `<table>` HTML + légendes), non réécrits :
  chaque tableau ayant une forme différente, tout « nettoyage » automatique risquerait de
  perdre une colonne. On préfère laisser le juge lire la forme d'origine.

### 3.4 Représentation minimaliste (déterministe)

Les configurations sont transmises au juge sous forme compacte : la **Task** (constante par
tableau) est factorisée en tête de section, le reste par ligne, avec un identifiant = index
d'origine dans le JSON (pour le remapping) :

```
== task: Link Prediction ==
id|dataset|metric|model|ns|val
0|WN18RR|MRR|RotatE|Unknown|0.476
1|WN18RR|MRR|MuRP|Unknown|0.477
...
```

Cette transformation JSON→forme minimaliste est **100 % déterministe** (recopie de chaînes,
aucun LLM). Le surcoût de tokens est faible : préambule fixe (~600 tokens) + le bloc de
configurations. Le plus gros article (cake, 320 configs) tient sous **~9 000 tokens** en entrée.

### 3.5 Les deux vérifications et la définition de « correct »

Une cellule de tableau de résultats n'encode que **trois coordonnées** (dataset, metric,
model) **+ une valeur** : il n'existe généralement ni colonne NS ni colonne Task. Le juge
effectue donc, par configuration, **deux contrôles** :

- **(A) La valeur existe** — le nombre apparaît‑il quelque part dans les tableaux ?
  *(distingue une valeur hallucinée d'une valeur réelle)*
- **(B) La combinaison est correcte** — le nombre est‑il à la **bonne cellule**, c'est‑à‑dire
  la cellule `(dataset, metric, model)` existe et vaut cette valeur, avec la NS cohérente ?

Une configuration est **correcte ⟺ (B)** (et alors (A) l'est nécessairement). Une
configuration peut avoir **(A) vrai mais (B) faux** : la valeur est réelle mais rattachée à la
**mauvaise combinaison** (bon nombre, mauvais dataset par exemple).

**NSMethod / Task :**
- `NSMethod = "Unknown"` est **toujours accepté** (le tableau n'a pas de colonne NS) ; une NS
  *spécifique* n'est fautive que si le tableau la contredit clairement.
- `Task` est **ignorée** ici (elle est contrôlée par la validation d'entités).

### 3.6 Comparaison numérique

Tolérance de **forme uniquement**, jamais de rééchelonnage :
`26.96 == "26.96%"` (on retire le signe `%`), `0.43 == 0.430` (zéros/arrondis), mais
`0.43 ≠ 43` (pas de ×100 — cette normalisation appartient au TTL, hors périmètre).

### 3.7 Règles de lecture des tableaux (durcies)

Le juge est explicitement instruit des schémas « pièges » rencontrés :
- **en‑têtes multi‑niveaux** (`colspan`) : mapper chaque cellule à (dataset = groupe de tête,
  metric = sous‑colonne) ;
- **abréviations / coquilles** : `H@1 == Hits@1`, `WN8RR == WN18RR`, `MuRp == MuRP` ;
- **ligne « méthode proposée »** : souvent labellisée `Proposed` / `Ours` / l'acronyme du
  papier, **pas** par le nom du modèle → utiliser la NS pour choisir la bonne ligne ;
- **rowspan imbriqué** : un modèle chapeautant plusieurs sous‑lignes (une par NS) → apparier
  `(model, ns)` à la bonne sous‑ligne.

### 3.8 Sortie et rapport

Le juge ne renvoie que les **anomalies** (report‑by‑exception) : `[{"id":i,"exists":bool}]`,
et `[]` si tout est correct. La sortie **scale avec le nombre d'erreurs**, pas avec le nombre
de configurations. Un script **déterministe** transforme ensuite cette réponse en rapports
lisibles (`.md`, `.json`, `_SUMMARY.md`).

### 3.9 Canari anti‑tamponnage (sanity par article)

Pour prouver, **article par article**, que le juge discrimine (et ne valide pas tout
aveuglément), une **fausse configuration déterministe** est injectée dans chaque appel,
indiscernable d'une vraie ligne (id séquentiel, valeur plausible). Il s'agit d'un **swap de
dataset** : une vraie valeur du tableau placée à la **mauvaise cellule** (repli sur
valeur×0.7 si aucun swap possible). Si le juge la signale, il a prouvé qu'il sait localiser
correctement. Le canari est retiré des statistiques réelles.

---

## 4. Résultats globaux

| Métrique | Valeur | Détail |
|---|---|---|
| Configurations vérifiées | **6 567** | 55 articles |
| ① La valeur existe | **99.9 %** | 6 562 / 6 567 |
| ② Combinaison correcte (brut) | **99.5 %** | 6 533 / 6 567 |
| ② Combinaison correcte (adjugé) | **99.92 %** | 6 562 / 6 567 |
| ③ Canaris attrapés | **54 / 55** | seul `eans` échoue (voir §6) |

**Observation clé.** Les 5 seules configurations à `valeur existe = faux` sont **exactement**
les 5 vraies imprécisions d'extraction. Toutes les autres configurations signalées (29) ont
`valeur existe = vrai` : leur valeur est réelle, seul le juge n'a pas su la localiser. La
métrique ① sépare donc, à elle seule, le **vrai signal** (imprécision réelle) du **bruit du
juge** (faux positif de localisation).

---

## 5. Adjudication des 34 configurations signalées

Chaque écart signalé par le juge a été vérifié **à la main** contre le tableau source.

| Catégorie | Nb | Nature |
|---|---:|---|
| **N — vraies imprécisions d'extraction** | **5** | valeur absente des tableaux |
| **M — limites de localisation du juge (faux positifs)** | **29** | valeur réelle, correctement placée, mal localisée par le juge |
| **Total signalé** | **34** | |

### 5.1 N — Vraies imprécisions d'extraction (5)

| Article | Configs | Cas |
|---|---|---|
| `localcognitive` | #57, #61, #77, #81 (4) | `result = None` — **valeur manquante** (Hits@1 / Hits@3 non extraits) |
| `noigan` | #78 (1) | `FB15K‑237 / MRR / Attention = 0.436` — la valeur **n'apparaît dans aucun tableau** |

Ces 5 cas sont de véritables lacunes : soit une valeur nulle, soit une valeur qui ne se
retrouve pas dans les tableaux de résultats. Ce sont les seuls écarts imputables au pipeline.

### 5.2 M — Faux positifs du juge (29)

Dans les 29 cas, la valeur extraite est **réelle et correctement placée** ; le juge n'a pas
su la relier à la bonne ligne à cause de la structure du tableau. Trois schémas :

**(a) Ligne labellisée par méthode NS, pas par modèle — `gns` (3)**
Table FB13 : lignes `UNS`, `PTNS`, `GNS`. Le pipeline a correctement associé
`ns=Uniform → UNS = 0.5182`, `ns=Pseudo Typed → PTNS = 0.8972`, `ns=Good → GNS = 0.9013`
(la proposée, en gras). Le juge cherchait `KGEModel = KG‑BERT` (absent du tableau, c'est le
modèle de base implicite) et n'a pas relié.

**(b) Ligne « méthode » sans modèle de base (KBGAN) — `hasa` (4) + `noigan` (16) = 20**
Le tableau contient une ligne `KBGAN [4]` (KBGAN est une méthode de NS concurrente), avec ses
valeurs (ex. MRR `0.277`, Hits@10 `0.458`). Le pipeline a correctement extrait ces valeurs
sous `ns=KBGAN` avec un `KGEModel` **vide** (la ligne ne mentionne pas de modèle de base). Le
juge, exigeant un modèle pour localiser la cellule, n'a pas pu confirmer — alors que la
valeur est exacte.

**(c) Rowspan imbriqué — `ccs` (6)**
Table à `<td rowspan="4">TransR</td>` chapeautant quatre sous‑lignes (une par méthode :
Bernoulli, KBGAN, NSCaching, …). Les six valeurs `TransR / NSCaching`
(`3639, 0.201, 0.4822, 181, 0.2751, 0.4773`) **existent toutes** dans la sous‑ligne
correspondante ; le juge a mal navigué la structure imbriquée.

> Note méthodologique : le durcissement du prompt (schémas *proposed‑row* et *rowspan*) a
> déjà ramené l'article `cans` de 66.7 % à 100 % (18 faux positifs corrigés). Les schémas (a),
> (b), (c) résiduels illustrent les limites de localisation d'un LLM sur les tableaux
> scientifiques les plus tordus.

---

## 6. Le cas `eans` — canari non attrapé (1 / 55)

Sur `eans`, le canari injecté n'a **pas** été signalé par le juge (0/1), y compris après une
seconde exécution. La sanity **échoue** pour cet article : son score de 100 % (aucune
anomalie sur ses 180 configurations réelles) **ne peut pas être confirmé** par le mécanisme
de canari. Aucune vraie erreur n'y a été trouvée, mais l'article est signalé comme **« à
vérifier »** par transparence — le canari a rempli son rôle de détecteur de non‑fiabilité.

---

## 7. Limites et menaces à la validité

- **Taux d'erreur propre du juge.** Le juge n'est pas parfait : 29 faux positifs de
  localisation, et 1 canari raté sur 55. La validation croisée fournit donc une **borne
  inférieure automatique** (99.5 %) ; l'adjudication manuelle établit la valeur réelle
  (99.92 %). La métrique ① (« valeur existe ») offre un garde‑fou robuste et automatique.
- **Frontière avec la validation d'entités.** Certaines informations (méthode NS décrite dans
  le *corps* de l'article mais absente des *tableaux*, ex. `randomcorrupt`) sont hors de portée
  d'une validation table‑only ; elles relèvent de la validation d'entités qui lit le corps.
  Les deux validations sont **complémentaires**.
- **Rappel non mesuré**, par conception.

---

## 8. Conclusion

La validation croisée par LLM‑juge indépendant établit, **de façon entièrement automatique**,
que les 6 567 configurations extraites sont correctes à **99.5 %** (borne brute) sur
l'association *combinaison → valeur*, et à **99.92 %** après adjudication des écarts. Les
valeurs numériques sont réelles à **99.9 %**. Le mécanisme de canari confirme, sur 54 des 55
articles, que le juge discrimine effectivement.

Les rares écarts se répartissent en **5 vraies imprécisions d'extraction** (valeurs
manquantes/absentes) et **29 faux positifs du juge** liés à la structure de certains tableaux
(lignes labellisées par méthode, rowspan imbriqués). L'ensemble constitue une preuve de
qualité **crédible et traçable** : un résultat non parfait, obtenu par un vérificateur
indépendant, auto‑contrôlé par canari, et intégralement adjugeable.
