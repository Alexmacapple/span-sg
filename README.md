# SPAN SG

Schéma Pluriannuel d'Accessibilité Numérique du Secrétariat Général

Framework modulaire pour la gestion collaborative des schémas d'accessibilité numérique des services du SG, avec scoring automatique sur les 33 critères DINUM et export PDF accessible.

---

![Build Status](https://github.com/Alexmacapple/span-sg/workflows/Build%20SPAN/badge.svg)
![E2E Tests](https://github.com/Alexmacapple/span-sg/actions/workflows/build.yml/badge.svg?event=push)
![Coverage](https://img.shields.io/badge/coverage-89%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Release](https://img.shields.io/github/v/release/Alexmacapple/span-sg)
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)

---

## À propos

La loi n° 2005-102 du 11 février 2005 rend obligatoire l'accessibilité de tout service de communication publique en ligne à tous les citoyens, y compris les personnes en situation de handicap. Le Référentiel Général d'Amélioration de l'Accessibilité (RGAA) fixe 33 critères de conformité.

Ce projet fournit un framework technique permettant aux services du Secrétariat Général de :

- Éditer de manière décentralisée leur Schéma Pluriannuel d'Accessibilité Numérique
- Bénéficier d'un scoring automatisé sur les 33 critères officiels DINUM
- Générer automatiquement un site web et un PDF accessible conforme au Système de Design de l'État (DSFR)
- Suivre l'évolution de leur conformité RGAA avec versioning Git

Le projet couvre 6 modules correspondant aux services du SG : SNUM, SIRCOM, SRH, SIEP, SAFI, BGS.

## Fonctionnalités principales

- **Édition collaborative** : Chaque service édite son module indépendamment
- **Scoring automatique** : Calcul en temps réel du taux de conformité (0/33, 31/33 ou 33/33 points)
- **Export PDF accessible** : Génération automatique avec métadonnées RGAA (titre, langue, keywords)
- **Thème DSFR** : Conformité au Système de Design de l'État (composants, header/footer Marianne)
- **CI/CD automatisée** : Tests E2E, linting, sécurité, déploiement staging/production
- **Sécurité intégrée** : Dependabot, Gitleaks, Bandit, Safety (scan CVE hebdomadaire)
- **Architecture Decision Records** : Traçabilité des décisions techniques majeures (10 ADR)

## Démarrage rapide

### Prérequis

- Docker Desktop : [Installation](https://www.docker.com/products/docker-desktop)
- Git (préinstallé sur macOS/Linux)

Vérification :
```bash
docker --version && docker compose version
```

### Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/Alexmacapple/span-sg.git
cd span-sg

# 2. Démarrer le serveur avec Docker (thème DSFR)
docker compose -f docker-compose-dsfr.yml up -d

# 3. Accéder au site
# http://localhost:8000/span-sg/
```

Le site est généré avec hot-reload automatique : toute modification dans `docs/` reconstruit le site en temps réel.

**Pour aller plus loin** : Consultez [HOWTO.md](HOWTO.md) pour l'installation détaillée, les commandes avancées, le troubleshooting et la génération PDF.

## Documentation

Le projet dispose d'une documentation technique complète :

- **[HOWTO.md](HOWTO.md)** : Installation, commandes utiles, troubleshooting Docker, génération PDF
- **[CONTRIBUTING.md](CONTRIBUTING.md)** : Guide contributeur, workflow Git, processus release automatisé
- **[CHANGELOG.md](CHANGELOG.md)** : Historique des versions et évolutions du projet
- **[SECURITY.md](SECURITY.md)** : Politique de sécurité, mesures actives, signalement vulnérabilités
- **[MIGRATION.md](MIGRATION.md)** : Guides de migration entre versions majeures
- **[docs/adr/](docs/adr/)** : Architecture Decision Records (10 ADR documentant les choix techniques)
- **[docs/dev/api-reference.md](docs/dev/api-reference.md)** : Documentation des scripts Python et hooks MkDocs
- **[docs/dev/hooks-guide.md](docs/dev/hooks-guide.md)** : Guide développeur pour création de hooks personnalisés
- **[docs/dev/dsfr-components-guide.md](docs/dev/dsfr-components-guide.md)** : Utilisation composants DSFR (Cards, Alerts, Grid, etc.)

## Architecture

### Stack technique

- **Générateur** : MkDocs 1.6+ avec plugin mkdocs-dsfr 0.17+
- **Langage** : Python 3.11+
- **Thème** : Système de Design de l'État (DSFR) - Conformité circulaire n°6411-SG du 7 juillet 2023
- **Export PDF** : mkdocs-with-pdf + WeasyPrint + pikepdf (enrichissement métadonnées)
- **CI/CD** : GitHub Actions (build, test, deploy staging/production)

### Structure modulaire

```
docs/
├── index.md                 # Page d'accueil
├── synthese.md              # Tableau de bord agrégé (généré automatiquement)
└── modules/
    ├── _template.md         # Template avec 33 critères DINUM
    ├── snum.md              # Service du Numérique
    ├── sircom.md            # Service de la Communication
    ├── srh.md               # Service des Ressources Humaines
    ├── siep.md              # Service des Infrastructures et de l'Environnement Professionnel
    ├── safi.md              # Service des Affaires Financières
    └── bgs.md               # Bureau de la Gestion des Services
```

Chaque module contient :
- Front-matter YAML (service, referent, updated)
- 5 sections obligatoires (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- 33 points de contrôle DINUM balisés `<!-- CHECKLIST -->`

### Pipeline de scoring automatisé

Le script `scripts/calculate_scores.py` :

1. Scanne tous les modules dans `docs/modules/*.md`
2. Compte les cases cochées `[x]` portant la balise `<!-- CHECKLIST -->`
3. Valide que chaque module a exactement 0 ou 33 points (fail si autre valeur)
4. Génère `docs/synthese.md` avec tableau agrégé par module
5. Calcule le score global SG (somme des 6 modules)

### Hooks Python DSFR

Deux hooks améliorent l'accessibilité et le rendu DSFR :

- `hooks/dsfr_table_wrapper.py` : Encapsule les tableaux Markdown dans `<div class="fr-table">` pour le responsive
- `hooks/title_cleaner.py` : Nettoie les titres HTML redondants (post-processing regex)

## Environnements

Le projet utilise 3 environnements de déploiement :

### Local (développement)
- **URL** : http://localhost:8000/span-sg/
- **Commande** : `docker compose -f docker-compose-dsfr.yml up -d`
- **Usage** : Développement avec hot-reload, tests modifications avant commit

### Staging (préproduction)
- **URL** : https://alexmacapple.github.io/span-sg/draft/
- **Déploiement** : Auto-deploy à chaque push sur `main`
- **Usage** : Revue validateurs avant production, accessible organisation uniquement

### Production
- **URL** : https://alexmacapple.github.io/span-sg/
- **Déploiement** : Nécessite approval manuel du Chef SNUM (GitHub Environment)
- **Usage** : Version stable validée, accessible organisation uniquement

### PDF
- **Releases** : https://github.com/Alexmacapple/span-sg/releases
- **Téléchargement** : `./scripts/download_latest_pdf.sh main`
- **Génération locale** : `ENABLE_PDF_EXPORT=1 mkdocs build --config-file mkdocs-dsfr-pdf.yml`

Documentation complète de l'architecture déploiement : [ADR-009](docs/adr/009-migration-github-environments.md)

## Contribution

### Workflow

1. Créer une branche feature : `git checkout -b feature/update-[service]`
2. Modifier les modules dans `docs/modules/[service].md`
3. Créer une Pull Request vers `main`
4. Validation par Alexandra (code review)
5. Merge → Auto-deploy staging (/draft/)
6. Approval Alexandra → Deploy production (/)

### Règles de modification

**Autorisé :**
- Cocher/décocher les cases `[x]` des 33 points CHECKLIST
- Compléter les 5 sections obligatoires des modules
- Mettre à jour le front-matter YAML (dates, référents)
- Ajouter des actions au plan d'action annuel

**Interdit :**
- Modifier la logique de scoring (33 points balisés `<!-- CHECKLIST -->`)
- Ajouter/supprimer des balises `<!-- CHECKLIST -->`
- Modifier le périmètre v1 (6 modules SG)
- Désactiver `strict: true` dans mkdocs-dsfr.yml

**Documentation complète** : Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour le guide détaillé, les conventions de commit et le processus release.

Pour toute question de sécurité, consultez [SECURITY.md](SECURITY.md).

## Contact

Alexandra : alexandra.guiderdoni@gmail.com
