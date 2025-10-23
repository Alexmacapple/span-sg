# Guide Chef SNUM - Approval Déploiements Production

Guide pour approuver les déploiements production SPAN SG via GitHub Environments.

Version: 1.0.0
Date: 2025-10-22
Public cible: Chef SNUM
Durée lecture: 10 minutes

---

## Vue d'ensemble

Depuis la migration GitHub Environments (ADR-009), vous êtes **gate-keeper** des déploiements production.

**Votre rôle** :
- Recevoir notifications "Deployment to production pending"
- Review staging https://alexmacapple.github.io/span-sg/draft/
- Approuver déploiement production https://alexmacapple.github.io/span-sg/

**Délai typique** :
- Hotfix urgent : Approuver immédiatement (< 1h)
- Contribution normale : Variable selon stratégie (0-60 jours)
- Batch releases : Accumulation 10-20 contributions puis approval groupée

---

## Processus Approval (5 étapes)

### Étape 1 : Recevoir Notification

**Email GitHub** :

```
From: notifications@github.com
Subject: [Alexmacapple/span-sg] Deployment to production pending review

Environment: production
URL: https://alexmacapple.github.io/span-sg/
Status: Pending approval
Commit: 02a52e7 (docs: amélioration documentation 8/10 → 10/10)

You have been requested to review this deployment.
Review deployment: https://github.com/Alexmacapple/span-sg/deployments/...
```

**Fréquence** : Variable selon activité contributeurs (1-5 notifications/semaine estimé)

**Action** : Cliquer lien "Review deployment" ou aller manuellement sur dashboard

---

### Étape 2 : Consulter Dashboard Deployments

**URL** : https://github.com/Alexmacapple/span-sg/deployments

**Interface** :

```
┌───────────────────────────────────────────────────────────┐
│ Deployments                                               │
├───────────────────────────────────────────────────────────┤
│ Environment: production                                   │
│ Status: ⏳ Waiting for review                            │
│ Deployed by: github-actions[bot]                         │
│ Commit: 02a52e7 (docs: amélioration...)                  │
│ Requested: 2025-10-22 14:10 (5 minutes ago)              │
│                                                           │
│ Changes in this deployment:                               │
│ - docs: amélioration documentation 8/10 → 10/10          │
│ - feat(sircom): ajoute 3 actions plan 2025               │
│ - fix(accessibility): corriger timeout urllib3            │
│                                                           │
│ Preview staging: https://...github.io/span-sg/draft/      │
│                                                           │
│ [Review deployment]                                       │
└───────────────────────────────────────────────────────────┘
```

**Informations disponibles** :
- Commit SHA et message
- Liste changements depuis dernier déploiement production
- Lien staging preview
- Timestamp demande approval

---

### Étape 3 : Review Staging

**URL staging** : https://alexmacapple.github.io/span-sg/draft/

**Checklist review** (5-10 minutes) :

- [ ] **Navigation générale** : Ouvrir site, tester menu latéral
- [ ] **SPAN par service du Secrétariat Général (SG)** : Vérifier 2-3 modules (SIRCOM, SNUM)
- [ ] **Synthèse** : Vérifier tableau scores cohérent
- [ ] **Badges DSFR** : Vérifier badges visibles (Validé, En cours)
- [ ] **PDF exports** : Télécharger span-sg.pdf, ouvrir (metadata OK)
- [ ] **Aucune régression** : Comparer avec production actuelle

**Outils** :
- Navigation manuelle navigateur
- Optionnel : Lighthouse accessibility score (devrait être 90+)
- Optionnel : Compare staging vs production (outil diff visuel)

**Durée** : 5-10 minutes selon ampleur changements

---

### Étape 4 : Vérifier Logs CI/CD

**URL GitHub Actions** : https://github.com/Alexmacapple/span-sg/actions

**Workflow à vérifier** : Dernier run "Build and Deploy"

**Statuts à vérifier** :

```
Job: build-and-test
  ✅ Linting (Black + Ruff)
  ✅ Security (Bandit + Safety)
  ✅ Tests (33 unitaires, coverage 89%+)
  ✅ Build HTML DSFR (strict mode)
  ✅ Generate PDF
  ✅ E2E tests (9 scenarios)

Job: deploy-staging
  ✅ Deploy /draft/

Job: deploy-production
  ⏳ Waiting for approval (vous)
```

**Vérifier logs** :
- Aucune erreur bloquante
- Coverage scripts ≥ 89%, hooks 100%
- E2E tests 9/9 passés
- PDF généré avec metadata enrichies

**Warnings acceptables** :
- git-revision-date plugin warnings (non bloquant)
- RGAA timeouts accessibilité (tests non bloquants, continue-on-error: true)

**Durée** : 2-3 minutes

