#!/usr/bin/env bash
# Scénario : Modifier 3 modules simultanément

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Modification multi-modules"

# Backup
cp docs/modules/{sircom,snum,srh}.md /tmp/

# Modifier SIRCOM (cocher premier point non coché) - sed avec numéro ligne
LINE=$(grep -n '^- \[ \].*<!-- CHECKLIST -->' docs/modules/sircom.md | head -1 | cut -d: -f1)
sed -i.bak "${LINE}s/- \[ \]/- [x]/" docs/modules/sircom.md
rm -f docs/modules/sircom.md.bak

# Modifier SNUM (cocher première checkbox CHECKLIST) - sed avec numéro ligne
LINE=$(grep -n '^- \[ \].*<!-- CHECKLIST -->' docs/modules/snum.md | head -1 | cut -d: -f1)
sed -i.bak "${LINE}s/- \[ \]/- [x]/" docs/modules/snum.md
rm -f docs/modules/snum.md.bak

# Modifier SRH (cocher première checkbox CHECKLIST) - sed avec numéro ligne
LINE=$(grep -n '^- \[ \].*<!-- CHECKLIST -->' docs/modules/srh.md | head -1 | cut -d: -f1)
sed -i.bak "${LINE}s/- \[ \]/- [x]/" docs/modules/srh.md
rm -f docs/modules/srh.md.bak

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier scores (scores actuels: SIRCOM 0/33, SNUM 0/33, SRH 0/33)
# SIRCOM passe à 1/33
grep -A 5 "^\s*SIRCOM\s*$" docs/synthese.md | grep -q "1/33 (" || { echo "FAIL: SIRCOM"; exit 1; }
# SNUM passe à 1/33
grep -A 5 "^\s*SNUM\s*$" docs/synthese.md | grep -q "1/33 (" || { echo "FAIL: SNUM"; exit 1; }
# SRH passe à 1/33
grep -A 5 "^\s*SRH\s*$" docs/synthese.md | grep -q "1/33 (" || { echo "FAIL: SRH"; exit 1; }
# TOTAL = SIRCOM (0→1) + SNUM (0→1) + SRH (0→1) + autres (0) = 3/198
grep -q "3/198 (" docs/synthese.md || { echo "FAIL: TOTAL"; exit 1; }

# Restaurer
mv /tmp/{sircom,snum,srh}.md docs/modules/
python3 scripts/calculate_scores.py

echo "✅ Scénario multi-modules OK"
