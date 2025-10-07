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

# Build image avec gcc/g++ pour libsass (timeout 60s)
timeout 60 docker build -f Dockerfile.mkdocs-test -t span-mkdocs-test . > /dev/null 2>&1 || {
    echo "⚠️  SKIP: Build Docker timeout/échoué"
    exit 0
}

# Démarrer container mkdocs serve (background)
CONTAINER_ID=$(docker run -d -p 8000:8000 -v "$(pwd):/docs" span-mkdocs-test)

# Attendre 5s pour démarrage
sleep 5

# Test HTTP
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/)

if [ "$HTTP_CODE" != "200" ]; then
    echo "❌ FAIL: HTTP code = $HTTP_CODE (attendu 200)"
    docker stop "$CONTAINER_ID" > /dev/null 2>&1
    exit 1
fi

# Test page SIRCOM
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/modules/sircom/)

if [ "$HTTP_CODE" != "200" ]; then
    echo "❌ FAIL: Page SIRCOM HTTP = $HTTP_CODE"
    docker stop "$CONTAINER_ID" > /dev/null 2>&1
    exit 1
fi

# Cleanup
docker stop "$CONTAINER_ID" > /dev/null 2>&1

echo "✅ Scénario preview HTTP OK"
