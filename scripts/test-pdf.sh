#!/bin/bash
# Script de test génération PDF pour SPAN SG
# Automatise S2-02: Export PDF avec fallback robuste
# Usage: ./scripts/test-pdf.sh

set -e

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variables
REPORT_FILE="PDF-TEST-REPORT.md"
ERRORS=0
WARNINGS=0
PDF_MAIN="exports/span-sg.pdf"
PDF_FALLBACK="exports/span-sg-fallback.pdf"

echo -e "${GREEN}=== Test Génération PDF SPAN SG ===${NC}\n"

# Function: Add to report
add_to_report() {
    echo "$1" >> "$REPORT_FILE"
}

# Function: Check PDF validity
check_pdf() {
    local pdf_file="$1"
    local pdf_name="$2"

    echo -e "${YELLOW}  Validation $pdf_name...${NC}"

    # Test 1: Fichier existe
    if [ ! -f "$pdf_file" ]; then
        echo -e "${RED}  ✗${NC} Fichier $pdf_file introuvable"
        add_to_report "  - [ ] Fichier existe"
        return 1
    fi
    echo -e "${GREEN}  ✓${NC} Fichier existe"
    add_to_report "  - [x] Fichier existe"

    # Test 2: Taille > 0
    FILESIZE=$(wc -c < "$pdf_file")
    if [ "$FILESIZE" -lt 1000 ]; then
        echo -e "${RED}  ✗${NC} Fichier trop petit ($FILESIZE bytes)"
        add_to_report "  - [ ] Taille valide : $FILESIZE bytes (< 1KB, suspect)"
        return 1
    fi
    echo -e "${GREEN}  ✓${NC} Taille : $(echo "scale=2; $FILESIZE/1024" | bc) KB"
    add_to_report "  - [x] Taille : $(echo "scale=2; $FILESIZE/1024" | bc) KB"

    # Test 3: Magic bytes PDF (%PDF-)
    if head -c 5 "$pdf_file" | grep -q "%PDF-"; then
        echo -e "${GREEN}  ✓${NC} Format PDF valide (magic bytes)"
        add_to_report "  - [x] Format PDF valide"
    else
        echo -e "${RED}  ✗${NC} Format PDF invalide (magic bytes manquants)"
        add_to_report "  - [ ] Format PDF invalide"
        return 1
    fi

    # Test 4: Nombre de pages (si pdfinfo disponible)
    if command -v pdfinfo >/dev/null 2>&1; then
        PAGES=$(pdfinfo "$pdf_file" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        if [ -n "$PAGES" ] && [ "$PAGES" -gt 0 ]; then
            echo -e "${GREEN}  ✓${NC} Nombre de pages : $PAGES"
            add_to_report "  - [x] Pages : $PAGES"

            if [ "$PAGES" -lt 10 ]; then
                echo -e "${YELLOW}  ⚠${NC}  Peu de pages ($PAGES < 10), contenu incomplet ?"
                add_to_report "  - ⚠️ Peu de pages (< 10)"
                ((WARNINGS++))
            fi
        else
            echo -e "${YELLOW}  ⚠${NC}  Impossible de lire nombre de pages"
            add_to_report "  - [ ] Pages : Non déterminé"
            ((WARNINGS++))
        fi
    else
        echo -e "${YELLOW}  ⚠${NC}  pdfinfo non disponible (skip test pages)"
        add_to_report "  - [ ] Pages : pdfinfo non installé"
    fi

    # Test 5: Contenu textuel (si pdftotext disponible)
    if command -v pdftotext >/dev/null 2>&1; then
        TEXT_CONTENT=$(pdftotext "$pdf_file" - 2>/dev/null | wc -c)
        if [ "$TEXT_CONTENT" -gt 1000 ]; then
            echo -e "${GREEN}  ✓${NC} Contenu textuel : $TEXT_CONTENT caractères"
            add_to_report "  - [x] Contenu textuel : $TEXT_CONTENT caractères"

            # Vérifier présence mots-clés SPAN
            if pdftotext "$pdf_file" - 2>/dev/null | grep -q "SPAN\|Accessibilité\|DINUM"; then
                echo -e "${GREEN}  ✓${NC} Mots-clés SPAN détectés"
                add_to_report "  - [x] Mots-clés SPAN/Accessibilité présents"
            else
                echo -e "${YELLOW}  ⚠${NC}  Mots-clés SPAN absents (contenu générique ?)"
                add_to_report "  - ⚠️ Mots-clés SPAN non trouvés"
                ((WARNINGS++))
            fi
        else
            echo -e "${RED}  ✗${NC} Contenu textuel insuffisant ($TEXT_CONTENT < 1000 chars)"
            add_to_report "  - [ ] Contenu textuel : $TEXT_CONTENT caractères (insuffisant)"
            return 1
        fi
    else
        echo -e "${YELLOW}  ⚠${NC}  pdftotext non disponible (skip test contenu)"
        add_to_report "  - [ ] Contenu : pdftotext non installé"
    fi

    # Test 6: Metadata PDF (si pdfinfo disponible)
    if command -v pdfinfo >/dev/null 2>&1; then
        TITLE=$(pdfinfo "$pdf_file" 2>/dev/null | grep "Title:" | cut -d: -f2- | xargs || echo "N/A")
        AUTHOR=$(pdfinfo "$pdf_file" 2>/dev/null | grep "Author:" | cut -d: -f2- | xargs || echo "N/A")
        echo -e "${GREEN}  ✓${NC} Metadata - Title: $TITLE, Author: $AUTHOR"
        add_to_report "  - [x] Metadata : Title=\"$TITLE\", Author=\"$AUTHOR\""
    fi

    return 0
}

# Initialize report
cat > "$REPORT_FILE" << EOF
# Rapport test génération PDF SPAN SG

Date : $(date +"%Y-%m-%d %H:%M:%S")
Machine : $(uname -a)

---

## Tests effectués

EOF

# ====================
# Test 0: Prérequis Python
# ====================
echo -e "${YELLOW}[0/3]${NC} Vérification prérequis..."

if command -v python3 >/dev/null 2>&1; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} Python installé : $PYTHON_VERSION"
    add_to_report "- [x] Python installé : \`$PYTHON_VERSION\`"
