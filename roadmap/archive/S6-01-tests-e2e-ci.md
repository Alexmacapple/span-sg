---
bmad_phase: maintenance
bmad_agent: dev
story_type: quality
autonomous: false
validation: human-qa
---

# Story S6-01 : Tests E2E Automatisés CI

**Phase** : Semaine 6 - Excellence Technique
**Priorité** : Moyenne (P2 - robustesse post-POC)
**Estimation** : 4-6h

---

## Contexte projet

**Après POC v1.0.0** : Score qualité 94/100
- ✅ Coverage scripts production : 89.6%
- ✅ Tests unitaires : 21 tests pytest
- ⚠️ Tests E2E manuels uniquement (`tests/e2e/*.sh`)
- ❌ Tests E2E non intégrés CI → régressions détectées tardivement

**Scripts E2E existants** :
```
tests/e2e/
├── run_all.sh                    # Exécute tous les scénarios
├── scenario_performance.sh        # Test temps de build
├── scenario_frontmatter.sh        # Validation YAML front-matter
├── scenario_rollback.sh           # Test intégrité après rollback
├── scenario_erreur_perimetre.sh   # Module avec ≠31 points
├── scenario_multi_modules.sh      # Calcul scores 6 modules
└── README.md                      # Doc tests E2E
```

**Problème** :
- Tests manuels (`./tests/e2e/run_all.sh`) non exécutés automatiquement
- CI ne détecte pas régressions comportementales (seulement build/unit)
- Pas de rapport E2E dans Actions

**Objectif S6-01** : Intégrer tests E2E dans CI avec reporting automatique

---

## Objectif

**Automatiser les tests E2E existants** pour détecter régressions en CI :
- Intégration workflow GitHub Actions
- Rapport HTML E2E généré (artefact uploadé)
- Tests parallélisés (réduction temps CI)
- Échec CI si tests E2E KO

**Livrables** :
- Job `e2e-tests` dans `.github/workflows/build.yml`
- Rapport HTML E2E (style pytest-html)
- Badge GitHub "E2E Tests Passing"
- Section Tests E2E dans CONTRIBUTING.md

---

## Prérequis

- [x] Tests E2E manuels fonctionnels (6 scénarios)
- [x] CI existante (build + unit tests + coverage)
- [x] Docker Compose configuré

---

## Étapes d'implémentation

### Phase 1 - Préparation Tests E2E (1h)

#### Microtâches

**1.1 Créer script runner E2E pour CI** (30 min)

```bash
# Fichier: tests/e2e/ci_runner.sh
#!/bin/bash
set -e

echo "🧪 Exécution tests E2E CI"

TESTS_DIR="$(dirname "$0")"
REPORT_DIR="$TESTS_DIR/reports"
mkdir -p "$REPORT_DIR"

# Exécuter chaque scénario et capturer résultat
FAILED=0
SCENARIOS=(
    "scenario_performance.sh"
    "scenario_frontmatter.sh"
    "scenario_multi_modules.sh"
    "scenario_erreur_perimetre.sh"
    "scenario_rollback.sh"
)

for scenario in "${SCENARIOS[@]}"; do
    echo ""
    echo "▶ Test: $scenario"

    if bash "$TESTS_DIR/$scenario" > "$REPORT_DIR/${scenario%.sh}.log" 2>&1; then
        echo "  ✅ PASS"
    else
        echo "  ❌ FAIL"
        FAILED=$((FAILED + 1))
    fi
done

# Générer rapport HTML
python3 "$TESTS_DIR/generate_report.py" "$REPORT_DIR"

if [ $FAILED -gt 0 ]; then
    echo ""
    echo "❌ $FAILED test(s) E2E échoué(s)"
    exit 1
fi

echo ""
echo "✅ Tous les tests E2E passent"
```

**Checklist** :
- [ ] Script ci_runner.sh créé
- [ ] Permissions exécution (+x)
- [ ] Logs capturés par scénario

**1.2 Créer générateur rapport HTML** (30 min)

