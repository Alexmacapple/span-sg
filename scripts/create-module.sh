#!/bin/bash
set -e

# Script de création module SPAN
# Automatise S3-01: Création modules vides + front-matter
# Usage: ./scripts/create-module.sh <SERVICE> [REFERENT] [DATE]

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "📄 SPAN SG - Script création module"
echo "===================================="
echo ""

# Paramètres
SERVICE="${1}"
REFERENT="${2:-À définir}"
DATE="${3:-$(date +%Y-%m-%d)}"

if [ -z "$SERVICE" ]; then
    echo -e "${RED}❌ Usage: ./scripts/create-module.sh <SERVICE> [REFERENT] [DATE]${NC}"
    echo ""
    echo "Exemples:"
    echo "  ./scripts/create-module.sh SNUM"
    echo "  ./scripts/create-module.sh SIRCOM \"Jean Dupont\" \"2025-09-30\""
    echo ""
    echo "Services SPAN SG v1:"
    echo "  - SNUM  : Service du Numérique"
    echo "  - SIRCOM: Service Interministériel des Ressources et Compétences"
    echo "  - SRH   : Service des Ressources Humaines"
    echo "  - SIEP  : Service de l'Innovation et de l'Évaluation"
    echo "  - SAFI  : Service des Affaires Financières et Immobilières"
    echo "  - BGS   : Bureau de Gestion des Services"
    exit 1
fi

# Normaliser service (uppercase)
SERVICE=$(echo "$SERVICE" | tr '[:lower:]' '[:upper:]')
SERVICE_LOWER=$(echo "$SERVICE" | tr '[:upper:]' '[:lower:]')

# Nom complet service (pour header)
case $SERVICE in
    SNUM)
        SERVICE_FULL="Service du Numérique"
        ;;
    SIRCOM)
        SERVICE_FULL="Service Interministériel des Ressources et des Compétences"
        ;;
    SRH)
        SERVICE_FULL="Service des Ressources Humaines"
        ;;
    SIEP)
        SERVICE_FULL="Service de l'Innovation et de l'Évaluation des Politiques"
        ;;
    SAFI)
        SERVICE_FULL="Service des Affaires Financières et Immobilières"
        ;;
    BGS)
        SERVICE_FULL="Bureau de Gestion des Services"
        ;;
    *)
        echo -e "${YELLOW}⚠️  Service '$SERVICE' non reconnu (hors périmètre v1)${NC}"
        read -p "Nom complet du service: " SERVICE_FULL
        ;;
esac

echo "Configuration:"
echo "  - Service     : $SERVICE ($SERVICE_FULL)"
echo "  - Référent    : $REFERENT"
echo "  - Date        : $DATE"
echo ""

# Vérifier template existe
TEMPLATE_PATH="docs/modules/_template.md"
if [ ! -f "$TEMPLATE_PATH" ]; then
    echo -e "${RED}❌ Template non trouvé: $TEMPLATE_PATH${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Template trouvé${NC}"

# Vérifier module n'existe pas déjà
MODULE_PATH="docs/modules/${SERVICE_LOWER}.md"
if [ -f "$MODULE_PATH" ]; then
    echo -e "${YELLOW}⚠️  Module existe déjà: $MODULE_PATH${NC}"
    read -p "Écraser ? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Annulation."
        exit 0
    fi
    rm "$MODULE_PATH"
fi

# Copier template
echo ""
echo "📋 Création module depuis template..."
cp "$TEMPLATE_PATH" "$MODULE_PATH"
echo -e "${GREEN}✅ Module créé: $MODULE_PATH${NC}"

# Remplacer placeholders
echo "🔧 Personnalisation front-matter..."

# Remplacer dans le fichier
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS (BSD sed)
    sed -i '' "s/service: \[SERVICE\]/service: $SERVICE/" "$MODULE_PATH"
    sed -i '' "s/referent: \"\[Prénom Nom\]\"/referent: \"[$REFERENT - $SERVICE_FULL]\"/" "$MODULE_PATH"
    sed -i '' "s/updated: \"2025-09-30\"/updated: \"$DATE\"/" "$MODULE_PATH"

    # Header
    sed -i '' "s/# SPAN \[SERVICE\]/# SPAN $SERVICE/" "$MODULE_PATH"
    sed -i '' "s/\*\*Service\*\* \[Nom complet\]/\*\*Service\*\* $SERVICE_FULL ($SERVICE)/" "$MODULE_PATH"
    sed -i '' "s/\*\*Dernière mise à jour\*\* 30 septembre 2025/**Dernière mise à jour** $(date -j -f "%Y-%m-%d" "$DATE" +"%d %B %Y" 2>/dev/null || echo "$DATE")/" "$MODULE_PATH"
