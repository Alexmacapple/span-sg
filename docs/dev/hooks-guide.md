# Guide Développeur - Hooks MkDocs

Guide pratique pour créer et maintenir des hooks MkDocs personnalisés.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-11

---

## Introduction

Les hooks MkDocs permettent d'intercepter et modifier le HTML généré à différentes étapes du build. Le projet SPAN SG utilise des hooks Python pour garantir la conformité DSFR.

**Hooks actuels:**
- `dsfr_table_wrapper.py`: Wrappe tables avec `<div class="fr-table">`
- `title_cleaner.py`: Nettoie titres HTML redondants
- `pdf_copy.py`: Copie PDF dans site/ (non testé)

---

## Architecture hooks/

```
hooks/
├── __init__.py                # Vide (marker Python package)
├── dsfr_table_wrapper.py      # ✅ 100% coverage, 7 tests
├── title_cleaner.py            # ✅ 100% coverage, 6 tests
└── pdf_copy.py                 # ❌ 0% coverage, non testé
```

---

## Cycle de vie hooks MkDocs

### Hooks disponibles

```python
def on_pre_build(config):
    """Avant démarrage build."""
    pass

def on_files(files, config):
    """Après détection fichiers, avant processing."""
    pass

def on_page_markdown(markdown, page, config, files):
    """Après lecture Markdown, avant conversion HTML."""
    return markdown

def on_page_content(html, page, config, files):
    """Après conversion Markdown → HTML (body seulement)."""
    return html

def on_post_page(output, page, config):
    """Après génération HTML complète (head + body)."""
    return output

def on_post_build(config):
    """Après build complet."""
    pass
```

### Hooks utilisés par SPAN SG

**`on_page_content`** (dsfr_table_wrapper.py):
- Moment: Après Markdown → HTML
- Contenu: Body HTML uniquement (sans `<head>`)
- Usage: Modifier contenu page (tables, listes, etc.)

**`on_post_page`** (title_cleaner.py):
- Moment: Après génération HTML complète
- Contenu: HTML complet (`<html>`, `<head>`, `<body>`)
- Usage: Modifier éléments globaux (title, meta, scripts)

---

## Configuration

### mkdocs-dsfr.yml

```yaml
hooks:
  - hooks/dsfr_table_wrapper.py
  - hooks/title_cleaner.py

# Hooks exécutés dans l'ordre listé
# Chaque hook doit retourner HTML modifié
```

---

## Créer un nouveau hook

### Template de base

```python
"""Hook MkDocs pour [description courte].

Date: YYYY-MM-DD
Contexte: [Pourquoi ce hook existe]
Solution: [Que fait le hook]
"""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page
    from mkdocs.config import Config
    from mkdocs.structure.files import Files


def on_page_content(
    html: str, page: "Page", config: "Config", files: "Files"
) -> str:
    """
    Hook appelé après conversion Markdown → HTML.

    [Description détaillée du comportement]

    Contexte:
        [Problème résolu par ce hook]
        [Architecture technique]

    Args:
        html: Contenu HTML de la page
        page: Instance MkDocs Page (non utilisé si pas nécessaire)
        config: Configuration MkDocs (non utilisé si pas nécessaire)
        files: Collection fichiers (non utilisé si pas nécessaire)

    Returns:
        HTML modifié avec [transformation appliquée]

    Example:
        Input:  '<before>content</before>'
        Output: '<after>content</after>'

    Note:
        [Points d'attention, comportements spéciaux, limitations]
    """
    # Pattern regex pour détecter éléments
    pattern = r'<element>(.*?)</element>'

    # Fonction replacement
    def transform(match) -> str:
        content = match.group(1)
        return f'<wrapper>{content}</wrapper>'

    # Appliquer transformation
    html = re.sub(pattern, transform, html, flags=re.DOTALL)

    return html
```

### Exemple complet: link_external.py

```python
"""Hook MkDocs pour ajouter target=_blank aux liens externes."""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page
    from mkdocs.config import Config
    from mkdocs.structure.files import Files


def on_page_content(
    html: str, page: "Page", config: "Config", files: "Files"
) -> str:
    """
    Ajoute target="_blank" et rel="noopener" aux liens externes.

    Contexte:
        Liens externes doivent s'ouvrir dans nouvel onglet (UX)
        et avoir rel="noopener" (sécurité).

    Args:
        html: Contenu HTML de la page
        page: Instance MkDocs Page
        config: Configuration MkDocs
        files: Collection fichiers

    Returns:
        HTML avec liens externes modifiés

    Example:
        Input:  '<a href="https://example.com">Link</a>'
        Output: '<a href="https://example.com" target="_blank" rel="noopener">Link</a>'
    """
    # Pattern: liens http(s) sans target déjà défini
    pattern = r'<a\s+href="(https?://[^"]+)"(?![^>]*target=)([^>]*)>'

    def add_target(match) -> str:
        url = match.group(1)
        attrs = match.group(2)
        return f'<a href="{url}" target="_blank" rel="noopener"{attrs}>'

    html = re.sub(pattern, add_target, html)

    return html
```

