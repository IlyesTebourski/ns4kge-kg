#!/usr/bin/env python3
"""
Validation des NS METHODS extraites par le KG, avec DISTINCTION DE PROVENANCE
(comme KGEModel) et 4 scores : precision evalues / precision mentionnes /
recall evalues / recall mentionnes.

Sources :
- proposedNSMethod + mentionedNSMethods -> prompt1 -> prose (no_tables)
- Configurations[].NSMethod             -> prompt2 -> tables (tables_only)

Difficultes specifiques NS methods (matching iteratif) :
- "Unknown" (placeholder du prompt pour baseline non identifiee) -> EXCLU.
- "Negative Sampling" souvent omis/abrege -> mots de liaison optionnels.
- Fortes ABREVIATIONS : le KG garde le nom complet, le texte utilise l'acronyme
  (Random Negative Sampling -> RNS, Self-Adversarial NS -> SANS) -> on derive et
  matche l'acronyme (sensible a la casse).

Matching hybride : precision insensible casse ; recall sensible casse (bruit).
Sorties : validation/reports_nsmethods/<slug>.md + _SUMMARY.md
"""
import json
import glob
import os
import re

import validate_datasets as VD

MD_DIR = VD.MD_DIR
KG_DIR = VD.KG_DIR
OUT_DIR = os.path.join(VD.HERE, "reports_nsmethods")

SEP = r"[\s\-_/.@()\[\]]*"
# mots de liaison optionnels (souvent omis dans le texte)
# Vrais mots de liaison OPTIONNELS (connecteurs) dans les deux modes.
CONNECTORS = {"based", "method", "approach", "technique", "strategy", "with", "w"}
# Mots-CATEGORIE qui nomment la methode NS. Meme regle que lossfunction :
# optionnels en PRECISION (leniente), REQUIS en RECALL — sinon "Simple Negative
# Sampling" se reduit a chercher "simple" tout seul (39 faux candidats mesures),
# "Good..."->"good" (31), etc. Regle linguistique de principe, PAS une stoplist.
CATEGORY = {"negative", "neg", "sampling", "sample"}
FILLER = CONNECTORS | CATEGORY       # gap optionnel ENTRE tokens (les deux modes)
GENERIC = {"sampling", "sample", "ns", "method", "negative"}


def normalize_label(label):
    """Retire les qualificatifs experimentaux pour matcher la methode de BASE :
    (...) [...] %, ratios, regimes d'entrainement (scratch/pretrain), et coupe
    sur les separateurs de compound (+, virgule, 'w/', 'with').
    Ex. 'NoiGAN (hard) (40%)' -> 'NoiGAN' ; 'NSCaching + scratch' -> 'NSCaching' ;
        'closed world constraints, neg_ratio=1' -> 'closed world constraints'."""
    s = re.sub(r"\([^)]*\)", " ", label)
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.split(r"\s*(?:\+|,|\bw/\b|\bwith\b)\s*", s)[0]
    s = re.sub(r"(?i)\b(?:scratch|pretrain)\b", " ", s)
    s = re.sub(r"\d+\s*%?", " ", s)
    s = " ".join(s.split()).strip()
    return s or label.strip()


def tokens_cs(label):
    return re.findall(r"[A-Za-z0-9]+", normalize_label(label))


def content_tokens(label):
    return [t for t in tokens_cs(label) if t.lower() not in FILLER]


def method_key(label):
    """Cle canonique = mots de contenu (sans negative/sampling...). Dedup les
    quasi-doublons : 'Bernoulli Sampling' == 'Bernoulli Negative Sampling'."""
    return "".join(t.lower() for t in content_tokens(label))


# acronymes trop generiques -> ne pas DERIVER de pattern de matching dessus
# (robustesse du matcher : "GAN"/"KG" matcheraient partout ; ce n'est PAS une
# stoplist d'entites qui etouffe le recall, c'est le meme principe que "loss"
# exige pour lossfunction — on ne matche pas sur un acronyme non distinctif).
GENERIC_ACR = {"GAN", "NS", "KG", "LP", "KGE"}

