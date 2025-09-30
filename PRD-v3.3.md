# PRD v3.3 SPAN SG – MkDocs avec checklist officielle

**Version** 3.3  
**Date** 30 septembre 2025  
**Owner** Alexandra  
**Validateurs** Bertrand, Alex  
**Sponsor** Yves (validation production uniquement)

---

## 1. objectif

Créer un framework simple et modulaire pour le SPAN SG permettant  
1) édition décentralisée par service, 2) agrégation automatique SG, 3) versioning, 4) export HTML/PDF, 5) scoring automatique sur la checklist DINUM (31 points).  
Principe directeur: simple, fonctionnel, efficace.

---

## 2. architecture simplifiée

### 2.1 structure pyramidale

```
Niveau 1 : SPAN SG (Global)
  ├─ Niveau 2 : Modules Services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
  │   └─ Niveau 3 : Détails par service
  └─ (Futur) extensions autres directions
```

### 2.2 structure des fichiers

```
span-sg/
├─ mkdocs.yml
├─ mkdocs-pdf.yml
├─ mkdocs-with-pdf.yml           # fallback PDF
├─ docker-compose.yml
├─ .github/workflows/build.yml
├─ docs/
│  ├─ index.md
│  ├─ synthese.md                # généré par script
│  ├─ modules/
│  │  ├─ _template.md
│  │  ├─ snum.md
│  │  ├─ sircom.md
│  │  ├─ srh.md
│  │  ├─ siep.md
│  │  ├─ safi.md
│  │  └─ bgs.md
│  └─ assets/custom.css
├─ scripts/calculate_scores.py
├─ exports/                      # non versionné
└─ site/                         # non versionné
```

---

## 3. configuration technique minimale

### 3.1 mkdocs configuration

```yaml
# mkdocs.yml
site_name: SPAN SG
site_url: https://[a-definir].github.io/span-sg/
repo_url: https://github.com/[organisation]/span-sg
strict: true

theme:
  name: material
  language: fr
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate

plugins:
  - search:
      lang: fr
  - pdf-export:
      combined: true
      combined_output_path: exports/span-sg.pdf

nav:
  - Accueil: index.md
  - Synthèse: synthese.md
  - Modules Services:
    - SNUM: modules/snum.md
    - SIRCOM: modules/sircom.md
    - SRH: modules/srh.md
    - SIEP: modules/siep.md
    - SAFI: modules/safi.md
    - BGS: modules/bgs.md

markdown_extensions:
  - tables
  - toc:
      permalink: true
```

### 3.2 scoring des 31 points

Principe: seules les cases marquées `<!-- DINUM -->` sont comptées.  
Le script échoue si un module contient un nombre de points différent de 31 (ou 0 si non renseigné).

```python
#!/usr/bin/env python3
# scripts/calculate_scores.py
import re
from pathlib import Path
from datetime import datetime

CHECK_TAG = "DINUM"
FENCE_RE = re.compile(r"```.*?```", re.S)
BOX_RE = re.compile(r"- \[(x|X| )\].*?<!--\\s*%s\\s*-->" % CHECK_TAG)

def load_text(p: Path) -> str:
    return FENCE_RE.sub("", p.read_text(encoding="utf-8"))

def score_module(p: Path):
    boxes = BOX_RE.findall(load_text(p))
    total = len(boxes)
    checked = sum(1 for b in boxes if b.lower() == "x")
    return checked, total

def generate_summary():
    modules_dir = Path("docs/modules")
    rows = [
        "# Tableau de bord SPAN SG",
        f"*Mis à jour le {datetime.now():%d/%m/%Y}*",
        "",
        "| Service | Score | Statut |",
        "|---------|-------|--------|",
    ]
    total_checked = 0
    total_items = 0
    errors = []

    for module in sorted(modules_dir.glob("*.md")):
        if module.name.startswith("_"):
            continue
        checked, total = score_module(module)
        if total not in (0, 31):
            errors.append(f"{module.name}: {total} points tagués <!-- {CHECK_TAG} --> (attendu 31 ou 0)")
        pct = round((checked / total) * 100, 1) if total else 0.0
        status = "✓ Conforme" if pct >= 75 else "En cours" if total else "Non renseigné"
        rows.append(f"| {module.stem.upper()} | {checked}/{total} ({pct}%) | {status} |")
        total_checked += checked
        total_items += total

    global_pct = round((total_checked / total_items) * 100, 1) if total_items else 0.0
    rows.append(f"| **TOTAL** | **{total_checked}/{total_items} ({global_pct}%)** | **Global** |")

    Path("docs/synthese.md").write_text("\\n".join(rows) + "\\n", encoding="utf-8")

    if errors:
        print("Erreurs de périmètre:")
        for e in errors:
            print(" -", e)
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(generate_summary())
```