---

## Tests obligatoires

### Template test

Créer `tests/test_hooks_mon_hook.py`:

```python
"""Tests unitaires pour hooks/mon_hook.py"""

from hooks.mon_hook import on_page_content


def test_cas_nominal():
    """Vérifie comportement nominal."""
    html = "<element>content</element>"
    result = on_page_content(html, None, None, None)
    assert "<wrapper>" in result
    assert "content" in result


def test_plusieurs_elements():
    """Vérifie traitement plusieurs éléments."""
    html = "<element>A</element><element>B</element>"
    result = on_page_content(html, None, None, None)
    assert result.count("<wrapper>") == 2


def test_deja_traite():
    """Vérifie idempotence (pas de double traitement)."""
    html = "<wrapper><element>content</element></wrapper>"
    result = on_page_content(html, None, None, None)
    # Ne doit pas re-wrapper
    assert result.count("<wrapper>") == 1


def test_html_vide():
    """Vérifie comportement avec HTML vide."""
    html = ""
    result = on_page_content(html, None, None, None)
    assert result == ""


def test_pas_element():
    """Vérifie HTML sans élément ciblé (inchangé)."""
    html = "<div>Pas d'élément ciblé</div>"
    result = on_page_content(html, None, None, None)
    assert result == html


def test_avec_attributs():
    """Vérifie préservation attributs."""
    html = '<element id="test" class="foo">content</element>'
    result = on_page_content(html, None, None, None)
    assert 'id="test"' in result
    assert 'class="foo"' in result


def test_multiligne():
    """Vérifie traitement contenu multiligne."""
    html = """<element>
        <div>
            Contenu
            multiligne
        </div>
    </element>"""
    result = on_page_content(html, None, None, None)
    assert "<wrapper>" in result
```

### Exécution tests

```bash
# Tests hooks spécifiques
pytest tests/test_hooks_mon_hook.py -v

# Coverage 100% requis
pytest tests/test_hooks_mon_hook.py --cov=hooks.mon_hook --cov-report=term-missing

# Tous tests hooks
pytest tests/test_hooks*.py -v
```

**Exigences:**
- ✅ Coverage 100% du hook
- ✅ Minimum 5 scénarios (nominal, limites, erreurs, idempotence, edge cases)
- ✅ Black + Ruff conformes

---

## Bonnes pratiques

### 1. Regex compilés (performance)

```python
# ✅ BON: Compilé une fois (module-level)
PATTERN = re.compile(r'<table[^>]*>.*?</table>', re.DOTALL)

def on_page_content(html: str, page, config, files) -> str:
    return PATTERN.sub(replacement, html)

# ❌ MAUVAIS: Compilé à chaque appel
def on_page_content(html: str, page, config, files) -> str:
    return re.sub(r'<table[^>]*>.*?</table>', replacement, html, flags=re.DOTALL)
```

### 2. Type hints modernes (PEP 563)

```python
# ✅ BON: TYPE_CHECKING (pas d'import runtime)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page

def on_page_content(html: str, page: "Page", config, files) -> str:
    pass

# ❌ MAUVAIS: Import direct (overhead runtime, circular imports)
from mkdocs.structure.pages import Page

def on_page_content(html: str, page: Page, config, files) -> str:
    pass
```

### 3. Lookahead/lookbehind (éviter double traitement)

```python
# ✅ BON: Lookahead négatif (ne matche pas si déjà wrappé)
pattern = r'(?<!<div class="fr-table">)\s*(<table[^>]*>.*?</table>)'
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Pas déjà précédé par wrapper

# ❌ MAUVAIS: Pas de vérification (risque double wrapping)
pattern = r'(<table[^>]*>.*?</table>)'
```

### 4. Flags regex appropriés

```python
# re.DOTALL: . matche newlines (tables/divs multilignes)
html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# re.IGNORECASE: Case-insensitive (tags HTML)
html = re.sub(r'<TABLE>', '<table>', html, flags=re.IGNORECASE)

# re.MULTILINE: ^ et $ matchent début/fin lignes
html = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
```

### 5. Docstrings complètes

Structure docstring obligatoire:
- Description courte (1 ligne)
- Description détaillée (paragraphe)
- Contexte (pourquoi ce hook existe)
- Args avec types
- Returns avec type
- Example avec Input/Output
- Note (limitations, cas spéciaux)

---

## Debugging

### Logs

