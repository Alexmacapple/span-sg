# Index Roadmaps SPAN SG

**Date mise à jour** : 2025-10-07
**Total roadmaps** : 37

---

## Vue d'Ensemble

### Statistiques
- **Archivées** : 32 (86.5%) - Sprints 0-6 complétés
- **Actives** : 5 (13.5%) - Modules optionnels
- **Nouvelle** : 1 - POC-FINALISATION

### Statut Projet
- **Score qualité** : 97/100
- **Phase** : POC Production-Ready
- **Prochaine étape** : Release v1.0.0 officielle

---

## Roadmaps Actives

**Localisation** : `roadmap/` (racine)

### POC Finalisation (P0 - Critique)
📋 **POC-FINALISATION.md** : Release v1.0.0 officielle
- Tag v1.0.0
- GitHub Release avec PDF
- CHANGELOG finalisé
- **Estimation** : 1-2h
- **Priorité** : P0 (critique)

### Sprint 6 - Modules Optionnels (P1)
⏳ **S6-03-completion-module-bgs.md** : Complétion module BGS
- 0/31 → 20-25/31 points
- **Estimation** : 4-6h
- **Priorité** : P1 (contenu)

⏳ **S6-04-completion-module-safi.md** : Complétion module SAFI
- 0/31 → 20-25/31 points
- **Estimation** : 4-6h
- **Priorité** : P1 (contenu)

⏳ **S6-05-completion-module-siep.md** : Complétion module SIEP
- 0/31 → 20-25/31 points
- **Estimation** : 4-6h
- **Priorité** : P1 (contenu)

⏳ **S6-06-completion-module-srh.md** : Complétion module SRH (DERNIER MODULE)
- 0/31 → 20-25/31 points
- **Résultat** : 45/186 → 169/186 (90.9%)
- **Estimation** : 4-6h
- **Priorité** : P1 (contenu)

### Sprint 6 - Infrastructure Optionnelle (P3)
⏳ **S6-02-notifications-ci-rollback.md** : Notifications CI + Rollback automatique
- Slack webhooks
- Rollback script
- Runbook incidents
- **Estimation** : 4-6h
- **Priorité** : P3 (nice to have)

---

## Roadmaps Archivées

**Localisation** : `roadmap/archive/`
**Documentation** : Voir `roadmap/archive/README.md` pour index complet

### Sprint 0 : Setup (1 roadmap)
- ✅ S0-00-env-setup.md

### Sprint 1 : Infrastructure Base (6 roadmaps)
- ✅ S1-01-repo-github-prive.md
- ✅ S1-02-docker-local.md
- ✅ S1-03-mkdocs-strict.md
- ✅ S1-04-template-31-points.md
- ✅ S1-05-script-scoring.md
- ✅ S1-06-import-sircom.md

### Sprint 2 : CI/CD & Documentation (10 roadmaps)
- ✅ S2-01 à S2-09 (CI/CD, PDF, preview, docs, tests)
- ❌ S2-10, S2-11 (obsolètes)

### Sprint 4 : Contenu & Validation (5 roadmaps)
- ✅ S4-00 à S4-04 (mapping, review, présentation, tag, publication)

### Sprint 5 : Robustesse (2 roadmaps)
- ✅ S5-01 (PDF accessible + coverage 89%+)

### Sprint 6 Tech First (3 roadmaps)
- ✅ S6-01-tests-e2e-ci.md
- ✅ S6-07-renforcement-securite.md
- ✅ S6-08-documentation-maintenabilite.md

### Hotfixes & Audits (3 roadmaps)
- ✅ HOTFIX-01, HOTFIX-02
- ✅ AUDIT-2025-10-07.md

---

## Parcours Recommandés

### Nouveau Contributeur
**Objectif** : Comprendre architecture projet

1. S0-00-env-setup.md (Setup initial)
2. S1-02-docker-local.md (Dev local)
3. S2-04-doc-contributeur.md (Workflow contribution)
4. CONTRIBUTING.md (Guide contributeur)

