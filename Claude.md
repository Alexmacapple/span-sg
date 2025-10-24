# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Version: 1.4
Date: 2025-10-23

## Langue et ton
- Répondre en français, sans émojis, concision.
- Respecter strictement le MVP et le cahier des charges.

## Règle stricte : Aucun émoji
- **JAMAIS d'émojis dans les fichiers Markdown** (✅ ❌ ⚠️ 🔄 ✓ ☑ ✏️ etc.)
- Exceptions : fichiers roadmap/ et inspiration/ (archives projet)
- Concerné : docs/, README.md, CONTRIBUTING.md, CHANGELOG.md, modules
- Remplacement : texte descriptif ("Validé", "En cours", "Conforme")

## Commandes essentielles

### Développement local
```bash
# Démarrer le serveur MkDocs en local (Docker DSFR)
docker compose -f docker-compose-dsfr.yml up
# → http://localhost:8000/span-sg/

# Sans Docker
pip install mkdocs-dsfr
mkdocs serve --config-file mkdocs-dsfr.yml

# Après modification de fichiers de configuration (mkdocs-dsfr.yml, navigation, etc.)
# Redémarrer le serveur pour voir les changements :
docker compose -f docker-compose-dsfr.yml restart

# Si le restart simple ne suffit pas, forcer la régénération complète :
docker compose -f docker-compose-dsfr.yml down && docker compose -f docker-compose-dsfr.yml up -d
```

### Build et génération
```bash
# Build site HTML
mkdocs build --config-file mkdocs-dsfr.yml

# Générer PDF (DSFR) - Nécessite libs système WeasyPrint
ENABLE_PDF_EXPORT=1 mkdocs build --config-file mkdocs-dsfr-pdf.yml

# Enrichir métadonnées PDF
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf

# Valider structure PDF
qpdf --check exports/span-sg.pdf

# Calculer les scores SPAN et générer docs/synthese.md
python scripts/calculate_scores.py
```

### Tests et validation
```bash
# Vérifier la configuration MkDocs (mode strict)
mkdocs build --strict

# Tester localement le scoring
python scripts/calculate_scores.py
# Attendu: 0 ou 31 points par module, sinon erreur
```

### CI et artefacts
```bash
# Télécharger PDF depuis dernière CI main
./scripts/download_latest_pdf.sh main

# Télécharger depuis staging (auto-deploy)
curl -O https://alexmacapple.github.io/span-sg/staging/exports/span-sg.pdf

# Télécharger depuis production
curl -O https://alexmacapple.github.io/span-sg/exports/span-sg.pdf

# Commande manuelle équivalente
RUN_ID=$(gh run list --branch main --limit 1 --json databaseId --jq '.[0].databaseId')
gh run download "$RUN_ID" --name exports-$COMMIT_SHA --repo Alexmacapple/span-sg
# → Télécharge exports/span-sg.pdf
```

### Workflow Git
```bash
# Créer une branche feature pour un service
git checkout -b feature/update-[service]

# Après modifications
git add docs/modules/[service].md
git commit -m "feat(service): description concise"
git push -u origin feature/update-[service]
# → créer PR vers main (validateur approve, puis auto-deploy staging)
```

## Architecture technique

### Pipeline de scoring (33 critères CHECKLIST)
Le système repose sur un **comptage strict** des cases cochées marquées `<!-- CHECKLIST -->`:
- `scripts/calculate_scores.py` scanne `docs/modules/*.md`
- Recherche les lignes: `- [x] ... <!-- CHECKLIST -->`
- Compte checked/total par module
- Échoue si total ≠ 0 ou 33 (validation périmètre)
- Génère `docs/synthese.md` avec tableau agrégé

**Règle absolue**: Ne jamais ajouter/supprimer de balises `<!-- CHECKLIST -->`. Seules les coches `[x]` peuvent être modifiées.

**Source officielle**: Checklist de 33 critères extraite du fichier DINUM/Arcom `SPAN-checklist-v2024-02-05-AAL.ots` (voir ADR-006).

### Workflow checklist et interactivité

**Édition et calcul:**
1. Éditer markdown: cocher/décocher cases `- [x]` ou `- [ ]` avec balise `<!-- CHECKLIST -->`
2. Exécuter: `python scripts/calculate_scores.py`
3. Script met à jour automatiquement:
   - Ligne "Score global X/33 critères validés (Y%)" dans chaque module
   - Tableau agrégé dans `docs/synthese.md`

