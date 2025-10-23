# Assets Documentation - SPAN SG

Gestion des ressources visuelles (screenshots, GIFs, images) pour la documentation SPAN SG.

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-22

---

## Structure des Assets

```
docs/assets/
├── README.md                 # Ce fichier
├── extra.js                  # Scripts JavaScript DSFR
├── screenshots/              # Captures d'écran documentation
│   ├── README.md             # Guide captures d'écran
│   ├── github-pr-*.png       # Workflow GitHub
│   ├── ci-*.png              # GitHub Actions
│   ├── mkdocs-*.png          # Interface MkDocs
│   └── dsfr-*.png            # Composants DSFR
├── gifs/                     # Animations GIF tutoriels
│   ├── README.md             # Guide GIFs
│   ├── onboarding-*.gif      # Workflow onboarding
│   └── e2e-*.gif             # Tests E2E
└── diagrams/                 # Diagrammes exportés (optionnel)
    └── *.svg                 # Exports Mermaid SVG
```

---

## Conventions de Nommage

### Screenshots

Format : `{categorie}-{description}-{taille}.png`

Catégories :
- `github-` : Interface GitHub (PR, Issues, Actions)
- `ci-` : GitHub Actions (logs, jobs, artifacts)
- `mkdocs-` : Interface MkDocs locale
- `dsfr-` : Composants DSFR
- `pdf-` : Exports PDF

Exemples :
- `github-pr-creation-1200x800.png`
- `ci-logs-build-1920x1080.png`
- `mkdocs-serve-localhost-1440x900.png`

### GIFs

Format : `{workflow}-{action}-{fps}.gif`

Workflows :
- `onboarding-` : Workflow contributeur
- `pr-` : Processus Pull Request
- `e2e-` : Tests bout-en-bout
- `build-` : Build MkDocs/PDF

Exemples :
- `onboarding-create-pr-10fps.gif`
- `e2e-selenium-test-15fps.gif`

---

## Spécifications Techniques

### Screenshots

Requis pour conformité RGAA et DSFR :

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| Format | PNG (sans perte) | Qualité texte optimal |
| Résolution | 1920x1080 (préféré) | Lisibilité écrans HD |
| Poids max | 500 KB | Performance chargement |
| Compression | pngquant/optipng | Réduction 60-80% sans perte visible |
| Texte alternatif | Obligatoire | RGAA 1.1.1 (Images avec alternative) |

### GIFs

Requis pour tutoriels interactifs :

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| Format | GIF animé | Compatibilité navigateurs |
| FPS | 10-15 fps | Fluidité/poids optimal |
| Durée | 5-15 secondes | Attention utilisateur |
| Résolution | 1280x720 | Compromis qualité/poids |
| Poids max | 2 MB | Performance chargement |
| Loop | Infini | UX tutoriels |

---

## Outils Recommandés

### Capture d'Écran

