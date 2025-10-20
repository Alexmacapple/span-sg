#!/bin/bash
set -e

# Script de release SPAN SG
# Automatise S4-03: Tag v1.0.0 et préparation release
# Usage: ./scripts/release.sh <VERSION>

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "🚀 SPAN SG - Script de release"
echo "================================"
echo ""

# Paramètre version
VERSION="${1}"

if [ -z "$VERSION" ]; then
    echo -e "${RED}❌ Usage: ./scripts/release.sh <VERSION>${NC}"
    echo ""
    echo "Exemples:"
    echo "  ./scripts/release.sh v1.0.0    # Première release majeure"
    echo "  ./scripts/release.sh v1.0.1    # Patch (correction bug)"
    echo "  ./scripts/release.sh v1.1.0    # Feature (nouvelle fonctionnalité)"
    echo "  ./scripts/release.sh v2.0.0    # Breaking change"
    echo ""
    echo "Convention Semantic Versioning:"
    echo "  vMAJOR.MINOR.PATCH"
    echo "  - MAJOR: Breaking changes (incompatibilité)"
    echo "  - MINOR: Nouvelles features (rétrocompatible)"
    echo "  - PATCH: Bug fixes uniquement"
    exit 1
fi

# Valider format version
if [[ ! "$VERSION" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo -e "${RED}❌ Format version invalide: $VERSION${NC}"
    echo "Format attendu: vX.Y.Z (ex: v1.0.0)"
    exit 1
fi

echo -e "${BLUE}Version: $VERSION${NC}"
echo ""

# Vérifications prérequis
echo "🔍 Vérifications prérequis..."

# Sur branche draft
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "draft" ]; then
    echo -e "${YELLOW}⚠️  Pas sur branche draft (actuel: $CURRENT_BRANCH)${NC}"
    read -p "Checkout draft et continuer ? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git checkout draft
        git pull origin draft
    else
        echo "Annulation. Lancer depuis draft."
        exit 1
    fi
fi
echo -e "${GREEN}✅ Sur branche draft${NC}"

# Working tree propre
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${RED}❌ Working tree pas propre (modifications non committées)${NC}"
    git status --short
    exit 1
fi
echo -e "${GREEN}✅ Working tree clean${NC}"

# Tag n'existe pas déjà
if git rev-parse "$VERSION" >/dev/null 2>&1; then
    echo -e "${RED}❌ Tag $VERSION existe déjà${NC}"
    echo "Tags existants:"
    git tag -l
    exit 1
fi
echo -e "${GREEN}✅ Tag $VERSION disponible${NC}"

# CHANGELOG.md existe
if [ ! -f "CHANGELOG.md" ]; then
    echo -e "${YELLOW}⚠️  CHANGELOG.md n'existe pas${NC}"
    read -p "Créer CHANGELOG.md minimal ? (Y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        cat > CHANGELOG.md << EOF
# Changelog SPAN SG

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [Unreleased]

---

## [$VERSION] - $(date +%Y-%m-%d)

### Ajouté
- Nouvelle fonctionnalité ou module
- Exemple : Génération PDF automatique en CI avec métadonnées RGAA

### Modifié
- Amélioration ou changement de comportement existant
- Exemple : Migration mkdocs-material → mkdocs-dsfr (Système de Design État)

### Corrigé
- Correction de bug ou d'erreur
- Exemple : Score CI/CD passant de 9/10 à 10/10 (génération PDF réactivée)

---

[$VERSION]: https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/releases/tag/$VERSION
EOF
        echo -e "${GREEN}✅ CHANGELOG.md créé${NC}"
    fi
fi

# Vérifier section version dans CHANGELOG
if ! grep -q "## \[$VERSION\]" CHANGELOG.md; then
    echo -e "${YELLOW}⚠️  Version $VERSION pas dans CHANGELOG.md${NC}"
    echo "Éditer CHANGELOG.md et ajouter section:"
    echo "  ## [$VERSION] - $(date +%Y-%m-%d)"
    echo ""
    read -p "Ouvrir éditeur maintenant ? (Y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        ${EDITOR:-vim} CHANGELOG.md
    fi

    # Re-vérifier
    if ! grep -q "## \[$VERSION\]" CHANGELOG.md; then
        echo -e "${RED}❌ CHANGELOG.md toujours sans section $VERSION${NC}"
        exit 1
    fi
fi
echo -e "${GREEN}✅ CHANGELOG.md contient $VERSION${NC}"

# Calculer scores actuels
echo ""
echo "🧮 Calcul scores actuels..."
if python scripts/calculate_scores.py > /dev/null 2>&1; then
    TOTAL_SCORE=$(grep "TOTAL" docs/synthese.md | grep -oP '\d+/\d+' | head -1)
    PERCENT_SCORE=$(grep "TOTAL" docs/synthese.md | grep -oP '\d+\.\d+%' | head -1)
    echo -e "${GREEN}✅ Score global: $TOTAL_SCORE ($PERCENT_SCORE)${NC}"
else
    echo -e "${RED}❌ Erreur calcul scores${NC}"
    exit 1
fi

# Build test
echo ""
echo "🔨 Test build MkDocs..."
if mkdocs build --strict > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Build MkDocs OK (mode strict)${NC}"
else
    echo -e "${RED}❌ Build MkDocs échoue${NC}"
    mkdocs build --strict
    exit 1
fi

# Commit préparation release
echo ""
echo "📝 Préparation commit release..."

# Mettre à jour versions dans fichiers (optionnel)
# Si vous avez un fichier VERSION ou package.json

read -p "Committer préparation release ? (Y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    git add CHANGELOG.md docs/synthese.md
    git commit -m "chore: prepare release $VERSION

- Update CHANGELOG.md $VERSION entry
- Current score: $TOTAL_SCORE ($PERCENT_SCORE)

Release notes: See CHANGELOG.md
" || echo "Rien à committer (déjà à jour)"

    git push origin draft
    echo -e "${GREEN}✅ Préparation commitée et pushée${NC}"
fi

# Attendre CI
echo ""
echo "⏳ Attendre validation CI sur draft..."
echo "   Vérifier: https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/actions"
echo ""
read -p "CI est verte ? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}⚠️  Attendre CI avant de continuer${NC}"
    exit 1
fi

# Créer tag annoté
echo ""
echo "🏷️  Création tag $VERSION..."

# Message tag détaillé
TAG_MESSAGE="Release SPAN SG $VERSION

Score global: $TOTAL_SCORE ($PERCENT_SCORE)

Highlights:
- 6 modules services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- CI/CD opérationnelle
- Export PDF automatique

Changelog: See CHANGELOG.md
Sponsor approval: decisions/v1.0/DECISION-GO-NO-GO-$VERSION.md (si applicable)
Reviewers: Bertrand, Alex
"

git tag -a "$VERSION" -m "$TAG_MESSAGE"
echo -e "${GREEN}✅ Tag $VERSION créé (local)${NC}"

# Afficher tag
echo ""
echo "Tag créé:"
git show "$VERSION" --stat

# Pusher tag
echo ""
read -p "Pusher tag vers origin ? (Y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    git push origin "$VERSION"
    echo -e "${GREEN}✅ Tag $VERSION pushé vers origin${NC}"
else
    echo -e "${YELLOW}⚠️  Tag pas pushé (lancer manuellement: git push origin $VERSION)${NC}"
fi

# Télécharger artefacts CI
echo ""
echo "📦 Artefacts CI..."
echo "Télécharger artefacts depuis:"
echo "  https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/actions"
echo ""
echo "Rechercher dernier run sur draft → Artifacts → span-site.zip"
echo "Extraire exports/span-sg.pdf pour la release GitHub"

# Préparer release notes
echo ""
echo "📋 Préparation release notes..."

RELEASE_NOTES_FILE="RELEASE-NOTES-$VERSION.md"
if [ ! -f "$RELEASE_NOTES_FILE" ]; then
    cat > "$RELEASE_NOTES_FILE" << EOF
# SPAN SG $VERSION - Release Notes

**Date de publication** : $(date +"%d/%m/%Y")
**Tag** : \`$VERSION\`

---

## 📊 Vue d'ensemble

- **Score global** : $TOTAL_SCORE ($PERCENT_SCORE)
- **Modules** : 6 services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- **31 points DINUM** par module (référentiel officiel)

---

## ✨ Changelog

$(grep -A 50 "## \[$VERSION\]" CHANGELOG.md | head -50)

---

## 📦 Assets disponibles

- **Site HTML** : \`https://[pages-url]/\`
- **PDF d'archive** : Télécharger ci-dessous
- **Code source** : \`https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')\`

---

## 🔐 Conformité

- ✅ Déclarations d'accessibilité : Modules renseignés
- ✅ Référentiel DINUM : 31 points respectés
- ✅ RGAA 4.x : Niveau AA cible

---

**Validé par** : Yves (Sponsor), Bertrand (Validateur), Alex (Validateur)
**Date de validation** : $(date +"%d/%m/%Y")
EOF
    echo -e "${GREEN}✅ Release notes créées: $RELEASE_NOTES_FILE${NC}"
else
    echo -e "${YELLOW}⚠️  $RELEASE_NOTES_FILE existe déjà${NC}"
fi

# Instructions finales
echo ""
echo "=========================================="
echo -e "${GREEN}✅ Préparation release terminée !${NC}"
echo ""
echo "Prochaines étapes (S4-04 Publication):"
echo ""
echo "1. Créer release GitHub:"
echo "   https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/releases/new"
echo ""
echo "   - Tag: $VERSION"
echo "   - Title: SPAN SG $VERSION"
echo "   - Description: Copier depuis $RELEASE_NOTES_FILE"
echo "   - Assets: Joindre exports/span-sg-$VERSION.pdf"
echo ""
echo "2. Créer PR draft → main:"
echo "   gh pr create --base main --head draft \\"
echo "     --title \"Release $VERSION\" \\"
echo "     --body-file $RELEASE_NOTES_FILE"
echo ""
echo "3. Après merge main:"
echo "   - Vérifier déploiement production"
echo "   - Communiquer à l'équipe"
echo "=========================================="
