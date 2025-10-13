# Analyse Technique: Impacts Migration 31 → 34

**Date:** 2025-10-13
**Phase:** 1 (Analyse technique)
**Auteur:** Système
**Durée:** 3h

---

## Résumé Exécutif

**Fichiers impactés:** 13 fichiers (10 modifiés + 2 nouveaux + 1 backup)

**Complexité:** Moyenne (scoring = cœur système)

**Risque régression:** ⚠️ Moyen (tests critiques à adapter)

---

## 1. Fichiers Code Python (3 fichiers)

### 1.1 scripts/calculate_scores.py (CRITIQUE)

**Occurrences:**
- Ligne 6: `CHECK_TAG = "DINUM"`
- Ligne 96: `if total not in (0, 31):`
- Ligne 98: Message erreur `"31 ou 0"`

**Modifications requises:**

```python
# AVANT
CHECK_TAG = "DINUM"  # Ligne 6

def calculate_module_score(filepath: Path) -> Tuple[int, int, str]:
    ...
    if total not in (0, 31):  # Ligne 96
        raise ValueError(
            f"{module.name}: {total} points tagués <!-- {CHECK_TAG} --> (attendu 31 ou 0)"  # Ligne 98
        )

# APRÈS
CHECK_TAG = "CHECKLIST"  # Ligne 6

def calculate_module_score(filepath: Path) -> Tuple[int, int, str]:
    ...
    if total not in (0, 34):  # Ligne 96
        raise ValueError(
            f"{module.name}: {total} critères tagués <!-- {CHECK_TAG} --> (attendu 34 ou 0)"  # Ligne 98
        )
```

**Autres modifications:**
- Commentaires/docstrings mentionnant "31 DINUM" → "34 checklist"
- Variables `EXPECTED_TOTAL = 31` → `EXPECTED_TOTAL = 34` (si existantes)

**Criticité:** ⭐⭐⭐ CRITIQUE (cœur logique scoring)

**Effort:** 30min (changement simple mais tests requis)

---

### 1.2 scripts/test_calculate_scores.py (MAJEUR)

**Occurrences:** 15+ lignes

**Tests impactés:**

#### Test 1: `test_module_0_of_31`
```python
# AVANT (Ligne 36-42)
def test_module_0_of_31(self, tmp_path):
    content = "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(31)])
    ...
    assert total == 31

# APRÈS
def test_module_0_of_34(self, tmp_path):
    content = "".join([f"- [ ] Critère {i} <!-- CHECKLIST -->\n" for i in range(34)])
    ...
    assert total == 34
```

#### Test 2: `test_module_6_of_31_sircom`
```python
# AVANT (Ligne 44-52)
def test_module_6_of_31_sircom(self, tmp_path):
    content = (
        "".join([f"- [x] Point {i} <!-- DINUM -->\n" for i in range(6)])
    ) + "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(6, 31)])
    ...
    assert total == 31

# APRÈS
def test_module_6_of_34_sircom(self, tmp_path):
    content = (
        "".join([f"- [x] Critère {i} <!-- CHECKLIST -->\n" for i in range(6)])
    ) + "".join([f"- [ ] Critère {i} <!-- CHECKLIST -->\n" for i in range(6, 34)])
    ...
    assert total == 34
```

#### Test 3: `test_module_31_of_31`
```python
# AVANT (Ligne 55-61)
def test_module_31_of_31(self, tmp_path):
    content = "".join([f"- [x] Point {i} <!-- DINUM -->\n" for i in range(31)])
    ...
    assert checked == 31
    assert total == 31

# APRÈS
def test_module_34_of_34(self, tmp_path):
    content = "".join([f"- [x] Critère {i} <!-- CHECKLIST -->\n" for i in range(34)])
    ...
    assert checked == 34
    assert total == 34
```

#### Test 4: `test_invalid_module_30_points`
```python
# AVANT (Ligne 63-69)
def test_invalid_module_30_points(self, tmp_path):
    content = "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(30)])
    ...
    assert total not in (0, 31)

# APRÈS
def test_invalid_module_33_criteria(self, tmp_path):
    content = "".join([f"- [ ] Critère {i} <!-- CHECKLIST -->\n" for i in range(33)])
    ...
    assert total not in (0, 34)
```

