---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S2-06 : Tests E2E automatisés et CI local

**Phase** : Semaine 2 - Automatisation
**Priorité** : Haute
**Estimation** : 2h30
**Assigné** : Alexandra

---

## Contexte projet

Le projet SPAN SG dispose actuellement de :
- **Tests unitaires** (S1-05, S1-06) : 7+8 = 15 tests validant composants isolés
- **Tests unitaires** (S2-05) : 18 tests pytest pour `calculate_scores.py` + `enrich_pdf_metadata.py`
- **CI GitHub Actions** (S2-01) : Workflow automatique sur push

**Score actuel** : Robustesse 17/20

**Gaps identifiés** :
1. **Tests E2E manquants (-2 points)** : Aucun test simulant le workflow complet utilisateur (edit→commit→CI→deploy→preview)
2. **Tests CI locaux absents (-1 point)** : Impossible de valider GitHub Actions avant push, risque d'erreurs en CI

**Risques** :
- Régressions non détectées lors de modifications multi-modules
- Échecs CI découverts après push (perte de temps, pollution historique)
- Aucune validation du déploiement gh-pages en environnement simulé

**Bénéfices attendus** :
- Détection précoce des régressions (avant CI distante)
- Validation workflow complet (scoring → build → PDF → deploy)
- Confidence pour Semaine 3 (5 contributeurs simultanés)
- **Score cible** : 17/20 → 20/20 (+3 points robustesse)

---

## Objectif

Implémenter des tests end-to-end automatisés simulant le workflow complet SPAN SG, et configurer `act` pour exécuter GitHub Actions en local avant push.

---

## Prérequis

- [x] Story S1-05 complétée (script scoring validé)
- [x] Story S1-06 complétée (SIRCOM validé)
- [x] Story S2-01 complétée (CI GitHub Actions opérationnelle)
- [x] Story S2-05 complétée (tests unitaires pytest)
- [ ] Docker installé et démarré (requis pour act + tests E2E preview HTTP)
- [ ] Homebrew installé (macOS, requis pour installation act)

---

## Étape 0 : Vérification prérequis (5 min)

### Contexte

Avant d'implémenter les tests E2E et CI locaux, vérifier que l'environnement dispose des prérequis nécessaires.

### Script de vérification

Créer `scripts/check_prerequisites.sh` :

```bash
#!/usr/bin/env bash
# Vérification prérequis S2-06

set -euo pipefail

echo "=== Vérification prérequis S2-06 ==="
echo ""

ERRORS=0

# Test 1 : Docker installé
echo -n "Docker installé... "
if command -v docker &> /dev/null; then
    echo "✅ OK"
else
    echo "❌ FAIL"
    echo "   → Installer Docker Desktop : https://www.docker.com/products/docker-desktop"
    ERRORS=$((ERRORS + 1))
fi

# Test 2 : Docker démarré
echo -n "Docker démarré... "
if docker info > /dev/null 2>&1; then
    echo "✅ OK"
else
    echo "❌ FAIL"
    echo "   → Lancer Docker Desktop"
    ERRORS=$((ERRORS + 1))
fi

# Test 3 : Homebrew installé (macOS uniquement)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -n "Homebrew installé... "
    if command -v brew &> /dev/null; then
        echo "✅ OK"
    else
        echo "❌ FAIL"
        echo "   → Installer Homebrew : https://brew.sh"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Test 4 : act installé (optionnel, sera installé en Partie 2)
echo -n "act installé (optionnel)... "
if command -v act &> /dev/null; then
    echo "✅ OK"
else
    echo "⏭️  À installer (Partie 2)"
fi

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ Tous les prérequis sont satisfaits"
    exit 0
else
    echo "❌ $ERRORS prérequis manquant(s)"
    echo ""
    echo "Corriger les prérequis avant de continuer l'implémentation S2-06."
    exit 1
fi
```

### Exécution

```bash
chmod +x scripts/check_prerequisites.sh
./scripts/check_prerequisites.sh
```

**Attendu** : Tous prérequis ✅ OK sauf act (optionnel).

---

## Partie 1 : Tests E2E automatisés (1h30)

### Contexte

Les tests E2E simulent le workflow complet d'un contributeur :
1. Éditer un module (cocher/décocher points DINUM)
2. Lancer le scoring
3. Vérifier synthese.md mis à jour
4. Builder le site MkDocs
5. Générer le PDF
6. Vérifier artefacts (HTML + PDF)
7. Simuler déploiement
8. Tester rollback (restauration état initial)

