# API Reference - Scripts et Hooks

Documentation technique complète des scripts Python et hooks MkDocs du projet SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-11

---

## Scripts Production

### calculate_scores.py

Calcul automatique des scores SPAN par module (31 points DINUM).

**Localisation:** `scripts/calculate_scores.py`
**Coverage:** 100%
**Tests:** `scripts/test_calculate_scores*.py` (26 tests)

**Usage:**
```bash
python scripts/calculate_scores.py
# Génère: docs/synthese.md
# Exit code: 0 (succès) ou 2 (erreur périmètre)
```

**Workflow CI:**
```yaml
- name: Calculate SPAN scores
  run: python scripts/calculate_scores.py
```

---

#### Constantes

```python
CHECK_TAG = "DINUM"                    # Tag marqueur des 31 points officiels
FENCE_RE = re.compile(r"```.*?```", re.S)  # Regex code fences
BOX_RE = re.compile(r"- \[(x|X| )\].*?<!--\s*DINUM\s*-->")  # Regex checkboxes
```

---

#### `load_text(p: Path) -> str`

Charge le contenu d'un module Markdown en excluant les blocs de code.

**Args:**
- `p` (Path): Chemin vers fichier .md du module

**Returns:**
- `str`: Contenu Markdown sans code fences (```...```)

**Justification:**
Les blocs de code peuvent contenir des checkboxes exemples qui ne doivent pas être comptées.

**Example:**
```python
from pathlib import Path
from scripts.calculate_scores import load_text

content = load_text(Path("docs/modules/sircom.md"))
# Returns: Markdown sans code blocks
```

**Tests:**
- `test_removes_code_fences()`: Vérifie exclusion code blocks

---

#### `score_module(p: Path) -> tuple[int, int]`

Compte les cases cochées parmi les 31 points DINUM d'un module.

