# Architecture Infrastructure - Runtime et Déploiement

Documentation détaillée de l'infrastructure runtime, ressources système et architecture de déploiement SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-22

---

## 1. Vue d'ensemble Infrastructure

Architecture cloud-native basée sur GitHub Actions et GitHub Pages.

```mermaid
graph TB
    subgraph "Developer Workstation"
        DEV[fa:fa-laptop Poste développeur<br/>macOS/Linux/Windows]
        DOCKER[fa:fa-docker Docker Desktop<br/>mkdocs-dsfr:latest]
        VSCODE[fa:fa-code VS Code<br/>Extension MkDocs]
    end

    subgraph "GitHub Cloud"
        direction TB
        subgraph "GitHub Repository"
            REPO[fa:fa-code span-sg<br/>Git Repository]
            ISSUES[fa:fa-bug Issues<br/>Suivi bugs]
            PR[fa:fa-code-branch Pull Requests<br/>Review process]
        end

        subgraph "GitHub Actions Runners"
            RUNNER[fa:fa-server ubuntu-latest<br/>8 vCPU, 14 GB RAM]
            CACHE[fa:fa-hdd Build Cache<br/>Docker layers + pip]
        end

        subgraph "GitHub Pages"
            GHP[fa:fa-globe GitHub Pages<br/>CDN CloudFlare]
            DRAFT[fa:fa-folder /draft/<br/>Preview org-only]
            PROD[fa:fa-folder / racine<br/>Production public]
        end

        subgraph "Artifacts Storage"
            ART[fa:fa-archive Artifacts<br/>Retention 30-90j]
        end
    end

    subgraph "External Services"
        DINUM[fa:fa-landmark DINUM<br/>Référentiel RGAA]
        NPM[fa:fa-cube npm registry<br/>Dependencies JS]
        PYPI[fa:fa-cube PyPI<br/>Dependencies Python]
    end

    DEV -->|git push| REPO
    DEV -->|docker-compose up| DOCKER

    REPO -->|Webhook| RUNNER
    RUNNER -->|Cache Docker| CACHE
    RUNNER -->|Upload| ART
    RUNNER -->|Deploy| GHP

    GHP --> DRAFT
    GHP --> PROD

    RUNNER -->|Download deps| NPM
    RUNNER -->|pip install| PYPI

    DEV -->|Référence| DINUM

    style RUNNER fill:#b5f5ec,stroke:#13c2c2,stroke-width:3px
    style GHP fill:#b7eb8f,stroke:#52c41a,stroke-width:3px
    style REPO fill:#ffc9c9,stroke:#ff4d4f,stroke-width:2px
```

---

## 2. CI/CD Runner Infrastructure

### GitHub Actions Runner Specs

```yaml
Runner: ubuntu-latest (Ubuntu 22.04 LTS)
vCPU: 8 cores
RAM: 14 GB
Disk: 14 GB SSD
Network: 1 Gbps
Runtime: ~15min (draft), ~20min (main)
```

### Software Stack Runner

```mermaid
graph TB
    subgraph "OS Layer"
        UBUNTU[Ubuntu 22.04 LTS<br/>Kernel 5.15+]
    end

    subgraph "Runtime Layer"
        PYTHON[Python 3.11.13<br/>CPython]
        NODE[Node.js 20 LTS<br/>npm 10]
        DOCKER[Docker 24.x<br/>Buildx]
    end

    subgraph "Build Tools"
        PIP[pip 24.3.1<br/>Package installer]
        GIT[Git 2.47<br/>Version control]
        APT[apt-get<br/>System packages]
    end

    subgraph "System Libraries"
        PANGO[libpango-1.0<br/>Text rendering]
        CAIRO[libcairo2<br/>Vector graphics]
        GDK[libgdk-pixbuf<br/>Image loading]
        HARFBUZZ[libharfbuzz<br/>Text shaping]
    end

    subgraph "Python Packages"
        MKDOCS[mkdocs==1.6.1<br/>Site generator]
        DSFR[mkdocs-dsfr==0.17<br/>Theme DSFR]
        WEASY[weasyprint==62.3<br/>PDF generator]
        PYTEST[pytest==8.3.4<br/>Test framework]
    end

    UBUNTU --> PYTHON
    UBUNTU --> NODE
    UBUNTU --> DOCKER

    PYTHON --> PIP
    UBUNTU --> GIT
    UBUNTU --> APT

    APT --> PANGO
    APT --> CAIRO
    APT --> GDK
    APT --> HARFBUZZ

    PIP --> MKDOCS
    PIP --> DSFR
    PIP --> WEASY
    PIP --> PYTEST

    WEASY -.->|requires| PANGO
    WEASY -.->|requires| CAIRO

    style PYTHON fill:#91d5ff,stroke:#1890ff,stroke-width:2px
    style MKDOCS fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
    style WEASY fill:#ffc9c9,stroke:#ff4d4f,stroke-width:2px
```

---

## 3. Build Pipeline Détaillé

### Phases de Build