**Checkboxes interactives web (mkdocs-dsfr.yml):**
- Extension `pymdownx.tasklist` activée avec `clickable_checkbox: true`
- Checkboxes cliquables dans interface MkDocs pour visualisation/démonstration
- État NON persisté : refresh page réinitialise les coches
- Source de vérité : fichiers markdown + CI/CD

**Limitations:**
- Pas de localStorage (hors scope MVP)
- Cliquer dans web n'édite pas markdown source
- Workflow contributeur : édition markdown puis CI recalcule scores

### Structure modulaire
```
docs/modules/
├── _template.md         # Template avec 31 points DINUM officiels
├── snum.md             # 6 modules services v1
├── sircom.md
├── srh.md
├── siep.md
├── safi.md
└── bgs.md
```

Chaque module contient:
1. **Front-matter YAML**: service, referent, updated
2. **5 sections obligatoires**: Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs
3. **31 points de contrôle DINUM**: liste fixe avec `<!-- DINUM -->`
4. **Blocs légaux**: déclaration accessibilité, charge disproportionnée

### Configuration MkDocs
- `mkdocs.yml`: config principale Material (legacy, non utilisé)
- `mkdocs-dsfr.yml`: config principale DSFR (strict mode, nav, theme DSFR)
- `mkdocs-dsfr-pdf.yml`: génération PDF via `mkdocs-pdf-export-plugin`

**Mode strict activé**: toute erreur de lien/référence bloque le build.

### Hooks DSFR
Le thème DSFR utilise des hooks Python pour améliorer l'accessibilité :
- `hooks/dsfr_table_wrapper.py`: Encapsule les tableaux Markdown dans `<div class="fr-table">` pour le responsive DSFR
- `hooks/title_cleaner.py`: Nettoie les titres HTML redondants (regex post-processing)

### CI/CD GitHub Actions
Workflow `.github/workflows/build.yml` (3 jobs séquentiels):

1. **build-and-test** (toujours):
   - Install Python + dépendances MkDocs
   - Linting (Black, Ruff), Security (Bandit, Safety)
   - Tests unitaires (pytest, coverage 89%+)
   - Calcul scores (`python scripts/calculate_scores.py`)
   - Build site HTML (`mkdocs build`)
   - Génération PDF (`mkdocs build --config-file mkdocs-dsfr-pdf.yml`)
   - Tests E2E accessibilité (Selenium, 9 scénarios)
   - Upload artefacts (site/ + exports/)

2. **deploy-staging** (si push sur main):
   - Environment: `staging` (nécessite approval)
   - Deploy vers `gh-pages/staging/` après validation
   - URL: https://alexmacapple.github.io/span-sg/staging/

3. **deploy-production** (si push sur main):
   - Environment: `production` (nécessite approval Chef SNUM)
   - Deploy vers `gh-pages/` (racine)
   - URL: https://alexmacapple.github.io/span-sg/

### Branches et déploiements

**Architecture GitHub Environments** (depuis 23/10/2025):
- **1 branche unique**: `main` (source de vérité)
- **2 Environments GitHub** (double approbation):
  - `staging`: Deploy /staging/ avec approval (manuel)
  - `production`: Deploy / avec approval Chef SNUM (manuel)

**Branches de travail**:
- `feature/*`: modifications par service (PR vers main)
- `hotfix/*`: corrections urgentes (PR vers main)

**Workflow contributeur**:
1. Créer branche feature → PR vers main
2. Validateur approve PR (code review)
3. Merge → Pause staging (attente approval)
4. Approve staging → Deploy /staging/ (tests recette)
5. Approve production → Deploy / (Chef SNUM)

**Pages privées**: Restreint aux membres organisation (paramètre org-only).

**Documentation complète**: Voir [ADR-009](docs/adr/009-migration-github-environments.md) et [Guide Chef SNUM](docs/guide-chef-snum-approvals.md).

## Checklist pré-modification

Avant toute modification du code, de la documentation ou des modules, exécuter cette checklist obligatoire :

### 1. Contexte et préparation
- [ ] Lire la section pertinente de ce fichier CLAUDE.md
- [ ] Identifier le type de modification (contenu, scoring, architecture, CI/CD)
- [ ] Vérifier l'ADR pertinent si changement architectural (docs/adr/)
- [ ] Créer une branche feature/hotfix appropriée