```python
import logging

logger = logging.getLogger(__name__)

def on_page_content(html: str, page, config, files) -> str:
    logger.debug(f"Processing: {page.file.src_path}")
    logger.debug(f"HTML length: {len(html)} chars")

    # ... transformation

    logger.debug(f"Transformed: {len(result)} chars")
    return result
```

**Activer logs:**
```bash
mkdocs build --verbose
```

### Tests locaux

```bash
# Build avec hooks actifs
mkdocs build --config-file mkdocs-dsfr.yml --strict

# Serveur local hot-reload
mkdocs serve --config-file mkdocs-dsfr.yml

# Vérifier HTML généré
grep -r "fr-table" site/
```

### Désactiver hook temporairement

```yaml
# mkdocs-dsfr.yml
hooks:
  # - hooks/dsfr_table_wrapper.py  # Commenté pour debug
  - hooks/title_cleaner.py
```

---

## Checklist ajout hook

### Phase 1: Développement
- [ ] Fichier hook créé dans `hooks/mon_hook.py`
- [ ] Type hints complets (TYPE_CHECKING)
- [ ] Docstring complète (Args/Returns/Example/Note/Contexte)
- [ ] Regex optimisé (compiled, lookahead si besoin)
- [ ] Tests unitaires créés `tests/test_hooks_mon_hook.py`
- [ ] 5+ scénarios de test (nominal, limites, erreurs, idempotence)

### Phase 2: Validation
- [ ] Coverage 100% du hook
- [ ] Black formatter passe (`black hooks/`)
- [ ] Ruff linter passe (`ruff check hooks/`)
- [ ] Tests unitaires passent (`pytest tests/test_hooks_mon_hook.py`)
- [ ] Build local réussit (`mkdocs build --config-file mkdocs-dsfr.yml`)

### Phase 3: Intégration
- [ ] Hook ajouté à `mkdocs-dsfr.yml` section `hooks:`
- [ ] Documentation ajoutée dans `docs/dev/hooks-guide.md`
- [ ] API Reference mise à jour (`docs/dev/api-reference.md`)
- [ ] Commit avec message explicatif

### Phase 4: CI
- [ ] CI passe (Black, Ruff, pytest, coverage 89%+)
- [ ] GitHub Pages déploie correctement
- [ ] Validation visuelle site déployé

---

## Checklist modification hook

### Phase 1: Modifications
- [ ] Tests existants toujours passent
- [ ] Nouveaux tests pour nouvelle logique
- [ ] Coverage maintenu 100%

### Phase 2: Documentation
- [ ] Docstring mise à jour
- [ ] Exemple mis à jour si changement comportement
- [ ] CHANGELOG.md entry créée

### Phase 3: Validation
- [ ] Black + Ruff passent
- [ ] Build local réussit
- [ ] CI passe

---

## Erreurs fréquentes

### Erreur 1: Import circulaire

```python
# ❌ MAUVAIS
from mkdocs.structure.pages import Page  # Circular import!

# ✅ BON
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mkdocs.structure.pages import Page
```

### Erreur 2: Regex non-greedy oublié

```python
# ❌ MAUVAIS: Greedy (matche tout jusqu'au dernier </table>)
pattern = r'<table>(.*)</table>'

# ✅ BON: Non-greedy (matche table par table)
pattern = r'<table>(.*?)</table>'
```

### Erreur 3: Oublier flags re.DOTALL

```python
# ❌ MAUVAIS: . ne matche pas \n (tables multilignes échouent)
re.sub(r'<table>.*?</table>', replacement, html)

# ✅ BON: . matche tout y compris \n
re.sub(r'<table>.*?</table>', replacement, html, flags=re.DOTALL)
```

### Erreur 4: Modifier HTML sans retourner

```python
# ❌ MAUVAIS: Modifie mais ne retourne pas
def on_page_content(html: str, page, config, files) -> str:
    html.replace('<old>', '<new>')  # str.replace ne modifie pas en place!
    # Manque: return html

# ✅ BON
def on_page_content(html: str, page, config, files) -> str:
    html = html.replace('<old>', '<new>')
    return html
```

---

## Références

**Documentation MkDocs:**
- [Developing Plugins](https://www.mkdocs.org/user-guide/plugins/)
- [Plugin API Reference](https://www.mkdocs.org/dev-guide/plugins/)

**Hooks SPAN SG:**
- `hooks/dsfr_table_wrapper.py`: Exemple complet avec tests
- `hooks/title_cleaner.py`: Exemple simple et efficace
- `tests/test_hooks*.py`: Exemples tests exhaustifs

**Standards:**
- PEP 8: Style guide Python
- PEP 484: Type hints
- PEP 563: Postponed evaluation (TYPE_CHECKING)

**Outils:**
- Black: Code formatter
- Ruff: Linter rapide
- pytest: Framework tests
- pytest-cov: Coverage measurement
