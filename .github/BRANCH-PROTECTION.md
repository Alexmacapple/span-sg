# Guide Branch Protection Rules - SPAN SG

Ce document explique la configuration des règles de protection de branche (Branch Protection Rules) pour garantir la qualité et la sécurité du code.

## Objectif

Protéger la branche `main` en imposant:
- Validation CI/CD obligatoire avant merge
- Code reviews obligatoires
- Prévention des force push et suppressions accidentelles
- Application stricte de CODEOWNERS

---

## Configuration requise

### Prérequis
- Droits admin sur le repository GitHub `Alexmacapple/span-sg`
- CODEOWNERS configuré (`.github/CODEOWNERS`)
- Workflow CI/CD fonctionnel (`.github/workflows/build.yml`)

### Accès configuration
```
Repository Settings → Branches → Add branch protection rule
```

URL directe: `https://github.com/Alexmacapple/span-sg/settings/branch_protection_rules/new`

---

## Règles recommandées pour `main`

### 1. Branch name pattern
```
main
```

### 2. Require a pull request before merging

**Activer:** `Require a pull request before merging`

**Sous-options:**
- `Require approvals`: **1 required** (au minimum)
- `Dismiss stale pull request approvals when new commits are pushed`: **Activé**
- `Require review from Code Owners`: **Activé** (impose reviews selon CODEOWNERS)

**Effet:**
- Interdit push direct sur `main` (force passage par PR)
- Nécessite validation d'au moins 1 reviewer
- Validation annulée si nouveau commit push après review

### 3. Require status checks to pass before merging

**Activer:** `Require status checks to pass before merging`

**Sous-options:**
- `Require branches to be up to date before merging`: **Activé**

**Status checks requis:**
- `build-and-test` (job principal du workflow build.yml)

**Effet:**
- CI doit passer (build, tests, linting, security checks)
- Branche PR doit être à jour avec `main` avant merge

### 4. Require conversation resolution before merging

**Activer:** `Require conversation resolution before merging`

**Effet:**
- Tous les commentaires de review doivent être résolus avant merge

### 5. Do not allow bypassing the above settings

**Activer:** `Do not allow bypassing the above settings`

**Effet:**
- Même les admins doivent respecter les règles (pas de bypass)
- Garantit application stricte des protections

### 6. Restrict who can push to matching branches

**Optionnel:** Laisser désactivé pour petit projet

**Si activé:**
- Limiter à: `@Alexmacapple`, `@bertrand`, `@alex`

### 7. Allow force pushes

**Désactiver:** `Allow force pushes` (laisser décoché)

**Effet:**
- Interdit `git push --force` sur `main`
- Prévient écrasement historique Git

### 8. Allow deletions

**Désactiver:** `Allow deletions` (laisser décoché)

**Effet:**
- Interdit suppression de la branche `main`

---

## Résumé configuration minimale

**Activé:**
- Require a pull request before merging (1 approval minimum)
- Require review from Code Owners
- Require status checks to pass: `build-and-test`
- Require conversation resolution before merging
- Do not allow bypassing the above settings

**Désactivé:**
- Allow force pushes
- Allow deletions

---

## Vérification configuration

### Tester les protections

1. **Tentative push direct sur main:**
```bash
git checkout main
echo "test" >> README.md
git commit -am "test: direct push"
git push origin main
```

**Attendu:** Erreur `remote: error: GH006: Protected branch update failed`

2. **Créer PR et tester workflow:**
```bash
git checkout -b test/branch-protection
echo "test" >> README.md
git commit -am "test: branch protection"
git push -u origin test/branch-protection
# Créer PR via GitHub UI
```

**Attendu:**
- Status check `build-and-test` apparaît automatiquement
- Merge bloqué tant que CI n'a pas passé
- Merge bloqué tant qu'aucune review approuvée

