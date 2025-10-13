# Roadmap: Migration Conformité 31 → 34 Critères Officiels DINUM

**Créé:** 2025-10-13
**Statut:** ✅ Validé (conformité légale requise)
**Effort:** 14h (9h dev + 3h doc + 2h tests)
**Risque:** Faible (technique uniquement)
**Urgence:** Moyenne-haute (rétablir conformité)

## Executive Summary

### Contexte

Le SPAN SG utilise actuellement un scoring basé sur 31 points (ancienne version). La référence officielle DINUM/Arcom comprend **34 critères** documentés dans `documentation/checklist-span.md`.

**Situation actuelle:** NON CONFORME
**Après migration:** CONFORME avec référence officielle

### Objectifs

1. Rétablir conformité légale DINUM/Arcom
2. Aligner sur standard national (tous ministères utilisent 34)
3. Améliorer guidage référents (checklist structurée 7 catégories)

### ROI

**Investissement:** 14h dev
**Bénéfices:**
- Conformité légale garantie (élimine risque sanctions Arcom)
- Comparabilité scores avec autres ministères
- Guidage référents amélioré (gain productivité 30%)

**Verdict:** ✅ ROI fortement positif (conformité obligatoire)

---

## Analyse BMAD

### Benefits (Bénéfices)

**B1 - Conformité légale rétablie**
- ✅ 34 critères = référence officielle DINUM/Arcom
- ✅ Élimine risque rejet lors contrôle
- ✅ Actuellement NON CONFORME avec 31 points obsolètes

**B2 - Alignement méthodologique**
- ✅ Checklist officielle utilisée par évaluateurs SPAN professionnels
- ✅ Grille fine (34 vs 31) = évaluation qualité accrue
- ✅ Catégorisation claire (7 thématiques)

**B3 - Guidage référents**
- ✅ Checklist structurée = workflow pas-à-pas pour référents novices
- ✅ Auto-évaluation progressive = motivation (voir avancement)
- ✅ Page accompagnement.md = ressources centralisées

**B4 - Comparabilité nationale**
- ✅ Score X/34 comparable avec autres ministères
- ✅ Inclusion baromètre DINUM national
- ✅ Communication externe facilitée

### Measures (Indicateurs de succès)

**M1 - Adoption référents**
- KPI: 5 modules vides passent à > 50% complétion en T1 2026
- Mesure: Nombre de commits par module/mois
- Cible: ≥ 2 commits/module/mois

**M2 - Qualité SPAN**
- KPI: Score moyen 34 critères
- Mesure: Moyenne pondérée des 6 modules
- Cible: ≥ 70% (conforme) d'ici fin 2026

**M3 - Efficacité validation**
- KPI: Temps moyen validation MiWeb par module
- Mesure: Durée entre PR draft → merge main
- Cible: ≤ 5 jours ouvrés

**M4 - Utilisation accompagnement**
- KPI: Vues page accompagnement.md
- Mesure: Analytics (si activé)
- Cible: ≥ 30 visites/mois

### Assumptions (Hypothèses critiques)

**A1 - Référence officielle confirmée**
- ✅ VALIDÉ: checklist-span.md = référence DINUM/Arcom
- Source: Fournie par utilisateur

**A2 - Capacité référents**
- Hypothèse: Référents ont 2-3h/semaine pour remplir SPAN
- Validation: À confirmer avec chefs de service
- Mitigation: Obtenir mandat officiel direction

**A3 - Disponibilité MiWeb**
- Hypothèse: MiWeb peut valider 5 modules × 34 critères = 170 évaluations
- Validation: Charge travail compatible
- Mitigation: Checklist guidée réduit itérations

**A4 - CI stable après refactoring**
- Hypothèse: Tests coverage 89%+ maintenus après modification
- Validation: Tests unitaires adaptés
- Mitigation: Adapter tests AVANT de modifier script

### Drawbacks (Inconvénients)

**D1 - Refactoring technique**
- ❌ 9h dev (calculate_scores.py, tests, CI)
- ❌ Dette technique: Abandon investissement 31 points
- ❌ Risque régression: CI peut casser si tests mal adaptés

**D2 - Réévaluation SIRCOM**
- ❌ Module validé 24/31 (77%) doit être réévalué avec 34 critères
- ❌ Charge travail: MiWeb doit auditer SIRCOM à nouveau
- ❌ Risque: Score peut varier (77% → X% si critères plus stricts)