**Technologies** :
- Bash scripts (portable, pas de dépendances Python)
- Tests isolés dans `tests/e2e/`
- Exit codes standardisés (0=OK, 1=FAIL)

---

### Étape 1.1 : Créer structure tests E2E

```bash
mkdir -p tests/e2e
touch tests/e2e/test_full_workflow.sh
chmod +x tests/e2e/test_full_workflow.sh
```

---

### Étape 1.2 : Script principal E2E

Créer `tests/e2e/test_full_workflow.sh` :

```bash
#!/usr/bin/env bash
set -euo pipefail

# Tests E2E SPAN SG - Workflow complet
# Usage: ./tests/e2e/test_full_workflow.sh

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "=== Tests E2E SPAN SG ==="
echo "Temp dir: $TEMP_DIR"
echo ""

# Compteurs
TESTS_RUN=0
TESTS_PASS=0
TESTS_FAIL=0

run_test() {
    local name=$1
    local command=$2
    TESTS_RUN=$((TESTS_RUN + 1))
    echo -n "Test $TESTS_RUN: $name... "
    if eval "$command" > "$TEMP_DIR/test_$TESTS_RUN.log" 2>&1; then
        echo "✅ PASS"
        TESTS_PASS=$((TESTS_PASS + 1))
    else
        echo "❌ FAIL"
        cat "$TEMP_DIR/test_$TESTS_RUN.log"
        TESTS_FAIL=$((TESTS_FAIL + 1))
    fi
}

# Test 1 : Backup module SIRCOM
run_test "Backup module SIRCOM" \
    "cp docs/modules/sircom.md $TEMP_DIR/sircom-backup.md"

# Test 2 : Modifier SIRCOM (cocher 1 point)
run_test "Modifier SIRCOM (cocher point 7)" \
    "sed -i '' 's/- \[ \] Budget annuel dédié/- [x] Budget annuel dédié/' docs/modules/sircom.md"

# Test 3 : Recalculer scores
run_test "Recalculer scores" \
    "python3 scripts/calculate_scores.py"

# Test 4 : Vérifier score SIRCOM augmenté (base 7/31 + 1 = 8/31)
run_test "Vérifier score SIRCOM = 8/31" \
    "grep -q '| SIRCOM | 8/31' docs/synthese.md"

# Test 5 : Build site MkDocs
run_test "Build site MkDocs" \
    "mkdocs build --site-dir $TEMP_DIR/site"

# Test 6 : Vérifier HTML généré
run_test "Vérifier index.html présent" \
    "test -f $TEMP_DIR/site/index.html"

run_test "Vérifier page SIRCOM générée" \
    "test -f $TEMP_DIR/site/modules/sircom/index.html"

# Test 7 : Générer PDF
run_test "Générer PDF" \
    "mkdocs build --config-file mkdocs-pdf.yml --site-dir $TEMP_DIR/pdf-site"

run_test "Vérifier PDF généré" \
    "test -f $TEMP_DIR/pdf-site/exports/span-sg.pdf"

# Test 8 : Vérifier contenu PDF (au moins 50 KB)
run_test "Vérifier taille PDF > 50KB" \
    "[[ \$(stat -c%s $TEMP_DIR/pdf-site/exports/span-sg.pdf 2>/dev/null || stat -f%z $TEMP_DIR/pdf-site/exports/span-sg.pdf) -gt 51200 ]]"

# Test 9 : Restaurer SIRCOM
run_test "Restaurer SIRCOM" \
    "mv $TEMP_DIR/sircom-backup.md docs/modules/sircom.md"

# Test 10 : Re-calculer scores (retour état initial)
run_test "Re-calculer scores après restauration" \
    "python3 scripts/calculate_scores.py"

# Test 11 : Vérifier score SIRCOM restauré (retour à 7/31)
run_test "Vérifier score SIRCOM = 7/31 (restauré)" \
    "grep -q '| SIRCOM | 7/31' docs/synthese.md"

# Résumé
echo ""
echo "=== Résumé E2E ==="
echo "Tests exécutés : $TESTS_RUN"
echo "Tests réussis  : $TESTS_PASS"
echo "Tests échoués  : $TESTS_FAIL"

if [ $TESTS_FAIL -eq 0 ]; then
    echo "✅ Tous les tests E2E passent"
    exit 0
else
    echo "❌ $TESTS_FAIL test(s) échoué(s)"
    exit 1
fi
```