#### Test 5: Test data `get_status_label`
```python
# AVANT (Ligne 78-82)
@pytest.mark.parametrize(
    "checked, total, expected",
    [
        (31, 31, "✓ Conforme"),  # 100%
        (24, 31, "✓ Conforme"),  # 77.4% >= 75%
        (23, 31, "En cours"),  # 74.2% < 75%
        (1, 31, "En cours"),  # 3.2% > 0%
        (0, 31, "Non renseigné"),  # 0%
    ],
)

# APRÈS
@pytest.mark.parametrize(
    "checked, total, expected",
    [
        (34, 34, "✓ Conforme"),  # 100%
        (26, 34, "✓ Conforme"),  # 76.5% >= 75%
        (25, 34, "En cours"),  # 73.5% < 75%
        (1, 34, "En cours"),  # 2.9% > 0%
        (0, 34, "Non renseigné"),  # 0%
    ],
)
```

#### Test 6: Fixtures test data (Lignes 13-16)
```python
# AVANT
- [x] Point réel <!-- DINUM -->
- [x] Point dans fence <!-- DINUM -->

# APRÈS
- [x] Critère réel <!-- CHECKLIST -->
- [x] Critère dans fence <!-- CHECKLIST -->
```

**Criticité:** ⭐⭐⭐ MAJEUR (tests garantissent non-régression)

**Effort:** 1h (15+ occurrences à modifier + validation)

---

### 1.3 scripts/calculate_scores_v1_31dinum.py (NOUVEAU - Backup)

**Action:** Créer backup avant modification

```bash
cp scripts/calculate_scores.py scripts/calculate_scores_v1_31dinum.py
git add scripts/calculate_scores_v1_31dinum.py
git commit -m "backup: scoring 31 DINUM avant migration 34"
```

**Justification:**
- Permet rollback rapide si régression
- Archive historique (scoring 31 fonctionnel)
- Référence pour debug

**Criticité:** ⭐ Utile (sécurité)

**Effort:** 5min

---

## 2. Fichiers Modules Markdown (7 fichiers)

### 2.1 docs/modules/_template.md (RÉFÉRENCE)

**Occurrences:** ~31 lignes `<!-- DINUM -->`

**Modification requise:**

```markdown
<!-- AVANT -->
## points de contrôle officiels (31)

- [ ] Stratégie numérique: accessibilité intégrée et publiée <!-- DINUM -->
- [ ] Politique d'inclusion des personnes handicapées formalisée <!-- DINUM -->
- [ ] Objectifs mesurables d'accessibilité définis (KPI) <!-- DINUM -->
...
[31 points au total, liste plate]

<!-- APRÈS -->
## Checklist de conformité (34 critères)

### 1. Vision (3 critères)
- [ ] Politique d'accessibilité numérique formalisée <!-- CHECKLIST -->
- [ ] Accessibilité intégrée dans la stratégie numérique <!-- CHECKLIST -->
- [ ] Politique d'intégration des personnes handicapées <!-- CHECKLIST -->

### 2. RAN - Référent Accessibilité Numérique (7 critères)
- [ ] SPAN durée ≤ 3 ans (conformité légale) <!-- CHECKLIST -->
- [ ] Position fonctionnelle et missions du référent définies <!-- CHECKLIST -->
- [ ] Plans d'actions annuels publiés (minimum année en cours) <!-- CHECKLIST -->
- [ ] SPAN publié et accessible en ligne <!-- CHECKLIST -->
- [ ] SPAN disponible dans un format accessible (PDF/A, HTML) <!-- CHECKLIST -->
- [ ] Liens vers SPAN présents dans déclarations d'accessibilité <!-- CHECKLIST -->
- [ ] SPAN mis à jour régulièrement (annuellement minimum) <!-- CHECKLIST -->

### 3. Organisation (6 critères)
...

### 4. Budget (2 critères)
...

### 5. Gestion de projets (7 critères)
...

### 6. RH - Ressources Humaines (3 critères)
...

### 7. Achats (5 critères)
...

[34 critères au total, structurés en 7 catégories]
```

**Criticité:** ⭐⭐ Important (template référence pour 6 modules)

**Effort:** 30min (extraction checklist-34 depuis checklist-span.md)

---

### 2.2 docs/modules/sircom.md (VALIDÉ - Réévaluation)

**État actuel:** 24/31 (77.4%) validé

**Action requise:** Réévaluation MiWeb

**Processus:**
1. Lire contenu SIRCOM actuel (250 lignes)
2. Mapper chaque critère 34 vs contenu présent
3. Cocher `[x]` critères conformes
4. Identifier 3 nouveaux critères ajoutés dans version 34:
   - Format accessible SPAN (PDF/A, HTML RGAA)
   - Mise à jour régulière SPAN (annuelle)
   - Suivi conformité marchés (recette livrables)
