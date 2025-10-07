#!/usr/bin/env bash
# Scénario : Détecter erreur Markdown (lien cassé en mode strict)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Erreur Markdown (lien cassé)"

# Backup
cp docs/modules/sircom.md /tmp/

# Injecter lien cassé
echo "[Lien cassé](page-inexistante.md)" >> docs/modules/sircom.md

# Tenter build strict (doit échouer)
if mkdocs build --strict 2>/dev/null; then
    echo "❌ FAIL: Build strict devrait échouer"
    mv /tmp/sircom.md docs/modules/
    exit 1
fi

# Restaurer
mv /tmp/sircom.md docs/modules/

echo "✅ Scénario erreur Markdown OK (strict mode détecté)"
