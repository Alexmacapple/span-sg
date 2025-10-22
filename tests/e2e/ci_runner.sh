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

# Fonction helper pour exécuter un scénario (parallélisation)
run_scenario() {
    local scenario="$1"
    local log_file="$REPORT_DIR/${scenario%.sh}.log"

    # Restaurer état propre avant chaque test (évite fuites d'état)
    git checkout -- docs/modules/*.md docs/synthese.md 2>/dev/null || true

    if bash "$TESTS_DIR/$scenario" > "$log_file" 2>&1; then
        echo "✅ PASS: $scenario"
        return 0
    else
        local exit_code=$?
        if [ $exit_code -eq 77 ]; then
            echo "⏭️  SKIP: $scenario"
            return 77
        else
            echo "❌ FAIL: $scenario"
            return 1
        fi
    fi
}

export -f run_scenario
export TESTS_DIR REPORT_DIR

# Exécuter scénarios en parallèle (3 workers max)
# Alternative GNU parallel si disponible: parallel -j 3 --halt soon,fail=1 run_scenario ::: "${SCENARIOS[@]}"
printf "%s\n" "${SCENARIOS[@]}" | xargs -n 1 -P 3 -I {} bash -c 'run_scenario "{}"'
PARALLEL_EXIT=$?

# Collecter résultats depuis logs (car xargs agrège stdout)
for scenario in "${SCENARIOS[@]}"; do
    LOG_FILE="$REPORT_DIR/${scenario%.sh}.log"
    if [ -f "$LOG_FILE" ]; then
        # Détecter succès par message de fin de scénario
        if grep -qE "(✅|OK|PASS)" "$LOG_FILE"; then
            PASSED=$((PASSED + 1))
        # Détecter skip par code exit 77 ou message SKIP
        elif grep -qE "(SKIP|skipped)" "$LOG_FILE"; then
            SKIPPED=$((SKIPPED + 1))
        # Sinon considérer comme échec
        else
            FAILED=$((FAILED + 1))
        fi
    else
        # Pas de log = échec
        FAILED=$((FAILED + 1))
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
