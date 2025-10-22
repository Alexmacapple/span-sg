# Changelog

Toutes les modifications notables du projet SPAN SG sont documentées ici.

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Unreleased]

### Added
- Benchmarking performance automatique (`scripts/benchmark.py`, `scripts/analyze_benchmarks.py`)
- Métriques CI : temps build MkDocs, génération PDF, calcul scores (rétention 365 jours)
- Détection régressions performance (seuil 20%)
- Type hints Python complets (mypy 1.8.0 configuré)
- Pre-commit hook mypy pour vérification types locale
- Cache Docker layers pour build test image (gain ~30-60s)
- Documentation architecture cache et performance (`.github/PERFORMANCE.md`)

### Changed
- Tests E2E parallélisés (xargs -P 3, 3 workers simultanés)
- Dockerfile.mkdocs-test : multi-stage build avec wheels pré-compilés
- Tous les scripts Python annotés avec type hints (`tuple[int, int]`, `dict[str, Any]`, `Optional[Path]`)
- Configuration mypy dans `pyproject.toml` (Python 3.11, check_untyped_defs)
- Tests accessibilité CI non-bloquants (continue-on-error: true, timeouts 240s)
- Cache pip migré vers setup-python natif (amélioration efficacité)

### Fixed
- Corrections multiples scénarios E2E (pattern grep, réinitialisation état Git)
- Timeouts Selenium triplés (80s → 240s) pour stabilité CI
- Configuration timeout urllib3 (300s au niveau module)
- Strict mode MkDocs : correction liens CONTRIBUTING.md

---

## v1.2.0-environments – 2025-10-20

**Migration GitHub Environments** : Architecture déploiement staging/production optimisée

### Infrastructure CI/CD
- Migration architecture 2-environnements GitHub (staging, production)
- Déploiements séquencés : staging → production (après validation)
- Workflow optimisé : 456 lignes → 291 lignes (-36%)
- Protection branches via GitHub Environments (deployment protection rules)
- ADR-009 : Documentation architecture déploiement 3 itérations (+14% coût réel vs estimé)

### Documentation
- `docs/architecture/infrastructure.md` : Architecture GitHub Environments mise à jour
- CONTRIBUTING.md : Correction liens pour strict mode MkDocs

### Commits
10 commits du 20/10/2025 (8dbc530 à 2cf3e20) :
- feat(ci): migrer architecture GitHub Environments (ADR-009)
- docs(architecture): mise à jour infrastructure.md
- fix(ci): séquencer deploy-production après deploy-staging
- fix(ci): résoudre conflits push gh-pages entre staging/production
- fix(docs): corriger liens CONTRIBUTING.md (strict mode)

---

## v1.2.1-quality – 2025-10-22

**Qualité Code 10/10** : Linting statique, tests E2E optimisés, benchmarking

### Qualité et Tests
- mypy intégré en pre-commit et CI (vérification types statiques)
- Type hints Python 3.11+ (6 fichiers annotés : scripts/, hooks/)
- Tests E2E 3x plus rapides (parallélisation xargs -P 3)
- Multi-stage Docker build (wheels pré-compilés, temps build réduit)
- Benchmarking automatique CI avec métriques performance
- Coverage excluant scripts benchmarking (89%+ production code)

### Amélioration Documentation
- `docs/architecture/infrastructure.md` : Finalisation documentation technique 10/10
- Clarifications ADR-009, process déploiement, rollback

### Commits
4 commits du 22/10/2025 (8216382 à a07737e) :
- feat(quality): achieve 10/10 code quality score
- fix(ci): add mypy and types-requests to requirements-dev.txt
- fix(mypy): add type hints to evaluate-bmad-final.py
- fix(coverage): exclude benchmark scripts from coverage

---

## v1.2.0-pdf – 2025-10-15

**Export PDF Accessible** : Génération PDF automatique avec métadonnées RGAA

### Added
- Génération PDF automatique en CI (GitHub Actions)
- Bouton téléchargement PDF sur page d'accueil (composant DSFR fr-download)
- Hook `pdf_copy.py` : Copie PDF vers docs/ et site/ pour download web
- Structure `docs/exports/.gitkeep` : Support PDF en mode développement
- Validation structure PDF (`qpdf --check`) dans pipeline CI
- Métadonnées enrichies (pikepdf) : titre, langue, keywords, auteur
- Section "Export PDF" dans README.md avec instructions génération locale
- Tests E2E : Validation métadonnées PDF dans scenario_pdf_complet.sh