# Verdicts de verification MANUELLE.
PREC_VERDICTS = {}
# Adjudication manuelle recall (2026-07-22) : justifications completes dans
# recall_checks/nsmethods_recall_check.csv (genere avec couverture verifiee).
RECALL_VERDICTS = {
    ('adaptativens', 'Subsampling'): ('fp', "Titre 'Adaptive Negative Subsampling' = methode propre extraite ('Adaptive NS'), granularite."),
    ('asa', 'Adversarial Negative Sampling'): ('fp', "Partiel de 'adaptive self-adversarial negative sampling' (methode propre extraite)."),
    ('asa', 'Noise contrastive estimation'): ('miss', "'unified within a sampled noise contrastive estimation framework (Yang et al.)' : approche NS citee, non extraite."),
    ('cake', 'CANS'): ('fp', "Ligne 'TransE+CANS' = 'Commonsense-Aware Negative Sampling' extraite (acronyme vs nom complet)."),
    ('cake', 'NS-KGE'): ('fp', "'None-sampling: NS-KGE (Li et al., 2021)' : concept capture par 'None Sampling' extrait du meme passage."),
    ('cans', 'CKRL (40%)'): ('miss', "Lignes de resultats 'CKRL(LT)'/'CKRL' avec scores : baseline evaluee non extraite (extraits: Bernoulli/Confidence-Aware/Uniform)."),
    ('ccs', 'Dynamic Distribution Sampling'): ('fp', "'divided into... fixed distribution sampling and dynamic distribution sampling' = categorie."),
    ('ccs', 'IGAN'): ('miss', "'IGAN [40] and Kbgan [41] both introduce GAN for negative sampling' : Kbgan extrait mais PAS IGAN."),
    ('conceptdriven', 'CAKE'): ('miss', "'[2] proposes a detachable Commonsense-Aware Knowledge Embedding (CAKE) framework' : framework cite ; CANS extraite mais pas CAKE."),
    ('conceptdriven', 'CANS'): ('fp', "Ligne '+CANS' = 'Commonsense-Aware Negative Sampling' extraite."),
    ('conceptdriven', 'Domain-based Negative Sampling'): ('fp', "'concept domain negative sampling (CDNS)' : 'Concept Domain NS' extraite."),
    ('conceptdriven', 'MVLP'): ('fp', "'multi-view link prediction (MVLP) module' = module de LINK PREDICTION, pas une methode NS."),
    ('dans', 'Adaptive Negative Sampling'): ('fp', "Titre/methode propre 'Diversified and Adaptive NS' extraite (partiel)."),
    ('dans', 'Adversarial Negative Sampling'): ('fp', "Partiel de 'self-adversarial negative sampling' ('Self-adversarial NS' extraite)."),
    ('dans', 'GAN-based Negative Sampling'): ('fp', "'previous GAN-based negative sampling' = categorie (KBGAN/IGAN/HeGAN extraits)."),
    ('dans', 'Importance Sampling'): ('fp', "'learning strategies including GANs, RL, and importance sampling [39]' = categorie de techniques."),
    ('dans', 'SANS'): ('fp', "Ligne 'SANS-RW' : SANS extraite sous 'Structure-Aware Negative Sampling' (variante RW = granularite)."),
    ('dans', 'Self-Adv'): ('fp', "Ligne 'Self-adv' = 'Self-adversarial Negative Sampling' extraite."),
    ('dans', 'Uniform Random Sampling'): ('fp', "'via uniform random sampling' : 'Random Negative Sampling' extraite."),
    ('demix', 'Adversarial Negative Sampling'): ('fp', "Partiel de 'self-adversarial negative sampling' ('Self-adversarial Sampling' extraite)."),
    ('demix', 'CAKE'): ('miss', "'The CANS is a component of CAKE [16]' : CANS extraite mais pas CAKE."),
    ('demix', 'MixGCF'): ('miss', "'MixGCF [13] integrates multiple negative samples...' : mention reelle (MixKG extrait, PAS MixGCF)."),
    ('demix', 'SANS'): ('fp', "Ligne 'TransE+RW-SANS' : 'RW-SANS' extraite."),
    ('demix', 'Self-Adv'): ('fp', "Ligne 'TransE+Self-Adv' = 'Self-adversarial Sampling' extraite."),
    ('demix', 'Commonsense-Aware Negative Sampling'): ('fp', "Ligne 'TransE+CANS' : 'CANS' extraite (nom complet vs acronyme)."),
    ('dhns', 'Self-adversarial Negative Sampling'): ('fp', "Ligne 'SANS' du tableau = la methode SANS extraite ; collision d'acronyme avec Self-adversarial."),
    ('dmns', 'DMNS'): ('fp', "Ligne 'DMNS' = methode propre extraite sous 'Conditional Diffusion-based Multi-level Negative Sampling'."),
    ('dmns', 'Noise contrastive estimation'): ('miss', "'many methods follow the noise contrastive estimation approach [13]' : approche citee, non extraite."),
    ('dmns', 'SANS'): ('miss', "'On graphs, SANS [2] select negative examples from k-hop neighborhoods' : mention reelle, non extraite."),
    ('dns', 'Local-Closed World Assumption Negative Sampling'): ('fp', "Assomption LCWA fondant la corruption aleatoire ; methode operationnelle ('Random NS') extraite."),
    ('eans', 'Adversarial Negative Sampling'): ('fp', "Partiel ('Self-Adversarial NS' extraite)."),
    ('eans', 'EANS'): ('fp', "Ligne 'EANS (ours)' = 'Entity Aware Negative Sampling' extraite."),
    ('eans', 'Random Negative Sampling'): ('fp', "'uniform random negative sampling method' : 'Uniform NS' extraite."),
    ('eans', 'Self-Adv'): ('fp', "Ligne 'Self-adv.(Sun et al.)' = 'Self-Adversarial Negative Sampling' extraite."),
    ('eans', 'Uniform Random Sampling'): ('fp', "'a uniform random sampling method' : 'Uniform NS' extraite."),
    ('eans', 'Structure-Aware Negative Sampling'): ('fp', "Ligne 'SANS + Self-adv.' : 'SANS' extraite (acronyme)."),
    ('erdns', 'Simple Negative Sampling'): ('fp', "'Simple negative sampling methods like uniform sampling' = adjectif."),
    ('erdns', 'Self-adversarial Negative Sampling'): ('fp', "Extraite sous 'Self-Adv' (acronymes [21],[1] du texte)."),
    ('ghn', 'Nearest Neighbor Sampling'): ('fp', "Ablation 'NN' = 'Approximate Nearest Neighbor Negative Sampling' extraite."),
    ('gibbsns', 'Entity Similarity-based Negative Sampling'): ('miss', "'semantic related NS models, such as..., entity similarity-based negative sampling' : methode citee (ESNS, Yao et al.), non extraite."),
    ('gibbsns', 'IGAN'): ('miss', "'IGAN [19] designed a generator and performed advanced negative sampling' : mention reelle, non extraite."),
    ('gibbsns', 'Random Negative Sampling'): ('fp', "'uniform random negative sampling' : 'Uniform Random NS' extraite."),
    ('gibbsns', 'Static Sampling'): ('fp', "'static negative sampling methods' = categorie."),
    ('gibbsns', 'Entity-Aware Negative Sampling'): ('fp', "Ligne 'EANS' : 'EANS' extraite (acronyme) ; le vocab nom-complet collisionne."),
    ('gns', 'Corrupting Positive Instances'): ('fp', 'Description de la meme approche [10] deja comptee via le FN LCWA (pas de double compte).'),
    ('gns', 'Local-Closed World Assumption Negative Sampling'): ('miss', "'a Local-Closed World Assumption (LCWA) approach [10] assumes...' : approche NS citee et discutee, non extraite."),
    ('graphgan', 'IRGAN'): ('miss', "'different with IRGAN (Wang et al. 2017a), the design of graph softmax...' : comparaison reelle, extraits vides."),
    ('hasa', 'Importance Sampling'): ('fp', "'approximated via importance sampling' = technique mathematique de leur derivation."),
    ('htens', 'Dynamic Distribution Sampling'): ('fp', "'dynamic distribution based sampling methods' = categorie."),
    ('kbgan', 'IRGAN'): ('miss', "'IRGAN (Wang et al., 2017) is a recent work which combines...' : related work reel, non extrait."),
    ('las', 'Adaptive Negative Sampling'): ('fp', "'the loss adaptive negative sampling approach' = LAS extraite ('Loss Adaptive Sampling')."),
    ('las', 'Adversarial Negative Sampling'): ('fp', "'LAS is a... adversarial negative sampling approach' = descripteur de LAS extraite ('Loss Adaptive Sampling')."),
    ('las', 'Random Negative Sampling'): ('fp', "'random negative sampling would cause...' : 'Uniform Random NS' extraite."),
    ('las', 'Static Sampling'): ('fp', "'the static negative sampling models, nearest-neighbour and near-miss' = categorie ; les methodes citees sont extraites."),
    ('lemon', 'RW-SANS'): ('fp', "'Uniform RW-SANS [2]' en table de COMPLEXITE ; 'Uniform RW-SANS' extraite."),
    ('lemon', 'SANS'): ('fp', "Table de complexite ; SANS extraite sous 'Structure-aware Negative Sampling'."),
    ('lemon', 'Self-Adv'): ('fp', "'Self-Adv. [15]' en table de complexite (ni resultats ni prose) ; variantes Self-Adv. SANS extraites."),
    ('localcognitive', 'Adversarial Negative Sampling'): ('fp', "Partiel ('Self-adversarial negative sampling' extraite)."),
    ('localcognitive', 'Self-Adv'): ('fp', "Ablation 'w/o self-adv' : 'Self-adversarial negative sampling' extraite."),
    ('m2ixkg', 'Dynamic Negative Sampling'): ('fp', "'fixed negative sampling and dynamic negative sampling' = categorie."),
    ('m2ixkg', 'MixGCF'): ('miss', "'MixGCF [Huang et al., 2021] uses positive mixing and hop mixing' : mention reelle, non extraite."),
    ('m2ixkg', 'Simple Negative Sampling'): ('fp', "'rely on simple negative sampling methods' = adjectif."),
    ('m2ixkg', 'Uniform RW-SANS'): ('fp', "Ligne couverte par 'RW-SANS' extraite (prefixe Uniform = base NS, granularite)."),
    ('m2ixkg', 'Uniform SANS'): ('fp', "Ligne couverte par 'SANS' extraite (granularite)."),
    ('m2ixkg', 'Self-adversarial Negative Sampling'): ('fp', "Collision d'acronyme : 'SANS [Ahrabian]' = Structure-Aware, extraite sous 'SANS'."),
    ('mcns', 'GAN-based Negative Sampling'): ('fp', 'En-tete de categorie ; IRGAN/KBGAN extraits.'),
    ('mcns', 'Importance Sampling'): ('fp', "'FastGCN adopts importance sampling in each layer' = technique GNN, pas une NS de KGE."),
    ('mcns', 'Noise contrastive estimation'): ('miss', "'unified within a Sampled Noise Contrastive Estimation (SampledNCE) framework' : cadre CENTRAL du papier, non extrait."),
    ('mdncaching', 'Dynamic Distribution Sampling'): ('fp', "'MDNCaching is a dynamic distribution-based NS strategy' = descripteur de la methode propre extraite."),
    ('mdncaching', 'Dynamic Negative Sampling'): ('fp', "'the dynamic negative sampling techniques were introduced' = categorie."),
    ('mdncaching', 'GAN-based Negative Sampling'): ('fp', "'GAN based NS strategies IGAN and KBGAN' = categorie ; methodes extraites."),
    ('mdncaching', 'Importance Sampling'): ('fp', "'updating the cache using importance sampling' = composant de NSCaching (extraite)."),
    ('mdncaching', 'MDNCaching'): ('fp', "Ligne 'MDNCaching' = methode propre extraite sous 'Matrix Decomposed Negative Caching'."),
    ('mdncaching', 'SANS'): ('fp', "'SANS [1]' : extraite sous 'Structure Aware Negative Sampling'."),
    ('nmiss', 'Nearest-neighbour Sampling'): ('fp', "'nearest neighbour sampling' : extraite sous 'Nearest Neighbor Sampling' (orthographe)."),
    ('nscaching', 'Cache-based Negative Sampling'): ('fp', "'our cache-based negative sampling scheme' = descripteur de NSCaching (extraite)."),
    ('nscaching', 'Importance Sampling'): ('fp', "'we design importance sampling (IS) strategy to update the cache' = composant de NSCaching (extraite)."),
    ('rcwc', 'Adversarial Negative Sampling'): ('fp', "Partiel ('Self-Adversarial NS' extraite)."),
    ('reasonkge', 'Iterative Negative Sampling'): ('fp', 'Titre de section de LEUR methode (ReasonKGE extraite).'),
    ('reasonkge', 'SANS'): ('fp', "'structure-aware negative sampling (SANS)' : extraite sous le nom complet."),
    ('reasonkge', 'Local-Closed World Assumption Negative Sampling'): ('fp', 'Discussion definitionnelle CWA/LCWA (assomption).'),
    ('sans', 'Adversarial Negative Sampling'): ('fp', "Match partiel dans 'Self-Adversarial negative sampling' ('Self-Adversarial NS' extraite)."),
    ('sans', 'Importance Sampling'): ('fp', "'partition function used in Importance Sampling (Bengio et al. 2003)' = historique NCE en LM."),
    ('sans', 'RW-SANS'): ('fp', "'Uniform RW-SANS (ours)' : extraite sous 'Uniform Random Walk Structure Aware NS'."),
    ('sans', 'SANS'): ('fp', "Extraite sous 'Structure Aware Negative Sampling' (acronyme du tableau)."),
    ('sans', 'Self-Adv'): ('fp', "'Self-Adv. (Sun et al.)' : 'Self-Adversarial Negative Sampling' extraite."),
    ('sans', 'Self-Adv. RW-SANS'): ('fp', "Extraite sous 'Self-Adversarial Random Walk Structure Aware NS'."),
    ('sans', 'Self-Adv. SANS'): ('fp', "Extraite sous 'Self-Adversarial Structure Aware NS'."),
    ('sans', 'Uniform SANS'): ('fp', "Extraite sous 'Uniform Structure Aware NS'."),
    ('selfadv', 'Adversarial Negative Sampling'): ('fp', "Match partiel dans 'self-adversarial negative sampling technique' (extraite)."),
    ('sns', 'Good Negative Sampling'): ('fp', "'still lacks a good negative sampling method' = adjectif anglais."),
    ('sns', 'SANS'): ('fp', "'structure aware negative sampling(SANS)' : extraite sous le nom complet."),
    ('stc', 'Local-Closed World Assumption Negative Sampling'): ('miss', "'we also FOLLOW the LCWA proposed in [Krompass] as a supplementary method' : methode UTILISEE par le papier, non extraite."),
    ('tans', 'Adaptive Negative Sampling'): ('fp', "Partiel de 'Triplet Adaptive Negative Sampling' extraite."),
    ('tans', 'Adversarial Negative Sampling'): ('fp', "Partiel de 'Self-Adversarial Negative Sampling (SANS)' extraite."),
    ('tans', 'SANS'): ('fp', "Colonne 'SANS' = abreviation du papier pour 'Self-Adversarial Negative Sampling' extraite."),
    ('tans', 'Subsampling'): ('fp', "Table analytique ; variantes 'Base/Frequency/Unique-based subsampling' extraites."),
    ('tuckerdncaching', 'Dynamic Distribution Sampling'): ('fp', "'previous dynamic distribution-based NS methods' = categorie."),
    ('tuckerdncaching', 'Dynamic Negative Sampling'): ('fp', "'previous dynamic NS methods IGAN, KBGAN, KSGAN' = categorie (methodes extraites)."),
    ('tuckerdncaching', 'ESNS'): ('fp', "'Entity Similarity-based NS (ESNS)' : extraite sous le nom complet."),
    ('tuckerdncaching', 'SANS'): ('fp', "'Structure Aware Negative Sampling (SANS)' : extraite sous le nom complet."),
    ('tuckerdncaching', 'Self-Adv'): ('fp', "'self-adversarial Self-Adv sampling (RotatE)' : 'Self-Adversarial NS' extraite."),
    ('typeaugmented', 'Adversarial Negative Sampling'): ('fp', "Partiel ('Self-adversarial negative sampling' extraite)."),
    ('sans', 'Uniform RW-SANS'): ('fp', "Figure 2 : extraite sous 'Uniform Random Walk Structure Aware NS'."),
}



