# Guide FALC vs Langage Clair - Fichiers disponibles

## 📁 Fichiers dans ce dossier

Ce dossier contient l'analyse complète du formulaire de décision FALC/LC de Com'access.

### 1. Documentation

| Fichier | Description | Format |
|---------|-------------|--------|
| **`regles-calcul-falc-lc.md`** | Documentation détaillée des règles de calcul | Markdown |
| **`arbre-decision-falc-lc.md`** | Arbre de décision complet avec exemples | Markdown |

### 2. Code source

| Fichier | Description | Format |
|---------|-------------|--------|
| **`falc-lc-calculator.js`** | JavaScript extrait du formulaire original | JavaScript |

### 3. Visualisations et exports

| Fichier | Description | Format | Usage |
|---------|-------------|--------|-------|
| **`arbre-decision-falc-lc.html`** | Version HTML stylisée prête pour PDF | HTML/CSS | Ouvrir dans navigateur et imprimer en PDF |
| **`arbre-decision-falc-lc.mmd`** | Diagramme Mermaid de l'arbre | Mermaid | Rendu sur mermaid.live ou GitHub |
| **`infographie-falc-lc.svg`** | Infographie visuelle de l'arbre | SVG | Afficher dans navigateur ou éditeur SVG |

---

## 🎯 Guide d'utilisation

### Option 1 : Générer un PDF depuis le HTML

**Méthode la plus simple et recommandée**

1. Ouvrir le fichier **`arbre-decision-falc-lc.html`** dans votre navigateur web (Chrome, Firefox, Edge, Safari)
2. Utiliser la fonction d'impression :
   - **Windows/Linux** : `Ctrl + P`
   - **Mac** : `Cmd + P`
3. Choisir **"Enregistrer en PDF"** comme destination
4. Cliquer sur **"Enregistrer"**

✅ **Résultat** : PDF de haute qualité avec mise en page professionnelle, couleurs, exemples et tableaux.

---

### Option 2 : Afficher l'infographie SVG

**Pour une vue visuelle de l'arbre de décision**

#### Dans un navigateur web
1. Ouvrir le fichier **`infographie-falc-lc.svg`** dans votre navigateur
2. Le navigateur affichera l'infographie

#### Convertir SVG en PDF/PNG
- **En ligne** : Utiliser https://cloudconvert.com/svg-to-pdf
- **Inkscape** (gratuit) : Ouvrir le SVG et exporter en PDF ou PNG
- **Chrome/Edge** : Ouvrir le SVG, puis `Ctrl+P` > Enregistrer en PDF

---

### Option 3 : Générer un diagramme depuis Mermaid

**Pour un diagramme interactif et modifiable**

1. Aller sur https://mermaid.live/
2. Copier le contenu de **`arbre-decision-falc-lc.mmd`**
3. Coller dans l'éditeur Mermaid Live
4. Exporter :
   - **PNG** : Cliquer sur "Actions" > "Download PNG"
   - **SVG** : Cliquer sur "Actions" > "Download SVG"
   - **PDF** : Télécharger le PNG/SVG, puis le convertir

---

### Option 4 : Utiliser un convertisseur Markdown vers PDF

**Pour les fichiers .md**

#### Avec Pandoc (ligne de commande)
```bash
# Installer pandoc (si pas déjà fait)
# Ubuntu/Debian
sudo apt-get install pandoc texlive-latex-base

# macOS
brew install pandoc basictex

# Windows
# Télécharger depuis https://pandoc.org/installing.html

# Convertir le fichier Markdown en PDF
pandoc arbre-decision-falc-lc.md -o arbre-decision-falc-lc.pdf
```

#### Avec VS Code (Extension)
1. Installer l'extension **"Markdown PDF"**
2. Ouvrir `arbre-decision-falc-lc.md`
3. Clic droit > "Markdown PDF: Export (pdf)"

#### En ligne
1. Aller sur https://www.markdowntopdf.com/
2. Uploader le fichier `.md`
3. Télécharger le PDF généré

---

## 📊 Comparaison des fichiers de visualisation

