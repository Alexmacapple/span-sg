# Story S1-06 : Import et validation module SIRCOM

**Phase** : Semaine 1 - Setup
**Priorité** : Haute
**Estimation** : 1h
**Assigné** : Alexandra

---

## Contexte projet

SIRCOM (Service Interministériel des Ressources et des Compétences) est le **module pilote** du projet SPAN SG. Il sert de :
- Référence pour la structure des autres modules
- Test du workflow complet (édition → commit → preview → scoring)
- Démonstration pour les autres services
- Validation du template et du scoring

Le fichier `docs/modules/sircom.md` doit :
- Suivre exactement le template `_template.md`
- Contenir les 31 points DINUM officiels
- Inclure du contenu réel (pas de placeholders)
- Passer le script de scoring sans erreur
- Être prévisualisable en local

---

## Objectif

Valider que le module SIRCOM existant est conforme au template, contient 31 points DINUM, possède du contenu cohérent, et peut servir de référence pour les autres services.

---

## Prérequis

- [ ] Story S1-01 complétée (repo accessible)
- [ ] Story S1-04 complétée (template validé)
- [ ] Story S1-05 complétée (script scoring fonctionnel)
- [ ] Connaissance du service SIRCOM et de son périmètre

---

## Étapes d'implémentation

### 1. Vérifier l'existence du module

```bash
ls -lh docs/modules/sircom.md
# Attendu : fichier présent
```

### 2. Valider le front-matter

```bash
head -n 5 docs/modules/sircom.md
```

Attendu :
```yaml
---
service: SIRCOM
referent: "[Nom Référent SIRCOM]"
updated: "2025-09-30"
---
```

Points à vérifier :
- Clé `service: SIRCOM` (en majuscules)
- Référent renseigné (si "[Nom]" → à compléter ultérieurement)
- Date récente

### 3. Compter les points DINUM

```bash
grep -c "<!-- DINUM -->" docs/modules/sircom.md
```

**Attendu : 31**

Si ≠ 31 :
- Comparer avec `_template.md`
- Identifier les points manquants ou en trop
- Aligner sur les 31 points officiels

### 4. Vérifier la structure obligatoire

```bash
grep "^## [0-9]" docs/modules/sircom.md
```

Attendu (minimum) :
```
## 1. Périmètre
## 2. État des lieux
## 3. Organisation
## 4. Plan d'action annuel
## 5. Indicateurs clés
```

Vérifier aussi la section :
```bash
grep "^## points de contrôle officiels" docs/modules/sircom.md
```

### 5. Calculer le score SIRCOM

```bash
python scripts/calculate_scores.py
```

Observer la ligne SIRCOM dans `docs/synthese.md` :
```
| SIRCOM | X/31 (XX.X%) | [Statut] |
```

Valider :
- Si 0/31 → module vide, normal en setup initial
- Si X/31 avec X > 0 → vérifier que X est cohérent avec les coches `[x]`
- Si total ≠ 31 → **ERREUR CRITIQUE** à corriger

### 6. Vérifier le contenu des 5 sections

Ouvrir `docs/modules/sircom.md` et vérifier que chaque section contient du contenu (pas juste le titre) :

**Section 1. Périmètre**
```bash
sed -n '/## 1\. Périmètre/,/## 2\./p' docs/modules/sircom.md | wc -l
```
Attendu : > 5 lignes (au moins quelques phrases)

**Section 4. Plan d'action annuel**
```bash
grep -A 10 "## 4\. Plan d'action" docs/modules/sircom.md | grep "|"
```
Attendu : Tableau avec au moins 1 action

### 7. Vérifier les blocs légaux

```bash
grep -A 8 "publication et conformité" docs/modules/sircom.md
```

Vérifier présence de :
- Déclaration d'accessibilité: [URL ou TODO]
- Charge disproportionnée: [Oui/Non]

### 8. Prévisualiser SIRCOM

```bash
docker compose up
```

Ouvrir http://localhost:8000/modules/sircom/ et valider :
- Page s'affiche sans erreur 404
- Navigation fonctionnelle
- Checkboxes visibles (cochées ou non)
- Tableaux bien formatés
- Pas d'erreur de syntaxe Markdown

### 9. Comparer avec le template

```bash
# Comparer structures
diff <(grep "^##" docs/modules/_template.md) \
     <(grep "^##" docs/modules/sircom.md)
```

Si différences :
- Analyser si SIRCOM a des sections supplémentaires pertinentes
- Décider si on aligne SIRCOM sur le template ou vice-versa

