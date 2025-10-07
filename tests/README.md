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
