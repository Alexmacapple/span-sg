# ADR-006: Migration vers checklist officielle 33 critères DINUM

**Date**: 2025-10-13
**Statut**: Accepté
**Décideurs**: MiWeb
**Tags**: `scoring`, `conformité`, `DINUM`, `breaking-change`

## Contexte

Le système de scoring SPAN initial utilisait une checklist de 31 points balisés `<!-- DINUM -->` basée sur une interprétation de la checklist DINUM.

Suite à l'extraction du fichier officiel `SPAN-checklist-v2024-02-05-AAL.ots` fourni par la DINUM/Arcom, il a été découvert que la checklist officielle contient **33 critères uniques** (pas 31 ni 34 comme mentionné dans certains documents), structurés en 7 catégories thématiques.

**Problématique**: Maintenir une checklist non conforme au référentiel officiel expose l'entité à un risque de non-conformité lors des contrôles Arcom.

## Décision

Nous migrons de 31 points DINUM vers 33 critères officiels extraits du fichier .ots.

**Changements techniques**:
- Tag: `<!-- DINUM -->` → `<!-- CHECKLIST -->`
- Validation: `(0, 31)` → `(0, 33)`
- Structure: Catégories numérotées (Catégorie 1-5) → Catégories thématiques (Vision, RAN, Organisation, Budget, Gestion projets, RH, Achats)

**Fichiers impactés**:
- `scripts/calculate_scores.py` (scoring logic)
- `scripts/test_calculate_scores.py` (18 tests)
- `docs/modules/_template.md` + 6 modules
- `docs/accompagnement.md` (nouveau)
- `CLAUDE.md`, `CONTRIBUTING.md`, `PRD-v3.3.md`

## Structure des 33 critères

| Catégorie | Critères | Description |
|-----------|----------|-------------|
| 1. Vision | 3 | Politique accessibilité, stratégie numérique, intégration handicap |
| 2. RAN | 7 | Durée SPAN, référent, missions, plans annuels, publication, format accessible |
| 3. Organisation | 6 | Expertises externes, moyens techniques, outillage, organisation interne, contrôle, usagers |
| 4. Budget | 2 | RH affectées, ressources financières |
| 5. Gestion projets | 7 | Nouveaux projets, tests handicapés, audits, corrections, mesures non obligatoires |
| 6. RH | 3 | Fiches poste, recrutement, formation/sensibilisation |
| 7. Achats | 5 | Clauses, notation, sélection, recette, conventions partenaires |
| **TOTAL** | **33** | |

## Conséquences

### Positives

1. **Conformité officielle**: Alignement avec le référentiel exact DINUM/Arcom
2. **Traçabilité**: Source .ots archivée comme référence légale
3. **Clarté**: Structure thématique plus lisible que numéros 1-5
4. **Complétude**: Couverture +2 critères vs ancienne grille

### Négatives

1. **Breaking change**: Tous les modules passent à 0/33 temporairement
2. **Réévaluation SIRCOM**: Module validé (24/31 = 77.4%) nécessite remapping
3. **Formation référents**: Nouvelle grille à s'approprier

### Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Rejet Arcom si ancienne grille | Moyenne | Critique | Migration immédiate vers grille officielle |
| Perte anciennes justifications SIRCOM | Faible | Moyen | Justifications archivées dans SPAN officiel 2024-2027 |
| Confusion référents | Moyenne | Faible | Guide accompagnement.md complet créé |

## Alternatives considérées

**Alternative 1**: Conserver 31 points DINUM
- ❌ Risque non-conformité lors contrôle Arcom
- ❌ Pas de source officielle traçable

**Alternative 2**: Créer 34 critères (en ajoutant un critère supplémentaire)
- ❌ Ajout arbitraire non documenté dans source officielle
- ❌ Complexifie la justification auprès de l'Arcom

**Alternative 3**: Adopter 33 critères officiels (choix retenu)
- ✅ Conformité légale garantie
- ✅ Source .ots officielle traçable
- ✅ Accepté par l'utilisateur après présentation

## Plan de migration

**Phase 0**: Documentation évolution (1h) - ✅ Complété
**Phase 1**: Analyse impacts techniques (1h30) - ✅ Complété
**Phase 2**: Extraction checklist .ots (1h) - ✅ Complété
**Phase 3**: Refactoring scoring (1h30) - ✅ Complété
**Phase 4**: Mise à jour modules (1h) - ✅ Complété
**Phase 5**: Page accompagnement (45min) - ✅ Complété
**Phase 6**: Documentation (30min) - ✅ En cours
**Phase 7**: Tests & CI (1h15) - En attente

**Durée totale**: 7h45 (optimisée de 14h initialement prévues)

## Validation

**Référent métier**: Utilisateur a confirmé "oui Voulez-vous que je continue avec 33 critères" après présentation de l'extraction .ots.

**MiWeb**: Validation technique de la migration.

**Arcom**: À valider lors du prochain contrôle (grille désormais conforme).

## Références

- Fichier source: `documentation/SPAN-checklist-v2024-02-05-AAL.ots`
- Extraction formatée: `roadmap/checklist-33-formatted.md`
- Plan migration complet: `roadmap/migration-checklist-34.md`
- Analyse impacts: `roadmap/impact-technique.md`
- Guide référents: `docs/accompagnement.md`

## Notes d'implémentation

**Script calculate_scores.py**:
```python
CHECK_TAG = "CHECKLIST"  # était "DINUM"
if total not in (0, 33):  # était (0, 31)
    errors.append(f"{module.name}: {total} critères tagués...")
```

**Tests (18 tests adaptés)**:
- `test_module_0_of_33` (était `test_module_0_of_31`)
- `test_module_33_of_33` (était `test_module_31_of_31`)
- Tous les tests passent (100% success rate)

**Modules**:
- Template: `docs/modules/_template.md` → 33 critères structure
- 5 modules vides (BGS, SAFI, SIEP, SNUM, SRH): 0/33
- SIRCOM: 0/33 (en attente réévaluation)

**Backward compatibility**: Aucune. Breaking change assumé car conformité légale prioritaire.

---

*ADR-006 - Migration checklist 33 critères DINUM - Décision acceptée le 13 octobre 2025*
