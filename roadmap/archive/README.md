# Roadmaps Archivées

Ce dossier contient les roadmaps obsolètes ou remplacées par l'évolution du projet.

## Roadmaps Archivées

### S2-10-prd-actions-prioritaires-obsolete.md

**Date archivage** : 2025-10-07
**Raison** : Checklist qualité manuelle devenue obsolète après Sprint 6 Tech First

**Contexte** :
- Créé post-S2-09 (politique "sans Pages")
- Demandait vérifications manuelles : workflow CI, balises DINUM, front-matter, build local
- Toutes vérifications désormais automatisées par CI/CD (S6-01, S6-07, S6-08)

**Résultat vérifications** (07/10/2025) :
- ✅ Workflow CI : Conforme (main → gh-pages uniquement)
- ✅ Modules : 31 balises DINUM par module, front-matter complet
- ✅ Build strict : Passe (0.36s)
- ✅ CI/CD : Tests unitaires + E2E + PDF + scoring automatique

**Remplacé par** :
- S6-01 : Tests E2E automatisés CI (vérifications comportementales)
- S6-07 : Renforcement sécurité (Dependabot scan automatique)
- S6-08 : Documentation maintenabilité (CHANGELOG + MIGRATION)

**Score qualité final** : 97/100 (confirme conformité toutes vérifications)

---

## Politique d'Archivage

**Critères archivage roadmap** :
1. Roadmap complétée ET dépassée par évolution projet
2. Roadmap non commencée ET devenue caduque
3. Roadmap remplacée par approche alternative

**Ne PAS archiver** :
- Roadmaps en cours (status: in_progress)
- Roadmaps planifiées futures (Unreleased)
- Roadmaps servant de référence historique importante

---

**Date création** : 2025-10-07
**Auteur** : Claude Code
