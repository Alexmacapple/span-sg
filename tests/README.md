# Structure des Tests SPAN SG

Documentation de l'organisation des tests et des conventions de test pour le projet SPAN SG.

Version: 1.0.0
Dernière mise à jour: 2025-10-22

---

## Vue d'ensemble

Le projet utilise pytest comme framework de test avec une organisation claire en trois catégories :

```
tests/
├── unit/              # Tests unitaires (isolés, rapides)
│   ├── scripts/       # Tests pour scripts de production
│   └── hooks/         # Tests pour hooks MkDocs
├── e2e/               # Tests end-to-end (complets, lents)
└── test_*.py          # Tests d'intégration (au niveau racine)
```

---

## Tests Unitaires (`tests/unit/`)

Tests isolés qui vérifient le comportement d'une seule fonction ou classe.

### Scripts de production (`tests/unit/scripts/`)

Tests pour les scripts Python de production :

| Fichier | Script testé | Coverage requis |
|---------|--------------|-----------------|
| `test_calculate_scores.py` | `scripts/calculate_scores.py` | 89%+ |
| `test_calculate_scores_extended.py` | `scripts/calculate_scores.py` | 89%+ |
| `test_enrich_pdf_metadata.py` | `scripts/enrich_pdf_metadata.py` | 89%+ |
| `test_enrich_pdf_extended.py` | `scripts/enrich_pdf_metadata.py` | 89%+ |

**Exécution :**
```bash
# Tous les tests unitaires scripts
pytest tests/unit/scripts/ -v

# Avec coverage (89% requis)
pytest tests/unit/scripts/ --cov=scripts --cov-fail-under=89
```

### Hooks MkDocs (`tests/unit/hooks/`)

Tests pour les hooks Python utilisés par MkDocs DSFR :

| Fichier | Hook testé | Coverage requis |
|---------|-----------|-----------------|
| `test_hooks_dsfr_table_wrapper.py` | `hooks/dsfr_table_wrapper.py` | 100% |
| `test_hooks_title_cleaner.py` | `hooks/title_cleaner.py` | 100% |
| `test_hooks_pdf_copy.py` | `hooks/pdf_copy.py` | 100% |

**Exécution :**
```bash
# Tous les tests hooks
pytest tests/unit/hooks/ -v

# Avec coverage strict (100% requis)
pytest tests/unit/hooks/ \
  --cov=hooks \
  --cov-config=.coveragerc-hooks \
  --cov-fail-under=100
```

**Important :** Les hooks nécessitent une couverture de 100% car ils impactent directement l'accessibilité RGAA du site.

---

## Tests d'Intégration (`tests/*.py`)

Tests au niveau racine vérifiant l'interaction entre plusieurs composants.

| Fichier | Description |
|---------|-------------|
| `test_accessibility.py` | Tests d'accessibilité RGAA globaux |

**Exécution :**
```bash
pytest tests/test_accessibility.py -v
```

---

## Tests End-to-End (`tests/e2e/`)

Tests complets simulant le parcours utilisateur réel via Selenium.

```
tests/e2e/
├── test_accessibility_scenarios.py   # 9 scénarios RGAA
├── ci_runner.sh                       # Script CI pour Docker
├── accessibility_report.json          # Rapport JSON généré
└── report.html                        # Rapport HTML détaillé
```

**Scénarios couverts :**
1. Navigation clavier complète
2. Titres de page accessibles
3. Landmarks ARIA présents
4. Skip links fonctionnels
5. Contraste conforme WCAG AA
6. Images avec alt text
7. Formulaires accessibles
8. Ordre de tabulation logique
9. Liens descriptifs

**Exécution locale :**
```bash
# Démarrer le serveur MkDocs
docker compose -f docker-compose-dsfr.yml up -d

# Lancer les tests E2E (dans le container)
docker run --rm mkdocs-test:latest bash tests/e2e/ci_runner.sh
```

**Exécution CI :**
Les tests E2E s'exécutent automatiquement sur push vers `main` (GitHub Actions).

---

## Configuration Coverage

Deux fichiers de configuration distincts :

### `.coveragerc` (scripts production)
```ini
[run]
omit = tests/*  # Exclure tous les tests

[report]
fail_under = 89  # Seuil minimum 89%
```

