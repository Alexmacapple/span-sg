# Guide Performance SPAN SG

Documentation architecture cache et optimisations CI/CD.

## Objectif

**Score Performance : 10/10**

- Build times optimaux (~8-10 min)
- Cache efficace (pip, Docker layers)
- Parallélisation maximale (E2E tests)

---

## Architecture Cache

### 1. Cache Pip (setup-python natif)

**Implementation :** `.github/workflows/build.yml:17-25`

```yaml
- name: Setup Python 3.11
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'
    cache: 'pip'
    cache-dependency-path: |
      requirements-dsfr.txt
      requirements-dev.txt
      requirements-security.txt
```

**Caracteristiques :**
- Cache natif GitHub Actions (optimise pour pip)
- Clef basee sur hash des 3 fichiers requirements
- Invalidation automatique si dependances changent

**Gain estim

e :** ~10-20s sur install dependencies (cache hit)

### 2. Cache Docker Layers

**Implementation :** `.github/workflows/build.yml:163-184`

```yaml
- name: Cache Docker layers
  uses: actions/cache@v3
  with:
    path: /tmp/.buildx-cache
    key: ${{ runner.os }}-buildx-${{ hashFiles('Dockerfile.mkdocs-test', 'requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-buildx-

- name: Build test Docker image
  run: |
    docker buildx build \
      -f Dockerfile.mkdocs-test \
      -t mkdocs-test:latest \
      --cache-from type=local,src=/tmp/.buildx-cache \
      --cache-to type=local,dest=/tmp/.buildx-cache-new,mode=max \
      --load \
      .

- name: Move Docker cache
  run: |
    rm -rf /tmp/.buildx-cache
    mv /tmp/.buildx-cache-new /tmp/.buildx-cache || true
```

**Caracteristiques :**
- Cache buildx layers incrementaux
- Strategy move pour eviter problemes cache corruption
- Clef basee sur Dockerfile + requirements.txt

**Gain estime :** ~30-60s sur build Docker image (cache hit)

---

## Parallelisation E2E Tests

**Implementation :** `tests/e2e/ci_runner.sh:59-61`

```bash
# Executer scenarios en parallele (3 workers max)
printf "%s\n" "${SCENARIOS[@]}" | xargs -n 1 -P 3 -I {} bash -c 'run_scenario "{}"'
```

**Caracteristiques :**
- 3 workers simultanees (xargs -P 3)
- Tests independants executes en parallele
- Logs individuels par scenario

**Gain mesure :** 300s → ~100s (speedup 3x)

**Note :** Deja implemente dans v1.2.1-quality (commit 8216382)

---

## Build HTML (Strict Mode)

### Configuration MkDocs

**Fichier :** `mkdocs-dsfr.yml:8`

```yaml
strict: true
```

**Pourquoi conserve ?**
- Detection erreurs liens casses
- Validation references internes
- Qualite documentation garantie

**Ralentissement acceptable :** ~5-10s additionnel pour validation exhaustive

### Pas de Build Incremental

**Raison :** MkDocs ne supporte pas nativement le build incremental (flag `--dirty` non fiable pour production)

**Alternative envisagee :** Cache `site/` (rejete car compromet reproductibilite)

---

## Benchmarks Build Times

### Sans Cache (cold build)

```
Setup Python              : ~20s
Install dependencies      : ~90s
Build MkDocs              : ~15s
Generate PDF              : ~40s
Build Docker image        : ~120s
Run E2E tests (parallele) : ~100s
Upload artifacts          : ~30s
Deploy                    : ~20s
---
Total                     : ~435s (~7 min)
```

### Avec Cache (warm build)

```
Setup Python              : ~20s
Install dependencies      : ~30s  (cache pip)
Build MkDocs              : ~15s
Generate PDF              : ~40s
Build Docker image        : ~60s  (cache Docker layers)
Run E2E tests (parallele) : ~100s
Upload artifacts          : ~30s
Deploy                    : ~20s
---
Total                     : ~315s (~5 min)
```

**Gain total cache :** ~120s (27% reduction)

---

## Optimisations Futures Envisagees

### 1. Cache MkDocs Build

**Non implemente :** Compromet reproductibilite

```yaml
# NE PAS FAIRE (exemple contre-productif)
- name: Cache MkDocs site
  uses: actions/cache@v3
  with:
    path: site/
    key: mkdocs-${{ hashFiles('docs/**/*.md') }}
```

**Raison :** Build MkDocs doit etre reproductible entre environnements.

### 2. Parallelisation Jobs CI

**Deja optimal :** 1 job avec steps sequentiels necessaires (dependances entre steps)

**Alternative envisagee :** Split en 3 jobs (lint, build, test) → Rejete car augmente temps total (overhead artifacts sharing)

### 3. Pre-commit Hooks Optimisation

**Actuel :** pre-commit hooks executent sur all-files en CI (ligne 45)

**Optimisation possible :** Executer seulement sur fichiers modifies (`--from-ref` et `--to-ref`)

**Non prioritaire :** Temps execution ~10-15s acceptable

---

## Monitoring Performance

### GitHub Actions Insights

```bash
# Lister derniers builds avec durées
gh run list --branch main --limit 10 --json conclusion,databaseId,displayTitle,createdAt,updatedAt

# Voir details build specifique
gh run view <run-id> --log
```

### Benchmarking Local

```bash
# Mesurer temps build MkDocs
time mkdocs build --config-file mkdocs-dsfr.yml

# Mesurer temps generation PDF
time ENABLE_PDF_EXPORT=1 mkdocs build --config-file mkdocs-dsfr-pdf.yml

# Mesurer temps E2E tests
time bash tests/e2e/ci_runner.sh
```

### Metriques Benchmark CI

**Script :** `scripts/benchmark.py`

```bash
# Execution manuelle
python scripts/benchmark.py > benchmark-$(git rev-parse --short HEAD).json

# Analyse historique
python scripts/analyze_benchmarks.py benchmark-*.json
```

**Retention :** 365 jours (artefacts GitHub Actions)

---

## Troubleshooting

### Cache Pip Ne Fonctionne Pas

**Symptome :** Temps install dependencies reste ~90s

**Diagnostic :**
```bash
gh run view <run-id> --log | grep -A 10 "Setup Python 3.11"
```

**Solutions :**
1. Verifier hash fichiers requirements inchange
2. Forcer invalidation cache (modifier clef manuellement)
3. Verifier limites quota cache GitHub (10 GB par repo)

### Cache Docker Trop Volumineux

**Symptome :** Step "Cache Docker layers" depasse timeout

**Solutions :**
```bash
# Nettoyer cache ancien
- name: Prune Docker cache
  run: |
    docker builder prune --force --filter until=168h  # 7 jours
```

### E2E Tests Echouent En Parallele

**Symptome :** Tests passent sequentiellement mais echouent en parallele

**Diagnostic :** Conflits etat partage (fichiers docs/modules/*.md)

**Solution :** Verifier `git checkout --` dans `ci_runner.sh:38` (restauration etat propre)

---

## References

- GitHub Actions Cache: https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows
- Docker Buildx Cache: https://docs.docker.com/build/cache/backends/local/
- MkDocs Performance: https://www.mkdocs.org/user-guide/configuration/#strict
- Benchmarking CI: `scripts/benchmark.py`, `scripts/analyze_benchmarks.py`
