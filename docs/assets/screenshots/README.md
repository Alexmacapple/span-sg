# Guide Screenshots - SPAN SG

Instructions pour capturer, optimiser et ajouter des screenshots à la documentation SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-22
Public cible: Contributeurs documentation

---

## Objectif

Les screenshots servent à :
1. Illustrer workflows GitHub (PR, Actions, Issues)
2. Documenter interface MkDocs DSFR
3. Montrer composants DSFR en action
4. Faciliter onboarding contributeurs débutants

---

## Checklist Capture

Avant de capturer un screenshot, vérifier :

- [ ] Nettoyer l'écran (fermer onglets inutiles, masquer dock/barre tâches)
- [ ] Résolution écran : 1920x1080 ou supérieur
- [ ] Zoom navigateur : 100% (pas de zoom excessif)
- [ ] Thème : Clair (éviter dark mode pour cohérence)
- [ ] Masquer données sensibles (tokens, emails, clés API)
- [ ] Inclure contexte (URL visible, breadcrumb navigation)

---

## Catégories de Screenshots

### 1. GitHub Interface

**Cas d'usage** :
- Création Pull Request
- Review PR (commentaires, approvals)
- GitHub Actions (logs, artifacts, jobs)
- Issues tracking

**Exemple capture** :

```
URL visible : https://github.com/Alexmacapple/span-sg/pull/42
Zones importantes :
- Sélecteur branches (base: draft, compare: feature/...)
- Bouton "Create Pull Request"
- Description PR (template)
- Reviewers (Bertrand, Alex)
```

**Nom fichier** : `github-pr-creation-1920x1080.png`

---

### 2. GitHub Actions CI/CD

**Cas d'usage** :
- Logs build (succès/échec)
- Durée jobs
- Artifacts téléchargeables
- Tests E2E/Accessibility

**Exemple capture** :

```
Workflow : build-deploy-draft
Job : Calculate SPAN scores
Logs :
  - python scripts/calculate_scores.py
  - Erreurs de périmètre: ...
  - Exit code 2
```

**Nom fichier** : `ci-logs-calculate-scores-1920x1080.png`

---

### 3. MkDocs Local

**Cas d'usage** :
- Interface `mkdocs serve` localhost:8000
- Rendu thème DSFR
- Navigation sidebar
- Tableaux DSFR wrappés

**Exemple capture** :

```
URL : http://localhost:8000/span-sg/modules/sircom/
Zones importantes :
- Header DSFR (SPAN SG, Secrétariat Général)
- Navigation latérale (modules services)
- Contenu module avec badges DSFR
- Footer liens légaux
```

**Nom fichier** : `mkdocs-serve-module-sircom-1440x900.png`

---

### 4. Composants DSFR

**Cas d'usage** :
- Badges statut (success, info, warning, error)
- Tableaux responsive (`<div class="fr-table">`)
- Accordéons
- Alertes (alert, info)

**Exemple capture** :

```
Page : docs/synthese.md
Composant : Tableau synthèse SPAN avec badges
HTML :
  <div class="fr-table">
    <table>
      <tr>
        <td>SIRCOM</td>
        <td><p class="fr-badge fr-badge--success">Validé</p></td>
      </tr>
    </table>
  </div>
```

**Nom fichier** : `dsfr-table-synthese-badges-1920x1080.png`

---

## Workflow Capture Détaillé

### Étape 1 : Préparation

**macOS** :
```bash
# 1. Nettoyer bureau (masquer icônes)
defaults write com.apple.finder CreateDesktop -bool false
killall Finder

# 2. Réduire dock (option UI ou cmd)
# 3. Ouvrir Chrome/Safari en mode fenêtre (pas plein écran)
# 4. Ajuster taille fenêtre : 1920x1080 ou 1440x900
```