| Fichier | Avantages | Inconvénients | Recommandé pour |
|---------|-----------|---------------|-----------------|
| **HTML** | ✅ Mise en page pro<br>✅ Couleurs<br>✅ Exemples détaillés<br>✅ Tableaux | ❌ Nécessite un navigateur | 📄 **PDF final professionnel** |
| **SVG** | ✅ Vectoriel (scalable)<br>✅ Léger<br>✅ Visuel simple | ❌ Moins de détails textuels | 🖼️ **Infographie à partager** |
| **Mermaid** | ✅ Modifiable facilement<br>✅ Interactif | ❌ Nécessite outil de rendu | 🔧 **Modification et customisation** |

---

## 🎨 Personnalisation

### Modifier le HTML

Ouvrir `arbre-decision-falc-lc.html` dans un éditeur de texte et modifier :
- **Couleurs** : Modifier les valeurs dans la section `<style>`
- **Texte** : Modifier directement dans le `<body>`
- **Mise en page** : Ajuster les CSS

### Modifier le SVG

Ouvrir `infographie-falc-lc.svg` dans :
- **Inkscape** (gratuit) : https://inkscape.org/
- **Adobe Illustrator** (payant)
- **Figma** (en ligne, gratuit) : https://figma.com/

### Modifier le Mermaid

Éditer le fichier `.mmd` dans un éditeur de texte, puis recharger sur https://mermaid.live/

---

## 📋 Cas d'usage

### Pour une présentation
→ Utiliser l'**infographie SVG** ou générer un PDF depuis le **HTML**

### Pour un document officiel
→ Générer un PDF depuis le **HTML** (mise en page professionnelle)

### Pour partager sur les réseaux sociaux
→ Convertir le **SVG en PNG** (1200x1600px)

### Pour une documentation technique
→ Utiliser les fichiers **Markdown** (.md)

### Pour une formation
→ PDF depuis **HTML** + **infographie SVG**

---

## 🔗 Ressources complémentaires

### Outils de conversion PDF

| Outil | Type | URL |
|-------|------|-----|
| **CloudConvert** | En ligne | https://cloudconvert.com/ |
| **Pandoc** | CLI | https://pandoc.org/ |
| **Markdown PDF (VS Code)** | Extension | https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf |
| **Print to PDF (navigateur)** | Natif | Intégré dans Chrome/Firefox/Edge |

### Outils de diagrammes

| Outil | Type | URL |
|-------|------|-----|
| **Mermaid Live** | En ligne | https://mermaid.live/ |
| **Inkscape** | Logiciel | https://inkscape.org/ |
| **Draw.io** | En ligne | https://draw.io/ |

---

## 📝 Source et licence

**Source** : Analyse du formulaire Com'access (https://com-access.fr/falc-ou-lc/)

**Organisme** : Com'access - SARL spécialisée en FALC, Accessibilité numérique et Langage clair

**Date d'analyse** : 2025-11-06

**Auteur de l'analyse** : Généré automatiquement depuis le formulaire original

---

## ❓ FAQ

### Q : Quel fichier utiliser pour obtenir rapidement un PDF ?
**R :** Ouvrir `arbre-decision-falc-lc.html` dans Chrome/Firefox > `Ctrl+P` > Enregistrer en PDF

### Q : Comment modifier les couleurs de l'infographie ?
**R :** Ouvrir `infographie-falc-lc.svg` dans Inkscape (gratuit) et modifier les couleurs

### Q : Le diagramme Mermaid ne s'affiche pas sur GitHub
**R :** GitHub supporte Mermaid nativement. Copier le contenu du fichier `.mmd` dans un bloc de code Mermaid :
```markdown
```mermaid
<contenu du fichier .mmd>
```
```

### Q : Je veux une version imprimable sans couleurs
**R :** Ouvrir le HTML dans le navigateur, aller dans les options d'impression et décocher "Couleurs de fond"

### Q : Puis-je modifier ces fichiers ?
**R :** Oui, tous les fichiers sont modifiables. Le HTML et le SVG peuvent être édités dans n'importe quel éditeur de texte.

---

## 📞 Support

Pour toute question sur le contenu (règles FALC/LC), contacter Com'access :
- 🌐 Site : https://com-access.fr/
- 📧 Email : contact@com-access.fr
- 📞 Téléphone : 09 81 81 09 07