```mermaid
graph LR
    subgraph "Phase 1: Setup (30s)"
        A[Checkout code]
        B[Setup Python 3.11]
        C[Install deps DSFR]
        D[Install deps dev]
    end

    subgraph "Phase 2: Quality (60s)"
        E[Black formatter]
        F[Ruff linter]
        G[Pytest 33 tests]
        H[Coverage 89%+]
    end

    subgraph "Phase 3: Security (45s)"
        I[Bandit scan]
        J[Safety CVE check]
        K[Upload reports]
    end

    subgraph "Phase 4: Build (90s)"
        L[Calculate scores]
        M[Build HTML DSFR]
        N[Verify DSFR theme]
        O[Generate PDF]
        P[Enrich metadata]
        Q[Validate qpdf]
    end

    subgraph "Phase 5: E2E (300s main)"
        R[Docker Buildx]
        S[Run 9 scenarios]
        T[Upload E2E report]
    end

    subgraph "Phase 6: Deploy (60s)"
        U[Clone gh-pages]
        V[Copy site/]
        W[Git push]
    end

    A --> B --> C --> D
    D --> E --> F --> G --> H
    H --> I --> J --> K
    K --> L --> M --> N --> O --> P --> Q
    Q --> R --> S --> T
    T --> U --> V --> W

    style W fill:#b7eb8f,stroke:#52c41a,stroke-width:3px
```

### Temps d'exécution

| Phase | Draft | Main | Critique |
|-------|-------|------|----------|
| Setup | 30s | 30s | Non |
| Quality | 60s | 60s | Oui (fail-fast) |
| Security | 45s | 45s | Oui (bloquant) |
| Build | 90s | 90s | Oui (strict mode) |
| E2E | - | 300s | Oui (main only) |
| Deploy | 60s | 60s | Non |
| **Total** | **~6min** | **~10min** | - |

---

## 4. Caching Strategy

### Docker Layer Cache

```yaml
Cache key: ${{ runner.os }}-buildx-${{ hashFiles('Dockerfile.mkdocs-test') }}
Storage: /tmp/.buildx-cache
Size: ~500 MB
Hit rate: 95% (runs consécutifs)
Miss penalty: +2min build
```

### Pip Dependencies Cache

```yaml
Cache key: ${{ runner.os }}-pip-${{ hashFiles('requirements-dsfr.txt') }}
Storage: ~/.cache/pip
Size: ~200 MB
Hit rate: 98%
Miss penalty: +30s install
```

### Build Cache Effectiveness

```mermaid
pie title "Cache Hit Rate (30 derniers builds)"
    "Cache Hit (13min)" : 85
    "Cache Miss (15min)" : 15
```

---

## 5. Déploiement GitHub Pages

### Architecture CDN

```mermaid
graph TB
    subgraph "GitHub Pages Infrastructure"
        GHP[GitHub Pages<br/>Static hosting]
        CF[CloudFlare CDN<br/>Global edge network]
    end

    subgraph "Edge Locations"
        EU[Europe<br/>Frankfurt, Paris]
        US[USA<br/>Virginia, California]
        ASIA[Asia<br/>Singapore, Tokyo]
    end

    subgraph "Content"
        HTML[site/*.html<br/>~2 MB]
        CSS[assets/*.css<br/>~500 KB]
        JS[assets/*.js<br/>~300 KB]
        PDF[exports/*.pdf<br/>~8 MB]
    end

    GHP --> CF
    CF --> EU
    CF --> US
    CF --> ASIA

    HTML --> GHP
    CSS --> GHP
    JS --> GHP
    PDF --> GHP

    style CF fill:#ffec3d,stroke:#faad14,stroke-width:2px
    style GHP fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
```

### Stratégie Branching gh-pages

```mermaid
gitGraph
    commit id: "Initial gh-pages"
    branch main-deploy
    commit id: "Deploy draft v0.9"
    checkout main
    commit id: "Deploy prod v1.0"
    checkout draft-deploy
    commit id: "Deploy draft v1.1-rc1"
    checkout main
    merge draft-deploy tag: "v1.1"
    commit id: "Deploy prod v1.1"
```

### URLs et Accès

| URL | Branche source | Déploiement | Accès | Latency |
|-----|----------------|-------------|-------|---------|
| `/` | main | gh-pages racine | Public | <100ms |
| `/draft/` | draft | gh-pages/draft/ | Org-only | <100ms |

---

## 6. Ressources et Quotas

### GitHub Actions Quotas

```yaml
Free tier (public repo):
  - Minutes: Unlimited
  - Concurrent jobs: 20
  - Storage artifacts: 500 MB
  - Retention: 90 jours max

Consommation SPAN SG:
  - Minutes/mois: ~300 min (60 builds × 5 min)
  - Concurrent jobs: 2 (draft + main)
  - Storage: ~50 MB (reports + PDF)
  - Retention: 30-90j selon type
```

### GitHub Pages Quotas