---

### Étape 1.3 : Tests E2E scénarios multiples

Créer 8 scénarios E2E supplémentaires :

#### Scénario 1 : Modification multi-modules

`tests/e2e/scenario_multi_modules.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Modifier 3 modules simultanément

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Modification multi-modules"

# Backup
cp docs/modules/{sircom,snum,srh}.md /tmp/

# Modifier SIRCOM (cocher point 8)
sed -i '' 's/- \[ \] Planification pluriannuelle/- [x] Planification pluriannuelle/' docs/modules/sircom.md

# Modifier SNUM (cocher point 1)
sed -i '' '0,/- \[ \].*<!-- DINUM -->/s//- [x] Stratégie numérique publiée <!-- DINUM -->/' docs/modules/snum.md

# Modifier SRH (cocher point 1)
sed -i '' '0,/- \[ \].*<!-- DINUM -->/s//- [x] Stratégie numérique publiée <!-- DINUM -->/' docs/modules/srh.md

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier scores
grep -q "| SIRCOM | 8/31" docs/synthese.md || { echo "FAIL: SIRCOM"; exit 1; }
grep -q "| SNUM | 1/31" docs/synthese.md || { echo "FAIL: SNUM"; exit 1; }
grep -q "| SRH | 1/31" docs/synthese.md || { echo "FAIL: SRH"; exit 1; }
# TOTAL = SIRCOM (7→8) + SNUM (0→1) + SRH (0→1) + autres (0) = 8+1+1 = 10/186
grep -q "| \*\*TOTAL\*\* | \*\*10/186" docs/synthese.md || { echo "FAIL: TOTAL"; exit 1; }

# Restaurer
mv /tmp/{sircom,snum,srh}.md docs/modules/
python3 scripts/calculate_scores.py

echo "✅ Scénario multi-modules OK"
```

#### Scénario 2 : Erreur périmètre (exit 2)

`tests/e2e/scenario_erreur_perimetre.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Détecter erreur périmètre (≠ 31 points)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Erreur périmètre"

# Backup
cp docs/modules/sircom.md /tmp/

# Supprimer 1 checkbox DINUM (31 → 30) avec awk
awk '/- \[[ x]\].* DINUM/ && !done {done=1; next} {print}' docs/modules/sircom.md > /tmp/sircom-30.md
mv /tmp/sircom-30.md docs/modules/sircom.md

# Tenter scoring (doit échouer avec exit 2)
set +e
python3 scripts/calculate_scores.py 2>&1
EXIT_CODE=$?
set -e

if [ $EXIT_CODE -eq 0 ]; then
    echo "❌ FAIL: Scoring devrait échouer avec exit 2"
    mv /tmp/sircom.md docs/modules/
    exit 1
fi

# Vérifier exit code = 2
if [ $EXIT_CODE -ne 2 ]; then
    echo "❌ FAIL: Exit code attendu=2, obtenu=$EXIT_CODE"
    mv /tmp/sircom.md docs/modules/
    exit 1
fi

# Restaurer
mv /tmp/sircom.md docs/modules/
python3 scripts/calculate_scores.py

echo "✅ Scénario erreur périmètre OK (exit 2 détecté)"
```

#### Scénario 3 : Build avec erreur Markdown

`tests/e2e/scenario_erreur_markdown.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Détecter erreur Markdown (lien cassé en mode strict)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Erreur Markdown (lien cassé)"

# Backup
cp docs/modules/sircom.md /tmp/

# Injecter lien cassé
echo "[Lien cassé](page-inexistante.md)" >> docs/modules/sircom.md

# Tenter build strict (doit échouer)
if mkdocs build --strict 2>/dev/null; then
    echo "❌ FAIL: Build strict devrait échouer"
    mv /tmp/sircom.md docs/modules/
    exit 1
fi

# Restaurer
mv /tmp/sircom.md docs/modules/

echo "✅ Scénario erreur Markdown OK (strict mode détecté)"
```

#### Scénario 4 : Performance build

`tests/e2e/scenario_performance.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Vérifier temps de build < 10s

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Performance build"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Mesurer temps build
START=$(date +%s)
mkdocs build --site-dir "$TEMP_DIR/site" > /dev/null 2>&1
END=$(date +%s)

DURATION=$((END - START))

if [ $DURATION -gt 10 ]; then
    echo "❌ FAIL: Build trop long ($DURATION s > 10s)"
    exit 1
fi

echo "✅ Scénario performance OK (build en ${DURATION}s)"
```