**Windows** :
```bash
# 1. Masquer barre tâches (option UI)
# 2. Fermer notifications (Win+A → Désactiver)
# 3. Ouvrir Edge/Chrome en mode fenêtre
# 4. Ajuster résolution si besoin (Paramètres Affichage)
```

---

### Étape 2 : Capture

**macOS (natif)** :
```bash
# Sélection zone (sauvegarde Bureau)
Cmd+Shift+4

# Fenêtre entière (avec ombre)
Cmd+Shift+4, puis Espace, clic fenêtre

# Options avancées (timer 5s)
Cmd+Shift+5 → Options → Timer 5 secondes
```

**Windows (natif)** :
```bash
# Outil Capture
Win+Shift+S → Sélectionner zone

# Enregistrer depuis Presse-papiers
Win+V → Coller dans Paint → Enregistrer PNG
```

**Outils tiers (recommandés)** :

| Outil | OS | Avantages | Lien |
|-------|----|-----------| -----|
| CleanShot X | macOS | Annotations, scrolling, cloud | [cleanshot.com](https://cleanshot.com/) |
| ShareX | Windows | Open source, upload, scripts | [getsharex.com](https://getsharex.com/) |
| Flameshot | Linux | GUI intuitive, annotations | [flameshot.org](https://flameshot.org/) |

---

### Étape 3 : Optimisation

**Compression PNG** :

```bash
# Option 1 : pngquant (perte visuelle imperceptible)
pngquant --quality=80-95 screenshot.png -o screenshot-opt.png

# Option 2 : optipng (sans perte)
optipng -o7 screenshot.png

# Option 3 : ImageMagick (resize + compress)
convert screenshot.png -resize 1920x1080 -quality 85 screenshot-opt.png

# Vérifier poids fichier (objectif <500 KB)
ls -lh screenshot-opt.png
```

**Outils GUI** :
- **macOS** : [ImageOptim](https://imageoptim.com/) (drag-and-drop)
- **Windows** : [PNGGauntlet](https://pnggauntlet.com/) (batch processing)
- **Web** : [TinyPNG](https://tinypng.com/) (max 5 MB, API disponible)

---

### Étape 4 : Nommage et Placement

**Convention nommage** :

```
{categorie}-{description}-{resolution}.png

Exemples valides :
✅ github-pr-creation-1920x1080.png
✅ ci-logs-e2e-tests-1440x900.png
✅ mkdocs-serve-localhost-1920x1080.png
✅ dsfr-badge-success-800x600.png

Exemples invalides :
❌ screenshot1.png (pas de contexte)
❌ image_final_v2.png (versionning manuel)
❌ Capture d'écran 2025-10-22.png (timestamp machine)
```

**Placement fichier** :

```bash
# Copier dans dossier assets/screenshots/
cp ~/Desktop/screenshot-opt.png docs/assets/screenshots/github-pr-creation-1920x1080.png

# Vérifier poids fichier
du -sh docs/assets/screenshots/github-pr-creation-1920x1080.png
# Attendu : < 500 KB
```

---

## Référencement dans Documentation

### Syntaxe Markdown

**Basique (obligatoire)** :

```markdown
![Création Pull Request sur GitHub avec sélection base draft et compare feature](../assets/screenshots/github-pr-creation-1920x1080.png)
```

**Avec légende** :

```markdown
![Interface GitHub Actions logs montrant succès build draft en 6 minutes](../assets/screenshots/ci-logs-build-success-1920x1080.png)

*Figure 1 : Logs GitHub Actions après merge PR vers draft (durée totale : 6min 12s)*
```

**Avec lien cliquable** :

```markdown
[![Tableau synthèse SPAN avec badges DSFR validé/en cours](../assets/screenshots/dsfr-table-synthese-1920x1080.png)](https://alexmacapple.github.io/span-sg/synthese/)

*Cliquer pour voir la synthèse en direct*
```

---

## Checklist Accessibilité RGAA

Avant commit, valider :

- [ ] **Alt text descriptif** : Décrit contenu image sans contexte externe (RGAA 1.1.1)
  ```markdown
  ✅ ![Création PR GitHub avec base draft et compare feature/update-sircom](...)
  ❌ ![Screenshot PR](...)
  ❌ ![](screenshot.png) # Alt text vide = ÉCHEC RGAA
  ```

- [ ] **Contraste suffisant** : Texte dans image lisible (RGAA 3.2.1)
  - Vérifier avec [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
  - Ratio minimum : 4.5:1 (texte normal), 3:1 (texte large)

- [ ] **Taille fichier optimale** : < 500 KB (performance)
  ```bash
  du -h docs/assets/screenshots/*.png | awk '$1 > 500 { print "❌", $2, "trop lourd" }'
  ```

- [ ] **Contexte fourni** : Légende ou texte adjacent explique image
  ```markdown
  ## Création Pull Request

  Pour créer une PR, suivre ces étapes :

  ![Interface GitHub création PR](../assets/screenshots/github-pr-creation.png)

  1. Sélectionner base : `draft`
  2. Sélectionner compare : `feature/update-sircom`
  ```

---

## Exemples Cas d'Usage

### Exemple 1 : Workflow GitHub PR

**Fichiers nécessaires** :
1. `github-pr-open-1920x1080.png` : Liste PRs ouvertes
2. `github-pr-creation-1920x1080.png` : Formulaire création PR
3. `github-pr-review-comments-1920x1080.png` : Commentaires validateur
4. `github-pr-merge-1920x1080.png` : Bouton merge PR

**Utilisation dans docs/onboarding-visual.md** :

```markdown
## Étape 2 : Créer Pull Request

Après avoir modifié votre module, créer une PR vers `draft` :

![Formulaire création Pull Request GitHub avec sélection branches](../assets/screenshots/github-pr-creation-1920x1080.png)

**Champs à remplir** :
- Base : `draft` (branche cible)
- Compare : `feature/update-sircom` (votre branche)
- Title : `feat(sircom): ajoute 3 actions plan 2025`
- Description : Template auto-rempli
```

---

### Exemple 2 : CI/CD Logs

**Fichiers nécessaires** :
1. `ci-logs-lint-success-1920x1080.png` : Linting OK (Black+Ruff)
2. `ci-logs-test-failed-1920x1080.png` : Tests échoués
3. `ci-logs-security-warnings-1920x1080.png` : Bandit warnings
4. `ci-artifacts-exports-1920x1080.png` : Artifacts téléchargeables

**Utilisation dans docs/contributing.md** :

```markdown
## Consulter Logs CI

En cas d'échec build, consulter les logs GitHub Actions :

![Logs GitHub Actions montrant échec tests avec exit code 2](../assets/screenshots/ci-logs-test-failed-1920x1080.png)

**Interpréter l'erreur** :
- Exit code 2 : Erreur périmètre (total critères ≠ 0 ou 33)
- Solution : Vérifier nombre de balises `<!-- CHECKLIST -->`
```

---

## Maintenance Screenshots

### Quand Mettre à Jour

Refaire screenshots lors de :
- Migration UI GitHub (redesign interface)
- Mise à jour thème DSFR (changements visuels)
- Refonte workflows CI/CD (nouveaux jobs)
- Changement URL production (migration repo)

### Versioning Assets

Conserver versions précédentes avec suffix :

```bash
# Version initiale (v1.0)
github-pr-creation-v1.0-1920x1080.png

# Après redesign GitHub 2025 (v1.1)
github-pr-creation-v1.1-1920x1080.png
```

---

## Ressources

- [RGAA 4.1 - Images](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#topic-images)
- [DSFR - Médias](https://www.systeme-de-design.gouv.fr/elements-d-interface/medias)
- [Assets General Guide](../README.md)
- [GIFs Guide](../gifs/README.md)
