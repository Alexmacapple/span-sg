#!/usr/bin/env bash
# Test : V\u00e9rifier que le th\u00e8me DSFR est pr\u00e9serv\u00e9 dans site/

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Test : Th\u00e8me DSFR pr\u00e9serv\u00e9 dans site/"

# V\u00e9rifier que site/ existe
if [ ! -d "site" ]; then
    echo "\u274c FAIL: R\u00e9pertoire site/ introuvable"
    exit 1
fi

# V\u00e9rifier que site/index.html existe
if [ ! -f "site/index.html" ]; then
    echo "\u274c FAIL: site/index.html introuvable"
    exit 1
fi

# V\u00e9rifier pr\u00e9sence fr-header (DSFR)
if ! grep -q 'fr-header' site/index.html; then
    echo "\u274c FAIL: Th\u00e8me DSFR perdu (fr-header manquant)"
    echo "D\u00e9tails HTML:"
    grep -E "<header|md-header|fr-header" site/index.html || true
    exit 1
fi

# V\u00e9rifier absence md-header (Material)
if grep -q 'md-header' site/index.html; then
    echo "\u274c FAIL: Th\u00e8me Material d\u00e9tect\u00e9 (md-header pr\u00e9sent)"
    exit 1
fi

echo "\u2705 Th\u00e8me DSFR pr\u00e9serv\u00e9 (fr-header pr\u00e9sent, md-header absent)"