**macOS** :
- Cmd+Shift+4 : Sélection zone
- Cmd+Shift+5 : Outils capture (avec timer)
- [CleanShot X](https://cleanshot.com/) : Annotations, scrolling

**Windows** :
- Win+Shift+S : Outil Capture
- [ShareX](https://getsharex.com/) : Open source, annotations

**Linux** :
- `scrot -s` : Sélection zone
- [Flameshot](https://flameshot.org/) : GUI annotations

### Création GIF

**Multiplateforme** :
- [ScreenToGif](https://www.screentogif.com/) : Capture + édition (Windows)
- [LICEcap](https://www.cockos.com/licecap/) : Léger, simple (Mac/Win)
- [Kap](https://getkap.co/) : Open source, plugins (macOS)

**Ligne de commande** :
```bash
# ffmpeg : Vidéo MP4 → GIF optimisé
ffmpeg -i input.mp4 -vf "fps=10,scale=1280:-1:flags=lanczos" -c:v gif output.gif

# gifsicle : Optimisation GIF
gifsicle -O3 --colors 256 input.gif -o output.gif
```

---

## Workflow d'Ajout

### 1. Capturer l'Asset

```bash
# Screenshot : Capturer fenêtre/zone pertinente
# - Inclure contexte (URL, menu, breadcrumb)
# - Éviter données sensibles (tokens, emails)
# - Nettoyer distractions (notifications, dock)

# GIF : Enregistrer workflow complet
# - Prévisualiser avant enregistrement
# - Nettoyer fenêtres en arrière-plan
# - Préparer actions à l'avance (réduire durée)
```

### 2. Optimiser le Fichier

```bash
# PNG : Compression sans perte
pngquant --quality=80-95 screenshot.png -o screenshot-opt.png
optipng -o7 screenshot-opt.png

# GIF : Réduction poids
gifsicle -O3 --lossy=80 --colors 128 animation.gif -o animation-opt.gif
```

### 3. Copier dans Dossier Assets

```bash
# Respecter convention nommage
cp screenshot-opt.png docs/assets/screenshots/github-pr-creation-1920x1080.png
cp animation-opt.gif docs/assets/gifs/onboarding-create-pr-10fps.gif
```

### 4. Référencer dans Markdown

```markdown
# Screenshot avec alt text (RGAA obligatoire)
![Création Pull Request sur GitHub interface web](../assets/screenshots/github-pr-creation-1920x1080.png)

# GIF avec alt text descriptif
![Animation démonstration workflow contributeur : édition module SIRCOM puis création PR vers branche main](../assets/gifs/onboarding-create-pr-10fps.gif)
```

### 5. Valider Accessibilité

```bash
# Vérifier alt text présent (requis RGAA 1.1.1)
grep -r "!\[.*\]" docs/ | grep -v "!\[.*\].*assets"
# → Aucun résultat = OK (tous les assets ont alt text)

# Tester chargement local
docker compose -f docker-compose-dsfr.yml up
# → Vérifier http://localhost:8000/span-sg/onboarding-visual/
```

---

## Exemples d'Utilisation

### Screenshot Inline

```markdown
## Création Pull Request

Pour créer une PR vers `draft`, suivre ces étapes :

![Interface GitHub création Pull Request avec sélection branche base main et branche compare feature/update-sircom](../assets/screenshots/github-pr-creation-1920x1080.png)

1. Sélectionner branche base : `draft`
2. Sélectionner branche compare : `feature/update-sircom`
3. Cliquer "Create Pull Request"
```

### GIF Tutoriel

```markdown
## Workflow Contributeur Complet

Animation démonstrant le processus de contribution de bout en bout :

![Animation workflow : édition module SIRCOM sur GitHub web, cochage 3 critères DINUM, création Pull Request vers staging, attente review validateur, merge automatique](../assets/gifs/onboarding-create-pr-10fps.gif)

Durée estimée : 15 minutes par contribution.
```

---

## Checklist Accessibilité

Avant d'ajouter un asset, valider :

- [ ] Texte alternatif (alt text) descriptif et concis
- [ ] Fichier optimisé (poids < seuils max)
- [ ] Nom fichier explicite (convention respectée)
- [ ] Contenu visible et lisible (contraste suffisant)
- [ ] Pas de données sensibles (tokens, emails privés)
- [ ] Contexte inclus (URL, breadcrumb) si pertinent
- [ ] Test chargement local OK
- [ ] Référencé dans documentation appropriée

---

## Maintenance Assets

### Rotation Assets Obsolètes

Supprimer screenshots/GIFs obsolètes lors de :
- Migration interface GitHub (UI refresh)
- Mise à jour thème DSFR (changements visuels)
- Refonte workflows CI/CD (nouveaux jobs)

### Versioning

Conserver assets précédents avec suffix version :

```
github-pr-creation-v1.0-1920x1080.png  # Version initiale
github-pr-creation-v1.1-1920x1080.png  # Mise à jour UI GitHub 2025
```

---

## Références

- [RGAA 4.1 - Critère 1.1.1 (Images)](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#1.1.1)
- [DSFR - Images et Médias](https://www.systeme-de-design.gouv.fr/elements-d-interface/medias)
- [Screenshots Guide](screenshots/README.md)
- [GIFs Guide](gifs/README.md)
