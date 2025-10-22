# Architecture C4 - Diagrammes Contexte et Containers

Représentations architecture C4 (Context, Containers, Components, Code) du projet SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-22
Standard: [C4 Model](https://c4model.com/)

---

## Introduction C4

Le modèle C4 décompose l'architecture en 4 niveaux de zoom :

1. **Context** : Vue système dans son écosystème (personnes, systèmes externes)
2. **Containers** : Applications, services, bases de données
3. **Components** : Modules logiques internes
4. **Code** : Classes, fonctions (optionnel)

Ce document couvre les niveaux 1-2.

---

## 1. C4 Level 1 : Diagramme de Contexte

Vue macro du système SPAN SG et ses acteurs.

```mermaid
graph TB
    subgraph "Acteurs"
        CONTRIB[fa:fa-user Contributeur Service<br/>SIRCOM, SNUM, SRH, etc.]
        VALID[fa:fa-user-check Validateur<br/>Bertrand, Alex]
        SPONSOR[fa:fa-user-tie Sponsor<br/>Chef SNUM]
        PUBLIC[fa:fa-users Public<br/>Consultation SPAN]
    end

    subgraph "Système SPAN SG"
        SPAN[fa:fa-file-alt SPAN SG<br/>Documentation Accessibilité<br/>MkDocs + DSFR]
    end

    subgraph "Systèmes Externes"
        GITHUB[fa:fa-github GitHub<br/>Hébergement repo + Pages]
        CI[fa:fa-cog GitHub Actions<br/>CI/CD Pipeline]
        DINUM[fa:fa-landmark DINUM<br/>Référentiel 33 critères]
    end

    CONTRIB -->|Édite modules| SPAN
    VALID -->|Valide PRs| SPAN
    SPONSOR -->|Approuve releases| SPAN
    PUBLIC -->|Consulte| SPAN

    SPAN -->|Versionné sur| GITHUB
    SPAN -->|Validé par| CI
    SPAN -->|Conforme à| DINUM
    GITHUB -->|Déclenche| CI
    CI -->|Déploie sur| GITHUB

    style SPAN fill:#91d5ff,stroke:#1890ff,stroke-width:3px
    style GITHUB fill:#ffc9c9,stroke:#ff4d4f,stroke-width:2px
    style CI fill:#b5f5ec,stroke:#13c2c2,stroke-width:2px
    style DINUM fill:#ffe7ba,stroke:#fa8c16,stroke-width:2px
```

**Acteurs principaux :**
- Contributeurs services (6 modules : SIRCOM, SNUM, SRH, SIEP, SAFI, BGS)
- Validateurs (review PRs, merge)
- Sponsor (validation conceptuelle, releases officielles)
- Public (consultation SPAN publié)

**Systèmes externes :**
- GitHub : Hébergement repo + Pages
- GitHub Actions : CI/CD automatisé
- DINUM : Référentiel 33 critères accessibilité

---

## 2. C4 Level 2 : Diagramme Containers

Détail des composants applicatifs du système SPAN SG.

```mermaid
graph TB
    subgraph "GitHub Repository"
        direction TB
        REPO[fa:fa-code Repository<br/>span-sg<br/>Git + Markdown]
        BRANCH_MAIN[fa:fa-code-branch main<br/>Production]
        BRANCH_DRAFT[fa:fa-code-branch draft<br/>Preview]
    end

    subgraph "CI/CD Pipeline (GitHub Actions)"
        direction TB
        JOB_DRAFT[fa:fa-cog Job: build-deploy-draft<br/>Python 3.11 + MkDocs]
        JOB_MAIN[fa:fa-cog Job: build-deploy-main<br/>Python 3.11 + MkDocs + E2E]
        TESTS[fa:fa-check-circle Tests<br/>Pytest + Coverage 89%+]
        SECURITY[fa:fa-shield-alt Sécurité<br/>Bandit + Safety]
    end

    subgraph "Build Artifacts"
        direction TB
        SITE_HTML[fa:fa-file-code site/<br/>HTML DSFR]
        PDF[fa:fa-file-pdf exports/<br/>span-sg.pdf]
        REPORTS[fa:fa-chart-bar Reports<br/>E2E + Security + Coverage]
    end

    subgraph "Deployment Targets"
        direction TB
        PAGES_DRAFT[fa:fa-globe gh-pages/draft/<br/>Preview privée]
        PAGES_PROD[fa:fa-globe gh-pages/<br/>Production publique]
    end

    subgraph "Build Tools"
        direction TB
        MKDOCS[fa:fa-book MkDocs 1.6<br/>Générateur site statique]
        DSFR[fa:fa-paint-brush mkdocs-dsfr 0.17<br/>Thème DSFR]
        WEASY[fa:fa-file-pdf WeasyPrint<br/>Générateur PDF]
    end

    REPO --> BRANCH_MAIN
    REPO --> BRANCH_DRAFT

    BRANCH_DRAFT --> JOB_DRAFT
    BRANCH_MAIN --> JOB_MAIN

    JOB_DRAFT --> TESTS
    JOB_DRAFT --> SECURITY
    JOB_MAIN --> TESTS
    JOB_MAIN --> SECURITY

    TESTS --> MKDOCS
    SECURITY --> MKDOCS

    MKDOCS --> DSFR
    MKDOCS --> WEASY

    DSFR --> SITE_HTML
    WEASY --> PDF

    JOB_DRAFT --> REPORTS
    JOB_MAIN --> REPORTS

    SITE_HTML --> PAGES_DRAFT
    SITE_HTML --> PAGES_PROD
    PDF --> PAGES_DRAFT
    PDF --> PAGES_PROD

    style REPO fill:#f0f0f0,stroke:#333,stroke-width:2px
    style JOB_DRAFT fill:#b5f5ec,stroke:#13c2c2,stroke-width:2px
    style JOB_MAIN fill:#b5f5ec,stroke:#13c2c2,stroke-width:2px
    style SITE_HTML fill:#91d5ff,stroke:#1890ff,stroke-width:2px
    style PDF fill:#ffc9c9,stroke:#ff4d4f,stroke-width:2px
    style PAGES_PROD fill:#b7eb8f,stroke:#52c41a,stroke-width:3px
```

**Containers identifiés :**

1. **Repository Git** :
   - Markdown sources (docs/modules/*.md)
   - Configurations (mkdocs-dsfr.yml, mkdocs-dsfr-pdf.yml)
   - Scripts Python (calculate_scores.py, enrich_pdf_metadata.py)
   - Hooks MkDocs (dsfr_table_wrapper.py, title_cleaner.py)

2. **CI/CD Pipeline** :
   - Job draft : Build + déploiement preview
   - Job main : Build + E2E + sécurité + déploiement production
   - Tests : Pytest (33 tests unitaires, 9 scénarios E2E)
   - Sécurité : Bandit (code security) + Safety (CVE dependencies)

3. **Build Artifacts** :
   - site/ : HTML DSFR (thème gouvernemental)
   - exports/span-sg.pdf : PDF avec métadonnées enrichies
   - Reports : E2E HTML, Security JSON, Coverage HTML

4. **Deployment Targets** :
   - gh-pages/draft/ : Preview privée (org-only)
   - gh-pages/ racine : Production publique

5. **Build Tools** :
   - MkDocs 1.6 : Générateur site statique
   - mkdocs-dsfr 0.17 : Thème DSFR officiel
   - WeasyPrint : Générateur PDF (CSS Paged Media)

---

## 3. Technologies et Dépendances

### Stack technique

| Layer | Technologie | Version | Rôle |
|-------|-------------|---------|------|
| Source | Markdown + YAML | - | Format documentation |
| Build | MkDocs | 1.6+ | Générateur site statique |
| Theme | mkdocs-dsfr | 0.17.0 | Design System État |
| PDF | WeasyPrint | 62.3 | Générateur PDF |
| Tests | Pytest | 8.3.4 | Tests unitaires + E2E |
| CI/CD | GitHub Actions | - | Pipeline automatisé |
| Hosting | GitHub Pages | - | Hébergement statique |

### Dépendances critiques

```python
# requirements-dsfr.txt
mkdocs==1.6.1
mkdocs-dsfr==0.17.0
mkdocs-git-revision-date-localized-plugin==1.3.0
pymdown-extensions==10.12
mkdocs-pdf-export-plugin==0.5.10
weasyprint==62.3
```

---

## 4. Flux de Données

Parcours typique d'une modification SPAN :

```mermaid
sequenceDiagram
    participant C as Contributeur
    participant G as GitHub
    participant CI as GitHub Actions
    participant P as GitHub Pages

    Note over C,G: 1. Contribution
    C->>G: Push feature/update-sircom
    C->>G: Create PR draft ← feature

    Note over G,CI: 2. CI Validation
    G->>CI: Trigger workflow (draft)
    CI->>CI: Linting (Black, Ruff)
    CI->>CI: Tests (33 unitaires)
    CI->>CI: Security (Bandit, Safety)
    CI->>CI: Build HTML DSFR
    CI->>CI: Generate PDF
    CI->>G: Status: ✅ Success / ❌ Failed

    Note over C,G: 3. Review
    C->>G: Request review (Bertrand/Alex)
    G->>C: Approve + Merge PR

    Note over G,CI: 4. Déploiement
    G->>CI: Trigger workflow (draft merge)
    CI->>CI: Run all checks + E2E (si main)
    CI->>P: Deploy gh-pages/draft/ (ou /)

    Note over C,P: 5. Publication
    P->>C: Preview visible org-only
```

---

## 5. Stratégie de Déploiement

### Environnements

| Environnement | Branche | URL | Accès | Déploiement |
|---------------|---------|-----|-------|-------------|
| Preview | draft | /draft/ | Org-only | Auto (push draft) |
| Production | main | / racine | Public | Auto (push main) |

### Workflow déploiement

```mermaid
graph LR
    A[Commit main/draft] --> B{Tests pass?}
    B -->|❌ Failed| C[STOP - Fix errors]
    B -->|✅ Success| D[Build HTML + PDF]
    D --> E{Branche?}
    E -->|draft| F[Deploy /draft/]
    E -->|main| G[Run E2E tests]
    G --> H{E2E pass?}
    H -->|❌| I[STOP - Check E2E report]
    H -->|✅| J[Deploy / racine]

    style C fill:#ff6b6b
    style I fill:#ff6b6b
    style F fill:#91d5ff
    style J fill:#b7eb8f
```

---

## 6. Sécurité et Qualité

### Gates qualité CI/CD

Chaque build passe par 7 gates obligatoires :

1. **Black formatter** : Formatage code uniforme
2. **Ruff linter** : Détection bugs, style, complexité
3. **Bandit** : Analyse sécurité code (HIGH/CRITICAL)
4. **Safety** : Scan CVE dependencies
5. **Pytest** : 33 tests unitaires (0 failed)
6. **Coverage** : Seuil 89%+ scripts, 100% hooks
7. **E2E** (main only) : 9 scénarios bout-en-bout

### Artefacts sécurité

Conservés en GitHub Actions Artifacts :

- **security-reports** : Bandit JSON + Safety JSON (90 jours)
- **e2e-report** : Rapport HTML scénarios (30 jours)
- **accessibility-report** : Tests RGAA Selenium (30 jours)
- **exports** : PDF SPAN (persistant)

---

## Références

- [C4 Model Official](https://c4model.com/)
- [Diagrammes Mermaid (6 existants)](diagrams.md)
- [ADR Architecture Decision Records](../adr/README.md)
- [API Reference Scripts](../dev/api-reference.md)
