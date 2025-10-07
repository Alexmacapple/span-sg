---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S0-00 : Validation environnement de développement

**Phase** : Semaine 0 - Prérequis
**Priorité** : Critique (bloquante)
**Estimation** : 30min
**Assigné** : Alexandra

---

## Contexte projet

Avant de démarrer le projet SPAN SG, l'environnement de développement doit être validé pour garantir que toutes les stories suivantes (S1-01 à S4-04) pourront s'exécuter sans blocage technique.

Cette story vérifie la présence et les versions minimales des outils nécessaires :
- **Git** : Versioning et collaboration
- **Docker** : Environnement MkDocs isolé
- **Python 3.11+** : Execution scripts (scoring, etc.)
- **GitHub CLI (optionnel)** : Automatisation repo
- **Éditeur** : VS Code, vim, ou autre

Sans ces prérequis, les stories S1-01 (repo GitHub) et S1-02 (Docker local) échoueront.

---

## Objectif

Vérifier que tous les outils nécessaires sont installés et fonctionnels sur la machine de développement, corriger les manques, et documenter la configuration validée.

---

## Prérequis

- [ ] Machine de développement (macOS, Linux, ou Windows avec WSL)
- [ ] Accès internet
- [ ] Droits administrateur (pour installations)

---

## Étapes d'implémentation

### 1. Vérifier Git

```bash
git --version
# Attendu : git version 2.30.0 ou supérieur
```

**Si absent** :
- **macOS** : `brew install git` (nécessite Homebrew)
- **Linux Debian/Ubuntu** : `sudo apt update && sudo apt install git`
- **Linux Fedora/RHEL** : `sudo dnf install git`
- **Windows** : Installer Git Bash depuis https://git-scm.com/

**Configuration minimale** :
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"

# Vérifier
git config user.name
git config user.email
```

### 2. Vérifier Docker

```bash
docker --version
# Attendu : Docker version 20.10.0 ou supérieur

docker compose version
# Attendu : Docker Compose version v2.0.0 ou supérieur
```

**Si absent** :
- **macOS** : Télécharger Docker Desktop depuis https://www.docker.com/products/docker-desktop/
- **Linux** : Suivre https://docs.docker.com/engine/install/
- **Windows** : Docker Desktop avec WSL2 backend

**Test fonctionnel** :
```bash
# Démarrer Docker Desktop (macOS/Windows)
# Tester pull d'une image
docker run hello-world
# Attendu : "Hello from Docker!" + explications
```

### 3. Vérifier Python

```bash
python3 --version
# Attendu : Python 3.11.0 ou supérieur
```

**Si version < 3.11** :
- **macOS avec Homebrew** : `brew install python@3.11`
- **Linux** : Utiliser pyenv ou ppa
- **Windows** : https://www.python.org/downloads/

**Vérifier pip** :
```bash
pip3 --version
# Attendu : pip 23.0 ou supérieur depuis Python 3.11
```

**Test installation packages** :
```bash
pip3 install --dry-run mkdocs-material
# Attendu : Simule installation sans erreur
```

### 4. Vérifier GitHub CLI (optionnel mais recommandé)

```bash
gh --version
# Attendu : gh version 2.20.0 ou supérieur
```

**Si absent** :
- **macOS** : `brew install gh`
- **Linux Debian/Ubuntu** : https://github.com/cli/cli/blob/trunk/docs/install_linux.md
- **Windows** : `winget install --id GitHub.cli`

**Authentification** :
```bash
gh auth login
# Suivre prompts interactifs
# Choisir : GitHub.com, HTTPS, Login with browser

# Vérifier
gh auth status
# Attendu : Logged in to github.com as [username]
```

**Si gh non disponible** : Workflow manuel possible (S1-01 option manuelle)

### 5. Vérifier éditeur de code

**Options recommandées** :
1. **VS Code** (débutants) : `code --version`
2. **Vim/Neovim** (experts) : `vim --version`
3. **Sublime Text, Atom, etc.**

**Si aucun éditeur** :
- Installer VS Code : https://code.visualstudio.com/
- Extensions recommandées VS Code :
  - Markdown All in One
  - YAML
  - Python

### 6. Vérifier accès réseau GitHub

```bash
# Test connexion HTTPS
curl -I https://github.com
# Attendu : HTTP/2 200

# Test SSH (si utilisé)
ssh -T git@github.com
# Attendu : "Hi [username]! You've successfully authenticated..."
```

**Si erreur proxy/firewall** :
- Configurer proxy Git : `git config --global http.proxy http://proxy:port`
- Ou utiliser HTTPS uniquement

### 7. Créer rapport de validation

```bash
cat > ENV-VALIDATION-REPORT.md << EOF
# Rapport validation environnement SPAN SG

Date : $(date +"%Y-%m-%d %H:%M")
Machine : $(uname -a)

## Outils vérifiés

- [x] Git : $(git --version)
- [x] Docker : $(docker --version)
- [x] Docker Compose : $(docker compose version)
- [x] Python : $(python3 --version)
- [x] pip : $(pip3 --version)
- [$(if command -v gh &> /dev/null; then echo "x"; else echo " "; fi)] GitHub CLI : $(gh --version 2>/dev/null || echo "Non installé (optionnel)")
- [x] Éditeur : $(if command -v code &> /dev/null; then echo "VS Code $(code --version | head -1)"; else echo "Autre"; fi)

## Configuration Git

- user.name : $(git config user.name)
- user.email : $(git config user.email)

## Accès réseau

- [x] GitHub HTTPS accessible
- [$(if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then echo "x"; else echo " "; fi)] GitHub SSH configuré

## Statut

✅ Environnement validé - Prêt pour S1-01

Toutes les dépendances critiques sont installées et fonctionnelles.
EOF

cat ENV-VALIDATION-REPORT.md
```

