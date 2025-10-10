# Guide d'installation - SPAN SG

Ce guide vous explique comment installer et démarrer le projet de documentation SPAN SG sur votre machine locale.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Docker Desktop** : [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- **Git** (normalement préinstallé sur macOS/Linux)

Pour vérifier que Docker est installé, exécutez :
```bash
docker --version
docker compose version
```

## Installation rapide

### 1. Cloner le dépôt

Ouvrez un terminal et exécutez :

```bash
# Cloner dans le répertoire de votre choix
git clone https://github.com/Alexmacapple/span-sg-repo.git

# Entrer dans le répertoire
cd span-sg-repo
```

### 2. Démarrer le projet

```bash
docker compose up -d
```

Cette commande va :
- Construire l'image Docker avec toutes les dépendances nécessaires (MkDocs, plugins PDF, etc.)
- Démarrer le conteneur en arrière-plan
- Exposer le serveur sur le port 8000

**Durée estimée** : 2-3 minutes lors de la première installation (téléchargement et compilation des dépendances).

### 3. Accéder à la documentation

Ouvrez votre navigateur et accédez à :

**http://localhost:8000/span-sg-repo/**

Vous devriez voir le site de documentation SPAN SG.

## Installation réussie

Une fois l'installation terminée, vous devriez avoir :

**Résumé de l'installation :**
1. Dépôt cloné localement
2. Image Docker construite avec toutes les dépendances (gcc, g++, musl-dev, libffi-dev, MkDocs, plugins)
3. Conteneur `span-sg-repo-mkdocs-1` en cours d'exécution

**Statut actuel :**
- Conteneur : `span-sg-repo-mkdocs-1` (actif)
- Port mappé : `0.0.0.0:8000->8000/tcp`
- URL d'accès : **http://localhost:8000/span-sg-repo/**

## Commandes utiles

### Gestion du conteneur

```bash
# Arrêter le conteneur
docker compose down

# Redémarrer le conteneur
docker compose up -d

# Voir les logs en temps réel
docker compose logs -f

# Reconstruire l'image (après modification du Dockerfile ou requirements.txt)
docker compose up -d --build

# Vérifier le statut du conteneur
docker ps --filter "name=span-sg-repo"
```

### Développement

```bash
# Calculer les scores SPAN et générer docs/synthese.md
docker compose exec mkdocs python scripts/calculate_scores.py

# Générer le site HTML statique
docker compose exec mkdocs mkdocs build

# Générer le PDF
docker compose exec mkdocs mkdocs build --config-file mkdocs-pdf.yml
```

## Installation alternative (sans Docker)

Si vous préférez ne pas utiliser Docker, vous pouvez installer MkDocs directement :

```bash
# Prérequis : Python 3.11+ et pip
python3 --version

# Installer les dépendances
pip install -r requirements.txt

# Démarrer le serveur local
mkdocs serve

# Accéder à : http://localhost:8000
```

**Note** : Sur macOS avec processeur Apple Silicon (M1/M2/M3), vous devrez peut-être installer des outils de compilation :
```bash
xcode-select --install
```

## Résolution des problèmes

### Erreur "port 8000 already in use"

Si le port 8000 est déjà utilisé par un autre service :

1. Arrêter l'autre service utilisant le port 8000, ou
2. Modifier le port dans `docker-compose.yml` :
   ```yaml
   ports:
     - "8080:8000"  # Utiliser le port 8080 au lieu de 8000
   ```
   Puis accéder à http://localhost:8080/span-sg-repo/

### Erreur de build Docker (libsass)

Si vous obtenez une erreur lors de la compilation de `libsass`, assurez-vous que le Dockerfile contient bien :

```dockerfile
RUN apk add --no-cache gcc musl-dev g++ libffi-dev
```

Cette ligne doit se trouver **avant** l'installation des dépendances Python.

### Conteneur qui redémarre en boucle

Vérifiez les logs pour identifier le problème :
```bash
docker compose logs -f
```

Souvent causé par une erreur dans `mkdocs.yml` ou un lien cassé (mode strict activé).

### Docker Desktop n'est pas installé

Téléchargez et installez Docker Desktop depuis :
- macOS : [https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)
- Windows : [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)
- Linux : [https://docs.docker.com/desktop/install/linux-install/](https://docs.docker.com/desktop/install/linux-install/)

## Workflow Git recommandé

Pour contribuer au projet :

```bash
# Créer une branche feature
git checkout -b feature/update-module-name

# Faire vos modifications
# ...

# Commiter les changements
git add .
git commit -m "feat(module): description des modifications"

# Pousser la branche
git push -u origin feature/update-module-name

# Créer une Pull Request vers la branche 'draft'
```

## Structure du projet

```
span-sg-repo/
├── docs/                    # Documentation MkDocs
│   ├── modules/            # Modules SPAN SG (SNUM, SIRCOM, etc.)
│   ├── index.md            # Page d'accueil
│   └── synthese.md         # Synthèse des scores (généré automatiquement)
├── scripts/                # Scripts Python (calcul des scores)
├── .github/workflows/      # CI/CD GitHub Actions
├── mkdocs.yml             # Configuration MkDocs principale
├── mkdocs-pdf.yml         # Configuration pour génération PDF
├── Dockerfile             # Configuration Docker
├── docker-compose.yml     # Orchestration Docker
├── requirements.txt       # Dépendances Python
├── README.md              # Documentation principale
└── HOWTO.md              # Ce fichier
```

## Support

Pour toute question ou problème :

1. Consultez le fichier `CLAUDE.md` pour les détails techniques
2. Vérifiez le `README.md` pour les informations générales
3. Consultez les issues GitHub : [https://github.com/Alexmacapple/span-sg-repo/issues](https://github.com/Alexmacapple/span-sg-repo/issues)

## Références

- Documentation MkDocs : [https://www.mkdocs.org/](https://www.mkdocs.org/)
- Thème Material : [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- Docker Desktop : [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
