#!/bin/bash
# Script de validation environnement Docker pour SPAN SG
# Automatise S1-02: Configuration Docker local pour développement
# Usage: ./scripts/validate-env.sh

set -e

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variables
REPORT_FILE="DOCKER-VALIDATION-REPORT.md"
ERRORS=0
WARNINGS=0

echo -e "${GREEN}=== Validation Environnement Docker SPAN SG ===${NC}\n"

# Function: Check command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function: Add to report
add_to_report() {
    echo "$1" >> "$REPORT_FILE"
}

# Initialize report
cat > "$REPORT_FILE" << EOF
# Rapport validation environnement Docker SPAN SG

Date : $(date +"%Y-%m-%d %H:%M:%S")
Machine : $(uname -a)

---

## Résultats validation

EOF

# ====================
# Test 1: Docker installé
# ====================
echo -e "${YELLOW}[1/8]${NC} Vérification Docker..."
if command_exists docker; then
    DOCKER_VERSION=$(docker --version)
    echo -e "${GREEN}✓${NC} Docker installé : $DOCKER_VERSION"
    add_to_report "- [x] Docker installé : \`$DOCKER_VERSION\`"

    # Vérifier version minimale Docker 20.10
    DOCKER_VERSION_NUM=$(docker --version | grep -oP '\d+\.\d+' | head -1)
    DOCKER_MAJOR=$(echo "$DOCKER_VERSION_NUM" | cut -d. -f1)
    DOCKER_MINOR=$(echo "$DOCKER_VERSION_NUM" | cut -d. -f2)

    if [ "$DOCKER_MAJOR" -ge 20 ] && [ "$DOCKER_MINOR" -ge 10 ]; then
        echo -e "${GREEN}✓${NC} Version Docker ≥ 20.10 (OK)"
        add_to_report "  - Version minimale respectée (≥20.10)"
    else
        echo -e "${YELLOW}⚠${NC}  Version Docker < 20.10 (upgrade recommandé)"
        add_to_report "  - ⚠️ Version < 20.10 (upgrade recommandé)"
        ((WARNINGS++))
    fi
else
    echo -e "${RED}✗${NC} Docker NON installé"
    add_to_report "- [ ] Docker NON installé"
    add_to_report "  - ❌ Installer Docker Desktop : https://docs.docker.com/get-docker/"
    ((ERRORS++))
fi
echo ""

# ====================
# Test 2: Docker daemon running
# ====================
echo -e "${YELLOW}[2/8]${NC} Vérification Docker daemon..."
if docker info > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Docker daemon running"
    add_to_report "- [x] Docker daemon running"
else
    echo -e "${RED}✗${NC} Docker daemon NOT running"
    add_to_report "- [ ] Docker daemon NOT running"
    add_to_report "  - ❌ Démarrer Docker Desktop (macOS/Windows) ou \`sudo systemctl start docker\` (Linux)"
    ((ERRORS++))
fi
echo ""

# ====================
# Test 3: Docker Compose disponible
# ====================
echo -e "${YELLOW}[3/8]${NC} Vérification Docker Compose..."
if docker compose version > /dev/null 2>&1; then
    COMPOSE_VERSION=$(docker compose version)
    echo -e "${GREEN}✓${NC} Docker Compose v2+ disponible : $COMPOSE_VERSION"
    add_to_report "- [x] Docker Compose disponible : \`$COMPOSE_VERSION\`"
elif command_exists docker-compose; then
    COMPOSE_VERSION=$(docker-compose --version)
    echo -e "${YELLOW}⚠${NC}  Docker Compose v1 (legacy) : $COMPOSE_VERSION"
    echo -e "    Recommandation : Migrer vers Docker Compose v2 (intégré à Docker)"
    add_to_report "- [x] Docker Compose disponible (v1 legacy) : \`$COMPOSE_VERSION\`"
    add_to_report "  - ⚠️ Migrer vers v2 recommandé"
    ((WARNINGS++))
else
    echo -e "${RED}✗${NC} Docker Compose NON disponible"
    add_to_report "- [ ] Docker Compose NON disponible"
    add_to_report "  - ❌ Installer Docker Desktop (inclut Compose) ou plugin Compose"
    ((ERRORS++))
fi
echo ""

