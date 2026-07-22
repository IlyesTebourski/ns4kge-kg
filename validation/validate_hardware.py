#!/usr/bin/env python3
"""
Validation du HARDWARE extrait par le KG — meme principe que datasets/metrics,
mais valide contre la PROSE (et non les tableaux).

Provenance (une seule source) : dans le pipeline, le hardware est extrait par
prompt1 (`prompt1_no_results.txt`, section HARDWARE), dont l'unique entree est le
`load_md_no_tables()` (prose sans tableaux). Aucun tableau n'extrait de hardware.
=> On valide donc `Experimentation.Hardware[]` contre le `no_tables` de CHAQUE
   article (fidelite garantie au pipeline).

METHODOLOGIE EN DEUX COUCHES (importante) :
1. PRECISION AUTOMATIQUE — un matcher DETERMINISTE et GENERIQUE (casse, espaces,
   ponctuation, marques typographiques ®™, et mots de specs generiques GPU/RAM/...
   traites comme liaison optionnelle). Il n'est PAS taille pour un article precis :
   on ne triche pas pour gonfler le score. Il rate ce qu'il rate.
2. VERIFICATION MANUELLE (adjudication) — pour CHAQUE hardware que l'algo n'a pas
   retrouve, un humain lit la prose et tranche : soit l'ecart n'est PAS une erreur
   du KG (coquille du papier, reformulation mineure, limite du matcher) -> recompte
   VALIDE ; soit c'est une vraie erreur d'extraction -> reste FAUX. Les verdicts et
   leur justification (citation de la prose) sont CONSERVES dans le rapport
   (MANUAL_VERDICTS ci-dessous) : la reclassification est tracable et auditable.
On publie donc DEUX chiffres : precision automatique (brute) et precision verifiee.

Difficulte specifique HARDWARE : ce ne sont pas des noms canoniques (datasets) ni
des metrics normalisees, mais des descriptions LIBRES ("24 Intel Xeon cores ...
256 GB RAM", "NVIDIA GeForce GTX 1080 Ti GPU"). Les mots de specs (GPU, RAM, GB,
cores...) sont traites comme des mots de liaison OPTIONNELS ; le reste (vendeur,
serie, code modele, tailles) doit apparaitre, dans l'ordre.

RECALL : quels hardware du vocabulaire global apparaissent dans la prose d'un
         article mais n'ont PAS ete extraits ? (candidats faux negatifs), restreint
         aux entrees DISTINCTIVES (code modele lettre+chiffre ou serie connue).

Sorties : validation/reports_hardware/<slug>.md + _SUMMARY.md
"""
import json
import glob
import os
import re

import validate_datasets as VD  # norm_key, snippet_around, dirs, io

MD_DIR = VD.MD_DIR
KG_DIR = VD.KG_DIR
OUT_DIR = os.path.join(VD.HERE, "reports_hardware")

# separateurs entre tokens : espaces, tirets, /, ., @, parentheses, crochets,
# virgules (les descriptions hardware sont ponctuees : "(two sockets), 256 GB")
# et marques typographiques (Intel® Xeon®, GeForce™). Normalisation GENERIQUE.
SEP = r"[\s\-_/.@()\[\],®™©×]*"

# Token = pur nombre + unite (taille RAM, frequence) -> spec, jamais un modele.
UNIT_RE = re.compile(r"(?i)^\d+(?:gb|mb|tb|ghz|mhz)$")

# Mots de specs generiques : ni distinctifs, ni obligatoires. Traites comme des
# mots de LIAISON OPTIONNELS entre les tokens distinctifs.
GENERIC = {
    "gpu", "gpus", "cpu", "cpus", "ram", "memory", "core", "cores", "card",
    "cards", "gb", "mb", "tb", "ghz", "mhz", "processor", "processors",
    "graphics", "single", "multiple", "virtual", "socket", "sockets",
    "hyperthread", "hyperthreads", "hyperthreading", "thread", "threads",
    "with", "and", "per", "two", "using", "of", "machine", "server", "node",
    "nodes", "only", "each", "on", "a", "the", "x",
}