```yaml
Soft limits:
  - Bandwidth: 100 GB/mois
  - Build time: 10 min/build
  - Site size: 1 GB
  - Files: 100k max

Consommation SPAN SG:
  - Bandwidth: <1 GB/mois (usage interne)
  - Build time: 1-2 min (MkDocs)
  - Site size: ~10 MB (HTML + assets)
  - Files: ~200 fichiers
```

---

## 7. Monitoring et Observabilité

### Métriques CI/CD

Métriques trackées automatiquement par GitHub Actions :

```mermaid
graph LR
    A[Build Duration] --> E[Grafana<br/>Dashboard]
    B[Test Success Rate] --> E
    C[Cache Hit Rate] --> E
    D[Deploy Frequency] --> E

    E --> F[Alertes<br/>Slack/Email]

    style E fill:#ffe7ba,stroke:#fa8c16,stroke-width:2px
```

### Health Checks

| Check | Fréquence | Seuil alerte | Action |
|-------|-----------|--------------|--------|
| Build success rate | Par build | <95% | Investigation |
| Build duration | Par build | >20min | Optimisation |
| Test coverage | Par build | <89% | Fail build |
| Deployment success | Par deploy | <100% | Rollback |

---

## 8. Disaster Recovery

### Stratégie de Sauvegarde

```mermaid
graph TB
    subgraph "Sources"
        REPO[GitHub Repo<br/>Git history]
        PAGES[GitHub Pages<br/>Static site]
        ART[Artifacts<br/>30-90j retention]
    end

    subgraph "Backups"
        GIT_MIRROR[Git Mirror<br/>Backup repo]
        PDF_ARCHIVE[PDF Archive<br/>Releases]
        LOCAL[Local clones<br/>Développeurs]
    end

    subgraph "Recovery Points"
        RTO[RTO: 15 min<br/>Rebuild from main]
        RPO[RPO: 1 commit<br/>Git history]
    end

    REPO -.->|Mirror| GIT_MIRROR
    PAGES -.->|Export| PDF_ARCHIVE
    REPO -.->|Clone| LOCAL

    GIT_MIRROR --> RTO
    PDF_ARCHIVE --> RPO

    style RTO fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
    style RPO fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
```

### Procédure Recovery

En cas de perte totale GitHub Pages :

1. **Rebuild from Git** (15 min) :
   ```bash
   git clone https://github.com/Alexmacapple/span-sg.git
   docker compose -f docker-compose-dsfr.yml up -d
   mkdocs build --config-file mkdocs-dsfr.yml
   # Deploy to alternative hosting
   ```

2. **Restore from Releases** (5 min) :
   ```bash
   gh release download latest --pattern "*.pdf"
   # PDF contient tout le contenu SPAN
   ```

3. **Alternative Hosting** :
   - Netlify : `netlify deploy --dir=site --prod`
   - Vercel : `vercel --prod`
   - GitLab Pages : Migrate repo + CI

---

## 9. Sécurité Infrastructure

### Secrets Management

```yaml
GitHub Secrets utilisés:
  GITHUB_TOKEN: Auto-generated (push gh-pages)
  # Pas d'autres secrets requis (sécurité minimale)

Rotation:
  GITHUB_TOKEN: Automatique par GitHub
```

### Surface d'Attaque

Analyse surface d'attaque réduite :

```mermaid
graph TB
    A[Attaquant potentiel]

    subgraph "Vecteurs d'attaque"
        B[Compromission repo]
        C[Injection CI/CD]
        D[Malicious PR]
        E[Dependency hijacking]
    end

    subgraph "Défenses"
        F[Branch protection<br/>main + draft]
        G[Code review<br/>requis]
        H[Dependabot<br/>alerts]
        I[Safety + Bandit<br/>scans]
    end

    A --> B
    A --> C
    A --> D
    A --> E

    B -->|Blocked by| F
    C -->|Blocked by| G
    D -->|Blocked by| G
    E -->|Detected by| H
    E -->|Blocked by| I

    style F fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
    style G fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
    style H fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
    style I fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
```

---

## 10. Performance et Optimisations

### Optimisations Appliquées

| Optimisation | Impact | Métrique |
|--------------|--------|----------|
| Docker layer cache | -40% build time | 5min → 3min |
| Pip dependencies cache | -20% install time | 90s → 72s |
| Strict mode MkDocs | +5% build time | Qualité +++ |
| PDF isolation (--site-dir) | Évite rebuild HTML | -30s |
| Shallow git clone | -10s checkout | depth=1 |

### Performance Metrics

```mermaid
graph LR
    A[Build Time Evolution]
    B[v0.9: 18min]
    C[v1.0: 12min]
    D[v1.1: 6min]

    B -->|Docker cache| C
    C -->|Pip cache| D

    style D fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
```

---

## Références

- [C4 Diagrams (Architecture)](c4-diagrams.md)
- [Diagrammes Mermaid (6 existants)](diagrams.md)
- [ADR-003: Isolation PDF Build](../adr/003-isolation-pdf-build.md)
- [SECURITY.md Politique Sécurité](../../SECURITY.md)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
