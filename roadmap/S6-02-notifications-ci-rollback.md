---
bmad_phase: maintenance
bmad_agent: dev
story_type: ops
autonomous: false
validation: human-qa
---

# Story S6-02 : Notifications CI & Rollback Automatique

**Phase** : Semaine 6 - Excellence Technique
**Priorité** : Faible (P3 - confort dev)
**Estimation** : 4-6h

---

## Contexte projet

**Après POC v1.0.0** : Score qualité 94/100
- ✅ CI GitHub Actions complète (build + tests + deploy)
- ✅ Déploiement automatique GitHub Pages (draft + main)
- ⚠️ Pas de notifications échecs CI (détection manuelle)
- ❌ Pas de rollback automatique si deploy échoue

**Problème actuel** :
- Échecs CI nécessitent surveillance GitHub Actions UI
- Deploy KO → site reste cassé jusqu'à correction manuelle
- Pas d'alerte proactive (email, Slack)

**Scénario problématique** :
1. Merge PR vers `main` avec régression
2. Deploy échoue (MkDocs build error)
3. Site production inaccessible
4. Détection tardive (heures/jours)
5. Rollback manuel (`git revert` + force push)

**Objectif S6-02** : Notifications temps réel + rollback automatique

---

## Objectif

**Améliorer la détection et récupération des échecs CI** :
- Notifications Slack/email temps réel
- Rollback automatique si deploy échoue
- Dashboard statut CI (optionnel)

**Livrables** :
- Webhook Slack pour notifications CI
- Script rollback automatique
- Job GitHub Actions rollback conditionnel
- Documentation notifications dans CONTRIBUTING.md

---

## Prérequis

- [x] CI GitHub Actions fonctionnelle
- [x] Déploiement GitHub Pages actif
- [x] Accès admin repo (webhooks, secrets)
- [ ] Workspace Slack (ou alternative email)

---

## Étapes d'implémentation

### Phase 1 - Configuration Notifications Slack (1-2h)

#### Microtâches

**1.1 Créer Slack App et Webhook** (30 min)

**Étapes Slack** :
1. Aller sur https://api.slack.com/apps
2. Créer nouvelle app "SPAN SG CI"
3. Activer "Incoming Webhooks"
4. Créer webhook vers channel `#span-sg-ci`
5. Copier Webhook URL (`https://hooks.slack.com/services/...`)

**Checklist** :
- [ ] App Slack créée
- [ ] Webhook activé
- [ ] Channel #span-sg-ci créé
- [ ] URL webhook copiée

**1.2 Ajouter secret GitHub** (10 min)

```bash
# Via GitHub UI
# Settings → Secrets and variables → Actions → New repository secret
# Name: SLACK_WEBHOOK_URL
# Value: https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX
```

**Checklist** :
- [ ] Secret SLACK_WEBHOOK_URL ajouté
- [ ] Secret accessible workflows

**1.3 Ajouter step notification dans workflow** (30 min)

```yaml
# Fichier: .github/workflows/build.yml
# Ajouter à la fin de chaque job critique

jobs:
  build:
    # ... steps existants ...

    - name: Notify Slack on failure
      if: failure()
      uses: slackapi/slack-github-action@v1.25.0
      with:
        payload: |
          {
            "text": "❌ Build SPAN SG échoué",
            "blocks": [
              {
                "type": "header",
                "text": {
                  "type": "plain_text",
                  "text": "❌ Build Failed"
                }
              },
              {
                "type": "section",
                "fields": [
                  {
                    "type": "mrkdwn",
                    "text": "*Repo:*\n${{ github.repository }}"
                  },
                  {
                    "type": "mrkdwn",
                    "text": "*Branch:*\n${{ github.ref_name }}"
                  },
                  {
                    "type": "mrkdwn",
                    "text": "*Commit:*\n<${{ github.event.head_commit.url }}|${{ github.sha }}>"
                  },
                  {
                    "type": "mrkdwn",
                    "text": "*Auteur:*\n${{ github.actor }}"
                  }
                ]
              },
              {
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "<${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|Voir logs CI>"
                }
              }
            ]
          }
      env:
        SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK

    - name: Notify Slack on success
      if: success()
      uses: slackapi/slack-github-action@v1.25.0
      with:
        payload: |
          {
            "text": "✅ Build SPAN SG réussi - ${{ github.ref_name }}"
          }
      env:
        SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
```