---

### Étape 5 : Approuver ou Rejeter

#### Option A : Approuver (cas nominal)

**Action** :

1. Retourner dashboard Deployments
2. Cliquer "Review deployment"
3. Sélectionner "Approve deployment"
4. (Optionnel) Ajouter commentaire : "LGTM, déploiement approuvé"
5. Cliquer "Approve"

**Résultat** :
- Déploiement production déclenché automatiquement
- Durée : 2-5 minutes
- Notification email : "Deployment to production succeeded"
- Site production mis à jour : https://alexmacapple.github.io/span-sg/

#### Option B : Rejeter (problème détecté)

**Action** :

1. Cliquer "Review deployment"
2. Sélectionner "Reject deployment"
3. Ajouter commentaire expliquant raison rejet :
   ```
   Régression détectée : Tableau synthèse cassé (badges non visibles)
   Merci de corriger avant re-déploiement
   ```
4. Cliquer "Reject"

**Résultat** :
- Déploiement production annulé
- Notification équipe développement
- Validateurs corrigent problème
- Nouveau déploiement soumis après corrections

#### Option C : Différer (attendre accumulation)

**Action** :

1. Ignorer notification (ne rien faire)
2. Déploiement reste "Pending approval"
3. Contributions ultérieures s'accumulent en staging
4. Approuver plus tard quand batch suffisant (ex: 10 contributions)

**Note** : Pas de limite temporelle, vous décidez quand approuver

---

## Cas d'Usage

### Cas 1 : Hotfix Urgent

**Contexte** : Bug critique production détecté, correctif développé

**Workflow** :

```
10:00 : Bug détecté production (lien cassé page Synthèse)
10:15 : Validateur crée hotfix branch, corrige, merge main
10:20 : CI/CD build-and-test passe
10:22 : Deploy staging automatique
10:22 : Vous recevez notification "Pending approval"
10:25 : Vous review staging (3 min) : Bug corrigé
10:28 : Vous approuvez immédiatement
10:33 : Deploy production terminé, bug résolu

Total : 33 minutes bug détecté → production
```

**Action recommandée** : **Approuver immédiatement** après review rapide

---

### Cas 2 : Contribution Normale

**Contexte** : Contributeur service complète module SIRCOM (3 critères cochés)

**Workflow** :

```
J+0  : Contributeur crée PR vers main
J+2  : Validateur review et merge
J+2  : Deploy staging automatique
J+2  : Vous recevez notification "Pending approval"
J+2-30 : Vous laissez pending (accumulation autres contributions)
J+30 : 8 contributions accumulées en staging
J+30 : Vous review staging (10 min) : Tout OK
J+30 : Vous approuvez batch 8 contributions
J+30 : Deploy production terminé

Total : 30 jours contribution → production (délai voulu)
```

**Action recommandée** : **Différer** jusqu'à accumulation suffisante (votre décision)

---

### Cas 3 : Régression Détectée

**Contexte** : Erreur staging détectée lors review

**Workflow** :

```
14:00 : Vous recevez notification "Pending approval"
14:05 : Vous review staging
14:08 : Problème détecté : Badges DSFR non visibles (CSS cassé)
14:10 : Vous rejetez deployment avec commentaire
14:15 : Validateur notifié, investigation
15:00 : Correctif mergé sur main
15:05 : Nouveau deployment staging automatique
15:05 : Nouvelle notification "Pending approval"
15:10 : Vous review staging : Bug corrigé
15:12 : Vous approuvez
15:17 : Deploy production terminé

Total : 1h17 (dont 45 min correction)
```

**Action recommandée** : **Rejeter** avec commentaire explicite

---

## Dashboard Centralisé

### Accès

**URL bookmark** : https://github.com/Alexmacapple/span-sg/deployments

Ajouter aux favoris navigateur pour accès rapide.

### Filtres

```
Environment: [All] [staging] [production]
Status: [All] [Active] [Pending] [Failed]
```

**Exemples filtres** :

- Voir déploiements production uniquement : Filter "Environment: production"
- Voir déploiements en attente approval : Filter "Status: Pending"
- Historique staging : Filter "Environment: staging"

### Historique

**Timeline déploiements** (scrollable) :

```
2025-10-22 14:35 : production → 02a52e7 (docs 10/10) [Active]
2025-10-22 14:10 : staging → 02a52e7 (docs 10/10) [Active]
2025-10-15 10:20 : production → 3c06ca1 (rollback strict) [Superseded]
2025-10-15 10:18 : staging → 3c06ca1 (rollback strict) [Superseded]
2025-10-08 16:45 : production → 1b11fea (sync main-draft) [Superseded]
...
```

**Utilité** :
- Audit trail complet
- Voir qui a approuvé (nom reviewer)
- Voir délai entre staging et production
- Rollback : Re-run deployment précédent