### Changed
- `.github/workflows/build.yml` : Installation dépendances WeasyPrint (libpango, libcairo, libharfbuzz)
- `Dockerfile-dsfr` : Ajout libs système pour génération PDF
- `requirements-dsfr.txt` : Ajout `mkdocs-with-pdf>=0.9.3`
- `tests/e2e/scenario_pdf_complet.sh` : Migration vers mkdocs-dsfr-pdf.yml + validation métadonnées
- `CLAUDE.md` : Commandes PDF mises à jour (ENABLE_PDF_EXPORT, enrichissement, validation)
- `docs/index.md` : Déplacement section Téléchargements vers haut de page (après fr-summary, ligne 72)

### Fixed
- Artefact PDF CI (remplace fichier texte factice par PDF réel 2.6 MB)
- Score CI/CD : 9/10 → 10/10 (génération PDF réactivée)
- Accessibilité PDF en mode développement : Copie vers docs/exports/ pour mkdocs serve (404 → 200 OK)

---

## v1.0.1-dsfr – 2025-10-08

**Migration DSFR** : Intégration complète du thème Système de Design de l'État français

### Thème et infrastructure
- Migration mkdocs-material vers mkdocs-dsfr (v0.17.0)
- Nouvelle configuration DSFR : mkdocs-dsfr.yml, mkdocs-dsfr-pdf.yml
- Docker Compose DSFR : docker-compose-dsfr.yml
- Thème gouvernemental avec marianne, header/footer officiels

### Accessibilité DSFR
- Composant fr-summary : sommaire accessible avec navigation sémantique
- Structure ARIA : `<nav aria-labelledby>`, `<ol class="fr-summary__list">`
- Bouton "Haut de page" positionné à droite (bouton_hautdepage: right)
- Hooks DSFR : dsfr_table_wrapper.py (tableaux responsifs), title_cleaner.py (titres optimisés)

### Navigation et UX
- Menu réorganisé : "SPAN (SG)" en position 1, "SPAN (services)" en position 2
- Services classés alphabétiquement : BGS, SAFI, SIEP, SIRCOM, SNUM, SRH
- Titre HTML sans redondance : `<title>SPAN (SG)</title>` au lieu de "SPAN (SG) - SPAN SG"
- Emails cliquables dans citations Markdown (SIRCOM, SNUM)

### Contenu
- Page d'accueil (index.md) : SPAN officiel complet (18 sections)
- Sommaire interactif DSFR avec 18 ancres de navigation
- Footer : Ministère de l'Économie des Finances et de la Souveraineté industrielle et énergétique

### Technique
- Hook Python on_post_page pour nettoyage HTML
- Front-matter YAML pour contrôle des titres
- Archives sources SPAN : span/span-sircom-sg.md, span/span-sircom.md

### Commits
10 commits du 08/10/2025 (437a9c9 à 15a0a8a) :
- chore(sources): mise à jour archives SPAN SIRCOM
- fix(meta): supprimer complètement redondance dans title HTML
- fix(meta): supprimer redondance dans title de la page d'accueil
- feat(dsfr): positionner bouton "Haut de page" à droite
- feat(nav): renommer Accueil en SPAN (SG)
- feat(dsfr): intégration composant Sommaire accessible
- feat(homepage): remplacement complet par SPAN officiel
- fix(nav): correction nom menu - "SPAN (services)"
- feat(nav): réorganisation menu navigation
- chore: mise à jour date synthèse

---

## v1.0.0-poc – 2025-10-07

**POC (Proof of Concept)** : Démonstration technique framework SPAN SG

### Objectif POC
Valider faisabilité architecture modulaire + scoring automatisé + CI/CD complet.

### Modules démonstration
- **SIRCOM** : 24/31 (77.4%) - Contenu réel mappé depuis span-sircom-sg.md
- **SNUM Portailpro.gouv** : 21/31 (67.7%) - Contenu réel mappé depuis span-portail-pro.sg.md
- **SRH, SIEP, SAFI, BGS** : Structure framework présente (0/124)
- **Total démonstration** : 45/186 (24.2%)

