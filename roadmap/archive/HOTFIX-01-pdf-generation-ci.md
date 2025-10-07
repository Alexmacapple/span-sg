---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: hotfix
autonomous: true
validation: ci-test
priority: critique
---

# HOTFIX-01 : Génération PDF bloquée en CI

**Phase** : Hotfix immédiat
**Priorité** : ⚠️ CRITIQUE
**Estimation** : 5 min
**Assigné** : Alexandra
**Détection** : CI run #40 (eb18e4a)

---

## Problème détecté

### Symptôme
❌ **Artefact `span-site.zip` ne contient pas `exports/span-sg.pdf`**

Workflow CI : https://github.com/Alexmacapple/span-sg-repo/actions/runs/18165934202

### Logs CI (étapes concernées)

#### Step "Generate PDF"
```
WARNING - without generate PDF(set environment variable ENABLE_PDF_EXPORT to 1 to enable)
INFO    - Cleaning site directory
INFO    - Building documentation to directory: /home/runner/work/span-sg-repo/span-sg-repo/site
INFO    - Documentation built in 0.29 seconds
```

**Analyse** : Le plugin `mkdocs-with-pdf` **refuse de générer le PDF** car `ENABLE_PDF_EXPORT` n'est pas définie.

#### Step "Enrich PDF metadata"
```
❌ Fichier introuvable: exports/span-sg.pdf
Error: Process completed with exit code 1.
```

**Analyse** : Conséquence du problème précédent. Le `continue-on-error: true` empêche le blocage complet.

---

## Cause racine

**Fichier** : `mkdocs-pdf.yml` ligne 19
```yaml
enabled_if_env: ENABLE_PDF_EXPORT
```

Cette directive dit au plugin : "Ne génère le PDF **que si** la variable d'environnement `ENABLE_PDF_EXPORT=1`"

**Contexte historique** : Cette ligne a été copiée depuis la documentation du plugin, mais :
- ❌ Variable jamais définie dans le workflow `.github/workflows/build.yml`
- ❌ Pas testé en local avant commit (nécessite `export ENABLE_PDF_EXPORT=1`)
- ✅ Workflow passe en vert (car `continue-on-error: true` sur enrichissement)
- ❌ **Mais aucun PDF généré**

---

## Impact

### Immédiat
- ❌ Pas de PDF dans les artefacts CI
- ❌ Pas de PDF déployé sur GitHub Pages `/draft/exports/span-sg.pdf`
- ❌ Story S2-02 (Export PDF) **partiellement bloquée**

### Bloquant pour
- ✋ S4-04 (Publication) : nécessite PDF pour la release
- ✋ Validation visuelle du PDF (tableaux, checkboxes, TOC)
- ✋ Tests d'accessibilité PDF (S5-01)

---

## Solutions envisagées

### Option A : Supprimer `enabled_if_env` ✅ **RECOMMANDÉ**

**Modification** : `mkdocs-pdf.yml` ligne 19
```yaml
# AVANT
      enabled_if_env: ENABLE_PDF_EXPORT
      verbose: false

# APRÈS
      verbose: false
```

**Avantages** :
- ✅ Simple (1 ligne à supprimer)
- ✅ PDF généré systématiquement en CI
- ✅ Reproductible en local (`mkdocs build --config-file mkdocs-pdf.yml`)
- ✅ Pas de dépendance à une variable d'environnement

