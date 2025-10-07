---
bmad_phase: maintenance
bmad_agent: dev
story_type: security
autonomous: false
validation: human-qa
---

# Story S6-07 : Renforcement Sécurité (Dependabot + BFG + SECURITY.md)

**Phase** : Semaine 6 - Excellence Technique
**Priorité** : Moyenne (P2 - robustesse)
**Estimation** : 3-5h

---

## Contexte projet

**Après POC v1.0.0** : Score qualité 94/100
- ✅ Secrets exclus (.gitignore, inspiration/ untracké)
- ✅ Pas de credentials hardcodés
- ⚠️ Pas de scan dépendances automatique (vulnérabilités CVE non détectées)
- ❌ Pas de SECURITY.md (responsible disclosure non documentée)
- ❌ Git history contient inspiration/ (fichiers sensibles dans historique)

**Scoring actuel** : Sécurité 18/20
- -1 : Pas de scan dépendances (Dependabot)
- -1 : Pas de SECURITY.md + Git history inspiration/

**Objectif S6-07** : Atteindre Sécurité 20/20 (+2 points → 96/100)

---

## Objectif

**Renforcer la sécurité du projet** sur 3 axes :
1. **Dependabot** : Scan automatique vulnérabilités dépendances
2. **SECURITY.md** : Responsible disclosure policy
3. **BFG Repo-Cleaner** : Purge inspiration/ de l'historique Git

**Livrables** :
- Dependabot configuré (`.github/dependabot.yml`)
- SECURITY.md créé (politique signalement vulnérabilités)
- Historique Git nettoyé (inspiration/ purgé)
- Documentation sécurité dans CONTRIBUTING.md

---

## Prérequis

- [x] Repo GitHub avec Actions activées
- [x] Permissions admin repo (Dependabot, force push)
- [x] inspiration/ déjà untracké (commit 0b768da)
- [ ] Backup repo avant BFG (sécurité)

---

## Étapes d'implémentation

### Phase 1 - Configuration Dependabot (1h)

#### Microtâches

**1.1 Créer fichier dependabot.yml** (20 min)

```yaml
# Fichier: .github/dependabot.yml
version: 2
updates:
  # Python dependencies (requirements.txt)
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
    open-pull-requests-limit: 5
    reviewers:
      - "Alexmacapple"
    labels:
      - "dependencies"
      - "security"
    commit-message:
      prefix: "chore(deps)"
      include: "scope"

  # GitHub Actions workflows
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
    open-pull-requests-limit: 3
    reviewers:
      - "Alexmacapple"
    labels:
      - "dependencies"
      - "ci"
    commit-message:
      prefix: "chore(ci)"

# Configuration avancée
rebase-strategy: "disabled"  # Éviter conflits auto-rebase
```

**Checklist** :
- [ ] Fichier `.github/dependabot.yml` créé
- [ ] Scan pip (requirements.txt) configuré
- [ ] Scan github-actions configuré
- [ ] Schedule hebdomadaire (lundi 9h)
- [ ] Limites PR (5 pip, 3 actions)
- [ ] Reviewers assignés
- [ ] Labels dependencies + security

**1.2 Activer Dependabot Security Alerts** (10 min)

**Via GitHub UI** :
1. Aller sur `https://github.com/Alexmacapple/span-sg-repo/settings/security_analysis`
2. Activer **Dependabot alerts** (vulnérabilités connues)
3. Activer **Dependabot security updates** (PR automatiques CVE)
4. Activer **Dependabot version updates** (mises à jour versions)

**Checklist** :
- [ ] Dependabot alerts activé
- [ ] Security updates activé
- [ ] Version updates activé
- [ ] Notifications email configurées

**1.3 Tester Dependabot** (30 min)

```bash
# Forcer scan initial
# GitHub détecte automatiquement dependabot.yml au push

# Créer branche test
git checkout -b test/dependabot-config
git add .github/dependabot.yml
git commit -m "chore(deps): configure Dependabot"
git push -u origin test/dependabot-config

# Vérifier :
# 1. Aller sur https://github.com/Alexmacapple/span-sg-repo/network/updates
# 2. Vérifier "Dependabot is configured"
# 3. Attendre première PR (peut prendre quelques minutes)

# Si vulnérabilités existantes → PR créées immédiatement
# Sinon → Scan hebdomadaire lundi 9h
```

**Checklist** :
- [ ] dependabot.yml poussé sur GitHub
- [ ] Dependabot détecté (network/updates)
- [ ] Pas d'erreur configuration
- [ ] PR Dependabot créée (si vulnérabilités)