**D3 - Formation utilisateurs**
- ❌ Référents doivent apprendre nouveau système (34 vs 31)
- ❌ Documentation à mettre à jour (CLAUDE, CONTRIBUTING, PRD)
- ❌ Communication changement (email référents, réunion)

---

## Impact Analysis

### Impact 1: Technique (MAJEUR)

**Fichiers modifiés:**
1. `scripts/calculate_scores.py` (scoring)
2. `docs/modules/_template.md` (checklist 34)
3. `docs/modules/{bgs,safi,siep,sircom,snum,srh}.md` (6 modules)
4. `docs/synthese.md` (tableau scores X/34)
5. `docs/index.md` (teaser accompagnement)
6. `docs/accompagnement.md` (NOUVEAU)
7. `mkdocs-dsfr.yml` (navigation)
8. `.github/workflows/build.yml` (CI adaptation)
9. `tests/test_calculate_scores.py` (tests unitaires)
10. `CLAUDE.md`, `CONTRIBUTING.md`, `PRD-v3.3.md` (docs)
11. `docs/adr/006-migration-checklist-34.md` (NOUVEAU)

**Total:** 11 fichiers modifiés, 2 nouveaux = **13 fichiers impactés**

**Complexité changement:**
- Scoring: Logique métier critique (régression = CI fail)
- Tests: 52 tests existants (adapter ceux qui touchent scoring)
- CI/CD: 2 workflows (draft + main) à tester

**Risque régression:** ⚠️ MOYEN (scoring = cœur système)

### Impact 2: Conformité Légale (MAJEUR - POSITIF)

**Situation actuelle:**
- ❌ SPAN SG utilise 31 points (ancienne version)
- ❌ **NON CONFORME** avec référence officielle 34 critères
- ⚠️ Risque rejet lors contrôle Arcom

**Après migration:**
- ✅ SPAN SG utilise 34 critères (version officielle)
- ✅ **CONFORME** DINUM/Arcom
- ✅ Risque rejet éliminé

**Urgence:** ⭐ Moyenne-haute (se mettre en conformité rapidement)

### Impact 3: Métier (MODÉRÉ)

**Référents services (5 personnes: SNUM, SRH, SIEP, SAFI, BGS)**
- ✅ Guidage amélioré (checklist structurée)
- ✅ Autonomie (auto-évaluation)
- ⚠️ Courbe apprentissage (nouveau système)
- ⚠️ Charge travail (34 critères à comprendre)

**MiWeb (1 équipe: validation)**
- ✅ Grille évaluation explicite (objectivité)
- ❌ Charge validation: 5 modules × 34 critères = 170 évaluations
- ❌ Réévaluation SIRCOM (24/31 → X/34)
- ⚠️ Formation interne (comprendre 34 critères)

**Sponsors (Direction SG)**
- ✅ Conformité légale rétablie
- ✅ Transparence accrue (score X/34 plus fin)
- ✅ Comparabilité nationale (baromètre DINUM)

### Impact 4: Utilisateurs Finaux (POSITIF)

**Citoyens consultant SPAN SG:**
- ✅ Score X/34 = format standard attendu
- ✅ Transparence identique

**Référents autres ministères:**
- ✅ Comparabilité rétablie (tous utilisent 34)
- ✅ Partage bonnes pratiques facilité

---

## Plan d'Action Détaillé (7 Phases)

### Phase 0: Documentation Évolution (30min) - OPTIONNEL

**Objectif:** Documenter différences 31→34 pour traçabilité.

**Actions:**
1. Créer `roadmap/evolution-31-34.md`
2. Identifier quels 3 critères ajoutés dans version 34
3. Documenter rationale changement

**Livrables:**
- `roadmap/evolution-31-34.md`

### Phase 1: Analyse Technique (3h)

**Objectif:** Cartographier impacts code avant modification.

**1.1 Audit codebase (1h)**
```bash
grep -r "DINUM" . --exclude-dir={site,node_modules,.git}
grep -r "31" scripts/ docs/ tests/
find . -name "*.py" -o -name "*.md" -o -name "*.yml" | xargs grep -l "DINUM\|31"
```