```python
# Fichier: tests/e2e/generate_report.py
#!/usr/bin/env python3
"""Génère rapport HTML tests E2E"""
import sys
from pathlib import Path
from datetime import datetime

def parse_log(log_file):
    """Parse log scénario et extrait résultat"""
    content = log_file.read_text()
    passed = "✅" in content or "SUCCESS" in content
    return {
        "name": log_file.stem.replace("scenario_", "").replace("_", " ").title(),
        "passed": passed,
        "log": content
    }

def generate_html(report_dir):
    """Génère rapport HTML depuis logs"""
    logs = sorted(Path(report_dir).glob("*.log"))
    results = [parse_log(log) for log in logs]

    passed = sum(1 for r in results if r["passed"])
    total = len(results)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tests E2E SPAN SG</title>
    <style>
        body {{ font-family: monospace; margin: 20px; }}
        .summary {{ background: #f0f0f0; padding: 10px; margin-bottom: 20px; }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
        .scenario {{ border: 1px solid #ccc; margin: 10px 0; padding: 10px; }}
        pre {{ background: #f5f5f5; padding: 10px; overflow: auto; }}
    </style>
</head>
<body>
    <h1>Tests E2E SPAN SG</h1>
    <div class="summary">
        <strong>Résultats</strong> : {passed}/{total} tests passent
        <br><strong>Date</strong> : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </div>
"""

    for result in results:
        status = "✅ PASS" if result["passed"] else "❌ FAIL"
        css_class = "pass" if result["passed"] else "fail"
        html += f"""
    <div class="scenario">
        <h2 class="{css_class}">{result["name"]} - {status}</h2>
        <pre>{result["log"]}</pre>
    </div>
"""

    html += """
</body>
</html>
"""

    report_file = Path(report_dir) / "e2e-report.html"
    report_file.write_text(html)
    print(f"Rapport généré : {report_file}")

if __name__ == "__main__":
    generate_html(sys.argv[1])
```

**Checklist** :
- [ ] Script generate_report.py créé
- [ ] Parsing logs fonctionnel
- [ ] HTML bien formaté

---

### Phase 2 - Intégration CI (2h)

#### Microtâches

**2.1 Ajouter job E2E dans workflow** (1h)

```yaml
# Fichier: .github/workflows/build.yml
# Ajouter après le job "build"

  e2e-tests:
    name: Tests E2E
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Install system dependencies (qpdf)
        run: |
          sudo apt-get update
          sudo apt-get install -y qpdf

      - name: Run E2E tests
        run: |
          chmod +x tests/e2e/ci_runner.sh
          ./tests/e2e/ci_runner.sh

      - name: Upload E2E report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: e2e-report
          path: tests/e2e/reports/e2e-report.html
          retention-days: 30

      - name: Comment PR with E2E results
        if: github.event_name == 'pull_request' && failure()
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '❌ Tests E2E échoués. Voir rapport dans artifacts.'
            })
```

**Checklist** :
- [ ] Job e2e-tests ajouté après build
- [ ] Dépendances installées (Python + qpdf)
- [ ] Rapport uploadé comme artefact
- [ ] Commentaire PR si échec

**2.2 Optimiser temps exécution** (30 min)

Stratégie : Parallélisation avec matrix

```yaml
  e2e-tests:
    name: Tests E2E (${{ matrix.scenario }})
    runs-on: ubuntu-latest
    needs: build
    strategy:
      fail-fast: false
      matrix:
        scenario:
          - performance
          - frontmatter
          - multi_modules
          - erreur_perimetre
          - rollback

    steps:
      # ... setup steps ...

      - name: Run E2E scenario
        run: |
          chmod +x tests/e2e/scenario_${{ matrix.scenario }}.sh
          ./tests/e2e/scenario_${{ matrix.scenario }}.sh
```

**Checklist** :
- [ ] Matrix configurée (5 jobs parallèles)
- [ ] fail-fast: false (tous scénarios exécutés même si 1 échoue)
- [ ] Temps CI réduit (~3 min → ~1 min)

**2.3 Créer badge E2E** (30 min)

```markdown
# Fichier: README.md
# Ajouter après badge build

[![E2E Tests](https://github.com/Alexmacapple/span-sg-repo/actions/workflows/build.yml/badge.svg?event=push)](https://github.com/Alexmacapple/span-sg-repo/actions/workflows/build.yml)
```

**Checklist** :
- [ ] Badge ajouté dans README.md
- [ ] Lien vers workflow fonctionnel

---

### Phase 3 - Documentation (1h)

#### Microtâches

**3.1 Documenter tests E2E dans CONTRIBUTING.md** (45 min)