def is_unknown(label):
    return VD.norm_key(label).startswith("unknown")


def is_excluded(label):
    # Seuls "Unknown" (placeholder du prompt pour baseline non identifiee) et une
    # cle vide sont exclus. Plus de GENERIC_METHODS (gan/ns...) : un terme trop
    # generique extrait comme NS method est une question de PRECISION (a condamner
    # en verif manuelle), pas a masquer d'office.
    k = method_key(label)
    return is_unknown(label) or k == ""


# Abreviations canoniques de la litterature (Wang et al., TransH) : le texte ecrit
# souvent la forme abregee entre guillemets ("bern"/"unif") plutot que le nom
# complet. On les reconnait comme alias pour ne pas rater la mention/evaluation.
ALIASES = {
    "bernoulli": ["Bernoulli", "bern"],
    "uniform":   ["Uniform", "unif"],
}


def _tok_re(t, strict=False):
    """Regex d'un token : alias canoniques si connus, + pluriel optionnel ('s?').
    strict=True (recall) : regle de casse homogene VD.tok_regex (stylise = exact)."""
    alts = ALIASES.get(t.lower(), [t])
    return r"(?:" + "|".join(VD.tok_regex(a, strict) for a in alts) + r")s?"


def name_pattern(label, ci):
    """Regex du nom complet, avec mots de liaison optionnels entre tokens.
    ci=True (precision) : tout insensible a la casse (inchange). ci=False (recall) :
    regle de casse homogene — token stylise = casse exacte, banal = insensible."""
    toks = tokens_cs(label)
    if not toks:
        return None
    # precision : categorie optionnelle (FILLER complet) ; recall : REQUISE.
    skip = FILLER if ci else CONNECTORS
    required = [t for t in toks if t.lower() not in skip]
    if not required or (len(required) == 1 and required[0].lower() in GENERIC):
        required = toks[:]
    filler_alt = "|".join(sorted(FILLER, key=len, reverse=True))
    gap = SEP + r"(?:(?i:" + filler_alt + r")" + SEP + r")*"
    core = gap.join(_tok_re(t, strict=not ci) for t in required)
    return re.compile(r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])")


