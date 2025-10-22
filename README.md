# SPAN SG – Repo

![Build Status](https://github.com/Alexmacapple/span-sg/workflows/Build%20SPAN/badge.svg)
![E2E Tests](https://github.com/Alexmacapple/span-sg/actions/workflows/build.yml/badge.svg?event=push)
![Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Release](https://img.shields.io/github/v/release/Alexmacapple/span-sg)
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)

Ce dépôt contient le SPAN SG (MkDocs), les modules services et la CI de build/deploy.

## État actuel du projet (22/10/2025)

**Version** : v1.0.1-dsfr - Migration thème DSFR complète + Architecture GitHub Environments

- **Infrastructure** : Production-ready (CI/CD, tests E2E automatisés, sécurité renforcée)
- **Architecture** : 1 branche (main) + 2 Environments (staging, production) avec approval gates
- **2 modules validés** : SIRCOM (24/31 - 77.4%), SNUM (21/31 - 67.7%)
- **4 modules optionnels** : BGS, SAFI, SIEP, SRH (structure créée, enrichissement progressif)
- **Roadmaps** : 32 archivées (Sprints 0-6), 5 actives (modules optionnels)
- **Prochaine étape** : Complétion modules optionnels (POC-FINALISATION terminé)

## Liens utiles

- **Local** : http://localhost:8000/span-sg/ (développement, hot-reload)
- **Staging** : https://alexmacapple.github.io/span-sg/draft/ (preview auto-deploy depuis main)
- **Production** : https://alexmacapple.github.io/span-sg/ (nécessite approval Chef SNUM)
- **PDF production** : https://github.com/Alexmacapple/span-sg/releases/latest
- **Changelog** : [CHANGELOG.md](CHANGELOG.md) - Historique versions
- **Migration** : [MIGRATION.md](MIGRATION.md) - Guides upgrade path

**Architecture déploiement** : Voir [ADR-009](docs/adr/009-migration-github-environments.md) et [Guide Chef SNUM](docs/guide-chef-snum-approvals.md)

## Architecture et Documentation

Documentation technique complète du projet :

- **API Reference** : [docs/dev/api-reference.md](docs/dev/api-reference.md) - Documentation scripts Python et hooks MkDocs
- **Guide Hooks** : [docs/dev/hooks-guide.md](docs/dev/hooks-guide.md) - Guide développeur création hooks MkDocs
- **Guide Composants DSFR** : [docs/dev/dsfr-components-guide.md](docs/dev/dsfr-components-guide.md) - Utilisation Cards, Callouts, Badges, Alerts, Grid (8 sections, 12+ exemples)
- **ADR (Architecture Decision Records)** : [docs/adr/](docs/adr/) - Décisions techniques majeures (DSFR, PDF, hooks, coverage)
- **Diagrammes Architecture** : [docs/architecture/diagrams.md](docs/architecture/diagrams.md) - 6 diagrammes Mermaid (CI/CD, composants, Git, hooks)

## Thème DSFR (Système de Design de l'État)

Le projet utilise le thème [mkdocs-dsfr](https://pypi.org/project/mkdocs-dsfr/) (v0.17.0) pour garantir la conformité avec le design gouvernemental français.

### Caractéristiques DSFR
- Header/footer officiels avec Marianne
- Composants accessibles (fr-summary, fr-grid, fr-button)
- Navigation RGAA conforme
- Hooks Python pour tableaux responsifs et titres optimisés

### Configuration
- **Docker** : `docker-compose-dsfr.yml`
- **Config principale** : `mkdocs-dsfr.yml`
- **Config PDF** : `mkdocs-dsfr-pdf.yml`
- **Hooks** : `hooks/dsfr_table_wrapper.py`, `hooks/title_cleaner.py`

## Démarrage rapide

### Installation en 3 étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/Alexmacapple/span-sg.git
cd span-sg

# 2. Démarrer avec Docker (thème DSFR)
docker compose -f docker-compose-dsfr.yml up -d

# 3. Accéder au site
# http://localhost:8000/span-sg/
```

**Guide complet** : Consultez [HOWTO.md](HOWTO.md) pour les instructions détaillées, la résolution de problèmes et les commandes utiles.

### Prérequis

- **Docker Desktop** : [Installation](https://www.docker.com/products/docker-desktop)
- **Git** (normalement préinstallé sur macOS/Linux)

Vérification :
```bash
docker --version && docker compose version
```

## Sprint 6 Tech First - Terminé (Score 97/100)

**Infrastructure production-ready** :
1. [COMPLETE] Tests E2E automatisés CI (S6-01) - Job GitHub Actions + reporting HTML
2. [COMPLETE] Renforcement sécurité (S6-07) - Dependabot + SECURITY.md + guide BFG
3. [COMPLETE] Documentation maintenabilité (S6-08) - CHANGELOG + MIGRATION + versioning

**Roadmaps organisées** :
- 32 roadmaps archivées (Sprints 0-6 terminés)
- Structure unifiée `roadmap/archive/`
- ROADMAP-INDEX.md créé (master index)

**Prochaines étapes** :
1. **Modules optionnels** (P1) : Compléter BGS, SAFI, SIEP, SRH (S6-03 à S6-06)
2. **Infrastructure optionnelle** (P3) : Notifications CI + Rollback (S6-02)
3. **Release v1.1.0** : Documentation GitHub Environments complète + modules enrichis

## Commandes utiles

**Pour un guide complet, consultez [HOWTO.md](HOWTO.md)**

### Développement local
```bash
# Démarrer le serveur (en arrière-plan)
docker compose up -d

# Voir les logs en temps réel
docker compose logs -f mkdocs

# Arrêter le serveur
docker compose down

# Redémarrer après modifications
docker compose restart

# Reconstruire après modification du Dockerfile
docker compose up -d --build
```

**URL du site** : http://localhost:8000/span-sg/

### Autres commandes
```bash
# Build manuel du site HTML
mkdocs build

# Build manuel du PDF avec enrichissement metadata
mkdocs build --config-file mkdocs-pdf.yml
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf

# Calcul des scores SPAN et génération synthèse
python scripts/calculate_scores.py

# Test complet du workflow PDF
./scripts/test_pdf_workflow.sh

# Script de développement
./scripts/start-dev-server.sh  # Lance Docker avec vérifications
```

## Export PDF

Le site est exportable en PDF avec métadonnées accessibilité (RGAA).

### Téléchargement

**Depuis le site web** :
- Staging : https://alexmacapple.github.io/span-sg/draft/ (bouton "Télécharger PDF")
- Production : https://alexmacapple.github.io/span-sg/ (bouton "Télécharger PDF")

**Depuis GitHub Actions** :
```bash
./scripts/download_latest_pdf.sh main
```

### Génération locale

**Prérequis** : Dépendances système WeasyPrint

**macOS (Homebrew)** :
```bash
brew install pango cairo gdk-pixbuf libffi
```

**Ubuntu/Debian** :
```bash
sudo apt-get install libpango-1.0-0 libcairo2 libgdk-pixbuf2.0-0
```

**Build** :
```bash
ENABLE_PDF_EXPORT=1 mkdocs build --config-file mkdocs-dsfr-pdf.yml
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
```

**Output** : `exports/span-sg.pdf` (environ 2.6 MB, PDF 1.7, accessible)

### Métadonnées

Le PDF contient :
- Titre : SPAN SG
- Langue : fr-FR
- Auteur : Secrétariat Général
- Subject : Schéma Pluriannuel d'Accessibilité Numérique
- Keywords : SPAN, accessibilité, SG, numérique, RGAA, DINUM

## Développement local avec Docker

### Architecture Docker

Le projet utilise 2 fichiers Docker complémentaires :

**`Dockerfile`** (la recette de l'image)
```dockerfile
FROM squidfunk/mkdocs-material:latest  # Image de base MkDocs Material
WORKDIR /docs                          # Répertoire de travail
EXPOSE 8000                            # Port exposé
CMD ["serve", "--dev-addr=0.0.0.0:8000"]  # Commande au démarrage
```

**Rôle** : Définit comment construire l'image Docker (le modèle du conteneur).

**`docker-compose.yml`** (la configuration de lancement)
```yaml
services:
  mkdocs:
    build: .              # Construire avec le Dockerfile du répertoire actuel
    volumes:
      - .:/docs           # Partager le dossier actuel avec le conteneur
    ports:
      - "8000:8000"       # Exposer le port 8000 sur l'hôte
```

**Rôle** : Définit comment lancer le conteneur (volumes, ports, configuration).

### Workflow de développement

1. **Lancer le serveur** : `docker compose up -d`
   - Docker lit `docker-compose.yml`
   - Si l'image n'existe pas, la construit avec `Dockerfile`
   - Démarre le conteneur en arrière-plan (`-d`)
   - Monte le répertoire actuel dans `/docs` (hot-reload automatique)

2. **Modifier le code** : Éditer les fichiers dans `docs/`
   - MkDocs détecte automatiquement les changements
   - Le site se reconstruit en temps réel
   - Rafraîchir le navigateur pour voir les modifications

3. **Arrêter le serveur** : `docker compose down`

### Troubleshooting Docker

**Erreur : "Cannot connect to Docker daemon"**
```bash
# Cause : Docker Desktop n'est pas démarré
# Solution : Lancer Docker Desktop et attendre qu'il soit prêt
docker ps  # Vérifier que Docker répond
```

**Erreur : "Port 8000 already in use"**
```bash
# Cause : Un autre processus utilise le port 8000
# Solution : Trouver et arrêter le processus
lsof -i :8000
kill <PID>

# Ou changer le port dans docker-compose.yml
ports:
  - "8001:8000"  # Utiliser 8001 au lieu de 8000
```

**Site inaccessible après `docker compose up`**
```bash
# Vérifier que le conteneur tourne
docker compose ps

# Voir les logs pour identifier l'erreur
docker compose logs mkdocs

# Problèmes courants :
# - Erreur dans mkdocs.yml : corriger la config
# - Plugin manquant : installer les dépendances
```

**Premier lancement très long**
- Normal : Docker télécharge l'image de base (~200MB)
- Les lancements suivants sont instantanés (image en cache)

### Notes techniques

- **Dépendances Python** : Toutes les dépendances sont centralisées dans `requirements.txt`. Pour développer en local sans Docker :
  ```bash
  pip install -r requirements.txt
  mkdocs serve
  ```

- **Plugin PDF** : Le projet utilise `mkdocs-with-pdf` (meilleur support que `mkdocs-pdf-export-plugin`). L'enrichissement automatique des metadata (titre, langue, keywords) est assuré par `scripts/enrich_pdf_metadata.py`.

- **Hot-reload automatique** : Le volume monté (`- .:/docs`) synchronise le répertoire local avec le conteneur. Toute modification est détectée instantanément par MkDocs.

## Dépannage rapide
- **PDF manquant** : Utiliser l'impression navigateur sur « Synthèse » (Cmd+P / Ctrl+P) ou vérifier que `exports/span-sg.pdf` existe après `mkdocs build --config-file mkdocs-pdf.yml`
- **Metadata PDF absentes** : Exécuter `python scripts/enrich_pdf_metadata.py exports/span-sg.pdf` (nécessite `pikepdf`)
- **Scores incohérents** : S'assurer que seuls les 31 points portent `<!-- DINUM -->`
- **Staging non mis à jour** : Vérifier que le push est sur `main` (auto-deploy vers /draft/)
- **Production non mise à jour** : Vérifier approval Chef SNUM (Dashboard Deployments)
- **Docker ne démarre pas** : Vérifier que Docker Desktop est lancé et fonctionnel (`docker ps`)
- **Dépendances manquantes** : Installer avec `pip install -r requirements.txt`

## Sécurité

Pour signaler une vulnérabilité, consultez [SECURITY.md](SECURITY.md).

**Ne créez PAS d'issue publique pour les vulnérabilités.**

### Mesures de Sécurité

- **Dependabot** : Scan automatique hebdomadaire (vulnérabilités CVE)
- **Security alerts** : Notifications activées
- **Git history** : Nettoyé (fichiers sensibles purgés)
- **CI/CD** : Validation automatique (linter, tests)

## Contribution

Pour contribuer au projet, consulter le [Guide contributeur](CONTRIBUTING.md).

## Contacts
- Owner: Alexandra (@alexandra)
- Validateurs: Bertrand (@bertrand), Alex (@alex)
- Sponsor: Stéphane (Chef mission numérique SNUM-SG)


## règles de validation
- Validation de contenu: Bertrand et Alex
- Stéphane (Chef mission numérique SNUM-SG): validation conceptuelle
- Chef SNUM: validation finale GO production


## Preview GitHub Pages (note)
- Ce dépôt public n’active pas Pages pour la preview avant validation.
- Pour un déploiement Pages privé, voir `.github/PAGES-ACCESS-CHECKLIST.md` (nécessite organisation/Enterprise).


## Checklist GO
- Voir `GO-CHECKLIST.md` pour valider Pages org-only, URLs légales, variables `site_url`/`repo_url`, exécution CI initiale, et gouvernance des accès.
- Voir `.github/PAGES-ACCESS-CHECKLIST.md` pour le détail du paramétrage Pages (organisation uniquement).



## Vibe coding
- Utiliser `Agents.md` (Codex/Cursor/Builder.io) pour les instructions d’agent standardisées
- Utiliser `Claude.md` pour Claude Code (format spécifique Anthropic)
- Conserver le périmètre MVP, ne pas modifier la logique des 31 points DINUM

## Preview et revue

Le projet utilise 3 environnements de revue :

1. **Local** : `docker compose -f docker-compose-dsfr.yml up` → http://localhost:8000/span-sg/
   - Hot-reload temps réel
   - Tests modifications avant commit

2. **Staging** : https://alexmacapple.github.io/span-sg/draft/
   - Auto-deploy depuis branche `main`
   - Revue validateurs avant production
   - Accessible membres organisation uniquement

3. **Production** : https://alexmacapple.github.io/span-sg/
   - Deploy après approval Chef SNUM
   - Version stable validée
   - Public (organisation uniquement)

**Architecture déploiement** : Voir [ADR-009](docs/adr/009-migration-github-environments.md) pour comprendre le workflow complet.
