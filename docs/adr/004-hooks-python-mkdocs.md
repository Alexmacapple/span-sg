# ADR-004: Architecture hooks Python vs JavaScript

**Date**: 2025-10-08
**Statut**: ✅ Accepted
**Décideurs**: Alexandra, Alex
**Contexte**: Besoin d'extensibilité pour wrapping DSFR

## Contexte

Le thème mkdocs-dsfr nécessite wrapping manuel des tables avec `<div class="fr-table">`. Markdown tables générées ne contiennent pas ce wrapper, compromettant responsive et accessibilité.

**Besoin:** Mécanisme automatique pour post-traiter HTML généré.

## Décision

Utiliser **hooks Python MkDocs** plutôt que JavaScript côté client.

**Architecture:** `hooks/` directory avec hooks Python
```python
# hooks/dsfr_table_wrapper.py
def on_page_content(html: str, page, config, files) -> str:
    # Wrappe tables avec fr-table
    return modified_html
```

**Justification:** Build-time processing (Python) vs Runtime processing (JavaScript).

## Alternatives considérées

### Option A: JavaScript côté client (rejeté)
**Exemple:**
```html
<script>
document.querySelectorAll('table').forEach(table => {
    const wrapper = document.createElement('div');
    wrapper.className = 'fr-table';
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
});
</script>
```

**Avantages**: Simple à implémenter, pas de dépendances Python
**Inconvénients**:
- ❌ FOUC (Flash of Unstyled Content) - tables non wrappées visibles avant JS
- ❌ Performance runtime (chaque page load)
- ❌ Pas de fallback si JS désactivé
- ❌ Pas de tests unitaires faciles
- ❌ SEO impacté (crawlers voient HTML non transformé)

**Rejeté**: Accessibilité compromis + performance

### Option B: Plugin MkDocs custom (rejeté)
**Avantages**: Architecture propre, réutilisable
**Inconvénients**:
- ❌ Overhead développement plugin complet
- ❌ Maintenance séparée du projet
- ❌ Sur-ingénierie pour besoin simple

**Rejeté**: Complexity vs benefit

### Option C: Hooks Python MkDocs (choisi)
**Avantages**:
- ✅ Build-time processing (HTML final correct)
- ✅ Pas de FOUC (HTML déjà transformé)
- ✅ Tests unitaires simples (pytest)
- ✅ Type hints + coverage 100%
- ✅ SEO optimal (crawlers voient HTML final)
- ✅ Fallback natif (HTML statique)

**Inconvénients**:
- ⚠️ Nécessite Python dans build pipeline (déjà présent)

**Choisi**: Meilleure solution pour accessibilité + performance

## Conséquences

**Positives:**
- ✅ HTML généré conforme DSFR dès le build
- ✅ Tests unitaires exhaustifs (7 tests dsfr_table_wrapper, 6 tests title_cleaner)
- ✅ Coverage 100% hooks
- ✅ Type hints modernes (TYPE_CHECKING)
- ✅ Pas de dépendance JavaScript runtime

**Négatives:**
- ⚠️ Hooks doivent être testés (ajout charge développement)
- ⚠️ Regex complexes pour edge cases

**Standards adoptés:**
- Type hints complets (PEP 563)
- Docstrings Args/Returns/Example
- Tests coverage 100% obligatoire
- Black + Ruff linting

## Validation

**Critères:**
- [x] Hooks exécutés automatiquement lors du build
- [x] HTML final contient wrappers DSFR
- [x] Tests unitaires 100% coverage
- [x] Pas de FOUC sur site déployé
- [x] SEO vérifié (crawlers voient HTML transformé)

**Tests:**
```bash
pytest tests/test_hooks*.py --cov=hooks --cov-report=term-missing
# 13 tests, 100% coverage hooks DSFR
```

## Références

- Hooks implémentés: `dsfr_table_wrapper.py`, `title_cleaner.py`
- Tests: `tests/test_hooks*.py` (13 tests, 100% coverage)
- Documentation: `docs/dev/hooks-guide.md`
- MkDocs Plugins API: https://www.mkdocs.org/dev-guide/plugins/
- Commit: `762a474` (feat: hooks tests + type hints)