# Mots de SERIE / VENDEUR connus : suffisent a rendre une entree distinctive
# (meme sans code modele lettre+chiffre) pour le RECALL.
SERIES = {
    "nvidia", "intel", "amd", "tesla", "geforce", "titan", "quadro", "xeon",
    "radeon", "ryzen", "epyc", "gtx", "rtx",
}


def tokens_cs(label):
    """Tokens en conservant la casse."""
    return re.findall(r"[A-Za-z0-9]+", label)


def has_letter_and_digit(t):
    return any(c.isalpha() for c in t) and any(c.isdigit() for c in t)


def content_tokens(label):
    """Tokens qui DOIVENT figurer dans la prose = tout sauf les mots de specs
    generiques et les tokens nombre+unite (16GB, 3GHz = simple formatage). On
    GARDE tout le reste tel quel : vendeur, serie, code modele ET nombres nus
    (256, 48, 1080...). Aucune tolerance aux coquilles/reformulations ici : c'est
    le role de la verification MANUELLE, pas du matcher automatique."""
    return [t for t in tokens_cs(label)
            if t.lower() not in GENERIC and not UNIT_RE.match(t)]


def is_distinctive(label):
    """Une entree hardware est exploitable pour le RECALL si elle porte un code
    modele (token lettre+chiffre : V100, i7, 2080Ti, E3) OU un mot de serie/vendeur
    connu. Sinon ("CPU only", "single GPU") : trop generique, exclue du recall."""
    toks = tokens_cs(label)
    if any(has_letter_and_digit(t) for t in toks):
        return True
    return bool({t.lower() for t in toks} & SERIES)


def name_pattern(label, ci=True):
    """Regex : tokens de contenu dans l'ordre, separateurs souples, avec les mots
    de specs generiques (GPU/RAM/cores...) TOLERES en liaison optionnelle. Matcher
    GENERIQUE : aucune regle taillee pour un article donne.
    ci=True (precision) : tout insensible (inchange). ci=False (recall) : regle de
    casse homogene VD.tok_regex — token stylise (V100, RTX) = casse exacte."""
    required = content_tokens(label) or tokens_cs(label)
    if not required:
        return None
    filler_alt = "|".join(sorted(GENERIC, key=len, reverse=True))
    gap = SEP + r"(?:(?i:" + filler_alt + r")" + SEP + r")*"
    core = gap.join(VD.tok_regex(t, strict_case=not ci) for t in required)
    return re.compile(r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])")


def find(label, text, ci=True):
    pat = name_pattern(label, ci)
    if pat is None:
        return None
    return pat.search(text)


# --------------------------------------------------------------------------
# VERIFICATION MANUELLE (adjudication humaine des ecarts precision)
# --------------------------------------------------------------------------
# Cle = (slug, label hardware extrait exactement). Valeur = (statut, justification).
#   "valid" -> l'ecart avec la prose N'EST PAS une erreur du KG : on recompte VALIDE.
#   "error" -> vraie erreur d'extraction : reste FAUX.
# Chaque verdict cite la prose source pour etre auditable. N'ajouter une entree
# qu'APRES avoir lu le texte de l'article. Un rate SANS verdict ici reste compte
# comme faux et est signale "a verifier" dans le rapport.
MANUAL_VERDICTS = {
    ("adns", "Nvidia RTX 2060"): (
        "valid",
        "Le papier ecrit litteralement « i7 4770 processor and Nvidia RTX 260 GPU » "
        "— coquille du papier : la « RTX 260 » n'existe pas, il s'agit de la RTX 2060. "
        "Le KG a restitue le bon device. Ecart du a l'erreur du PAPIER, pas du KG."),
    ("ccs", "Tesla P100 GPU 16GB RAM"): (
        "valid",
        "Le papier ecrit « ran on a single Teals P100 GPU with 16 GB RAM » — coquille "
        "vendeur « Teals » pour « Tesla ». Le modele (P100) et la RAM (16 GB) sont "
        "corrects et presents verbatim. Ecart du a la coquille du PAPIER, pas du KG."),
    ("batchns",
     "24 Intel Xeon cores (two sockets) with two hyperthreads per core "
     "(48 virtual cores), 256 GB RAM"): (
        "error",
        "Prose : « 24 Intel Xeon cores (two sockets) and two hyperthreads per core, "
        "for a total of 48 virtual cores, and 256 GB of RAM ». Meme machine, mais ce "
        "n'est PAS une coquille du papier (contrairement a Teals/RTX 260) : c'est le KG "
        "qui a REFORMULE le libelle (« and »->« with », « for a total of 48 »->« (48 »). "
        "Choix strict : on ne credite que le verbatim et les coquilles averees du papier "
        "-> comptee comme 1 erreur de precision."),
}


