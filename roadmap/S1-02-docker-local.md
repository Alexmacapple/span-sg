---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S1-02 : Configuration Docker local pour développement

**Phase** : Semaine 1 - Setup
**Priorité** : Haute
**Estimation** : 30min
**Assigné** : Alexandra

---

## Contexte projet

Le projet SPAN SG nécessite un environnement de développement local pour :
- Prévisualiser les modifications MkDocs en temps réel
- Tester le rendu avant commit
- Travailler sans connexion internet
- Éviter les installations Python complexes

Docker permet d'encapsuler MkDocs + dépendances dans un conteneur isolé, garantissant la reproductibilité de l'environnement entre développeurs.

Le fichier `docker-compose.yml` déjà présent dans le repo configure :
- Build d'un Dockerfile custom basé sur MkDocs Material
- Plugin PDF intégré (mkdocs-pdf-export-plugin)
- Volumes pour hot-reload automatique
- Port 8000 exposé pour accès navigateur
- Configuration service `mkdocs`

Le `Dockerfile` étend l'image officielle `squidfunk/mkdocs-material` avec le plugin PDF nécessaire pour la génération des exports documentaires (voir `mkdocs-pdf.yml`).

---

## Objectif

Vérifier et démarrer l'environnement Docker local pour le développement MkDocs, garantir que le site s'affiche sur http://localhost:8000/span-sg-repo/ avec hot-reload fonctionnel.

---

## Prérequis

- [ ] Docker Desktop installé et démarré
- [ ] Story S1-01 complétée (repo cloné localement)
- [ ] Terminal ouvert dans le répertoire du projet

---

## Étapes d'implémentation

### 1. Vérifier Docker

```bash
# Vérifier que Docker est installé et actif
docker --version
# Attendu : Docker version 20.x ou supérieur

docker-compose --version
# Attendu : Docker Compose version 2.x ou supérieur
```

Si Docker n'est pas installé :
- Mac : https://docs.docker.com/desktop/install/mac-install/
- Windows : https://docs.docker.com/desktop/install/windows-install/
- Linux : https://docs.docker.com/engine/install/

### 2. Vérifier le fichier docker-compose.yml

```bash
cat docker-compose.yml
```

Contenu attendu :
```yaml
version: '3.8'
services:
  mkdocs:
    build: .  # Dockerfile custom avec plugins PDF
    volumes:
      - .:/docs
    ports:
      - "8000:8000"
```

**Note** : La configuration utilise `build: .` au lieu de `image: squidfunk/mkdocs-material` car le projet nécessite les plugins PDF (`mkdocs-pdf-export-plugin`, `mkdocs-with-pdf`) qui ne sont pas inclus dans l'image officielle. Le Dockerfile custom étend l'image Material et ajoute ces dépendances.

### 3. Vérifier le Dockerfile

```bash
cat Dockerfile
```

Contenu attendu :
```dockerfile
# Dockerfile
FROM squidfunk/mkdocs-material:latest
WORKDIR /docs
RUN pip install mkdocs-pdf-export-plugin mkdocs-with-pdf
EXPOSE 8000
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
```

Ce Dockerfile :
- Part de l'image officielle MkDocs Material
- Installe le plugin PDF (mkdocs-pdf-export-plugin)
- Configure le serveur pour écouter sur toutes les interfaces (0.0.0.0)
- Expose le port 8000 pour accès depuis l'hôte

### 4. Démarrer le serveur MkDocs

```bash
# Depuis la racine du projet
docker compose up

# OU en mode détaché (background)
docker compose up -d
```

Logs attendus :
```
[+] Running 1/0
 ✔ Container span-sg-repo-mkdocs-1  Created
Attaching to mkdocs-1
mkdocs-1  | INFO     -  Building documentation...
mkdocs-1  | INFO     -  Cleaning site directory
mkdocs-1  | INFO     -  Documentation built in 0.45 seconds
mkdocs-1  | INFO     -  [12:34:56] Serving on http://0.0.0.0:8000/
```