5. Calculer nouveau score X/34

**Scénarios:**
- Optimiste: 28/34 (82.4%) si 3 nouveaux conformes → +5%
- Réaliste: 26/34 (76.5%) si 2/3 nouveaux → Stable
- Pessimiste: 24/34 (70.6%) si 0/3 nouveaux + 1 ancien décoché → -7%

**Criticité:** ⭐⭐ Important (module référence)

**Effort:** 1h (lecture + mapping + validation MiWeb)

---

### 2.3 docs/modules/{bgs,safi,siep,snum,srh}.md (5 modules VIDES)

**État actuel:** 0/31 (0.0%)

**Action requise:** Remplacement template

**Processus:**
1. Ouvrir module (ex: snum.md)
2. Supprimer section `## points de contrôle officiels (31)`
3. Copier section `## Checklist de conformité (34 critères)` depuis _template.md mis à jour
4. Conserver front-matter et structure 5 sections

**Impact:** ✅ Nul (déjà vides, intègrent directement 34)

**Criticité:** ⭐ Faible (modules vides)

**Effort:** 15min total (5 modules × 3min chacun)

---

## 3. Fichier Synthèse (1 fichier)

### 3.1 docs/synthese.md (AUTO-GÉNÉRÉ)

**Modification:** Indirecte (via calculate_scores.py)

**Changement attendu:**

```html
<!-- AVANT -->
<tr>
    <td>SIRCOM</td>
    <td>24/31 (77.4%)</td>
    <td>Conforme</td>
    <td>Validé</td>
</tr>
<tr>
    <td>SNUM</td>
    <td>0/31 (0.0%)</td>
    <td>Non renseigné</td>
    <td>Brouillon</td>
</tr>

<!-- APRÈS -->
<tr>
    <td>SIRCOM</td>
    <td>26/34 (76.5%)</td>  ← Score réévalué
    <td>Conforme</td>
    <td>Validé</td>
</tr>
<tr>
    <td>SNUM</td>
    <td>0/34 (0.0%)</td>
    <td>Non renseigné</td>
    <td>Brouillon</td>
</tr>
```

**Note:** Fichier généré par `calculate_scores.py`, pas de modification manuelle.

**Criticité:** ⭐ Automatique

**Effort:** 0min (auto)

---

## 4. Fichier CI/CD (1 fichier)

### 4.1 .github/workflows/build.yml (VALIDATION)

**Occurrences:** Aucune directe (appelle calculate_scores.py)

**Steps impactés:**

#### Step: Calculate SPAN scores (Ligne 100)
```yaml
- name: Calculate SPAN scores
  run: python scripts/calculate_scores.py
```

**Impact:** Script modifié mais commande identique → ✅ Pas de changement workflow

#### Step: Build site DSFR (Ligne 103)
```yaml
- name: Build site DSFR
  run: mkdocs build --config-file mkdocs-dsfr.yml --strict
```

**Impact:** synthese.md régénéré avec scores X/34 → ✅ Build OK

#### Step: Run unit tests (Ligne 78)
```yaml
- name: Run unit tests
  run: python -m pytest scripts/ -v --cov=scripts --cov-report=term-missing
```

**Impact:** Tests modifiés pour 34 critères → ⚠️ Doit passer après adaptation tests

**Action:** Tester CI sur branche feature avant merge main

**Criticité:** ⭐⭐ Important (validation CI obligatoire)

**Effort:** 30min (monitoring CI)

---

## 5. Fichiers Documentation (4 fichiers)

### 5.1 CLAUDE.md (RÈGLES AGENTS)

**Occurrences:**
- Ligne ~40: "31 points balisés `<!-- DINUM -->`"
- Ligne ~44: "total ≠ 0 ou 31"

**Modifications requises:**

```markdown
<!-- AVANT -->
### Contraintes strictes
- Ne pas modifier la logique de scoring: 31 points balisés `<!-- DINUM -->` uniquement.
- Périmètre v1: 6 modules (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS).

### Pipeline de scoring (31 points DINUM)
Le système repose sur un comptage strict des cases cochées marquées `<!-- DINUM -->`:
- Compte checked/total par module
- Échoue si total ≠ 0 ou 31 (validation périmètre)

<!-- APRÈS -->
### Contraintes strictes
- Ne pas modifier la logique de scoring: 34 critères balisés `<!-- CHECKLIST -->` uniquement.
- Périmètre v1: 6 modules (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS).

### Pipeline de scoring (34 critères checklist)
Le système repose sur un comptage strict des cases cochées marquées `<!-- CHECKLIST -->`:
- Compte checked/total par module
- Échoue si total ≠ 0 ou 34 (validation périmètre)
- Génère `docs/synthese.md` avec scores X/34

**Règle absolue**: Ne jamais ajouter/supprimer de balises `<!-- CHECKLIST -->`. Seules les coches `[x]` peuvent être modifiées.
```

