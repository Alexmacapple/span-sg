#!/usr/bin/env bash
# Scénario : Vérifier temps de build < 10s

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Performance build"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Mesurer temps build DSFR
START=$(date +%s)
mkdocs build --config-file mkdocs-dsfr.yml --site-dir "$TEMP_DIR/site" > /dev/null 2>&1
END=$(date +%s)

DURATION=$((END - START))

if [ $DURATION -gt 10 ]; then
    echo "❌ FAIL: Build trop long ($DURATION s > 10s)"
    exit 1
fi

echo "✅ Scénario performance OK (build en ${DURATION}s)"
