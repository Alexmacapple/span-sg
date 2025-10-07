# Options pour la preview privée GitHub Pages

**Date** : 01/10/2025
**Contexte** : S2-01 GitHub Actions CI/CD

---

## Situation actuelle

**Repo** : Public
**GitHub Pages** : Désactivé (pas de preview publique avant validation)
**Preview** : Revue locale/PDF (voir `docs/dev-local.md`)

**Problème** : Les URLs sont **accessibles publiquement** par tout le monde (pas de restriction d'accès).

**PRD initial (Section 5.1)** prévoyait :
> Preview privée via GitHub Pages (organisation uniquement)

Cette configuration nécessite **repo privé + GitHub Enterprise/Pro**, incompatible avec plan Free actuel.

---

## Option 1 : Retour repo privé + GitHub Pro

### Configuration

```bash
# 1. Passer le repo en privé
gh repo edit Alexmacapple/span-sg-repo --visibility private --accept-visibility-change-consequences

# 2. Souscrire GitHub Pro (interface web)
# https://github.com/settings/billing/plans

# 3. Activer Pages avec restriction d'accès
# GitHub → Settings → Pages → Visibility → "Private" (membres org uniquement)
```

### Avantages

✅ **Confidentialité maximale** : Seuls les membres de l'organisation accèdent aux URLs
✅ **URLs partageable** : https://alexmacapple.github.io/span-sg-repo/draft/ (avec authentification GitHub)
✅ **Workflow inchangé** : CI/CD continue de fonctionner tel quel
✅ **GitHub native** : Pas de service tiers

### Inconvénients

❌ **Coût** : $4/mois par utilisateur (compte Pro)
❌ **Maintenance** : Gérer les accès membres organisation
⚠️ **Engagement** : Abonnement mensuel

### Cas d'usage idéal

- Contenu SPAN SG **confidentiel**
- Budget disponible ($48/an)
- Équipe de 5+ contributeurs nécessitant accès preview
- Preview partageable avec validateurs (Bertrand, Alex, Yves)

---

## Option 2 : Repo privé + Preview locale uniquement

### Configuration

```bash
# 1. Passer le repo en privé
gh repo edit Alexmacapple/span-sg-repo --visibility private --accept-visibility-change-consequences

# 2. Désactiver GitHub Pages (ou laisser 404)
# GitHub → Settings → Pages → Disable

# 3. Preview locale via Docker
docker compose up
# → http://localhost:8000

# 4. OU télécharger artefacts CI
# https://github.com/Alexmacapple/span-sg-repo/actions
# Télécharger "span-site" → Extraire → Ouvrir site/index.html
```

### Avantages

✅ **Gratuit** : Aucun coût supplémentaire
✅ **Confidentialité totale** : Site uniquement en local ou via artefacts CI
✅ **Repo privé** : Code et contenu protégés
✅ **CI fonctionnelle** : Artefacts (site + PDF) disponibles 90 jours

### Inconvénients

❌ **Pas d'URL partageable** : Impossible de donner lien preview à validateurs
❌ **Friction preview** : Chaque contributeur doit lancer Docker ou télécharger artefacts
❌ **Validation complexe** : Bertrand/Alex/Yves doivent télécharger artefacts manuellement
⚠️ **Pas de preview persistante** : Artefacts expirent après 90 jours

### Cas d'usage idéal

- Contenu SPAN SG **strictement confidentiel**
- Pas de budget
- Contributeurs techniques (à l'aise avec Docker/artefacts CI)
- Validation interne uniquement (pas besoin URL externe pour Yves)

---

## Option 3 : Garder repo public + Assumer contenu public

### Configuration

```bash
# Aucune action requise (configuration actuelle)
```

### Avantages

✅ **Gratuit** : GitHub Pages illimité pour repos publics
✅ **URLs partageable** : https://alexmacapple.github.io/span-sg-repo/draft/ (accessible sans compte)
✅ **Workflow simple** : CI/CD déploie automatiquement
✅ **Validation facile** : Validateurs accèdent preview par simple clic
✅ **SEO/Visibilité** : Site indexable par moteurs de recherche (si souhaité)

### Inconvénients

❌ **Aucune confidentialité** : Contenu SPAN SG visible par tous
❌ **Repo public** : Code et historique Git accessibles
⚠️ **Conformité** : Vérifier que contenu SPAN SG peut être public (pas de données sensibles)

### Cas d'usage idéal

- Contenu SPAN SG **acceptable en public** (données ouvertes, transparence)
- Pas de budget
- Besoin de partager facilement avec validateurs externes
- Communication publique assumée (accessibilité numérique = thème public)

### Correction documentation

Si cette option est retenue, mettre à jour PRD Section 5.1 :

```markdown
### 5.1 Accès preview public (Option C retenue)

**Principe** : GitHub Pages sert la prévisualisation publiquement (repo public).

**URLs** :
- Draft : https://alexmacapple.github.io/span-sg-repo/draft/
- Production : https://alexmacapple.github.io/span-sg-repo/

**Raison** : Plan GitHub Free nécessite repo public pour Pages gratuit.
Preview privée nécessiterait GitHub Pro ($4/mois).
```

---

## Option 4 : Repo privé + Vercel/Netlify avec password

### Configuration

#### Vercel

```bash
# 1. Passer repo en privé
gh repo edit Alexmacapple/span-sg-repo --visibility private --accept-visibility-change-consequences

# 2. Installer Vercel CLI
npm install -g vercel

# 3. Déployer avec protection password
vercel --prod
# Puis activer Password Protection dans dashboard Vercel
# → Settings → Password Protection → Enable
```

#### Netlify

```bash
# 1. Passer repo en privé
gh repo edit Alexmacapple/span-sg-repo --visibility private --accept-visibility-change-consequences

# 2. Connecter repo à Netlify
# https://app.netlify.com/start

# 3. Activer password (plan payant ou Basic Auth gratuit)
# Site settings → Access control → Password protection
```

### Avantages

✅ **Confidentialité partielle** : Protection par mot de passe
✅ **Repo privé** : Code protégé
✅ **URLs partageable** : https://span-sg.vercel.app/ (avec password)
✅ **Plan gratuit possible** : Vercel/Netlify Free avec limitations
✅ **Flexibilité** : Peut changer password facilement

### Inconvénients

❌ **Complexité** : Configuration service tiers (Vercel/Netlify)
❌ **Maintenance** : Gérer 2 plateformes (GitHub + Vercel/Netlify)
❌ **Password partagé** : Tous les validateurs ont le même mot de passe (pas d'authentification individuelle)
⚠️ **Limitations plan Free** : Bande passante limitée, pas de support
⚠️ **Dépendance externe** : Service tiers (si Vercel/Netlify down, preview inaccessible)

### Cas d'usage idéal

- Contenu SPAN SG **modérément confidentiel**
- Pas de budget pour GitHub Pro
- Besoin URL partageable avec validateurs
- À l'aise avec configuration services tiers

---

## Tableau comparatif

| Critère | Option 1<br>GitHub Pro | Option 2<br>Local uniquement | Option 3<br>Public | Option 4<br>Vercel/Netlify |
|---------|------------------------|------------------------------|--------------------|-----------------------------|
| **Coût** | 💰 $4/mois | ✅ Gratuit | ✅ Gratuit | ⚠️ Gratuit (limité) |
| **Confidentialité** | ✅✅✅ Maximale | ✅✅✅ Totale | ❌ Aucune | ✅✅ Password |
| **URL partageable** | ✅ Oui (auth GitHub) | ❌ Non | ✅ Oui (public) | ✅ Oui (password) |
| **Complexité setup** | ⚠️ Moyenne | ✅ Faible | ✅ Faible | ❌ Élevée |
| **Maintenance** | ⚠️ Gérer accès org | ✅ Aucune | ✅ Aucune | ❌ 2 plateformes |
| **CI/CD inchangé** | ✅ Oui | ✅ Oui | ✅ Oui | ❌ Config à adapter |
| **Validation facile** | ✅ URL + login GitHub | ❌ Télécharger artefacts | ✅ URL direct | ⚠️ URL + password |
| **Conformité RGPD** | ✅ Conforme | ✅ Conforme | ⚠️ Si contenu public OK | ✅ Conforme |

---

## Recommandations

### Si budget disponible
→ **Option 1** (GitHub Pro) : Solution native, intégration parfaite, gestion accès individuelle

### Si budget limité + contenu confidentiel
→ **Option 2** (Local uniquement) : Gratuit, sécurisé, mais friction validation

### Si contenu acceptable en public
→ **Option 3** (Public) : **Recommandé** - Gratuit, simple, validation facile
- ✅ Projet SPAN SG = accessibilité numérique (thème public)
- ✅ 31 points DINUM = référentiel public DINUM
- ✅ Transparence administration publique

### Si besoin compromis
→ **Option 4** (Vercel/Netlify) : Protection password, mais complexité supplémentaire

---

## Décision pour SPAN SG

**Option actuellement en place** : Sans Pages — revue locale/PDF (prépublication)

**Raison** :
1. Éviter toute exposition publique avant validation
2. Plan GitHub Free (pas de Pages privées)
3. Revue interne via `mkdocs serve` et PDF CI

**Action si changement requis** :
- Contacter Alexandra pour décision sponsor Yves
- Si confidentialité nécessaire → Option 1 (GitHub Pro) ou Option 2 (Local)

---

## Références

- **PRD v3.3** : Section 5.1 "Accès preview privé"
- **S2-01** : Configuration GitHub Actions + Pages
- **GitHub Docs** : [About GitHub Pages visibility](https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)
- **GitHub Pro** : https://github.com/pricing
- **Vercel Password Protection** : https://vercel.com/docs/security/deployment-protection/password-protection
- **Netlify Access Control** : https://docs.netlify.com/visitor-access/password-protection/

---

**Date de révision** : 01/10/2025
**Statut** : Option 3 (Public) retenue pour MVP
**Prochaine révision** : Semaine 4 (avant publication production)
