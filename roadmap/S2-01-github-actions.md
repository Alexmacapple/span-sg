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
- Génération PDF automatique
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
5. ✅ Generate PDF
6. ✅ Upload artifacts
7. ✅ deploy_draft (si branche=draft)

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
- Si PDF vide ou erreur → Consulter logs step "Generate PDF"

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
Par défaut, si la génération PDF échoue, le workflow continue (artefact `exports/` sera vide). Pour rendre l'échec PDF bloquant et stopper le workflow :
```yaml
- name: Generate PDF
  run: mkdocs build --config-file mkdocs-pdf.yml
  # Sans continue-on-error, l'échec bloque le workflow
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

---

## Résultats validation (01/10/2025)

### Environnement
- Système CI : GitHub Actions (ubuntu-latest)
- Python : 3.11.13
- Runner Image : ubuntu-24.04
- Branche : draft

### Workflows exécutés

**Run 1** (`3efb09a`) - ❌ Échec 7s
- Erreur : `actions/upload-artifact@v3` deprecated
- Correction : Upgrade vers `@v4`

**Run 2** (`a30cb64`) - ✅ Succès 44s
- Build + scoring OK
- Déploiement incorrect (pas de `draft/`)
- Cause : Manque `download-artifact` dans jobs deploy

**Run 3** (`d614e64`) - ✅ Succès 53s
- Ajout `download-artifact@v4` dans `deploy_draft` et `deploy_main`
- Déploiement correct vers `gh-pages/draft/`
- ✅ **Premier workflow complet réussi**

### Corrections appliquées

**1. Upgrade artifact action**
```yaml
# AVANT
uses: actions/upload-artifact@v3

# APRÈS
uses: actions/upload-artifact@v4
```

**2. Ajout download-artifact dans jobs deploy**
```yaml
deploy_draft:
  steps:
    - uses: actions/checkout@v3

    # AJOUT
    - name: Download artifacts
      uses: actions/download-artifact@v4
      with:
        name: span-site

    - name: Deploy...
      uses: peaceiris/actions-gh-pages@v3
      with:
        publish_dir: ./site  # Maintenant présent
```

### Validation GitHub Pages

**Repo visibility** : Public (requis pour Pages gratuit)

**Activation** :
```bash
curl -X POST https://api.github.com/repos/Alexmacapple/span-sg-repo/pages \
  -d '{"source":{"branch":"gh-pages","path":"/"}}'
```

**URLs actives** :
- ✅ Draft : https://alexmacapple.github.io/span-sg-repo/draft/ (HTTP 200)
- ✅ Production : https://alexmacapple.github.io/span-sg-repo/ (racine)
- ✅ PDF : https://alexmacapple.github.io/span-sg-repo/draft/exports/span-sg.pdf (48 KB)

### Test erreur périmètre

**Commit test** (`822f5fd`) : SIRCOM 30 points (au lieu de 31)

**Résultat** : ❌ Échec 23s
```
Erreurs de périmètre:
 - sircom.md: 30 points tagués <!-- DINUM --> (attendu 31 ou 0)
##[error]Process completed with exit code 2.
```

**Revert** (`2b0f5b2`) : ✅ Succès 49s

✅ **Validation périmètre fonctionnelle**

### Optimisations

**Cache pip** :
```yaml
- name: Setup Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'
    cache: 'pip'  # AJOUT
```

**Badge CI** dans README.md :
```markdown
![Build Status](https://github.com/Alexmacapple/span-sg-repo/workflows/Build%20SPAN/badge.svg)
```

### Performance

**Durée totale** : ~50 secondes
- Install dependencies : ~15s (avec cache pip)
- Calculate scores : ~1s
- Build site : ~5s
- Generate PDF : ~20s
- Upload artifacts : ~3s
- Deploy draft : ~6s

**Total attendu future runs** : ~20-30s (cache pip actif)

### Artefacts générés

**Artefact `span-site`** :
- Taille : 682 KB
- Contenu : `site/` + `exports/span-sg.pdf`
- Rétention : 90 jours
- Téléchargeable : https://github.com/Alexmacapple/span-sg-repo/actions

**Déploiement gh-pages** :
```
draft/
├── index.html
├── modules/
│   ├── sircom/
│   ├── snum/
│   └── ...
├── synthese/
├── exports/
│   └── span-sg.pdf (48 KB)
└── assets/
```

### Critères d'acceptation (10/10 validés)

- [x] Workflow `.github/workflows/build.yml` existe et valide
- [x] GitHub Actions activé sur le repo
- [x] Permissions `GITHUB_TOKEN` = Read and write
- [x] Premier run sur `draft` réussit sans erreur
- [x] Job `build` termine en < 5 minutes (53s)
- [x] Artefacts `span-site` contient `site/` + `exports/span-sg.pdf`
- [x] PDF généré et lisible (48 KB)
- [x] Job `deploy_draft` déploie vers `gh-pages/draft/`
- [x] Test erreur scoring bloque bien le build (exit 2)
- [x] Logs clairs et exploitables

### Tests de validation (5/5 validés)

| Test | Résultat |
|------|----------|
| 1. Workflow YAML valide | ✅ OK |
| 2. Triggers branches [main, draft] | ✅ OK |
| 3. Script scoring présent | ✅ OK |
| 4. Déploiement conditionnel draft | ✅ OK |
| 5. Branche gh-pages créée | ✅ OK |

### Notes

**Repo public** : Nécessaire pour GitHub Pages gratuit (repos privés = GitHub Pro $4/mois)

**Force orphan** : Chaque deploy écrase complètement gh-pages (pas d'historique pollué)

**Quota CI** : Repos publics = illimité (repos privés = 2000 min/mois)