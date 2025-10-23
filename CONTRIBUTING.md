# Guide de contribution SPAN SG

## Principe

Chaque service gère son propre module dans `docs/modules/[service].md`.
Les modifications passent par une **Pull Request** vers `main` pour validation.

---

## Option A : Interface GitHub (recommandé pour débutants)

**Pas besoin de Git, tout se fait dans le navigateur.**

### 1. Aller sur le fichier de votre service

https://github.com/Alexmacapple/span-sg-repo/blob/main/docs/modules/[votre-service].md

Exemple : `sircom.md`, `snum.md`, `srh.md`, etc.

### 2. Cliquer sur l'icône ✏️ (Edit this file)

En haut à droite du fichier.

### 3. Modifier le contenu

**Ce que vous pouvez faire** :

- ✅ Cocher des cases `[x]` dans les 33 critères de conformité
- ✅ Compléter les sections 1-5 (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- ✅ Ajouter des actions au tableau "Plan d'actions prioritaires"
- ✅ Renseigner l'URL de déclaration d'accessibilité

**Ce que vous ne devez PAS faire** :

- ❌ Ajouter/supprimer des lignes `<!-- CHECKLIST -->`
- ❌ Modifier la structure (titres des sections)
- ❌ Toucher au front-matter (section `---` en haut)

### 4. Sauvegarder et créer la Pull Request

En bas de la page :

- **Commit message** : `feat(sircom): ajoute 3 actions au plan 2025` (exemple)
- ☑ **Create a new branch** : `update-sircom-[date]`
- Cliquer **Propose changes**

Sur la page suivante :

- **Base** : `main` (important !)
- **Compare** : votre branche
- Cliquer **Create Pull Request**

### 5. Validation

Alexandra reviendra la PR et la mergera si OK.
Vous recevrez une notification par email.

Après merge vers main : Auto-deploy Staging (https://alexmacapple.github.io/span-sg/draft/) puis approval Alexandra pour Production. Voir ADR-009.

---

## Option B : Git local (avancés)

**Nécessite Git installé localement.**

### 1. Cloner le repo

```bash
git clone https://github.com/Alexmacapple/span-sg-repo.git
cd span-sg-repo
```

### 2. Créer une branche feature

```bash
git checkout main
git pull origin main
git checkout -b feature/update-[votre-service]
```

### 3. Éditer votre module

```bash
# Ouvrir dans votre éditeur
code docs/modules/[votre-service].md

# OU
vim docs/modules/[votre-service].md
```

### 4. Prévisualiser en local (optionnel)

```bash
docker compose up
# Ouvrir http://localhost:8000/span-sg-repo/
```

### 5. Committer et pusher

```bash
git add docs/modules/[votre-service].md
git commit -m "feat(service): description des modifications"
git push -u origin feature/update-[votre-service]
```

### 6. Créer la Pull Request

Sur GitHub :

- Cliquer le lien affiché dans le terminal
- OU aller sur https://github.com/Alexmacapple/span-sg-repo/pulls → New Pull Request
- **Base** : `main`
- **Compare** : votre branche

---

## Tests et Coverage

### Exécuter tests localement

```bash
# Tests unitaires seuls
pytest scripts/test_*.py -v

# Tests avec coverage production (89%+ requis)
./scripts/check_coverage.sh

# Générer rapport HTML
pytest --cov=scripts --cov-report=html scripts/test_*.py
open tests/htmlcov/index.html
```

### Objectif Coverage

**Scripts production** : 89%+ obligatoire (calculate_scores, enrich_pdf_metadata)
- CI bloquée si coverage < 89%
- Configuration .coveragerc exclut scripts dev + __main__ blocks
- Rapport généré automatiquement dans Actions

**Scripts développement** : Non requis (add-bmad-headers, evaluate-bmad-final)
- Outils internes, non utilisés en production
- Tests optionnels

### Ajouter nouveaux tests

1. Créer fichier `test_[module].py` dans `scripts/`
2. Run coverage : `./scripts/check_coverage.sh`
3. Viser 89%+ pour modules production
4. Commit avec tests inclus

### Note Coverage ImportError

Les lignes 23-26 de `enrich_pdf_metadata.py` (ImportError pikepdf) ne sont pas testées :
- Import top-level difficile à mocker proprement
- pikepdf toujours installé (requirements.txt + CI + Docker)
- Edge case non critique (erreur claire si pikepdf absent)
- Coverage production scripts : 89.6% acceptable

---

## Pre-commit Hooks

Hooks automatiques pour valider qualité et sécurité du code AVANT commit.

### Installation

```bash
# Installer pre-commit
pip install pre-commit

# Activer hooks dans le repo
pre-commit install

# Vérifier installation (run sur tous fichiers)
pre-commit run --all-files
```

### Hooks Actifs

1. **Gitleaks** : Détection secrets et credentials
   - Scanne patterns secrets (API keys, tokens, passwords)
   - Bloque commit si secret détecté
   - Prévient fuites credentials accidentelles
   - Exemples: AWS keys, GitHub tokens, private keys

2. **Bandit** : Détection patterns insecures Python
   - Severity: HIGH et CRITICAL bloquent commit
   - Exclude: tests/ (évite faux positifs subprocess)
   - Exemples: shell=True, eval/exec, hardcoded secrets

3. **Safety** : Check CVE dépendances
   - Base PyUp.io (200k+ vulnérabilités)
   - Scan requirements-dsfr.txt
   - Redondant avec Dependabot (mais feedback plus rapide)

4. **Black** : Formatage automatique code
   - Config: pyproject.toml (line-length 88)
   - Modifie fichiers automatiquement

5. **Ruff** : Linting Python
   - Checks: E, W, F, I, N (pycodestyle, pyflakes, isort, naming)
   - Auto-fix activé (--fix)

### Bypass Hooks (si nécessaire)

```bash
# Skip hooks pour commit urgence/WIP
git commit --no-verify -m "wip: bypass hooks"

# ⚠️  ATTENTION: CI bloquera quand même si issues réelles
```

### Mise à Jour Hooks

```bash
# Mettre à jour vers dernières versions
pre-commit autoupdate

# Re-run sur tous fichiers après update
pre-commit run --all-files
```

### Troubleshooting

**Hook fail sans raison apparente** :
```bash
# Clear cache hooks
pre-commit clean
pre-commit install --install-hooks
```

**Bandit faux positif (tests)** :
- Vérifier `exclude: ^tests/` dans `.pre-commit-config.yaml`
- Ou ajouter commentaire `# nosec` sur ligne concernée

**Safety timeout** :
- API PyUp.io peut être lente (< 30s normal)
- Retry : `pre-commit run safety --all-files`

**Gitleaks faux positif** :
- Créer `.gitleaksignore` à la racine avec paths à ignorer
- Ou ajouter `gitleaks:allow` en commentaire sur ligne concernée
- Exemple : `API_KEY = "test-key" # gitleaks:allow`

---

## Tests End-to-End (E2E)

### Exécuter tests E2E localement

```bash
# Tous les scénarios
./tests/e2e/run_all.sh

# Scénario spécifique
./tests/e2e/scenario_performance.sh
./tests/e2e/scenario_frontmatter.sh

# Avec rapport HTML (identique CI)
./tests/e2e/ci_runner.sh
open tests/e2e/reports/e2e-report.html
```

### Scénarios E2E disponibles

| Scénario | Description | Temps |
|----------|-------------|-------|
| **test_full_workflow** | Workflow complet (calcul scores + build + PDF) | ~15s |
| **scenario_multi_modules** | Calcul scores 6 modules | ~8s |
| **scenario_erreur_perimetre** | Module ≠33 critères → erreur | ~5s |
| **scenario_erreur_markdown** | Markdown invalide → build fail | ~5s |
| **scenario_performance** | Temps build < 10s | ~10s |
| **scenario_pdf_complet** | PDF généré avec métadonnées | ~12s |
| **scenario_rollback** | Intégrité après rollback Git | ~12s |
| **scenario_preview_http** | Serveur MkDocs démarrable | ~8s |
| **scenario_frontmatter** | Validation YAML front-matter | ~5s |

### Ajouter nouveau test E2E

1. Créer script `tests/e2e/scenario_[nom].sh`
2. Utiliser structure standardisée :
   ```bash
   #!/usr/bin/env bash
   set -euo pipefail
   PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
   cd "$PROJECT_ROOT"

   echo "Scénario : [Description]"

   # ... vos tests ...

   echo "✅ Scénario [nom] OK"
   ```
3. Ajouter dans `ci_runner.sh` (array SCENARIOS)
4. Tester localement : `./tests/e2e/ci_runner.sh`
5. Commit et pusher (CI exécutera automatiquement)

### CI Integration

Tests E2E exécutés automatiquement sur :
- ✅ Push vers `main`
- ✅ Pull Requests
- ✅ Job séparé dans GitHub Actions
- ✅ Rapport HTML disponible dans Actions artifacts (30 jours)

**En cas d'échec** :
1. Consulter logs CI (onglet Actions)
2. Télécharger artefact `e2e-report`
3. Ouvrir `e2e-report.html` localement
4. Reproduire scénario échoué en local
5. Corriger et repousher

**Temps CI E2E** : ~2 min (9 scénarios séquentiels)

---

## Règles de validation des PR

Chaque PR est vérifiée automatiquement (CI) et manuellement (Alexandra) :

### Vérifications automatiques (CI)
- ✅ Exactement 33 critères `<!-- CHECKLIST -->` présents (ou 0 si module vide)
- ✅ Pas de liens cassés (mode strict MkDocs)
- ✅ Synthèse recalculée sans erreur

### Vérifications manuelles
- ✅ Front-matter à jour (service, referent, updated)
- ✅ Contenu cohérent et de qualité
- ✅ Blocs légaux remplis (déclaration accessibilité)
- ✅ Pas de secrets/informations sensibles

---

## Workflow complet

```
Service modifie son module (branche feature)
          ↓
   PR vers main (code review)
          ↓
Revue Alexandra (validateur)
          ↓
Merge PR → Auto-deploy Staging (/draft/)
          ↓
Revue Alexandra sur Staging
          ↓
Approval Alexandra (deployment review)
          ↓
Deploy Production (/)
```

**Détails architecture** : Voir [ADR-009](docs/adr/009-migration-github-environments.md) et [Guide Chef SNUM](docs/guide-chef-snum-approvals.md).

---

## Gestion des Versions

### CHANGELOG.md

Tous les changements notables sont documentés dans [CHANGELOG.md](CHANGELOG.md).

**Mise à jour CHANGELOG** :
- Chaque PR significative ajoute entry dans section `[Unreleased]`
- Catégories : `Added`, `Changed`, `Fixed`, `Security`
- Format : Bullet point descriptif concis

**Exemple** :
```markdown
## [Unreleased]

### Added
- Tests E2E automatisés CI avec reporting HTML (S6-01)

### Fixed
- Migration vers 33 critères CHECKLIST officiels (ADR-006)
```

**Release** :
Lors de la création d'une release (tag vX.Y.Z) :
1. Déplacer section `[Unreleased]` vers `[X.Y.Z] - AAAA-MM-JJ`
2. Ajouter lien release en bas de fichier
3. Créer nouvelle section `[Unreleased]` vide

Note : Le processus de release est automatisé via le script `scripts/release.sh`. Voir section [Processus de Release Automatisé](#processus-de-release-automatisé) pour la documentation complète.

### Semantic Versioning

SPAN SG suit [SemVer 2.0.0](https://semver.org/lang/fr/) :
- **MAJOR (X.0.0)** : Breaking changes (ex: refonte structure modules, modification checklist critères)
- **MINOR (1.X.0)** : Nouvelles fonctionnalités rétrocompatibles (ex: nouveau module)
- **PATCH (1.0.X)** : Corrections bugs rétrocompatibles (ex: fix calcul score)

**Exemples** :
- v1.0.0 → v1.1.0 : Ajout module SRH (nouvelle fonctionnalité)
- v1.1.0 → v1.1.1 : Fix lien cassé module SIRCOM (correction)
- v1.1.1 → v2.0.0 : Migration 31 → 33 critères CHECKLIST (breaking change, voir ADR-006)

### Migration Versions

Pour migrer entre versions majeures, consultez [MIGRATION.md](MIGRATION.md).

Guides disponibles :
- v0.x → v1.0 : Migration POC vers production
- v1.x → v2.0 : Migration vers checklist officielle 33 critères DINUM (voir ADR-006)

---

## Processus de Release Automatisé

Le projet inclut un script de release automatisé qui standardise et sécurise la création de nouvelles versions.

### Vue d'ensemble

Le script `scripts/release.sh` automatise l'ensemble du workflow de release :
- Validation des prérequis (branche, working tree, CI)
- Vérification CHANGELOG.md
- Calcul des scores actuels
- Test build MkDocs
- Création du tag annoté
- Génération des release notes
- Instructions pour publication GitHub Release

### Prérequis

Avant d'exécuter le script, assurez-vous que :
- Vous êtes sur la branche `main` (ou prêt à checkout)
- Votre working tree est propre (pas de modifications non committées)
- La CI GitHub Actions est verte sur `main`
- Le CHANGELOG.md contient une section pour la version à publier

Note : Le script `release.sh` a été créé avant la migration GitHub Environments (ADR-009) et vérifie toujours la branche `draft`. Cette branche n'existe plus depuis le 22/10/2025. Le script checkout automatiquement `main` si vous n'êtes pas sur `draft`

### Utilisation de base

```bash
# Syntaxe
./scripts/release.sh vX.Y.Z

# Exemples
./scripts/release.sh v1.0.1    # Patch (correction bug)
./scripts/release.sh v1.1.0    # Minor (nouvelle fonctionnalité)
./scripts/release.sh v2.0.0    # Major (breaking change)
```

### Ce que fait le script automatiquement

1. **Vérifications prérequis** :
   - Checkout branche `main` si nécessaire
   - Vérification working tree propre
   - Vérification que le tag n'existe pas déjà
   - Vérification présence CHANGELOG.md

2. **Validation contenu** :
   - Vérification section version dans CHANGELOG.md
   - Proposition d'édition CHANGELOG si section manquante
   - Calcul scores SPAN actuels (via `calculate_scores.py`)
   - Test build MkDocs en mode strict

3. **Préparation release** :
   - Commit préparatoire (CHANGELOG + synthèse)
   - Push vers origin
   - Attente validation CI (confirmation manuelle)

4. **Création tag** :
   - Génération message tag détaillé (score, highlights, changelog)
   - Création tag annoté Git
   - Push tag vers origin

5. **Génération artefacts** :
   - Création fichier `RELEASE-NOTES-vX.Y.Z.md`
   - Instructions pour téléchargement PDF depuis CI
   - Commandes prêtes à copier pour GitHub Release

### Étapes post-release

Après exécution du script, effectuer manuellement :

1. **Créer GitHub Release** :
   ```bash
   # Aller sur https://github.com/Alexmacapple/span-sg/releases/new
   # - Tag : vX.Y.Z (sélectionner tag créé)
   # - Title : SPAN SG vX.Y.Z
   # - Description : Copier depuis RELEASE-NOTES-vX.Y.Z.md
   # - Assets : Télécharger exports/span-sg.pdf depuis CI et joindre
   ```

2. **Vérifier déploiement production** :
   - Consulter https://alexmacapple.github.io/span-sg/
   - Vérifier version déployée correspond au tag

3. **Communication** :
   - Annoncer release à l'équipe
   - Notifier les référents de services si applicable

### Exemples d'utilisation

**Cas 1 : Correction bug (PATCH)**
```bash
# Contexte : Fix lien cassé dans module SIRCOM
git checkout main
git pull origin main

# Vérifier CHANGELOG.md contient section v1.0.1
# Section présente : ## [1.0.1] - 2025-10-23 avec entry "Fixed"

./scripts/release.sh v1.0.1

# Suivre les prompts :
# - Committer préparation ? Y
# - CI est verte ? Y (vérifier Actions)
# - Pusher tag ? Y

# Créer GitHub Release manuellement (instructions affichées)
```

**Cas 2 : Nouvelle fonctionnalité (MINOR)**
```bash
# Contexte : Ajout nouveau module SRH
git checkout main
git pull origin main

# Éditer CHANGELOG.md pour ajouter section v1.1.0
# Ajouter entrée "Added" pour nouveau module

./scripts/release.sh v1.1.0

# Script propose d'éditer CHANGELOG.md si section manquante
# Suivre workflow complet
```

**Cas 3 : Breaking change (MAJOR)**
```bash
# Contexte : Migration vers nouvelle structure checklist
git checkout main
git pull origin main

# CHANGELOG.md doit documenter breaking changes
# Section v2.0.0 avec détails migration

./scripts/release.sh v2.0.0

# Vérifier MIGRATION.md à jour pour utilisateurs
# Communiquer largement breaking changes
```

### Troubleshooting

**Erreur : "Working tree pas propre"**
```bash
# Vérifier modifications
git status

# Committer ou stash modifications
git add .
git commit -m "chore: prepare for release"
# OU
git stash
```

**Erreur : "Tag vX.Y.Z existe déjà"**
```bash
# Lister tags existants
git tag -l

# Supprimer tag local si erreur
git tag -d vX.Y.Z

# Supprimer tag remote (ATTENTION : seulement si pas encore publié)
git push origin :refs/tags/vX.Y.Z
```

**Erreur : "CHANGELOG.md toujours sans section"**
```bash
# Éditer CHANGELOG.md manuellement
vim CHANGELOG.md

# Ajouter section au format Keep a Changelog :
## [X.Y.Z] - AAAA-MM-JJ

### Added
- Nouvelles fonctionnalités

### Fixed
- Corrections bugs

# Relancer script
./scripts/release.sh vX.Y.Z
```

**CI pas verte**
```bash
# Consulter Actions GitHub
# Attendre fin CI ou corriger erreurs

# Vérifier statut
gh run list --branch main --limit 5

# Re-vérifier après corrections
./scripts/release.sh vX.Y.Z
```

**PDF manquant dans artefacts CI**
```bash
# Vérifier job build-and-test terminé avec succès
gh run view --log

# Télécharger artefacts manuellement
RUN_ID=$(gh run list --branch main --limit 1 --json databaseId --jq '.[0].databaseId')
gh run download "$RUN_ID" --name exports-* --repo Alexmacapple/span-sg

# OU utiliser script utilitaire
./scripts/download_latest_pdf.sh main
```

---

## Sécurité

### Signaler une Vulnérabilité

**Ne créez PAS d'issue publique pour les vulnérabilités de sécurité.**

Consultez [SECURITY.md](SECURITY.md) pour la procédure de responsible disclosure.

### Dependabot

Le projet utilise Dependabot pour détecter automatiquement les vulnérabilités :
- **Scan hebdomadaire** : Lundi 9h (dépendances Python + GitHub Actions)
- **PR automatiques** : Vulnérabilités CVE créent des PR immédiatement
- **Labels** : `dependencies`, `security`, `ci`

**Reviewer PR Dependabot** :
1. Consulter CHANGELOG dépendance mise à jour
2. Vérifier breaking changes
3. Tester localement si changements majeurs
4. Merger si CI passe

### Secrets et Données Sensibles

**Interdictions strictes** :
- ❌ Committer secrets (tokens, passwords, API keys)
- ❌ Committer données personnelles
- ❌ Committer fichiers sensibles (même temporairement)

**Si secret committé par erreur** :
1. Ne pas simplement supprimer (reste dans historique Git)
2. Suivre guide BFG : `docs/security/bfg-purge-guide.md`
3. Révoquer immédiatement secret compromis
4. Notifier équipe sécurité

### Bonnes Pratiques

- ✅ Utiliser variables d'environnement pour secrets locaux
- ✅ Vérifier `.gitignore` avant commit
- ✅ Run `git diff --cached` avant push
- ✅ Activer notifications Dependabot
- ✅ Maintenir dépendances à jour (merge PR Dependabot régulièrement)

---

## Besoin d'aide ?

- **Questions techniques** : Alexandra (alexandra.guiderdoni@gmail.com)
- **Vulnérabilités sécurité** : Voir [SECURITY.md](SECURITY.md)
- **Issues GitHub** : <https://github.com/Alexmacapple/span-sg-repo/issues>

---

**Principe directeur : Simple, fonctionnel, efficace.**

---

## Note sur les URLs

**URLs actuelles** : Ce projet est hébergé sur `Alexmacapple/span-sg-repo` (compte utilisateur).

**Migration prévue** : Lors de la mise en production, le dépôt sera transféré vers une organisation GitHub. Les URLs seront mises à jour à ce moment-là.
