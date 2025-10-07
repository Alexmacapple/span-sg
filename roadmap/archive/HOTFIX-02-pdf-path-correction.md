---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: hotfix
autonomous: true
validation: ci-test
priority: critique
---

# HOTFIX-02 : Correction chemin PDF pour enrichissement metadata

**Phase** : Hotfix immédiat (suite HOTFIX-01)
**Priorité** : ⚠️ CRITIQUE
**Estimation** : 3 min
**Assigné** : Alexandra
**Détection** : CI run (b0be98d) - suite HOTFIX-01

---

## Problème détecté

### Symptôme
❌ **Step "Enrich PDF metadata" échoue avec "Fichier introuvable"**

Malgré HOTFIX-01, le PDF est bien généré mais le script d'enrichissement ne le trouve pas.

Workflow CI : https://github.com/Alexmacapple/span-sg-repo/actions/runs/18166288931/job/51709314693

### Logs CI

#### Step "Generate PDF" ✅
```
INFO - Output a PDF to "/home/runner/work/span-sg-repo/span-sg-repo/site/exports/span-sg.pdf"
INFO - Converting 10 articles to PDF took 5.9s
INFO - Documentation built in 6.23 seconds
```

**Constat** : Le PDF est généré avec succès dans **`site/exports/span-sg.pdf`**

#### Step "Enrich PDF metadata" ❌
```
❌ Fichier introuvable: exports/span-sg.pdf
Error: Process completed with exit code 1.
```

**Constat** : Le script cherche dans **`exports/span-sg.pdf`** (chemin incorrect)

---

## Cause racine

### Discordance de chemins

**Config `mkdocs-pdf.yml` ligne 18** :
```yaml
output_path: exports/span-sg.pdf
```

MkDocs interprète ce chemin comme **relatif au dossier de build `site/`**, donc le PDF est créé à :
```
site/exports/span-sg.pdf
```

**Workflow `.github/workflows/build.yml` ligne 34** :
```yaml
- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
```

Le script cherche à la racine :
```
exports/span-sg.pdf  ← N'EXISTE PAS
```

### Pourquoi ce problème n'a pas été détecté avant ?

1. HOTFIX-01 a résolu le problème de génération (`enabled_if_env`)
2. Mais on n'a jamais testé le workflow complet en local
3. Le `continue-on-error: true` masque l'erreur (workflow reste vert)

---

## Impact

### Immédiat
- ✅ PDF généré dans `site/exports/span-sg.pdf`
- ❌ Metadata **non enrichies** (titre, langue, keywords manquants)
- ⚠️ Artefact uploadé contient `site/` mais le PDF n'a pas les bonnes metadata

### Utilisateurs
- ⚠️ PDF accessible mais sans metadata optimales (accessibilité réduite)
- ⚠️ Titre du document vide dans les lecteurs PDF
- ⚠️ Pas de langue définie (problème accessibilité)

---

## Solutions envisagées

### Option A : Corriger le chemin dans le workflow ✅ **RECOMMANDÉ**

**Modification** : `.github/workflows/build.yml` ligne 34
```yaml
# AVANT
- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
  continue-on-error: true

# APRÈS
- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py site/exports/span-sg.pdf
  continue-on-error: true
```

**Avantages** :
- ✅ Simple (1 mot à changer : `site/exports/...`)
- ✅ Pas de modification de structure de dossiers
- ✅ Cohérent avec l'output réel du plugin

**Inconvénients** :
- Aucun

---

### Option B : Copier le PDF à la racine après génération

**Modification** : `.github/workflows/build.yml` ligne 31
```yaml
- name: Generate PDF
  run: mkdocs build --config-file mkdocs-pdf.yml

- name: Copy PDF to root exports
  run: |
    mkdir -p exports
    cp site/exports/span-sg.pdf exports/

- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
  continue-on-error: true
```

**Avantages** :
- ✅ PDF disponible à 2 endroits (`site/exports/` et `exports/`)