**Livrables:**
- `roadmap/impact-technique.md`: Liste fichiers + lignes à modifier

**1.2 Analyser tests unitaires (1h)**
```bash
grep -r "31\|DINUM" tests/
pytest --collect-only tests/ | grep calculate_scores
```

**Livrables:**
- `roadmap/tests-impactes.md`: Liste tests à modifier

**1.3 Analyser dépendances CI (1h)**
```bash
cat .github/workflows/build.yml | grep -A5 "calculate_scores"
cat .github/workflows/build.yml | grep -B2 -A2 "synthese"
```

**Livrables:**
- `roadmap/ci-impacts.md`: Steps CI à tester

### Phase 2: Extraction Checklist 34 (2h)

**Objectif:** Transformer checklist-span.md en Markdown structuré.

**2.1 Parser checklist-span.md (30min)**

Créer `roadmap/checklist-34-raw.md` avec:
- 1. Vision (3 critères)
- 2. RAN (7 critères)
- 3. Organisation (6 critères)
- 4. Budget (2 critères)
- 5. Gestion projets (7 critères)
- 6. RH (3 critères)
- 7. Achats (5 critères)

**2.2 Formater en Markdown cochable (1h)**

```markdown
### 1. Vision (3 critères)
- [ ] Politique d'accessibilité numérique formalisée <!-- CHECKLIST -->
- [ ] Accessibilité intégrée stratégie numérique <!-- CHECKLIST -->
- [ ] Politique intégration personnes handicapées <!-- CHECKLIST -->
...
```

**2.3 Valider exhaustivité (30min)**
- Compter critères: doit totaliser 34
- Vérifier balises `<!-- CHECKLIST -->` sur chaque ligne
- Peer review MiWeb

**Livrables:**
- `roadmap/checklist-34-formatted.md`: Checklist prête à intégrer

### Phase 3: Refactoring Scoring (3h)

**Objectif:** Modifier calculate_scores.py pour scorer 34 checklist.

**3.1 Sauvegarder version actuelle (5min)**
```bash
cp scripts/calculate_scores.py scripts/calculate_scores_v1_31dinum.py
git add scripts/calculate_scores_v1_31dinum.py
git commit -m "backup: scoring 31 DINUM avant migration 34"
```

**3.2 Modifier calculate_scores.py (1h30)**

**Changements:**
```python
# AVANT
DINUM_PATTERN = r'- \[([ x])\].*?<!-- DINUM -->'
EXPECTED_TOTAL = 31

# APRÈS
CHECKLIST_PATTERN = r'- \[([ x])\].*?<!-- CHECKLIST -->'
EXPECTED_TOTAL = 34
```

**3.3 Adapter tests unitaires (1h)**

Modifier `scripts/test_calculate_scores.py`:
```python
def test_valid_module_34_criteria():
    content = "- [x] Test <!-- CHECKLIST -->\n" * 34
    assert calculate_module_score(content) == (34, 34)
```

**3.4 Tester localement (30min)**
```bash
python -m pytest scripts/test_calculate_scores.py -v
python scripts/calculate_scores.py
cat docs/synthese.md | grep "0/34"
```

**Livrables:**
- `scripts/calculate_scores.py`: Modifié
- `scripts/test_calculate_scores.py`: Tests adaptés
- Tests passent: ✅ Coverage ≥ 89%

### Phase 4: Mise à Jour Modules (2h30)

**Objectif:** Intégrer checklist 34 dans les 6 modules.

**4.1 Mettre à jour _template.md (30min)**

Structure:
```markdown
# SPAN [SERVICE]

## Checklist de conformité (34 critères)

[Copier roadmap/checklist-34-formatted.md]

**Score: 0/34 (0.0%)**

---

## 1. Périmètre
## 2. État des lieux
## 3. Organisation
## 4. Plan d'action annuel
## 5. Indicateurs clés
```

**4.2 Appliquer aux 5 modules vides (30min)**

Modules: BGS, SAFI, SIEP, SNUM, SRH

**4.3 Réévaluer SIRCOM (1h)**

Mapper chaque critère 34 vs contenu SIRCOM actuel.

**4.4 Mettre à jour synthese.md (30min)**

Afficher scores X/34 pour les 6 modules.

**Livrables:**
- 6 modules avec checklist 34
- synthese.md affiche X/34

### Phase 5: Page Accompagnement (1h30)