```markdown
# Ajouter section après "Tests et Coverage"

## Tests End-to-End (E2E)

### Exécuter tests E2E localement

```bash
# Tous les scénarios
./tests/e2e/run_all.sh

# Scénario spécifique
./tests/e2e/scenario_performance.sh

# Avec rapport HTML
./tests/e2e/ci_runner.sh
open tests/e2e/reports/e2e-report.html
```

### Scénarios E2E disponibles

| Scénario | Description | Temps |
|----------|-------------|-------|
| **performance** | Vérifie temps build < 30s | ~10s |
| **frontmatter** | Valide YAML front-matter modules | ~5s |
| **multi_modules** | Calcul scores 6 modules | ~8s |
| **erreur_perimetre** | Module ≠31 points → erreur | ~5s |
| **rollback** | Intégrité après rollback Git | ~12s |

### Ajouter nouveau test E2E

1. Créer script `tests/e2e/scenario_[nom].sh`
2. Utiliser structure :
   ```bash
   #!/bin/bash
   set -e
   echo "Test: [Description]"
   # ... tests ...
   echo "✅ SUCCESS"
   ```
3. Ajouter dans `ci_runner.sh` (array SCENARIOS)
4. Tester localement : `./tests/e2e/ci_runner.sh`
5. Commit et pusher (CI exécutera automatiquement)

### CI Integration

Tests E2E exécutés automatiquement sur :
- ✅ Push vers `draft` ou `main`
- ✅ Pull Requests
- ✅ Parallélisés (5 jobs simultanés)
- ✅ Rapport HTML disponible dans Actions artifacts

En cas d'échec :
1. Consulter logs CI (onglet Actions)
2. Télécharger artefact `e2e-report`
3. Ouvrir `e2e-report.html` localement
4. Reproduire scénario échoué en local
```

**Checklist** :
- [ ] Section Tests E2E ajoutée CONTRIBUTING.md
- [ ] Tableau scénarios documenté
- [ ] Guide ajout nouveau test
- [ ] Procédure debugging

**3.2 Mettre à jour tests/e2e/README.md** (15 min)

```markdown
# Ajouter section CI

## CI Integration

Tests E2E intégrés dans GitHub Actions (`.github/workflows/build.yml`).

**Exécution automatique** :
- Push vers `draft`/`main`
- Pull Requests
- Parallélisation : 5 jobs simultanés

**Rapport HTML** :
- Généré automatiquement (`tests/e2e/reports/e2e-report.html`)
- Uploadé comme artefact (rétention 30 jours)
- Accessible dans Actions → Artifacts

**Commande locale (identique CI)** :
```bash
./tests/e2e/ci_runner.sh
```

**Checklist** :
- [ ] Section CI ajoutée
- [ ] Lien vers workflow
- [ ] Commande locale documentée

---

### Phase 4 - Tests & Validation (1-2h)

#### Microtâches

**4.1 Tester ci_runner.sh localement** (30 min)

```bash
# Exécution complète
./tests/e2e/ci_runner.sh

# Vérifications
ls -lh tests/e2e/reports/e2e-report.html  # Rapport généré
open tests/e2e/reports/e2e-report.html     # Visuel OK
echo $?                                     # Exit code 0
```

**Checklist** :
- [ ] Tous scénarios passent
- [ ] Rapport HTML généré
- [ ] Logs capturés par scénario
- [ ] Exit code 0 si succès

**4.2 Pusher branche feature et vérifier CI** (30 min)

```bash
git checkout -b feature/s6-01-e2e-ci
git add tests/e2e/ci_runner.sh tests/e2e/generate_report.py .github/workflows/build.yml
git commit -m "feat(tests): intègre tests E2E dans CI (S6-01)

- Ajoute ci_runner.sh pour exécution automatique
- Génère rapport HTML E2E
- Job GitHub Actions avec parallélisation (5 scénarios)
- Upload artefact e2e-report
- Badge E2E dans README
- Documentation CONTRIBUTING.md

Closes: roadmap/S6-01-tests-e2e-ci.md"
git push -u origin feature/s6-01-e2e-ci
```

**Checklist CI** :
- [ ] Workflow s'exécute sans erreur
- [ ] Job e2e-tests visible dans Actions
- [ ] Artefact e2e-report uploadé
- [ ] Badge E2E vert dans README

**4.3 Créer PR et valider** (30 min)

```bash
# Créer PR vers draft
gh pr create --title "feat(tests): Tests E2E automatisés CI (S6-01)" \
  --body "## Objectif
