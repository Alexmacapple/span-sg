#!/usr/bin/env bash
# Scénario : Vérifier preview HTTP local (Docker)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Preview HTTP local"

# Vérifier Docker running
if ! docker info > /dev/null 2>&1; then
    echo "⚠️  SKIP: Docker non démarré"
    exit 0
fi

# Démarrer mkdocs serve (background)
docker compose up -d mkdocs 2>/dev/null || {
    echo "⚠️  SKIP: Service mkdocs indisponible"
    exit 0
}

# Attendre 5s
sleep 5

# Test HTTP
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/)

if [ "$HTTP_CODE" != "200" ]; then
    echo "❌ FAIL: HTTP code = $HTTP_CODE (attendu 200)"
    docker compose down
    exit 1
fi

# Test page SIRCOM
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/modules/sircom/)

if [ "$HTTP_CODE" != "200" ]; then
    echo "❌ FAIL: Page SIRCOM HTTP = $HTTP_CODE"
    docker compose down
    exit 1
fi

docker compose down > /dev/null 2>&1

echo "✅ Scénario preview HTTP OK"
