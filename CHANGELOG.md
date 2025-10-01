# Changelog


## v0.2.0 – 2025-10-01

**Semaine 2 - Automatisation : Tests, Documentation et Qualité**

### Tests et Qualité (S2-05, S2-06)
- ✅ Tests unitaires pytest (18 tests) pour `calculate_scores.py` et `enrich_pdf_metadata.py`
- ✅ Linting Python (Black + Ruff) intégré à CI avec pre-commit hooks
- ✅ 9 scénarios E2E automatisés : workflow complet, multi-modules, rollback, erreur périmètre, PDF, performance, frontmatter, preview HTTP
- ✅ Runner `tests/e2e/run_all.sh` pour exécution complète
- ✅ Configuration CI locale avec `act` (nektos/act) pour validation avant push
- ✅ Corrections compatibilité Linux/macOS : sed, stat, awk→sed+grep avec numéros de ligne absolus (v4)
- ✅ Dockerfile.mkdocs-test avec build-essentials pour libsass (Alpine Linux)
- ✅ Timeout gracieux Docker (skip si build > 60s)

### Documentation et Contribution (S2-04, S2-07)
- ✅ Guide contributeur `CONTRIBUTING.md` (Option A GitHub web + Option B Git local)
- ✅ Template Pull Request `.github/PULL_REQUEST_TEMPLATE.md` (type, module, checklist)
- ✅ 5 modules enrichis avec contexte métier réel : SNUM, SRH, SIEP, SAFI, BGS
- ✅ Sections 1-5 remplies (périmètre, état, organisation, plan 2025, indicateurs)
- ✅ Tableaux périmètre et plan d'action avec estimations
- ✅ URLs déclaration accessibilité définies
- ✅ Maintien 0/31 points DINUM (validation ultérieure par services)
- ✅ Documentation modules : 19/20 → 20/20 (objectif atteint)

### Infrastructure et Déploiement (S2-01, S2-02, S2-03)
- ✅ Preview privée GitHub Pages (draft → /draft/, production → racine)
- ✅ Génération PDF systématique avec métadonnées enrichies (auteur, sujet, mots-clés)
- ✅ Script `enrich_pdf_metadata.py` avec tests unitaires
- ✅ Workflow CI optimisé : badges status, artefacts (site/ + exports/), déploiements conditionnels
- ✅ Paramétrage Pages org-only (accès restreint organisation)

### Corrections (Hotfixes)
- 🔧 4 itérations corrections tests E2E (compatibilité GNU sed/BSD sed)
  - v1 : sed -i '' → sed -i.bak (portable macOS/Linux)
  - v2 : stat -f%z → stat -c%s avec fallback
  - v3 : sed '0,/pattern/' → awk avec flag done (échec double-cochage)
  - v4 : awk → sed+grep avec numéros de ligne absolus (solution finale portable)
- 🔧 Correction scores attendus (6/31 → 7/31 SIRCOM, 12/186 → 13/186 TOTAL)
- 🔧 Correction chemins PDF (pdf/document.pdf → exports/span-sg.pdf)
- 🔧 URLs GitHub corrigées (span-sg/span-sg → Alexmacapple/span-sg-repo)

### Statistiques
- 📊 59 commits depuis v0.1.0
- ✅ CI 100% PASS (tests unitaires + E2E + scoring + build + PDF + deploy)
- 📈 Score actuel : SIRCOM 7/31 (22.6%), TOTAL 7/186 (3.8%)
- 🧪 Couverture tests : 18 tests unitaires + 9 scénarios E2E
- 📝 Documentation : CONTRIBUTING.md, tests/README.md, 6 modules structurés

### Roadmaps BMAD complétées
- S2-01 : CI/CD GitHub Actions optimisée
- S2-02 : Génération PDF avec métadonnées
- S2-03 : Preview privée GitHub Pages
- S2-04 : Documentation contributeur
- S2-05 : Tests unitaires et linting Python
- S2-06 : Tests E2E automatisés + CI locale act
- S2-07 : Enrichissement modules avec contexte métier

---

## v0.1.0 – 2025-09-30
- Initialisation du dépôt SPAN SG (MVP)
- MkDocs + CI GitHub Actions + PDF (fallback)
- Template modules avec 5 sections obligatoires + 31 points DINUM
- Preview privée via GitHub Pages (organisation uniquement)