**Objectif:** Créer ressources guidées pour référents.

**5.1 Créer docs/accompagnement.md (1h)**

Structure:
- Introduction SPAN SG
- Comprendre checklist 34 (7 catégories)
- Workflow de complétion (diagramme)
- Ressources disponibles
- Accompagnement MiWeb
- Formations IGPDE/MENTOR
- Salon Tchap
- FAQ

**5.2 Ajouter teaser dans index.md (15min)**

```markdown
## Nouveau référent ? Besoin d'aide ?

La MiWeb accompagne les services du SG.

→ [Voir les ressources disponibles](accompagnement.md)

**Contact:** accessibilite.miweb@finances.gouv.fr
```

**5.3 Mettre à jour navigation (15min)**

`mkdocs-dsfr.yml`:
```yaml
nav:
  - SPAN (SG): index.md
  - Accompagnement: accompagnement.md  # ← NOUVEAU (position 2)
  - SPAN (services): [...]
```

**Livrables:**
- `docs/accompagnement.md`
- `docs/index.md`: Teaser ajouté
- `mkdocs-dsfr.yml`: Navigation mise à jour

### Phase 6: Documentation (2h)

**Objectif:** Documenter décision et impacts.

**6.1 Créer ADR-006 (45min)**

`docs/adr/006-migration-checklist-34.md`:
- Contexte: 31 points obsolètes, 34 critères officiels
- Décision: Migration vers 34 pour conformité
- Justification: Conformité légale + guidage
- Conséquences: Positives (conformité) + Négatives (refactoring)

**6.2 Mettre à jour CONTRIBUTING.md (30min)**

Ajouter section "Compléter un Module SPAN":
- Workflow référent (5 étapes)
- Workflow MiWeb (4 étapes validation)
- Auto-évaluation 34 critères

**6.3 Mettre à jour CLAUDE.md (30min)**

Modifier sections:
- Contraintes strictes: 34 points `<!-- CHECKLIST -->`
- Pipeline de scoring: 34 critères (pas 31 DINUM)

**6.4 Mettre à jour PRD-v3.3.md (15min)**

Section "2.2 scoring des 34 critères":
- Grille évaluation 7 catégories
- Règle validation: 0 ou 34 exactement

**Livrables:**
- ADR-006 complet
- CONTRIBUTING.md enrichi
- CLAUDE.md mis à jour
- PRD-v3.3.md mis à jour

### Phase 7: Tests & CI (2h)

**Objectif:** Valider que tout fonctionne end-to-end.

**7.1 Tests unitaires (30min)**
```bash
python -m pytest tests/ -v --cov=scripts --cov=hooks --cov-report=term-missing
python -m pytest scripts/test_calculate_scores.py --cov=scripts --cov-fail-under=89
```

**7.2 Tests intégration (30min)**
```bash
python scripts/calculate_scores.py
cat docs/synthese.md | grep "0/34\|28/34"
mkdocs build --config-file mkdocs-dsfr.yml --strict
```

**7.3 Tests E2E (30min)**
```bash
cd tests/e2e
./ci_runner.sh
```

**7.4 Tester CI sur branche (30min)**
```bash
git checkout -b feature/migration-checklist-34
git add .
git commit -m "feat(scoring): migration 31 → 34 critères officiels (ADR-006)"
git push origin feature/migration-checklist-34
gh run watch
```

**Livrables:**
- ✅ Tests unitaires: 52/52 pass
- ✅ Coverage: ≥ 89%
- ✅ E2E: 9/9 scenarios OK
- ✅ CI: Build success

---

## Timeline

| Phase | Durée | Dépendances | Livrable |
|-------|-------|-------------|----------|
| 0. Documentation évolution | 30min | - | evolution-31-34.md |
| 1. Analyse technique | 3h | Phase 0 | impact-technique.md |
| 2. Extraction checklist | 2h | - | checklist-34-formatted.md |
| 3. Refactoring scoring | 3h | Phase 2 | calculate_scores.py modifié |
| 4. Mise à jour modules | 2h30 | Phase 3 | 6 modules + synthese.md |
| 5. Page accompagnement | 1h30 | - | accompagnement.md |
| 6. Documentation | 2h | - | ADR-006 + docs |
| 7. Tests & CI | 2h | Phases 3-6 | CI green |

