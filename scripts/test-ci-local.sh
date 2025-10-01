#!/usr/bin/env bash
# Test GitHub Actions en local avec act

set -euo pipefail

echo "=== Test CI local avec act ==="

# Vérifier act installé
if ! command -v act &> /dev/null; then
    echo "❌ act non installé. Installer avec: brew install act"
    exit 1
fi

# Vérifier Docker running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker non démarré. Lancer Docker Desktop."
    exit 1
fi

# Lister jobs disponibles
echo "Jobs disponibles :"
act -l

echo ""
echo "Exécution job 'build' :"

# Exécuter job build
if act -j build; then
    echo "✅ CI locale réussie"
    exit 0
else
    echo "❌ CI locale échouée"
    exit 1
fi
