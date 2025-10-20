#!/bin/bash
set -e

# Script d'initialisation repository SPAN SG
# Automatise S1-01: Création du dépôt GitHub privé
# Usage: ./scripts/init-repo.sh [repo-name] [github-org-or-user]

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "📦 SPAN SG - Script d'initialisation repository"
echo "=============================================="
echo ""

# Paramètres
REPO_NAME="${1:-span-sg-repo}"
GITHUB_OWNER="${2:-Alexmacapple}"

echo "Configuration:"
echo "  - Repository : ${REPO_NAME}"
echo "  - Owner      : ${GITHUB_OWNER}"
echo ""

# Vérifications prérequis
echo "🔍 Vérification prérequis..."

# Git installé
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git n'est pas installé${NC}"
    echo "Installer avec: brew install git (macOS) ou apt install git (Linux)"
    exit 1
fi
echo -e "${GREEN}✅ Git $(git --version)${NC}"

# GitHub CLI (optionnel mais recommandé)
if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}⚠️  GitHub CLI (gh) non installé - création repo manuelle nécessaire${NC}"
    GH_AVAILABLE=false
else
    echo -e "${GREEN}✅ GitHub CLI $(gh --version | head -1)${NC}"
    GH_AVAILABLE=true
fi

# Working directory propre
if [ -d ".git" ]; then
    echo -e "${YELLOW}⚠️  Repository Git déjà initialisé${NC}"
    read -p "Réinitialiser ? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf .git
        echo -e "${GREEN}✅ .git supprimé${NC}"
    else
        echo "Annulation."
        exit 0
    fi
fi

echo ""
echo "🚀 Initialisation Git local..."

# Init Git
git init
echo -e "${GREEN}✅ Repository Git initialisé${NC}"

# Config user (si pas déjà configuré globalement)
if [ -z "$(git config user.name)" ]; then
    read -p "Nom utilisateur Git: " git_name
    git config user.name "$git_name"
fi
if [ -z "$(git config user.email)" ]; then
    read -p "Email utilisateur Git: " git_email
    git config user.email "$git_email"
fi
echo -e "${GREEN}✅ Git config: $(git config user.name) <$(git config user.email)>${NC}"

# Branche principale
git branch -M main
echo -e "${GREEN}✅ Branche main créée${NC}"

# Premier commit
echo ""
echo "📝 Création commit initial..."
git add .
git commit -m "chore: import repo v3.3 GO-ready + enrichissements + agents + prompts

- Skeleton projet SPAN SG complet
- MkDocs Material configuré
- Scripts scoring automatique
- CI/CD GitHub Actions
- Documentation contributeur
- Roadmap BMAD 17 stories

🤖 Generated with [Claude Code](https://claude.com/claude-code)
"
echo -e "${GREEN}✅ Commit initial créé${NC}"

# Création repo GitHub
echo ""
if [ "$GH_AVAILABLE" = true ]; then
    echo "🌐 Création repository GitHub..."

    # Vérifier auth gh
    if ! gh auth status &> /dev/null; then
        echo -e "${YELLOW}⚠️  Non authentifié sur GitHub CLI${NC}"
        echo "Lancer: gh auth login"
        exit 1
    fi

    # Créer repo (privé par défaut)
    if gh repo create "${GITHUB_OWNER}/${REPO_NAME}" --private --source=. --remote=origin --description "SPAN SG - Schéma Pluriannuel d'Accessibilité Numérique du Secrétariat Général"; then
        echo -e "${GREEN}✅ Repository ${GITHUB_OWNER}/${REPO_NAME} créé (privé)${NC}"
    else
        echo -e "${RED}❌ Échec création repository${NC}"
        echo "Erreurs possibles:"
        echo "  - Repository existe déjà : https://github.com/${GITHUB_OWNER}/${REPO_NAME}"
        echo "  - Permissions insuffisantes"
        echo "  - Quota organisation atteint"
        exit 1
    fi

    # Push
    echo ""
    echo "⬆️  Push vers GitHub..."
    if git push -u origin main; then
        echo -e "${GREEN}✅ Code pushé sur origin/main${NC}"
    else
        echo -e "${RED}❌ Échec push${NC}"
        echo "Message erreur typique:"
        echo "  fatal: remote origin already exists → git remote remove origin"
        echo "  fatal: Authentication failed → gh auth refresh"
        exit 1
    fi

else
    # Création manuelle
    echo "📋 Étapes manuelles (GitHub CLI non disponible):"
    echo ""
    echo "1. Créer repository sur GitHub:"
    echo "   https://github.com/new"
    echo "   - Name: ${REPO_NAME}"
    echo "   - Visibility: Private"
    echo "   - Ne pas initialiser (README, .gitignore, license)"
    echo ""
    echo "2. Ajouter remote et push:"
    echo "   git remote add origin https://github.com/${GITHUB_OWNER}/${REPO_NAME}.git"
    echo "   git push -u origin main"
    echo ""
    exit 0
fi

# Créer branche draft
echo ""
echo "🌿 Création branche draft..."
git checkout -b draft
if git push -u origin draft; then
    echo -e "${GREEN}✅ Branche draft créée et pushée${NC}"
else
    echo -e "${RED}❌ Échec push draft${NC}"
    exit 1
fi

# Protection branche main (optionnel)
echo ""
read -p "Configurer protection branche main ? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🔒 Configuration protection branche..."
    echo "Étapes manuelles (API GitHub limitée):"
    echo "1. Aller sur: https://github.com/${GITHUB_OWNER}/${REPO_NAME}/settings/branches"
    echo "2. Add branch protection rule"
    echo "3. Branch name pattern: main"
    echo "4. Cocher: Require pull request before merging"
    echo "5. Cocher: Require approvals (1)"
fi

# Résumé
echo ""
echo "=========================================="
echo -e "${GREEN}✅ Initialisation terminée !${NC}"
echo ""
echo "Repository créé:"
echo "  📁 Local  : $(pwd)"
echo "  🌐 Remote : https://github.com/${GITHUB_OWNER}/${REPO_NAME}"
echo "  🌿 Branches: main (protection), draft (working)"
echo ""
echo "Prochaines étapes (S1-02):"
echo "  docker compose up    # Démarrer MkDocs local"
echo "  mkdocs build --strict    # Tester build"
echo ""
echo "Preview URL (après S2-03):"
echo "  https://${GITHUB_OWNER}.github.io/span-sg/"
echo "=========================================="
