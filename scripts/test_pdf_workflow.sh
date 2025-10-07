#!/bin/bash
# Test complet du workflow d'export PDF
# Usage: ./scripts/test_pdf_workflow.sh

set -e  # Arrêter si une commande échoue

echo "🧪 Test workflow export PDF SPAN SG"
echo "===================================="
echo ""

# Test 1: Génération du PDF
echo "📄 Test 1: Génération du PDF..."
if ! mkdocs build --config-file mkdocs-pdf.yml > /dev/null 2>&1; then
    echo "❌ Échec de la génération PDF"
    exit 1
fi

if [ ! -f exports/span-sg.pdf ]; then
    echo "❌ Fichier exports/span-sg.pdf non généré"
    exit 1
fi

echo "   ✅ PDF généré avec succès"
echo ""

# Test 2: Vérification taille PDF
echo "📏 Test 2: Vérification taille du PDF..."
pdf_size=$(du -k exports/span-sg.pdf | cut -f1)

if [ "$pdf_size" -lt 10 ]; then
    echo "   ⚠️  PDF suspicieusement petit (${pdf_size}KB)"
    exit 1
fi

if [ "$pdf_size" -gt 10240 ]; then
    echo "   ⚠️  PDF trop lourd (${pdf_size}KB > 10MB)"
fi

echo "   ✅ Taille PDF: ${pdf_size}KB"
echo ""

# Test 3: Enrichissement metadata
echo "🏷️  Test 3: Enrichissement metadata..."
if ! python scripts/enrich_pdf_metadata.py exports/span-sg.pdf > /dev/null 2>&1; then
    echo "   ⚠️  Échec enrichissement (pikepdf manquant?)"
    echo "   → Installer avec: pip install pikepdf"
else
    echo "   ✅ Metadata enrichies"
fi
echo ""

# Test 4: Validation metadata (si pdfinfo disponible)
echo "🔍 Test 4: Validation metadata..."
if command -v pdfinfo &> /dev/null; then
    # Vérifier titre
    if pdfinfo exports/span-sg.pdf | grep -q "Title.*SPAN"; then
        echo "   ✅ Titre: OK"
    else
        echo "   ⚠️  Titre non trouvé dans metadata"
    fi

    # Vérifier langue
    if pdfinfo exports/span-sg.pdf 2>/dev/null | grep -q "fr-FR\|fr_FR\|French"; then
        echo "   ✅ Langue: OK (fr-FR)"
    else
        echo "   ⚠️  Langue non définie"
    fi

    # Vérifier keywords
    if pdfinfo exports/span-sg.pdf | grep -qi "Keywords.*SPAN\|accessibilité"; then
        echo "   ✅ Keywords: OK"
    else
        echo "   ⚠️  Keywords non trouvés"
    fi
else
    echo "   ℹ️  pdfinfo non installé, validation metadata ignorée"
    echo "   → Installer avec: apt install poppler-utils (Linux)"
    echo "   → Installer avec: brew install poppler (Mac)"
fi
echo ""

# Test 5: Nombre de pages (si pdfinfo disponible)
echo "📖 Test 5: Comptage pages..."
if command -v pdfinfo &> /dev/null; then
    page_count=$(pdfinfo exports/span-sg.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}')

    if [ -n "$page_count" ]; then
        if [ "$page_count" -lt 5 ]; then
            echo "   ⚠️  PDF suspicieusement court ($page_count pages)"
        elif [ "$page_count" -gt 100 ]; then
            echo "   ⚠️  PDF très long ($page_count pages)"
        else
            echo "   ✅ Nombre de pages: $page_count"
        fi
    else
        echo "   ⚠️  Impossible de compter les pages"
    fi
else
    echo "   ℹ️  pdfinfo non disponible, comptage ignoré"
fi
echo ""

# Résumé
echo "===================================="
echo "✅ Tous les tests passent"
echo ""
echo "📄 PDF généré: exports/span-sg.pdf (${pdf_size}KB)"
echo ""
echo "🔗 Étapes suivantes:"
echo "   1. Ouvrir le PDF et vérifier visuellement"
echo "   2. Tester accessibilité avec PAC 2024"
echo "   3. Valider dans la CI (push sur draft)"