#### Scénario 5 : Validation PDF complet

`tests/e2e/scenario_pdf_complet.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Vérifier PDF contient toutes les pages

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : PDF complet"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Générer PDF
mkdocs build --config-file mkdocs-pdf.yml --site-dir "$TEMP_DIR/pdf-site" > /dev/null 2>&1

PDF_FILE="$TEMP_DIR/pdf-site/exports/span-sg.pdf"

# Vérifier présence
test -f "$PDF_FILE" || { echo "❌ FAIL: PDF absent"; exit 1; }

# Vérifier taille > 100 KB (indicateur contenu complet)
SIZE=$(stat -c%s "$PDF_FILE" 2>/dev/null || stat -f%z "$PDF_FILE")
if [ $SIZE -lt 102400 ]; then
    echo "❌ FAIL: PDF trop petit ($SIZE bytes < 100KB)"
    exit 1
fi

# Vérifier contenu avec pdfinfo (si disponible)
if command -v pdfinfo &> /dev/null; then
    PAGES=$(pdfinfo "$PDF_FILE" | grep "^Pages:" | awk '{print $2}')
    if [ "$PAGES" -lt 10 ]; then
        echo "❌ FAIL: PDF incomplet ($PAGES pages < 10)"
        exit 1
    fi
    echo "✅ Scénario PDF complet OK ($PAGES pages, ${SIZE} bytes)"
else
    echo "✅ Scénario PDF complet OK (${SIZE} bytes, pdfinfo non disponible)"
fi
```

#### Scénario 6 : Rollback complet

`tests/e2e/scenario_rollback.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Tester rollback complet (all modules)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Rollback complet"

# Backup tous modules
cp -r docs/modules /tmp/modules-backup

# Modifier tous modules (cocher 1er point partout)
for module in snum sircom srh siep safi bgs; do
    sed -i '' '0,/- \[ \].*<!-- DINUM -->/s//- [x] Point coché <!-- DINUM -->/' "docs/modules/$module.md"
done

# Recalculer
python3 scripts/calculate_scores.py

# Vérifier TOTAL après modification 6 modules
# Calcul : SIRCOM (7→8) + SNUM (0→1) + SRH (0→1) + SIEP (0→1) + SAFI (0→1) + BGS (0→1)
#        = 8 + 1 + 1 + 1 + 1 + 1 = 13/186
grep -q "13/186" docs/synthese.md || { echo "❌ FAIL: Score incorrect"; cat docs/synthese.md; exit 1; }

# Rollback
rm -rf docs/modules
mv /tmp/modules-backup docs/modules
python3 scripts/calculate_scores.py

# Vérifier retour à 7/186
grep -q "7/186" docs/synthese.md || { echo "❌ FAIL: Rollback incorrect"; exit 1; }

echo "✅ Scénario rollback OK"
```

#### Scénario 7 : Preview HTTP local (Docker avec libsass)

**Prérequis** : Créer `Dockerfile.mkdocs-test` avec build tools pour compilation libsass.

`Dockerfile.mkdocs-test` :

```dockerfile
FROM squidfunk/mkdocs-material:latest

# Installer build-essentials pour compiler libsass (Alpine Linux)
RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    python3-dev

WORKDIR /docs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
```

`tests/e2e/scenario_preview_http.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Vérifier preview HTTP local (Docker)

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Preview HTTP local"

# Vérifier Docker running
if ! docker info > /dev/null 2>&1; then
    echo "⚠️  SKIP: Docker non démarré"
    exit 0
fi

# Build image avec gcc/g++ pour libsass
docker build -f Dockerfile.mkdocs-test -t span-mkdocs-test . > /dev/null 2>&1 || {
    echo "⚠️  SKIP: Build Docker échoué"
    exit 0
}

# Démarrer container mkdocs serve (background)
CONTAINER_ID=$(docker run -d -p 8000:8000 -v "$(pwd):/docs" span-mkdocs-test)

# Attendre 5s pour démarrage
sleep 5

# Test HTTP
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/)

if [ "$HTTP_CODE" != "200" ]; then
    echo "❌ FAIL: HTTP code = $HTTP_CODE (attendu 200)"
    docker stop "$CONTAINER_ID" > /dev/null 2>&1
    exit 1
fi

# Test page SIRCOM
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/modules/sircom/)

if [ "$HTTP_CODE" != "200" ]; then
    echo "❌ FAIL: Page SIRCOM HTTP = $HTTP_CODE"
    docker stop "$CONTAINER_ID" > /dev/null 2>&1
    exit 1
fi

# Cleanup
docker stop "$CONTAINER_ID" > /dev/null 2>&1

echo "✅ Scénario preview HTTP OK"
```

