# Checklist GO – SPAN SG v1.0

**Dernière mise à jour** : 07/10/2025
**État** : En cours de validation intermédiaire (branche draft)

## 1. Infrastructure technique
- [x] CI/CD GitHub Actions configurée et fonctionnelle
- [x] Tests unitaires (18 tests pytest) + E2E (9 scénarios) → 100% PASS
- [x] Génération PDF automatique avec métadonnées enrichies
- [x] Pipeline de scoring (`calculate_scores.py`) validé
- [x] Dockerfile + docker-compose.yml opérationnels
- [x] Preview privée déployée (https://alexmacapple.github.io/span-sg-repo/draft/)
- [ ] Production déployée (en attente merge draft → main)

## 2. Modules services (6/6 créés, 2/6 validés)
- [x] SIRCOM : 24/31 (77.4%) - Validé
- [x] SNUM : 21/31 (67.7%) - Validé
- [ ] SRH : 0/31 - Structure créée, en cours de complétion
- [ ] SIEP : 0/31 - Structure créée, en cours de complétion
- [ ] SAFI : 0/31 - Structure créée, en cours de complétion
- [ ] BGS : 0/31 - Structure créée, en cours de complétion

**Score global** : 45/186 (24.2%)

## 3. Documentation
- [x] README.md à jour avec état actuel (07/10/2025)
- [x] CONTRIBUTING.md (Option A web + Option B Git local)
- [x] CHANGELOG.md maintenu (v0.1.0, v0.2.0, Unreleased)
- [x] Template PR (`.github/PULL_REQUEST_TEMPLATE.md`)
- [x] Guide développement local (`docs/dev-local.md`)
- [x] Agents.md (Cursor/Codex) + Claude.md (Claude Code)

## 4. Configuration GitHub Pages
- [ ] Organisation → Settings → Pages → Restreindre accès **membres organisation**
- [x] Dépôt → Settings → Pages → Branche `gh-pages` déployée
- [x] Preview draft accessible (/draft/)
- [ ] Production racine accessible (après merge vers main)
- [ ] Test d'accès externe validé (non-membre bloqué)

## 5. URLs et conformité légale
- [x] `mkdocs.yml` → `site_url: https://alexmacapple.github.io/span-sg-repo/`
- [x] `mkdocs.yml` → `repo_url: https://github.com/Alexmacapple/span-sg-repo`
- [ ] URLs déclarations d'accessibilité (TODO modules en cours)
- [ ] Sections "Charge disproportionnée" renseignées (si applicable)

**Note** : URLs actuelles basées sur compte utilisateur. Migration vers organisation GitHub prévue lors de mise en production.

## 6. Validation intermédiaire (roadmap S4)
- [ ] **S4-01** : Review Bertrand/Alexandra → EN COURS
- [ ] **S4-02** : Présentation Stéphane (validation conceptuelle)
- [ ] **S4-03** : Tag v1.0.0 + CHANGELOG finalisé
- [ ] **S4-04** : Merge draft → main + déploiement production
- [ ] **Validation finale** : Chef SNUM (GO/NO-GO production)

## 7. Gouvernance et accès
- [x] Owner défini : Alexandra (@alexandra)
- [x] Validateurs identifiés : Bertrand (@bertrand), Alex (@alex)
- [x] Sponsor : Stéphane (Chef mission numérique SNUM-SG)
- [ ] Restriction Pages organisation (accès membres uniquement)
- [ ] Procédure offboarding définie (désactivation accès sortants)