### 3.3 export PDF avec fallback robuste

Objectif  
Garantir un PDF d’archive à chaque build, sans bloquer la release.

Choix tranché  
1) Plugin principal: `mkdocs-pdf-export-plugin`  
2) Fallback automatique: `mkdocs-with-pdf`  
3) Filet ultime: impression navigateur sur « Synthèse »

Fichier fallback

```yaml
# mkdocs-with-pdf.yml
site_name: SPAN SG
theme:
  name: material
plugins:
  - with-pdf:
      output_path: exports/span-sg.pdf
      cover_title: "SPAN SG"
      toc_level: 2
```

---

## 4. workflow git simplifié

Branches  
main production  
draft preview privée  
feature/ modifications par service

Process  
1) service crée `feature/update-[service]`  
2) modifie son module  
3) PR vers `draft`  
4) revue Bertrand/Alex  
5) preview privée (voir 5.1)  
6) PR `draft` vers `main`  
7) validation Yves  
8) tag version

Gestion d’urgence  
`hotfix/` vers `main` pour corrections critiques, revue rapide.

Checklist de revue PR  
31 points DINUM présents, pas de cases orphelines, front-matter, dates cohérentes, liens valides, pas d’identifiants en clair, synthèse CI OK, intitulés propres.

---

## 5. authentification et accès

### 5.1 accès preview privé (option A figée)

Principe  
GitHub Pages sert la prévisualisation de `draft`; l’accès est limité aux membres de l’organisation GitHub.

Quand l’utiliser  
Lorsque toute l’équipe dispose d’un compte GitHub dans l’organisation.

Mise en place en 3 lignes  
1) Activer GitHub Pages sur le dépôt (ou un dépôt dédié `gh-pages`) au niveau de l’organisation  
2) Restreindre l’accès aux **membres de l’organisation** dans les paramètres Pages  
3) Déployer depuis la CI vers la branche `gh-pages` via `peaceiris/actions-gh-pages` (destination `draft/`)

### 5.2 production

Déploiement `main` vers GitHub Pages (branche `gh-pages`, racine). Accès selon politique de l’organisation.

---

## 6. conformité et transparence

### 6.1 blocs légaux à intégrer

Bloc pour `docs/index.md`

```
## Déclarations d’accessibilité

Pour chaque service
- Nom du service
- URL de la déclaration d’accessibilité
- Date de mise à jour de la déclaration
- Méthode d’évaluation (audit interne/tiers, date)
- Contact accessibilité

## Mentions de charge disproportionnée

Si applicable, pour chaque service
- Fonctionnalité/section concernée
- Justification documentée (technique/financière/organisationnelle)
- Alternative proposée (canal/équivalent)
- Échéance de réévaluation
```

Bloc pour chaque module (en pied de page)

```
## publication et conformité

- Déclaration d’accessibilité: [URL]
- Charge disproportionnée: [Oui/Non]. Si Oui, préciser
  - Élément: [...]
  - Justification: [...]
  - Alternative: [...]
  - Réévaluation: [date]
```

---

## 7. guide contributeur (1 page)

Option A interface GitHub (débutants)  
1) aller sur github.com/[org]/span-sg  
2) docs/modules/[service].md  
3) icône crayon Edit  
4) cocher uniquement les lignes `<!-- DINUM -->`  
5) Commit changes  
6) PR vers `draft`

Option B Git local (avancés)  
clone, branche, éditer, `docker compose up`, commit, push, PR.