# NB : plus de stoplists WEAK_BOTH / WEAK_PROSE. C'etait l'overfit principal —
# on retirait a la main "random"/"uniform"/"bernoulli"/... du recall pour tuer le
# bruit. Desormais, honnete : le recall sur-genere ces candidats, et on les tranche
# a la main (RECALL_VERDICTS : "fp" si la chaine matche un usage non-NS). Le vocab
# n'etant bati que sur les items VERIFIES CORRECTS, un faux item ne contamine rien.


def acronyms_of(label, min_len=3):
    """Acronymes candidats : initiales de TOUS les mots ET des seuls mots de
    contenu. Ex. 'Adaptive Self-Adversarial NS' -> {'ASANS','ASA'} ;
    'Confidence-Aware NS' -> {'CANS'}."""
    toks = tokens_cs(label)
    if len(toks) < 2:
        return set()
    cands = set()
    for seq in (toks, content_tokens(label)):
        acr = "".join(t[0] for t in seq if t and t[0].isalpha()).upper()
        if len(acr) >= min_len and acr not in GENERIC_ACR:
            cands.add(acr)
    return cands


def acr_pattern(label, min_len=3):
    cands = acronyms_of(label, min_len)
    if not cands:
        return None
    alt = "|".join(re.escape(a) for a in sorted(cands, key=len, reverse=True))
    # acronyme = mot entier, SENSIBLE A LA CASSE (evite les faux matchs)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + alt + r")(?![A-Za-z0-9])")