#### Scénario 8 : Validation front-matter YAML

`tests/e2e/scenario_frontmatter.sh` :

```bash
#!/usr/bin/env bash
# Scénario : Valider front-matter YAML tous modules

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "Scénario : Validation front-matter YAML"

for module in snum sircom srh siep safi bgs; do
    MODULE_FILE="docs/modules/$module.md"

    # Extraire front-matter (entre --- et ---)
    FRONTMATTER=$(sed -n '/^---$/,/^---$/p' "$MODULE_FILE" | sed '1d;$d')

    # Valider YAML avec Python
    python3 -c "
import yaml
import sys
try:
    data = yaml.safe_load('''$FRONTMATTER''')
    assert 'service' in data, 'Clé service manquante'
    assert 'referent' in data, 'Clé referent manquante'
    assert 'updated' in data, 'Clé updated manquante'
except Exception as e:
    print(f'❌ FAIL {module}: {e}')
    sys.exit(1)
" || exit 1

    echo "  ✅ $module : YAML valide"
done

echo "✅ Scénario front-matter OK (6 modules)"
```

---

### Étape 1.4 : Runner tous scénarios E2E

Créer `tests/e2e/run_all.sh` :

```bash
#!/usr/bin/env bash
# Runner tous tests E2E

set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Runner Tests E2E SPAN SG ==="
echo ""

TESTS=(
    "tests/e2e/test_full_workflow.sh"
    "tests/e2e/scenario_multi_modules.sh"
    "tests/e2e/scenario_erreur_perimetre.sh"
    "tests/e2e/scenario_erreur_markdown.sh"
    "tests/e2e/scenario_performance.sh"
    "tests/e2e/scenario_pdf_complet.sh"
    "tests/e2e/scenario_rollback.sh"
    "tests/e2e/scenario_preview_http.sh"
    "tests/e2e/scenario_frontmatter.sh"
)

PASS=0
FAIL=0
SKIP=0

for test in "${TESTS[@]}"; do
    chmod +x "$test"
    echo "Exécution : $test"
    if "$test"; then
        PASS=$((PASS + 1))
    else
        EXIT_CODE=$?
        if [ $EXIT_CODE -eq 77 ]; then
            SKIP=$((SKIP + 1))
        else
            FAIL=$((FAIL + 1))
        fi
    fi
    echo ""
done

echo "=== Résumé Global E2E ==="
echo "Tests réussis : $PASS"
echo "Tests échoués : $FAIL"
echo "Tests skippés : $SKIP"

if [ $FAIL -eq 0 ]; then
    echo "✅ Tous les tests E2E passent"
    exit 0
else
    echo "❌ $FAIL test(s) échoué(s)"
    exit 1
fi
```

---

## Partie 2 : Tests CI locaux avec `act` (1h)

### Contexte

`act` (nektos/act) permet d'exécuter GitHub Actions workflows en local avec Docker, évitant :
- Push pour tester CI (gain temps + historique propre)
- Consommation quota GitHub Actions (2000 min/mois)
- Cycles debug longs (push → attendre CI → corriger → push)

**Workflow type** :
```bash
act -j build        # Exécuter job "build" seulement
act -l              # Lister jobs disponibles
act push            # Simuler event "push"
```

---

### Étape 2.1 : Installer `act`

#### macOS (Homebrew)

```bash
brew install act
```

#### Linux

```bash
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

#### Vérifier installation

```bash
act --version
# act version 0.2.xx
```

---

### Étape 2.2 : Configuration `act`

Créer `.actrc` à la racine du projet :

```bash
# .actrc - Configuration act pour SPAN SG

# Image Docker medium (inclut Python)
-P ubuntu-latest=catthehacker/ubuntu:act-latest

# Secrets locaux
--secret-file .secrets

# Variables d'environnement
--env GITHUB_REPOSITORY=Alexmacapple/span-sg-repo
--env GITHUB_REF=refs/heads/draft