### 2. Modifications de modules (docs/modules/*.md)
Si vous modifiez un fichier dans docs/modules/ :
- [ ] Vérifier que le front-matter YAML est complet (service, referent, updated)
- [ ] S'assurer que EXACTEMENT 0 ou 33 balises `<!-- CHECKLIST -->` sont présentes
- [ ] Ne PAS ajouter/supprimer de balises `<!-- CHECKLIST -->` (uniquement modifier `[x]`)
- [ ] Respecter les 5 sections obligatoires (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- [ ] Aucun émoji ajouté (sauf dans roadmap/ et inspiration/)

### 3. Validation locale obligatoire
Exécuter ces commandes AVANT de commit :
- [ ] `python scripts/calculate_scores.py` → Doit retourner 0 ou 33 points par module
- [ ] `mkdocs build --config-file mkdocs-dsfr.yml --strict` → Build sans erreur
- [ ] `pre-commit run --all-files` → Tous les hooks passent (linting, security)
- [ ] Tester localement : `docker compose -f docker-compose-dsfr.yml up`

### 4. Validation spécifique selon le type de modification

**Si modification de scripts Python (scripts/, hooks/)** :
- [ ] `python -m black --check scripts/ hooks/`
- [ ] `python -m ruff check scripts/ hooks/`
- [ ] `python -m pytest tests/unit/ -v --cov`

**Si modification de la CI (.github/workflows/)** :
- [ ] Tester localement avec `act` si possible
- [ ] Vérifier que les 3 jobs sont préservés (build-and-test, deploy-staging, deploy-production)
- [ ] Documenter le changement dans un ADR si impact architectural

**Si modification des dépendances (requirements*.txt)** :
- [ ] Justifier l'ajout dans la description de PR
- [ ] Vérifier les CVE avec `safety check -r requirements-dsfr.txt`
- [ ] Mettre à jour ADR-010 si changement de stratégie

### 5. Avant de créer la PR
- [ ] Commit message suit les conventions : `type(scope): description`
- [ ] Aucun secret ou credential dans les fichiers
- [ ] CHANGELOG.md mis à jour si nécessaire (features, breaking changes)
- [ ] Liens internes valides (mode strict les détectera, mais vérifier avant)

### En cas de doute
- Consulter CONTRIBUTING.md pour le processus détaillé
- Relire l'ADR pertinent dans docs/adr/
- Demander une revue de code anticipée aux validateurs

## Règles de modification

### Contraintes strictes
- Ne pas modifier la logique de scoring: 31 points balisés `<!-- DINUM -->` uniquement.
- Ne pas ajouter de dépendances ni de nouveaux plugins CI.
- Périmètre v1: 6 modules (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS).
- Aucune fonctionnalité hors périmètre (dashboard, API, notifications).
- Préserver `strict: true` dans `mkdocs.yml`.

### Modifications autorisées
- Cocher/décocher les cases `[x]` des 31 points DINUM
- Compléter les 5 sections obligatoires des modules
- Ajouter actions au plan 2025 (tableau)
- Renseigner URLs de déclaration d'accessibilité
- Mettre à jour front-matter (dates, référents)
- Corriger orthographe dans docs/ et PRD
- Préparer CHANGELOG pour releases

## Processus de release

### Préparer une version
```bash
# 1. Éditer CHANGELOG.md
# Ajouter section: ## vX.Y.Z – AAAA-MM-JJ

# 2. Créer tag
git tag -a vX.Y.Z -m "Release SPAN SG vX.Y.Z"
git push origin vX.Y.Z

# 3. Récupérer artefact PDF depuis Actions
# 4. Créer release GitHub avec exports/span-sg.pdf joint
```

### Checklist validation
- [ ] 31 points DINUM présents (ou 0 si module vide)
- [ ] Front-matter complet (service, referent, updated)
- [ ] Blocs légaux remplis ou TODO explicite
- [ ] Liens valides, pas de secrets
- [ ] CI passe (build-and-test + deploy-staging + deploy-production)
- [ ] Staging accessible (/staging/, org-only, après approval)
- [ ] Production déployée après approval Chef SNUM (/, org-only)

## Contacts et gouvernance
- **Owner/Validateur**: Alexandra (alexandra.guiderdoni@gmail.com)
- **Sponsor**: Stéphane (Chef mission numérique SNUM-SG, validation conceptuelle)
- **Validation finale production**: Chef SNUM

Note: Configuration Required Reviewers validée le 2025-10-23

## Références
- PRD complet: `PRD-v3.3.md`
- Checklist GO: `GO-CHECKLIST.md`
- Paramétrage Pages: `.github/PAGES-ACCESS-CHECKLIST.md`
- Instructions Agents (Cursor/Codex): `Agents.md`
