# Stats v1.0 SPAN SG

Support mémo-chiffres pour présentation Stéphane (S4-02)

Date : 07/10/2025

---

## Framework technique

- 31 points DINUM × 6 modules = **186 points total**
- Architecture modulaire production-ready
- Scoring automatisé (calculate_scores.py → docs/synthese.md)

---

## Modules validés (2/6)

| Module | Score | Taux | Statut |
|--------|-------|------|--------|
| SIRCOM | 24/31 | 77.4% | Validé |
| SNUM Portailpro.gouv | 21/31 | 67.7% | Validé |
| **Total validés** | **45/62** | **72.6%** | Validé |

Moyenne modules opérationnels : **72.6%** (démonstration maturité framework)

---

## Modules en cours (4/6)

| Module | Score | Structure | Statut |
|--------|-------|-----------|--------|
| SRH | 0/31 | Framework présent | En cours |
| SIEP | 0/31 | Framework présent | En cours |
| SAFI | 0/31 | Framework présent | En cours |
| BGS | 0/31 | Framework présent | En cours |
| **Total en cours** | **0/124** | **0%** | En cours |

Structure 5 sections + 31 points présente, prête pour onboarding Phase 2.

---

## Taux global

**45/186 (24.2%)**

Reflète stratégie hybrid pragmatique : 2 modules professionnels validés + 4 modules framework.

---

## Qualité technique

### CI/CD

- **Statut** : 100% PASS
- **Workflow** : Build SPAN (tests + scoring + PDF + deploy)
- **Dernière exécution** : 02 Oct 2025, run #18198519191
- **Durée moyenne** : 2-3 minutes

### Tests

- **Tests unitaires** : 18 (pytest)
  - calculate_scores.py (9 tests)
  - enrich_pdf_metadata.py (9 tests)
- **Tests E2E** : 9 scénarios
  - Workflow complet
  - Multi-modules
  - Rollback
  - Erreur périmètre
  - PDF génération
  - Performance
  - Frontmatter
  - Preview HTTP
  - Docker build
- **Couverture** : 100% fonctionnalités critiques

### Documentation

- **CONTRIBUTING.md** : Option A (GitHub web) + Option B (Git local)
- **Template PR** : `.github/PULL_REQUEST_TEMPLATE.md`
- **6 modules structurés** : docs/modules/*.md
- **Guide dev local** : docs/dev-local.md
- **Agents.md + Claude.md** : Instructions IA standardisées

---

## Déploiement

### Preview privée

- **URL draft** : https://alexmacapple.github.io/span-sg-repo/draft/
- **Accès** : Restreint membres organisation (org-only)
- **Mise à jour** : Automatique à chaque push sur draft

### Production (standby)

- **URL main** : https://alexmacapple.github.io/span-sg-repo/
- **Statut** : En attente validation Stéphane (S4-02) + tag v1.0.0 (S4-03)
- **Déploiement** : Automatique après merge draft → main (S4-04)

### PDF

- **Génération** : Automatique via CI (mkdocs-with-pdf + enrich_pdf_metadata.py)
- **Artefact** : Téléchargeable depuis GitHub Actions (90 jours)
- **Métadonnées enrichies** :
  - Title : "SPAN SG"
  - Author : "Secrétariat Général"
  - Subject : "Schéma pluriannuel d'accessibilité numérique"
  - Keywords : "SPAN, accessibilité, SG, numérique, RGAA, DINUM"
  - Language : "fr-FR"

---

## Gouvernance

- **Owner** : Alexandra (@alexandra)
- **Validateurs** : Bertrand (@bertrand), Alex (@alex)
- **Sponsor** : Stéphane (Chef mission numérique SNUM-SG)
- **Validation finale** : Chef SNUM (GO/NO-GO production)

---

## Timeline roadmap

- **S4-00** : Guide mapping - Complété
- **S4-01** : Review interne Bertrand/Alexandra - Complété
- **S4-02** : Présentation Stéphane - En cours (validation concept)
- **S4-03** : Tag v1.0.0 - Bloqué par S4-02
- **S4-04** : Publication production - Bloqué par S4-03

---

## Messages clés pour Stéphane

1. **Framework production-ready** : Infrastructure technique complète, testée, documentée
2. **2 modules opérationnels** : SIRCOM 77.4%, SNUM 67.7% = démonstration maturité
3. **Stratégie hybrid pragmatique** : Qualité > quantité, périmètre réaliste (2 contributeurs)
4. **Transparence totale** : Disclaimers 5 emplacements, colonne État, scoring automatisé
5. **Scalabilité assurée** : 4 modules framework prêts pour onboarding Phase 2
6. **CI/CD 100% PASS** : Automatisation complète, tests exhaustifs, déploiement sécurisé