def variant_find(label, text):
    """Match d'une variante '<base> w/ <suffixe>' via l'ACRONYME de la base +
    le suffixe, tel que les tableaux l'ecrivent reellement :
    'Self-Adversarial Negative Sampling w/ Base' -> entete 'SANS w/ Base'.
    Sans ca, le nom complet extrait par le KG ne matche jamais l'acronyme du
    tableau (faux negatif de precision). Acronyme sensible a la casse (bruit)."""
    parts = re.split(r"\s*\bw/\s*|\s+with\s+", label, maxsplit=1)
    if len(parts) != 2:
        return None, None
    base, suffix = parts
    acrs = acronyms_of(base)
    suf_toks = re.findall(r"[A-Za-z0-9]+", suffix)
    if not acrs or not suf_toks:
        return None, None
    alt = "|".join(re.escape(a) for a in sorted(acrs, key=len, reverse=True))
    suf = SEP.join(re.escape(t) for t in suf_toks)
    pat = re.compile(r"(?<![A-Za-z0-9])(?:" + alt + r")" + SEP + r"w/?" + SEP
                     + suf + r"(?![A-Za-z0-9])")
    m = pat.search(text)
    return (m, "variant") if m else (None, None)


def find(label, text, ci, min_acr=3):
    """Retourne (match, via) ou (None, None). via in {name, acro, variant}."""
    p = name_pattern(label, ci)
    if p:
        m = p.search(text)
        if m:
            return m, "name"
    pa = acr_pattern(label, min_acr)
    if pa:
        m = pa.search(text)
        if m:
            return m, "acro"
    return variant_find(label, text)