**Checklist** :
- [ ] Action Slack ajoutée (failure + success)
- [ ] Payload JSON formaté (blocks Slack)
- [ ] Lien vers logs CI inclus
- [ ] Métadonnées commit/branch/auteur

**1.4 Tester notification** (30 min)

```bash
# Créer branche test avec build cassé
git checkout -b test/slack-notification
echo "invalid yaml" >> mkdocs.yml
git commit -am "test: break build pour tester Slack"
git push -u origin test/slack-notification

# Vérifier :
# 1. CI échoue
# 2. Message Slack reçu dans #span-sg-ci
# 3. Lien logs fonctionnel

# Nettoyer
git checkout draft
git branch -D test/slack-notification
git push origin --delete test/slack-notification
```

**Checklist** :
- [ ] Notification échec reçue dans Slack
- [ ] Format message correct (emoji, blocs, lien)
- [ ] Notification succès reçue après fix

---

### Phase 2 - Rollback Automatique (2-3h)

#### Microtâches

**2.1 Créer script rollback** (1h)

```bash
# Fichier: scripts/rollback.sh
#!/bin/bash
# Rollback automatique du dernier déploiement GitHub Pages

set -e

BRANCH="${1:-main}"
PAGES_BRANCH="gh-pages"

echo "🔄 Rollback déploiement GitHub Pages ($BRANCH)"

# Récupérer dernier commit OK (avant le deploy actuel)
LAST_GOOD_COMMIT=$(git log "$PAGES_BRANCH" --oneline -2 | tail -1 | cut -d' ' -f1)

if [ -z "$LAST_GOOD_COMMIT" ]; then
    echo "❌ Impossible de trouver commit précédent"
    exit 1
fi

echo "📍 Dernier commit OK : $LAST_GOOD_COMMIT"

# Rollback gh-pages
git checkout "$PAGES_BRANCH"
git reset --hard "$LAST_GOOD_COMMIT"
git push origin "$PAGES_BRANCH" --force

echo "✅ Rollback effectué vers $LAST_GOOD_COMMIT"
echo "🌐 Site restauré : https://alexmacapple.github.io/span-sg-repo/"

# Retour branche initiale
git checkout "$BRANCH"
```

**Checklist** :
- [ ] Script rollback.sh créé
- [ ] Permissions exécution (+x)
- [ ] Gestion erreurs (set -e)
- [ ] Logs clairs (étapes visibles)

**2.2 Ajouter job rollback dans workflow** (1h)

```yaml
# Fichier: .github/workflows/build.yml
# Ajouter nouveau job après deploy

  rollback:
    name: Rollback on Deploy Failure
    runs-on: ubuntu-latest
    needs: deploy
    if: failure() && (github.ref == 'refs/heads/main' || github.ref == 'refs/heads/draft')

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Historique complet pour rollback
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Configure Git
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

      - name: Execute rollback
        run: |
          chmod +x scripts/rollback.sh
          ./scripts/rollback.sh ${{ github.ref_name }}

      - name: Notify Slack rollback
        if: success()
        uses: slackapi/slack-github-action@v1.25.0
        with:
          payload: |
            {
              "text": "🔄 Rollback automatique effectué - ${{ github.ref_name }}",
              "blocks": [
                {
                  "type": "header",
                  "text": {
                    "type": "plain_text",
                    "text": "🔄 Rollback Automatique"
                  }
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "Le déploiement a échoué. Site restauré à la version précédente.\n\n*Action requise:* Corriger le commit défaillant avant nouveau merge."
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {
                      "type": "mrkdwn",
                      "text": "*Branch:*\n${{ github.ref_name }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Commit échoué:*\n${{ github.sha }}"
                    }
                  ]
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK

      - name: Notify Slack rollback failed
        if: failure()
        uses: slackapi/slack-github-action@v1.25.0
        with:
          payload: |
            {
              "text": "⚠️ URGENT: Rollback automatique échoué - ${{ github.ref_name }}",
              "blocks": [
                {
                  "type": "header",
                  "text": {
                    "type": "plain_text",
                    "text": "⚠️ Rollback Failed"
                  }
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "**Action immédiate requise**: Site potentiellement inaccessible.\n\nIntervention manuelle nécessaire."
                  }
                },
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "<${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|Voir logs CI>"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
```

**Checklist** :
- [ ] Job rollback conditionnel (if: failure())
- [ ] Déclenchement seulement main/draft
- [ ] fetch-depth: 0 (historique complet)
- [ ] Notifications Slack (succès + échec rollback)