Intégration tests E2E existants dans CI GitHub Actions.

## Changements
- ✅ Script ci_runner.sh (orchestration tests)
- ✅ Générateur rapport HTML (generate_report.py)
- ✅ Job GitHub Actions avec parallélisation
- ✅ Upload artefact e2e-report (30 jours rétention)
- ✅ Badge E2E dans README
- ✅ Documentation CONTRIBUTING.md

## Tests
- [x] ci_runner.sh local : 5/5 scénarios passent
- [x] CI exécution : job e2e-tests ✅
- [x] Rapport HTML généré et accessible
- [x] Badge E2E fonctionnel

## Impact
- Détection régressions comportementales en CI
- Temps CI : +1-2 min (parallélisé)
- Couverture tests : +5 scénarios critiques

🤖 Generated with [Claude Code](https://claude.com/claude-code)" \
  --base draft
```

**Checklist PR** :
- [ ] PR créée vers `draft`
- [ ] CI passe (build + unit + e2e)
- [ ] Rapport e2e-report téléchargeable
- [ ] Revue Alex/Bertrand

---

## Critères d'acceptation

### Fonctionnels
- [ ] 5 scénarios E2E exécutés automatiquement en CI
- [ ] Rapport HTML généré et uploadé (artefact)
- [ ] Badge E2E ajouté dans README
- [ ] CI échoue si tests E2E KO

### Techniques
- [ ] Script ci_runner.sh fonctionnel
- [ ] Générateur HTML (generate_report.py) fonctionnel
- [ ] Job GitHub Actions configuré
- [ ] Parallélisation (5 jobs simultanés)
- [ ] Logs E2E capturés par scénario

### Documentation
- [ ] Section Tests E2E dans CONTRIBUTING.md
- [ ] Guide ajout nouveau test E2E
- [ ] tests/e2e/README.md mis à jour

### Performance
- [ ] Temps CI total : +1-2 min max (parallélisé)
- [ ] Rapport HTML < 500 KB

---

## Risques & Solutions

### Risque 1 : Tests E2E flaky (intermittents)
**Probabilité** : Moyenne
**Impact** : Moyen (faux négatifs CI)

**Solution** :
- Ajouter retry automatique (3 tentatives)
- Timeout par scénario (max 60s)
- Logs détaillés pour debugging

### Risque 2 : Temps CI trop long
**Probabilité** : Faible
**Impact** : Moyen (ralentit workflow)

**Solution** :
- Parallélisation avec matrix (déjà prévu)
- Cache dépendances Python (actions/cache)
- Skip tests E2E sur commits docs-only

### Risque 3 : Rapport HTML trop volumineux
**Probabilité** : Faible
**Impact** : Faible (quota artefacts)

**Solution** :
- Limiter logs à 1000 lignes/scénario
- Compresser rapport (gzip)
- Rétention 30 jours (pas 90)

---

## Métriques succès

**Avant S6-01** :
- Tests E2E manuels uniquement
- Régressions détectées tardivement
- Pas de rapport automatique

**Après S6-01** :
- 5 scénarios E2E automatisés
- Détection régressions en CI (<5 min)
- Rapport HTML disponible dans Actions
- Coverage tests : Unit (89.6%) + E2E (5 scénarios)

**Impact scoring** : 94/100 → 96/100 (+2 points Tests)

---

## Dépendances

**Bloquants** : Aucun (tests E2E existent)

**Facilitateurs** :
- S5-01 (Coverage 89%+) : Tests unitaires robustes
- S2-06 (Tests E2E manuels) : Scénarios éprouvés

**Bloque** :
- S6-02 (Notifications CI) : Notifications échecs E2E

---

## Notes d'implémentation

### Alternative : pytest pour tests E2E
**Option non retenue** : Réécrire tests shell en Python/pytest

**Justification** :
- Tests shell existants fonctionnels (6 scénarios)
- Temps migration : +4-6h
- Bénéfice faible (scripts shell suffisants pour E2E)
- Priorité : intégration rapide, pas refactoring

### Évolution future (v2.0)
- Tests E2E cross-platform (macOS, Windows)
- Tests charge (1000+ modules)
- Tests accessibilité PDF (pa11y)
- Intégration Playwright (tests UI MkDocs)