**Inconvénients** :
- ❌ Duplication du fichier (double espace disque)
- ❌ Plus complexe (3 lignes au lieu de 1)
- ❌ Confusion : quel PDF uploader dans artefacts ?

---

### Option C : Changer `output_path` pour sortir de `site/`

**Modification** : `mkdocs-pdf.yml` ligne 18
```yaml
# AVANT
output_path: exports/span-sg.pdf

# APRÈS
output_path: ../exports/span-sg.pdf  # Remonte d'un niveau
```

**Avantages** :
- ✅ PDF directement à la racine

**Inconvénients** :
- ❌ Comportement non standard de MkDocs (chemins relatifs avec `..`)
- ❌ Risque de confusion future
- ⚠️ Peut ne pas fonctionner selon version du plugin

---

## Décision : Option A

**Justification** :
1. **Principe de moindre surprise** : Le plugin crée le PDF dans `site/`, c'est son comportement par défaut
2. **Simplicité maximale** : 1 seul caractère à ajouter (`site/`)
3. **Pas de side-effect** : Aucun changement de structure
4. **Facilité de debug** : Chemin explicite et tracé

---

## Plan d'action (BMAD)

### Étape 1 : Corriger le chemin dans le workflow

**Fichier** : `.github/workflows/build.yml` ligne 34

```yaml
- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py site/exports/span-sg.pdf
  continue-on-error: true
```

### Étape 2 : Vérifier cohérence upload artifacts

**Fichier** : `.github/workflows/build.yml` ligne 41-43

Actuellement :
```yaml
path: |
  site/
  exports/
```

Le chemin `exports/` est inutile (vide), mais **ne pose pas de problème** (GitHub Actions ignore les chemins inexistants).

**Décision** : On le laisse pour éviter des changements superflus. Si besoin futur, on pourra le retirer.

### Étape 3 : Retirer `continue-on-error: true` (optionnel mais recommandé)

Maintenant que le chemin est correct, on peut faire échouer le build si l'enrichissement échoue.

```yaml
- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py site/exports/span-sg.pdf
  # Retiré : continue-on-error: true
```

**Avantages** :
- ✅ Détection immédiate de régressions
- ✅ Fail-fast (ne pas déployer un PDF sans metadata)

**Inconvénients** :
- ⚠️ Si `pikepdf` a un bug, le build échoue complètement

**Décision** : **On retire** `continue-on-error: true` pour garantir qualité du PDF.

### Étape 4 : Commiter et pousser

```bash
git add .github/workflows/build.yml
git commit -m "fix(pdf): correction chemin enrichissement metadata (site/exports/)

Problème :
- Plugin génère PDF dans site/exports/span-sg.pdf
- Script cherchait dans exports/span-sg.pdf (racine)
- Erreur 'Fichier introuvable' malgré PDF généré

Solution :
- Corrige chemin : site/exports/span-sg.pdf
- Retire continue-on-error: true (fail-fast)

Suite de : HOTFIX-01 (suppression enabled_if_env)

Fixes https://github.com/Alexmacapple/span-sg-repo/actions/runs/18166288931

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin draft
```

### Étape 5 : Valider en CI

1. Attendre fin du workflow GitHub Actions
2. Vérifier logs step "Enrich PDF metadata" :
   - ✅ `📄 Enrichissement metadata: site/exports/span-sg.pdf`
   - ✅ `✅ Metadata enrichies avec succès`
   - ✅ `📋 Metadata ajoutées: Titre, Langue, Auteur...`
3. Télécharger artefact `span-site.zip`
4. Vérifier `site/exports/span-sg.pdf` avec metadata :
   ```bash
   pdfinfo site/exports/span-sg.pdf | grep -E "Title|Language|Keywords"
   ```

---

## Critères d'acceptation