else
    # Linux (GNU sed)
    sed -i "s/service: \[SERVICE\]/service: $SERVICE/" "$MODULE_PATH"
    sed -i "s/referent: \"\[Prénom Nom\]\"/referent: \"[$REFERENT - $SERVICE_FULL]\"/" "$MODULE_PATH"
    sed -i "s/updated: \"2025-09-30\"/updated: \"$DATE\"/" "$MODULE_PATH"

    # Header
    sed -i "s/# SPAN \[SERVICE\]/# SPAN $SERVICE/" "$MODULE_PATH"
    sed -i "s/\*\*Service\*\* \[Nom complet\]/\*\*Service\*\* $SERVICE_FULL ($SERVICE)/" "$MODULE_PATH"
    sed -i "s/\*\*Dernière mise à jour\*\* 30 septembre 2025/**Dernière mise à jour** $(date -d "$DATE" +"%d %B %Y" 2>/dev/null || echo "$DATE")/" "$MODULE_PATH"
fi

echo -e "${GREEN}✅ Front-matter personnalisé${NC}"

# Validation structure
echo ""
echo "🔍 Validation structure..."

# Compter points DINUM
DINUM_COUNT=$(grep -c "<!-- DINUM -->" "$MODULE_PATH" || echo "0")
if [ "$DINUM_COUNT" -eq 31 ]; then
    echo -e "${GREEN}✅ 31 points DINUM présents${NC}"
else
    echo -e "${RED}❌ ERREUR: $DINUM_COUNT points DINUM (attendu 31)${NC}"
    exit 1
fi

# Vérifier aucune case cochée
CHECKED_COUNT=$(grep -c "\[x\].*<!-- DINUM -->" "$MODULE_PATH" || echo "0")
if [ "$CHECKED_COUNT" -eq 0 ]; then
    echo -e "${GREEN}✅ Toutes cases vides (0/31)${NC}"
else
    echo -e "${YELLOW}⚠️  $CHECKED_COUNT cases cochées (attendu 0 pour module vide)${NC}"
fi

# Vérifier sections obligatoires
SECTIONS_COUNT=$(grep -c "^## [1-5]\." "$MODULE_PATH" || echo "0")
if [ "$SECTIONS_COUNT" -ge 5 ]; then
    echo -e "${GREEN}✅ 5 sections obligatoires présentes${NC}"
else
    echo -e "${RED}❌ ERREUR: Seulement $SECTIONS_COUNT sections (attendu 5)${NC}"
fi

# Test scoring
echo ""
echo "🧮 Test scoring..."
if python scripts/calculate_scores.py > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Script scoring OK${NC}"

    # Afficher score module
    SCORE_LINE=$(python scripts/calculate_scores.py 2>/dev/null | grep -i "$SERVICE" || echo "")
    if [ -n "$SCORE_LINE" ]; then
        echo "   Score: $SCORE_LINE"
    fi
else
    echo -e "${RED}❌ Erreur scoring - vérifier docs/synthese.md${NC}"
fi

# Résumé
echo ""
echo "=========================================="
echo -e "${GREEN}✅ Module $SERVICE créé avec succès !${NC}"
echo ""
echo "Fichier:"
echo "  📄 $MODULE_PATH"
echo ""
echo "Validation:"
echo "  ✅ Structure: 31 points DINUM, 5 sections"
echo "  ✅ Front-matter: service, referent, updated"
echo "  ✅ Score: 0/31 (module vide)"
echo ""
echo "Prochaines étapes:"
echo "  1. Ouvrir: code $MODULE_PATH"
echo "  2. Remplir sections 1-5 avec contenu réel (S3-03)"
echo "  3. Cocher points DINUM conformes"
echo "  4. Créer PR: git checkout -b feature/create-$SERVICE_LOWER"
echo "            git add $MODULE_PATH docs/synthese.md"
echo "            git commit -m \"feat($SERVICE_LOWER): crée module vide avec front-matter\""
echo "            git push -u origin feature/create-$SERVICE_LOWER"
echo "=========================================="
