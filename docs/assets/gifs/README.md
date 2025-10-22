# Guide GIFs - SPAN SG

Instructions pour créer, optimiser et ajouter des GIFs animés à la documentation SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-22
Public cible: Contributeurs documentation

---

## Objectif

Les GIFs animés servent à :
1. Démontrer workflows complets (édition → PR → merge)
2. Tutoriels interactifs (onboarding contributeurs)
3. Tests E2E visuels (Selenium scenarios)
4. Builds MkDocs (génération site/PDF)

---

## Checklist Enregistrement

Avant d'enregistrer un GIF, vérifier :

- [ ] Nettoyer l'écran (fermer applications inutiles)
- [ ] Résolution : 1280x720 (compromis qualité/poids)
- [ ] FPS : 10-15 fps (fluidité sans lourdeur)
- [ ] Durée : 5-15 secondes maximum
- [ ] Préparer actions à l'avance (script mental)
- [ ] Masquer données sensibles (tokens, emails)
- [ ] Tester enregistrement 1 fois avant version finale

---

## Catégories de GIFs

### 1. Onboarding Contributeur

**Cas d'usage** :
- Édition module GitHub web (clic Edit → modification)
- Cochage critères DINUM (3 cases cochées)
- Création Pull Request (formulaire → submit)
- Review et merge (commentaires → approve → merge)

**Durée recommandée** : 10-15 secondes
**FPS recommandé** : 10 fps
**Nom fichier** : `onboarding-edit-module-10fps.gif`

---

### 2. Tests E2E

**Cas d'usage** :
- Selenium navigate (ouverture page → clic liens)
- Tests accessibilité (RGAA checks visibles)
- Validation formulaires (remplissage → submit)

**Durée recommandée** : 5-10 secondes
**FPS recommandé** : 15 fps (actions rapides)
**Nom fichier** : `e2e-selenium-navigation-15fps.gif`

---

### 3. Build MkDocs

**Cas d'usage** :
- `mkdocs serve` terminal (commande → output logs)
- Génération PDF (WeasyPrint progress)
- Docker compose up (container startup)

**Durée recommandée** : 8-12 secondes
**FPS recommandé** : 10 fps
**Nom fichier** : `build-mkdocs-serve-10fps.gif`

---

## Outils Recommandés

### Capture Écran → GIF

