#!/usr/bin/env bash
# Runner tous tests E2E

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Runner Tests E2E SPAN SG ==="
echo ""

TESTS=(
    "tests/e2e/test_full_workflow.sh"
    "tests/e2e/scenario_multi_modules.sh"
    "tests/e2e/scenario_erreur_perimetre.sh"
    "tests/e2e/scenario_erreur_markdown.sh"
    "tests/e2e/scenario_performance.sh"
    "tests/e2e/scenario_pdf_complet.sh"
    "tests/e2e/scenario_rollback.sh"
    "tests/e2e/scenario_preview_http.sh"
    "tests/e2e/scenario_frontmatter.sh"
)

PASS=0
FAIL=0
SKIP=0

for test in "${TESTS[@]}"; do
    chmod +x "$test"
    echo "Exécution : $test"
    if "$test"; then
        PASS=$((PASS + 1))
    else
        EXIT_CODE=$?
        if [ $EXIT_CODE -eq 77 ]; then
            SKIP=$((SKIP + 1))
        else
            FAIL=$((FAIL + 1))
        fi
    fi
    echo ""
done

echo "=== Résumé Global E2E ==="
echo "Tests réussis : $PASS"
echo "Tests échoués : $FAIL"
echo "Tests skippés : $SKIP"

if [ $FAIL -eq 0 ]; then
    echo "✅ Tous les tests E2E passent"
    exit 0
else
    echo "❌ $FAIL test(s) échoué(s)"
    exit 1
fi
