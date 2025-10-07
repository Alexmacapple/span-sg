---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S1-01 : Création du dépôt GitHub privé

**Phase** : Semaine 1 - Setup
**Priorité** : Critique
**Estimation** : 1h
**Assigné** : Alexandra

---

## Contexte projet

Le projet SPAN SG (Schéma Pluriannuel d'Accessibilité Numérique du Secrétariat Général) vise à créer un framework simple et modulaire permettant :
- Édition décentralisée par service (6 modules v1 : SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- Agrégation automatique SG
- Versioning Git
- Export HTML/PDF via MkDocs
- Scoring automatique sur 31 points checklist DINUM

Architecture technique :
- MkDocs Material (mode strict)
- GitHub Actions pour CI/CD
- GitHub Pages (org-only) pour preview/production
- Python pour scoring automatique

Cette story constitue la **première étape fondamentale** : créer le repository GitHub qui hébergera tout le code, la documentation, et servira de base pour la CI/CD et le déploiement.

---

## Objectif

Créer et configurer le dépôt GitHub privé `span-sg-repo` dans le compte `Alexmacapple` (ou organisation si disponible) avec :
- Visibilité privée
- Branches `main` et `draft` configurées
- Remote configuré localement
- Premier commit avec structure complète
- Protection de branche activée

---

## Prérequis

- [ ] Compte GitHub actif (Alexmacapple)
- [ ] Archive repo complète `span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts.zip` dézippée localement
- [ ] Git installé en local
- [ ] Accès terminal/ligne de commande

---

## Étapes d'implémentation

### Option automatique (recommandée) : Script init-repo.sh

**Si GitHub CLI (`gh`) installé** :
```bash
./scripts/init-repo.sh span-sg-repo Alexmacapple
```

Le script automatise toutes les étapes ci-dessous. Passer à la section "Critères d'acceptation" si succès.

---

### Option manuelle (si script échoue)

### 1. Créer le dépôt sur GitHub.com

1. Aller sur https://github.com/new
2. Paramètres :
   - **Repository name** : `span-sg-repo`
   - **Description** : `SPAN SG - Schéma Pluriannuel d'Accessibilité Numérique du Secrétariat Général`
   - **Visibility** : Private
   - **Initialize** : Ne pas cocher README, .gitignore, ni license (on a déjà les fichiers)
3. Cliquer **Create repository**

### 2. Initialiser Git localement

Dans le répertoire local du projet :

```bash
cd /chemin/vers/span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts

# Initialiser Git
git init

# Configurer l'identité
git config user.name "Alexmacapple"
git config user.email "alexandra.guiderdoni@gmail.com"
```

### 3. Créer le commit initial

```bash
# Ajouter tous les fichiers
git add .

# Commit initial
git commit -m "chore: import repo v3.3 GO-ready + enrichissements + agents + prompts"
```

### 4. Connecter au remote et push

```bash
# Renommer branche en main
git branch -M main

# Ajouter remote origin
git remote add origin https://github.com/Alexmacapple/span-sg-repo.git

# Push vers main avec tracking
git push -u origin main
```

### 5. Créer branche draft

```bash
# Créer et checkout draft depuis main
git checkout -b draft

# Push draft avec tracking
git push -u origin draft
```

### 6. Configurer protection de branche (optionnel mais recommandé)

Sur GitHub.com :
1. Aller dans **Settings** → **Branches**
2. **Add branch protection rule** pour `main` :
   - Branch name pattern : `main`
   - ☑ Require a pull request before merging
   - ☑ Require approvals (1 minimum)
   - Assigné : Bertrand ou Alex
3. Sauvegarder

---

## Critères d'acceptation

- [ ] Dépôt `Alexmacapple/span-sg-repo` créé et privé
- [ ] Branche `main` existe avec 25 fichiers committés
- [ ] Branche `draft` existe et track origin/draft
- [ ] Remote `origin` configuré localement
- [ ] Commit initial contient : PRD, README, CLAUDE.md, Agents.md, GO-CHECKLIST, CI workflow, scripts, docs/, mkdocs configs
- [ ] `git status` local indique "nothing to commit, working tree clean"
- [ ] `git remote -v` affiche l'URL correcte

---

## Tests de validation

```bash
# Vérifier branches
git branch -a
# Attendu : main, draft, remotes/origin/main, remotes/origin/draft

# Vérifier remote
git remote -v
# Attendu : origin https://github.com/Alexmacapple/span-sg-repo.git

# Vérifier historique
git log --oneline --graph --all
# Attendu : 1 commit "chore: import repo v3.3..."

# Vérifier fichiers committés
git ls-tree -r HEAD --name-only | wc -l
# Attendu : 25 fichiers
```

---

## Dépendances

**Bloque** :
- S1-02 (Docker local nécessite le repo)
- S1-03 (MkDocs strict nécessite le repo)
- Toutes les autres stories

**Dépend de** : Aucune (première tâche)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 1 Setup
- **PRD v3.3** : Section 4 "Workflow Git simplifié" → Branches main/draft
- **README.md** : Section "Checklist première release v0.1"
- **Fichiers concernés** : Tous les fichiers du repo

---

## Notes et risques

**Risques** :
- Si organisation GitHub disponible, préférer créer le repo dans l'organisation pour activer preview org-only
- Si repo public par erreur, passer immédiatement en Private dans Settings

**Messages d'erreur courants** :

1. **`fatal: remote origin already exists`**
   ```bash
   # Solution: Supprimer remote existant
   git remote remove origin
   git remote add origin https://github.com/Alexmacapple/span-sg-repo.git
   ```

2. **`error: failed to push some refs`**
   - Cause: Branche distante a des commits que vous n'avez pas localement
   - Solution: `git pull origin main --rebase` puis `git push`

3. **`Repository creation failed: name already exists`**
   - Cause: Un repo avec ce nom existe déjà
   - Solution: Choisir autre nom OU supprimer ancien repo sur GitHub

4. **`fatal: Authentication failed`**
   - Cause: Token GitHub expiré ou credentials invalides
   - Solution avec gh CLI: `gh auth refresh`
   - Solution avec HTTPS: Régénérer Personal Access Token

5. **`error: src refspec main does not match any`**
   - Cause: Aucun commit n'a été créé
   - Solution: Vérifier `git log` montre au moins 1 commit

6. **`HTTP 403: Upgrade to GitHub Pro or make this repository public to enable this feature`**
   - Cause: Protection de branche requiert GitHub Pro pour dépôts privés personnels
   - Solution Option A: Migrer repo vers une organisation GitHub (protection gratuite)
   - Solution Option B: Workflow manuel strict (toujours créer PR, validation humaine avant merge)
   - Solution Option C: Upgrade GitHub Pro (4$/mois)

**Post-tâche** :
- Informer Bertrand et Alex de la création du repo
- Leur donner accès (Settings → Collaborators)
- **Limitation identifiée** : Protection branche `main` non disponible (GitHub Free + repo privé personnel). Workflow PR manuel obligatoire : `feature/*` → `draft` → `main` avec validation humaine systématique
- Noter l'URL exacte pour la suite