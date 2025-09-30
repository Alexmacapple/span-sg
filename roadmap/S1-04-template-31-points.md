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

Ouvrir http://localhost:8000/modules/_template/ (ou créer temporairement une page visible dans la nav) et vérifier :
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

## Post-tâche

Documenter dans CLAUDE.md la règle absolue :
```markdown
**Règle absolue sur les 31 points DINUM** :
- Ne jamais ajouter/supprimer de balises `<!-- DINUM -->`
- Seules les coches `[x]` peuvent être modifiées
- Tout module doit avoir exactement 0 (vide) ou 31 points
```