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
- Image Python avec MkDocs Material
- Volumes pour hot-reload automatique
- Port 8000 exposé pour accès navigateur
- Configuration service `mkdocs`

---

## Objectif

Vérifier et démarrer l'environnement Docker local pour le développement MkDocs, garantir que le site s'affiche sur http://localhost:8000 avec hot-reload fonctionnel.

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
    image: squidfunk/mkdocs-material
    ports:
      - "8000:8000"
    volumes:
      - ./:/docs
    command: serve --dev-addr=0.0.0.0:8000
```

### 3. Démarrer le serveur MkDocs

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

### 4. Tester l'accès navigateur

1. Ouvrir navigateur : http://localhost:8000
2. Vérifier :
   - Page d'accueil "SPAN SG" s'affiche
   - Navigation fonctionnelle (Synthèse, Modules, Processus)
   - Theme Material appliqué
   - Recherche disponible

### 5. Tester le hot-reload

1. Garder http://localhost:8000 ouvert
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

### 6. Arrêter le serveur

```bash
# Si lancé en mode interactif : Ctrl+C

# Si lancé en mode détaché
docker compose down
```

---

## Critères d'acceptation

- [ ] `docker compose up` démarre sans erreur
- [ ] http://localhost:8000 affiche le site SPAN SG
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
curl -s http://localhost:8000 | grep "SPAN SG"
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

## Notes et risques

**Alternative sans Docker** :
Si Docker pose problème, installation native Python possible :
```bash
pip install mkdocs-material mkdocs-pdf-export-plugin mkdocs-with-pdf
mkdocs serve
```

**Ports occupés** :
Si port 8000 déjà utilisé, modifier dans `docker-compose.yml` :
```yaml
ports:
  - "8001:8000"  # Utiliser 8001 au lieu de 8000
```

**Performance Mac M1/M2** :
Image `squidfunk/mkdocs-material` supporte nativement ARM64, pas de configuration supplémentaire nécessaire.