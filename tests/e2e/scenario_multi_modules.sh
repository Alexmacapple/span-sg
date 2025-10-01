#!/usr/bin/env bash
# Scénario : Modifier 3 modules simultanément

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Modification multi-modules"

# Backup
cp docs/modules/{sircom,snum,srh}.md /tmp/

# Modifier SIRCOM (cocher "Budget annuel dédié") - sed avec numéro ligne
LINE=$(grep -n '^- \[ \] Budget annuel' docs/modules/sircom.md | head -1 | cut -d: -f1)
sed -i.bak "${LINE}s/- \[ \]/- [x]/" docs/modules/sircom.md
rm -f docs/modules/sircom.md.bak

# Modifier SNUM (cocher première checkbox DINUM) - sed avec numéro ligne
LINE=$(grep -n '^- \[ \].*<!-- DINUM -->' docs/modules/snum.md | head -1 | cut -d: -f1)
sed -i.bak "${LINE}s/- \[ \]/- [x]/" docs/modules/snum.md
rm -f docs/modules/snum.md.bak

# Modifier SRH (cocher première checkbox DINUM) - sed avec numéro ligne
LINE=$(grep -n '^- \[ \].*<!-- DINUM -->' docs/modules/srh.md | head -1 | cut -d: -f1)
sed -i.bak "${LINE}s/- \[ \]/- [x]/" docs/modules/srh.md
rm -f docs/modules/srh.md.bak

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