**Criticité:** ⭐ Important (règles agents IA)

**Effort:** 15min

---

### 5.2 CONTRIBUTING.md (GUIDE CONTRIBUTEUR)

**Modifications:** Ajout section "Compléter un Module SPAN"

**Contenu nouveau:**
- Workflow référent (5 étapes)
- Workflow MiWeb (validation)
- Auto-évaluation 34 critères

**Criticité:** ⭐⭐ Important (guide utilisateurs)

**Effort:** 30min (nouvelle section ~100 lignes)

---

### 5.3 PRD-v3.3.md (PRODUCT REQUIREMENTS)

**Occurrences:**
- Section "2.2 scoring des 31 points"

**Modifications requises:**

```markdown
<!-- AVANT -->
### 2.2 scoring des 31 points

Chaque module contient une checklist de 31 points de contrôle DINUM, balisés `<!-- DINUM -->`.

**Règle de validation:**
- Module vide: 0/31 accepté
- Module complété: exactement 31 points

<!-- APRÈS -->
### 2.2 scoring des 34 critères

Chaque module contient une checklist de 34 critères de conformité SPAN, balisés `<!-- CHECKLIST -->`.

**Grille d'évaluation:**
1. Vision (3 critères)
2. RAN - Référent (7 critères)
3. Organisation (6 critères)
4. Budget (2 critères)
5. Gestion projets (7 critères)
6. RH (3 critères)
7. Achats (5 critères)

**Règle de validation:**
- Module vide: 0/34 accepté
- Module complété: exactement 34 critères

**Note:** Cette grille remplace les 31 points DINUM initiaux (voir ADR-006).
```

**Criticité:** ⭐ Important (documentation officielle)

**Effort:** 15min

---

### 5.4 docs/adr/006-migration-checklist-34.md (NOUVEAU)

**Contenu:** Architecture Decision Record complet

**Sections:**
- Contexte (31 obsolète, 34 officiel)
- Décision (migration)
- Justification (conformité + guidage)
- Conséquences (positives/négatives)
- Alternatives considérées
- Validation

**Criticité:** ⭐⭐ Important (traçabilité décision)

**Effort:** 45min (ADR complet ~200 lignes)

---

## 6. Nouveaux Fichiers (2 fichiers)

### 6.1 docs/accompagnement.md (NOUVEAU)

**Contenu:** Page guide référents

**Sections:**
- Introduction SPAN SG
- Comprendre checklist 34 (7 catégories)
- Workflow de complétion (diagramme Mermaid)
- Ressources disponibles
- Accompagnement MiWeb
- Formations IGPDE/MENTOR
- Salon Tchap
- FAQ

**Criticité:** ⭐⭐⭐ MAJEUR (guidage référents)

**Effort:** 1h (page complète ~250 lignes)

---

### 6.2 docs/index.md (MODIFIÉ - Teaser)

**Ajout:** Section "Nouveau référent ? Besoin d'aide ?"

```markdown
## Nouveau référent ? Besoin d'aide ?

La MiWeb accompagne les services du SG dans la réalisation de leur SPAN :
sensibilisation, formation, audit, validation.

→ [Voir les ressources disponibles](accompagnement.md)

**Contact :** accessibilite.miweb@finances.gouv.fr
```

**Criticité:** ⭐ Utile (visibilité accompagnement)

**Effort:** 15min

---

## 7. Configuration (1 fichier)

### 7.1 mkdocs-dsfr.yml (NAVIGATION)

**Modification:** Ajout page accompagnement.md

```yaml
# AVANT
nav:
  - SPAN (SG): index.md
  - SPAN (services):
    - BGS: modules/bgs.md
    ...

# APRÈS
nav:
  - SPAN (SG): index.md
  - Accompagnement: accompagnement.md  # ← NOUVEAU (position 2)
  - SPAN (services):
    - BGS: modules/bgs.md
    ...
```

**Criticité:** ⭐ Important (navigation visible)

**Effort:** 5min

---

## Synthèse Impacts

### Fichiers par Type

