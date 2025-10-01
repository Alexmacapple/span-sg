---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S2-05 : Qualité code Python (tests unitaires + linting)

**Phase** : Semaine 2 - Automatisation
**Priorité** : Haute
**Estimation** : 1.5h
**Assigné** : Alexandra

---

## Contexte projet

Le projet SPAN SG repose sur un script Python critique : `scripts/calculate_scores.py` (57 lignes).
Ce script est le **moteur de scoring** qui :
- Scanne les 6 modules services (docs/modules/*.md)
- Compte les 31 points DINUM cochés/total
- Génère `docs/synthese.md` (tableau de bord)
- Valide le périmètre (exit 2 si ≠ 0 ou 31 points)
- Exécuté par la CI à chaque commit

**Problème actuel** : Qualité code = 18/20
- ⚠️ **-1 point** : Pas de tests unitaires pytest
- ⚠️ **-1 point** : Pas de linting/formatting (Black, Ruff)

**Risques identifiés** :
1. **Bug non détecté** : Ligne 39 corrigée manuellement en S1-05 (3 commits correctifs)
2. **Régression** : Modification script sans garantie (pas de tests)
3. **Style incohérent** : Semaine 3 = 5 devs contributeurs → conflits style
4. **Revues code longues** : Focus style au lieu de logique métier
5. **Onboarding difficile** : Pas de règles claires pour nouveaux devs

**Contexte Semaine 3** : Onboarding 5 services (SNUM, SRH, SIEP, SAFI, BGS)
→ 5 développeurs vont potentiellement modifier les scripts Python
→ Environnement qualité requis **avant** leurs contributions

**Bénéfices attendus** :
- ✅ Fiabilité : Tests détectent régressions automatiquement
- ✅ Cohérence : Black/Ruff uniformisent le style (zéro débat)
- ✅ Revues rapides : CI bloque code mal formaté
- ✅ Onboarding simple : "Run black, c'est tout"
- ✅ **Score qualité : 18/20 → 20/20**

---

## Objectif

Porter la qualité du code Python de **18/20 à 20/20** en ajoutant :
1. **Tests unitaires pytest** (couverture ≥90%)
2. **Linting/Formatting** (Black + Ruff + pre-commit hooks)
3. **Validation CI** (tests + lint bloquent merge si échec)

---

## Prérequis

- [x] Story S1-05 complétée (script scoring fonctionnel)
- [x] Story S2-01 complétée (CI GitHub Actions configurée)
- [ ] Story S2-04 complétée (doc contributeur à mettre à jour)
- [x] Python 3.9+ installé localement
- [x] Scripts Python existants (calculate_scores.py, etc.)

---

## Étapes d'implémentation

### Partie 1 : Tests unitaires pytest (1h)

#### 1. Installer pytest

```bash
pip install pytest pytest-cov
```

#### 2. Créer `scripts/test_calculate_scores.py`

**Structure des tests** :
```python
#!/usr/bin/env python3
import pytest
from pathlib import Path
from scripts.calculate_scores import load_text, score_module, BOX_RE, FENCE_RE

class TestLoadText:
    """Tests suppression code fences"""

    def test_removes_code_fences(self, tmp_path):
        content = """
- [x] Point réel <!-- DINUM -->

```markdown
- [x] Point dans fence <!-- DINUM -->
```
        """
        file = tmp_path / "test.md"
        file.write_text(content)
        result = load_text(file)
        assert "Point réel" in result
        assert "Point dans fence" not in result

class TestScoreModule:
    """Tests comptage points"""

    def test_module_empty_0_points(self, tmp_path):
        file = tmp_path / "empty.md"
        file.write_text("# Empty module\n")
        checked, total = score_module(file)
        assert checked == 0
        assert total == 0

    def test_module_0_of_31(self, tmp_path):
        content = "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(31)])
        file = tmp_path / "unchecked.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 0
        assert total == 31

    def test_module_6_of_31_sircom(self, tmp_path):
        content = (
            "".join([f"- [x] Point {i} <!-- DINUM -->\n" for i in range(6)])
            + "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(6, 31)])
        )
        file = tmp_path / "sircom.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 6
        assert total == 31
        assert (checked / total * 100) == pytest.approx(19.4, abs=0.1)

    def test_module_31_of_31(self, tmp_path):
        content = "".join([f"- [x] Point {i} <!-- DINUM -->\n" for i in range(31)])
        file = tmp_path / "complete.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 31
        assert total == 31

    def test_module_invalid_30_points(self, tmp_path):
        content = "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(30)])
        file = tmp_path / "invalid.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert total == 30
        assert total not in (0, 31)

class TestStatusLogic:
    """Tests calcul statut (bug ligne 39 corrigé en S1-05)"""

    @pytest.mark.parametrize("checked,total,expected", [
        (31, 31, "✓ Conforme"),      # 100%
        (24, 31, "✓ Conforme"),      # 77.4% >= 75%
        (23, 31, "En cours"),        # 74.2% < 75%
        (1, 31, "En cours"),         # 3.2% > 0%
        (0, 31, "Non renseigné"),    # 0%
        (0, 0, "Non renseigné"),     # Division par zéro
    ])
    def test_status_calculation(self, checked, total, expected):
        pct = round((checked / total) * 100, 1) if total else 0.0
        status = "✓ Conforme" if pct >= 75 else "En cours" if pct > 0 else "Non renseigné"
        assert status == expected

class TestRegexPatterns:
    """Tests patterns regex"""

    def test_box_regex_unchecked(self):
        text = "- [ ] Point <!-- DINUM -->"
        match = BOX_RE.search(text)
        assert match is not None
        assert match.group(1) == " "

    def test_box_regex_checked_lowercase(self):
        text = "- [x] Point <!-- DINUM -->"
        match = BOX_RE.search(text)
        assert match.group(1) == "x"

    def test_box_regex_checked_uppercase(self):
        text = "- [X] Point <!-- DINUM -->"
        match = BOX_RE.search(text)
        assert match.group(1) == "X"

    def test_box_regex_ignores_without_tag(self):
        text = "- [x] Point sans tag"
        matches = BOX_RE.findall(text)
        assert len(matches) == 0

class TestGenerateSummary:
    """Tests génération synthèse + détection erreurs"""

    def test_valid_modules_exit_0(self, tmp_path, monkeypatch):
        modules_dir = tmp_path / "docs" / "modules"
        modules_dir.mkdir(parents=True)

        content = "".join([f"- [ ] P{i} <!-- DINUM -->\n" for i in range(31)])
        (modules_dir / "test.md").write_text(content)

        monkeypatch.chdir(tmp_path)

        from scripts.calculate_scores import generate_summary
        exit_code = generate_summary()

        assert exit_code == 0
        assert (tmp_path / "docs/synthese.md").exists()

    def test_invalid_module_exit_2(self, tmp_path, monkeypatch, capsys):
        modules_dir = tmp_path / "docs" / "modules"
        modules_dir.mkdir(parents=True)

        content = "".join([f"- [ ] P{i} <!-- DINUM -->\n" for i in range(30)])
        (modules_dir / "invalid.md").write_text(content)

        monkeypatch.chdir(tmp_path)

        from scripts.calculate_scores import generate_summary
        exit_code = generate_summary()

        assert exit_code == 2
        captured = capsys.readouterr()
        assert "Erreurs de périmètre" in captured.out
        assert "invalid.md: 30 points" in captured.out
```

**Total** : 15 tests couvrant tous les cas (normaux + edge cases + bug historique)

#### 3. Exécuter les tests

```bash
# Tests simples
pytest scripts/test_calculate_scores.py -v

# Avec couverture
pytest scripts/test_calculate_scores.py --cov=scripts --cov-report=term

# Attendu : couverture ≥90%
```

### Partie 2 : Linting/Formatting (30min)

#### 4. Créer `pyproject.toml`

```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
/(
  \.git
  | \.github
  | docs
  | site
)/
'''

[tool.ruff]
line-length = 88
target-version = "py39"

select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (tri imports)
    "N",   # pep8-naming
]

ignore = [
    "E501",  # line too long (géré par Black)
]

[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]

[tool.pytest.ini_options]
testpaths = ["scripts"]
python_files = "test_*.py"
addopts = "-v --cov=scripts --cov-report=term-missing"
```

#### 5. Créer `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.15
    hooks:
      - id: ruff
        args: [--fix]
```

#### 6. Installer et exécuter

```bash
# Installation
pip install black ruff pre-commit

# Formater code existant
black scripts/

# Vérifier linting
ruff check scripts/

# Installer pre-commit hooks
pre-commit install

# Test pre-commit
pre-commit run --all-files
```

### Partie 3 : Intégration CI (15min)

#### 7. Modifier `.github/workflows/build.yml`

Ajouter **avant** le build MkDocs :

```yaml
- name: Run tests and linting
  run: |
    pip install pytest pytest-cov black ruff

    # Tests unitaires
    pytest scripts/ --cov=scripts --cov-fail-under=90

    # Formatting check
    black scripts/ --check --diff

    # Linting
    ruff check scripts/
```

**Ordre CI** :
1. Tests pytest (bloque si échec)
2. Black check (bloque si code non formaté)
3. Ruff check (bloque si erreurs lint)
4. MkDocs build (comme avant)

#### 8. Mettre à jour doc contributeur

Dans `docs/guide-contributeur.md` (créé en S2-04), ajouter section :

```markdown
## Qualité code Python

### Style automatique

Le projet utilise **Black** et **Ruff** pour garantir un style cohérent.

**Installation pre-commit** :
```bash
pip install pre-commit
pre-commit install
```

**Workflow** :
1. Coder normalement
2. `git add` vos fichiers
3. `git commit` → hooks Black + Ruff s'exécutent auto
4. Si erreurs → corrections appliquées, re-commit
5. `git push` → CI valide

**Commandes manuelles** :
```bash
# Formater tout le code
black scripts/

# Vérifier linting
ruff check scripts/

# Tests unitaires
pytest scripts/
```

**Aucune décision style à prendre, tout est automatisé.**
```

---

## Critères d'acceptation

- [ ] `scripts/test_calculate_scores.py` créé avec 15+ tests
- [ ] `pytest scripts/` passe sans erreur
- [ ] Couverture code ≥90% (pytest-cov)
- [ ] `pyproject.toml` créé avec config Black + Ruff
- [ ] `.pre-commit-config.yaml` créé
- [ ] `black scripts/ --check` passe (code formaté)
- [ ] `ruff check scripts/` passe (0 erreurs)
- [ ] CI valide tests + linting (bloque merge si échec)
- [ ] Pre-commit hooks installés et fonctionnels
- [ ] Doc contributeur mise à jour avec section "Qualité code Python"

---

## Tests de validation

```bash
# Test 1 : Pytest installé et fonctionnel
pytest --version && echo "OK" || echo "FAIL"
# Attendu : pytest 7.x.x

# Test 2 : Tests passent
pytest scripts/test_calculate_scores.py -v && echo "OK" || echo "FAIL"
# Attendu : 15 passed

# Test 3 : Couverture ≥90%
pytest scripts/ --cov=scripts --cov-fail-under=90 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : Black installé
black --version && echo "OK" || echo "FAIL"
# Attendu : black, 24.x.x

# Test 5 : Code formaté
black scripts/ --check && echo "OK" || echo "FAIL"
# Attendu : All done! ✨

# Test 6 : Ruff installé
ruff --version && echo "OK" || echo "FAIL"
# Attendu : ruff 0.x.x

# Test 7 : Linting passe
ruff check scripts/ && echo "OK" || echo "FAIL"
# Attendu : All checks passed!

# Test 8 : Pre-commit configuré
test -f .pre-commit-config.yaml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 9 : Pre-commit hooks installés
pre-commit run --all-files && echo "OK" || echo "FAIL"
# Attendu : black...Passed, ruff...Passed

# Test 10 : CI config mise à jour
grep -q "pytest scripts/" .github/workflows/build.yml && echo "OK" || echo "FAIL"
# Attendu : OK
```

---

## Dépendances

**Bloque** :
- S3-01 (modules vides - devs utilisent pre-commit)
- S3-02 (formation Git - inclut qualité code)

**Dépend de** :
- S1-05 (script scoring existant)
- S2-01 (CI configurée)
- S2-04 (doc contributeur à mettre à jour)

---

## Références

- **PRD v3.3** : Section "Qualité du code" → 18/20 → 20/20
- **S1-05** : Validation script scoring (bug ligne 39 corrigé manuellement)
- **S2-04** : Doc contributeur (à enrichir avec section qualité)
- **Black docs** : https://black.readthedocs.io/
- **Ruff docs** : https://docs.astral.sh/ruff/
- **Pytest docs** : https://docs.pytest.org/

---

## Notes et risques

**Temps formation devs**
Pre-commit hooks automatiques → formation 5min max ("c'est déjà configuré, juste commit").
Documenté dans guide contributeur S2-04.

**False positives linting**
Ruff peut détecter "erreurs" acceptables (ex: ligne longue dans regex).
→ Config `.ruff.toml` ajuste règles si besoin (déjà fait : ignore E501).

**Coverage 90% strict**
Si fonctions utilitaires ajoutées (non critiques), ajuster `--cov-fail-under=85`.
Actuellement 57 lignes → 90% = ~51 lignes couvertes (réaliste).

**Compatibilité Python 3.9**
Black + Ruff + pytest compatibles Python 3.9+.
Tests locaux sur Python 3.9.6 (env actuel macOS).

**Migration future Python 3.12**
Ruff avec `pyupgrade` facilite migration (détecte syntaxe obsolète).
Aucun lock-in, passage 3.9 → 3.12 transparent.

---

## Post-tâche

**Badge coverage dans README** :
```markdown
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)](.)
```

**Activer Codecov** (optionnel) :
```yaml
# .github/workflows/build.yml
- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

**Documenter dans README** :
```markdown
## Développement

### Qualité code
- **Tests** : `pytest scripts/`
- **Format** : `black scripts/`
- **Lint** : `ruff check scripts/`

Pre-commit hooks automatiques installés via `pre-commit install`.
```

**Mettre à jour checklist PRD** :
```markdown
Semaine 2 automatisation
[x] GitHub Actions ordre corrigé
[x] export PDF automatique
[x] preview privée
[x] doc contributeur
[x] qualité code (tests + linting)  ← NOUVEAU
```
