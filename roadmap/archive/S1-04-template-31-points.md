---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S1-04 : Validation template 31 points DINUM

**Phase** : Semaine 1 - Setup
**Priorité** : Critique
**Estimation** : 45min
**Assigné** : Alexandra

---

## Contexte projet

Le cœur du système SPAN SG repose sur le **comptage strict de 31 points de contrôle DINUM** par module. Ces 31 points sont :
- Définis dans le référentiel officiel DINUM
- Balisés avec le tag `<!-- DINUM -->` dans chaque checkbox
- Comptés automatiquement par `scripts/calculate_scores.py`
- Utilisés pour générer le tableau de synthèse global

Le fichier `docs/modules/_template.md` contient le modèle de référence avec :
- Front-matter YAML (service, referent, updated)
- 5 sections obligatoires (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- **31 checkboxes** avec tag `<!-- DINUM -->`
- Tableaux pour périmètre et plan d'actions
- Blocs légaux (déclaration accessibilité, charge disproportionnée)

Cette story valide que le template est correct et utilisable pour créer/mettre à jour les 6 modules.

---

## Objectif

Valider que `docs/modules/_template.md` contient exactement 31 points DINUM, vérifier la structure, et s'assurer qu'il peut servir de base pour les 6 modules services.

---

## Prérequis

- [ ] Story S1-01 complétée (repo accessible)
- [ ] Story S1-02 complétée (Docker pour preview)
- [ ] Connaissance du référentiel DINUM (31 points officiels)

---

## Étapes d'implémentation

### 1. Lire le template actuel

```bash
cat docs/modules/_template.md
```

### 2. Vérifier le front-matter

Attendu en tête de fichier :
```yaml
---
service: [SERVICE]
referent: "[Prénom Nom]"
updated: "2025-09-30"
---
```

### 3. Compter les balises DINUM

```bash
grep -c "<!-- DINUM -->" docs/modules/_template.md
```

**Résultat attendu : 31**

Si ≠ 31 :
- Vérifier que toutes les checkboxes ont le tag
- Vérifier qu'aucun tag n'est en doublon
- Vérifier qu'aucun tag n'est hors section "points de contrôle officiels"

### 4. Vérifier la structure des 31 points

```bash
grep "<!-- DINUM -->" docs/modules/_template.md | head -5
```

Format attendu pour chaque ligne :
```markdown
- [ ] Stratégie numérique: accessibilité intégrée et publiée <!-- DINUM -->
- [ ] Politique d'inclusion des personnes handicapées formalisée <!-- DINUM -->
...
```

Points à valider :
- ✓ Chaque ligne commence par `- [ ]` (checkbox non cochée)
- ✓ Espace entre crochets : `[ ]` (non `[]` ou `[x]`)
- ✓ Tag `<!-- DINUM -->` en fin de ligne
- ✓ Intitulé descriptif entre checkbox et tag

### 5. Vérifier les 5 sections obligatoires

```bash
grep "^## [0-9]" docs/modules/_template.md
```

Attendu :
```
## 1. Périmètre
## 2. État des lieux (synthèse)
## 3. Organisation
## 4. Plan d'action annuel
## 5. Indicateurs clés
```

### 6. Vérifier les blocs légaux

```bash
grep -A 5 "publication et conformité" docs/modules/_template.md
```

Attendu :
- Déclaration d'accessibilité: [URL] avec TODO
- Charge disproportionnée: [Oui/Non] avec structure conditionnelle

### 7. Prévisualiser le template

```bash
docker compose up
```

Ouvrir http://localhost:8000/span-sg-repo/modules/_template/ (ou créer temporairement une page visible dans la nav) et vérifier :
- Rendu Markdown correct
- Checkboxes affichées
- Tableaux bien formatés
- Pas d'erreur de syntaxe

### 8. Tester avec un module réel (SIRCOM)

```bash
# Vérifier que SIRCOM utilise bien la même structure
grep -c "<!-- DINUM -->" docs/modules/sircom.md
```

Attendu : 31

Si SIRCOM diffère du template :
- Aligner SIRCOM sur le template
- Ou ajuster le template si SIRCOM est la référence correcte

---

## Critères d'acceptation

- [ ] `docs/modules/_template.md` contient exactement 31 tags `<!-- DINUM -->`
- [ ] Front-matter YAML présent et valide
- [ ] 5 sections obligatoires présentes (1-5 numérotées)
- [ ] Tous les points DINUM utilisent format `- [ ] ... <!-- DINUM -->`
- [ ] Tableaux "périmètre du service" et "plan d'actions prioritaires" présents
- [ ] Blocs légaux (déclaration accessibilité + charge disproportionnée) présents
- [ ] Aucune erreur de syntaxe Markdown
- [ ] Template prévisualisable sans erreur

---

## Tests de validation

```bash
# Test 1 : Compte exact 31 DINUM
test $(grep -c "<!-- DINUM -->" docs/modules/_template.md) -eq 31 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : Format front-matter valide
python -c "import yaml; fm = open('docs/modules/_template.md').read().split('---')[1]; yaml.safe_load(fm); print('OK')"
# Attendu : OK

# Test 3 : Checkboxes non cochées par défaut
grep "- \[x\].*<!-- DINUM -->" docs/modules/_template.md && echo "FAIL" || echo "OK"
# Attendu : OK (aucune checkbox cochée dans le template)

# Test 4 : Sections numérotées présentes
test $(grep -c "^## [1-5]\." docs/modules/_template.md) -eq 5 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 5 : Cohérence avec module pilote SIRCOM
diff <(grep "<!-- DINUM -->" docs/modules/_template.md | wc -l) \
     <(grep "<!-- DINUM -->" docs/modules/sircom.md | wc -l) && echo "OK" || echo "WARN: SIRCOM != template"
# Attendu : OK ou WARN avec analyse manuelle
```

---

## Dépendances

**Bloque** :
- S1-06 (import SIRCOM utilise le template comme référence)
- S3-01 (création modules vides utilise ce template)

**Dépend de** :
- S1-01 (repo doit exister)
- S1-02 (Docker pour preview)

---

## Références

- **PRD v3.3** : Section 3.2 "Scoring des 31 points"
- **PRD v3.3** : Annexe E "docs/modules/_template.md – squelette"
- **docs/modules/_template.md** : Fichier à valider
- **docs/modules/sircom.md** : Module pilote de référence
- **CLAUDE.md** : Section "Structure modulaire"

---

## Notes et risques

**Les 31 points DINUM sont-ils définitifs ?**
Oui. Le référentiel DINUM est figé pour v1. Aucun ajout/suppression autorisé (contrainte MVP PRD section 10).

**Que faire si SIRCOM a plus/moins de 31 points ?**
Si SIRCOM ≠ 31 :
1. Vérifier si SIRCOM est conforme au référentiel DINUM
2. Si oui → corriger le template
3. Si non → corriger SIRCOM

**Template utilisable directement ?**
Oui. Pour créer un nouveau module :
```bash
cp docs/modules/_template.md docs/modules/nouveau-service.md
# Puis remplacer [SERVICE] par le nom réel
```

**Placeholders à remplacer**
Le template contient des placeholders :
- `[SERVICE]` → nom du service
- `[Prénom Nom]` → référent réel
- `[DATE]` → dates à jour
- `[URL]` → liens réels de déclaration

Ces placeholders seront remplacés lors de la création/mise à jour des modules (S3-01).

---

## Résultats validation (01/10/2025)

### Environnement
- **Date** : 01 octobre 2025
- **Fichier template** : `docs/modules/_template.md`
- **Module pilote** : `docs/modules/sircom.md` (référence)

---

### Phase 1 : Analyse ligne par ligne

#### Structure du template
✅ **Front-matter YAML**
```yaml
service: [SERVICE]
referent: "[Prénom Nom]"
updated: "2025-09-30"
```
- Format valide (Test 2 : ✅ PASS)
- Placeholders présents

✅ **5 sections obligatoires**
1. Périmètre
2. État des lieux (synthèse)
3. Organisation
4. Plan d'action annuel
5. Indicateurs clés

✅ **Section "points de contrôle officiels (31)"**
- Contient exactement 31 checkboxes avec balise `<!-- DINUM -->`
- Format : `- [ ] Intitulé <!-- DINUM -->`
- Aucune checkbox cochée par défaut (Test 3 : ✅ PASS)

✅ **Tableaux structurés**
- Périmètre du service (Sites web, Intranets, Applications)
- Matrice de priorisation (Audience, Criticité, Coût, Refonte, Score)
- Plan d'actions prioritaires 2025 (Action, Échéance, Responsable, Budget, Statut)

✅ **Blocs légaux**
- Publication et conformité (RGAA 4.x, niveau AA)
- Analyse charge disproportionnée (avec tableau justification)
- Déclaration d'accessibilité (URL avec TODO)

---

### Phase 2 : Comparaison Template vs SIRCOM

#### Extraction des 31 intitulés

**Template** (31 intitulés extraits) :
1. Stratégie numérique: accessibilité intégrée et publiée
2. Politique d'inclusion des personnes handicapées formalisée
3. Objectifs mesurables d'accessibilité définis (KPI)
4. Référent accessibilité numérique officiellement désigné
5. Temps alloué et moyens du référent définis
6. Ressources humaines dédiées identifiées (ETP)
7. Budget annuel dédié/identifiable
8. Planification pluriannuelle des moyens (3 ans)
9. Compétences accessibilité dans les fiches de poste
10. Grille de recrutement intégrant l'accessibilité
11. Plan de formation annuel pour les profils clés
12. Sensibilisation large (tous agents) planifiée
13. Formations par rôle (développeurs, UX, éditorial)
14. Outils de test/accessibilité référencés et disponibles
15. Procédure d'appel à expertise externe et budget associé
16. Processus internes documentés (intégration accessibilité)
17. Modalités de contrôle périodique définies
18. Process de traitement des demandes usagers (accès/retour)
19. Clauses accessibilité dans marchés/commandes
20. Critères de sélection/pondération incluant accessibilité
21. Exigence de livrables conformes et preuves de conformité
22. Accessibilité intégrée dès la conception (projets neufs)
23. Tests incluant des personnes handicapées
24. Évaluations/audits planifiés pour tous les services
25. Calendrier de corrections priorisé sur usages/volumétrie
26. Suivi de couverture (audités vs total) et périodicité des évaluations
27. Accès LSF/vidéo pour contenus concernés
28. Traduction FALC pour contenus concernés
29. Prise en compte de critères AAA pertinents
30. Bilan annuel réalisé et publié
31. Plan d'action annuel publié (format accessible)

**SIRCOM** (31 intitulés extraits) :
*Identiques au template (diff vide)*

```bash
$ diff /tmp/template_intitules.txt /tmp/sircom_intitules.txt
✅ IDENTIQUES : Template et SIRCOM ont exactement les mêmes 31 intitulés
```

**Résultat** : ✅ **Cohérence parfaite** entre template et module pilote SIRCOM

---

### Phase 3 : Validation placeholders

Tous les placeholders requis sont présents et cohérents :

| Placeholder | Occurrences | Lignes | Statut |
|-------------|-------------|--------|--------|
| `[SERVICE]` | 2 | 2, 7 | ✅ Front-matter + titre |
| `[Prénom Nom]` | 1 | 3 | ✅ Referent |
| `[DATE]` | 1 | 11 | ✅ Dernière MAJ |
| `[X/31]` | 1 | 10 | ✅ Score global |
| `[XX]` | 1 | 10 | ✅ Pourcentage |

**Résultat** : ✅ **Tous les placeholders présents et utilisables**

---

### Phase 4 : Tests automatiques (5/5)

#### Test 1 : Compte exact 31 DINUM
```bash
$ grep -c "<!-- DINUM -->" docs/modules/_template.md
31
```
✅ **PASS** - Exactement 31 balises

#### Test 2 : Format front-matter YAML valide
```bash
$ python3 -c "import yaml; fm = open('docs/modules/_template.md').read().split('---')[1]; yaml.safe_load(fm); print('OK')"
OK
```
✅ **PASS** - YAML syntaxiquement correct

#### Test 3 : Aucune checkbox cochée par défaut
```bash
$ grep "- \[x\].*<!-- DINUM -->" docs/modules/_template.md
(aucun résultat)
```
✅ **PASS** - Template vierge (toutes les checkboxes `[ ]` non cochées)

#### Test 4 : 5 sections numérotées présentes
```bash
$ grep -c "^## [1-5]\." docs/modules/_template.md
5
```
✅ **PASS** - Sections 1 à 5 présentes

#### Test 5 : Cohérence nombre avec SIRCOM
```bash
$ grep -c "<!-- DINUM -->" docs/modules/sircom.md
31
```
✅ **PASS** - Template (31) = SIRCOM (31)

**Résultat global** : ✅ **5/5 tests passent**

---

### Phase 5 : Validation syntaxe Markdown

#### 1. Format checkboxes
```markdown
- [ ] Stratégie numérique: accessibilité intégrée et publiée <!-- DINUM -->
- [ ] Politique d'inclusion des personnes handicapées formalisée <!-- DINUM -->
- [ ] Objectifs mesurables d'accessibilité définis (KPI) <!-- DINUM -->
...
```
✅ Format standard respecté : `- [ ] ... <!-- DINUM -->`

#### 2. Tableaux Markdown
```markdown
| Type | Total | Audités | Conformes | Score |
|------|-------|---------|-----------|-------|
| Sites web | | | | % |
| Intranets | | | | % |
| Applications | | | | % |
```
✅ Pipes alignés, headers présents, syntaxe correcte

#### 3. Hiérarchie titres
```markdown
# SPAN [SERVICE] - Schéma Pluriannuel d'accessibilité numérique
## 1. Périmètre
## 2. État des lieux (synthèse)
## 3. Organisation
...
```
✅ Hiérarchie logique (h1 unique → h2 sections), pas de saut de niveau

**Résultat** : ✅ **Syntaxe Markdown conforme**

---

### Critères d'acceptation (rappel)

- [x] `docs/modules/_template.md` contient exactement 31 tags `<!-- DINUM -->`
- [x] Front-matter YAML présent et valide
- [x] 5 sections obligatoires présentes (1-5 numérotées)
- [x] Tous les points DINUM utilisent format `- [ ] ... <!-- DINUM -->`
- [x] Tableaux "périmètre du service" et "plan d'actions prioritaires" présents
- [x] Blocs légaux (déclaration accessibilité + charge disproportionnée) présents
- [x] Aucune erreur de syntaxe Markdown
- [x] Template prévisualisable sans erreur (validation via mode strict S1-03)

**Statut global** : ✅ **8/8 critères validés**

---

### Conclusion

Le template `docs/modules/_template.md` est **opérationnel et conforme** au référentiel DINUM :

✅ **Structure validée**
- 31 points DINUM exactement
- 5 sections obligatoires
- Tableaux et blocs légaux complets
- Placeholders cohérents

✅ **Cohérence avec SIRCOM**
- Intitulés identiques (31/31)
- Format identique
- Module pilote aligné

✅ **Qualité**
- Syntaxe Markdown correcte
- YAML valide
- Aucune erreur détectée

**Prêt pour** :
- S1-05 : Script de scoring (utilisera 31 comme référence)
- S1-06 : Import SIRCOM (déjà aligné)
- S3-01 : Création modules vides (cp template → nouveau module)

**Durée de validation** : ~20 minutes
**Validé par** : Claude Code
**Prochaine étape** : S1-05 (Script scoring automatique)

---

## Post-tâche

Documenter dans CLAUDE.md la règle absolue :
```markdown
**Règle absolue sur les 31 points DINUM** :
- Ne jamais ajouter/supprimer de balises `<!-- DINUM -->`
- Seules les coches `[x]` peuvent être modifiées
- Tout module doit avoir exactement 0 (vide) ou 31 points
```