**Durée totale:** 14h30
**Échéance suggérée:** 3 semaines (itérations hebdomadaires)

### Planning Suggéré

**Semaine 1 (5h):**
- Lundi: Phase 0 + Phase 1 (analyse)
- Mercredi: Phase 2 (extraction checklist)

**Semaine 2 (6h):**
- Lundi: Phase 3 (refactoring scoring)
- Mercredi: Phase 4 (modules)
- Vendredi: Phase 5 (accompagnement)

**Semaine 3 (3h30):**
- Lundi: Phase 6 (documentation)
- Mercredi: Phase 7 (tests CI)
- Vendredi: Déploiement production

---

## Jalons Critiques

### Jalon 1: Code Freeze (Fin S2)
- ✅ calculate_scores.py modifié
- ✅ Tests unitaires passent (≥89% coverage)
- ✅ 6 modules mis à jour

### Jalon 2: Documentation Complete (Fin S3)
- ✅ ADR-006 publié
- ✅ Page accompagnement.md accessible
- ✅ Guides contributeur à jour

### Jalon 3: Production (Fin S3)
- ✅ CI draft success
- ✅ Merge main + déploiement
- ✅ Communication référents

---

## Risques & Mitigations

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Régression CI | 10% | Bloquant | Tests avant modification |
| Coverage drop | 15% | CI fail | Adapter tests unitaires |
| SIRCOM score baisse | 30% | Réputation | MiWeb validation rigoureuse |
| Référents dépassés | 20% | Adoption lente | Page accompagnement.md détaillée |
| Bugs scoring | 10% | Scores erronés | Tests intégration exhaustifs |

**Risque légal:** ✅ NUL (migration = conformité)

**Risque global:** ⚠️ FAIBLE (principalement technique)

---

## Rollback Plan

**Probabilité rollback:** < 5% (uniquement si régression technique majeure)

**Actions rollback:**
1. Restaurer code 31 DINUM depuis backup
   ```bash
   cp scripts/calculate_scores_v1_31dinum.py scripts/calculate_scores.py
   ```

2. Reverter commits migration
   ```bash
   git revert <commit-migration>
   ```

3. Recalculer scores avec 31 DINUM
   ```bash
   python scripts/calculate_scores.py
   ```

4. Push rollback vers main

**Coût rollback:** 2h (automatisable via script)

**Note:** Pas de rollback légal nécessaire (34 = conformité obligatoire)

---

## Métriques de Succès

### Post-déploiement (T+1 mois)

**Adoption:**
- KPI 1: ≥ 3 modules passent de 0% à > 20%
- KPI 2: ≥ 30 visites/mois accompagnement.md

**Qualité:**
- KPI 3: Temps moyen validation < 5 jours
- KPI 4: Score global 12.9% → 25%+ (doublement)

**Conformité:**
- KPI 5: 0 rejet Arcom (pas de contrôle dans 3 mois)
- KPI 6: Inclusion baromètre DINUM national

### Post-déploiement (T+6 mois)

**Maturité:**
- KPI 7: ≥ 5 modules > 50% complétés
- KPI 8: Score global > 50%
- KPI 9: SIRCOM maintient score > 75%

---

## Ressources

### Documentation Projet

- [ADR-006](../docs/adr/006-migration-checklist-34.md)
- [Checklist 34 formatted](checklist-34-formatted.md)
- [Évolution 31→34](evolution-31-34.md)
- [Impact technique](impact-technique.md)

### Références Externes

- [Checklist SPAN 34 critères](../documentation/checklist-span.md)
- [Les attendus du SPAN](../documentation/les-attendus-du-span.md)
- [RGAA - Schéma pluriannuel](https://accessibilite.numerique.gouv.fr/obligations/schema-pluriannuel/)

---

## Décision Finale

**Statut:** ✅ **GO VALIDÉ**

**Justification:**
- Conformité légale obligatoire (34 critères = référence officielle)
- Risque faible (technique uniquement)
- ROI positif (conformité + guidage référents)

**Validation:** 2025-10-13
**Décideurs:** Alexandra, MiWeb
**Sponsor:** Stéphane (Chef SNUM-SG)

**Prochaine action:** Lancer Phase 0 (documentation évolution 31→34)

---

*Dernière mise à jour: 2025-10-13*
