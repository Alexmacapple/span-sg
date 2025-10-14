# mkdocs-dsfr 0.17.0
Nécessite : Python >=3.10

Créé par : Ministère Transition Écologique - DNUM

## Source : 
https://pypi.org/project/mkdocs-dsfr/#description

## Site de documentation du thème Mkdocs DSFR  :
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/

## Projet d'exemple
https://gitlab-forge.din.developpement-durable.gouv.fr/pub/numeco/mkdocs-dsfr-exemple

## URL dépôt
https://gitlab-forge.din.developpement-durable.gouv.fr/pub/numeco/mkdocs-dsfr/

## Guide configuration MKDOCS
https://www.mkdocs.org/user-guide/configuration/#nav


# Thème DSFR pour MkDocs

## Description du projet

**⚠️ ATTENTION** : Ce thème est uniquement destiné à être utilisé pour les sites et applications officiels des services publics français. Son objectif principal est de faciliter l'identification des sites gouvernementaux pour les citoyens.

[Mentions légales](#)


## Démarrage rapide

Pour expérimenter rapidement mkdocs avec le DSFR, vous pouvez cloner le projet d'exemple. 

## Configuration du dépôt et des liens d'édition

Dans le fichier `mkdocs.yml`, trois configurations importantes sont définies pour permettre aux utilisateurs de naviguer vers le dépôt source et d'éditer les pages directement :

### Paramètres principaux

- **`repo_url`** : URL du dépôt Git où le code source de la documentation est hébergé

- **`edit_uri`** : Chemin relatif vers le dossier contenant les fichiers Markdown de la documentation dans le dépôt Git

- **`edit_text`** : Texte à afficher pour le lien d'édition

### Exemple de configuration

```yaml
repo_url: https://gitlab-forge.din.developpement-durable.gouv.fr/pub/numeco/mkdocs-dsfr/
edit_uri: blob/main/docs/
```

### Fonctionnement

1. `repo_url` pointe vers le dépôt GitLab où se trouve le code source de la documentation
2. `edit_uri` indique le chemin relatif vers les fichiers Markdown dans ce dépôt
3. Si l'une de ces variables n'est pas remplie, le lien d'édition n'apparaîtra pas

## Configuration du thème DSFR MkDocs

Ce document décrit les différentes options de configuration pour le thème DSFR MkDocs. Dans votre fichier de configuration `mkdocs.yml`, vous pouvez définir les options de thème pour personnaliser votre site.

### Configuration complète

```yaml
theme:
  # Config par défaut (modifiable)
  include_search_page: true
  afficher_date_de_revision: false
  afficher_menu_lateral: true
  afficher_bouton_editer: true
  bouton_hautdepage: left
  libelle_bouton_editer: Éditer dans Gitlab Forge

  # Ces valeurs sont à modifier
  intitule: "République <br> française"
  header:
    titre: "Titre"
    sous_titre: "Sous-titre"
  footer:
    description: "Description à modifier"
    links:
      - name: legifrance.gouv.fr
        url: https://legifrance.gouv.fr
      - name: gouvernement.fr
        url: https://gouvernement.fr
      - name: service-public.fr
        url: https://service-public.fr
      - name: data.gouv.fr
        url: https://data.gouv.fr
```

## Options de thème

### Options générales

#### `name`
Le nom du thème. Il doit être défini sur `dsfr`.

#### `locale`
La locale pour le thème. Il est défini sur `fr` pour le français.

#### `include_search_page`
Permet l'affichage et l'utilisation de la barre de recherche.

#### `afficher_date_de_revision`
Permet d'afficher la date de dernière révision git. 
- **Type** : Booléen
- **Valeur par défaut** : `false`
- **Description** : Affiche ou masque la date de la dernière révision de la page actuelle dans le pied de page
- **Prérequis** : Installation du plugin `mkdocs-git-revision-date-localized-plugin`

```bash
pip install mkdocs-git-revision-date-localized-plugin
```

#### `afficher_menu_lateral`
- **Type** : Booléen
- **Valeur par défaut** : `true`
- **Description** : Affiche ou masque le menu latéral

#### `afficher_bouton_editer`
- **Type** : Booléen
- **Valeur par défaut** : `true`
- **Description** : Affiche ou masque le bouton d'édition

#### `bouton_hautdepage`
Position du bouton "Haut de page" pour les pages longues.
- **Valeurs possibles** :
  - `left` (par défaut) : Alignement à gauche
  - `right` : Alignement à droite
  - `false` : Désactivé

#### `libelle_bouton_editer`
Permet de personnaliser le libellé du bouton d'édition.

#### `intitule`
Cette option définit le titre principal du logo dans l'en-tête et le pied de page.

### Options d'en-tête

#### `header.titre`
Définit le titre qui apparaît dans l'en-tête de la page.

#### `header.sous_titre`
Définit le sous-titre qui apparaît sous le titre dans l'en-tête de la page.

### Options de pied de page

#### `footer.description`
Définit une description qui apparaît dans le pied de page.

#### `footer.links`
Cette option vous permet de définir une liste de liens qui apparaîtront dans le pied de page. Chaque lien doit être un dictionnaire avec les clés suivantes :
- `name` : Nom du lien à afficher
- `url` : URL de destination

## Exemple d'utilisation

Voici un exemple de configuration minimale pour utiliser le thème DSFR :

```yaml
site_name: Mon site DSFR
theme:
  name: dsfr
  intitule: "République <br> française"
  header:
    titre: "Mon service public"
    sous_titre: "Documentation officielle"
  footer:
    description: "Documentation du service public"
    links:
      - name: service-public.fr
        url: https://service-public.fr
```
---

Voici la page formatée en markdown :

```markdown
# Documentation du thème Mkdocs DSFR

Le composant mkdocs-dsfr est un thème pour Mkdocs permettant de créer une documentation conforme au DSFR, le système de design de l'État.

## Avertissement

Ce thème est uniquement destiné à être utilisé pour les sites et applications officiels des services publics français. Son objectif principal est de faciliter l'identification des sites gouvernementaux pour les citoyens.

## Prérequis

- Python 3.10 ou supérieur
- (Facultatif mais recommandé) : uv pour la gestion des paquets Python. Vous pouvez néanmoins utiliser pip si vous le souhaitez. Le guide de démarrage rapide ci-dessous utilise uv.

## Démarrage rapide

Pour expérimenter rapidement mkdocs avec le DSFR, vous pouvez cloner le projet d'exemple, construit avec uv, un gestionnaire de paquets Python moderne et rapide.

### Installation avec uv

1. **Initialiser un nouveau projet avec uv**

```bash
mkdir ma-doc-dsfr
cd ma-doc-dsfr
uv init
```

2. **Installer la dépendance mkdocs-dsfr**. Cette dépendance installera sur votre projet Mkdocs lui-même et toutes les dépendances nécessaires.

```bash
uv add mkdocs-dsfr
```

3. **(Recommandé) Installer le plugin Open in a new tab** afin de détecter les liens externes et de les ouvrir dans un nouvel onglet, avec une icône reconnaissable.

```bash
uv add mkdocs-open-in-new-tab
```

4. **Modifier le fichier `mkdocs.yml`** pour utiliser le thème dsfr. Ajouter les lignes suivantes en fin de fichier.

```yaml
theme:
  name: dsfr
  locale: fr

plugins:
  - search:
      lang: fr
  - open-in-new-tab

markdown_extensions:
  - dsfr_structure.extension.all_extensions
  - pymdownx.snippets
  - pymdownx.highlight:
      use_pygments: true
  - pymdownx.emoji:
    options:
      attributes:
        align: absmiddle
        height: 20px
        width: 20px
  - pymdownx.superfences
  - toc:
      permalink: false
      toc_depth: 2
  - attr_list
  - def_list
  - tables
```

La directive `theme` permet de spécifier le thème à utiliser. Dans ce cas, nous utilisons le thème `dsfr`. L'option `locale` permet de définir la langue de la documentation. C'est utile pour l'accessibilité de la page et le fonctionnement de certains plugins. Dans ce cas, nous utilisons le français (`fr`).

La directive `plugins` permet d'ajouter des plugins supplémentaires à Mkdocs. Dans ce cas, nous ajoutons le plugin `search` pour la recherche dans la documentation.

Enfin, la directive `markdown_extensions` permet d'ajouter des extensions Markdown supplémentaires. Dans ce cas, nous ajoutons plusieurs extensions pour améliorer la syntaxe Markdown et profiter pleinement du thème DSFR.

5. **Lancer Mkdocs en mode développement**. Ce mode permet de visualiser la documentation générée en temps réel.

```bash
uv run mkdocs serve
```

6. **Pour construire la documentation**, utilisez la commande suivante :

```bash
uv run mkdocs build
```

La documentation est alors créée dans le dossier `site` de votre projet. Félicitations, vous avez créé votre première documentation avec le thème DSFR ! Dans la section suivante, nous allons explorer les différentes options de configuration disponibles pour personnaliser votre documentation.
```

---
Voici la page formatée en markdown :

```markdown
# Options du thème DSFR

Dans votre fichier de configuration `mkdocs.yml`, vous pouvez définir les options de thème pour personnaliser votre site. Voici les options de thème disponibles et leurs valeurs par défaut :

```yaml
theme:
  name: dsfr
  locale: fr
  # Configuration par défaut (modifiable)
  afficher_bouton_editer: true
  afficher_date_de_revision: false
  afficher_menu_lateral: true
  afficher_sommaire: false
  bouton_hautdepage: left
  include_search_page: true
  intitule: "République <br> française"
  libelle_bouton_editer: Éditer dans Gitlab Forge
  header:
    titre: "Titre"
    sous_titre: "Sous-titre"
  footer:
    description: "Description à modifier"
    links:
      - name: legifrance.gouv.fr
        url: https://legifrance.gouv.fr
      - name: gouvernement.fr
        url: https://gouvernement.fr
      - name: service-public.fr
        url: https://service-public.fr
      - name: data.gouv.fr
        url: https://data.gouv.fr
```

## Options du thème

### name

Le nom du thème. Il doit être défini sur `dsfr`.

### locale

La locale pour le thème. Il doit être défini sur `fr` pour le français.

### afficher_bouton_editer

Afficher ou masquer le menu latéral. Définissez-le sur `true` ou `false`.

### afficher_date_de_revision

Afficher la date de dernière révision du document, à partir de Git. Cela suppose que vous utilisez un dépôt Git pour gérer votre documentation. Si vous utilisez un autre système de gestion de version, cette option ne fonctionnera pas. De plus, vous devez ajouter le plugin `git-revision-date-localized` dans la définition des plugins, sous `search` :

```yaml
plugins:
  - search:
      lang: fr
  - git-revision-date-localized
```

### afficher_menu_lateral

Afficher ou masquer le menu latéral sur l'ensemble de la documentation.

### afficher_sommaire

Afficher ou masquer le sommaire sur l'ensemble de la documentation. Le sommaire est un menu de navigation qui s'affiche en haut de chaque page, permettant de naviguer rapidement dans le contenu.

### bouton_hautdepage

Définir la position du bouton de retour en haut de page, affiché pour les pages longues (de longueur supérieure à deux fois la hauteur de l'écran). Les valeurs possibles sont `left`, `right` ou `false` pour le désactiver.

### include_search_page

Afficher et utiliser la barre de recherche. C'est une option standard dans MkDocs.

### libelle_bouton_editer

Personnaliser le libellé de bouton d'édition.

### intitule

Cette option définit l'intitulé du ministère dans le logo de l'en-tête et du pied de page. Utilisez les balises `<br>` pour aller à la ligne en fonction de la charte de chaque ministère.

## Options de l'en-tête avec header

### titre

Définir le titre qui apparaît dans l'en-tête de la page.

### sous_titre

Définir le sous-titre qui apparaît sous le titre dans l'en-tête de la page.

## Options du pied de page avec footer

### description

Définir une description qui apparaît dans le pied de page.

### links

Lister les liens qui apparaîtront dans le pied de page. Chaque lien doit être un dictionnaire YAML avec des clés `name` et `url`.

## Menu de navigation principal

Comme tout document créé avec Mkdocs, le menu de navigation est défini dans le fichier `mkdocs.yml` sous la clé `nav`. Voici un exemple de configuration :

```yaml
nav:
  - Accueil: index.md
  - Guide de démarrage: guide.md
  - Référence API: api.md
  - À propos: about.md
```

Pour en savoir plus sur la configuration du menu de navigation, consultez la documentation officielle de Mkdocs.
```
---

Voici la page formatée en markdown :

```markdown
# Mise en page avec le thème mkdocs-dsfr

La mise en page avec le thème `mkdocs-dsfr` se base sur une mise en page standard du DSFR :

- Un en-tête avec le logo du ministère, le titre, le sous-titre, et une barre de recherche
- Un menu de navigation conforme au DSFR
- Un contenu principal avec des sections et des sous-sections
- Un menu latéral pour la navigation dans le contenu
- Un pied de page avec des informations de contact et des liens

## Les composants optionnels de mise en page

Le thème `mkdocs-dsfr` permet d'ajouter des composants optionnels de mise en page. Ce sont des composants DSFR qui n'apparaissent qu'une fois par page, à une place prédéfinie. Vous pouvez consulter la liste des composants uniques par page pour les ajouter.

## Configuration d'un composant unique par page

Les composants uniques par page sont configurés dans les métadonnées du fichier Markdown de la page. Voici un exemple de configuration pour le menu latéral, le fil d'Ariane et le sommaire :

```yaml
---
sidemenu: true
breadcrumb:
  - Accueil: /
  - Composants: /composants/
  - Fil d'Ariane
summary: true
---

# Titre de la page

Contenu de la page avec le menu latéral, le fil d'Ariane et le sommaire.
```

Consultez la documentation de chaque composant unique par page pour connaître sa configuration.

## Le système de grille

Le thème `mkdocs-dsfr` utilise un système de grille basé sur le DSFR pour organiser le contenu sur plusieurs colonnes. Consultez la documentation du composant grille pour en savoir plus sur sa configuration.
```


--- 

## Les composants DSFR

### Généralité
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/

### Accordéon
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/accordion/

### Alerte
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/alert/

### Badge
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/badge/

### Composant bandeau d'information importante
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/notice/

### Carte
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/card/

### Composant Citation

https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/quote/


### Fil d'ariane
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/breadcrumb/

### Le système de grille
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/grid/

### Médias
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/media/

### Menu latéral
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/sidemenu/

###  Mise en avant simple
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/callout/

### Sommaire
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/summary/

### Composant Tuile
https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/composants/tile/