3. **Vérifier CODEOWNERS:**
```bash
# Modifier fichier sous CODEOWNERS
vim docs/modules/snum.md
git commit -am "test: codeowners"
git push
```

**Attendu:** PR nécessite review par `@Alexmacapple @bertrand @alex` (ownership `/docs/modules/`)

---

## Workflow PR recommandé

### Créateur de la PR
1. Créer branche feature: `git checkout -b feature/description`
2. Développer et tester localement
3. Push et créer PR vers `main`
4. Attendre CI (build-and-test)
5. Répondre aux commentaires de review
6. Résoudre toutes conversations

### Reviewer
1. Vérifier que CI a passé (statut vert)
2. Effectuer code review (commenter si nécessaire)
3. Si satisfait: "Approve" la PR
4. Si CODEOWNERS ownership: review obligatoire

### Merge
- Bouton "Merge" débloqué seulement si:
  - Au moins 1 approval
  - CI `build-and-test` passée
  - Toutes conversations résolues
  - Branche à jour avec `main`

---

## Exceptions et cas particuliers

### Hotfix urgent

**Si bug critique bloquant production:**

1. Créer PR hotfix: `hotfix/critical-bug`
2. Demander review express à owner (`@Alexmacapple`)
3. Une fois approuvé et CI passée: merge immédiat
4. Documenter dans CHANGELOG.md

**Important:** Même pour hotfix, respecter les protections (pas de bypass)

### Release tagging

**Créer tag après merge dans main:**
```bash
git checkout main
git pull origin main
git tag -a vX.Y.Z -m "Release vX.Y.Z: description"
git push origin vX.Y.Z
gh release create vX.Y.Z --title "..." --notes "..."
```

**Note:** Tags peuvent être créés sans PR (pas de branche protégée)

---

## Métriques et suivi

### Dashboard GitHub Insights

**Accès:** `https://github.com/Alexmacapple/span-sg/pulse`

**Métriques utiles:**
- Nombre PRs mergées / semaine
- Temps moyen review → merge
- Nombre conversations par PR

### Labels automatiques

Combiner avec labels `.github/LABELS.md`:
- `status:review-needed`: PR créée, attend review
- `priority:critical`: Hotfix urgent
- `area:ci-cd`: Modifications workflow (review @alex)

---

## Troubleshooting

### Erreur "Required status check is expected"

**Problème:** Status check `build-and-test` introuvable

**Solution:**
1. Vérifier nom exact job dans `.github/workflows/build.yml:10` (`build-and-test`)
2. Dans Settings → Branches → Edit rule, supprimer et re-ajouter status check
3. Créer nouvelle PR test pour valider

### Erreur "Review required by Code Owners"

**Problème:** Aucun CODEOWNER disponible pour review

**Solution:**
1. Temporairement désactiver "Require review from Code Owners"
2. Merger PR avec autre reviewer
3. Mettre à jour `.github/CODEOWNERS` avec reviewers actifs
4. Ré-activer protection

### CI bloquée par pre-commit hooks

**Problème:** PR échoue sur pre-commit mais passe localement

**Solution:**
```bash
# Forcer exécution locale
pre-commit run --all-files

# Si nécessaire: mettre à jour versions hooks
pre-commit autoupdate

# Commit corrections
git add .pre-commit-config.yaml
git commit -m "chore: update pre-commit hooks"
```

---

## Évolution future

### Protections avancées (optionnelles)

**Si projet grandit:**
- `Require deployments to succeed before merging` (environnement staging)
- `Require signed commits` (GPG signing obligatoire)
- `Restrict who can dismiss pull request reviews` (limite admin uniquement)

**Protections additionnelles branches:**
- Protéger `gh-pages` (déploiements)
- Protéger tags `v*.*.*` (releases stables)

---

## Références

- GitHub Docs: [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- CODEOWNERS: `.github/CODEOWNERS`
- Workflow CI/CD: `.github/workflows/build.yml`
- Labels: `.github/LABELS.md`