---

### Phase 2 - SECURITY.md (30 min)

#### Microtâches

**2.1 Créer SECURITY.md** (20 min)

```markdown
# Fichier: SECURITY.md
# Politique de Sécurité SPAN SG

## Versions Supportées

Seule la dernière version stable de SPAN SG reçoit des correctifs de sécurité.

| Version | Support |
| ------- | ------- |
| 1.0.x   | ✅ Supportée |
| < 1.0   | ❌ Non supportée (POC) |

## Signaler une Vulnérabilité

### Responsible Disclosure

Si vous découvrez une vulnérabilité de sécurité dans SPAN SG, merci de **NE PAS** créer d'issue publique. Suivez cette procédure :

### 1. Contact Privé

Envoyez un email à **[security@sg.gouv.fr]** (ou **alex@example.com** provisoire) avec :
- Description détaillée de la vulnérabilité
- Étapes de reproduction
- Impact potentiel
- Version affectée
- Votre nom/pseudo (si vous souhaitez être crédité)

### 2. Délai de Réponse

- **Accusé réception** : < 48h
- **Analyse vulnérabilité** : < 7 jours
- **Correctif publié** : < 30 jours (selon gravité)

### 3. Coordination

Nous coordonnerons avec vous pour :
- Valider le correctif
- Planifier publication (disclosure coordonnée)
- Créditer votre découverte (si souhaité)

### 4. Gravité

Nous utilisons CVSS 3.1 pour évaluer la gravité :
- **Critique (9.0-10.0)** : Correctif < 7 jours
- **Haute (7.0-8.9)** : Correctif < 14 jours
- **Moyenne (4.0-6.9)** : Correctif < 30 jours
- **Faible (0.1-3.9)** : Correctif prochaine release

## Vulnérabilités Hors Périmètre

Ne sont **PAS** considérées comme vulnérabilités :
- Déni de service local (build MkDocs)
- Accès physique machine (scripts locaux)
- Social engineering
- Vulnérabilités dépendances tierces déjà publiques (Dependabot gère)

## Historique Sécurité

### v1.0.0-poc (2025-10-07)
- Aucune vulnérabilité connue
- Audit informel réalisé (07/10/2025)
- Secrets exclus (.gitignore + untrack inspiration/)

## Reconnaissance

Nous remercions les chercheurs en sécurité ayant signalé des vulnérabilités :
- [Aucun pour l'instant]

---

**Merci de contribuer à la sécurité de SPAN SG !**
```

**Checklist** :
- [ ] SECURITY.md créé (racine repo)
- [ ] Email contact sécurité renseigné (provisoire si besoin)
- [ ] Procédure responsible disclosure claire
- [ ] Délais réponse documentés
- [ ] Gravité CVSS 3.1 expliquée
- [ ] Hors périmètre explicite

**2.2 Ajouter lien SECURITY.md dans README** (10 min)

```markdown
# Fichier: README.md
# Ajouter section Sécurité après "Contribution"

## Sécurité

Pour signaler une vulnérabilité, consultez [SECURITY.md](SECURITY.md).

**Ne créez PAS d'issue publique pour les vulnérabilités.**
```

**Checklist** :
- [ ] Section Sécurité ajoutée README.md
- [ ] Lien vers SECURITY.md
- [ ] Avertissement issue publique

---

### Phase 3 - Purge Git History (BFG) (1-2h)

#### Microtâches

**3.1 Backup repo** (10 min)

```bash
# Backup complet avant opération irréversible
cd /Users/alex/Desktop
cp -r span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts span-sg-repo-BACKUP-$(date +%Y%m%d)

# Vérifier backup
ls -lh span-sg-repo-BACKUP-*

# Alternative : export GitHub
gh repo clone Alexmacapple/span-sg-repo /tmp/span-sg-backup
```

**Checklist** :
- [ ] Backup local créé (copie répertoire)
- [ ] Backup GitHub (clone séparé)
- [ ] Taille backup vérifiée (> 0 bytes)

**3.2 Installer BFG Repo-Cleaner** (10 min)

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

**Checklist** :
- [ ] BFG installé (brew ou JAR)
- [ ] Version vérifiée (1.14.0+)
- [ ] Commande `bfg` fonctionnelle

**3.3 Purger inspiration/ de l'historique** (30 min)

