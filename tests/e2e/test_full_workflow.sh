#!/usr/bin/env bash
set -euo pipefail

# Tests E2E SPAN SG - Workflow complet
# Usage: ./tests/e2e/test_full_workflow.sh

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "=== Tests E2E SPAN SG ==="
echo "Temp dir: $TEMP_DIR"
echo ""

# Compteurs
TESTS_RUN=0
TESTS_PASS=0
TESTS_FAIL=0

run_test() {
    local name=$1
    local command=$2
    TESTS_RUN=$((TESTS_RUN + 1))
    echo -n "Test $TESTS_RUN: $name... "
    if eval "$command" > "$TEMP_DIR/test_$TESTS_RUN.log" 2>&1; then
        echo "✅ PASS"
        TESTS_PASS=$((TESTS_PASS + 1))
    else
        echo "❌ FAIL"
        cat "$TEMP_DIR/test_$TESTS_RUN.log"
        TESTS_FAIL=$((TESTS_FAIL + 1))
    fi
}

# Test 1 : Backup module SIRCOM
run_test "Backup module SIRCOM" \
    "cp docs/modules/sircom.md $TEMP_DIR/sircom-backup.md"

# Test 2 : Modifier SIRCOM (cocher 1 point)
run_test "Modifier SIRCOM (cocher point 7)" \
    "sed -i '' 's/- \[ \] Budget annuel dédié/- [x] Budget annuel dédié/' docs/modules/sircom.md"

# Test 3 : Recalculer scores
run_test "Recalculer scores" \
    "python3 scripts/calculate_scores.py"

# Test 4 : Vérifier score SIRCOM augmenté
run_test "Vérifier score SIRCOM = 7/31" \
    "grep -q '| SIRCOM | 7/31' docs/synthese.md"

# Test 5 : Build site MkDocs
run_test "Build site MkDocs" \
    "mkdocs build --site-dir $TEMP_DIR/site"

# Test 6 : Vérifier HTML généré
run_test "Vérifier index.html présent" \
    "test -f $TEMP_DIR/site/index.html"

run_test "Vérifier page SIRCOM générée" \
    "test -f $TEMP_DIR/site/modules/sircom/index.html"

# Test 7 : Générer PDF
run_test "Générer PDF" \
    "mkdocs build --config-file mkdocs-pdf.yml --site-dir $TEMP_DIR/pdf-site"

run_test "Vérifier PDF généré" \
    "test -f $TEMP_DIR/pdf-site/pdf/document.pdf"

# Test 8 : Vérifier contenu PDF (au moins 50 KB)
run_test "Vérifier taille PDF > 50KB" \
    "[[ \$(stat -f%z $TEMP_DIR/pdf-site/pdf/document.pdf) -gt 51200 ]]"

# Test 9 : Restaurer SIRCOM
run_test "Restaurer SIRCOM" \
    "mv $TEMP_DIR/sircom-backup.md docs/modules/sircom.md"

# Test 10 : Re-calculer scores (retour état initial)
run_test "Re-calculer scores après restauration" \
    "python3 scripts/calculate_scores.py"

# Test 11 : Vérifier score SIRCOM restauré
run_test "Vérifier score SIRCOM = 6/31 (restauré)" \
    "grep -q '| SIRCOM | 6/31' docs/synthese.md"

# Résumé
echo ""
echo "=== Résumé E2E ==="
echo "Tests exécutés : $TESTS_RUN"
echo "Tests réussis  : $TESTS_PASS"
echo "Tests échoués  : $TESTS_FAIL"

if [ $TESTS_FAIL -eq 0 ]; then
    echo "✅ Tous les tests E2E passent"
    exit 0
else
    echo "❌ $TESTS_FAIL test(s) échoué(s)"
    exit 1
fi