### 10. Tester une modification

Cocher une case DINUM dans SIRCOM :
```bash
# Sauvegarder l'original
cp docs/modules/sircom.md /tmp/sircom-backup.md

# Cocher le premier point
sed -i '' '0,/- \[ \].*<!-- DINUM -->/s//- [x] Stratégie numérique: accessibilité intégrée et publiée <!-- DINUM -->/' docs/modules/sircom.md

# Recalculer
python scripts/calculate_scores.py

# Vérifier que le score a augmenté
grep "SIRCOM" docs/synthese.md
# Attendu : X+1/31

# Restaurer
mv /tmp/sircom-backup.md docs/modules/sircom.md
python scripts/calculate_scores.py
```

---

## Critères d'acceptation

- [ ] `docs/modules/sircom.md` existe
- [ ] Front-matter YAML valide avec `service: SIRCOM`
- [ ] Exactement 31 tags `<!-- DINUM -->` présents
- [ ] 5 sections obligatoires présentes (1-5)
- [ ] Section "points de contrôle officiels (31)" présente
- [ ] Blocs légaux (déclaration + charge disproportionnée) présents
- [ ] `python scripts/calculate_scores.py` inclut SIRCOM sans erreur
- [ ] Score SIRCOM = X/31 avec X cohérent
- [ ] http://localhost:8000/modules/sircom/ s'affiche correctement
- [ ] Aucune erreur de syntaxe Markdown

---

## Tests de validation

```bash
# Test 1 : Fichier existe
test -f docs/modules/sircom.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : Front-matter valide
python -c "
import yaml
content = open('docs/modules/sircom.md').read()
fm = content.split('---')[1]
data = yaml.safe_load(fm)
assert data['service'] == 'SIRCOM', 'Service incorrect'
print('OK')
"
# Attendu : OK

# Test 3 : Exactement 31 DINUM
test $(grep -c "<!-- DINUM -->" docs/modules/sircom.md) -eq 31 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : Sections numérotées présentes
test $(grep -c "^## [1-5]\." docs/modules/sircom.md) -ge 5 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 5 : Section points de contrôle présente
grep -q "^## points de contrôle officiels" docs/modules/sircom.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 6 : Scoring passe
python scripts/calculate_scores.py >/dev/null 2>&1 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 7 : SIRCOM dans synthese.md
grep -q "| SIRCOM |" docs/synthese.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 8 : Blocs légaux présents
grep -q "publication et conformité" docs/modules/sircom.md && echo "OK" || echo "FAIL"
# Attendu : OK
```

---

## Dépendances

**Bloque** :
- S3-01 (modules vides s'inspirent de SIRCOM)
- S3-02 (formation Git utilise SIRCOM comme exemple)

**Dépend de** :
- S1-01 (repo doit exister)
- S1-04 (template validé)
- S1-05 (script scoring testé)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 1 Setup
- **docs/modules/sircom.md** : Module à valider
- **docs/modules/_template.md** : Référence structure
- **CLAUDE.md** : Section "Structure modulaire"

---

## Notes et risques

**SIRCOM est-il complet ou vide ?**
En phase Setup (Semaine 1), SIRCOM peut être :
- **Vide** : 0/31 points cochés, structure présente → OK pour débuter
- **Partiellement rempli** : quelques points cochés → OK si cohérent
- **Complet** : 31/31 cochés → rare en S1 mais OK

L'important est que la **structure** soit conforme (31 points présents).

**Contenu réel vs placeholder**
Si le contenu des 5 sections est générique/placeholder ("À compléter", "TODO"), c'est acceptable pour S1. Le contenu sera enrichi en S3 (onboarding).

**Référent non renseigné**
Si `referent: "[Nom Référent]"` → à compléter ultérieurement avec le contact SIRCOM réel.

**URL déclaration d'accessibilité**
Si placeholder `https://[votre-domaine]/[service]/declaration-accessibilite` → normal pour S1. URLs réelles à ajouter en S4 (production).

---

## Post-tâche

Documenter SIRCOM comme module de référence dans README :
```markdown
## Module pilote : SIRCOM

Le module SIRCOM sert de référence pour la structure des autres modules.
Pour créer un nouveau module, s'inspirer de `docs/modules/sircom.md`.
```

Si SIRCOM nécessite des corrections, créer un commit dédié :
```bash
git add docs/modules/sircom.md
git commit -m "fix(sircom): aligne structure sur template 31 points DINUM"
git push origin draft
```