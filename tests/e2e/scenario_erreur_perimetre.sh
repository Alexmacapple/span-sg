#!/usr/bin/env bash
# Scénario : Détecter erreur périmètre (≠ 31 points)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Erreur périmètre"

# Backup
cp docs/modules/sircom.md /tmp/

# Supprimer 1 checkbox DINUM (31 → 30) avec awk
awk '/- \[[ x]\].* DINUM/ && !done {done=1; next} {print}' docs/modules/sircom.md > /tmp/sircom-30.md
mv /tmp/sircom-30.md docs/modules/sircom.md

# Tenter scoring (doit échouer avec exit 2)
set +e
python3 scripts/calculate_scores.py 2>&1
EXIT_CODE=$?
set -e

if [ $EXIT_CODE -eq 0 ]; then
    echo "❌ FAIL: Scoring devrait échouer avec exit 2"
    mv /tmp/sircom.md docs/modules/
    exit 1
fi

# Vérifier exit code = 2
if [ $EXIT_CODE -ne 2 ]; then
    echo "❌ FAIL: Exit code attendu=2, obtenu=$EXIT_CODE"
    mv /tmp/sircom.md docs/modules/
    exit 1
fi

# Restaurer
mv /tmp/sircom.md docs/modules/
python3 scripts/calculate_scores.py

echo "✅ Scénario erreur périmètre OK (exit 2 détecté)"
