#!/usr/bin/env bash
# Vérification prérequis S2-06

set -euo pipefail

echo "=== Vérification prérequis S2-06 ==="
echo ""

ERRORS=0

# Test 1 : Docker installé
echo -n "Docker installé... "
if command -v docker &> /dev/null; then
    echo "✅ OK"
else
    echo "❌ FAIL"
    echo "   → Installer Docker Desktop : https://www.docker.com/products/docker-desktop"
    ERRORS=$((ERRORS + 1))
fi

# Test 2 : Docker démarré
echo -n "Docker démarré... "
if docker info > /dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FAIL"
    echo "   → Lancer Docker Desktop"
    ERRORS=$((ERRORS + 1))
fi

# Test 3 : Homebrew installé (macOS uniquement)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -n "Homebrew installé... "
    if command -v brew &> /dev/null; then
        echo "✅ OK"
    else
        echo "❌ FAIL"
        echo "   → Installer Homebrew : https://brew.sh"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Test 4 : act installé (optionnel, sera installé en Partie 2)
echo -n "act installé (optionnel)... "
if command -v act &> /dev/null; then
    echo "✅ OK"
else
    echo "⏭️  À installer (Partie 2)"
fi

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ Tous les prérequis sont satisfaits"
    exit 0
else
    echo "❌ $ERRORS prérequis manquant(s)"
    echo ""
    echo "Corriger les prérequis avant de continuer l'implémentation S2-06."
    exit 1
fi