**2.3 Tester rollback en staging** (1h)

```bash
# Créer branche test avec deploy cassé
git checkout -b test/rollback-auto
echo "invalid: yaml: syntax" >> mkdocs.yml
git commit -am "test: break deploy pour tester rollback"
git push -u origin test/rollback-auto

# Merger vers draft (simule production)
gh pr create --base draft --title "test: rollback auto" --body "Test rollback automatique"
gh pr merge --merge

# Vérifier :
# 1. CI échoue au deploy
# 2. Job rollback s'exécute
# 3. Site draft restauré version précédente
# 4. Notification Slack rollback reçue

# Nettoyer
git checkout draft
git revert HEAD --no-edit
git push origin draft
```

**Checklist** :
- [ ] Deploy échoue comme attendu
- [ ] Job rollback exécuté automatiquement
- [ ] Site restauré version précédente
- [ ] Notification Slack "Rollback effectué"
- [ ] Pas d'interruption service (downtime < 1 min)

---

### Phase 3 - Alternative Email (Optionnel) (1h)

#### Microtâches

**3.1 Configurer notifications email** (30 min)

Si pas de Slack, alternative avec SendGrid/Mailgun :

```yaml
# Utiliser action email au lieu de Slack
- name: Send email on failure
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: "❌ Build SPAN SG échoué - ${{ github.ref_name }}"
    to: ${{ secrets.NOTIFICATION_EMAIL }}
    from: GitHub Actions
    body: |
      Build échoué sur ${{ github.repository }}

      Branch: ${{ github.ref_name }}
      Commit: ${{ github.sha }}
      Auteur: ${{ github.actor }}

      Logs: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

**Checklist** :
- [ ] Secrets EMAIL_USERNAME, EMAIL_PASSWORD, NOTIFICATION_EMAIL configurés
- [ ] Action send-mail testée
- [ ] Email reçu lors échec CI

**3.2 GitHub native notifications** (30 min)

Alternative sans service externe :

```yaml
# Créer issue automatiquement en cas d'échec
- name: Create issue on deploy failure
  if: failure() && github.ref == 'refs/heads/main'
  uses: actions/github-script@v7
  with:
    script: |
      github.rest.issues.create({
        owner: context.repo.owner,
        repo: context.repo.repo,
        title: `🚨 Deploy Failed - ${context.sha.substring(0, 7)}`,
        body: `Deploy échoué sur \`main\` au commit ${context.sha}.

        **Rollback**: ${context.payload.repository.html_url}/actions/runs/${context.runId}

        **Action requise**: Corriger le build avant nouveau merge.`,
        labels: ['ci-failure', 'urgent']
      })
```

**Checklist** :
- [ ] Issue créée automatiquement si deploy main échoue
- [ ] Labels ci-failure + urgent
- [ ] Notifications GitHub natives activées

---

### Phase 4 - Documentation (1h)

#### Microtâches

**4.1 Documenter notifications dans CONTRIBUTING.md** (30 min)

```markdown
# Ajouter section après CI/CD

## Notifications CI

### Slack
Les échecs/succès CI sont notifiés dans `#span-sg-ci` :
- ❌ Build échoué : Message détaillé (branch, commit, auteur, logs)
- ✅ Build réussi : Confirmation simple
- 🔄 Rollback effectué : Alerte restauration automatique

**Configurer notifications** :
1. Rejoindre channel Slack `#span-sg-ci`
2. Activer notifications (@mentions + all messages)

### Email (Alternative)
Si pas d'accès Slack :
- Ajouter email dans secret `NOTIFICATION_EMAIL`
- Emails envoyés via GitHub Actions (SendGrid)

### Issues GitHub
En cas d'échec deploy `main` :
- Issue créée automatiquement (label `ci-failure`)
- Assignée à auteur du commit
- Notifications GitHub natives

---

## Rollback Automatique

### Comportement
Si déploiement GitHub Pages échoue :
1. Job `rollback` déclenché automatiquement
2. Site restauré à version précédente (commit n-1)
3. Notification Slack "Rollback effectué"
4. Downtime < 1 minute

### Rollback Manuel
Si rollback auto échoue :

```bash
# Identifier dernier commit OK
gh api /repos/Alexmacapple/span-sg-repo/pages/builds | jq '.[1].commit'

# Rollback gh-pages
git checkout gh-pages
git reset --hard <commit-ok>
git push origin gh-pages --force

# OU utiliser script
./scripts/rollback.sh main
```