else
    echo -e "${RED}✗${NC} Python 3 non installé"
    add_to_report "- [ ] Python 3 non installé"
    ((ERRORS++))
fi

if command -v mkdocs >/dev/null 2>&1; then
    MKDOCS_VERSION=$(mkdocs --version)
    echo -e "${GREEN}✓${NC} MkDocs installé : $MKDOCS_VERSION"
    add_to_report "- [x] MkDocs installé : \`$MKDOCS_VERSION\`"
else
    echo -e "${RED}✗${NC} MkDocs non installé"
    add_to_report "- [ ] MkDocs non installé"
    add_to_report "  - ❌ Installer : \`pip install mkdocs-material\`"
    ((ERRORS++))
fi

echo ""
add_to_report ""

# ====================
# Test 1: Génération PDF principale (mkdocs-pdf-export-plugin)
# ====================
echo -e "${YELLOW}[1/3]${NC} Test génération PDF principale (mkdocs-pdf-export-plugin)..."
add_to_report "### Test 1 : PDF principal (mkdocs-pdf-export-plugin)"
add_to_report ""

# Vérifier plugin installé
if python3 -c "import mkdocs_pdf_export_plugin" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Plugin mkdocs-pdf-export-plugin installé"
    add_to_report "- [x] Plugin \`mkdocs-pdf-export-plugin\` installé"
else
    echo -e "${YELLOW}⚠${NC}  Plugin mkdocs-pdf-export-plugin non installé"
    echo -e "    Installation : pip install mkdocs-pdf-export-plugin"
    add_to_report "- [ ] Plugin \`mkdocs-pdf-export-plugin\` non installé"
    add_to_report "  - ⚠️ Installer : \`pip install mkdocs-pdf-export-plugin\`"
    ((WARNINGS++))
fi

# Vérifier config existe
if [ -f "mkdocs-pdf.yml" ]; then
    echo -e "${GREEN}✓${NC} Configuration mkdocs-pdf.yml trouvée"
    add_to_report "- [x] Configuration \`mkdocs-pdf.yml\` présente"

    # Tenter génération
    echo "    Génération PDF (peut prendre 30-60s)..."
    if mkdocs build --config-file mkdocs-pdf.yml > /tmp/mkdocs-pdf-build.log 2>&1; then
        echo -e "${GREEN}✓${NC} Build réussi"
        add_to_report "- [x] Build réussi"

        # Vérifier PDF généré
        if check_pdf "$PDF_MAIN" "PDF principal"; then
            echo -e "${GREEN}✅ PDF principal valide${NC}"
            add_to_report ""
            add_to_report "**Résultat** : ✅ PDF principal généré avec succès"
        else
            echo -e "${RED}❌ PDF principal invalide${NC}"
            add_to_report ""
            add_to_report "**Résultat** : ❌ PDF principal invalide"
            ((ERRORS++))
        fi
    else
        echo -e "${RED}✗${NC} Build échoué"
        add_to_report "- [ ] Build échoué"
        add_to_report ""
        add_to_report "**Logs erreur** :"
        add_to_report "\`\`\`"
        tail -20 /tmp/mkdocs-pdf-build.log >> "$REPORT_FILE"
        add_to_report "\`\`\`"
        add_to_report ""
        add_to_report "**Résultat** : ❌ Build PDF principal échoué"
        ((ERRORS++))
    fi
