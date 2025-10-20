#!/usr/bin/env bash
# Orchestrateur tests E2E pour CI
# Exécute tous les scénarios, capture logs, génère rapport HTML

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "🧪 Exécution Tests E2E CI"
echo ""

TESTS_DIR="tests/e2e"
REPORT_DIR="$TESTS_DIR/reports"
mkdir -p "$REPORT_DIR"

# Liste des scénarios à exécuter
SCENARIOS=(
    "test_full_workflow.sh"
    "scenario_multi_modules.sh"
    "scenario_erreur_perimetre.sh"
    "scenario_erreur_markdown.sh"
    "scenario_performance.sh"
    "scenario_pdf_complet.sh"
    "scenario_rollback.sh"
    "scenario_preview_http.sh"
    "scenario_frontmatter.sh"
)

FAILED=0
PASSED=0
SKIPPED=0

for scenario in "${SCENARIOS[@]}"; do
    # Restaurer état propre avant chaque test (évite fuites d'état)
    git checkout -- docs/modules/*.md docs/synthese.md 2>/dev/null || true

    echo "▶ Test: $scenario"

    LOG_FILE="$REPORT_DIR/${scenario%.sh}.log"

    if bash "$TESTS_DIR/$scenario" > "$LOG_FILE" 2>&1; then
        echo "  ✅ PASS"
        PASSED=$((PASSED + 1))
    else
        EXIT_CODE=$?
        if [ $EXIT_CODE -eq 77 ]; then
            echo "  ⏭️  SKIP"
            SKIPPED=$((SKIPPED + 1))
        else
            echo "  ❌ FAIL"
            FAILED=$((FAILED + 1))
        fi
    fi
done

echo ""
echo "=== Résumé E2E ==="
echo "✅ Passés   : $PASSED"
echo "❌ Échoués  : $FAILED"
echo "⏭️  Skippés : $SKIPPED"

# Générer rapport HTML
echo ""
echo "📊 Génération rapport HTML..."
python3 "$TESTS_DIR/generate_report.py" "$REPORT_DIR"

if [ $FAILED -gt 0 ]; then
    echo ""
    echo "❌ $FAILED test(s) E2E échoué(s)"
    exit 1
fi

echo ""
echo "✅ Tous les tests E2E passent"
exit 0