# --------------------------------------------------------------------------
# Chargement / extraction
# --------------------------------------------------------------------------

def extracted_hardware(data: dict):
    """{norm_key: label} du hardware extrait (Experimentation.Hardware[])."""
    out = {}
    exp = data.get("Experimentation", {}) or {}
    for hw in exp.get("Hardware", []) or []:
        v = str(hw).strip()
        if not v:
            continue
        k = VD.norm_key(v)
        if k:
            out.setdefault(k, v)
    return out


def load_articles():
    from no_facts_pipeline.core import load_md_no_tables
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            print(f"[WARN] pas de .md pour {slug}")
            continue
        data = json.load(open(p, encoding="utf-8"))
        arts.append({
            "slug": slug,
            "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "prose": VD.strip_references(load_md_no_tables(md)),
            "hardware": extracted_hardware(data),
        })
    return arts


def build_global_vocab(arts):
    vocab = {}
    for a in arts:
        for k, lab in a["hardware"].items():
            vocab.setdefault(k, lab)
    return vocab


# --------------------------------------------------------------------------
# Validation d'un article
# --------------------------------------------------------------------------

def validate(article, vocab):
    slug, prose = article["slug"], article["prose"]
    # prec_rows : (label, found_auto, snippet, verdict) ; verdict=None si trouve auto,
    # sinon ("valid"/"error"/"unreviewed", justification).
    prec_rows = []
    tp = fp = 0                 # scores AUTOMATIQUES (bruts)
    extracted_spans = []
    for k, lab in sorted(article["hardware"].items(), key=lambda kv: kv[1].lower()):
        m = find(lab, prose, ci=True)
        if m:
            prec_rows.append((lab, True, VD.snippet_around(prose, m), None))
            extracted_spans.append((m.start(), m.end()))
            tp += 1
        else:
            verdict = MANUAL_VERDICTS.get((slug, lab))
            if verdict is None:
                verdict = ("unreviewed", "")
            prec_rows.append((lab, False, "", verdict))
            fp += 1

    # RECALL : hardware du vocab global present dans la prose mais non extrait.
    # Regle de casse homogene (stylise = exact) ; restreint aux entrees distinctives ;
    # on ignore un candidat deja couvert par un hardware extrait plus detaille (ex.
    # 'NVIDIA A100' tombant sur la prose 'NVIDIA A100-PCIE-40GB' BIEN extraite).
    suspects = []
    for k, lab in sorted(vocab.items(), key=lambda kv: kv[1].lower()):
        if k in article["hardware"] or not is_distinctive(lab):
            continue
        m = find(lab, prose, ci=False)
        if not m:
            continue
        if any(not (m.end() <= s or m.start() >= e) for s, e in extracted_spans):
            continue
        suspects.append((lab, VD.snippet_around(prose, m)))
    return prec_rows, suspects, tp, fp


# --------------------------------------------------------------------------
# Rendu
# --------------------------------------------------------------------------

def esc(s):
    return s.replace("|", "\\|")