| Outil | OS | Avantages | Lien |
|-------|----|-----------| -----|
| ScreenToGif | Windows | Édition intégrée, codec efficace | [screentogif.com](https://www.screentogif.com/) |
| Kap | macOS | Léger, plugins, formats multiples | [getkap.co](https://getkap.co/) |
| LICEcap | Mac/Win | Simple, output direct GIF | [cockos.com/licecap](https://www.cockos.com/licecap/) |
| Peek | Linux | Natif Wayland/X11, minimal | [github.com/phw/peek](https://github.com/phw/peek) |

### Conversion Vidéo → GIF

**ffmpeg (ligne de commande)** :

```bash
# MP4 → GIF optimisé (palette 256 couleurs)
ffmpeg -i input.mp4 -vf "fps=10,scale=1280:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=256[p];[s1][p]paletteuse=dither=bayer:bayer_scale=5" output.gif

# Options expliquées :
# - fps=10 : 10 images/seconde
# - scale=1280:-1 : Largeur 1280px, hauteur auto
# - flags=lanczos : Filtre qualité haute
# - palettegen : Palette optimale pour vidéo
# - paletteuse : Appliquer palette avec dithering Bayer
```

---

## Workflow Création Détaillé

### Étape 1 : Préparation Environnement

**Script mental** :

```
Objectif : Démontrer édition module SIRCOM sur GitHub
Actions :
1. Naviguer https://github.com/Alexmacapple/span-sg/blob/draft/docs/modules/sircom.md
2. Cliquer icône Edit (crayon)
3. Scroller ligne 50 (critère 1.1.1)
4. Cocher case : - [ ] → - [x]
5. Scroll bas formulaire
6. Commit message : "feat(sircom): coche critère 1.1.1"
7. Cliquer "Commit changes"
Durée estimée : 12 secondes
```

**Nettoyage écran** :

```bash
# macOS : Masquer dock et menu
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock autohide-delay -float 1000
killall Dock

# Fermer onglets inutiles navigateur (garder 1 seul)
# Zoom navigateur : 90% (pour inclure plus de contexte)
```

---

### Étape 2 : Enregistrement

**Kap (macOS)** :

```bash
# 1. Lancer Kap (Cmd+Space → Kap)
# 2. Sélectionner zone (1280x720 recommandé)
# 3. Paramètres :
#    - FPS : 10
#    - Format : GIF
#    - Crop : On (ajuster zone précise)
# 4. Cliquer Record → Exécuter script mental
# 5. Stop (Cmd+Shift+5 ou icône menu)
# 6. Export GIF (Save As...)
```

**ScreenToGif (Windows)** :

```bash
# 1. Lancer ScreenToGif
# 2. Mode "Recorder" (Ctrl+N)
# 3. Ajuster fenêtre : 1280x720
# 4. FPS : 10 (slider)
# 5. Cliquer Record (F7) → Exécuter actions
# 6. Stop (F8) → Editor s'ouvre
# 7. Éditer si besoin (crop, vitesse, texte)
# 8. File → Save As → GIF
#    - Encoder : System.Drawing
#    - Quantization : Octree
#    - Colors : 256
```

**ffmpeg (depuis vidéo existante)** :

```bash
# Si vous avez déjà une vidéo MP4 (ex: OBS Studio)
ffmpeg -ss 00:00:02 -t 00:00:12 -i recording.mp4 \
  -vf "fps=10,scale=1280:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  onboarding-edit-module-10fps.gif

# Options :
# -ss 00:00:02 : Démarrer à 2s (skip intro)
# -t 00:00:12 : Durée 12s
# -i recording.mp4 : Fichier source
```

---

### Étape 3 : Optimisation

**gifsicle (ligne de commande)** :

```bash
# Installation
# macOS : brew install gifsicle
# Linux : apt install gifsicle
# Windows : choco install gifsicle

# Optimisation basique (niveau 3, perte minimale)
gifsicle -O3 input.gif -o output.gif

# Optimisation avancée (lossy compression 80%, 128 couleurs)
gifsicle -O3 --lossy=80 --colors=128 input.gif -o output.gif

# Réduction poids ~60-80% sans perte visible
# Vérifier poids avant/après
ls -lh input.gif output.gif
```

**ImageMagick (alternative)** :

```bash
# Réduire FPS (de 15 à 10 fps)
convert input.gif -fuzz 10% -layers Optimize output.gif

# Réduire résolution (de 1920x1080 à 1280x720)
convert input.gif -resize 1280x720 -fuzz 5% -layers Optimize output.gif

# Réduire palette couleurs (256 → 128)
convert input.gif -colors 128 -fuzz 5% -layers Optimize output.gif
```

**Outils GUI** :
- **ezgif.com** : Web (max 100 MB, gratuit, rapide)
  - Optimize GIF : Compression level 35-100
  - Resize : 1280x720
  - Speed : Ralentir/accélérer
- **RIOT** : Windows (batch processing, comparaison visuelle)

---

### Étape 4 : Validation Qualité

**Checklist technique** :

```bash
# Poids fichier (objectif < 2 MB)
du -h output.gif
# Attendu : 500 KB - 2 MB selon durée

# Dimensions (idéal 1280x720)
identify output.gif | head -n 1
# Attendu : GIF 1280x720 ...

# Nombre frames et FPS
identify -verbose output.gif | grep "Scene:"
# Attendu : Scene: XX of YY (FPS = YY/durée)

# Test visuel (ouvrir dans navigateur)
open output.gif  # macOS
start output.gif # Windows
xdg-open output.gif # Linux
```

**Validation UX** :

- [ ] Actions clairement visibles (pas flou)
- [ ] Durée acceptable (5-15s max)
- [ ] Loop infini fonctionne (pas freeze fin)
- [ ] Texte lisible (si présent dans UI)
- [ ] Pas de distractions (notifications, curseur erratique)

---

### Étape 5 : Nommage et Placement

**Convention nommage** :

```
{workflow}-{action}-{fps}.gif

Exemples valides :
✅ onboarding-create-pr-10fps.gif
✅ e2e-selenium-test-15fps.gif
✅ build-mkdocs-serve-10fps.gif
✅ pr-review-approve-10fps.gif

Exemples invalides :
❌ animation.gif (pas de contexte)
❌ test_final_v3.gif (versioning manuel)
❌ Recording 2025-10-22.gif (timestamp machine)
```

**Placement fichier** :

```bash
# Copier dans dossier assets/gifs/
cp ~/Desktop/output.gif docs/assets/gifs/onboarding-create-pr-10fps.gif

# Vérifier poids fichier (objectif < 2 MB)
du -sh docs/assets/gifs/onboarding-create-pr-10fps.gif
# Attendu : < 2 MB
```

---

## Référencement dans Documentation

### Syntaxe Markdown

**Basique (obligatoire)** :

```markdown
![Animation démonstration création Pull Request : édition module SIRCOM puis création PR vers draft](../assets/gifs/onboarding-create-pr-10fps.gif)
```

**Avec légende** :

```markdown
![Animation workflow contributeur complet : édition GitHub web, cochage 3 critères, création PR, attente review, merge automatique](../assets/gifs/onboarding-full-workflow-10fps.gif)

*Figure 1 : Workflow contributeur de bout en bout (durée réelle : 15 minutes, accéléré 10x)*
```

**Avec contexte textuel** :

```markdown
## Workflow Contributeur

Le processus de contribution suit ces étapes :

![Animation : ouvrir module → éditer → cocher critères → créer PR](../assets/gifs/onboarding-create-pr-10fps.gif)

1. **Édition module** : Cliquer icône Edit sur GitHub web
2. **Cochage critères** : Remplacer `[ ]` par `[x]`
3. **Commit** : Message descriptif (feat/fix/docs)
4. **Pull Request** : Base `draft`, compare `feature/...`

Durée estimée : 15 minutes par contribution.
```

---

## Checklist Accessibilité RGAA

Avant commit, valider :

- [ ] **Alt text descriptif** : Décrit actions dans GIF (RGAA 1.1.1)
  ```markdown
  ✅ ![Animation : édition module SIRCOM, cochage critères, création PR](...)
  ❌ ![GIF demo](...)
  ❌ ![](animation.gif) # Alt text vide = ÉCHEC RGAA
  ```

- [ ] **Durée raisonnable** : 5-15 secondes max (UX)
  - Si > 15s : découper en plusieurs GIFs
  - Éviter fatigue visuelle utilisateur

- [ ] **Pas de clignotement rapide** : < 3 flashs/seconde (RGAA 13.1.1)
  - Risque épilepsie si > 3 Hz
  - Vérifier transitions brusques (ex: modal popup)

- [ ] **Contrôle lecture** : Pas de lecture auto obligatoire (RGAA 4.8.1)
  - Markdown natif = OK (GIF loop = contrôle natif navigateur)
  - Éviter `<video autoplay>` sans contrôles

- [ ] **Contexte fourni** : Texte adjacent explique actions
  ```markdown
  ## Création Pull Request

  Le GIF ci-dessous montre le processus complet :

  ![Animation création PR](../assets/gifs/onboarding-create-pr-10fps.gif)

  **Étapes détaillées** :
  1. Éditer module sur GitHub
  2. Cocher critères DINUM
  3. Créer Pull Request vers draft
  ```

---

## Exemples Cas d'Usage

### Exemple 1 : Onboarding Contributeur Complet

**Fichier** : `onboarding-full-workflow-10fps.gif`
**Durée** : 12 secondes (workflow 15 minutes accéléré)
**Actions** :
1. Naviguer module SIRCOM
2. Cliquer Edit
3. Cocher 3 critères
4. Commit changes
5. Create Pull Request
6. (Optionnel) Review approval

**Utilisation dans docs/onboarding-visual.md** :

```markdown
## Parcours Contributeur Complet

Animation démonstrant le workflow de bout en bout :

![Animation : édition module SIRCOM sur GitHub web, cochage 3 critères DINUM, création Pull Request vers draft, attente review validateur, merge automatique](../assets/gifs/onboarding-full-workflow-10fps.gif)

**Détail des étapes** :

1. **Édition** (0-3s) : Clic Edit → Scroll critère
2. **Modification** (3-6s) : Cocher 3 cases `[x]`
3. **Commit** (6-9s) : Message + Create new branch
4. **Pull Request** (9-12s) : Base draft + Create PR

Durée réelle : 15 minutes pour contributeur débutant.
```

---

### Exemple 2 : Tests E2E Selenium

**Fichier** : `e2e-selenium-navigation-15fps.gif`
**Durée** : 8 secondes
**Actions** :
1. Ouvrir localhost:8000/span-sg/
2. Cliquer menu "SPAN (services)"
3. Cliquer "SIRCOM"
4. Scroller module
5. Vérifier badges DSFR visibles

**Utilisation dans docs/dev/api-reference.md** :

```markdown
## Tests E2E Visuels

Les scénarios Selenium naviguent l'interface MkDocs DSFR :

![Animation tests E2E : navigation menu SPAN services, ouverture module SIRCOM, scroll contenu, vérification badges DSFR](../assets/gifs/e2e-selenium-navigation-15fps.gif)

**Scénarios testés** :
- Navigation menu latéral
- Ouverture modules services
- Scroll page (test anchors)
- Badges DSFR visibles

Durée totale E2E : 300 secondes (9 scénarios).
```

---

## Maintenance GIFs

### Quand Refaire

Refaire GIFs lors de :
- Migration UI GitHub (redesign interface)
- Changement workflow CI/CD (nouveaux jobs)
- Refonte thème DSFR (changements visuels)
- Modification processus onboarding (nouveaux steps)

### Versioning Assets

Conserver versions précédentes avec suffix :

```bash
# Version initiale (v1.0)
onboarding-create-pr-v1.0-10fps.gif

# Après redesign GitHub 2025 (v1.1)
onboarding-create-pr-v1.1-10fps.gif
```

---

## Troubleshooting

### GIF trop lourd (> 2 MB)

**Solutions** :

```bash
# 1. Réduire FPS (de 15 à 10 fps)
gifsicle --delay=10 input.gif -o output.gif  # 10 fps (delay=100ms)

# 2. Réduire résolution (de 1920x1080 à 1280x720)
convert input.gif -resize 1280x720 output.gif

# 3. Réduire durée (couper 2s début + 1s fin)
gifsicle input.gif '#2-80' -o output.gif  # Frames 2 à 80

# 4. Réduire couleurs (de 256 à 128)
gifsicle --colors=128 input.gif -o output.gif

# 5. Lossy compression (perte visuelle acceptable)
gifsicle -O3 --lossy=80 input.gif -o output.gif
```

### GIF saccadé (FPS trop bas)

**Solutions** :

```bash
# Augmenter FPS (de 10 à 15 fps)
# Option 1 : gifsicle
gifsicle --delay=6 input.gif -o output.gif  # 15 fps (delay=60ms)

# Option 2 : ffmpeg (recréer depuis vidéo)
ffmpeg -i video.mp4 -vf "fps=15,scale=1280:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" output.gif
```

### GIF ne loop pas

**Solutions** :

```bash
# Forcer loop infini
gifsicle --loopcount=0 input.gif -o output.gif

# Vérifier loop count actuel
identify -verbose input.gif | grep "Loop"
# Attendu : Loop Count: 0 (infini)
```

---

## Ressources

- [RGAA 4.1 - Multimédia](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#topic-multimedia)
- [DSFR - Médias](https://www.systeme-de-design.gouv.fr/elements-d-interface/medias)
- [gifsicle Documentation](https://www.lcdf.org/gifsicle/)
- [ffmpeg GIF Guide](https://trac.ffmpeg.org/wiki/Encode/HighQualityGifs)
- [Assets General Guide](../README.md)
- [Screenshots Guide](../screenshots/README.md)