# --------------------------------------------------------------------------
def load_articles():
    from no_facts_pipeline.core import load_md_tables_only, load_md_no_tables
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            continue
        data = json.load(open(p, encoding="utf-8"))
        methods = {}

        def add(val, src):
            if not val or not str(val).strip() or is_excluded(val):
                return
            val = str(val).strip()
            k = method_key(val)   # cle canonique (dedup quasi-doublons)
            if k:
                methods.setdefault(k, {"label": val, "src": set()})["src"].add(src)

        add(data.get("proposedNSMethod"), "prose")
        for m in data.get("mentionedNSMethods", []) or []:
            add(m, "prose")
        for c in data.get("Experimentation", {}).get("Configurations", []) or []:
            if isinstance(c, dict):
                add(c.get("NSMethod"), "table")

        arts.append({
            "slug": slug, "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "prose": VD.strip_references(load_md_no_tables(md)), "tables": load_md_tables_only(md),
            "methods": methods,
        })
    return arts


def build_global_vocab(arts):
    vocab = {}
    for a in arts:
        for k, e in a["methods"].items():
            vocab.setdefault(k, e["label"])
    return vocab


def precision_pass(article):
    """Precision (insensible casse) + collecte des items VERIFIES CORRECTS (vocab)."""
    slug, prose, tables = article["slug"], article["prose"], article["tables"]
    evaluated, mentioned = [], []
    verified = {}          # method_key -> label
    te = fe = tm = fm = 0
    for k, e in sorted(article["methods"].items(), key=lambda kv: kv[1]["label"].lower()):
        label, src = e["label"], e["src"]
        # espace de recherche = union des entrees vues par le(s) prompt(s) source(s)
        text = "\n".join(([prose] if "prose" in src else []) +
                         ([tables] if "table" in src else []))
        m, via = find(label, text, ci=True)
        v = PREC_VERDICTS.get((slug, label))
        ok = bool(m) if not v else (v[0] == "valid" or (bool(m) and v[0] != "error"))
        row = (label, bool(m), (via or ""), VD.snippet_around(text, m) if m else "")
        if "table" in src:
            evaluated.append(row); te += bool(m); fe += (not m)
        else:
            mentioned.append(row); tm += bool(m); fm += (not m)
        if ok:
            verified[k] = label
    return evaluated, mentioned, verified, (te, fe, tm, fm)


