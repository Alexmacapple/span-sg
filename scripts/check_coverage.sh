#!/bin/bash
# Vérification coverage scripts production (89%+ requis)
# Usage: ./scripts/check_coverage.sh

echo "🔍 Vérification coverage scripts production..."

python3 -m pytest \
  --cov=scripts \
  --cov-report=term-missing \
  --cov-report=html \
  --cov-fail-under=89 \
  scripts/test_calculate_scores*.py scripts/test_enrich_pdf*.py

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "✅ Coverage 89%+ atteint !"
    echo "   Rapport HTML : tests/htmlcov/index.html"
else
    echo ""
    echo "❌ Coverage < 89%"
    echo "   Voir lignes manquantes ci-dessus"
    echo "   Rapport HTML : tests/htmlcov/index.html"
    exit 1
fi