**Args:**
- `p` (Path): Chemin vers module (docs/modules/*.md)

**Returns:**
- `tuple[int, int]`: (checked, total)
  - `checked`: Nombre de cases cochées `[x]`
  - `total`: Nombre total de cases avec `<!-- DINUM -->`

**Validation:**
- `total` doit être 0 (module vide) ou 31 (périmètre complet)
- Sinon erreur détectée par `generate_summary()`

**Example:**
```python
from pathlib import Path
from scripts.calculate_scores import score_module

checked, total = score_module(Path("docs/modules/sircom.md"))
# Returns: (24, 31) pour SIRCOM actuel
# Pourcentage: 24/31 = 77.4%
```

**Format attendu dans .md:**
```markdown
- [x] Point validé <!-- DINUM -->
- [ ] Point non validé <!-- DINUM -->
```

**Tests:**
- `test_module_0_of_31()`: Module vide
- `test_module_6_of_31_sircom()`: Module partiel
- `test_module_31_of_31()`: Module complet
- `test_module_invalid_30_points()`: Erreur périmètre

---

#### `get_validation_status(p: Path) -> str`

Extrait le statut de validation depuis le front-matter YAML du module.

**Args:**
- `p` (Path): Chemin vers module

**Returns:**
- `str`: Statut traduit
  - `"Validé"` si `validation_status: validated`
  - `"En cours"` si `validation_status: in_progress`
  - `"Brouillon"` si `validation_status: draft` ou absent

**Front-matter attendu:**
```yaml
---
service: SIRCOM
referent: "Pôle web"
updated: "2025-10-02"
validation_status: validated  # validated | in_progress | draft
---
```

**Example:**
```python
from pathlib import Path
from scripts.calculate_scores import get_validation_status

status = get_validation_status(Path("docs/modules/sircom.md"))
# Returns: "Validé"
```

**Tests:**
- `test_validated_status_returns_valide()`
- `test_in_progress_status_returns_en_cours()`
- `test_draft_status_returns_brouillon()`
- `test_missing_validation_status_returns_brouillon()`

---

#### `generate_summary() -> int`

Point d'entrée principal. Génère `docs/synthese.md` avec tableau HTML DSFR des scores.

**Returns:**
- `int`: Exit code
  - `0`: Succès, synthèse générée
  - `2`: Erreur périmètre (module avec ≠ 0 ou 31 points)

**Processus:**
1. Scanne tous fichiers `docs/modules/*.md` (sauf `_template.md`)
2. Pour chaque module:
   - Compte cases cochées avec `score_module()`
   - Extrait statut avec `get_validation_status()`
   - Calcule pourcentage et statut global
3. Génère tableau HTML DSFR dans `docs/synthese.md`
4. Valide périmètre (0 ou 31 points par module)

**Format output (HTML DSFR):**
```html
<div class="fr-table fr-table--bordered" id="table-synthese-span">
    <table id="table-span-modules">
        <tr>
            <td>SIRCOM</td>
            <td>24/31 (77.4%)</td>
            <td>Conforme</td>
            <td>Validé</td>
        </tr>
        <tr>
            <td><strong>TOTAL</strong></td>
            <td><strong>24/186 (12.9%)</strong></td>
            ...
        </tr>
    </table>
</div>
```

**Statuts calculés:**
- `"Conforme"`: ≥ 75% (≥ 24/31)
- `"En cours"`: > 0% et < 75%
- `"Non renseigné"`: 0%

**Example:**
```python
from scripts.calculate_scores import generate_summary

exit_code = generate_summary()
# Génère: docs/synthese.md
# Returns: 0 (succès) ou 2 (erreur)
```

**Validation périmètre:**
```python
# Erreur affichée si total ≠ 0 ou 31
Erreurs de périmètre:
 - sircom.md: 30 points tagués <!-- DINUM --> (attendu 31 ou 0)
```

**Tests:**
- `test_valid_modules_exit_0()`: Modules valides (0 ou 31)
- `test_invalid_module_exit_2()`: Module invalide (30 points)
- `test_status_calculation[...]`: 6 scénarios calcul statut

---

### enrich_pdf_metadata.py

Enrichit les métadonnées XMP/PDF pour conformité accessibilité RGAA.

**Localisation:** `scripts/enrich_pdf_metadata.py`
**Coverage:** 78%
**Tests:** `scripts/test_enrich_pdf*.py` (7 tests)
**Dépendances:** `pikepdf>=8.0.0`

**Usage:**
```bash
# Modifier sur place (défaut)
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf

# Input/output explicites
python scripts/enrich_pdf_metadata.py input.pdf output.pdf
```

**Workflow CI:**
```yaml
- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
```

---

#### `enrich_pdf_metadata(input_path: Path, output_path: Path = None) -> None`

Ajoute métadonnées Dublin Core et XMP au PDF généré par MkDocs.

**Args:**
- `input_path` (Path): Chemin vers PDF source
- `output_path` (Path, optional): Chemin vers PDF enrichi
  - Si `None`: Modification sur place (défaut)

**Returns:**
- `None`

**Raises:**
- `FileNotFoundError`: Si `input_path` n'existe pas
- `ImportError`: Si `pikepdf` non installé
- `Exception`: Si erreur lors du traitement PDF (corrompu, etc.)

**Métadonnées ajoutées:**

**Dublin Core (DC):**
```python
meta["dc:title"] = "SPAN SG"
meta["dc:language"] = "fr-FR"
meta["dc:creator"] = ["Secrétariat Général"]
meta["dc:subject"] = "Schéma Pluriannuel d'Accessibilité Numérique"
meta["dc:description"] = "Plan d'accessibilité numérique du SG 2025-2027..."
```

**PDF spécifiques:**
```python
meta["pdf:Keywords"] = "SPAN, accessibilité, SG, numérique, RGAA, DINUM"
meta["pdf:Producer"] = "MkDocs Material + mkdocs-with-pdf + pikepdf"
```

**XMP:**
```python
meta["xmp:CreatorTool"] = "MkDocs Material 9.x"
meta["xmp:CreateDate"] = datetime.now(timezone.utc).isoformat()
meta["xmp:MetadataDate"] = datetime.now(timezone.utc).isoformat()
```

**Example:**
```python
from pathlib import Path
from scripts.enrich_pdf_metadata import enrich_pdf_metadata

# Modification sur place
enrich_pdf_metadata(Path("exports/span-sg.pdf"))

# Avec output distinct
enrich_pdf_metadata(
    Path("exports/span-sg.pdf"),
    Path("exports/span-sg-enriched.pdf")
)
```

**Gestion erreurs:**
```python
# 1. Import manquant
try:
    import pikepdf
except ImportError:
    print("❌ Erreur: pikepdf non installé")
    sys.exit(1)

# 2. Fichier inexistant
if not input_path.exists():
    print(f"❌ Fichier introuvable: {input_path}")
    sys.exit(1)

# 3. Erreur traitement
try:
    with pikepdf.open(input_path) as pdf:
        # ... traitement
except Exception as e:
    print(f"❌ Erreur lors de l'enrichissement: {e}")
    sys.exit(1)
```

**Tests:**
- `test_file_not_found_exits_1()`: Fichier inexistant
- `test_enrich_valid_pdf_adds_metadata()`: Enrichissement réussi
- `test_corrupted_pdf_raises_exception()`: PDF corrompu
- `test_pdf_save_error_caught()`: Erreur sauvegarde

---

## Hooks MkDocs

### dsfr_table_wrapper.py

Wrappe automatiquement les `<table>` avec `<div class="fr-table">` pour conformité DSFR.

**Localisation:** `hooks/dsfr_table_wrapper.py`
**Coverage:** 100%
**Tests:** `tests/test_hooks_dsfr_table_wrapper.py` (7 tests)

**Hook MkDocs:** `on_page_content`

**Usage automatique:**
```yaml
# mkdocs-dsfr.yml
hooks:
  - hooks/dsfr_table_wrapper.py
```

---

#### `on_page_content(html: str, page: "Page", config: "Config", files: "Files") -> str`

Hook appelé après conversion Markdown → HTML. Wrappe toutes les tables.

**Args:**
- `html` (str): Contenu HTML de la page après conversion Markdown
- `page` (Page): Instance MkDocs Page (non utilisé)
- `config` (Config): Configuration MkDocs (non utilisé)
- `files` (Files): Collection fichiers MkDocs (non utilisé)

**Returns:**
- `str`: HTML modifié avec toutes les tables wrappées dans `<div class="fr-table">`

**Comportement:**
- Détecte toutes balises `<table>` (avec ou sans attributs id, class, etc.)
- Wrappe avec `<div class="fr-table">\n{table}\n</div>`
- Évite double-wrapping avec lookahead négatif regex

**Regex utilisée:**
```python
pattern = r'(?<!<div class="fr-table">)\s*(<table[^>]*>.*?</table>)'
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Lookahead négatif (pas déjà wrappé)
#                                        ^^^^^^^^ Match attributs optionnels
```

**Example transformation:**
```html
<!-- INPUT -->
<table id="my-table" class="custom">
    <tr><td>Data</td></tr>
</table>

<!-- OUTPUT -->
<div class="fr-table">
<table id="my-table" class="custom">
    <tr><td>Data</td></tr>
</table>
</div>
```

**Justification:**
Le thème mkdocs-dsfr supprime les divs HTML lors du preprocessing Markdown.
Ce hook post-traite le HTML pour réinjecter le wrapper DSFR requis pour :
- Accessibilité RGAA (navigation clavier)
- Responsive design (scroll horizontal mobile)

**Tests coverage 100%:**
- `test_wrap_simple_table()`: Table basique
- `test_wrap_multiple_tables()`: Plusieurs tables (wrappées individuellement)
- `test_already_wrapped_table()`: Pas de double-wrapping
- `test_no_table()`: HTML sans table (inchangé)
- `test_complex_table_multiline()`: Table avec thead/tbody
- `test_table_with_attributes()`: Table avec id/class préservés
- `test_malformed_html_graceful()`: HTML malformé (graceful fallback)

**Bug historique corrigé (2025-10-11):**
```python
# AVANT (bug)
pattern = r'<table>.*?</table>'  # ❌ Ne matche pas <table id="...">

# APRÈS (fixé)
pattern = r'<table[^>]*>.*?</table>'  # ✅ Matche tous attributs
```

---

### title_cleaner.py

Nettoie les titres HTML redondants quand `site_name` est vide (thème DSFR).

**Localisation:** `hooks/title_cleaner.py`
**Coverage:** 100%
**Tests:** `tests/test_hooks_title_cleaner.py` (6 tests)

**Hook MkDocs:** `on_post_page`

**Usage automatique:**
```yaml
# mkdocs-dsfr.yml
hooks:
  - hooks/title_cleaner.py
```

---

#### `on_post_page(output: str, page: "Page", config: "Config") -> str`

Hook appelé après génération HTML complète de la page. Nettoie titres.

**Args:**
- `output` (str): HTML complet de la page après génération
- `page` (Page): Instance MkDocs Page (non utilisé)
- `config` (Config): Configuration MkDocs (non utilisé)

**Returns:**
- `str`: HTML modifié avec titre nettoyé

**Comportement:**
Transforme `<title>Page  -  </title>` en `<title>Page</title>`

**Regex utilisée:**
```python
pattern = r"<title>\s*(.*?)\s*-\s*\s*</title>"
replacement = r"<title>\1</title>"
```

**Example transformation:**
```html
<!-- INPUT -->
<title>
        SPAN (SG)
        -

    </title>

<!-- OUTPUT -->
<title>SPAN (SG)</title>
```

**Justification:**
Lorsque `site_name` est vide dans `mkdocs.yml`, MkDocs génère des titres avec tirets orphelins et espaces superflus. Ce hook nettoie ces artefacts pour améliorer :
- SEO (titres propres indexés par moteurs recherche)
- Accessibilité (lecteurs d'écran lisent titres propres)

**Config déclencheuse:**
```yaml
# mkdocs-dsfr.yml
site_name: ""  # Vide → titres avec tirets orphelins
```

**Tests coverage 100%:**
- `test_clean_title_with_dash_and_spaces()`: Titre multiligne avec tiret
- `test_clean_title_simple_dash()`: Tiret simple
- `test_clean_title_without_dash()`: Titre sans tiret (inchangé)
- `test_no_title_tag()`: HTML sans title (inchangé)
- `test_title_with_rich_content()`: Contenu riche préservé
- `test_multiple_titles()`: Plusieurs titres nettoyés

---

## Bonnes pratiques

### Type hints modernes (PEP 563)

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.structure.pages import Page
    from mkdocs.config import Config

def on_page_content(html: str, page: "Page", config: "Config", files) -> str:
    # TYPE_CHECKING = False en runtime (pas d'import réel)
    # Mais IDE/mypy voient les types
    pass
```

### Gestion erreurs robuste

```python
# 3 niveaux (enrich_pdf_metadata.py)
try:
    import pikepdf  # 1. Import
except ImportError:
    sys.exit(1)

if not path.exists():  # 2. Validation input
    sys.exit(1)

try:
    # ... traitement  # 3. Erreurs runtime
except Exception as e:
    sys.exit(1)
```

### Tests exhaustifs

```python
# Minimum 5 scénarios par fonction
def test_nominal():        # Cas nominal
def test_edge_case():      # Cas limite
def test_empty_input():    # Input vide
def test_invalid_input():  # Input invalide
def test_multiple():       # Plusieurs éléments
```

---

## Références

**Tests:**
- `scripts/test_calculate_scores*.py`: 26 tests, 100% coverage
- `scripts/test_enrich_pdf*.py`: 7 tests, 78% coverage
- `tests/test_hooks*.py`: 13 tests, 100% coverage

**Standards:**
- PEP 8: Style guide Python
- PEP 257: Docstring conventions
- PEP 563: Postponed evaluation annotations (TYPE_CHECKING)
- Black: Code formatter (line-length 88)
- Ruff: Linter (select E,W,F,I,N)

**Coverage global ciblé:** 92% (seuil 89%+)