---

## Rollback Production

### Quand Rollback ?

**Situations** :
- Bug critique détecté production après déploiement
- Régression fonctionnelle majeure
- Performance dégradée
- Erreur 500 site production

### Procédure Rollback (2-5 minutes)

**Étape 1** : Identifier version stable précédente

```
Dashboard Deployments
→ Environment: production
→ Historique : Voir déploiement précédent [Active] avant actuel
→ Exemple : 3c06ca1 (rollback strict) était stable
```

**Étape 2** : Re-run deployment

```
1. Cliquer déploiement stable précédent (3c06ca1)
2. Cliquer "Re-run all jobs" (icône en haut à droite)
3. Confirmation : "Re-run workflow?"
4. Cliquer "Re-run jobs"
```

**Étape 3** : Approuver rollback

```
1. Notification "Deployment to production pending" (rollback 3c06ca1)
2. Approuver immédiatement (pas de review nécessaire, version connue stable)
```

**Étape 4** : Vérifier production restaurée

```
1. Ouvrir https://alexmacapple.github.io/span-sg/
2. Vérifier version affichée (footer ou CHANGELOG)
3. Tester fonctionnalité qui était cassée
4. Confirmer bug résolu
```

**Durée totale** : 2-5 minutes (vs 10-15 minutes rebuild classique)

**Avantage** : Pas de rebuild CI/CD, réutilisation artifacts précédents

---

## Notifications

### Configuration Email

**Par défaut** : Notifications actives

**Vérifier configuration** :

```
GitHub → Settings (profil) → Notifications
→ Email notification preferences
→ ☑ Actions: Deployment review requested
```

**Fréquence attendue** :
- 5-10 notifications/semaine (selon activité contributeurs)
- Peak : Fin trimestre (rapports SPAN)
- Creux : Été, vacances

### Notifications Slack (optionnel)

**Si souhaité** : Webhook Slack configurable

```yaml
# .github/workflows/build.yml
- name: Notify Slack deployment pending
  uses: 8398a7/action-slack@v3
  with:
    status: pending
    text: "Deployment production en attente @chef-snum"
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

**Nécessite** : Configuration Slack webhook (demander admin GitHub)

---

## FAQ

### Q1 : Que se passe-t-il si j'ignore notification ?

**R** : Déploiement reste "Pending approval" indéfiniment. Aucune limite temporelle.

Contributions ultérieures s'accumulent en staging. Vous approuvez quand prêt (batch).

---

### Q2 : Puis-je déléguer approval à quelqu'un ?

**R** : Oui, demander admin GitHub ajouter reviewer supplémentaire :

```
Settings → Environments → production → Required reviewers
→ Add: [username_adjoint]
```

N'importe quel reviewer peut alors approuver (pas besoin tous approuver).

---

### Q3 : Combien de temps prend déploiement après approval ?

**R** : 2-5 minutes automatique.

Étapes :
1. Approval (vous)
2. GitHub Actions déclenché (Job: deploy-production)
3. Clone gh-pages branch
4. Copy artifacts (site HTML + PDF)
5. Git push gh-pages
6. CloudFlare CDN propagation (< 1 min)

Total : 2-5 minutes.

---

### Q4 : Puis-je annuler approval après avoir cliqué ?

**R** : Non, approval irréversible. Déploiement démarre immédiatement.

Si erreur détectée après : Faire rollback (procédure ci-dessus, 2-5 min).

---

### Q5 : Que faire si E2E tests échouent ?

**R** : Déploiement staging n'aura pas lieu (fail-fast).

Vous ne recevrez PAS de notification approval car job deploy-staging nécessite build-and-test success.

Validateurs corrigent tests, nouveau push main, nouveau build.

---

### Q6 : Puis-je voir diff staging vs production ?

**R** : Oui, outils :

**Option 1 : GitHub Compare** :
```
https://github.com/Alexmacapple/span-sg/compare/production...staging

