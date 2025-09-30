---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S2-01 : Configuration GitHub Actions CI/CD

**Phase** : Semaine 2 - Automatisation
**Priorité** : Critique
**Estimation** : 2h
**Assigné** : Alexandra

---

## Contexte projet

La CI/CD GitHub Actions est le **cœur de l'automatisation** SPAN SG. Elle garantit :
- Build automatique à chaque push (main, draft)
- Validation scoring (exit 2 si erreur périmètre)
- Génération PDF avec fallback robuste
- Déploiement conditionnel vers GitHub Pages
- Artefacts disponibles pour releases

Le workflow `.github/workflows/build.yml` comprend 3 jobs :
1. **build** : Install deps → Scoring → Build site → PDF → Upload artifacts
2. **deploy_draft** : Si branche=draft → Deploy vers `gh-pages/draft/`
3. **deploy_main** : Si branche=main → Deploy vers `gh-pages/` (racine)

Ordre d'exécution critique :
- Scoring **AVANT** build (si scoring échoue, pas de build)
- Build **AVANT** PDF (PDF dépend du site généré)
- Upload artifacts **APRÈS** PDF
- Deploy **APRÈS** build réussi

---

## Objectif

Valider et ajuster le workflow GitHub Actions existant, tester l'exécution sur draft, vérifier la génération d'artefacts, et garantir que la CI est opérationnelle.

---

## Prérequis

- [ ] Story S1-01 complétée (repo avec branches main/draft)
- [ ] Story S1-05 complétée (script scoring fonctionnel)
- [ ] Accès GitHub Actions activé sur le repo
- [ ] Permissions `GITHUB_TOKEN` configurées

---

## Étapes d'implémentation

### 1. Vérifier le workflow existant

```bash
cat .github/workflows/build.yml
```

Points clés à valider :
- Triggers : `push: branches: [main, draft]` + `pull_request: branches: [main]`
- Job `build` : Python 3.11, install deps, scoring, build, PDF
- Job `deploy_draft` : condition `if: github.ref == 'refs/heads/draft'`
- Job `deploy_main` : condition `if: github.ref == 'refs/heads/main'`
- Action `peaceiris/actions-gh-pages@v3` pour déploiement

### 2. Vérifier les permissions GitHub Token

Le workflow utilise `${{ secrets.GITHUB_TOKEN }}`. Vérifier permissions :

Sur GitHub → Settings → Actions → General → Workflow permissions :
- ☑ Read and write permissions (obligatoire pour gh-pages)
- ☑ Allow GitHub Actions to create and approve pull requests (optionnel)

### 3. Activer GitHub Actions

Sur GitHub → Actions :
- Si message "Workflows aren't being run on this repository" → Cliquer **I understand, enable them**

### 4. Déclencher un premier build sur draft

```bash
# Depuis la branche draft locale
git checkout draft

# Créer un commit trigger
echo "" >> README.md
git add README.md
git commit -m "ci: trigger initial workflow"
git push origin draft
```

### 5. Suivre l'exécution du workflow

Sur GitHub → Actions → Workflow "Build SPAN" :

Observer les étapes :
1. ✅ Setup Python
2. ✅ Install dependencies (pip install mkdocs-material...)
3. ✅ Calculate SPAN scores
4. ✅ Build site (mkdocs build)
5. ✅ Generate PDF (principal)
6. ⚠️ Generate PDF fallback (si échec step 5)
7. ✅ Upload artifacts
8. ✅ deploy_draft (si branche=draft)

### 6. Vérifier les artefacts

Une fois le workflow terminé :

Cliquer sur le run → Section "Artifacts" → Télécharger `span-site`

Vérifier contenu du zip :
```
span-site/
├── site/
│   ├── index.html
│   ├── modules/
│   ├── assets/
│   └── ...
└── exports/
    └── span-sg.pdf
```

### 7. Tester le PDF généré

Extraire et ouvrir `exports/span-sg.pdf` :
- Vérifier contenu : Accueil, Synthèse, 6 modules
- Vérifier formatage (theme Material, tableaux)
- Vérifier table des matières
- Si PDF vide ou erreur → Vérifier step "Generate PDF fallback" a fonctionné

### 8. Vérifier le déploiement draft

Si job `deploy_draft` a réussi, vérifier branche gh-pages :

```bash
git fetch origin
git checkout gh-pages
ls -la draft/
# Attendu : index.html, modules/, etc.
```

**Note** : GitHub Pages doit être activé manuellement (voir S2-03).

### 9. Tester l'échec du scoring

Créer volontairement une erreur de périmètre pour tester l'arrêt CI :

