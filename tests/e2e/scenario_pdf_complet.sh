#!/usr/bin/env bash
# Scénario : Vérifier PDF contient toutes les pages

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : PDF complet"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Générer PDF
mkdocs build --config-file mkdocs-pdf.yml --site-dir "$TEMP_DIR/pdf-site" > /dev/null 2>&1

PDF_FILE="$TEMP_DIR/pdf-site/pdf/document.pdf"

# Vérifier présence
test -f "$PDF_FILE" || { echo "❌ FAIL: PDF absent"; exit 1; }

# Vérifier taille > 100 KB (indicateur contenu complet)
SIZE=$(stat -f%z "$PDF_FILE")
if [ $SIZE -lt 102400 ]; then
    echo "❌ FAIL: PDF trop petit ($SIZE bytes < 100KB)"
    exit 1
fi

# Vérifier contenu avec pdfinfo (si disponible)
if command -v pdfinfo &> /dev/null; then
    PAGES=$(pdfinfo "$PDF_FILE" | grep "^Pages:" | awk '{print $2}')
    if [ "$PAGES" -lt 10 ]; then
        echo "❌ FAIL: PDF incomplet ($PAGES pages < 10)"
        exit 1
    fi
    echo "✅ Scénario PDF complet OK ($PAGES pages, ${SIZE} bytes)"
else
    echo "✅ Scénario PDF complet OK (${SIZE} bytes, pdfinfo non disponible)"
fi
