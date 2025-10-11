#!/usr/bin/env bash
# Scénario : Tester rollback complet (all modules)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Rollback complet"

# Backup tous modules
cp -r docs/modules /tmp/modules-backup

# Modifier tous modules (cocher 1er point partout) - sed avec numéro ligne
for module in snum sircom srh siep safi bgs; do
    LINE=$(grep -n '^- \[ \].*<!-- DINUM -->' "docs/modules/$module.md" | head -1 | cut -d: -f1)
    sed -i.bak "${LINE}s/- \[ \]/- [x]/" "docs/modules/$module.md"
    rm -f "docs/modules/$module.md.bak"
done

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier TOTAL après modification 6 modules (scores actuels: SIRCOM 24/31, autres 0/31)
# Calcul : SIRCOM (24→25) + SNUM (0→1) + SRH (0→1) + SIEP (0→1) + SAFI (0→1) + BGS (0→1)
#        = 25 + 1 + 1 + 1 + 1 + 1 = 30/186
grep -q "30/186" docs/synthese.md || { echo "❌ FAIL: Score incorrect"; cat docs/synthese.md; exit 1; }

# Rollback
rm -rf docs/modules
mv /tmp/modules-backup docs/modules
python3 scripts/calculate_scores.py

# Vérifier retour à 24/186 (score initial)
grep -q "24/186" docs/synthese.md || { echo "❌ FAIL: Rollback incorrect"; exit 1; }

echo "✅ Scénario rollback OK"
