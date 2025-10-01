#!/usr/bin/env bash
# Scénario : Modifier 3 modules simultanément

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Modification multi-modules"

# Backup
cp docs/modules/{sircom,snum,srh}.md /tmp/

# Modifier SIRCOM (cocher point 8)
sed -i 's/- \[ \] Planification pluriannuelle/- [x] Planification pluriannuelle/' docs/modules/sircom.md

# Modifier SNUM (cocher point 1)
sed -i '0,/- \[ \].*<!-- DINUM -->/s//- [x] Stratégie numérique publiée <!-- DINUM -->/' docs/modules/snum.md

# Modifier SRH (cocher point 1)
sed -i '0,/- \[ \].*<!-- DINUM -->/s//- [x] Stratégie numérique publiée <!-- DINUM -->/' docs/modules/srh.md

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier scores
grep -q "| SIRCOM | 7/31" docs/synthese.md || { echo "FAIL: SIRCOM"; exit 1; }
grep -q "| SNUM | 1/31" docs/synthese.md || { echo "FAIL: SNUM"; exit 1; }
grep -q "| SRH | 1/31" docs/synthese.md || { echo "FAIL: SRH"; exit 1; }
# TOTAL = SIRCOM (6→7) + SNUM (0→1) + SRH (0→1) + autres (0) = 7+1+1 = 9/186
grep -q "| \*\*TOTAL\*\* | \*\*9/186" docs/synthese.md || { echo "FAIL: TOTAL"; exit 1; }

# Restaurer
mv /tmp/{sircom,snum,srh}.md docs/modules/
python3 scripts/calculate_scores.py

echo "✅ Scénario multi-modules OK"