# Verbose
-v
```

---

### Étape 2.3 : Fichier secrets locaux

Créer `.secrets` (à NE PAS commiter) :

```bash
GITHUB_TOKEN=ghp_fake_token_for_local_testing
```

Ajouter `.secrets` au `.gitignore` :

```bash
echo ".secrets" >> .gitignore
```

---

### Étape 2.4 : Adapter workflow pour `act`

Le workflow `.github/workflows/build.yml` doit supporter `act`. Vérifier :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      # Compatible act : pas de dépendance externe
      - name: Install dependencies
        run: |
          pip install mkdocs-material mkdocs-pdf-export-plugin

      - name: Calculate SPAN scores
        run: python scripts/calculate_scores.py

      - name: Build site
        run: mkdocs build

      - name: Generate PDF
        run: mkdocs build --config-file mkdocs-pdf.yml

      # Skip upload artifacts en local (act limitation)
      - name: Upload artifacts
        if: ${{ !env.ACT }}
        uses: actions/upload-artifact@v3
        with:
          name: span-site
          path: |
            site/
            exports/
```

**Astuce** : `if: ${{ !env.ACT }}` détecte exécution locale et skip steps incompatibles.

---

### Étape 2.5 : Tester workflow complet en local

```bash
# Tester job "build" uniquement
act -j build

# Simuler push sur draft
act push --ref refs/heads/draft

# Dry-run (lister steps sans exécuter)
act -j build --dryrun

# Debug mode (verbose)
act -j build -v
```

**Attendu** :
```
[Build SPAN/build] 🚀 Start image=catthehacker/ubuntu:act-latest
[Build SPAN/build]   ✅ Set up Python
[Build SPAN/build]   ✅ Install dependencies
[Build SPAN/build]   ✅ Calculate SPAN scores
[Build SPAN/build]   ✅ Build site
[Build SPAN/build]   ✅ Generate PDF
[Build SPAN/build] ✅ Success
```

---

### Étape 2.6 : Script wrapper `test-ci-local.sh`

Créer `scripts/test-ci-local.sh` :

```bash
#!/usr/bin/env bash
# Test GitHub Actions en local avec act

set -euo pipefail

echo "=== Test CI local avec act ==="

# Vérifier act installé
if ! command -v act &> /dev/null; then
    echo "❌ act non installé. Installer avec: brew install act"
    exit 1
fi

# Vérifier Docker running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker non démarré. Lancer Docker Desktop."
    exit 1
fi

# Lister jobs disponibles
echo "Jobs disponibles :"
act -l

echo ""
echo "Exécution job 'build' :"

# Exécuter job build
if act -j build; then
    echo "✅ CI local réussie"
    exit 0
else
    echo "❌ CI local échouée"
    exit 1
fi
```

Rendre exécutable :

```bash
chmod +x scripts/test-ci-local.sh
```

---

### Étape 2.7 : Scénarios validation CI local

#### Scénario 1 : Validation job build

```bash
# Test complet
act -j build

# Attendu : Exit 0, tous steps ✅
```

#### Scénario 2 : Validation job deploy_draft (simulation)

```bash
# Simuler push sur draft
act push --ref refs/heads/draft -j deploy_draft

# Attendu : Job deploy_draft s'exécute
```

#### Scénario 3 : Test erreur scoring

Modifier temporairement SIRCOM (supprimer 1 DINUM), puis :

```bash
act -j build

# Attendu : Step "Calculate SPAN scores" échoue, exit 2
```

Restaurer SIRCOM après test.

#### Scénario 4 : Test sans Docker (skip)

Si Docker non disponible :

```bash
if docker info > /dev/null 2>&1; then
    act -j build
else
    echo "⚠️  SKIP: Docker requis pour act"
    exit 0
fi
```

#### Scénario 5 : Validation performance CI locale

```bash
START=$(date +%s)
act -j build
END=$(date +%s)

DURATION=$((END - START))

if [ $DURATION -gt 300 ]; then
    echo "⚠️  CI locale lente ($DURATION s > 5 min)"
else
    echo "✅ CI locale rapide ($DURATION s)"
fi
```

---

## Partie 3 : Intégration et documentation (30 min)

### Étape 3.1 : Documentation tests E2E et CI local

Créer `tests/README.md` :