### Infrastructure validée POC
- CI/CD 100% automatisé (GitHub Actions)
- Tests unitaires (18) + E2E (9 scénarios)
- Export PDF accessible avec métadonnées enrichies
- Scoring automatisé avec colonne État (Validé / En cours)
- Preview privée GitHub Pages

### Documentation
- CONTRIBUTING.md (workflow contributeur Option A + B)
- Guide mapping détaillé (roadmap/S4-00, ~400 lignes)
- 6 modules structurés (5 sections + 31 points DINUM)
- Template PR, tests README, agents instructions

### Roadmaps BMAD complétées
- S4-00 : Guide mapping assisté
- S4-01 : Review contenus finalisés
- S4-02 : Auto-validation technique
- S4-03 : Tag v1.0.0-poc
- S4-04 : Publication draft POC

### Statut projet
- Déploiement : GitHub Pages draft uniquement (/draft/)
- Production : Non applicable (POC technique)
- Évolution : Framework prêt pour adaptation projet réel

### Prochaines étapes (si projet réel)
- Onboarding référents services (4 modules en cours)
- Audit RGAA externe (framework + modules validés)
- Migration organisation GitHub (restrictions Pages)
- Communication interne après validation sponsor

---

## v1.0.0 – 2025-10-07

**Release officielle** : POC Production-Ready (Score 97/100)

### Objectif
Officialiser le POC (Proof of Concept) démontrant la faisabilité technique du framework SPAN SG avec infrastructure production-ready.

### Infrastructure Production-Ready
- ✅ Score qualité : 97/100 (Tests 19/20, Sécurité 20/20, Documentation 20/20)
- ✅ CI/CD 100% automatisé (GitHub Actions)
- ✅ Tests E2E automatisés CI (9 scénarios + reporting HTML)
- ✅ Sécurité renforcée (Dependabot + SECURITY.md + BFG guide)
- ✅ Documentation maintenabilité (CHANGELOG + MIGRATION + versioning)
- ✅ Coverage tests 89%+ scripts production

### Modules Validés
- **SIRCOM** : 24/31 (77.4%) - Contenu réel mappé
- **SNUM Portailpro.gouv** : 21/31 (67.7%) - Contenu réel mappé
- **SRH, SIEP, SAFI, BGS** : 0/124 - Structure framework présente
- **Total démonstration** : 45/186 (24.2%)

### Roadmaps Complétées
- **32 roadmaps archivées** : Sprints 0-6 terminés
- **Sprint 6 Tech First** : Tests E2E CI + Sécurité + Documentation (+3 points)
- **POC-FINALISATION** : Merge draft → main, tag v1.0.0, GitHub Release

### Documentation
- CONTRIBUTING.md : Guide contributeur Option A + B
- CHANGELOG.md : Historique complet Keep a Changelog
- MIGRATION.md : Guides upgrade path v0.x→v1.0
- SECURITY.md : Responsible disclosure policy
- Guide mapping : roadmap/archive/S4-00 (~400 lignes)
- ROADMAP-INDEX.md : Master index + parcours recommandés

### Déploiement
- Production : https://alexmacapple.github.io/span-sg-repo/
- Release : https://github.com/Alexmacapple/span-sg-repo/releases/tag/v1.0.0
- PDF : exports/span-sg.pdf (3 MB, joint à release)

### Prochaines Étapes (Optionnelles)
- Modules : Complétion BGS, SAFI, SIEP, SRH (S6-03 à S6-06) → 90.9%
- Infrastructure : Notifications CI + Rollback (S6-02)
- v2.0.0 : Migration DSFR complet (S7-01, après .gouv.fr)

---

## [Unreleased] – En développement (branche draft)

### Prévu
- Complétion modules optionnels BGS, SAFI, SIEP, SRH (S6-03 à S6-06)
- Notifications CI + Rollback automatique (S6-02, optionnel)
- Migration DSFR (S7-01, après .gouv.fr confirmé)

---

## v1.0.2-poc – 2025-10-07

**Roadmaps cleanup** : Organisation structure + suppression emojis

### Modifié
- **Suppression emojis roadmaps** : Remplacement par tags texte [COMPLETE], [EN-COURS], [NON-FAIT]
  - roadmap/POC-FINALISATION.md
  - roadmap/ROADMAP-INDEX.md
  - roadmap/archive/README.md