# ====================
# Test 4: Port 8000 disponible
# ====================
echo -e "${YELLOW}[4/8]${NC} Vérification port 8000..."
if command_exists lsof; then
    PORT_CHECK=$(lsof -i :8000 2>/dev/null || true)
    if [ -z "$PORT_CHECK" ]; then
        echo -e "${GREEN}✓${NC} Port 8000 disponible"
        add_to_report "- [x] Port 8000 disponible"
    else
        echo -e "${YELLOW}⚠${NC}  Port 8000 déjà utilisé :"
        echo "$PORT_CHECK"
        echo -e "    Solution : Tuer processus avec \`kill <PID>\` ou changer port dans docker-compose.yml"
        add_to_report "- [x] Port 8000 utilisé (modifier docker-compose.yml ou tuer processus)"
        ((WARNINGS++))
    fi
elif command_exists netstat; then
    PORT_CHECK=$(netstat -an | grep :8000 | grep LISTEN || true)
    if [ -z "$PORT_CHECK" ]; then
        echo -e "${GREEN}✓${NC} Port 8000 disponible"
        add_to_report "- [x] Port 8000 disponible"
    else
        echo -e "${YELLOW}⚠${NC}  Port 8000 déjà utilisé"
        echo "$PORT_CHECK"
        add_to_report "- [x] Port 8000 utilisé (modifier docker-compose.yml)"
        ((WARNINGS++))
    fi
else
    echo -e "${YELLOW}⚠${NC}  Impossible de vérifier port 8000 (lsof/netstat non disponible)"
    add_to_report "- [ ] Port 8000 : Vérification impossible (lsof/netstat absent)"
    ((WARNINGS++))
fi
echo ""

# ====================
# Test 5: Image MkDocs Material disponible
# ====================
echo -e "${YELLOW}[5/8]${NC} Test pull image MkDocs Material..."
if docker info > /dev/null 2>&1; then
    echo "    Tentative pull squidfunk/mkdocs-material:latest (peut prendre 1-2 min)..."
    if docker pull squidfunk/mkdocs-material:latest > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} Image squidfunk/mkdocs-material pullée avec succès"
        add_to_report "- [x] Image \`squidfunk/mkdocs-material:latest\` disponible"

        # Vérifier taille image
        IMAGE_SIZE=$(docker images squidfunk/mkdocs-material:latest --format "{{.Size}}")
        echo -e "    Taille image : $IMAGE_SIZE"
        add_to_report "  - Taille : $IMAGE_SIZE"
    else
        echo -e "${RED}✗${NC} Échec pull image MkDocs Material"
        echo -e "    Possible timeout réseau ou problème proxy"
        add_to_report "- [ ] Image \`squidfunk/mkdocs-material\` : Pull failed"
        add_to_report "  - ❌ Vérifier connexion réseau ou configurer proxy Docker"
        ((ERRORS++))
    fi
else
    echo -e "${YELLOW}⚠${NC}  Docker daemon non actif, skip test pull image"
    add_to_report "- [ ] Image pull skipped (daemon non actif)"
fi
echo ""

# ====================
# Test 6: docker-compose.yml présent
# ====================
echo -e "${YELLOW}[6/8]${NC} Vérification docker-compose.yml..."
if [ -f "docker-compose.yml" ]; then
    echo -e "${GREEN}✓${NC} Fichier docker-compose.yml trouvé"
    add_to_report "- [x] Fichier \`docker-compose.yml\` présent"

    # Vérifier contenu minimal
    if grep -q "squidfunk/mkdocs-material" docker-compose.yml && \
       grep -q "8000:8000" docker-compose.yml && \
       grep -q "volumes:" docker-compose.yml; then
        echo -e "${GREEN}✓${NC} Configuration docker-compose.yml valide"
        add_to_report "  - Configuration valide (image, port, volumes)"
    else
        echo -e "${YELLOW}⚠${NC}  Configuration docker-compose.yml incomplète"
        add_to_report "  - ⚠️ Configuration potentiellement invalide"
        ((WARNINGS++))
    fi
else
    echo -e "${RED}✗${NC} Fichier docker-compose.yml absent"
    add_to_report "- [ ] Fichier \`docker-compose.yml\` absent"
    add_to_report "  - ❌ Créer docker-compose.yml selon S1-02"
    ((ERRORS++))
