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
    sed -i '' '0,/- \[ \].*<!-- DINUM -->/s//- [x] Point coché <!-- DINUM -->/' "docs/modules/$module.md"
done

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier TOTAL après modification 6 modules
# Calcul : SIRCOM (6→7) + SNUM (0→1) + SRH (0→1) + SIEP (0→1) + SAFI (0→1) + BGS (0→1)
#        = 7 + 1 + 1 + 1 + 1 + 1 = 12/186
grep -q "12/186" docs/synthese.md || { echo "❌ FAIL: Score incorrect"; cat docs/synthese.md; exit 1; }

# Rollback
rm -rf docs/modules
mv /tmp/modules-backup docs/modules
python3 scripts/calculate_scores.py

# Vérifier retour à 6/186
grep -q "6/186" docs/synthese.md || { echo "❌ FAIL: Rollback incorrect"; exit 1; }

echo "✅ Scénario rollback OK"