# Voir commits pas encore en production
```

**Option 2 : Visual diff** (optionnel) :
```bash
# Percy.io ou Chromatic (tools visuels)
# Nécessite configuration externe (payant)
```

**Option 3 : Manuel** :
```
1. Ouvrir /draft/ (staging)
2. Ouvrir / (production) dans onglet séparé
3. Comparer visuellement côte-à-côte
```

---

### Q7 : Combien de contributions attendre avant approuver batch ?

**R** : Votre décision, basée sur stratégie :

**Stratégie fréquente** (recommandé début) :
- Approuver tous les vendredis (releases hebdomadaires)
- Accumulation 2-5 contributions/semaine

**Stratégie groupée** :
- Approuver fin trimestre (releases trimestrielles)
- Accumulation 20-50 contributions

**Stratégie mixte** :
- Hotfix : Immédiat (< 1h)
- Normal : Hebdomadaire (vendredis)
- Batch : Trimestriel (rapports SPAN)

---

### Q8 : Que faire si staging /draft/ inaccessible (404) ?

**R** : Vérifier :

1. **URL correcte** : https://alexmacapple.github.io/span-sg/draft/ (pas /draft sans trailing slash)
2. **Accès org-only** : Connecté GitHub avec compte org (pas mode incognito)
3. **Déploiement staging réussi** : Vérifier GitHub Actions logs

Si toujours inaccessible : Contacter validateurs (Bertrand/Alex).

---

### Q9 : Puis-je approuver depuis mobile ?

**R** : Oui, interface GitHub mobile fonctionne.

App GitHub Mobile :
- iOS : https://apps.apple.com/app/github/id1477376905
- Android : https://play.google.com/store/apps/details?id=com.github.android

Notifications push + approval possible mobile.

---

### Q10 : Quel délai attendre avant approuver (sécurité) ?

**R** : Configurable via "Wait timer" environment production.

**Actuellement** : 0 minutes (approval immédiat possible)

**Optionnel** : Configurer 30-60 min safety delay :

```
Settings → Environments → production
→ Wait timer: 60 minutes
```

Empêche approval < 1h après staging deploy (temps reflection).

---

## Métriques et Reporting

### Métriques personnelles

**Dashboard personnel** :

```bash
# Nombre approvals/mois
gh api repos/Alexmacapple/span-sg/deployments \
  --jq '.[] | select(.environment=="production") | select(.created_at | startswith("2025-10")) | length'

# Délai moyen staging → production
# (Nécessite script custom, ou Insights GitHub)
```

**Insights GitHub** (Admin uniquement) :
- Settings → Insights → Deployments
- Frequency, lead time, success rate

---

## Support et Contacts

### Contacts techniques

| Rôle | Personne | Email | Disponibilité |
|------|----------|-------|---------------|
| Validateur | Bertrand | @bertrand | Sous 48h |
| Validateur | Alex | @alex | Sous 48h |
| Admin GitHub | [Nom admin] | admin@... | Sous 24h |

### Ressources documentation

- [ADR-009 : Migration GitHub Environments](adr/009-migration-github-environments.md)
- [CONTRIBUTING.md](https://github.com/Alexmacapple/span-sg/blob/main/CONTRIBUTING.md)
- [GitHub Deployments Documentation](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)

---

## Annexe : Checklist Approval Complète

```markdown
## Checklist Approval Déploiement Production

Date: _____________
Commit SHA: _____________
Contributeur(s): _____________

### 1. Review Staging (5-10 min)

- [ ] Ouvrir https://alexmacapple.github.io/span-sg/draft/
- [ ] Tester navigation menu latéral (6 modules services)
- [ ] Ouvrir 2-3 modules (ex: SIRCOM, SNUM)
- [ ] Vérifier tableau Synthèse (scores cohérents, badges visibles)
- [ ] Télécharger exports/span-sg.pdf
- [ ] Ouvrir PDF (metadata OK, contenu lisible)
- [ ] Comparer staging vs production (aucune régression visuelle)

### 2. Vérifier Logs CI/CD (2-3 min)

- [ ] Ouvrir GitHub Actions : https://github.com/Alexmacapple/span-sg/actions
- [ ] Workflow "Build and Deploy" : Status ✅ Success
- [ ] Job build-and-test : Tous steps ✅
- [ ] Linting (Black + Ruff) : ✅
- [ ] Security (Bandit + Safety) : ✅
- [ ] Tests (33 unitaires, coverage 89%+) : ✅
- [ ] E2E tests (9 scenarios) : ✅
- [ ] Build HTML DSFR (strict mode) : ✅
- [ ] Generate PDF (metadata enrichies) : ✅
- [ ] Job deploy-staging : ✅ Deployed to /draft/
- [ ] Aucune erreur bloquante dans logs

### 3. Décision

- [ ] **Approuver** : Staging OK, logs OK, aucune régression
- [ ] **Rejeter** : Problème détecté (commentaire : ________________)
- [ ] **Différer** : Attendre accumulation (prochaine review : __________)

### 4. Post-Approval (si approuvé)

- [ ] Attendre notification "Deployment to production succeeded" (2-5 min)
- [ ] Vérifier https://alexmacapple.github.io/span-sg/ accessible
- [ ] Test rapide navigation production (1 min)
- [ ] Confirmer déploiement réussi

---

**Signature** : _____________
**Date/Heure** : _____________
```

---

**Dernière mise à jour** : 2025-10-22
**Version** : 1.0.0
**Auteur** : Claude Code