else
    echo -e "${RED}✗${NC} Configuration mkdocs-pdf.yml absente"
    add_to_report "- [ ] Configuration \`mkdocs-pdf.yml\` absente"
    add_to_report ""
    add_to_report "**Résultat** : ❌ Config manquante"
    ((ERRORS++))
fi

echo ""
add_to_report ""

# ====================
# Test 2: Génération PDF fallback (mkdocs-with-pdf)
# ====================
echo -e "${YELLOW}[2/3]${NC} Test génération PDF fallback (mkdocs-with-pdf)..."
add_to_report "### Test 2 : PDF fallback (mkdocs-with-pdf)"
add_to_report ""

# Vérifier plugin installé
if python3 -c "import mkdocs_with_pdf" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Plugin mkdocs-with-pdf installé"
    add_to_report "- [x] Plugin \`mkdocs-with-pdf\` installé"
else
    echo -e "${YELLOW}⚠${NC}  Plugin mkdocs-with-pdf non installé"
    echo -e "    Installation : pip install mkdocs-with-pdf"
    add_to_report "- [ ] Plugin \`mkdocs-with-pdf\` non installé"
    add_to_report "  - ⚠️ Installer : \`pip install mkdocs-with-pdf\`"
    ((WARNINGS++))
fi

# Vérifier config existe
if [ -f "mkdocs-with-pdf.yml" ]; then
    echo -e "${GREEN}✓${NC} Configuration mkdocs-with-pdf.yml trouvée"
    add_to_report "- [x] Configuration \`mkdocs-with-pdf.yml\` présente"

    # Tenter génération
    echo "    Génération PDF fallback (peut prendre 30-60s)..."
    if mkdocs build --config-file mkdocs-with-pdf.yml > /tmp/mkdocs-with-pdf-build.log 2>&1; then
        echo -e "${GREEN}✓${NC} Build fallback réussi"
        add_to_report "- [x] Build réussi"

        # Vérifier PDF généré
        if check_pdf "$PDF_FALLBACK" "PDF fallback"; then
            echo -e "${GREEN}✅ PDF fallback valide${NC}"
            add_to_report ""
            add_to_report "**Résultat** : ✅ PDF fallback généré avec succès"
        else
            echo -e "${RED}❌ PDF fallback invalide${NC}"
            add_to_report ""
            add_to_report "**Résultat** : ❌ PDF fallback invalide"
            ((ERRORS++))
        fi
    else
        echo -e "${RED}✗${NC} Build fallback échoué"
        add_to_report "- [ ] Build échoué"
        add_to_report ""
        add_to_report "**Logs erreur** :"
        add_to_report "\`\`\`"
        tail -20 /tmp/mkdocs-with-pdf-build.log >> "$REPORT_FILE"
        add_to_report "\`\`\`"
        add_to_report ""
        add_to_report "**Résultat** : ❌ Build PDF fallback échoué"
        ((ERRORS++))
    fi
else
    echo -e "${RED}✗${NC} Configuration mkdocs-with-pdf.yml absente"
    add_to_report "- [ ] Configuration \`mkdocs-with-pdf.yml\` absente"
    add_to_report ""
    add_to_report "**Résultat** : ❌ Config manquante"
    ((ERRORS++))
fi

echo ""
add_to_report ""

# ====================
# Test 3: Comparaison PDF principal vs fallback
# ====================
echo -e "${YELLOW}[3/3]${NC} Comparaison PDF principal vs fallback..."
add_to_report "### Test 3 : Comparaison"
add_to_report ""

