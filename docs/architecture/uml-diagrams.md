# Architecture UML - Diagrammes Classes et États

Diagrammes UML (Unified Modeling Language) pour les composants Python et workflows du projet SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-22
Standard: [UML 2.5](https://www.omg.org/spec/UML/)

---

## Introduction UML

Ce document présente deux types de diagrammes UML :

1. **Diagrammes de Classes** : Structure statique des scripts et hooks Python
2. **Diagrammes d'États** : Transitions dynamiques des workflows (PR, CI/CD, modules)

---

## 1. Diagrammes de Classes

### 1.1 Module calculate_scores.py

Script principal de calcul des scores SPAN (33 critères DINUM).

```mermaid
classDiagram
    class CalculateScores {
        +String CHECK_TAG = "CHECKLIST"
        +Regex FENCE_RE
        +Regex BOX_RE
        +load_text(Path p) String
        +score_module(Path p) Tuple[int, int]
        +get_validation_status(Path p) String
        +status_to_badge(String status) String
        +validation_to_badge(String validation_state) String
        +generate_summary() int
    }

    class PathModule {
        +Path modules_dir
        +glob(String pattern) List[Path]
        +read_text(String encoding) String
        +write_text(String content, String encoding)
    }

    class RegexModule {
        +compile(String pattern, int flags) Regex
        +sub(String pattern, String repl, String text, int flags) String
        +search(String pattern, String text, int flags) Match
    }

    CalculateScores ..> PathModule : uses
    CalculateScores ..> RegexModule : uses

    note for CalculateScores "Responsabilité principale :
    - Scanner docs/modules/*.md
    - Compter cases cochées [x] avec tag CHECKLIST
    - Générer docs/synthese.md avec badges DSFR
    - Valider périmètre (total = 0 ou 33)

    Exit codes :
    - 0 : Succès
    - 2 : Erreur périmètre (total ≠ 0 ou 33)"
```

**Fonctions principales** :

| Fonction | Signature | Description |
|----------|-----------|-------------|
| `load_text()` | `Path → String` | Charge fichier et supprime code fences (```) |
| `score_module()` | `Path → (int, int)` | Compte checked/total avec tag CHECKLIST |
| `get_validation_status()` | `Path → String` | Extrait validation_status du front-matter YAML |
| `status_to_badge()` | `String → String` | Convertit statut en badge DSFR HTML |
| `validation_to_badge()` | `String → String` | Convertit état validation en badge DSFR |
| `generate_summary()` | `() → int` | Génère synthese.md avec tableau DSFR |

---

### 1.2 Hook dsfr_table_wrapper.py

Hook MkDocs pour wrapper les tableaux avec `<div class="fr-table">`.

```mermaid
classDiagram
    class DsfrTableWrapper {
        +on_page_content(String html, Page page, Config config, Files files) String
        -wrap_table(Match match) String
    }

    class MkDocsHook {
        <<interface>>
        +on_page_content(String html, Page page, Config config, Files files) String
    }

    class RegexModule {
        +sub(String pattern, Function repl, String text, int flags) String
    }

    DsfrTableWrapper ..|> MkDocsHook : implements
    DsfrTableWrapper ..> RegexModule : uses

    note for DsfrTableWrapper "Responsabilité :
    - Post-traiter HTML après Markdown → HTML
    - Détecter tables non wrappées
    - Injecter div.fr-table pour RGAA/DSFR

    Pattern regex :
    (?<!<div class=\"fr-table\">)\s*(<table[^>]*>.*?</table>)

    Évite re-wrapping avec lookahead négatif"
```

**Contexte technique** :

Le thème `mkdocs-dsfr` supprime les divs HTML lors du preprocessing Markdown. Ce hook réinjecte le wrapper DSFR après conversion HTML pour garantir l'accessibilité RGAA et le responsive design.

---

### 1.3 Hook title_cleaner.py

Hook MkDocs pour nettoyer les titres HTML redondants.

```mermaid
classDiagram
    class TitleCleaner {
        +on_post_page(String output, Page page, Config config) String
    }

    class MkDocsHook {
        <<interface>>
        +on_post_page(String output, Page page, Config config) String
    }

    class RegexModule {
        +sub(String pattern, String replacement, String text, int flags) String
    }

    TitleCleaner ..|> MkDocsHook : implements
    TitleCleaner ..> RegexModule : uses

    note for TitleCleaner "Responsabilité :
    - Post-traiter HTML après génération complète
    - Nettoyer titres avec tirets orphelins
    - Améliorer SEO et accessibilité

    Pattern regex :
    <title>\s*(.*?)\s*-\s*\s*</title>

    Exemple :
    Input  : <title>SPAN (SG) - </title>
    Output : <title>SPAN (SG)</title>"
```

**Cas d'usage** :

Lorsque `site_name` est vide dans `mkdocs-dsfr.yml`, MkDocs génère des titres avec tirets superflus. Ce hook nettoie ces artefacts pour un meilleur référencement et conformité accessibilité.

---

### 1.4 Script enrich_pdf_metadata.py

Script d'enrichissement des métadonnées PDF (XMP, Dublin Core).

```mermaid
classDiagram
    class EnrichPdfMetadata {
        +enrich_pdf_metadata(Path input_path, Path output_path) void
        +main() void
    }

    class PikePdf {
        +open(Path path, bool allow_overwriting_input) Pdf
        +Pdf.open_metadata(bool set_pikepdf_as_editor) Metadata
        +Metadata.__setitem__(String key, String value)
        +Pdf.Root.Lang String
        +Pdf.save(Path path)
    }

    class DatetimeModule {
        +now(timezone tz) datetime
        +datetime.isoformat() String
    }

    EnrichPdfMetadata ..> PikePdf : uses
    EnrichPdfMetadata ..> DatetimeModule : uses

    note for EnrichPdfMetadata "Responsabilité :
    - Ouvrir PDF généré par MkDocs
    - Injecter metadata XMP/Dublin Core
    - Définir langue PDF (Root.Lang = fr-FR)
    - Valider conformité RGAA 13.3

    Metadata ajoutées :
    - dc:title, dc:language, dc:creator
    - dc:subject, dc:description
    - pdf:Keywords, pdf:Producer
    - xmp:CreatorTool, xmp:CreateDate

    Exit codes :
    - 0 : Succès
    - 1 : Erreur (fichier introuvable, pikepdf)"
```

**Métadonnées Dublin Core injectées** :

| Clé | Valeur | Conformité |
|-----|--------|------------|
| `dc:title` | SPAN SG | RGAA 13.3 |
| `dc:language` | fr-FR | RGAA 13.3 (test_pdf_metadata_language) |
| `dc:creator` | Secrétariat Général | Metadata standard |
| `dc:subject` | Schéma Pluriannuel Accessibilité | SEO PDF |
| `pdf:Keywords` | SPAN, accessibilité, RGAA, DINUM | Recherche PDF |

---

## 2. Diagrammes d'États

### 2.1 États PR (Pull Request Workflow)

Cycle de vie d'une contribution depuis création jusqu'au déploiement.

```mermaid
stateDiagram-v2
    [*] --> BranchCreated: Contributeur crée branche feature
    BranchCreated --> DraftPR: Créer PR draft ← feature
    DraftPR --> InReview: Request review (@bertrand @alex)

    InReview --> ChangesRequested: Commentaires validateur
    InReview --> Approved: Validation OK

    ChangesRequested --> Fixing: Contributeur corrige
    Fixing --> DraftPR: Push corrections

    Approved --> Merging: Validateur merge PR
    Merging --> CIRunning: Trigger CI/CD draft

    CIRunning --> CIFailed: Tests échouent
    CIRunning --> CISuccess: Tests passent

    CIFailed --> Fixing: Investigation erreurs
    CISuccess --> DeployedDraft: Deploy /draft/ (org-only)

    DeployedDraft --> WaitingRelease: Accumulation contributions
    WaitingRelease --> ProdPR: Validateur crée PR draft → main

    ProdPR --> ChefApproval: Chef SNUM review
    ChefApproval --> ProdMerge: Approbation release
    ProdMerge --> E2ETests: Run 9 scenarios E2E

    E2ETests --> E2EFailed: E2E échec
    E2ETests --> E2ESuccess: E2E succès

    E2EFailed --> Rollback: Investigation + hotfix
    E2ESuccess --> DeployedProd: Deploy / racine (public)

    DeployedProd --> [*]: Contribution visible production
    Rollback --> Fixing: Créer branche hotfix

    note right of InReview
        Délai typique : 2-5 jours
        Notifications : Email GitHub
    end note

    note right of DeployedDraft
        Preview privée (org-only)
        URL : /draft/
        Persistance : Jusqu'à release
    end note

    note right of E2ETests
        9 scénarios Pytest-Selenium
        Timeout : 240s par test
        Bloquant : Échec → STOP
    end note
```

**États clés** :

1. **DraftPR** : PR créée vers branche `draft` (base review)
2. **InReview** : Validateur notifié, review en cours (2-5j)
3. **ChangesRequested** : Corrections demandées (loop possible)
4. **CIRunning** : Pipeline CI/CD (linting, tests, security, build)
5. **DeployedDraft** : Preview déployée `/draft/` (org-only)
6. **WaitingRelease** : Contributions accumulées (30-60j)
7. **E2ETests** : Tests bout-en-bout (main only, bloquant)
8. **DeployedProd** : Production publique `/` (final)

---

### 2.2 États CI/CD Pipeline

États du pipeline GitHub Actions (draft et main).

```mermaid
stateDiagram-v2
    [*] --> Triggered: git push (draft/main)
    Triggered --> Setup: Checkout + Python 3.11 + deps
    Setup --> Linting: Black + Ruff

    Linting --> LintFailed: Code non conforme
    Linting --> LintSuccess: Code OK

    LintFailed --> [*]: STOP (exit 1)
    LintSuccess --> Testing: Pytest 33 tests

    Testing --> TestFailed: Tests échouent
    Testing --> TestSuccess: Tests passent (coverage 89%+)

    TestFailed --> [*]: STOP (exit 1)
    TestSuccess --> Security: Bandit + Safety

    Security --> SecurityFailed: Vulnérabilités HIGH/CRITICAL
    Security --> SecuritySuccess: Aucune vulnérabilité

    SecurityFailed --> [*]: STOP (exit 1, continueOnError annotations)
    SecuritySuccess --> BuildHTML: mkdocs build --strict

    BuildHTML --> BuildFailed: Erreurs MkDocs (liens cassés)
    BuildHTML --> BuildSuccess: Site généré site/

    BuildFailed --> [*]: STOP (exit 1)
    BuildSuccess --> BuildPDF: WeasyPrint + enrich metadata

    BuildPDF --> PDFFailed: Erreur génération PDF
    BuildPDF --> PDFSuccess: PDF enrichi exports/span-sg.pdf

    PDFFailed --> [*]: STOP (exit 1)
    PDFSuccess --> BranchCheck: Vérifier branche

    BranchCheck --> E2ETestsMain: main → Tests E2E
    BranchCheck --> SkipE2E: draft → Skip E2E

    E2ETestsMain --> E2EFailed: Scénarios échec
    E2ETestsMain --> E2ESuccess: 9/9 scenarios pass

    E2EFailed --> [*]: STOP (exit 1, main only)
    E2ESuccess --> Deploy: Deploy GitHub Pages
    SkipE2E --> Deploy

    Deploy --> DeployDraft: draft → /draft/
    Deploy --> DeployProd: main → / racine

    DeployDraft --> Artifacts: Upload exports + reports
    DeployProd --> Artifacts

    Artifacts --> [*]: Pipeline SUCCESS

    note right of Linting
        Durée : ~10s
        Bloquant : Oui
        Tools : Black 24.x + Ruff 0.x
    end note

    note right of Security
        Durée : ~15s
        Bloquant : Oui (HIGH/CRITICAL)
        Tools : Bandit + Safety
    end note

    note right of E2ETestsMain
        Durée : ~300s (5 min)
        Bloquant : Oui (main only)
        Parallélisme : Non (séquentiel)
    end note
```

**Phases critiques** :

| Phase | Durée | Fail-fast | Sortie |
|-------|-------|-----------|--------|
| Linting | 10s | Oui | exit 1 (non conforme) |
| Testing | 60s | Oui | exit 1 (tests KO, coverage <89%) |
| Security | 15s | Oui | exit 1 (vuln HIGH/CRITICAL) |
| Build HTML | 90s | Oui | exit 1 (strict mode, liens cassés) |
| Build PDF | 30s | Oui | exit 1 (WeasyPrint erreur) |
| E2E (main) | 300s | Oui | exit 1 (scénarios échec) |
| Deploy | 60s | Non | Rollback manuel si échec |

---

### 2.3 États Validation Module

États de validation d'un module SPAN (front-matter `validation_status`).

```mermaid
stateDiagram-v2
    [*] --> Draft: Module créé depuis _template.md
    Draft --> InProgress: Contributeur complète sections 1-5
    InProgress --> InProgress: Cocher critères DINUM progressivement

    InProgress --> ReadyValidation: 31/31 critères cochés
    ReadyValidation --> Validated: Validateur approuve contenu

    Validated --> Published: Merge main → production
    Published --> [*]: Module visible public

    InProgress --> Draft: Reset module (décocher critères)
    Validated --> InProgress: Modifications post-validation

    note right of Draft
        Front-matter :
        validation_status: draft

        Score attendu : 0/33 ou X/33
        Badge : Brouillon (warning)
    end note

    note right of InProgress
        Front-matter :
        validation_status: in_progress

        Score attendu : 1-32/33
        Badge : En cours (info)
    end note

    note right of Validated
        Front-matter :
        validation_status: validated

        Score attendu : 33/33
        Badge : Validé (success)
    end note
```

**Règles de transition** :

1. **Draft → InProgress** : Première coche `[x]` d'un critère DINUM
2. **InProgress → ReadyValidation** : 33/33 critères cochés (automatique)
3. **ReadyValidation → Validated** : Validation manuelle validateur (review contenu)
4. **Validated → Published** : Merge vers `main` (release production)
5. **Validated → InProgress** : Régression (décochage critère, corrections)

---

## 3. Diagramme Séquence : Génération PDF

Interaction entre composants pour générer le PDF SPAN.

```mermaid
sequenceDiagram
    participant CI as GitHub Actions
    participant MK as MkDocs
    participant PDF as mkdocs-with-pdf
    participant WP as WeasyPrint
    participant EN as enrich_pdf_metadata.py
    participant QP as qpdf

    Note over CI,QP: Étape 1 : Build HTML DSFR (mode normal)
    CI->>MK: mkdocs build --config-file mkdocs-dsfr.yml
    MK->>MK: Load hooks (dsfr_table_wrapper, title_cleaner)
    MK->>MK: Render Markdown → HTML
    MK->>CI: site/ HTML DSFR généré

    Note over CI,QP: Étape 2 : Génération PDF (config isolée)
    CI->>MK: ENABLE_PDF_EXPORT=1 mkdocs build --config-file mkdocs-dsfr-pdf.yml
    MK->>PDF: Plugin with-pdf activé
    PDF->>WP: Convertir HTML → PDF (CSS Paged Media)
    WP->>WP: Render Cairo/Pango (libpango, libcairo)
    WP->>PDF: PDF brut généré
    PDF->>MK: exports/span-sg.pdf créé
    MK->>CI: Build PDF terminé

    Note over CI,QP: Étape 3 : Enrichissement metadata
    CI->>EN: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
    EN->>EN: pikepdf.open(pdf)
    EN->>EN: Inject Dublin Core (dc:title, dc:language, dc:creator)
    EN->>EN: Inject XMP (xmp:CreatorTool, xmp:CreateDate)
    EN->>EN: Set Root.Lang = fr-FR (RGAA 13.3)
    EN->>EN: pdf.save()
    EN->>CI: Metadata enrichies SUCCESS

    Note over CI,QP: Étape 4 : Validation structure
    CI->>QP: qpdf --check exports/span-sg.pdf
    QP->>QP: Validate PDF/A compliance
    QP->>QP: Check XRef table, metadata
    QP->>CI: PDF valid (exit 0) ou warnings (exit 3)

    Note over CI,QP: Étape 5 : Upload artifacts
    CI->>CI: Upload artifact 'exports' (span-sg.pdf)
    CI->>CI: Retention 90 jours
```

**Étapes critiques** :

1. **Build HTML DSFR** : MkDocs avec thème DSFR (strict mode, hooks actifs)
2. **Génération PDF isolée** : Config séparée `mkdocs-dsfr-pdf.yml` (strict: false, theme readthedocs requis)
3. **Enrichissement metadata** : Injection XMP/Dublin Core avec `pikepdf` (conformité RGAA 13.3)
4. **Validation qpdf** : Vérification structure PDF (exit 3 = warnings non bloquants)
5. **Upload artifacts** : Persistance GitHub Actions (30-90j retention)

---

## 4. Diagramme Activité : Workflow Contributeur

Activités typiques d'un contributeur depuis identification du module jusqu'au déploiement.

```mermaid
flowchart TD
    Start([Contributeur identifie module]) --> Identify{Module existe?}

    Identify -->|Non| CreateModule[Copier _template.md → service.md]
    Identify -->|Oui| CheckStatus[Lire front-matter validation_status]
    CreateModule --> FillFrontmatter[Renseigner front-matter YAML]

    FillFrontmatter --> EditContent[Compléter 5 sections obligatoires]
    CheckStatus --> EditContent

    EditContent --> CheckBoxes[Cocher critères DINUM applicables]
    CheckBoxes --> AddActions[Ajouter actions plan 2025]
    AddActions --> FillDeclaration[Renseigner URL déclaration accessibilité]

    FillDeclaration --> LocalTest{Test local?}
    LocalTest -->|Oui| RunDocker[docker compose -f docker-compose-dsfr.yml up]
    LocalTest -->|Non| CreateBranch[git checkout -b feature/update-service]

    RunDocker --> VerifyLocal[Vérifier http://localhost:8000/span-sg/]
    VerifyLocal --> CreateBranch

    CreateBranch --> CommitChanges[git add + commit -m 'feat service...']
    CommitChanges --> PushBranch[git push -u origin feature/update-service]

    PushBranch --> CreatePR[Créer PR feature → draft sur GitHub]
    CreatePR --> WaitReview[Attendre review validateur 2-5j]

    WaitReview --> ReviewResult{Review résultat?}
    ReviewResult -->|Changes requested| FixComments[Corriger commentaires]
    FixComments --> CommitFixes[git add + commit -m 'fix...']
    CommitFixes --> PushFixes[git push]
    PushFixes --> WaitReview

    ReviewResult -->|Approved| ValidatorMerge[Validateur merge PR]
    ValidatorMerge --> CITrigger[CI/CD déclenché automatiquement]

    CITrigger --> CIResult{CI succès?}
    CIResult -->|Failed| CheckLogs[Consulter GitHub Actions logs]
    CheckLogs --> FixErrors[Corriger erreurs CI]
    FixErrors --> CommitFixes

    CIResult -->|Success| DeployDraft[Déploiement /draft/ automatique]
    DeployDraft --> End([Contribution visible org-only])

    style Start fill:#91d5ff
    style End fill:#b7eb8f
    style CIResult fill:#ffe7ba
    style ReviewResult fill:#ffe7ba
```

**Durée totale estimée** : 30-60 jours (15 min édition + 2-5j review + 30-60j release production)

---

## 5. Diagramme Composants : Architecture Scripts

Organisation des scripts Python et leurs dépendances.

```mermaid
graph TB
    subgraph "Scripts Production"
        CALC[calculate_scores.py<br/>Calcul scores SPAN]
        ENRICH[enrich_pdf_metadata.py<br/>Metadata PDF]
    end

    subgraph "Hooks MkDocs"
        WRAP[dsfr_table_wrapper.py<br/>Wrapper tables DSFR]
        CLEAN[title_cleaner.py<br/>Nettoyage titres]
        COPY[pdf_copy.py<br/>Copie PDF vers site/]
    end

    subgraph "Tests"
        UNIT[tests/test_scores.py<br/>33 tests unitaires]
        E2E[tests/e2e/<br/>9 scenarios Selenium]
    end

    subgraph "Bibliothèques Python"
        PATHLIB[pathlib<br/>Gestion fichiers]
        RE[re<br/>Regex]
        PIKEPDF[pikepdf<br/>Manipulation PDF]
        PYTEST[pytest<br/>Framework tests]
        SELENIUM[selenium<br/>Tests E2E]
    end

    subgraph "Système"
        FS[Filesystem<br/>docs/ exports/]
        GIT[Git<br/>Version control]
    end

    CALC --> PATHLIB
    CALC --> RE
    CALC --> FS

    ENRICH --> PIKEPDF
    ENRICH --> PATHLIB
    ENRICH --> FS

    WRAP --> RE
    CLEAN --> RE

    UNIT --> CALC
    UNIT --> PYTEST
    UNIT --> FS

    E2E --> SELENIUM
    E2E --> PYTEST
    E2E --> GIT

    CALC -.->|Génère| FS
    ENRICH -.->|Lit/Écrit| FS

    style CALC fill:#91d5ff,stroke:#1890ff,stroke-width:2px
    style ENRICH fill:#91d5ff,stroke:#1890ff,stroke-width:2px
    style WRAP fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
    style CLEAN fill:#b7eb8f,stroke:#52c41a,stroke-width:2px
```

**Dépendances critiques** :

| Script | Dépendances | Utilisation |
|--------|-------------|-------------|
| `calculate_scores.py` | pathlib, re | Scan modules, regex critères, I/O fichiers |
| `enrich_pdf_metadata.py` | pikepdf, pathlib | Manipulation PDF, metadata XMP |
| `dsfr_table_wrapper.py` | re | Regex wrapper tables HTML |
| `title_cleaner.py` | re | Regex nettoyage titres |
| `tests/test_scores.py` | pytest, pathlib | Tests unitaires, fixtures |
| `tests/e2e/` | pytest, selenium, git | Tests E2E, navigation, état Git |

---

## Références

- [UML 2.5 Specification](https://www.omg.org/spec/UML/)
- [Mermaid Class Diagrams](https://mermaid.js.org/syntax/classDiagram.html)
- [Mermaid State Diagrams](https://mermaid.js.org/syntax/stateDiagram.html)
- [C4 Diagrams (Architecture)](c4-diagrams.md)
- [Infrastructure Runtime](infrastructure.md)
- [API Reference Scripts](../dev/api-reference.md)
