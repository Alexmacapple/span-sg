# Workflow Git - Branches `draft` et `main`

**Projet** : SPAN SG (Schéma Pluriannuel d'Accessibilité Numérique)
**Date** : 30 septembre 2025
**Version** : 1.0

---

## Concept général

Le projet SPAN SG utilise un **workflow Git à 2 branches principales** pour séparer le travail en cours de la version officielle :

- **`draft`** : Environnement de prévisualisation et validation
- **`main`** : Version officielle et stable en production

Cette architecture garantit que la production reste stable tout en permettant un développement continu et collaboratif.

---

## Branche `draft` - Preview privée

### Rôle
Environnement de **prévisualisation et validation** avant publication officielle.

### Caractéristiques
- **État** : Travail en cours, peut contenir des bugs mineurs
- **Accès** : Privé, réservé aux membres de l'organisation GitHub
- **Fréquence MAJ** : Continue (quotidienne, voire plusieurs fois par jour)
- **Validateurs** : Bertrand, Alex (revues techniques)
- **Tags** : Aucun

### Utilisations principales
1. Recevoir toutes les nouvelles modifications via Pull Requests
2. Permettre aux validateurs de **revoir le contenu** avant production
3. Tester le rendu final sur une **preview privée**
4. Itérer rapidement sans impacter la production
5. Servir de base pour les formations et démonstrations internes

### Déploiement automatique
- **URL preview** : `https://span-sg.github.io/span-sg/draft/`
- **Accès** : Membres de l'organisation GitHub uniquement (paramètre org-only)
- **CI/CD** : Build + déploiement automatique à chaque push sur `draft`
- **Temps de déploiement** : 2-3 minutes après le push

### Workflow type avec draft
```
1. Référent service crée branche feature/update-sircom
         ↓
2. Modifie son module docs/modules/sircom.md
         ↓
3. Crée Pull Request vers draft
         ↓
4. Revue Bertrand/Alex sur https://.../draft/
         ↓
5. Demande corrections si nécessaire
         ↓
6. Merge dans draft
         ↓
7. Preview mise à jour automatiquement (CI)
```

### Commandes Git courantes
```bash
# Checkout sur draft
git checkout draft
git pull origin draft

# Créer une branche feature depuis draft
git checkout -b feature/update-sircom

# Après modifications, push et créer PR vers draft
git add docs/modules/sircom.md
git commit -m "feat(sircom): ajoute 3 actions au plan 2025"
git push -u origin feature/update-sircom
# Créer PR sur GitHub : feature/update-sircom → draft
```

---

## Branche `main` - Production officielle

### Rôle
Version **officielle et stable** accessible à tous (ou selon politique d'accès).

### Caractéristiques
- **État** : Stable, testé, validé
- **Accès** : Public ou selon politique organisation
- **Fréquence MAJ** : Mensuelle (releases planifiées)
- **Validateurs** : Bertrand, Alex + Yves (sponsor)
- **Tags** : v1.0.0, v1.1.0, v2.0.0 (releases)

### Utilisations principales
1. Contenir uniquement le code **validé et approuvé**
2. Servir la version **publique/officielle** du SPAN SG
3. Marquer les releases avec tags sémantiques
4. Garantir la **stabilité** (pas de travaux en cours)
5. Base pour la communication officielle (direction, services)

### Déploiement automatique
- **URL production** : `https://span-sg.github.io/span-sg/`
- **Accès** : Public (ou selon paramétrage organisation)
- **CI/CD** : Build + déploiement automatique à chaque push sur `main`
- **Artefacts** : PDF d'archive joint aux releases GitHub

### Workflow type vers main
```
1. Contenu validé et stable sur draft
         ↓
2. Création Pull Request draft → main
         ↓
3. Review finale + présentation à Yves (sponsor)
         ↓
4. Validation GO/NO-GO sponsor
         ↓
5. Merge dans main
         ↓
6. Tag version (ex: v1.0.0)
         ↓
7. Production mise à jour automatiquement (CI)
         ↓
8. Création release GitHub avec PDF joint
```

### Commandes Git pour release
```bash
# Préparer la release sur draft
git checkout draft
# ... ajuster CHANGELOG.md, versions ...
git add CHANGELOG.md
git commit -m "chore: prepare release v1.0.0"
git push origin draft

# Créer PR draft → main sur GitHub
# Après validation et merge :

git checkout main
git pull origin main

# Créer tag annoté
git tag -a v1.0.0 -m "Release SPAN SG v1.0.0"
git push origin v1.0.0

# Créer release GitHub avec assets (PDF)
```

---

## Flux complet (3 niveaux de branches)

```
┌──────────────────┐
│   feature/*      │  Branches de travail individuelles
│                  │  (feature/update-sircom, feature/fix-typo, etc.)
└────────┬─────────┘
         │ Pull Request
         ↓
┌──────────────────┐
│      draft       │  Preview privée + validation technique
│                  │  URL : https://.../draft/
│                  │  Validateurs : Bertrand, Alex
└────────┬─────────┘
         │ Pull Request (mensuelle)
         │ + Validation sponsor
         ↓
┌──────────────────┐
│      main        │  Production officielle + releases
│                  │  URL : https://.../ (racine)
│                  │  Tags : v1.0.0, v1.1.0, v2.0.0...
└──────────────────┘
```

---

## Tableau comparatif détaillé

| Aspect | `draft` | `main` |
|--------|---------|--------|
| **État du code** | Travail en cours | Stable et validé |
| **Accès preview** | Privé (org-only) | Public (ou selon config) |
| **URL** | `/draft/` | `/` (racine) |
| **Validateurs** | Bertrand, Alex | + Yves (sponsor) |
| **Fréquence MAJ** | Continue (quotidien) | Mensuelle (releases) |
| **Tags Git** | Aucun | v1.0.0, v1.1.0... |
| **Risque bugs** | Possible (toléré) | Très faible (testé) |
| **CI/CD** | Build + deploy draft/ | Build + deploy racine |
| **Artefacts** | Temporaires (90j) | Permanents (releases) |
| **Communication** | Interne équipe | Officielle (direction) |
| **Rollback** | Facile (revert commit) | Évité (hotfix préféré) |

---

## Pourquoi cette architecture ?

### Avantages

#### 1. **Sécurité**
- Production protégée par validation multi-niveaux
- Pas de modification directe sur `main`
- Branche `main` protégée (settings GitHub)

#### 2. **Qualité**
- Double validation : technique (Bertrand/Alex) + sponsor (Yves)
- Possibilité de tester sur preview avant publication
- Détection bugs avant production

#### 3. **Transparence**
- Preview permet feedback visuel avant publication
- Historique Git clair et tracé
- Décisions documentées (GO/NO-GO)

#### 4. **Traçabilité**
- Releases tagguées sur `main` (v1.0.0, v1.1.0...)
- Changelog associé à chaque version
- Artefacts PDF archivés par version

#### 5. **Collaboration**
- Équipe peut travailler en parallèle sur `draft`
- Pas de risque de casser la production
- Référents services autonomes (PR vers draft)

### Cas d'usage concret

**Scénario : Mise à jour module SAFI**

1. **Lundi** : Référent SAFI crée branche `feature/update-safi`
2. **Lundi** : Modifie `docs/modules/safi.md`, ajoute 3 actions au plan 2025
3. **Lundi** : Crée PR vers `draft`, CI vérifie (scoring, liens)
4. **Mardi** : Bertrand revoit la PR sur preview `https://.../draft/modules/safi/`
5. **Mardi** : Demande ajustements (budget à préciser)
6. **Mercredi** : Référent SAFI corrige, push dans la même branche
7. **Mercredi** : Bertrand approuve, merge dans `draft`
8. **Mercredi** : Preview draft mise à jour automatiquement
9. **Fin du mois** : Revue globale, PR `draft → main`
10. **Fin du mois** : Présentation à Yves, validation GO
11. **Fin du mois** : Merge `draft → main`, tag `v1.1.0`
12. **Fin du mois** : Production mise à jour, PDF v1.1.0 publié

**Résultat** : Module SAFI amélioré en production après validation complète, sans jamais mettre en risque la stabilité de `main`.

---

## Configuration technique

### GitHub Actions (`.github/workflows/build.yml`)

Le workflow CI/CD déploie automatiquement selon la branche :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Calculate SPAN scores
        run: python scripts/calculate_scores.py
      - name: Build site
        run: mkdocs build
      - name: Generate PDF
        run: mkdocs build --config-file mkdocs-pdf.yml
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: span-site
          path: |
            site/
            exports/

  deploy_draft:
    if: github.ref == 'refs/heads/draft'
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy draft to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages
          destination_dir: draft        # ← Déploie dans /draft/
          force_orphan: true

  deploy_main:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy production to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages      # ← Déploie à la racine
          force_orphan: true
```

### Résultat déploiement

Branche `gh-pages` (GitHub Pages) :
```
gh-pages/
├── index.html              # Production (depuis main)
├── modules/
├── synthese.html
└── draft/                  # Preview (depuis draft)
    ├── index.html
    ├── modules/
    └── synthese.html
```

**Accès** :
- Production : `https://span-sg.github.io/span-sg/`
- Preview : `https://span-sg.github.io/span-sg/draft/`

---

## Protections et bonnes pratiques

### Protection branche `main`

Sur GitHub → Settings → Branches → Add rule :
- **Branch name pattern** : `main`
- [x] Require a pull request before merging
- [x] Require approvals (1 minimum)
- [x] Require status checks to pass (CI)
- [x] Include administrators (même les admins passent par PR)

### Bonnes pratiques

#### Pour les contributeurs (référents services)
- Toujours créer une branche `feature/` depuis `draft`
- Faire des PR vers `draft` (jamais vers `main` directement)
- Commits atomiques avec messages clairs
- Tester localement avec `docker compose up` avant PR

#### Pour les validateurs (Bertrand, Alex)
- Revoir chaque PR sur la preview `draft`
- Vérifier checklist : 31 points, front-matter, liens, secrets
- Demander corrections via commentaires GitHub
- Approuver uniquement si qualité suffisante

#### Pour le sponsor (Yves)
- Valider uniquement les PR `draft → main`
- Focus stratégie (pas technique)
- GO/NO-GO documenté dans `decisions/`

---

## Gestion des urgences

### Hotfix (correction critique en production)

Si bug critique détecté sur `main` (production) :

```bash
# 1. Créer branche hotfix depuis main
git checkout main
git pull origin main
git checkout -b hotfix/fix-broken-link

# 2. Corriger le bug
# ... éditer fichiers ...

# 3. Commit et push
git add .
git commit -m "fix: corrige lien cassé page synthèse"
git push -u origin hotfix/fix-broken-link

# 4. Créer PR hotfix → main (validation rapide)
# 5. Après merge, tag patch v1.0.1
git checkout main
git pull origin main
git tag -a v1.0.1 -m "Hotfix: lien synthèse"
git push origin v1.0.1

# 6. Backport vers draft pour synchroniser
git checkout draft
git cherry-pick <commit-hotfix>
git push origin draft
```

**Délai cible hotfix** : < 24h (validation accélérée)

---

## Calendrier type de releases

### Rythme mensuel recommandé

**Semaine 1-3** : Développement continu sur `draft`
- Référents services soumettent PRs
- Validations techniques au fil de l'eau
- Preview draft mise à jour en continu

**Semaine 4** : Préparation release
- Lundi : Freeze `draft` (pas de nouveau merge)
- Mardi : Review globale Bertrand/Alex
- Mercredi : Corrections finales si nécessaire
- Jeudi : Présentation Yves + validation GO/NO-GO
- Vendredi : Merge `draft → main`, tag, release GitHub

**Début mois suivant** : Communication
- Email direction
- Rapport mensuel (évolution scores)
- Annonce interne services

---

## Références

- **PRD v3.3** : Section 4 "Workflow Git simplifié"
- **CLAUDE.md** : Section "Branches et déploiements"
- **README.md** : Section "Checklist première release"
- **Roadmap** : Stories S4-03 (tag) et S4-04 (publication)

---

## Contact

**Questions workflow Git** :
- Bertrand (@bertrand) : Validation technique
- Alex (@alex) : Validation technique
- Alexandra (@alexandra) : Coordination releases

**Support Git** :
- Documentation : `CONTRIBUTING.md`
- Formation : `docs/formation/git-basics.md`
- Office hours : Jeudis 14h-15h (lien visio dans README)

---

**Document créé le** : 30 septembre 2025
**Version** : 1.0
**Statut** : Validé

*Ce document sera mis à jour en cas d'évolution du workflow.*