### `.coveragerc-hooks` (hooks MkDocs)
```ini
[run]
source = hooks/
omit = tests/*, scripts/*

[report]
fail_under = 100  # Seuil strict 100%
```

---

## Commandes Utiles

### Exécuter tous les tests
```bash
# Tous les tests unitaires
pytest tests/unit/ -v

# Tous les tests (unit + intégration)
pytest tests/ -v --ignore=tests/e2e/

# Avec coverage combiné
pytest tests/unit/ --cov=scripts --cov=hooks --cov-report=term-missing
```

### Vérifier coverage individuellement
```bash
# Scripts uniquement (89% requis)
pytest tests/unit/scripts/ \
  --cov=scripts \
  --cov-fail-under=89

# Hooks uniquement (100% requis)
pytest tests/unit/hooks/ \
  --cov=hooks \
  --cov-config=.coveragerc-hooks \
  --cov-fail-under=100
```

### Générer rapports HTML
```bash
# Coverage HTML pour scripts
pytest tests/unit/scripts/ \
  --cov=scripts \
  --cov-report=html
# → htmlcov/index.html

# Coverage HTML pour hooks
pytest tests/unit/hooks/ \
  --cov=hooks \
  --cov-config=.coveragerc-hooks \
  --cov-report=html:htmlcov-hooks
# → htmlcov-hooks/index.html
```

---

## Conventions de Nommage

| Convention | Usage | Exemple |
|------------|-------|---------|
| `test_*.py` | Fichiers de test | `test_calculate_scores.py` |
| `test_*()` | Fonctions de test | `def test_valid_score():` |
| `Test*` | Classes de test | `class TestScoreCalculation:` |
| `*_extended.py` | Tests étendus/edge cases | `test_calculate_scores_extended.py` |

---

## Bonnes Pratiques

### 1. Isolation des tests
Chaque test doit être indépendant et ne pas dépendre de l'état d'autres tests.

```python
# Bon : utiliser des fixtures
@pytest.fixture
def sample_module():
    return {"service": "SNUM", "checked": 10, "total": 33}

def test_score_calculation(sample_module):
    assert calculate_score(sample_module) == 30.3
```

### 2. Nommage descriptif
Les noms de tests doivent décrire clairement le comportement testé.

```python
# Bon
def test_calculate_scores_returns_zero_when_no_criteria_checked():
    pass

# Mauvais
def test_scores():
    pass
```

### 3. Coverage ≠ Qualité
Un coverage de 100% ne garantit pas l'absence de bugs. Privilégiez des tests pertinents.

### 4. Tests rapides pour unit, lents pour E2E
- Tests unitaires : < 1s par fichier
- Tests intégration : < 10s par fichier
- Tests E2E : < 5min par suite

---

## CI/CD Workflow

Le workflow GitHub Actions (`.github/workflows/build.yml`) exécute :

1. **Pre-commit verification** : Validation hooks pre-commit
2. **Unit tests** : Tous les tests unitaires
3. **Coverage checks** :
   - Scripts production : 89%+
   - Hooks MkDocs : 100%
4. **E2E tests** : Uniquement sur push `main` (300s timeout)

**Durée totale CI :** ~11 minutes (avec E2E), ~6 minutes (sans E2E sur PR)

---

## Debugging Tests

### Afficher stdout/stderr
```bash
pytest tests/unit/ -v -s
```

### Stopper au premier échec
```bash
pytest tests/unit/ -x
```

### Exécuter un seul test
```bash
pytest tests/unit/scripts/test_calculate_scores.py::test_valid_module -v
```

### Mode debug interactif
```bash
pytest tests/unit/ --pdb
```

---

## Références

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Plugin](https://pytest-cov.readthedocs.io/)
- [Selenium WebDriver](https://selenium-python.readthedocs.io/)
- [RGAA 4.1 Critères](https://accessibilite.numerique.gouv.fr/)
- [Coverage.py Configuration](https://coverage.readthedocs.io/en/latest/config.html)

---

## Contacts

- **Mainteneur tests** : Alex (@alex)
- **Validation accessibilité** : Bertrand (@bertrand)
- **Questions** : GitHub Issues ou Discussions
