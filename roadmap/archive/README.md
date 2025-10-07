# Roadmaps Archivées

Ce dossier contient les roadmaps terminées ou obsolètes archivées après complétion.

**Date archivage massif** : 2025-10-07 (Post-Sprint 6 Tech First)
**Total archivé** : 32 roadmaps (Sprints 0-6 complétés)

---

## Index Par Sprint

### Sprint 0 : Setup Environnement (1 roadmap)
- ✅ **S0-00-env-setup.md** : Configuration environnement initial

### Sprint 1 : Infrastructure Base (6 roadmaps)
- ✅ **S1-01-repo-github-prive.md** : Création repo GitHub privé
- ✅ **S1-02-docker-local.md** : Configuration Docker Compose
- ✅ **S1-03-mkdocs-strict.md** : Mode strict MkDocs
- ✅ **S1-04-template-31-points.md** : Template modules 31 points DINUM
- ✅ **S1-05-script-scoring.md** : Script calcul scores automatique
- ✅ **S1-06-import-sircom.md** : Import module SIRCOM

### Sprint 2 : CI/CD & Documentation (10 roadmaps)
- ✅ **S2-01-github-actions.md** : Workflow GitHub Actions
- ✅ **S2-02-export-pdf.md** : Génération PDF automatique
- ✅ **S2-03-preview-privee.md** : Preview privée GitHub Pages
- ✅ **S2-04-doc-contributeur.md** : Guide contributeur (CONTRIBUTING.md)
- ✅ **S2-05-qualite-code-python.md** : Linting (ruff + black)
- ✅ **S2-06-tests-e2e-ci-local.md** : Tests E2E manuels
- ✅ **S2-07-enrichissement-modules.md** : Enrichissement 6 modules
- ✅ **S2-08-bmad-conformite-mvp.md** : Conformité MVP
- ✅ **S2-09-pr-preview-locale-pdf.md** : Preview locale/PDF (désactivation Pages)
- ❌ **S2-10-prd-actions-prioritaires-obsolete.md** : Checklist qualité (obsolète)
- ❌ **S2-11-prd-evaluation-et-actions-obsolete.md** : PRD détaillé (obsolète, duplique S2-10)

### Sprint 4 : Contenu & Validation (5 roadmaps)
- ✅ **S4-00-mapping-contenus.md** : Guide mapping assisté
- ✅ **S4-01-review-contenus.md** : Revue contenus finalisés
- ✅ **S4-02-presentation-stephane.md** : Présentation sponsor (fictif)
- ✅ **S4-03-tag-v1.md** : Tag v1.0.0-poc
- ✅ **S4-04-publication.md** : Publication draft POC

### Sprint 5 : Robustesse (2 roadmaps)
- ✅ **S5-01-pdf-accessible.md** : PDF accessible (métadonnées)
- ✅ **S5-01-tests-coverage-100.md** : Coverage 89%+ scripts production

### Sprint 6 Tech First (3 roadmaps complétées)
- ✅ **S6-01-tests-e2e-ci.md** : Tests E2E automatisés CI (+2 points Tests)
- ✅ **S6-07-renforcement-securite.md** : Dependabot + SECURITY.md (+2 points Sécurité)
- ✅ **S6-08-documentation-maintenabilite.md** : CHANGELOG + MIGRATION (+1 point Maintenabilité)

### Hotfixes (2 roadmaps)
- ✅ **HOTFIX-01-pdf-generation-ci.md** : Correction génération PDF CI
- ✅ **HOTFIX-02-pdf-path-correction.md** : Correction chemin PDF

### Audits (1 roadmap)
- ✅ **AUDIT-2025-10-07.md** : Audit informel post-POC

---

## Roadmaps Actives (Non Archivées)

**Localisation** : `roadmap/` (racine)

### Sprint 6 - Modules (Optionnel P1)
- ⏳ **S6-02-notifications-ci-rollback.md** : Notifications CI + Rollback (P3, optionnel)
- ⏳ **S6-03-completion-module-bgs.md** : Complétion module BGS (P1, 4-6h)
- ⏳ **S6-04-completion-module-safi.md** : Complétion module SAFI (P1, 4-6h)
- ⏳ **S6-05-completion-module-siep.md** : Complétion module SIEP (P1, 4-6h)
- ⏳ **S6-06-completion-module-srh.md** : Complétion module SRH (P1, 4-6h)

### POC Finalisation
- 📋 **POC-FINALISATION.md** : Release v1.0.0 officielle (nouvelle roadmap)

---

## Statistiques Archivage

**Total roadmaps projet** : 37
- **Archivées** : 32 (86.5%)
- **Actives** : 5 (13.5%)

**Par statut** :
- ✅ Terminées : 30 (81%)
- ❌ Obsolètes : 2 (5.4%) - S2-10, S2-11
- ⏳ À faire : 5 (13.5%) - S6-02 à S6-06

**Score qualité projet** : 97/100 (après archivage Sprint 6 Tech First)

---

## Politique d'Archivage

### Critères Archivage

**Archiver SI** :
1. Roadmap 100% complétée (toutes tâches terminées)
2. Roadmap obsolète (remplacée par évolution projet)
3. Roadmap caduque (non commencée ET devenue inutile)

**Ne PAS Archiver** :
- Roadmaps en cours (`status: in_progress`)
- Roadmaps planifiées futures (`status: pending`)
- Roadmaps référence historique importante

### Process Archivage

```bash
# 1. Vérifier roadmap terminée
cat roadmap/SX-YY-nom.md  # Toutes tâches complétées ?

# 2. Déplacer vers archive
mv roadmap/SX-YY-nom.md roadmap/archive/

# 3. Mettre à jour README.md archive
# Ajouter entrée dans index approprié

# 4. Commit
git add roadmap/archive/
git commit -m "chore(roadmap): archive SX-YY terminée"
```

---

## Notes Historiques

### Sprint 3 : Skippé

**Contexte** : Sprint 3 (Onboarding référents services) skippé car projet POC avec contributeurs autonomes (Alexandra, Bertrand, Alex uniquement). Pas de référents services externes à former.

**Roadmaps** : S3-01 (Création modules vides), S3-02 (Formation Git), S3-03 (Premiers contenus) → Remplacés par S2-07 (Enrichissement modules direct)

### S2-10 et S2-11 : Roadmaps Obsolètes

**S2-10-prd-actions-prioritaires-obsolete.md** :
- Checklist qualité manuelle (vérif CI, modules, build)
- Obsolète après Sprint 6 Tech First (automatisé par S6-01/07/08)

**S2-11-prd-evaluation-et-actions-obsolete.md** :
- Version PRD détaillée de S2-10 (même contenu, format BMAD)
- Archivé pour même raison (vérifications automatisées)

### Sprint 6 Tech First : Score +3 points

**Avant** : 94/100
**Après** : 97/100

**Améliorations** :
- Tests : 17/20 → 19/20 (+2 - S6-01 E2E CI)
- Sécurité : 18/20 → 20/20 (+2 - S6-07 Dependabot + SECURITY.md)
- Maintenabilité : 19/20 → 20/20 (+1 - S6-08 CHANGELOG + MIGRATION)

---

**Date mise à jour** : 2025-10-07
**Auteur** : Claude Code
**Version** : 2.0 (refonte complète post-Sprint 6)