### 5. Tester l'accès navigateur

1. Ouvrir navigateur : http://localhost:8000/span-sg-repo/
2. Vérifier :
   - Page d'accueil "SPAN SG" s'affiche
   - Navigation fonctionnelle (Synthèse, Modules, Processus)
   - Theme Material appliqué
   - Recherche disponible

### 6. Tester le hot-reload

1. Garder http://localhost:8000/span-sg-repo/ ouvert
2. Éditer `docs/index.md` :
   ```bash
   echo "\n\n## Test hot-reload" >> docs/index.md
   ```
3. Observer dans les logs Docker :
   ```
   INFO     -  Detected file change, rebuilding...
   INFO     -  Building documentation...
   ```
4. Rafraîchir navigateur → la modification apparaît instantanément
5. Annuler le test :
   ```bash
   git checkout docs/index.md
   ```

### 7. Arrêter le serveur

```bash
# Si lancé en mode interactif : Ctrl+C

# Si lancé en mode détaché
docker compose down
```

---

## Critères d'acceptation

- [ ] `docker compose up` démarre sans erreur
- [ ] http://localhost:8000/span-sg-repo/ affiche le site SPAN SG
- [ ] Navigation fonctionnelle entre toutes les pages
- [ ] Hot-reload détecte les modifications et rebuild automatiquement
- [ ] `docker compose down` arrête proprement le conteneur
- [ ] Aucune erreur MkDocs dans les logs

---

## Tests de validation

```bash
# Test 1 : Vérifier que le conteneur tourne
docker compose ps
# Attendu : span-sg-repo-mkdocs-1 Up

# Test 2 : Vérifier les logs
docker compose logs mkdocs
# Attendu : "Serving on http://0.0.0.0:8000/"

# Test 3 : Test HTTP
curl -s http://localhost:8000/span-sg-repo/ | grep "SPAN SG"
# Attendu : Sortie HTML contenant "SPAN SG"

# Test 4 : Arrêt propre
docker compose down
# Attendu : "Container span-sg-repo-mkdocs-1 Stopped"
```

---

## Dépendances

**Bloque** :
- S1-03 (nécessite serveur local pour tester strict mode)
- S1-04 (édition template nécessite preview locale)

**Dépend de** :
- S1-01 (repo doit exister localement)

---

## Références

- **README.md** : Section "Commandes utiles" → Dev local
- **docker-compose.yml** : Configuration service MkDocs
- **CLAUDE.md** : Section "Commandes essentielles" → Développement local

---

## Messages d'erreur courants

### Erreur 1 : Cannot connect to Docker daemon

**Message** :
```
ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
Is the docker daemon running?
```

**Cause** : Docker Desktop n'est pas démarré

**Solution** :
```bash
# macOS/Windows : Démarrer Docker Desktop depuis Applications
# Linux : Démarrer le service Docker
sudo systemctl start docker

# Vérifier que Docker tourne
docker ps
# Attendu : Liste des conteneurs (vide ou avec conteneurs)
```

### Erreur 2 : Port 8000 déjà utilisé

**Message** :
```
Error starting userland proxy: listen tcp4 0.0.0.0:8000: bind: address already in use
```

**Cause** : Un autre processus utilise le port 8000

**Solution Option A** : Tuer le processus existant
```bash
# Identifier le processus sur port 8000
lsof -i :8000
# OU sur Linux
sudo netstat -nlp | grep 8000

# Tuer le processus (remplacer PID par le numéro affiché)
kill <PID>
```

**Solution Option B** : Changer le port dans `docker-compose.yml`
```yaml
ports:
  - "8001:8000"  # Utiliser 8001 au lieu de 8000
```
Puis accéder à http://localhost:8001

### Erreur 3 : Image pull failed

**Message** :
```
Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled
```

**Cause** : Timeout réseau, proxy, ou limites Docker Hub

