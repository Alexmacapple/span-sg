# Guide BFG Repo-Cleaner : Purge Git History

**Contexte** : Purge du dossier `inspiration/` de l'historique Git pour supprimer fichiers sensibles.

**Date exécution** : À planifier (après validation backup)

---

## Prérequis

### 1. Backup Complet

```bash
# Backup local
cd /Users/alex/Desktop
cp -r span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts \
     span-sg-repo-BACKUP-$(date +%Y%m%d-%H%M%S)

# Vérifier backup
ls -lh span-sg-repo-BACKUP-*

# Alternative : clone GitHub
gh repo clone Alexmacapple/span-sg-repo /tmp/span-sg-backup-$(date +%Y%m%d)
```

### 2. Installation BFG

```bash
# macOS via Homebrew
brew install bfg

# OU téléchargement JAR
curl -L https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar -o /tmp/bfg.jar
alias bfg='java -jar /tmp/bfg.jar'

# Vérifier installation
bfg --version
# Attendu: bfg 1.14.0
```

---

## Procédure de Purge

### Étape 1 : Clone Bare Repository

```bash
cd /tmp
git clone --mirror https://github.com/Alexmacapple/span-sg-repo.git span-sg-bfg
cd span-sg-bfg
```

**Note** : `--mirror` clone toutes refs (branches, tags, historique complet).

### Étape 2 : Exécuter BFG

```bash
# Supprimer dossier inspiration/ de tout l'historique
bfg --delete-folders inspiration

# Output attendu :
# Using repo : /tmp/span-sg-bfg
# Found X commits
# Found Y trees
# Removing inspiration/ from all commits...
# BFG run completed
```

### Étape 3 : Vérifier Purge

```bash
# Vérifier que inspiration/ n'apparaît plus dans l'historique
git log --all --oneline --graph -- inspiration/

# Attendu : Aucun résultat

# Vérifier taille repo
du -sh .
# Doit être plus petit qu'avant
```

### Étape 4 : Nettoyage Git

```bash
# Expirer reflog (supprimer références anciennes)
git reflog expire --expire=now --all

# Garbage collection (supprimer objets orphelins)
git gc --prune=now --aggressive

# Vérifier réduction taille
du -sh .
```

### Étape 5 : Force Push

```bash
# Push vers GitHub (ATTENTION : irréversible)
git push --force

# Output attendu :
# + refs/heads/draft:refs/heads/draft (forced update)
# + refs/heads/main:refs/heads/main (forced update)
```

### Étape 6 : Re-clone Local

```bash
# Supprimer repo local (ancien historique)
cd /Users/alex/Desktop
rm -rf span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts

# Re-cloner depuis GitHub (historique nettoyé)
git clone https://github.com/Alexmacapple/span-sg-repo.git span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts
cd span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts

# Vérifier absence inspiration/ dans historique
git log --all --oneline -- inspiration/
# Attendu : Aucun résultat
```

---

## Vérifications Post-Purge

### 1. Historique Git

```bash
# Rechercher inspiration/ dans tous commits
git log --all --full-history -- inspiration/
# Attendu : Aucun commit

# Vérifier taille repo
du -sh .git
# Doit être significativement réduit
```

### 2. GitHub Web

1. Aller sur https://github.com/Alexmacapple/span-sg-repo
2. Utiliser recherche GitHub : `inspiration/ in:file`
3. Attendu : Aucun résultat

### 3. CI/CD

```bash
# Vérifier que CI passe après force push
gh run list --limit 3

# Si CI échoue, vérifier logs
gh run view <run-id> --log-failed
```

---

## Résolution Problèmes

### Erreur : "Cannot push non-fastforward"

```bash
# Si force push bloqué par protection branches
# 1. Désactiver temporairement protection (GitHub Settings → Branches)
# 2. Re-tenter force push
# 3. Réactiver protection
```

### Erreur : "BFG not found"

```bash
# Vérifier installation
which bfg
# Si vide, réinstaller via brew

brew install bfg
```

### Repo local désynchronisé

```bash
# Supprimer et re-cloner
cd /Users/alex/Desktop
rm -rf span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts
git clone https://github.com/Alexmacapple/span-sg-repo.git span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts
```

---

## Alternatives à BFG

### git filter-repo (plus récent)

```bash
# Installation
brew install git-filter-repo

# Purge inspiration/
git filter-repo --path inspiration/ --invert-paths

# Force push
git push --force --all
```

### git filter-branch (legacy, lent)

```bash
# Non recommandé (deprecated), utiliser BFG ou git-filter-repo
```

---

## Sécurité

### ⚠️ Avertissements

- **Opération irréversible** : Impossible de récupérer fichiers après purge + GC
- **Force push** : Écrase historique GitHub, tous clones locaux deviennent obsolètes
- **Collaboration** : Informer tous contributeurs de re-cloner après purge

### ✅ Bonnes Pratiques

- Toujours faire backup avant BFG
- Tester sur clone test avant production
- Notifier équipe avant force push
- Vérifier CI après purge
- Documenter opération (commit message, changelog)

---

## Références

- **BFG Repo-Cleaner** : <https://rtyley.github.io/bfg-repo-cleaner/>
- **GitHub Docs** : <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
- **git-filter-repo** : <https://github.com/newren/git-filter-repo>

---

**Date document** : 2025-10-07
**Auteur** : Claude Code
**Status** : Documentation préparatoire (purge non exécutée)