fi
echo ""

# ====================
# Test 7: Volume mount test (si Docker actif)
# ====================
echo -e "${YELLOW}[7/8]${NC} Test montage volume..."
if docker info > /dev/null 2>&1 && [ -f "docker-compose.yml" ]; then
    # Test simple : monter volume et vérifier accès
    TEST_RESULT=$(docker run --rm -v "$(pwd):/test" alpine:latest ls /test/docker-compose.yml 2>&1 || true)
    if echo "$TEST_RESULT" | grep -q "docker-compose.yml"; then
        echo -e "${GREEN}✓${NC} Montage volume fonctionnel"
        add_to_report "- [x] Montage volume testé : OK"
    else
        echo -e "${YELLOW}⚠${NC}  Montage volume échoué ou répertoire non partagé"
        echo -e "    macOS : Vérifier Docker Desktop → Settings → Resources → File Sharing"
        add_to_report "- [ ] Montage volume : Échec"
        add_to_report "  - ⚠️ Configurer File Sharing dans Docker Desktop (macOS)"
        ((WARNINGS++))
    fi
else
    echo -e "${YELLOW}⚠${NC}  Test volume skipped (Docker inactif ou docker-compose.yml absent)"
    add_to_report "- [ ] Montage volume : Test skipped"
fi
echo ""

# ====================
# Test 8: Test fonctionnel docker compose up (dry-run)
# ====================
echo -e "${YELLOW}[8/8]${NC} Test docker compose (dry-run)..."
if docker info > /dev/null 2>&1 && [ -f "docker-compose.yml" ]; then
    # Test config docker-compose
    if docker compose config > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} Configuration docker-compose valide"
        add_to_report "- [x] \`docker compose config\` : OK"
    else
        echo -e "${RED}✗${NC} Configuration docker-compose invalide"
        add_to_report "- [ ] \`docker compose config\` : Erreur de syntaxe"
        ((ERRORS++))
    fi
else
    echo -e "${YELLOW}⚠${NC}  Test docker compose skipped"
    add_to_report "- [ ] Test docker compose : skipped"
fi
echo ""

# ====================
# Résumé et rapport final
# ====================
add_to_report ""
add_to_report "---"
add_to_report ""
add_to_report "## Statut global"
add_to_report ""

echo -e "${GREEN}=== Résumé validation ===${NC}"
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ Environnement Docker validé${NC}"
    echo -e "${GREEN}✅ Prêt pour S1-02 (docker compose up)${NC}"
    add_to_report "✅ **Environnement Docker validé**"
    add_to_report ""
    add_to_report "Tous les prérequis sont remplis. Vous pouvez démarrer :"
    add_to_report "\`\`\`bash"
    add_to_report "docker compose up"
    add_to_report "# → http://localhost:8000"
    add_to_report "\`\`\`"
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  Environnement OK avec $WARNINGS warning(s)${NC}"
    echo -e "${GREEN}✅ Prêt pour S1-02 (avec corrections mineures recommandées)${NC}"
    add_to_report "⚠️ **Environnement OK avec warnings**"
    add_to_report ""
    add_to_report "Vous pouvez démarrer, mais corrections mineures recommandées."
else
    echo -e "${RED}❌ Environnement incomplet : $ERRORS erreur(s), $WARNINGS warning(s)${NC}"
    echo -e "${RED}❌ Corriger les erreurs avant S1-02${NC}"
    add_to_report "❌ **Environnement incomplet**"
    add_to_report ""
    add_to_report "Corriger les erreurs ci-dessus avant de continuer."
fi

echo ""
echo -e "Erreurs : ${RED}$ERRORS${NC}"
echo -e "Warnings : ${YELLOW}$WARNINGS${NC}"
echo ""
echo -e "Rapport généré : ${GREEN}$REPORT_FILE${NC}"

add_to_report ""
add_to_report "---"
add_to_report ""
add_to_report "*Généré par : \`scripts/validate-env.sh\`*"
add_to_report ""
add_to_report "*Prochaine étape : Story S1-02 - Configuration Docker local*"

# Exit code
if [ $ERRORS -gt 0 ]; then
    exit 2
elif [ $WARNINGS -gt 0 ]; then
    exit 1
else
    exit 0
fi