**Inconvénients** :
- ⚠️ PDF généré même si on ne le veut pas (mais pas de cas d'usage identifié)

---

### Option B : Définir `ENABLE_PDF_EXPORT=1` dans le workflow

**Modification** : `.github/workflows/build.yml` ligne 30
```yaml
# AVANT
      - name: Generate PDF
        run: mkdocs build --config-file mkdocs-pdf.yml

# APRÈS
      - name: Generate PDF
        env:
          ENABLE_PDF_EXPORT: 1
        run: mkdocs build --config-file mkdocs-pdf.yml
```

**Avantages** :
- ✅ Contrôle fin (PDF uniquement en CI, pas en local)
- ✅ Garde la sémantique originale du plugin

**Inconvénients** :
- ❌ Plus complexe (2 fichiers à coordonner)
- ❌ Tests locaux nécessitent `export ENABLE_PDF_EXPORT=1` (friction développeur)
- ❌ Risque d'oubli lors de futures modifications

---

### Option C : Les deux (hybride)

Supprimer `enabled_if_env` **ET** documenter comment désactiver en local si besoin.

**Pas de valeur ajoutée identifiée pour ce projet.**

---

## Décision : Option A

**Justification** :
1. **Simplicité** : MVP privilégie solutions simples
2. **Pas de cas d'usage pour désactivation** : Le PDF est un livrable attendu à chaque build
3. **Reproductibilité** : Tests locaux identiques à la CI
4. **Moindre risque** : 1 seul fichier modifié

**Validation** : PRD Semaine 2 indique "Export PDF automatique" → génération systématique attendue.

---

## Plan d'action (BMAD)

### Étape 1 : Corriger `mkdocs-pdf.yml`

**Action** : Supprimer ligne 19 `enabled_if_env: ENABLE_PDF_EXPORT`

**Fichier modifié** :
```yaml
plugins:
  - with-pdf:
      author: Secrétariat Général
      copyright: © 2025 Secrétariat Général
      cover_title: SPAN SG
      cover_subtitle: Schéma Pluriannuel d'Accessibilité Numérique 2025-2027
      toc_title: Table des matières
      toc_level: 3
      ordered_chapter_level: 3
      output_path: exports/span-sg.pdf
      verbose: false
```

### Étape 2 : Tester en local (optionnel mais recommandé)

```bash
# Générer PDF localement
mkdocs build --config-file mkdocs-pdf.yml

# Vérifier existence
ls -lh exports/span-sg.pdf
# Attendu : Fichier PDF présent

# Vérifier contenu (optionnel)
open exports/span-sg.pdf
```

### Étape 3 : Commiter et pousser

```bash
git add mkdocs-pdf.yml
git commit -m "fix(pdf): suppression enabled_if_env pour génération systématique

- Supprime condition ENABLE_PDF_EXPORT dans mkdocs-pdf.yml
- PDF généré automatiquement à chaque build CI
- Corrige erreur 'Fichier introuvable' sur enrichissement metadata
- Fixes #40 (artefact sans PDF)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin draft
```

### Étape 4 : Valider en CI

1. Attendre fin du workflow GitHub Actions
2. Vérifier logs step "Generate PDF" :
   - ✅ **Pas de WARNING "without generate PDF"**
   - ✅ Message "PDF generated: exports/span-sg.pdf"
3. Télécharger artefact `span-site.zip`
4. Vérifier présence de `exports/span-sg.pdf`
5. Ouvrir PDF et valider visuellement

### Étape 5 : Mettre à jour roadmap S2-02

Ajouter note dans section "Résultats obtenus" :

```markdown
### 🐛 Hotfix appliqué (HOTFIX-01)
- **Problème** : `enabled_if_env: ENABLE_PDF_EXPORT` bloquait génération PDF en CI
- **Solution** : Suppression de la directive pour génération systématique
- **Commit** : [hash] fix(pdf): suppression enabled_if_env
```

---

## Critères d'acceptation

- [ ] Ligne `enabled_if_env: ENABLE_PDF_EXPORT` supprimée de `mkdocs-pdf.yml`
- [ ] Commit poussé sur `draft`
- [ ] CI passe en vert (workflow "Build SPAN")
- [ ] Step "Generate PDF" affiche succès (pas de WARNING)
- [ ] Step "Enrich PDF metadata" affiche succès (metadata enrichies)
- [ ] Artefact `span-site.zip` contient `exports/span-sg.pdf` (taille > 100 KB)
- [ ] PDF téléchargeable et lisible (page de garde, TOC, modules)

---

## Tests de validation

```bash
# Test 1 : Ligne supprimée
! grep -q "enabled_if_env" mkdocs-pdf.yml && echo "✅ OK" || echo "❌ FAIL"
# Attendu : ✅ OK

# Test 2 : Génération locale fonctionne
mkdocs build --config-file mkdocs-pdf.yml && test -f exports/span-sg.pdf && echo "✅ OK" || echo "❌ FAIL"
# Attendu : ✅ OK

# Test 3 : Taille PDF raisonnable
test $(du -k exports/span-sg.pdf | cut -f1) -gt 100 && echo "✅ OK" || echo "❌ FAIL"
# Attendu : ✅ OK (> 100 KB)
```

---

## Rollback (si nécessaire)

Si la suppression cause des problèmes inattendus :

```bash
# Restaurer ligne originale
git revert [hash-du-commit]
git push origin draft

# Puis appliquer Option B (définir variable dans CI)
```

**Probabilité de rollback** : < 5% (correction simple et bien délimitée)

---

## Communication

**Notification** : Aucune (hotfix technique transparent pour utilisateurs)

**Documentation** :
- ✅ Commit message explicite
- ✅ Note dans roadmap S2-02
- ✅ Ce fichier PRD hotfix (traçabilité)

---

## Post-mortem

### Leçons apprises

1. **Toujours tester en local avant push** : La ligne `enabled_if_env` n'a jamais été testée
2. **Lire la doc plugin attentivement** : `enabled_if_env` est une feature avancée, pas un défaut obligatoire
3. **Vérifier contenu des artefacts** : Le workflow passait en vert malgré PDF manquant

### Améliorations process

1. ✅ Ajouter test automatique : `test -f exports/span-sg.pdf` dans CI (après génération)
2. ✅ Documenter dans README : comment tester génération PDF en local
3. ✅ Créer checklist validation PR : "Artefacts testés en local"

### Actions futures

- [ ] Ajouter step CI de vérification existence PDF (après "Generate PDF")
- [ ] Documenter dans CONTRIBUTING.md : checklist tests avant push
- [ ] Envisager pre-commit hook : `mkdocs build --config-file mkdocs-pdf.yml --strict`

---

## Références

- **Issue** : Aucune (détecté en interne via CI logs)
- **CI Run** : https://github.com/Alexmacapple/span-sg-repo/actions/runs/18165934202
- **Commit problématique** : eb18e4a (feat(pdf): requirements.txt...)
- **Plugin docs** : https://pypi.org/project/mkdocs-with-pdf/
- **S2-02** : roadmap/S2-02-export-pdf.md

---

## Estimation temps

- **Analyse** : ✅ 5 min (logs CI)
- **Correction** : 1 min (supprimer 1 ligne)
- **Test local** : 2 min (générer + vérifier PDF)
- **Commit/push** : 1 min
- **Validation CI** : 3 min (attente workflow)
- **Total** : **12 minutes**

---

## Métrique de succès

✅ **Hotfix réussi si** : Prochain CI run génère `exports/span-sg.pdf` dans artefact

📊 **KPI** : Temps entre détection et correction < 30 min (objectif MTTR)