```bash
# 1. Clone bare repo (requis BFG)
cd /tmp
git clone --mirror https://github.com/Alexmacapple/span-sg-repo.git span-sg-bfg
cd span-sg-bfg

# 2. Lancer BFG pour supprimer dossier inspiration/
bfg --delete-folders inspiration

# Output attendu:
# Found X commits
# Found Y trees
# Removing inspiration/ from all commits...
# BFG run completed

# 3. Vérifier changements (dry-run)
git log --all --oneline --graph -- inspiration/
# Attendu: Aucun commit (dossier purgé)

# 4. Finaliser nettoyage (expire refs)
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 5. Force push vers GitHub
git push --force

# 6. Vérifier sur GitHub
# https://github.com/Alexmacapple/span-sg-repo/commits/draft
# Rechercher "inspiration/" → Aucun résultat
```

**Checklist** :
- [ ] Clone bare repo créé
- [ ] BFG exécuté sans erreur
- [ ] inspiration/ absent git log
- [ ] Reflog expiré
- [ ] Garbage collection effectuée
- [ ] Force push vers GitHub réussi

**3.4 Mettre à jour clones locaux** (10 min)

```bash
# Revenir au repo local principal
cd /Users/alex/Desktop/span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts

# Sauvegarder modifications locales (si applicable)
git stash

# Reset complet vers historique nettoyé
git fetch origin
git reset --hard origin/draft

# Vérifier inspiration/ toujours présent localement
ls -la inspiration/
# Attendu: Dossier existe (non versionné grâce .gitignore)

# Vérifier historique Git propre
git log --all --oneline -- inspiration/
# Attendu: Aucun résultat (purgé)
```

**Checklist** :
- [ ] Repo local synchronisé avec historique nettoyé
- [ ] inspiration/ toujours présent localement (non versionné)
- [ ] Historique Git propre (git log vide)

**3.5 Notifier collaborateurs** (10 min)

**Action critique** : Collaborateurs doivent re-cloner repo

```markdown
# Message Slack #span-sg-ci ou email équipe

⚠️ **ACTION REQUISE : Re-cloner le repository**

L'historique Git du projet SPAN SG a été nettoyé (purge fichiers sensibles).

**Si vous avez un clone local** :
1. Sauvegarder modifications en cours (`git stash`)
2. Supprimer clone existant
3. Re-cloner : `git clone https://github.com/Alexmacapple/span-sg-repo.git`

**Raison** : Fichiers sensibles retirés historique Git (S6-07).

**Deadline** : Avant prochain commit (sinon risque divergence historique).

Questions : @alex
```

**Checklist** :
- [ ] Message notif préparé
- [ ] Envoyé à tous collaborateurs (Slack/email)
- [ ] Instructions re-clone claires
- [ ] Contact support mentionné

---

### Phase 4 - Documentation (30 min)

#### Microtâches

**4.1 Documenter sécurité dans CONTRIBUTING.md** (20 min)

```markdown
# Fichier: CONTRIBUTING.md
# Ajouter section après "Tests et Coverage"

## Sécurité

### Signaler une Vulnérabilité

**NE PAS créer d'issue publique** pour les vulnérabilités.

Suivre la procédure dans [SECURITY.md](../SECURITY.md) :
- Email privé : security@sg.gouv.fr
- Délai réponse : < 48h
- Coordinated disclosure

### Dependabot

**Scan automatique** : Hebdomadaire (lundi 9h)
- Dépendances Python (requirements.txt)
- GitHub Actions (workflows)

**PR Dependabot** :
1. Revue changelog dépendance
2. Tester localement : `pip install -r requirements.txt && pytest`
3. Merger si tests passent
4. Label : `dependencies` + `security` (si CVE)