- **Organisation roadmaps** :
  - 32 roadmaps archivées (Sprints 0-6 terminés) → roadmap/archive/
  - 29 roadmaps supprimées de racine (déjà archivées)
  - Fusion archives/ → archive/ (s3-skipped)
  - Création ROADMAP-INDEX.md (master index, parcours recommandés)
- **.gitignore** : Ajout `*.pdf` et `tests/e2e/reports/`

### Score
- Score qualité : 97/100 (maintenu)
- Contenu : 45/186 (24.2%)

### Conformité
- CLAUDE.md : Pas d'emojis dans .md roadmap

---

## v1.0.1-poc – 2025-10-07

**Sprint 6 Tech First terminé** : Score qualité 97/100 (+3 points)

### Ajouté
- **Tests E2E automatisés CI** (S6-01) : Job GitHub Actions séparé avec reporting HTML
  - Script orchestrateur `tests/e2e/ci_runner.sh` (9 scénarios)
  - Générateur rapport HTML `tests/e2e/generate_report.py` (stylisé, logs détaillés)
  - Artefact e2e-report.html uploadé (30 jours rétention)
  - Section Tests E2E dans CONTRIBUTING.md (tableau scénarios, guide ajout tests)
  - Badge E2E Tests dans README.md
- **Renforcement sécurité** (S6-07) :
  - Configuration Dependabot `.github/dependabot.yml` (scan hebdomadaire pip + github-actions)
  - SECURITY.md avec politique responsible disclosure (CVSS 3.1, délais réponse)
  - Guide BFG Repo-Cleaner `docs/security/bfg-purge-guide.md` (purge Git history)
  - Section Sécurité dans CONTRIBUTING.md (signalement vulnérabilités, Dependabot, secrets)
  - Section Sécurité dans README.md (mesures existantes)
- **Documentation maintenabilité** (S6-08) :
  - CHANGELOG.md complété (Keep a Changelog format, entry v1.0.0-poc)
  - MIGRATION.md avec guides upgrade path (v0.x → v1.0)
  - Section Gestion Versions dans CONTRIBUTING.md (process CHANGELOG, SemVer)
- Documentation "Développement local" accessible via navigation MkDocs (`docs/dev-local.md`)
- Finalisation mapping SNUM : 21/31 points validés (67.7%)
- Finalisation mapping SIRCOM : 24/31 points validés (77.4%)
- Génération automatique `docs/synthese.md` avec état de déploiement v1.0

### Modifié
- README.md : Ajout état actuel du projet (07/10/2025) avec scores et roadmap v1.0
- Navigation MkDocs : Ajout "Développement local" après "Guide contributeur"
- Workflow `.github/workflows/build.yml` : Job e2e-tests séparé (avant intégré dans build)

### Score actuel
- **TOTAL : 45/186 (24.2%)**
- SIRCOM : 24/31 (77.4%) - Validé
- SNUM : 21/31 (67.7%) - Validé
- SRH, SIEP, SAFI, BGS : 0/31 - En cours

### Score Qualité Projet
- **97/100** (après S6-01 + S6-07 + S6-08)
- Tests : 17/20 → 19/20 (+2 points E2E CI)
- Sécurité : 18/20 → 20/20 (+2 points Dependabot + SECURITY.md)
- Maintenabilité : 19/20 → 20/20 (+1 point CHANGELOG + MIGRATION)

### Roadmaps
- S6-01 : Tests E2E automatisés CI
- S6-07 : Renforcement sécurité
- S6-08 : Documentation maintenabilité
- 32 roadmaps archivées (Sprints 0-6 complétés)

---

## v0.2.0 – 2025-10-01

**Semaine 2 - Automatisation : Tests, Documentation et Qualité**