**Durée** : 1-2h lecture

### Développeur Infrastructure
**Objectif** : Comprendre CI/CD et tests

1. S2-01-github-actions.md (Workflow CI)
2. S2-05-qualite-code-python.md (Linting)
3. S5-01-tests-coverage-100.md (Coverage 89%+)
4. S6-01-tests-e2e-ci.md (E2E automatisés)

**Durée** : 2-3h lecture

### Référent Service
**Objectif** : Compléter module service

1. S1-04-template-31-points.md (Comprendre 31 points)
2. S4-00-mapping-contenus.md (Guide mapping)
3. S6-03 à S6-06 (Complétion modules)
4. CONTRIBUTING.md Section Modules

**Durée** : 1h lecture + 4-6h rédaction

---

## Roadmaps Par Thème

### Infrastructure & DevOps
- S1-02 : Docker local
- S2-01 : GitHub Actions
- S2-02 : Export PDF
- S2-03 : Preview privée (désactivée)
- S2-09 : Preview locale/PDF
- S6-02 : Notifications CI (optionnel)

### Qualité & Tests
- S2-05 : Linting (ruff + black)
- S2-06 : Tests E2E manuels
- S5-01 : Coverage 89%+
- S6-01 : Tests E2E automatisés CI

### Documentation
- S2-04 : Guide contributeur
- S2-08 : Conformité MVP
- S6-08 : CHANGELOG + MIGRATION

### Sécurité
- S6-07 : Dependabot + SECURITY.md + BFG guide

### Contenu Modules
- S1-06 : Import SIRCOM
- S2-07 : Enrichissement 6 modules
- S4-00 : Mapping contenus
- S4-01 : Review contenus
- S6-03 à S6-06 : Complétion modules (optionnel)

### Releases & Validation
- S4-02 : Présentation sponsor (fictif)
- S4-03 : Tag v1.0.0-poc
- S4-04 : Publication draft
- POC-FINALISATION : Release v1.0.0 officielle

---

## Évolution Score Qualité

### v0.1.0 (Sprint 1) : ~60/100
- Infrastructure base
- Template modules

### v0.2.0 (Sprint 2) : ~80/100
- CI/CD complète
- Tests unitaires + E2E
- Documentation

### v1.0.0-poc (Sprint 4-5) : 94/100
- PDF accessible
- Coverage 89%+
- 2 modules validés

### v1.0.0 (Sprint 6) : 97/100 ⭐
- Tests E2E automatisés CI (+2)
- Sécurité renforcée (+2)
- Documentation maintenabilité (+1)

**Cible v1.1.0** : 100/100 (avec 6 modules complétés)

---

## Références

### Documentation Principale
- **README.md** : Installation, quick start
- **CONTRIBUTING.md** : Guide contributeur
- **CHANGELOG.md** : Historique versions
- **MIGRATION.md** : Guides upgrade
- **SECURITY.md** : Responsible disclosure

### Documentation Technique
- **CLAUDE.md** : Instructions LLM
- **Agents.md** : Configuration Cursor/Codex
- **roadmap/archive/README.md** : Index roadmaps archivées

### Templates
- **roadmap/templates/** : Templates PR, présentation sponsor
- **.github/PULL_REQUEST_TEMPLATE.md** : Template PR standard

---

## Prochaines Étapes

### Court Terme (Semaine courante)
1. ✅ Archiver Sprints 0-6 terminés (32 roadmaps)
2. ✅ Créer POC-FINALISATION.md
3. ⏳ Exécuter POC-FINALISATION (release v1.0.0)

### Moyen Terme (1-2 semaines)
4. ⏳ Compléter 4 modules (S6-03 à S6-06) → 90.9% conformité
5. ⏳ Release v1.1.0 (si modules complétés)

### Long Terme (1-3 mois)
6. Migration vers organisation GitHub (production finale)
7. Onboarding référents services réels
8. Audits RGAA externes

---

**Date création** : 2025-10-07
**Auteur** : Claude Code
**Version** : 1.0
