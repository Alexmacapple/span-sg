#!/usr/bin/env bash
# Scénario : Tester rollback complet (all modules)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Rollback complet"

# Backup tous modules
cp -r docs/modules /tmp/modules-backup

# Modifier tous modules (cocher 1er point partout)
for module in snum sircom srh siep safi bgs; do
    awk '/- \[ \].* DINUM/ && !done {sub(/- \[ \]/, "- [x]"); done=1} {print}' "docs/modules/$module.md" > "/tmp/$module.tmp"
    mv "/tmp/$module.tmp" "docs/modules/$module.md"
done

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier TOTAL après modification 6 modules
# Calcul : SIRCOM (7→8) + SNUM (0→1) + SRH (0→1) + SIEP (0→1) + SAFI (0→1) + BGS (0→1)
#        = 8 + 1 + 1 + 1 + 1 + 1 = 13/186
grep -q "13/186" docs/synthese.md || { echo "❌ FAIL: Score incorrect"; cat docs/synthese.md; exit 1; }

# Rollback
rm -rf docs/modules
mv /tmp/modules-backup docs/modules
python3 scripts/calculate_scores.py

# Vérifier retour à 7/186
grep -q "7/186" docs/synthese.md || { echo "❌ FAIL: Rollback incorrect"; exit 1; }

echo "✅ Scénario rollback OK"