def recall_pass(article, vocab):
    """RECALL (sensible casse) : methode du vocab VERIFIE presente dans l'article mais
    non extraite. Plus de stoplists WEAK_* : on sur-genere honnetement, dedup par
    position (une occurrence = un seul candidat), puis on tranche a la main."""
    prose, tables = article["prose"], article["tables"]
    raw = []   # (label, src, via, start, end, snippet)
    for k, label in sorted(vocab.items(), key=lambda kv: kv[1].lower()):
        if k in article["methods"]:
            continue
        for src, txt in (("prose", prose), ("table", tables)):
            m, via = find(label, txt, ci=False, min_acr=4)
            if m:
                raw.append((label, src, via, m.start(), m.end(), VD.snippet_around(txt, m)))
    raw.sort(key=lambda x: 0 if x[2] == "name" else 1)   # noms d'abord
    claimed = {"prose": [], "table": []}
    survivors = {}
    for label, src, via, s, e, snip in raw:
        if any(not (e <= cs or s >= ce) for cs, ce in claimed[src]):
            continue   # span deja pris par un autre candidat -> collision, on saute
        claimed[src].append((s, e))
        d = survivors.setdefault(label, {"where": set(), "via": via, "snip": snip})
        d["where"].add(src)
    return [(label, "+".join(sorted(d["where"])), d["via"], d["snip"])
            for label, d in survivors.items()]


def split_suspects(suspects):
    me = [s for s in suspects if "table" in s[1]]
    mm = [s for s in suspects if "table" not in s[1]]
    return me, mm


# --------------------------------------------------------------------------
def esc(s):
    return s.replace("|", "\\|")


def render_article(a, evaluated, mentioned, suspects, counts):
    te, fe, tm, fm = counts
    tp, fp = te + tm, fe + fm
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    pe = te / (te + fe) if (te + fe) else 1.0
    pm = tm / (tm + fm) if (tm + fm) else 1.0
    miss_e, miss_m = split_suspects(suspects)
    # ADJUGE : candidats juges "fp" ecartes ; non adjuge = oubli (convention plancher).
    slug = a["slug"]
    adj_e = [x for x in miss_e if RECALL_VERDICTS.get((slug, x[0]), ("", ""))[0] != "fp"]
    adj_m = [x for x in miss_m if RECALL_VERDICTS.get((slug, x[0]), ("", ""))[0] != "fp"]
    re_e = te / (te + len(adj_e)) if (te + len(adj_e)) else 1.0
    re_m = tm / (tm + len(adj_m)) if (tm + len(adj_m)) else 1.0

    L = [f"# NS Methods — {a['md_name']}", "", f"**Titre :** {a['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Methodes EVALUEES (tableaux) | {te + fe} |",
         f"| Methodes MENTIONNEES seulement (prose) | {tm + fm} |",
         f"| Precision evalues | {pe:.0%} | ",
         f"| Precision mentionnes | {pm:.0%} |",
         f"| Recall evalues | {re_e:.0%} |",
         f"| Recall mentionnes | {re_m:.0%} |", "",
         "## A. Methodes EVALUEES (valides vs `tables_only`)", "",
         "| Methode | Trouvee ? | Via | Extrait |", "|---|:---:|:---:|---|"]
    for label, ok, via, snip in evaluated:
        L.append(f"| {esc(label)} | {'✅' if ok else '❌'} | {via} | {esc(snip) if ok else '_(absent)_'} |")
    L += ["", "## B. Methodes MENTIONNEES seulement (valides vs prose)", ""]
    if mentioned:
        L += ["| Methode | Trouvee ? | Via | Extrait |", "|---|:---:|:---:|---|"]
        for label, ok, via, snip in mentioned:
            L.append(f"| {esc(label)} | {'✅' if ok else '❌'} | {via} | {esc(snip) if ok else '_(absent)_'} |")
    else:
        L.append("_Aucune._")
    L += ["", "## C1. Recall EVALUES — dans un tableau mais non extrait", ""]
    if miss_e:
        L += ["| Methode | Ou | Via | Extrait |", "|---|---|:---:|---|"]
        L += [f"| {esc(l)} | {w} | {v} | {esc(s)} |" for l, w, v, s in miss_e]
    else:
        L.append("_Aucun._")
    L += ["", "## C2. Recall MENTIONNES — en prose seulement mais non extrait", ""]
    if miss_m:
        L += ["| Methode | Ou | Via | Extrait |", "|---|---|:---:|---|"]
        L += [f"| {esc(l)} | {w} | {v} | {esc(s)} |" for l, w, v, s in miss_m]
    else:
        L.append("_Aucun._")
    return "\n".join(L), (te, fe, tm, fm, len(miss_e), len(miss_m), len(adj_e), len(adj_m))


