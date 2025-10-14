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
    LINE=$(grep -n '^- \[ \].*<!-- CHECKLIST -->' "docs/modules/$module.md" | head -1 | cut -d: -f1)
    sed -i.bak "${LINE}s/- \[ \]/- [x]/" "docs/modules/$module.md"
    rm -f "docs/modules/$module.md.bak"
done

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier TOTAL après modification 6 modules (scores actuels: tous 0/33)
# Calcul : SIRCOM (0→1) + SNUM (0→1) + SRH (0→1) + SIEP (0→1) + SAFI (0→1) + BGS (0→1)
#        = 1 + 1 + 1 + 1 + 1 + 1 = 6/198
grep -q "6/198" docs/synthese.md || { echo "❌ FAIL: Score incorrect"; cat docs/synthese.md; exit 1; }

# Rollback
rm -rf docs/modules
mv /tmp/modules-backup docs/modules
python3 scripts/calculate_scores.py

# Vérifier retour à 0/198 (score initial actuel)
grep -q "0/198" docs/synthese.md || { echo "❌ FAIL: Rollback incorrect"; exit 1; }

echo "✅ Scénario rollback OK"