if [ -f "$PDF_MAIN" ] && [ -f "$PDF_FALLBACK" ]; then
    SIZE_MAIN=$(wc -c < "$PDF_MAIN")
    SIZE_FALLBACK=$(wc -c < "$PDF_FALLBACK")

    echo -e "${GREEN}✓${NC} PDF principal : $(echo "scale=2; $SIZE_MAIN/1024" | bc) KB"
    echo -e "${GREEN}✓${NC} PDF fallback : $(echo "scale=2; $SIZE_FALLBACK/1024" | bc) KB"

    add_to_report "- PDF principal : $(echo "scale=2; $SIZE_MAIN/1024" | bc) KB"
    add_to_report "- PDF fallback : $(echo "scale=2; $SIZE_FALLBACK/1024" | bc) KB"

    if [ "$SIZE_MAIN" -gt "$SIZE_FALLBACK" ]; then
        DIFF_PERCENT=$(echo "scale=1; ($SIZE_MAIN - $SIZE_FALLBACK) * 100 / $SIZE_FALLBACK" | bc)
        echo -e "    Principal ${DIFF_PERCENT}% plus gros que fallback"
        add_to_report "- Principal ${DIFF_PERCENT}% plus volumineux"
    else
        DIFF_PERCENT=$(echo "scale=1; ($SIZE_FALLBACK - $SIZE_MAIN) * 100 / $SIZE_MAIN" | bc)
        echo -e "    Fallback ${DIFF_PERCENT}% plus gros que principal"
        add_to_report "- Fallback ${DIFF_PERCENT}% plus volumineux"
    fi

    if command -v pdfinfo >/dev/null 2>&1; then
        PAGES_MAIN=$(pdfinfo "$PDF_MAIN" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        PAGES_FALLBACK=$(pdfinfo "$PDF_FALLBACK" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        echo -e "    Pages principal : $PAGES_MAIN, fallback : $PAGES_FALLBACK"
        add_to_report "- Pages : principal $PAGES_MAIN vs fallback $PAGES_FALLBACK"
    fi
elif [ -f "$PDF_MAIN" ]; then
    echo -e "${GREEN}✓${NC} Seul PDF principal disponible (fallback non généré)"
    add_to_report "- Seul PDF principal disponible"
elif [ -f "$PDF_FALLBACK" ]; then
    echo -e "${YELLOW}⚠${NC}  Seul PDF fallback disponible (principal échoué)"
    add_to_report "- ⚠️ Seul PDF fallback disponible (principal échoué)"
    ((WARNINGS++))
else
    echo -e "${RED}✗${NC} Aucun PDF généré"
    add_to_report "- ❌ Aucun PDF généré"
    ((ERRORS++))
fi

echo ""
add_to_report ""

# ====================
# Résumé et rapport final
# ====================
add_to_report "---"
add_to_report ""
add_to_report "## Statut global"
add_to_report ""

echo -e "${GREEN}=== Résumé test PDF ===${NC}"
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ Génération PDF validée${NC}"
    echo -e "${GREEN}✅ Stratégie double PDF fonctionnelle${NC}"
    add_to_report "✅ **Génération PDF validée**"
    add_to_report ""
    add_to_report "Les deux stratégies PDF fonctionnent correctement."
    add_to_report "CI peut utiliser stratégie avec fallback (S2-02)."
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  Tests OK avec $WARNINGS warning(s)${NC}"
    echo -e "${GREEN}✅ Au moins un PDF généré${NC}"
    add_to_report "⚠️ **Tests OK avec warnings**"
    add_to_report ""
    add_to_report "Au moins une stratégie PDF fonctionne."
else
    echo -e "${RED}❌ Tests échoués : $ERRORS erreur(s), $WARNINGS warning(s)${NC}"
    echo -e "${RED}❌ Corriger les erreurs avant intégration CI${NC}"
    add_to_report "❌ **Tests échoués**"
    add_to_report ""
    add_to_report "Corriger les erreurs ci-dessus."
    add_to_report ""
    add_to_report "**Actions recommandées** :"
    add_to_report "1. Installer plugins : \`pip install mkdocs-pdf-export-plugin mkdocs-with-pdf\`"
    add_to_report "2. Vérifier configs : \`mkdocs-pdf.yml\` et \`mkdocs-with-pdf.yml\`"
    add_to_report "3. Re-tester : \`./scripts/test-pdf.sh\`"
fi

echo ""
echo -e "Erreurs : ${RED}$ERRORS${NC}"
echo -e "Warnings : ${YELLOW}$WARNINGS${NC}"
echo ""
echo -e "Rapport généré : ${GREEN}$REPORT_FILE${NC}"

if [ -f "$PDF_MAIN" ]; then
    echo -e "PDF principal : ${GREEN}$PDF_MAIN${NC}"
fi
if [ -f "$PDF_FALLBACK" ]; then
    echo -e "PDF fallback : ${GREEN}$PDF_FALLBACK${NC}"
fi

add_to_report ""
add_to_report "---"
add_to_report ""
add_to_report "*Généré par : \`scripts/test-pdf.sh\`*"
add_to_report ""
add_to_report "*Prochaine étape : Story S2-02 - Intégration CI/CD*"

# Exit code
if [ $ERRORS -gt 0 ]; then
    exit 2
elif [ $WARNINGS -gt 0 ]; then
    exit 1
else
    exit 0
fi