def _adjudicated(prec_rows):
    """Renvoie (valides_manuels, erreurs_reelles, a_verifier) a partir des ratés."""
    misses = [r for r in prec_rows if not r[1]]
    valid = [r for r in misses if r[3][0] == "valid"]
    error = [r for r in misses if r[3][0] == "error"]
    todo = [r for r in misses if r[3][0] == "unreviewed"]
    return valid, error, todo


def render_article(article, prec_rows, suspects, tp, fp):
    valid, error, todo = _adjudicated(prec_rows)
    tp_v = tp + len(valid)              # verifie = auto + ratés reclasses valides
    fp_v = len(error) + len(todo)       # restent faux : vraies erreurs + non verifies
    prec_a = tp / (tp + fp) if (tp + fp) else 1.0
    prec_v = tp_v / (tp_v + fp_v) if (tp_v + fp_v) else 1.0
    rec = tp / (tp + len(suspects)) if (tp + len(suspects)) else 1.0

    L = [f"# Hardware — {article['md_name']}", "",
         f"**Titre :** {article['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Hardware extrait | {tp + fp} |",
         f"| Trouve automatiquement (TP auto) | {tp} |",
         f"| Non trouve par l'algo (a verifier) | {fp} |",
         f"| **Precision automatique** | **{prec_a:.0%}** |",
         f"| Ratés reclasses VALIDES apres verif manuelle | {len(valid)} |",
         f"| Vraies erreurs d'extraction | {len(error) + len(todo)} |",
         f"| **Precision verifiee** | **{prec_v:.0%}** |",
         f"| Candidats faux negatifs recall (dans la prose, non extraits) | {len(suspects)} |",
         f"| **Recall relatif (indicatif)** | **{rec:.0%}** |", ""]

    L += ["## Precision automatique — hardware extrait vs prose", "",
          "| Hardware extrait | Trouve (algo) ? | Extrait de la prose |", "|---|:---:|---|"]
    if prec_rows:
        for lab, found, snip, _ in prec_rows:
            mark = "✅ oui" if found else "❌ non"
            L.append(f"| {esc(lab)} | {mark} | {esc(snip) if found else '_(non trouve automatiquement)_'} |")
    else:
        L.append("| _(aucun hardware extrait)_ | — | — |")
    L.append("")

    misses = valid + error + todo
    if misses:
        L += ["## Verification manuelle des ratés (adjudication)", "",
              "Chaque hardware non retrouve par l'algo est verifie a la main contre la "
              "prose. Regle stricte : seules les **coquilles averees du papier** "
              "(ex. « Teals »->Tesla, « RTX 260 »->2060, modele inexistant) sont "
              "reclassees **valides** ; une **reformulation par le KG** ou un identifiant "
              "absent de la source compte comme **erreur**. Chaque verdict cite la source.", "",
              "| Hardware | Verdict | Justification (source citee) |", "|---|:---:|---|"]
        for lab, found, snip, verdict in misses:
            status, why = verdict
            badge = {"valid": "✅ valide (pas une erreur KG)",
                     "error": "❌ vraie erreur",
                     "unreviewed": "⚠️ A VERIFIER"}[status]
            L.append(f"| {esc(lab)} | {badge} | {esc(why) if why else '_(non encore verifie)_'} |")
        L.append("")

    L += ["## Recall — hardware dans la prose mais NON extrait", ""]
    if suspects:
        L += ["| Hardware | Extrait |", "|---|---|"]
        for lab, snip in suspects:
            L.append(f"| {esc(lab)} | {esc(snip)} |")
    else:
        L.append("_Aucun candidat._")
    return "\n".join(L), (tp, fp, len(valid), len(error) + len(todo), len(todo),
                          len(suspects), prec_a, prec_v, rec)