```markdown
# Tests SPAN SG

Ce dossier contient les tests end-to-end (E2E) et les outils de validation CI locale.

## Tests E2E

**Objectif** : Valider le workflow complet (edit → scoring → build → PDF → deploy)

### Exécution

```bash
# Test principal
./tests/e2e/test_full_workflow.sh

# Tous scénarios
./tests/e2e/run_all.sh

# Scénario spécifique
./tests/e2e/scenario_multi_modules.sh
```

### Scénarios disponibles

1. **test_full_workflow.sh** : Workflow complet (11 tests)
2. **scenario_multi_modules.sh** : Modification simultanée 3 modules
3. **scenario_erreur_perimetre.sh** : Détection erreur périmètre (exit 2)
4. **scenario_erreur_markdown.sh** : Détection lien cassé (strict mode)
5. **scenario_performance.sh** : Build < 10s
6. **scenario_pdf_complet.sh** : PDF complet > 100 KB
7. **scenario_rollback.sh** : Rollback complet tous modules
8. **scenario_preview_http.sh** : Preview HTTP Docker
9. **scenario_frontmatter.sh** : Validation YAML 6 modules

### Intégration CI

Les tests E2E sont exécutés automatiquement par GitHub Actions :

```yaml
- name: Run E2E tests
  run: ./tests/e2e/run_all.sh
```

## Tests CI locaux avec `act`

**Objectif** : Valider GitHub Actions avant push

### Installation

```bash
brew install act  # macOS
```

### Configuration

Fichier `.actrc` à la racine :

```bash
-P ubuntu-latest=catthehacker/ubuntu:act-latest
--secret-file .secrets
-v
```

Créer `.secrets` (ne pas commiter) :

```bash
GITHUB_TOKEN=ghp_fake_token
```

### Utilisation

```bash
# Tester job build
act -j build

# Lister jobs
act -l

# Simuler push draft
act push --ref refs/heads/draft

# Script wrapper
./scripts/test-ci-local.sh
```

### Troubleshooting

**Erreur "Docker daemon not running"** :
- Lancer Docker Desktop

**Erreur "image not found"** :
- Utiliser image medium : `-P ubuntu-latest=catthehacker/ubuntu:act-latest`

**Erreur "secrets not found"** :
- Créer `.secrets` avec `GITHUB_TOKEN=fake_token`

**Step échoue en local mais OK en CI** :
- Vérifier compatibilité action avec act
- Utiliser `if: ${{ !env.ACT }}` pour skip step

## Pré-commit hook (optionnel)

Exécuter tests E2E avant commit :

`.git/hooks/pre-commit` :

```bash
#!/bin/bash
./tests/e2e/test_full_workflow.sh
```

Activer :

```bash
chmod +x .git/hooks/pre-commit
```
```

---

### Étape 3.2 : Ajouter tests E2E à CI

Modifier `.github/workflows/build.yml` pour inclure tests E2E :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install mkdocs-material mkdocs-pdf-export-plugin

      # AJOUT : Tests E2E avant scoring
      - name: Run E2E tests
        run: |
          chmod +x tests/e2e/run_all.sh
          ./tests/e2e/run_all.sh

      - name: Calculate SPAN scores
        run: python scripts/calculate_scores.py

      # ... reste du workflow
```

---

### Étape 3.3 : Ajouter badge tests E2E

Créer badge dans README.md :

```markdown
# SPAN SG