- [ ] Chemin corrigé dans `.github/workflows/build.yml` ligne 34 : `site/exports/span-sg.pdf`
- [ ] `continue-on-error: true` retiré (fail-fast activé)
- [ ] Commit poussé sur `draft`
- [ ] CI passe en vert (workflow "Build SPAN")
- [ ] Step "Enrich PDF metadata" affiche succès avec logs détaillés
- [ ] Artefact `span-site.zip` contient `site/exports/span-sg.pdf` avec metadata
- [ ] Validation metadata : `pdfinfo` affiche Titre, Langue, Keywords

---

## Tests de validation

```bash
# Test 1 : Chemin corrigé dans workflow
grep -q "site/exports/span-sg.pdf" .github/workflows/build.yml && echo "✅ OK" || echo "❌ FAIL"
# Attendu : ✅ OK

# Test 2 : continue-on-error retiré
! grep -A1 "Enrich PDF metadata" .github/workflows/build.yml | grep -q "continue-on-error" && echo "✅ OK" || echo "⚠️ WARN: continue-on-error encore présent"
# Attendu : ✅ OK

# Test 3 : Génération locale + enrichissement
mkdocs build --config-file mkdocs-pdf.yml
python scripts/enrich_pdf_metadata.py site/exports/span-sg.pdf
test -f site/exports/span-sg.pdf && echo "✅ OK" || echo "❌ FAIL"
# Attendu : ✅ OK
```

---

## Rollback (si nécessaire)

Si problème inattendu :

```bash
git revert [hash-du-commit]
git push origin draft
```

**Probabilité de rollback** : < 1% (correction triviale)

---

## Leçons apprées (ajout au post-mortem HOTFIX-01)

### Pourquoi le problème a persisté après HOTFIX-01 ?

1. **Tests incomplets** : On a testé que le PDF se génère, mais pas que l'enrichissement fonctionne
2. **continue-on-error masque les erreurs** : Le workflow passait en vert malgré l'échec
3. **Mauvaise compréhension du comportement du plugin** : On pensait que `output_path: exports/` était relatif à la racine

### Améliorations process

1. ✅ **Tester le workflow complet en local** avant de push :
   ```bash
   mkdocs build --config-file mkdocs-pdf.yml
   python scripts/enrich_pdf_metadata.py site/exports/span-sg.pdf
   ```

2. ✅ **Retirer continue-on-error sauf cas justifié** : Fail-fast pour détecter régressions

3. ✅ **Documenter comportement des plugins** : Noter dans README que le PDF est généré dans `site/exports/`

---

## Mise à jour documentation

### README.md

Ajouter dans section "Commandes utiles" :

```markdown
# Build manuel du PDF avec enrichissement metadata
mkdocs build --config-file mkdocs-pdf.yml
python scripts/enrich_pdf_metadata.py site/exports/span-sg.pdf

# Note : Le PDF est généré dans site/exports/ (pas à la racine)
```

### roadmap/S2-02-export-pdf.md

Ajouter note dans section "Résultats obtenus" :

```markdown
### 🐛 Hotfixes appliqués
1. **HOTFIX-01** : Suppression `enabled_if_env` (génération bloquée)
2. **HOTFIX-02** : Correction chemin `site/exports/span-sg.pdf` (enrichissement bloqué)
```

---

## Références

- **HOTFIX-01** : roadmap/HOTFIX-01-pdf-generation-ci.md
- **CI Run problématique** : https://github.com/Alexmacapple/span-sg-repo/actions/runs/18166288931
- **Plugin docs** : https://pypi.org/project/mkdocs-with-pdf/

---

## Estimation temps

- **Analyse** : ✅ 2 min (logs CI)
- **Correction** : 1 min (changer 1 ligne)
- **Commit/push** : 1 min
- **Validation CI** : 3 min (attente workflow)
- **Total** : **7 minutes**

---

## Métrique de succès

✅ **Hotfix réussi si** :
- Step "Enrich PDF metadata" passe en vert
- PDF contient metadata (vérifiable avec `pdfinfo`)

📊 **KPI cumulé** : 2 hotfixes, 19 minutes total (< 30 min objectif MTTR)