def render_summary(rows, TE, FE, TM, FM, SE, SM):
    TP, FP = TE + TM, FE + FM
    mp = TP / (TP + FP) if (TP + FP) else 1.0
    pe = TE / (TE + FE) if (TE + FE) else 1.0
    pm = TM / (TM + FM) if (TM + FM) else 1.0
    re_e = TE / (TE + SE) if (TE + SE) else 1.0
    re_m = TM / (TM + SM) if (TM + SM) else 1.0
    L = ["# Recap validation NS METHODS (provenance explicite)", "",
         f"Articles : **{len(rows)}**", "",
         "| Article | Eval | Ment | Prec.eval | Prec.ment | Manq.eval | Manq.ment |",
         "|---|---:|---:|:---:|:---:|---:|---:|"]
    for name, te, fe, tm, fm, se, sm in rows:
        pe_ = te / (te + fe) if (te + fe) else 1.0
        pm_ = tm / (tm + fm) if (tm + fm) else 1.0
        L.append(f"| {name} | {te+fe} | {tm+fm} | {pe_:.0%} | {pm_:.0%} | {se} | {sm} |")
    L += ["", "## Totaux (4 scores)", "", "| Metrique | Valeur |", "|---|---|",
          f"| Methodes EVALUEES | {TE + FE} |",
          f"| Methodes MENTIONNEES seulement | {TM + FM} |",
          f"| **Precision evalues** | **{pe:.1%}** |",
          f"| **Precision mentionnes** | **{pm:.1%}** |",
          f"| **Recall evalues (indicatif)** | **{re_e:.1%}** |",
          f"| **Recall mentionnes (indicatif)** | **{re_m:.1%}** |",
          f"| Precision globale (micro) | {mp:.1%} |",
          f"| Candidats manques (eval / ment) | {SE} / {SM} |"]
    return "\n".join(L)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    arts = load_articles()

    # Phase 1 : precision -> vocab bati UNIQUEMENT sur les items verifies corrects
    prec = {}
    vocab = {}
    for a in arts:
        ev, me, verified, counts = precision_pass(a)
        prec[a["slug"]] = (ev, me, counts)
        for k, lab in verified.items():
            vocab.setdefault(k, lab)
    print(f"Vocab global NS methods (items verifies corrects) = {len(vocab)}")

    # Phase 2 : recall contre le vocab verifie
    rows = []
    TE = FE = TM = FM = SE = SM = AE = AM = 0
    for a in arts:
        ev, me, counts = prec[a["slug"]]
        sus = recall_pass(a, vocab)
        report, (te, fe, tm, fm, se, sm, ae, am) = render_article(a, ev, me, sus, counts)
        open(os.path.join(OUT_DIR, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        rows.append((a["md_name"], te, fe, tm, fm, se, sm))
        TE += te; FE += fe; TM += tm; FM += fm; SE += se; SM += sm; AE += ae; AM += am
    open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(rows, TE, FE, TM, FM, SE, SM))
    TP, FP = TE + TM, FE + FM
    print(f"{len(arts)} rapports -> {OUT_DIR}/")
    print(f"Evalues={TE+FE} Mentionnes={TM+FM}")
    print(f"Precision  evalues={TE/(TE+FE):.1%}  mentionnes={TM/(TM+FM):.1%}")
    print(f"Recall BRUT   evalues={TE/(TE+SE):.1%} (candidats={SE})  mentionnes={TM/(TM+SM):.1%} (candidats={SM})")
    print(f"Recall ADJUGE evalues={TE/(TE+AE):.1%} (vrais FN={AE}, FP ecartes={SE-AE})  "
          f"mentionnes={TM/(TM+AM):.1%} (vrais FN={AM}, FP ecartes={SM-AM})")


if __name__ == "__main__":
    main()