---

## 8. maintenance minimale

Hebdomadaire revue PR + synthèse CI.  
Mensuelle merge draft→main + tag version + export PDF d’archive.  
Trimestrielle mise à jour dépendances et revue globale.

---

## 9. release en 5 étapes

But  
Tag, traçabilité, PDF d’archive attaché à la release.

Étapes  
1) préparer la version  
   Mettre à jour la version/date en tête de PRD et vérifier la synthèse CI.  
2) changelog bref  
   Créer/mettre à jour `CHANGELOG.md`  
   ```
   ## vX.Y.Z – AAAA-MM-JJ
   - Ajout …
   - Correction …
   - Note d’impact …
   ```  
3) taguer  
   ```bash
   git tag -a vX.Y.Z -m "Release SPAN SG vX.Y.Z"
   git push origin vX.Y.Z
   ```  
4) construire et récupérer artefacts  
   CI publie `site/` et `exports/span-sg.pdf`.  
5) créer la release GitHub  
   Titre `SPAN SG vX.Y.Z`  
   Joindre `exports/span-sg.pdf`  
   Lier le changelog et la décision GO/NO-GO.

Critères d’acceptation  
Release publiée avec tag, changelog ≤ 3 puces, PDF joint.

---

## 10. décisions et hypothèses mvp

Décisions figées  
- Preview privée: GitHub Pages restreint aux membres de l’organisation (Option A)  
- PDF d’archive: plugin principal + fallback `mkdocs-with-pdf` + filet impression navigateur  
- Modèles légaux: blocs standardisés dans `index.md` et dans chaque module

Hors périmètre MVP  
dashboard temps réel, API, notifications, signature électronique, multi-tenant.

---

## 11. plan de mise en œuvre

Semaine 1 setup  
[ ] repo GitHub privé  
[ ] docker local  
[ ] mkdocs base + strict  
[ ] template 31 `<!-- DINUM -->`  
[ ] script scoring testé  
[ ] import module SIRCOM

Semaine 2 automatisation  
[ ] GitHub Actions ordre corrigé  
[ ] export PDF + fallback  
[ ] preview privée (Option A)  
[ ] doc contributeur 1 page

Semaine 3 onboarding services  
[ ] modules vides + front-matter  
[ ] formation Git basique 2 h  
[ ] premiers contenus

Semaine 4 production  
[ ] review contenus  
[ ] validation Yves  
[ ] tag v1.0.0  
[ ] publication

---

## 12. contacts

| Rôle | Nom | GitHub |
|------|-----|--------|
| Owner | Alexandra | @alexandra |
| Validateur | Bertrand | @bertrand |
| Validateur | Alex | @alex |
| Sponsor | Yves | - |

---

## 13. décision go/no-go

- [ ] architecture v3.3 validée  
- [ ] repository créé  
- [ ] accès configurés  
- [ ] template checklist approuvé  
- [ ] script scoring testé  
- [ ] planning accepté

*PRD v3.3 avec checklist officielle, 30 septembre 2025*  
*Principe: simple, fonctionnel, efficace, conforme*

---

# annexes « prêts à coller »

## A. scripts/calculate_scores.py

*(identique au bloc 3.2 ci-dessus, fourni pour collage direct dans le repo)*

## B. mkdocs-with-pdf.yml

```yaml
site_name: SPAN SG
theme:
  name: material
plugins:
  - with-pdf:
      output_path: exports/span-sg.pdf
      cover_title: "SPAN SG"
      toc_level: 2
```

## C. .github/workflows/build.yml

```yaml
name: Build SPAN

on:
  push:
    branches: [main, draft]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install mkdocs-material
          pip install mkdocs-pdf-export-plugin
          pip install mkdocs-with-pdf

      - name: Calculate SPAN scores
        run: python scripts/calculate_scores.py

      - name: Build site
        run: mkdocs build

      - name: Generate PDF (plugin principal)
        run: mkdocs build --config-file mkdocs-pdf.yml
        continue-on-error: true

      - name: Generate PDF fallback (mkdocs-with-pdf si échec)
        if: failure()
        run: mkdocs build --config-file mkdocs-with-pdf.yml

      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: span-site
          path: |
            site/
            exports/

  deploy_draft:
    if: github.ref == 'refs/heads/draft'
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy draft to GitHub Pages (org-only)
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages
          destination_dir: draft
          force_orphan: true

  deploy_main:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy production to GitHub Pages (org-only)
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages
          force_orphan: true
```