def render_summary(rows, TP, FP, VALID, ERR, TODO, SUS):
    tp_v = TP + VALID
    micro_pa = TP / (TP + FP) if (TP + FP) else 1.0
    micro_pv = tp_v / (tp_v + ERR) if (tp_v + ERR) else 1.0
    micro_r = TP / (TP + SUS) if (TP + SUS) else 1.0
    L = ["# Recap validation HARDWARE (prose `no_tables`, avec verif manuelle)", "",
         f"Articles : **{len(rows)}**", "",
         "| Article | Extrait | TP auto | Prec.auto | Valides(manuel) | Erreurs | Prec.verif | Cand.recall |",
         "|---|---:|---:|:---:|---:|---:|:---:|---:|"]
    for name, tp, fp, valid, err, todo, sus, pa, pv, rec in rows:
        if tp + fp == 0:
            continue   # articles sans hardware extrait : n'alourdissent pas le tableau
        L.append(f"| {name} | {tp+fp} | {tp} | {pa:.0%} | {valid} | {err} | {pv:.0%} | {sus} |")
    L += ["", "## Totaux", "", "| Metrique | Valeur |", "|---|---|",
          f"| Hardware extrait (total) | {TP + FP} |",
          f"| Trouves automatiquement (TP auto) | {TP} |",
          f"| Non trouves par l'algo | {FP} |",
          f"| **Precision automatique (micro)** | **{micro_pa:.1%}** |",
          f"| Ratés reclasses VALIDES (verif manuelle) | {VALID} |",
          f"| Vraies erreurs d'extraction | {ERR} |",
          (f"| Ratés ENCORE a verifier | {TODO} |" if TODO else
           "| Ratés encore a verifier | 0 |"),
          f"| **Precision verifiee (micro)** | **{micro_pv:.1%}** |",
          f"| Candidats faux negatifs recall | {SUS} |",
          f"| **Recall relatif (indicatif, micro)** | **{micro_r:.1%}** |", "",
          "> Methodo : la **precision automatique** vient d'un matcher deterministe non "
          "taille pour un article (aucune triche). La **precision verifiee** integre "
          "l'adjudication manuelle STRICTE : seules les coquilles averees du PAPIER "
          "(Teals->Tesla, RTX 260->2060) sont reclassees valides ; une reformulation par le "
          "KG ou un identifiant absent de la source reste comptee comme erreur. Chaque verdict "
          "cite la prose (section 'Verification manuelle' de chaque rapport d'article). "
          "Source unique : hardware = prompt1 (prose) ; aucun tableau n'en extrait."]
    return "\n".join(L)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    arts = load_articles()
    vocab = build_global_vocab(arts)
    print(f"Vocab global hardware = {len(vocab)}")

    rows = []
    TP = FP = VALID = ERR = TODO = SUS = 0
    for a in arts:
        prec_rows, suspects, tp, fp = validate(a, vocab)
        report, (tp, fp, valid, err, todo, sus, pa, pv, rec) = render_article(
            a, prec_rows, suspects, tp, fp)
        open(os.path.join(OUT_DIR, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        rows.append((a["md_name"], tp, fp, valid, err, todo, sus, pa, pv, rec))
        TP += tp; FP += fp; VALID += valid; ERR += err; TODO += todo; SUS += sus

    open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(rows, TP, FP, VALID, ERR, TODO, SUS))
    tp_v = TP + VALID
    print(f"{len(arts)} rapports -> {OUT_DIR}/")
    print(f"Hardware extrait = {TP + FP}")
    print(f"Precision AUTO    = {TP/(TP+FP) if (TP+FP) else 1.0:.1%} "
          f"(trouves {TP}, ratés {FP})")
    print(f"Precision VERIFIEE = {tp_v/(tp_v+ERR) if (tp_v+ERR) else 1.0:.1%} "
          f"(valides manuels {VALID}, vraies erreurs {ERR}, a verifier {TODO})")
    print(f"Recall relatif micro = {TP/(TP+SUS) if (TP+SUS) else 1.0:.1%} (candidats={SUS})")


if __name__ == "__main__":
    main()
