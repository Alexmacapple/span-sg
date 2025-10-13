# Guide de contribution SPAN SG

## Principe

Chaque service gère son propre module dans `docs/modules/[service].md`.
Les modifications passent par une **Pull Request** vers `draft` pour validation.

---

## Option A : Interface GitHub (recommandé pour débutants)

**Pas besoin de Git, tout se fait dans le navigateur.**

### 1. Aller sur le fichier de votre service

https://github.com/Alexmacapple/span-sg-repo/blob/draft/docs/modules/[votre-service].md

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

- **Base** : `draft` (important !)
- **Compare** : votre branche
- Cliquer **Create Pull Request**

### 5. Validation

Bertrand ou Alex reviendra la PR et la mergera si OK.
Vous recevrez une notification par email.

Preview désactivée : revue locale/PDF. Voir `docs/dev-local.md` et `.github/PAGES-ACCESS-CHECKLIST.md`.

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
git checkout draft
git pull origin draft
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
- **Base** : `draft`
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

1. **Bandit** : Détection patterns insecures Python
   - Severity: HIGH et CRITICAL bloquent commit
   - Exclude: tests/ (évite faux positifs subprocess)
   - Exemples: shell=True, eval/exec, hardcoded secrets

2. **Safety** : Check CVE dépendances
   - Base PyUp.io (200k+ vulnérabilités)
   - Scan requirements-dsfr.txt
   - Redondant avec Dependabot (mais feedback plus rapide)

3. **Black** : Formatage automatique code
   - Config: pyproject.toml (line-length 88)
   - Modifie fichiers automatiquement

4. **Ruff** : Linting Python
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
- ✅ Push vers `draft` ou `main`
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

Chaque PR est vérifiée automatiquement (CI) et manuellement (Bertrand/Alex) :

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
Service modifie son module
          ↓
   PR vers draft
          ↓
Revue Bertrand/Alex
          ↓
Merge dans draft → Revue locale/PDF (sans Pages)
          ↓
PR draft → main (mensuel)
          ↓
Présentation Stéphane → Validation Chef SNUM → Production
```

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

- **Questions techniques** : Bertrand (@bertrand), Alex (@alex)
- **Questions contenu** : Alexandra (@alexandra)
- **Vulnérabilités sécurité** : Voir [SECURITY.md](SECURITY.md)
- **Issues GitHub** : <https://github.com/Alexmacapple/span-sg-repo/issues>

---

**Principe directeur : Simple, fonctionnel, efficace.**

---

## Note sur les URLs

**URLs actuelles** : Ce projet est hébergé sur `Alexmacapple/span-sg-repo` (compte utilisateur).

**Migration prévue** : Lors de la mise en production, le dépôt sera transféré vers une organisation GitHub. Les URLs seront mises à jour à ce moment-là.