| Type | Modifiés | Nouveaux | Total |
|------|----------|----------|-------|
| **Code Python** | 2 | 1 (backup) | 3 |
| **Modules Markdown** | 7 | 0 | 7 |
| **Documentation** | 4 | 2 (ADR, accompagnement) | 6 |
| **Configuration** | 2 (synthese auto, CI validation) | 0 | 2 |
| **TOTAL** | **13** | **3** | **16** |

### Criticité par Fichier

| Criticité | Fichiers | Impact | Effort Total |
|-----------|----------|--------|--------------|
| ⭐⭐⭐ CRITIQUE | calculate_scores.py, test_calculate_scores.py, accompagnement.md | Bloquant | 2h30 |
| ⭐⭐ MAJEUR | _template.md, sircom.md, CONTRIBUTING.md, ADR-006 | Important | 3h15 |
| ⭐ IMPORTANT | 5 modules vides, CLAUDE.md, PRD, index, mkdocs | Utile | 1h30 |
| ✅ AUTO | synthese.md, CI validation | Automatique | 30min |

**Effort total estimé:** 7h45 (vs 9h initial) → Optimisé de 14%

---

## Dépendances & Ordre Exécution

### Phase 3 (Refactoring scoring)
**Dépendances:** Aucune
**Fichiers:**
1. scripts/calculate_scores_v1_31dinum.py (backup)
2. scripts/calculate_scores.py (modification)
3. scripts/test_calculate_scores.py (adaptation)

**Ordre:** Backup → Modification script → Adaptation tests → Tests locaux

---

### Phase 4 (Mise à jour modules)
**Dépendances:** Phase 2 (checklist-34-formatted.md)
**Fichiers:**
1. docs/modules/_template.md
2. docs/modules/{bgs,safi,siep,snum,srh}.md (5 modules vides)
3. docs/modules/sircom.md (réévaluation)
4. docs/synthese.md (auto-généré)

**Ordre:** Template → Modules vides → Réévaluation SIRCOM → Génération synthèse

---

### Phase 5 (Page accompagnement)
**Dépendances:** Aucune (parallélisable avec Phase 4)
**Fichiers:**
1. docs/accompagnement.md
2. docs/index.md (teaser)
3. mkdocs-dsfr.yml (navigation)

**Ordre:** Accompagnement → Teaser → Navigation

---

### Phase 6 (Documentation)
**Dépendances:** Phases 3-5 terminées
**Fichiers:**
1. docs/adr/006-migration-checklist-34.md
2. CONTRIBUTING.md
3. CLAUDE.md
4. PRD-v3.3.md

**Ordre:** ADR → Guides (CONTRIBUTING, CLAUDE, PRD)

---

### Phase 7 (Tests CI)
**Dépendances:** Toutes phases précédentes
**Fichiers:**
1. Tests unitaires (scripts/test_calculate_scores.py)
2. Tests intégration (calculate_scores.py + build)
3. Tests E2E (9 scenarios)
4. CI GitHub Actions (.github/workflows/build.yml)

**Ordre:** Tests unitaires → Tests intégration → Tests E2E → CI branche

---

## Risques Techniques Identifiés

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| **Régression calculate_scores.py** | 10% | Bloquant (CI fail) | Tests unitaires avant modification |
| **Tests coverage drop < 89%** | 15% | Bloquant (CI fail) | Adapter tous tests score-related |
| **SIRCOM score baisse significative** | 30% | Réputation (77% → <70%) | MiWeb réévaluation rigoureuse |
| **Oubli modification docs** | 20% | Confusion utilisateurs | Checklist exhaustive (16 fichiers) |
| **CI cache invalide** | 10% | Build lent (5min → 10min) | Acceptable, pas bloquant |

---

## Checklist Validation Phase 1

- [x] Identifier tous fichiers Python utilisant DINUM/31
- [x] Identifier tous modules Markdown avec `<!-- DINUM -->`
- [x] Cartographier dépendances CI/CD
- [x] Lister fichiers documentation impactés
- [x] Estimer effort par fichier
- [x] Définir ordre exécution phases
- [x] Identifier risques techniques

**Résultat Phase 1:** ✅ Analyse complète (16 fichiers cartographiés, effort optimisé 9h → 7h45)

---

## Prochaine Étape

**Phase 2:** Extraction et formatage checklist 34 critères depuis `documentation/checklist-span.md`

**Livrables attendus:**
- `roadmap/checklist-34-raw.md` (34 critères bruts)
- `roadmap/checklist-34-formatted.md` (Markdown cochable avec `<!-- CHECKLIST -->`)

---

*Analyse terminée: 2025-10-13*