---

## Critères d'acceptation

- [ ] Git ≥ 2.30 installé et configuré (user.name, user.email)
- [ ] Docker ≥ 20.10 installé et fonctionnel (`docker run hello-world` OK)
- [ ] Docker Compose ≥ v2.0 disponible
- [ ] Python ≥ 3.11 installé
- [ ] pip fonctionnel (test installation package)
- [ ] GitHub CLI installé et authentifié (OU acceptation workflow manuel)
- [ ] Éditeur de code disponible
- [ ] Accès réseau GitHub validé (HTTPS minimum)
- [ ] Rapport `ENV-VALIDATION-REPORT.md` créé

---

## Tests de validation

```bash
# Test 1 : Git présent et configuré
test "$(git config user.name)" && test "$(git config user.email)" && echo "OK" || echo "FAIL"

# Test 2 : Docker fonctionnel
docker run --rm hello-world > /dev/null 2>&1 && echo "OK" || echo "FAIL"

# Test 3 : Python version
python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" && echo "OK" || echo "FAIL"

# Test 4 : pip install test
pip3 install --dry-run pyyaml > /dev/null 2>&1 && echo "OK" || echo "FAIL"

# Test 5 : GitHub accessible
curl -s -o /dev/null -w "%{http_code}" https://github.com | grep -q "200" && echo "OK" || echo "FAIL"

# Test 6 : Rapport créé
test -f ENV-VALIDATION-REPORT.md && echo "OK" || echo "FAIL"
```

---

## Dépendances

**Bloque** :
- S1-01 (repo GitHub nécessite Git + gh CLI)
- S1-02 (Docker local nécessite Docker + docker-compose)
- S1-05 (script scoring nécessite Python 3.11+)
- Toutes les autres stories

**Dépend de** : Aucune (première story absolue)

---

## Références

- **Git** : https://git-scm.com/downloads
- **Docker** : https://docs.docker.com/get-docker/
- **Python** : https://www.python.org/downloads/
- **GitHub CLI** : https://cli.github.com/
- **VS Code** : https://code.visualstudio.com/

---

## Notes et risques

**Versions minimales strictes**
- Python 3.11+ requis (syntaxes modernes dans calculate_scores.py)
- Docker Compose v2+ requis (syntaxe `docker compose` sans tiret)
- Si versions antérieures, adapter les scripts ou upgrader

**Architecture ARM (Apple Silicon M1/M2)**
- Docker Desktop supporte nativement ARM64
- Image MkDocs Material compatible multi-arch
- Pas de configuration spéciale nécessaire

**Windows avec WSL2**
- Docker Desktop doit utiliser WSL2 backend (pas Hyper-V)
- Git Bash OU WSL2 terminal (pas PowerShell classique)
- Chemins Windows/Linux peuvent causer problèmes (privilégier WSL2)

**Proxies d'entreprise**
Si derrière proxy :
```bash
# Configurer Git
git config --global http.proxy http://proxy.entreprise:port
git config --global https.proxy http://proxy.entreprise:port

# Configurer Docker (dans daemon.json)
# Configurer pip (dans ~/.pip/pip.conf)
```

**Quotas et permissions**
- Docker : Nécessite droits admin pour installation (pas pour utilisation)
- Python packages : Utiliser `--user` si pas admin : `pip3 install --user`
- Git : Aucun droit spécial nécessaire

**Alternatives GitHub CLI**
Si `gh` non disponible et pas d'installation possible :
- Workflows manuels documentés dans chaque story (S1-01, S4-03, S4-04)
- Création PR via interface web GitHub
- Téléchargement artefacts manuel

---

## Post-tâche

**Archiver rapport** :
```bash
mkdir -p .validations/
mv ENV-VALIDATION-REPORT.md .validations/env-$(date +%Y%m%d).md
```

**Documenter dans README** :
```markdown
## Prérequis système

Environnement validé avec story S0-00 :
- Git ≥ 2.30
- Docker ≥ 20.10 + Compose v2+
- Python ≥ 3.11
- GitHub CLI (optionnel)

Voir `.validations/env-YYYYMMDD.md` pour détails configuration.
```

**Partager avec l'équipe** :
```
📧 À : Bertrand, Alex
Objet : SPAN SG - Environnement développement validé

Mon environnement est prêt pour démarrer le projet.

Rapport : [joindre .validations/env-YYYYMMDD.md]

Prochaine étape : S1-01 (Création repo GitHub)
```

**Créer aide-mémoire commandes** :
```bash
cat > .commands-cheatsheet.md << 'EOF'
# Commandes fréquentes SPAN SG

## Développement local
docker compose up              # Démarrer MkDocs local
mkdocs build --strict          # Build avec validation
python scripts/calculate_scores.py  # Recalculer scores

## Git workflow
git checkout draft             # Travailler sur draft
git checkout -b feature/XXX    # Nouvelle branche
git add . && git commit -m "..." && git push  # Commit + push

## Scripts utiles
./scripts/init-repo.sh         # Initialiser repo
./scripts/create-module.sh SRV # Créer module
./scripts/release.sh vX.Y.Z    # Préparer release
EOF
```

---

## Estimation temps par OS

- **macOS avec Homebrew** : 15-20 min (installations rapides)
- **Linux (Debian/Ubuntu)** : 20-30 min (apt peut être lent)
- **Windows + WSL2** : 30-45 min (setup WSL2 + Docker Desktop)

**Temps inclut** : Téléchargements, installations, configurations, tests

**Si tout déjà installé** : 5 min (juste validation + rapport)