```bash
# Sur draft
# Modifier SIRCOM pour avoir 30 points (supprimer 1 ligne DINUM)
sed -i '' '0,/<!-- DINUM -->/d' docs/modules/sircom.md

git add docs/modules/sircom.md
git commit -m "test: erreur périmètre volontaire"
git push origin draft
```

Observer workflow :
- ❌ Step "Calculate SPAN scores" doit échouer (exit 2)
- ❌ Build et déploiement ne doivent PAS s'exécuter

Puis corriger :
```bash
git revert HEAD
git push origin draft
```

### 10. Optimiser le workflow (optionnel)

Améliora possibles :
- Cacher pip dependencies : `actions/cache@v3`
- Paralléliser jobs : `deploy_draft` et `deploy_main` ne dépendent pas l'un de l'autre
- Ajouter badge status : `![Build](https://github.com/.../workflows/Build%20SPAN/badge.svg)`

---

## Critères d'acceptation

- [ ] Workflow `.github/workflows/build.yml` existe et valide
- [ ] GitHub Actions activé sur le repo
- [ ] Permissions `GITHUB_TOKEN` = Read and write
- [ ] Premier run sur `draft` réussit sans erreur
- [ ] Job `build` termine en < 5 minutes
- [ ] Artefacts `span-site` contient `site/` + `exports/span-sg.pdf`
- [ ] PDF généré et lisible
- [ ] Job `deploy_draft` déploie vers `gh-pages/draft/`
- [ ] Test erreur scoring bloque bien le build
- [ ] Logs clairs et exploitables

---

## Tests de validation

```bash
# Test 1 : Workflow existe et valide YAML
python -c "import yaml; yaml.safe_load(open('.github/workflows/build.yml')); print('OK')"
# Attendu : OK

# Test 2 : Trigger branches correct
grep -q "branches: \[main, draft\]" .github/workflows/build.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : Script scoring présent dans CI
grep -q "python scripts/calculate_scores.py" .github/workflows/build.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : Déploiement conditionnel draft
grep -q "if: github.ref == 'refs/heads/draft'" .github/workflows/build.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 5 : Vérifier branche gh-pages créée (après premier deploy)
git ls-remote --heads origin gh-pages && echo "OK" || echo "WARN: gh-pages pas encore créée"
# Attendu : OK (après premier run)
```

---

## Dépendances

**Bloque** :
- S2-03 (preview privée dépend de la CI)
- S4-04 (publication production utilise la CI)

**Dépend de** :
- S1-01 (repo doit exister avec branches)
- S1-05 (script scoring doit fonctionner)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 2 Automatisation
- **PRD v3.3** : Annexe C ".github/workflows/build.yml"
- **.github/workflows/build.yml** : Workflow à configurer
- **CLAUDE.md** : Section "CI/CD GitHub Actions"

---

## Notes et risques

**Échec PDF non bloquant**
Le step "Generate PDF (plugin principal)" utilise `continue-on-error: true`. Cela permet au fallback de s'exécuter même si le plugin principal échoue.

Si le fallback échoue aussi, le workflow continue (artefact `exports/` sera vide). Pour rendre l'échec PDF bloquant :
```yaml
- name: Generate PDF fallback
  if: failure()
  run: mkdocs build --config-file mkdocs-with-pdf.yml
  # Retirer continue-on-error pour bloquer
```

**Temps d'exécution**
- Install dependencies : ~60s (pip install)
- Calculate scores : ~1s
- Build site : ~5s
- Generate PDF : ~20s
- Deploy : ~10s

**Total attendu : 2-3 minutes**

Si > 10 min → Vérifier cache pip ou images lourdes dans docs/assets/.

**Quotas GitHub Actions**
- Repo privé : 2000 min/mois (plan Free)
- Repo public : illimité

Avec 2-3 min par run, budget ~600 runs/mois.

**Artifacts retention**
Par défaut : 90 jours. Configurable dans Settings → Actions → General.

**Déploiement force_orphan**
Le paramètre `force_orphan: true` écrase complètement la branche gh-pages à chaque deploy. Cela garantit pas d'historique pollué mais supprime les deploys précédents.

---

## Post-tâche

Ajouter badge CI dans README.md :
```markdown
# SPAN SG

![Build Status](https://github.com/Alexmacapple/span-sg-repo/workflows/Build%20SPAN/badge.svg)

Ce dépôt contient le SPAN SG...
```

Documenter le workflow :
```markdown
## CI/CD

Le workflow GitHub Actions s'exécute automatiquement :
- Push sur `main` ou `draft` → Build + Deploy
- Pull request vers `main` → Build only (pas de deploy)

Artefacts disponibles pendant 90 jours dans Actions → Artifacts.
```