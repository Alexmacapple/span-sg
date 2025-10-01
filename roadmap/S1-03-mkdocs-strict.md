---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S1-03 : Configuration MkDocs base + mode strict

**Phase** : Semaine 1 - Setup
**Priorité** : Critique
**Estimation** : 1h
**Assigné** : Alexandra

---

## Contexte projet

MkDocs Material est le générateur de site statique choisi pour SPAN SG. Le **mode strict** (`strict: true`) est une contrainte critique du projet qui garantit :
- Détection d'erreurs de liens cassés
- Validation des références internes
- Blocage du build en cas d'incohérence
- Qualité documentaire élevée

La configuration actuelle dans `mkdocs.yml` doit être validée et testée pour garantir :
1. Site_url et repo_url corrects
2. Navigation cohérente vers les 6 modules
3. Plugin PDF configuré
4. Thème Material en français
5. Mode strict activé sans erreur

---

## Objectif

Valider la configuration MkDocs existante, ajuster les URLs, tester le mode strict, et garantir que le build fonctionne sans erreur ni warning.

---

## Prérequis

- [ ] Story S1-01 complétée (repo créé)
- [ ] Story S1-02 complétée (Docker fonctionnel)
- [ ] URLs GitHub Pages et repo définitives connues

---

## Étapes d'implémentation

### 1. Vérifier la configuration actuelle

```bash
cat mkdocs.yml
```

Points à vérifier :
- `strict: true` présent
- `site_name: SPAN SG`
- `theme.name: material` + `theme.language: fr`
- Navigation contient les 6 modules
- Plugins : search (fr) + pdf-export configuré

### 2. Ajuster site_url et repo_url

Éditer `mkdocs.yml` :

```yaml
site_url: https://alexmacapple.github.io/span-sg-repo/
repo_url: https://github.com/Alexmacapple/span-sg-repo
```

**Note** : Si migration vers organisation prévue, ajuster en conséquence :
```yaml
site_url: https://[organisation].github.io/span-sg/
repo_url: https://github.com/[organisation]/span-sg
```

### 3. Tester le build en mode strict

```bash
# Via Docker
docker compose up

# Ou sans Docker
mkdocs build --strict
```

Observer les logs pour détecter :
- ❌ Erreurs (liens cassés, fichiers manquants)
- ⚠️ Warnings (références ambiguës)

### 4. Résoudre les erreurs détectées

Erreurs possibles et solutions :

**Erreur : "file not found"**
```
ERROR - Doc file 'modules/sircom.md' not found
```
→ Vérifier que tous les fichiers listés dans `nav:` existent

**Erreur : "broken link"**
```
WARNING - Broken link to 'modules/inexistant.md'
```
→ Corriger ou supprimer le lien

**Erreur : "duplicate heading"**
```
WARNING - Duplicate heading in docs/index.md
```
→ Renommer les titres en doublon

### 5. Valider la navigation

Tester l'accès à toutes les pages via http://localhost:8000 :
- ✓ Accueil (`docs/index.md`)
- ✓ Synthèse (`docs/synthese.md`)
- ✓ Processus (`docs/processus.md`)
- ✓ SNUM (`docs/modules/snum.md`)
- ✓ SIRCOM (`docs/modules/sircom.md`)
- ✓ SRH (`docs/modules/srh.md`)
- ✓ SIEP (`docs/modules/siep.md`)
- ✓ SAFI (`docs/modules/safi.md`)
- ✓ BGS (`docs/modules/bgs.md`)

### 6. Tester le build de production

```bash
# Build complet avec artifacts
mkdocs build

# Vérifier répertoire site/ généré
ls -la site/
# Attendu : index.html, modules/, assets/, search/, etc.
```

### 7. Committer les ajustements

```bash
git add mkdocs.yml
git commit -m "chore: configure site_url et repo_url pour GitHub Pages"
git push origin draft
```

---

## Critères d'acceptation

- [ ] `mkdocs.yml` contient `strict: true`
- [ ] `site_url` et `repo_url` pointent vers le bon repo
- [ ] `mkdocs build --strict` termine avec exit code 0
- [ ] Aucun WARNING ni ERROR dans les logs
- [ ] http://localhost:8000 affiche toutes les pages de la nav
- [ ] Navigation entre pages fonctionnelle
- [ ] Recherche fonctionne (test : rechercher "DINUM")
- [ ] Build produit un répertoire `site/` complet

---

## Tests de validation

```bash
# Test 1 : Build strict sans erreur
mkdocs build --strict
echo $?
# Attendu : 0 (succès)

# Test 2 : Vérifier site/ généré
test -f site/index.html && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : Vérifier tous les modules présents
for module in snum sircom srh siep safi bgs; do
  test -f "site/modules/$module/index.html" && echo "$module OK" || echo "$module FAIL"
done
# Attendu : 6x "OK"

# Test 4 : Vérifier strict mode activé
grep "strict: true" mkdocs.yml
# Attendu : strict: true

# Test 5 : Lint configuration
python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))" && echo "YAML valid"
# Attendu : YAML valid
```

---

## Dépendances

**Bloque** :
- S1-05 (script scoring dépend de la structure docs/)
- S2-01 (CI GitHub Actions utilise mkdocs build)

**Dépend de** :
- S1-01 (repo doit exister)
- S1-02 (Docker pour tester localement)

---

## Références

- **PRD v3.3** : Section 3.1 "MkDocs configuration"
- **mkdocs.yml** : Configuration principale
- **CLAUDE.md** : Section "Configuration MkDocs triple"
- **Documentation MkDocs** : https://www.mkdocs.org/user-guide/configuration/#strict

---

## Notes et risques

**Mode strict trop contraignant ?**
Si le mode strict bloque le build pour des warnings mineurs, possibilité de le désactiver temporairement pour débloquer, mais c'est **fortement déconseillé** (contrainte MVP).

**Plugin PDF optionnel pour ce test**
Le plugin `mkdocs-pdf-export-plugin` n'est pas nécessaire pour valider le strict mode. Il sera testé dans S2-02.

**CSS custom**
Le fichier `docs/assets/custom.css` peut être édité ultérieurement sans impact sur le strict mode.

**Performance du build**
Build actuel ~2-3 secondes. Si > 10s, vérifier la taille des images dans `docs/assets/`.

---

## Post-tâche

Une fois validé, documenter dans le README :
```markdown
## Build et validation

Le projet utilise le mode strict MkDocs (`strict: true`).
Tout build doit passer sans WARNING ni ERROR.

Test local : `mkdocs build --strict`
```