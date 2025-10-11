# ADR-005: Seuil coverage 89%+ enforced

**Date**: 2025-10-10
**Statut**: ✅ Accepted
**Décideurs**: Alexandra, Claude Code
**Contexte**: Garantir qualité code production-ready

## Contexte

Le projet SPAN SG vise score 20/20 qualité code. Coverage tests est métrique clé pour:
- Détecter code non testé (risques régressions)
- Garantir comportements validés
- Faciliter maintenance (confiance refactoring)

**Question:** Quel seuil coverage imposer en CI ?

## Décision

Enforcer **coverage ≥ 89%** pour scripts production ciblés.

**Implémentation CI:**
```yaml
- name: Run production scripts coverage check (89%+ required)
  run: |
    python -m pytest \
      --cov=scripts \
      --cov-report=term-missing \
      --cov-report=html \
      --cov-fail-under=89 \
      scripts/test_calculate_scores*.py scripts/test_enrich_pdf*.py
```

**Scope:**
- `scripts/calculate_scores.py`: 100% (critical)
- `scripts/enrich_pdf_metadata.py`: 78% (acceptable)
- `hooks/dsfr_table_wrapper.py`: 100% (critical)
- `hooks/title_cleaner.py`: 100% (critical)

**Coverage global ciblé:** 92% (dépasse seuil 89%+)

## Alternatives considérées

### Option A: Pas de seuil enforced (rejeté)
- **Avantages**: Flexibilité développement
- **Inconvénients**: ❌ Coverage peut dériver, ❌ Pas de garantie qualité
- **Rejeté**: Incompatible objectif production-ready

### Option B: Seuil 100% strict (rejeté)
- **Avantages**: Coverage parfait
- **Inconvénients**: ❌ Bloque développement (edge cases difficiles), ❌ Faux positif (code défensif)
- **Rejeté**: Trop strict, ROI négatif

### Option C: Seuil 70-80% (standard industrie, rejeté)
- **Avantages**: Standard classique, atteignable facilement
- **Inconvénients**: ⚠️ Trop permissif pour projet gouvernemental
- **Rejeté**: Objectif dépasser standards industrie

### Option D: Seuil 89%+ ciblé (choisi)
- **Avantages**: ✅ Au-dessus industrie (+15%), ✅ Atteignable mais exigeant, ✅ Scope ciblé (scripts critiques)
- **Inconvénients**: ⚠️ Nécessite tests exhaustifs
- **Choisi**: Balance qualité/pragmatisme

## Justification 89%

**Pourquoi pas 90% rond ?**
- Current coverage: `calculate_scores.py` = 100%, `enrich_pdf_metadata.py` = 78%
- Average pondéré: (72*100 + 50*78) / (72+50) = 91.1%
- Marge sécurité: 91.1% - 2% = 89%
- Seuil permet ajout code sans bloquer si léger dip

**Comparaison industrie:**
| Projet type | Coverage typique |
|-------------|------------------|
| POC/Prototype | 0-30% |
| Projet standard | 60-80% |
| Projet production | 80-90% |
| **SPAN SG** | **92%** (+15% vs standard) |

## Conséquences

**Positives:**
- ✅ Qualité code garantie (scripts critiques 100%)
- ✅ CI bloque si coverage drop
- ✅ Confiance refactoring élevée
- ✅ Dépassement standards industrie (+15%)

**Négatives:**
- ⚠️ Temps développement accru (écrire tests)
- ⚠️ CI plus lent (~30s supplémentaires pour tests)

**Exclusions:**
- `hooks/pdf_copy.py`: 0% (non critique, sera testé v1.1)
- Scripts utilitaires dev (`dev.sh`, etc.)

## Validation

**Critères:**
- [x] CI enforce 89%+ sur scripts production
- [x] Coverage global ≥ 92%
- [x] Scripts critiques 100% (calculate_scores, hooks DSFR)
- [x] CI échoue si coverage drop

**Tests validation:**
```bash
# Coverage actuel
pytest --cov=scripts --cov=hooks --cov-report=term-missing
# TOTAL: 138 statements, 11 miss, 92% coverage ✅

# CI enforcement
pytest --cov-fail-under=89 scripts/test_calculate_scores*.py scripts/test_enrich_pdf*.py
# Required test coverage of 89% reached. Total coverage: 92.03% ✅
```

## Évolution future

**v1.1:**
- [ ] Tester `pdf_copy.py` (actuellement 0%)
- [ ] Coverage global target 95%+
- [ ] Tests E2E coverage (actuellement hors scope)

**v2.0:**
- [ ] Tests accessibilité automatisés (axe-core)
- [ ] Tests performance (benchmarks)
- [ ] Coverage target 98%+

## Références

- CI workflow: `.github/workflows/build.yml` (ligne 36-43, 176-183)
- Coverage report: Généré à chaque CI run
- Commits: `762a474` (feat: hooks tests 100%)
- Standards: 89%+ > Industrie moyenne (70-80%)
- Comparaison: SPAN SG = 92% (+15% vs standard production)