**Vulnérabilités critiques** :
- Dependabot crée PR immédiatement (pas d'attente lundi)
- Reviewer notifié (email GitHub)
- Merge prioritaire (< 24h)

### Secrets & Informations Sensibles

**Interdit de committer** :
- ❌ Credentials (API keys, tokens, passwords)
- ❌ .env files (secrets environnement)
- ❌ Fichiers sensibles (inspiration/, notes internes)
- ❌ Données personnelles (emails, noms agents)

**Si secret commis accidentellement** :
1. **NE PAS** simplement supprimer fichier (reste historique)
2. Révoquer secret immédiatement (régénérer clé API, etc.)
3. Contacter @alex pour purge historique (BFG)
4. Créer issue privée (Security Advisory GitHub)

### Pre-commit Hooks

**Hooks activés** :
- ruff : Détection secrets basique (patterns communs)
- Vérification .gitignore (exclusion .env, .secrets)

**Installer hooks** :
```bash
pre-commit install
```

Hooks bloquent commit si :
- Secrets détectés (AWS keys, tokens)
- Fichiers sensibles (*.pem, *.key)

### Bonnes Pratiques

- ✅ Utiliser variables environnement (`.env` + `.gitignore`)
- ✅ Secrets GitHub Actions (Settings → Secrets)
- ✅ Revue PR systématique (détection secrets échappés)
- ✅ Dependabot activé (scan vulnérabilités auto)
- ✅ SECURITY.md à jour (contact sécurité)
```

**Checklist** :
- [ ] Section Sécurité ajoutée CONTRIBUTING.md
- [ ] Procédure Dependabot documentée
- [ ] Interdictions secrets explicites
- [ ] Procédure si secret commis
- [ ] Bonnes pratiques listées

**4.2 Badge Dependabot README** (10 min)

```markdown
# Fichier: README.md
# Ajouter badge après badge Build/Deploy

[![Dependabot Status](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)](https://github.com/Alexmacapple/span-sg-repo/network/updates)
```

**Checklist** :
- [ ] Badge Dependabot ajouté README
- [ ] Lien vers network/updates fonctionnel

---

### Phase 5 - Tests & Validation (30 min)

#### Microtâches

**5.1 Vérifier Dependabot actif** (10 min)

```bash
# 1. Vérifier configuration détectée
curl -s https://api.github.com/repos/Alexmacapple/span-sg-repo/vulnerability-alerts | jq .

# 2. Forcer scan manuel (via GitHub UI)
# Settings → Code security and analysis → Dependabot → "Check for updates"

# 3. Vérifier PR Dependabot (si vulnérabilités)
gh pr list --label dependencies
```

**Checklist** :
- [ ] API GitHub confirme Dependabot activé
- [ ] Scan manuel déclenché
- [ ] PR Dependabot visibles (si applicable)

**5.2 Vérifier historique Git propre** (10 min)

```bash
# Rechercher "inspiration" dans tout l'historique
git log --all --source --full-history -- "*inspiration*"
# Attendu: Aucun résultat

# Vérifier taille repo réduite
du -sh .git
# Attendu: Réduction ~1-2 MB (9033 lignes purgées)

# Vérifier sur GitHub
# Recherche code : "inspiration/" → Aucun résultat historique
```

**Checklist** :
- [ ] git log vide pour inspiration/
- [ ] Taille .git réduite
- [ ] Recherche GitHub code négatif

**5.3 Valider SECURITY.md** (10 min)

```bash
# Vérifier SECURITY.md accessible publiquement
curl -s https://raw.githubusercontent.com/Alexmacapple/span-sg-repo/main/SECURITY.md | head -20

# GitHub affiche onglet Security avec SECURITY.md
# https://github.com/Alexmacapple/span-sg-repo/security/policy
```

**Checklist** :
- [ ] SECURITY.md accessible GitHub
- [ ] Onglet Security visible repo
- [ ] Contenu bien formaté

---

### Phase 6 - Commit & PR (30 min)

#### Microtâches

**6.1 Branche + Commit** (15 min)

```bash
git checkout draft
git pull origin draft
git checkout -b feature/s6-07-security-hardening

git add .github/dependabot.yml SECURITY.md README.md CONTRIBUTING.md
git commit -m "feat(security): renforce sécurité projet (S6-07)

- Dependabot configuré (scan hebdomadaire pip + actions)
- SECURITY.md créé (responsible disclosure policy)
- Git history nettoyé (inspiration/ purgé via BFG)
- Documentation sécurité dans CONTRIBUTING.md
- Badge Dependabot README

Score Sécurité: 18/20 → 20/20 (+2 points)
Score Global: 94/100 → 96/100

Closes: roadmap/S6-07-renforcement-securite.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push -u origin feature/s6-07-security-hardening
```

**6.2 Pull Request** (15 min)

```bash
gh pr create --base draft \
  --title "feat(security): Renforcement Sécurité (S6-07)" \
  --body "## Objectif
Améliorer scoring Sécurité 18/20 → 20/20 (+2 points → 96/100).

## Changements
- ✅ Dependabot configuré (`.github/dependabot.yml`)
  - Scan hebdomadaire pip + github-actions
  - Security alerts activées
  - PR automatiques vulnérabilités
- ✅ SECURITY.md créé
  - Responsible disclosure policy
  - Email contact : security@sg.gouv.fr
  - Délais réponse < 48h
  - Gravité CVSS 3.1
- ✅ Git history nettoyé (BFG Repo-Cleaner)
  - inspiration/ purgé historique (9033 lignes)
  - Force push effectué
  - Collaborateurs notifiés (re-clone requis)
- ✅ Documentation CONTRIBUTING.md
  - Section Sécurité complète
  - Procédure Dependabot
  - Bonnes pratiques secrets
- ✅ Badge Dependabot README

## Validation
- [x] Dependabot actif (network/updates)
- [x] SECURITY.md accessible (onglet Security)
- [x] Git history propre (git log inspiration/ vide)
- [x] Backup repo effectué avant BFG

## Impact
**Score Sécurité** : 18/20 → 20/20 (+2 points)
**Score Global** : 94/100 → 96/100

## Note Collaborateurs
⚠️ **Git history modifié** : Re-cloner repo si clone local existant.

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

**Checklist** :
- [ ] PR créée vers `draft`
- [ ] CI passe
- [ ] Note re-clone visible
- [ ] Revue Alexandra/Bertrand

---

## Critères d'acceptation

### Fonctionnels
- [ ] Dependabot configuré et actif
- [ ] SECURITY.md créé et accessible
- [ ] Git history purgé (inspiration/ absent)
- [ ] Collaborateurs notifiés re-clone

### Techniques
- [ ] `.github/dependabot.yml` valide
- [ ] Security alerts GitHub activées
- [ ] BFG exécuté sans erreur
- [ ] Force push réussi
- [ ] Backup repo effectué

### Documentation
- [ ] Section Sécurité CONTRIBUTING.md
- [ ] Lien SECURITY.md README
- [ ] Badge Dependabot README
- [ ] Procédure secrets documentée

### Performance
- [ ] Taille .git réduite (~1-2 MB)
- [ ] Scan Dependabot < 5 min (hebdo)

---

## Risques & Solutions

### Risque 1 : Force push casse clones collaborateurs
**Probabilité** : Haute
**Impact** : Moyen (divergence historique)

**Solution** :
- Notifier TOUS collaborateurs AVANT force push
- Instructions re-clone claires
- Deadline annoncée (ex: "avant 18h")
- Support disponible (Slack, email)

### Risque 2 : BFG purge fichiers légitimes
**Probabilité** : Faible
**Impact** : Critique (perte données)

**Solution** :
- Backup complet AVANT BFG (obligatoire)
- Dry-run BFG (vérifier changements)
- Tester sur clone séparé d'abord
- Garder backup 30 jours

### Risque 3 : Spam PR Dependabot
**Probabilité** : Faible
**Impact** : Faible (bruit)

**Solution** :
- Limiter PR (5 pip, 3 actions)
- Schedule hebdomadaire (pas quotidien)
- Auto-merge PR mineures (future)
- Labels clairs (dependencies, security)

---

## Métriques succès

**Avant S6-07** :
- Dependabot : ❌ Non configuré
- SECURITY.md : ❌ Absent
- Git history : ⚠️ inspiration/ présent (9033 lignes)
- Score Sécurité : 18/20

**Après S6-07** :
- Dependabot : ✅ Actif (scan hebdo)
- SECURITY.md : ✅ Publié (responsible disclosure)
- Git history : ✅ Propre (inspiration/ purgé)
- Score Sécurité : **20/20**

**Impact scoring** : 94/100 → 96/100 (+2 points Sécurité)

---

## Dépendances

**Bloquants** :
- Permissions admin repo (Dependabot, force push)
- Backup repo avant BFG

**Facilitateurs** :
- inspiration/ déjà untracké (commit 0b768da)
- Pas de collaborateurs actifs (POC solo)

**Bloque** : Aucune story

---

## Notes d'implémentation

### Alternative : git filter-repo vs BFG
**BFG recommandé** :
- Plus simple (1 commande)
- Plus rapide (10-50x vs filter-branch)
- Maintenu activement

**git filter-repo** (alternative moderne) :
```bash
pip install git-filter-repo
git filter-repo --path inspiration/ --invert-paths
```

### Dependabot auto-merge (future)
**Évolution v2.0** :
```yaml
# .github/workflows/dependabot-auto-merge.yml
# Auto-merge PR Dependabot si tests passent + version patch/minor
```

### Email sécurité provisoire
**SECURITY.md utilise email provisoire** :
- `security@sg.gouv.fr` (à valider avec Alexandra)
- Fallback : `alex@example.com` (remplacer avant prod)
- Alternative : GitHub Security Advisories (privé)

### Post-BFG : Vérification approfondie
```bash
# Rechercher patterns sensibles dans historique
git log --all -S"password" --source
git log --all -S"secret" --source
git log --all -S"token" --source
# Attendu: Aucun résultat suspect
```