**Solution** :
```bash
# Option 1 : Retry avec timeout augmenté
DOCKER_CLIENT_TIMEOUT=300 docker compose up

# Option 2 : Si derrière proxy d'entreprise
# Éditer ~/.docker/config.json et ajouter :
{
  "proxies": {
    "default": {
      "httpProxy": "http://proxy.entreprise:port",
      "httpsProxy": "http://proxy.entreprise:port"
    }
  }
}

# Option 3 : Pull manuel de l'image
docker pull squidfunk/mkdocs-material:latest
```

### Erreur 4 : Permission denied /var/run/docker.sock

**Message** :
```
permission denied while trying to connect to the Docker daemon socket
```

**Cause** : User n'a pas les permissions Docker (Linux uniquement)

**Solution** :
```bash
# Ajouter user au groupe docker
sudo usermod -aG docker $USER

# Redémarrer session (logout/login) OU
newgrp docker

# Vérifier
docker ps
```

### Erreur 5 : Container exits immediately

**Message** :
```
span-sg-repo-mkdocs-1 exited with code 1
```

**Cause** : Erreur dans mkdocs.yml ou fichiers markdown

**Solution** :
```bash
# Voir les logs du conteneur
docker compose logs mkdocs

# Chercher la ligne d'erreur, exemples :
# - "Config file 'mkdocs.yml' does not exist" → mauvais répertoire
# - "Error reading page 'docs/xxx.md'" → fichier markdown invalide
# - "Strict mode: warnings have been elevated to errors" → corriger warnings

# Tester build en local pour debug
docker compose run --rm mkdocs build --strict
```

### Erreur 6 : Hot-reload ne fonctionne pas

**Symptôme** : Modifications dans `docs/` non détectées automatiquement

**Cause** : Problème de montage volume ou OS-specific

**Solution** :
```bash
# Vérifier que volumes sont bien montés
docker compose ps -a
docker inspect span-sg-repo-mkdocs-1 | grep -A 10 Mounts

# macOS : Vérifier Docker Desktop → Settings → Resources → File Sharing
# Le répertoire projet doit être dans les chemins autorisés

# Redémarrer conteneur
docker compose down && docker compose up

# Si problème persiste : forcer rebuild
docker compose up --force-recreate
```

### Erreur 7 : Build errors en mode strict

**Message** :
```
ERROR   -  Error reading page 'docs/modules/sircom.md':
Strict mode: '404.html' not found in docs files.
```

**Cause** : Mode strict MkDocs détecte liens cassés, références invalides

**Solution** :
```bash
# Identifier toutes les erreurs
docker compose logs mkdocs | grep ERROR

# Corriger les fichiers problématiques
# Exemples courants :
# - Lien interne cassé : [texte](page-inexistante.md)
# - Image manquante : ![alt](image-inexistante.png)
# - Navigation vers fichier absent dans mkdocs.yml

# Tester build sans strict pour voir warnings
docker compose run --rm mkdocs build
```

### Erreur 8 : Out of disk space

**Message** :
```
no space left on device
```

**Cause** : Docker images/volumes/containers consomment trop d'espace

**Solution** :
```bash
# Voir l'espace utilisé par Docker
docker system df

# Nettoyer images/containers inutilisés (libère souvent 5-10 GB)
docker system prune -a

# Avec confirmation
# Removing unused containers, networks, images...
# Total reclaimed space: 8.5 GB

# Nettoyer aussi volumes (ATTENTION : perte données)
docker volume prune
```

---

## Notes et risques

**Alternative sans Docker** :
Si Docker pose problème, installation native Python possible :
```bash
pip install mkdocs-material mkdocs-pdf-export-plugin mkdocs-with-pdf
mkdocs serve
```

**Performance Mac M1/M2** :
Image `squidfunk/mkdocs-material` supporte nativement ARM64, pas de configuration supplémentaire nécessaire.