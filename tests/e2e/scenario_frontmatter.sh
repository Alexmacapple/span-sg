#!/usr/bin/env bash
# Scénario : Valider front-matter YAML tous modules

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Validation front-matter YAML"

for module in snum sircom srh siep safi bgs; do
    MODULE_FILE="docs/modules/$module.md"

    # Extraire front-matter (entre le premier et deuxième ---)
    FRONTMATTER=$(awk '/^---$/ {if (++count == 2) exit} count == 1 && !/^---$/ {print}' "$MODULE_FILE")

    # Valider YAML avec Python
    python3 -c "
import yaml
import sys
try:
    data = yaml.safe_load('''$FRONTMATTER''')
    assert 'service' in data, 'Clé service manquante'
    assert 'referent' in data, 'Clé referent manquante'
    assert 'updated' in data, 'Clé updated manquante'
except Exception as e:
    print(f'❌ FAIL $module: {e}')
    sys.exit(1)
" || exit 1

    echo "  ✅ $module : YAML valide"
done

echo "✅ Scénario front-matter OK (6 modules)"