## D. docs/index.md – blocs légaux

```markdown
## Déclarations d’accessibilité

Pour chaque service
- Nom du service
- URL de la déclaration d’accessibilité
- Date de mise à jour de la déclaration
- Méthode d’évaluation (audit interne/tiers, date)
- Contact accessibilité

## Mentions de charge disproportionnée

Si applicable, pour chaque service
- Fonctionnalité/section concernée
- Justification documentée (technique/financière/organisationnelle)
- Alternative proposée (canal/équivalent)
- Échéance de réévaluation
```

## E. docs/modules/_template.md – squelette 31 points balisés

```markdown
---
service: [SERVICE]
referent: "[Prénom Nom]"
updated: "2025-09-30"
---

# SPAN [SERVICE] - Schéma Pluriannuel d'accessibilité numérique

**Période** 2025-2027  
**Score global** [X/31] questions validées ([XX] %)  
**Dernière mise à jour** [DATE]

## points de contrôle officiels (31)

- [ ] Point #01 <!-- DINUM -->
- [ ] Point #02 <!-- DINUM -->
- [ ] Point #03 <!-- DINUM -->
- [ ] Point #04 <!-- DINUM -->
- [ ] Point #05 <!-- DINUM -->
- [ ] Point #06 <!-- DINUM -->
- [ ] Point #07 <!-- DINUM -->
- [ ] Point #08 <!-- DINUM -->
- [ ] Point #09 <!-- DINUM -->
- [ ] Point #10 <!-- DINUM -->
- [ ] Point #11 <!-- DINUM -->
- [ ] Point #12 <!-- DINUM -->
- [ ] Point #13 <!-- DINUM -->
- [ ] Point #14 <!-- DINUM -->
- [ ] Point #15 <!-- DINUM -->
- [ ] Point #16 <!-- DINUM -->
- [ ] Point #17 <!-- DINUM -->
- [ ] Point #18 <!-- DINUM -->
- [ ] Point #19 <!-- DINUM -->
- [ ] Point #20 <!-- DINUM -->
- [ ] Point #21 <!-- DINUM -->
- [ ] Point #22 <!-- DINUM -->
- [ ] Point #23 <!-- DINUM -->
- [ ] Point #24 <!-- DINUM -->
- [ ] Point #25 <!-- DINUM -->
- [ ] Point #26 <!-- DINUM -->
- [ ] Point #27 <!-- DINUM -->
- [ ] Point #28 <!-- DINUM -->
- [ ] Point #29 <!-- DINUM -->
- [ ] Point #30 <!-- DINUM -->
- [ ] Point #31 <!-- DINUM -->

## périmètre du service

| Type | Total | Audités | Conformes | Score |
|------|-------|---------|-----------|-------|
| Sites web | | | | % |
| Intranets | | | | % |
| Applications | | | | % |

## plan d'actions prioritaires 2025

| Action | Échéance | Responsable | Budget | Statut |
|--------|----------|-------------|--------|--------|
| | T1 2025 | | € | |
| | T2 2025 | | € | |

## publication et conformité

- Déclaration d’accessibilité: [URL]
- Charge disproportionnée: [Oui/Non]. Si Oui, préciser
  - Élément: [...]
  - Justification: [...]
  - Alternative: [...]
  - Réévaluation: [date]

---
*Dernière mise à jour [date]*
```


## clarification périmètre v1

Seuls les 6 modules suivants sont inclus en v1: SNUM, SIRCOM, SRH, SIEP, SAFI, BGS. Les autres directions sont planifiées en phase 2+.


## options non retenues (mvp)

- HTML avec includes: non retenu (CDC impose MkDocs/GitHub Pages)
- PHP avec includes: non retenu (CDC impose MkDocs/GitHub Pages)
