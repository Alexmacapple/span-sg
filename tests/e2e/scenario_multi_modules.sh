#!/usr/bin/env bash
# Scénario : Modifier 3 modules simultanément

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Modification multi-modules"

# Backup
cp docs/modules/{sircom,snum,srh}.md /tmp/

# Modifier SIRCOM (cocher "Budget annuel dédié" - point 7 non coché) avec awk
awk '/- \[ \] Budget annuel/ && !done {sub(/- \[ \]/, "- [x]"); done=1} {print}' docs/modules/sircom.md > /tmp/sircom.tmp
mv /tmp/sircom.tmp docs/modules/sircom.md

# Modifier SNUM (cocher point 1) avec awk
awk '/- \[ \].* DINUM/ && !done {sub(/- \[ \]/, "- [x]"); done=1} {print}' docs/modules/snum.md > /tmp/snum.tmp
mv /tmp/snum.tmp docs/modules/snum.md

# Modifier SRH (cocher point 1) avec awk
awk '/- \[ \].* DINUM/ && !done {sub(/- \[ \]/, "- [x]"); done=1} {print}' docs/modules/srh.md > /tmp/srh.tmp
mv /tmp/srh.tmp docs/modules/srh.md

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier scores
grep -q "| SIRCOM | 8/31" docs/synthese.md || { echo "FAIL: SIRCOM"; exit 1; }
grep -q "| SNUM | 1/31" docs/synthese.md || { echo "FAIL: SNUM"; exit 1; }
grep -q "| SRH | 1/31" docs/synthese.md || { echo "FAIL: SRH"; exit 1; }
# TOTAL = SIRCOM (7→8) + SNUM (0→1) + SRH (0→1) + autres (0) = 8+1+1 = 10/186
grep -q "| \*\*TOTAL\*\* | \*\*10/186" docs/synthese.md || { echo "FAIL: TOTAL"; exit 1; }

# Restaurer
mv /tmp/{sircom,snum,srh}.md docs/modules/
python3 scripts/calculate_scores.py

echo "✅ Scénario multi-modules OK"
