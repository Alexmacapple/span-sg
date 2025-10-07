# SPAN SG – Repo

![Build Status](https://github.com/Alexmacapple/span-sg-repo/workflows/Build%20SPAN/badge.svg)

Ce dépôt contient le SPAN SG (MkDocs), les modules services et la CI de build/deploy.

## État actuel du projet (07/10/2025)

**Version en développement** : Branche `draft` active avec 45/186 points validés (24.2%)

- **2 modules validés** : SIRCOM (24/31 - 77.4%), SNUM (21/31 - 67.7%)
- **4 modules en cours** : SRH, SIEP, SAFI, BGS (structure créée, 0/31)
- **Infrastructure opérationnelle** : CI/CD, tests E2E, preview privée, génération PDF
- **Production** : En attente de validation finale (branche `main` en standby)

## Liens utiles

- **Preview (draft)** : https://alexmacapple.github.io/span-sg-repo/draft/
- **Production** : https://alexmacapple.github.io/span-sg-repo/
- **PDF production** : https://github.com/Alexmacapple/span-sg-repo/releases/latest

## Démarrage rapide

### Prérequis
1. **Installer Docker Desktop**
   - Mac : [docs.docker.com/desktop/install/mac-install](https://docs.docker.com/desktop/install/mac-install/)
   - Windows : [docs.docker.com/desktop/install/windows-install](https://docs.docker.com/desktop/install/windows-install/)
   - Linux : [docs.docker.com/engine/install](https://docs.docker.com/engine/install/)

2. **Installer dépendances système** (optionnel, si vous voulez run scripts localement)

   **macOS** :
   ```bash
   brew install qpdf
   ```

   **Ubuntu/Debian** :
   ```bash
   sudo apt-get install qpdf
   ```

   **Note** : Requis pour le script `enrich_pdf_metadata.py` (métadonnées PDF).
   Docker inclut déjà ces dépendances.

3. **Démarrer Docker Desktop**
   - Ouvrir l'application Docker Desktop
   - Attendre que l'icône dans la barre de menu affiche "Docker Desktop is running"

4. **Vérifier que Docker fonctionne**
   ```bash
   docker --version
   # Attendu : Docker version 20.x ou supérieur

   docker ps
   # Attendu : Liste des conteneurs (vide ou avec conteneurs existants)
   ```

### Installation
1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Alexmacapple/span-sg-repo.git
   cd span-sg-repo
   ```

2. **Créer les branches principales**
   ```bash
   git checkout -b main
   git checkout -b draft
   ```

3. **Configurer les URLs** (si nécessaire)
   - Éditer `mkdocs.yml` : ajuster `site_url` et `repo_url`

### Premier lancement
```bash
# Lancer le serveur de développement
docker compose up -d

# Le premier lancement télécharge l'image Docker (~200MB)
# Cela peut prendre 1-2 minutes
```

**Accéder au site** : http://localhost:8000/span-sg-repo/

**Arrêter le serveur** :
```bash
docker compose down
```

## Prochaines étapes vers v1.0 production

1. **Infrastructure** : CI/CD, tests, preview privée → TERMINÉ
2. **Modules pilotes** : SIRCOM (77.4%), SNUM (67.7%) → VALIDÉS
3. **Modules restants** : Compléter SRH, SIEP, SAFI, BGS (0/31 actuellement)
4. **Validation intermédiaire** : Review Bertrand/Alexandra → EN COURS
5. **Présentation Stéphane** : Validation conceptuelle (roadmap S4-02)
6. **Tag v1.0.0** : Création release après validation finale (roadmap S4-03)
7. **Production** : Merge `draft` → `main` + déploiement (roadmap S4-04)

## Commandes utiles

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
```

**URL du site** : http://localhost:8000/span-sg-repo/

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
./scripts/dev.sh  # Lance Docker avec vérifications
```

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
- **Preview inaccessible** : Vérifier restriction GitHub Pages à l'organisation et branche `gh-pages`
- **Docker ne démarre pas** : Vérifier que Docker Desktop est lancé et fonctionnel (`docker ps`)
- **Dépendances manquantes** : Installer avec `pip install -r requirements.txt`

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


## preview privée (Pages organisation GitHub)
- Restreindre l’accès aux membres de l’organisation dans les paramètres Pages
- Déploiement `draft` vers `gh-pages` sous `draft/`
- Pas d’identifiants génériques; seuls les comptes org sont autorisés


## Checklist GO
- Voir `GO-CHECKLIST.md` pour valider Pages org-only, URLs légales, variables `site_url`/`repo_url`, exécution CI initiale, et gouvernance des accès.
- Voir `.github/PAGES-ACCESS-CHECKLIST.md` pour le détail du paramétrage Pages (organisation uniquement).



## Vibe coding
- Utiliser `Agents.md` (Codex/Cursor/Builder.io) pour les instructions d’agent standardisées
- Utiliser `Claude.md` pour Claude Code (format spécifique Anthropic)
- Conserver le périmètre MVP, ne pas modifier la logique des 31 points DINUM