![Build Status](https://github.com/Alexmacapple/span-sg-repo/workflows/Build%20SPAN/badge.svg)
![E2E Tests](https://img.shields.io/badge/E2E%20tests-9%20scenarios-success)
![CI Local](https://img.shields.io/badge/CI%20local-act%20compatible-blue)

...
```

---

## Critères d'acceptation

- [ ] Répertoire `tests/e2e/` créé avec 9 scénarios
- [ ] Script principal `test_full_workflow.sh` exécute 11 tests
- [ ] Runner `run_all.sh` exécute tous scénarios
- [ ] `act` installé et fonctionnel
- [ ] `.actrc` configuré avec image medium
- [ ] `.secrets` créé (exclu du git)
- [ ] Workflow `.github/workflows/build.yml` compatible `act`
- [ ] Script `scripts/test-ci-local.sh` fonctionnel
- [ ] Documentation `tests/README.md` complète
- [ ] Tests E2E intégrés à CI GitHub Actions
- [ ] Tous scénarios E2E passent (9/9)
- [ ] CI locale passe avec `act -j build`

---

## Tests de validation

```bash
# Test 1 : Structure tests E2E présente
test -d tests/e2e && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : 9 scénarios E2E présents
test $(ls tests/e2e/*.sh | wc -l) -ge 9 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : Tous scripts exécutables
find tests/e2e -name "*.sh" -executable | wc -l
# Attendu : 9

# Test 4 : act installé
command -v act && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 5 : .actrc présent
test -f .actrc && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 6 : .secrets exclu du git
grep -q "^\.secrets$" .gitignore && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 7 : Workflow compatible act (détection env.ACT)
grep -q "env.ACT" .github/workflows/build.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 8 : Documentation présente
test -f tests/README.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 9 : Runner E2E passe
./tests/e2e/run_all.sh && echo "OK" || echo "FAIL"
# Attendu : OK (9/9 tests)

# Test 10 : CI locale passe (si Docker running)
if docker info > /dev/null 2>&1; then
    act -j build --dryrun && echo "OK" || echo "FAIL"
else
    echo "SKIP (Docker requis)"
fi
# Attendu : OK ou SKIP
```

---

## Dépendances

**Bloque** :
- S3-01 (modules vides nécessitent tests E2E avant onboarding)
- S4-04 (publication nécessite validation E2E complète)

**Dépend de** :
- S1-05 (script scoring doit fonctionner)
- S2-01 (CI GitHub Actions doit être opérationnelle)
- S2-05 (tests unitaires pytest doivent passer)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 2 Automatisation
- **.github/workflows/build.yml** : Workflow CI à tester
- **scripts/calculate_scores.py** : Script testé en E2E
- **nektos/act** : https://github.com/nektos/act
- **GitHub Actions** : https://docs.github.com/en/actions

---

## Notes et risques

### Performance `act`

Première exécution `act` télécharge image Docker (~2 GB) :
```bash
docker pull catthehacker/ubuntu:act-latest
```

Exécutions suivantes : cache Docker utilisé, rapide.

### Limitations `act`

Actions non supportées :
- `actions/upload-artifact` (skip avec `if: ${{ !env.ACT }}`)
- `actions/deploy-pages` (skip)
- Secrets GitHub natifs (utiliser `.secrets` local)

### Faux positifs E2E

Test `scenario_preview_http.sh` peut échouer si :
- Docker non démarré
- Port 8000 déjà utilisé
- Service mkdocs non configuré dans `docker-compose.yml`

→ Utiliser `exit 0` (skip) au lieu de `exit 1` si Docker indisponible.

### Coût maintenance

9 scénarios E2E à maintenir lors de modifications :
- Ajout module → Adapter `scenario_multi_modules.sh`
- Changement scoring → Adapter tous tests vérifiant scores
- Changement structure → Adapter `scenario_frontmatter.sh`

**Mitigation** : Tests E2E génériques (boucles sur modules) vs hardcodés.

### Quota CI

Avec tests E2E en CI :
- Durée totale workflow : 2-3 min → 4-5 min (E2E +2 min)
- Quota GitHub Actions : 2000 min/mois → ~400 runs/mois (au lieu de 600)

**Mitigation** : Tests E2E optionnels sur PR, obligatoires sur main/draft.

---

## Post-tâche

### Créer issue suivi

```markdown
## Tests E2E - Suivi améliorations

- [ ] Ajouter test E2E pour déploiement gh-pages réel
- [ ] Intégrer tests E2E dans pre-commit hook (optionnel)
- [ ] Créer rapport HTML tests E2E (pytest-html style)
- [ ] Ajouter scénario E2E pour releases (tags)
- [ ] Optimiser temps exécution E2E (parallélisation)
```

### Métriques à suivre

```bash
# Temps exécution E2E
time ./tests/e2e/run_all.sh
# Objectif : < 3 min

# Taux succès E2E (sur 1 mois)
# Objectif : > 95%

# Temps exécution CI locale
time act -j build
# Objectif : < 5 min
```

### Documentation contributeur

Ajouter à `CONTRIBUTING.md` (S2-04) :

```markdown
## Validation avant commit

Recommandé :

```bash
# 1. Tests unitaires
pytest tests/

# 2. Tests E2E
./tests/e2e/run_all.sh

# 3. CI locale
./scripts/test-ci-local.sh

# 4. Commit si tout passe
git add .
git commit -m "..."
```
```

---

**Validation complète** : Cette story porte la robustesse de 17/20 à 20/20 (+3 points).