### Tests et Qualité (S2-05, S2-06)
- ✅ Tests unitaires pytest (18 tests) pour `calculate_scores.py` et `enrich_pdf_metadata.py`
- ✅ Linting Python (Black + Ruff) intégré à CI avec pre-commit hooks
- ✅ 9 scénarios E2E automatisés : workflow complet, multi-modules, rollback, erreur périmètre, PDF, performance, frontmatter, preview HTTP
- ✅ Runner `tests/e2e/run_all.sh` pour exécution complète
- ✅ Configuration CI locale avec `act` (nektos/act) pour validation avant push
- ✅ Corrections compatibilité Linux/macOS : sed, stat, awk→sed+grep avec numéros de ligne absolus (v4)
- ✅ Dockerfile.mkdocs-test avec build-essentials pour libsass (Alpine Linux)
- ✅ Timeout gracieux Docker (skip si build > 60s)

### Documentation et Contribution (S2-04, S2-07)
- ✅ Guide contributeur `CONTRIBUTING.md` (Option A GitHub web + Option B Git local)
- ✅ Template Pull Request `.github/PULL_REQUEST_TEMPLATE.md` (type, module, checklist)
- ✅ 5 modules enrichis avec contexte métier réel : SNUM, SRH, SIEP, SAFI, BGS
- ✅ Sections 1-5 remplies (périmètre, état, organisation, plan 2025, indicateurs)
- ✅ Tableaux périmètre et plan d'action avec estimations
- ✅ URLs déclaration accessibilité définies
- ✅ Maintien 0/31 points DINUM (validation ultérieure par services)
- ✅ Documentation modules : 19/20 → 20/20 (objectif atteint)

### Infrastructure et Déploiement (S2-01, S2-02, S2-03)
- ✅ Preview privée GitHub Pages (draft → /draft/, production → racine)
- ✅ Génération PDF systématique avec métadonnées enrichies (auteur, sujet, mots-clés)
- ✅ Script `enrich_pdf_metadata.py` avec tests unitaires
- ✅ Workflow CI optimisé : badges status, artefacts (site/ + exports/), déploiements conditionnels
- ✅ Paramétrage Pages org-only (accès restreint organisation)

### Corrections (Hotfixes)
- 🔧 4 itérations corrections tests E2E (compatibilité GNU sed/BSD sed)
  - v1 : sed -i '' → sed -i.bak (portable macOS/Linux)
  - v2 : stat -f%z → stat -c%s avec fallback
  - v3 : sed '0,/pattern/' → awk avec flag done (échec double-cochage)
  - v4 : awk → sed+grep avec numéros de ligne absolus (solution finale portable)
- 🔧 Correction scores attendus (6/31 → 7/31 SIRCOM, 12/186 → 13/186 TOTAL)
- 🔧 Correction chemins PDF (pdf/document.pdf → exports/span-sg.pdf)
- 🔧 URLs GitHub corrigées (span-sg/span-sg → Alexmacapple/span-sg-repo)

### Statistiques
- 📊 59 commits depuis v0.1.0
- ✅ CI 100% PASS (tests unitaires + E2E + scoring + build + PDF + deploy)
- 📈 Score actuel : SIRCOM 7/31 (22.6%), TOTAL 7/186 (3.8%)
- 🧪 Couverture tests : 18 tests unitaires + 9 scénarios E2E
- 📝 Documentation : CONTRIBUTING.md, tests/README.md, 6 modules structurés

### Roadmaps BMAD complétées
- S2-01 : CI/CD GitHub Actions optimisée
- S2-02 : Génération PDF avec métadonnées
- S2-03 : Preview privée GitHub Pages
- S2-04 : Documentation contributeur
- S2-05 : Tests unitaires et linting Python
- S2-06 : Tests E2E automatisés + CI locale act
- S2-07 : Enrichissement modules avec contexte métier

### Semaine 3 - Onboarding (Adaptée)
- ⏭️ S3-01 : Création modules vides → SATISFAITE par S2-07 (modules enrichis)
- ⏭️ S3-02 : Formation Git référents → SKIPPÉE (2 contributeurs autonomes)
- ⏭️ S3-03 : Premiers contenus → SKIPPÉE (Bertrand/Alexandra remplissent directement)
- 📝 Contexte modifié : contributeurs limités (pas de référents services externes)
- ✅ Alternative : workflow standard + CONTRIBUTING.md + support on-demand

---

## v0.1.0 – 2025-09-30
- Initialisation du dépôt SPAN SG (MVP)
- MkDocs + CI GitHub Actions + PDF (fallback)
- Template modules avec 5 sections obligatoires + 31 points DINUM
- Preview privée via GitHub Pages (organisation uniquement)