### Prévention
- Tester localement avant merge : `mkdocs build --strict`
- Utiliser PR vers `draft` (preview avant production)
- Valider preview draft avant merge vers `main`
```

**Checklist** :
- [ ] Section Notifications CI ajoutée
- [ ] Section Rollback Automatique documentée
- [ ] Procédure rollback manuel
- [ ] Conseils prévention

**4.2 Ajouter badge statut CI** (15 min)

```markdown
# Fichier: README.md
# Remplacer badge existant par version dynamique

[![Build Status](https://img.shields.io/github/actions/workflow/status/Alexmacapple/span-sg-repo/build.yml?branch=main&label=build&logo=github)](https://github.com/Alexmacapple/span-sg-repo/actions/workflows/build.yml)
[![Deploy Status](https://img.shields.io/github/deployments/Alexmacapple/span-sg-repo/github-pages?label=deploy&logo=github)](https://github.com/Alexmacapple/span-sg-repo/deployments)
```

**Checklist** :
- [ ] Badge Build Status ajouté (workflow build.yml)
- [ ] Badge Deploy Status ajouté (GitHub Pages)
- [ ] Badges fonctionnels (statut temps réel)

**4.3 Créer runbook incidents** (15 min)

```markdown
# Fichier: docs/runbook-incidents.md
# Runbook Incidents CI/CD

## Incident : Deploy Failed

### Symptômes
- Notification Slack "❌ Build échoué"
- Site production inaccessible ou version obsolète
- Badge Deploy rouge dans README

### Diagnostic
1. Consulter logs CI : [Actions](https://github.com/Alexmacapple/span-sg-repo/actions)
2. Identifier étape échec (build, tests, deploy)
3. Vérifier commit problématique

### Résolution Automatique
- Rollback auto exécuté (< 1 min)
- Site restauré version précédente
- Notification "🔄 Rollback effectué"

### Résolution Manuelle (si rollback auto échoue)
```bash
# Rollback gh-pages
./scripts/rollback.sh main

# OU force push commit précédent
git checkout gh-pages
git reset --hard HEAD~1
git push origin gh-pages --force
```

### Prévention Future
1. Corriger commit défaillant localement
2. Tester : `mkdocs build --strict`
3. Créer PR vers `draft` (preview)
4. Valider preview : https://alexmacapple.github.io/span-sg-repo/draft/
5. Merger vers `main` seulement si draft OK

---

## Incident : Rollback Failed

### Symptômes
- Notification Slack "⚠️ URGENT: Rollback automatique échoué"
- Site potentiellement inaccessible
- Job rollback en erreur

### Action Immédiate
**Priorité 1** : Restaurer service

```bash
# Rollback manuel forcé
git checkout gh-pages
git log --oneline -5  # Identifier dernier commit OK
git reset --hard <commit-ok>
git push origin gh-pages --force
```

**Vérification** :
- Site accessible : https://alexmacapple.github.io/span-sg-repo/
- Version correcte affichée

### Post-Mortem
1. Analyser logs job rollback
2. Identifier cause échec (permissions, historique Git, etc.)
3. Corriger script `scripts/rollback.sh`
4. Ajouter tests rollback (simulation)
```

**Checklist** :
- [ ] Runbook incidents créé
- [ ] Procédures diagnostic/résolution
- [ ] Commandes copy-paste prêtes

---

### Phase 5 - Tests & Validation (1h)

#### Microtâches

**5.1 Test complet workflow** (30 min)

```bash
# Scénario 1 : Build réussi
git checkout -b test/notification-success
echo "# Test" >> README.md
git commit -am "test: notification succès"
git push -u origin test/notification-success
# → Vérifier notification Slack "✅ Build réussi"

# Scénario 2 : Build échoué
git checkout -b test/notification-failure
echo "invalid yaml" >> mkdocs.yml
git commit -am "test: notification échec"
git push -u origin test/notification-failure
# → Vérifier notification Slack "❌ Build échoué"

# Scénario 3 : Deploy échoué + rollback
git checkout draft
git merge test/notification-failure --no-ff
git push origin draft
# → Vérifier :
#    1. Deploy échoue
#    2. Rollback auto exécuté
#    3. Notification "🔄 Rollback effectué"
#    4. Site draft restauré

# Nettoyer
git revert HEAD --no-edit
git push origin draft
```

**Checklist** :
- [ ] Notification succès reçue
- [ ] Notification échec reçue (avec détails)
- [ ] Rollback auto fonctionnel
- [ ] Notification rollback reçue
- [ ] Site restauré version précédente

**5.2 Créer PR et valider** (30 min)

```bash
git checkout -b feature/s6-02-notifications-rollback
git add scripts/rollback.sh .github/workflows/build.yml docs/runbook-incidents.md
git commit -m "feat(ops): notifications CI + rollback auto (S6-02)

- Notifications Slack (échec/succès/rollback)
- Rollback automatique si deploy échoue
- Script rollback.sh pour intervention manuelle
- Runbook incidents CI/CD
- Badges statut dynamiques README

Closes: roadmap/S6-02-notifications-ci-rollback.md"
git push -u origin feature/s6-02-notifications-rollback

gh pr create --base draft --title "feat(ops): Notifications CI + Rollback Auto (S6-02)" --body "..."
```

**Checklist PR** :
- [ ] PR créée vers `draft`
- [ ] CI passe
- [ ] Notifications testées
- [ ] Rollback testé (simulation)
- [ ] Revue Alex/Bertrand

---

## Critères d'acceptation

### Fonctionnels
- [ ] Notifications Slack temps réel (échec + succès)
- [ ] Rollback automatique si deploy échoue
- [ ] Script rollback.sh manuel fonctionnel
- [ ] Downtime < 1 minute en cas d'échec deploy

### Techniques
- [ ] Webhook Slack configuré
- [ ] Secret SLACK_WEBHOOK_URL sécurisé
- [ ] Job rollback conditionnel (if: failure())
- [ ] Notifications détaillées (branch, commit, auteur, logs)

### Documentation
- [ ] Section Notifications CI dans CONTRIBUTING.md
- [ ] Section Rollback Automatique documentée
- [ ] Runbook incidents créé (docs/runbook-incidents.md)
- [ ] Badges statut ajoutés README

### Performance
- [ ] Notification < 10s après échec CI
- [ ] Rollback < 60s après échec deploy

---

## Risques & Solutions

### Risque 1 : Spam notifications Slack
**Probabilité** : Moyenne
**Impact** : Faible (bruit)

**Solution** :
- Désactiver notifications succès (garder seulement échecs)
- Throttling : 1 notification/10 min max
- Channel dédié (pas #general)

### Risque 2 : Rollback casse site différemment
**Probabilité** : Faible
**Impact** : Critique (double panne)

**Solution** :
- Tester rollback sur draft avant activation main
- Rollback seulement si deploy échoue (pas build)
- Alerte Slack si rollback échoue (escalation manuelle)

### Risque 3 : Permissions rollback insuffisantes
**Probabilité** : Faible
**Impact** : Moyen (rollback échoue)

**Solution** :
- Utiliser GITHUB_TOKEN avec permissions write
- Vérifier permissions gh-pages (force push autorisé)
- Fallback manuel documenté (runbook)

---

## Métriques succès

**Avant S6-02** :
- Détection échecs : Manuelle (GitHub UI)
- Temps résolution : 1h-24h (détection tardive)
- Downtime moyen : 30 min - 2h
- Rollback : Manuel uniquement

**Après S6-02** :
- Détection : < 10s (notification Slack)
- Temps résolution : < 5 min (rollback auto)
- Downtime : < 1 min
- Rollback : Automatique + manuel (fallback)

**Impact scoring** : 94/100 → 95/100 (+1 point CI/CD)

---

## Dépendances

**Bloquants** :
- Workspace Slack (ou alternative email)
- Permissions GitHub Actions (secrets, force push gh-pages)

**Facilitateurs** :
- S2-01 (GitHub Actions) : Workflow existant
- S2-03 (Preview privée) : GitHub Pages configuré

**Bloque** : Aucune story

---

## Notes d'implémentation

### Alternative : GitHub Status Checks
**Option** : Utiliser GitHub native commit status au lieu de Slack

**Avantages** :
- Pas de service externe
- Intégré UI GitHub (commits + PR)

**Inconvénients** :
- Pas de notifications proactives (nécessite surveillance GitHub)
- Moins visible que Slack

**Décision** : Slack recommandé (notifications temps réel), GitHub Status Checks en complément

### Évolution future (v2.0)
- Intégration PagerDuty (alertes on-call)
- Rollback intelligent (tests santé avant/après)
- Métriques MTTR (Mean Time To Recovery)
- Dashboard statut public (status.span-sg.gouv.fr)
