# Guide d'utilisation des composants DSFR

Ce guide documente l'utilisation des composants du Système de Design de l'État (DSFR) dans le projet SPAN SG avec le thème mkdocs-dsfr v0.17.0.

Version: 1.0.0
Date: 2025-10-14
Auteur: Équipe technique SPAN SG

---

## Table des matières

1. [Introduction](#introduction)
2. [Cards - Cartes de navigation](#cards-cartes-de-navigation)
3. [Callouts - Encadrés informatifs](#callouts-encadres-informatifs)
4. [Badges - Indicateurs d'état](#badges-indicateurs-detat)
5. [Alerts - Notifications](#alerts-notifications)
6. [Grid - Grilles responsives](#grid-grilles-responsives)
7. [Tables - Tableaux accessibles](#tables-tableaux-accessibles)
8. [Accordions - Accordéons pliables](#accordions-accordeons-pliables)
9. [Tabs - Onglets](#tabs-onglets)
10. [Snippets réutilisables](#snippets-reutilisables)

---

## Introduction

Le thème mkdocs-dsfr utilise l'extension `dsfr_structure.extension.all_extensions` qui permet d'écrire des composants DSFR en syntaxe Markdown simplifiée.

### Référence officielle

- **Documentation DSFR** : https://www.systeme-de-design.gouv.fr/
- **mkdocs-dsfr** : https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/
- **Composants disponibles** : Cards, Callouts, Badges, Alerts, Grid, Accordions, Tabs, etc.

### Configuration requise

Dans `mkdocs-dsfr.yml` :

```yaml
markdown_extensions:
  - dsfr_structure.extension.all_extensions  # Active tous composants DSFR
  - pymdownx.superfences  # Support syntaxe ///
  - attr_list  # Support attributs HTML
  - def_list   # Support listes définitions
```

---

## Cards - Cartes de navigation

Les cards DSFR sont utilisées pour créer des cartes de navigation visuelles avec badges et liens.

### Syntaxe de base

```markdown
/// card | Titre de la card
    target: chemin/vers/page.md
    badge: Texte badge | type
Description de la card affichée en bas
///
```

### Paramètres

| Paramètre | Obligatoire | Description | Exemple |
|-----------|-------------|-------------|---------|
| `title` | Oui | Titre (1ère ligne après `card`) | `SIRCOM` |
| `target` | Oui | Lien destination | `modules/sircom.md` |
| `badge` | Non | Badge avec type | `Validé \| success` |
| `description` | Non | Texte explicatif | Service de la Communication |

### Types de badges

- `success` : Vert (validé, conforme)
- `warning` : Orange (brouillon, en cours)
- `error` : Rouge (bloqué, non conforme)
- `info` : Bleu (information)

### Exemple complet (docs/index.md:125-129)

```markdown
/// card | SIRCOM
    target: modules/sircom.md
    badge: Validé | success
Service de la Communication - Portails ministériels, sites internet/intranet
///
```

### Rendu HTML généré

```html
<div class="fr-card fr-enlarge-link" id="card-0">
  <div class="fr-card__body">
    <div class="fr-card__content">
      <h5 class="fr-card__title" id="sircom">
        <a href="modules/sircom/">SIRCOM</a>
      </h5>
      <div class="fr-card__start">
        <p class="fr-badge fr-badge--success">Validé</p>
      </div>
      <div class="fr-card__end">
        <p class="fr-card__detail">Service de la Communication...</p>
      </div>
    </div>
  </div>
</div>
```

### Cas d'usage

Navigation homepage vers modules de services (docs/index.md:119-167)

---

## Callouts - Encadrés informatifs

Les callouts sont des encadrés visuels pour mettre en avant des informations importantes.

### Syntaxe de base

```markdown
/// callout | Titre du callout
    icon: nom-icon-remixicon
    color: couleur-dsfr
    link_label: Texte lien
    link_url: https://example.com
Contenu du callout en Markdown
///
```

### Paramètres

| Paramètre | Obligatoire | Description | Exemple |
|-----------|-------------|-------------|---------|
| `title` | Oui | Titre | `Besoin d'aide ?` |
| `icon` | Non | Icône Remix Icon | `question-line` |
| `color` | Non | Couleur DSFR | `blue-france` |
| `link_label` | Non | Texte bouton | `En savoir plus` |
| `link_url` | Non | URL bouton | `https://...` |

### Couleurs DSFR disponibles

- `blue-france` : Bleu France (défaut, informatif)
- `orange-terre-battue` : Orange (alerte, attention)
- `green-menthe` : Vert menthe (positif, financement)
- `red-marianne` : Rouge (critique, urgent)
- `purple-glycine` : Violet (spécial)

### Icônes Remix Icon

Liste complète : https://remixicon.com/

Exemples courants :
- `question-line` : Point d'interrogation
- `alert-line` : Triangle alerte
- `money-euro-circle-line` : Euro (financement)
- `building-line` : Bâtiment
- `user-line` : Utilisateur

### Exemple 1 : Callout informatif (docs/accompagnement.md)

```markdown
/// callout | Besoin d'aide ?
    icon: question-line
    color: blue-france
    link_label: Contacter la MiWeb
    link_url: mailto:accessibilite.miweb@finances.gouv.fr
La MiWeb accompagne les référents de service dans la complétion de leur SPAN.
///
```

### Exemple 2 : Callout alerte (docs/processus.md:92-96)

```markdown
/// callout | Actions critiques pour le succès
    icon: alert-line
    color: orange-terre-battue
Ces 6 actions préalables conditionnent la réussite de votre SPAN. Ne pas les réaliser expose à l'échec du projet, à des sanctions financières (jusqu'à 75K€/site) et à un risque réputationnel important.
///
```

### Exemple 3 : Callout financement (docs/processus.md:99-104)

```markdown
/// callout | Financement FIPHFP disponible
    icon: money-euro-circle-line
    color: green-menthe
    link_label: En savoir plus sur le FIPHFP
    link_url: https://www.fiphfp.fr/
Le FIPHFP peut financer jusqu'à 10 000€ par an pendant 3 ans (30 000€ total) pour vos actions d'accessibilité : formations, audits RGAA, outils spécialisés.
///
```

### Exemple 4 : Callout critique (exemple)

```markdown
/// callout | Échéance légale imminente
    icon: time-line
    color: red-marianne
    link_label: Voir le calendrier
    link_url: /processus/#calendrier
Tous les services publics doivent publier leur SPAN avant le 31 décembre 2025 sous peine de sanctions Arcom.
///
```

### Différence avec Alerts

| Callouts | Alerts |
|----------|--------|
| Contenu éditorial | Messages système |
| Personnalisables (icon, color) | Types fixes (info, warning, error) |
| Peuvent avoir bouton CTA | Pas de bouton |
| Usage : mise en avant contenu | Usage : notifications utilisateur |

---

## Badges - Indicateurs d'état

Les badges DSFR sont utilisés pour indiquer l'état ou le statut d'un élément.

### Pourquoi HTML au lieu de Markdown ?

**Contexte (ADR-002)** : La syntaxe Markdown `/// badge` ne fonctionne pas dans les tableaux HTML. Le projet utilise donc la syntaxe HTML DSFR native pour les badges dans les tableaux.

### Syntaxe HTML DSFR

```html
<p class="fr-badge fr-badge--{type}">{Texte}</p>
```

### Types de badges

| Type | Classe CSS | Couleur | Usage |
|------|-----------|---------|-------|
| `success` | `fr-badge--success` | Vert | Validé, conforme, actif |
| `warning` | `fr-badge--warning` | Orange | Brouillon, en cours |
| `error` | `fr-badge--error` | Rouge | Bloqué, non conforme |
| `info` | `fr-badge--info` | Bleu | Informatif, en cours |

### Exemple 1 : Badge dans tableau (docs/synthese.md)

```html
<td>
    <p class="fr-badge fr-badge--success">Validé</p>
</td>
```

### Exemple 2 : Badge warning

```html
<p class="fr-badge fr-badge--warning">Brouillon</p>
```

### Exemple 3 : Badge error

```html
<p class="fr-badge fr-badge--error">Non renseigné</p>
```

### Exemple 4 : Badge info

```html
<p class="fr-badge fr-badge--info">En cours</p>
```

### Génération dynamique (scripts/calculate_scores.py:42-66)

```python
def generate_status_badge(checked: int, total: int) -> str:
    """Génère badge HTML DSFR selon score."""
    if total == 0:
        return '<p class="fr-badge fr-badge--error">Non renseigné</p>'
    elif checked == total:
        return '<p class="fr-badge fr-badge--success">Conforme</p>'
    elif checked > 0:
        return '<p class="fr-badge fr-badge--info">En cours</p>'
    else:
        return '<p class="fr-badge fr-badge--warning">À démarrer</p>'
```

### Badges dans Cards (syntaxe Markdown)

Dans les cards, utiliser la syntaxe Markdown simplifiée :

```markdown
/// card | Titre
    badge: Validé | success
///
```

Le type `success`, `warning`, `error`, `info` sera converti en classe CSS `fr-badge--{type}`.

---

## Alerts - Notifications

Les alerts DSFR sont des notifications système pour informer l'utilisateur.

### Syntaxe de base

```markdown
/// alert | Titre de l'alerte
    type: info
Contenu de l'alerte en Markdown
///
```

### Types disponibles

| Type | Couleur | Icône | Usage |
|------|---------|-------|-------|
| `info` | Bleu | ℹ️ | Information générale |
| `warning` | Orange | ⚠️ | Avertissement |
| `error` | Rouge | ❌ | Erreur, action requise |
| `success` | Vert | ✅ | Succès, confirmation |

### Exemple 1 : Alert info

```markdown
/// alert | Information
    type: info
Le site est accessible en mode prévisualisation pendant les travaux.
///
```

### Exemple 2 : Alert warning

```markdown
/// alert | Attention
    type: warning
Cette page sera archivée le 31 décembre 2025. Consultez la nouvelle version.
///
```

### Exemple 3 : Alert error

```markdown
/// alert | Erreur de configuration
    type: error
Le fichier `mkdocs.yml` contient des erreurs. Corrigez-les avant de continuer.
///
```

### Exemple 4 : Alert success

```markdown
/// alert | Validation réussie
    type: success
Votre SPAN a été validé par le comité de pilotage. Publication prévue le 15/11/2025.
///
```

### Alert vs Callout : Quand utiliser quoi ?

| Critère | Alert | Callout |
|---------|-------|---------|
| **Nature** | Message système | Contenu éditorial |
| **Durée** | Temporaire | Permanent |
| **Style** | Types fixes | Personnalisable |
| **Exemple** | "Maintenance en cours" | "Financement FIPHFP disponible" |

---

## Grid - Grilles responsives

Le système de grille DSFR permet de créer des layouts responsives sur 12 colonnes.

### Syntaxe de base

```markdown
/// row | fr-grid-row--gutters
/// col | 12 md-6 lg-4
Contenu colonne 1
///
/// col | 12 md-6 lg-4
Contenu colonne 2
///
/// col | 12 md-6 lg-4
Contenu colonne 3
///
///
```

### Structure

1. **Ligne** : `/// row | fr-grid-row--gutters`
2. **Colonnes** : `/// col | breakpoints`
3. **Fermeture** : Trois `///` pour fermer row

### Breakpoints

| Classe | Résolution | Colonnes | Usage |
|--------|-----------|----------|-------|
| `12` | Mobile (<768px) | 12/12 (pleine largeur) | Défaut |
| `md-6` | Tablette (≥768px) | 6/12 (2 colonnes) | Medium |
| `lg-4` | Desktop (≥1024px) | 4/12 (3 colonnes) | Large |

### Exemple complet : Grille 3 colonnes (docs/index.md:123-167)

```markdown
/// row | fr-grid-row--gutters
/// col | 12 md-6 lg-4
/// card | SIRCOM
    target: modules/sircom.md
    badge: Validé | success
Service de la Communication
///
///
/// col | 12 md-6 lg-4
/// card | SNUM
    target: modules/snum.md
    badge: Brouillon | warning
Service du Numérique
///
///
/// col | 12 md-6 lg-4
/// card | SRH
    target: modules/srh.md
    badge: Brouillon | warning
Service des Ressources Humaines
///
///
///
```

### Rendu responsive

- **Mobile** : 3 cards empilées verticalement (12/12)
- **Tablette** : 2 cards par ligne (6/12 + 6/12)
- **Desktop** : 3 cards par ligne (4/12 + 4/12 + 4/12)

### Variantes de row

| Classe | Description |
|--------|-------------|
| `fr-grid-row` | Grille sans espacement |
| `fr-grid-row--gutters` | Grille avec gouttières (recommandé) |
| `fr-grid-row--center` | Alignement centré |
| `fr-grid-row--middle` | Alignement vertical milieu |

### Exemple 2 : Grille 2 colonnes

```markdown
/// row | fr-grid-row--gutters
/// col | 12 md-6
Colonne gauche (50% tablette+)
///
/// col | 12 md-6
Colonne droite (50% tablette+)
///
///
```

### Exemple 3 : Grille 4 colonnes desktop

```markdown
/// row | fr-grid-row--gutters
/// col | 12 sm-6 lg-3
Colonne 1 (25% desktop)
///
/// col | 12 sm-6 lg-3
Colonne 2 (25% desktop)
///
/// col | 12 sm-6 lg-3
Colonne 3 (25% desktop)
///
/// col | 12 sm-6 lg-3
Colonne 4 (25% desktop)
///
///
```

---

## Tables - Tableaux accessibles

Le projet utilise un hook Python pour rendre automatiquement les tableaux Markdown accessibles RGAA.

### Hook automatique (hooks/dsfr_table_wrapper.py)

```python
def on_page_content(html, page, **kwargs):
    """Encapsule les tableaux Markdown dans divs DSFR."""
    return wrap_tables_dsfr(html)
```

Transforme :
```html
<table>...</table>
```

En :
```html
<div class="fr-table fr-table--bordered">
  <div class="fr-table__wrapper">
    <div class="fr-table__container">
      <div class="fr-table__content">
        <table>...</table>
      </div>
    </div>
  </div>
</div>
```

### Syntaxe Markdown standard

```markdown
| Colonne 1 | Colonne 2 | Colonne 3 |
|-----------|-----------|-----------|
| Ligne 1   | Donnée 1  | Donnée 2  |
| Ligne 2   | Donnée 3  | Donnée 4  |
```

Le wrapper DSFR est ajouté automatiquement par le hook.

### Caption RGAA (obligatoire)

Pour les tableaux de données, ajouter un caption HTML :

```html
<table id="table-span-modules">
    <caption>
        Synthèse des modules SPAN par service
    </caption>
    <thead>
        ...
    </thead>
</table>
```

### Tableaux avec badges HTML (docs/synthese.md)

```html
<div class="fr-table fr-table--bordered" id="table-synthese-span">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-span-modules">
                    <caption>
                        Synthèse des modules SPAN par service
                    </caption>
                    <thead>
                        <tr>
                            <th scope="col">Service</th>
                            <th scope="col">Score</th>
                            <th scope="col">Statut</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="table-span-row-sircom">
                            <td>SIRCOM</td>
                            <td>24/33 (72.7%)</td>
                            <td>
                                <p class="fr-badge fr-badge--success">Validé</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

### Attributs RGAA obligatoires

| Attribut | Élément | Valeur | Obligatoire |
|----------|---------|--------|-------------|
| `id` | `<table>` | Unique | Oui |
| `scope` | `<th>` | `col` ou `row` | Oui |
| `<caption>` | Dans `<table>` | Texte descriptif | Oui (tableaux données) |

### Responsive DSFR

Le wrapper DSFR rend le tableau scrollable horizontalement sur mobile si nécessaire.

---

## Snippets réutilisables

Bibliothèque de composants DSFR prêts à l'emploi.

### Card module standard

```markdown
/// card | [NOM_SERVICE]
    target: modules/[service].md
    badge: Brouillon | warning
[Description du service]
///
```

### Callout aide générique

```markdown
/// callout | Besoin d'aide ?
    icon: question-line
    color: blue-france
    link_label: Contacter le support
    link_url: mailto:support@example.com
Pour toute question sur ce contenu, contactez notre équipe support.
///
```

### Callout avertissement

```markdown
/// callout | Attention
    icon: alert-line
    color: orange-terre-battue
Cette information est critique pour la conformité de votre service.
///
```

### Callout financement

```markdown
/// callout | Financement disponible
    icon: money-euro-circle-line
    color: green-menthe
    link_label: Demander un financement
    link_url: https://fiphfp.fr/
Des aides financières sont disponibles pour vos actions d'accessibilité.
///
```

### Alert maintenance

```markdown
/// alert | Maintenance programmée
    type: warning
Le site sera indisponible le [DATE] de [HEURE] à [HEURE] pour maintenance.
///
```

### Alert succès validation

```markdown
/// alert | Validation réussie
    type: success
Votre module a été validé par le comité de pilotage.
///
```

### Badge inline personnalisé

```html
<p class="fr-badge fr-badge--info">Nouveau</p>
```

### Grille 3 cards template

```markdown
/// row | fr-grid-row--gutters
/// col | 12 md-6 lg-4
/// card | Card 1
    target: page1.md
    badge: Type | success
Description card 1
///
///
/// col | 12 md-6 lg-4
/// card | Card 2
    target: page2.md
    badge: Type | warning
Description card 2
///
///
/// col | 12 md-6 lg-4
/// card | Card 3
    target: page3.md
    badge: Type | error
Description card 3
///
///
///
```

### Tableau scores template

```html
<div class="fr-table fr-table--bordered">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table>
                    <caption>Titre du tableau</caption>
                    <thead>
                        <tr>
                            <th scope="col">Colonne 1</th>
                            <th scope="col">Colonne 2</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Donnée 1</td>
                            <td>
                                <p class="fr-badge fr-badge--success">Badge</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

---

## Accordions - Accordéons pliables

Les accordéons permettent de masquer/afficher du contenu de manière interactive. Idéal pour FAQ, sections longues ou documentation technique.

### Syntaxe de base

```markdown
/// accordion | Titre de l'accordéon
Contenu masqué par défaut
///
```

### Paramètres disponibles

| Paramètre | Description | Valeurs | Défaut |
|-----------|-------------|---------|--------|
| `title` | Titre de l'accordéon | Texte | Requis |
| `expanded` | État initial | `true`/`false` | `false` |
| `id` | ID HTML unique | string | auto |

### Exemple 1 : FAQ simple

```markdown
/// accordion | Comment contribuer au projet ?
Consultez le [Guide contributeur](../contributing.md) pour les instructions détaillées.

Processus en 3 étapes :
1. Fork du dépôt
2. Créer une branche feature
3. Ouvrir une Pull Request
///

/// accordion | Où trouver la documentation API ?
    expanded: true
La documentation complète est disponible dans [API Reference](api-reference.md).
///
```

### Exemple 2 : Documentation technique pliable

```markdown
/// accordion | Détails techniques du hook dsfr_table_wrapper.py
**Fonction** : Encapsule automatiquement les tableaux Markdown dans `<div class="fr-table">`.

**Code source** :
```python
def on_page_content(html, page, config, files):
    soup = BeautifulSoup(html, 'html.parser')
    for table in soup.find_all('table'):
        wrapper = soup.new_tag('div', **{'class': 'fr-table'})
        table.wrap(wrapper)
    return str(soup)
```

**Tests** : Voir `tests/test_hooks_dsfr_table_wrapper.py` (100% coverage).
///
```

### Exemple 3 : Sections multiples (groupe)

```markdown
/// accordion | SIRCOM - Service de la Communication
**Score** : 24/33 (72.7%)
**Référent** : Équipe Communication

Plan d'action 2025 : 9 actions en cours.
///

/// accordion | SNUM - Service du Numérique
**Score** : 21/33 (63.6%)
**Référent** : Chef de mission numérique

Plan d'action 2025 : 12 actions prioritaires.
///
```

### Différence avec Collapsible divs

- **Accordions** : Syntaxe markdown, intégration native mkdocs-dsfr
- **Collapsible HTML** : `<details><summary>` HTML natif

Privilégier les accordions pour cohérence DSFR.

### Accessibilité

Les accordions génèrent automatiquement :
- `role="button"` sur le titre
- `aria-expanded="true/false"` selon l'état
- Navigation clavier (Entrée/Espace pour toggle)

---

## Tabs - Onglets

Les onglets permettent d'organiser du contenu alternatif (exemples multi-langages, configurations alternatives).

### Syntaxe de base

```markdown
/// tabs
/// tab | Python
```python
print("Hello SPAN")
```
///

/// tab | Bash
```bash
echo "Hello SPAN"
```
///
///
```

### Exemple 1 : Exemples multi-langages

```markdown
/// tabs
/// tab | Python
```python
import yaml

with open('mkdocs-dsfr.yml') as f:
    config = yaml.safe_load(f)
    print(config['site_name'])
```
///

/// tab | JavaScript
```javascript
const fs = require('fs');
const yaml = require('js-yaml');

const config = yaml.load(fs.readFileSync('mkdocs-dsfr.yml', 'utf8'));
console.log(config.site_name);
```
///

/// tab | Bash
```bash
grep "^site_name:" mkdocs-dsfr.yml | cut -d: -f2
```
///
///
```

### Exemple 2 : Configurations alternatives

```markdown
/// tabs
/// tab | Docker (Recommandé)
```bash
docker compose -f docker-compose-dsfr.yml up -d
# Accès : http://localhost:8000/span-sg-repo/
```

**Avantages** : Isolation, pas de dépendances locales.
///

/// tab | Python local
```bash
pip install -r requirements-dsfr.txt
mkdocs serve --config-file mkdocs-dsfr.yml
```

**Prérequis** : Python 3.11+, pip.
///

/// tab | macOS Homebrew
```bash
brew install mkdocs
pip3 install mkdocs-dsfr
mkdocs serve --config-file mkdocs-dsfr.yml
```

**Note** : Utiliser Python 3 de Homebrew.
///
///
```

### Exemple 3 : Workflows Git

```markdown
/// tabs
/// tab | Feature (nouveau module)
```bash
git checkout -b feature/update-sircom
# Modifications dans docs/modules/sircom.md
git add docs/modules/sircom.md
git commit -m "feat(sircom): mise à jour plan 2025"
git push -u origin feature/update-sircom
# Créer PR vers draft
```
///

/// tab | Hotfix (production)
```bash
git checkout -b hotfix/fix-typo-synthese
# Corrections dans docs/synthese.md
git add docs/synthese.md
git commit -m "fix(synthese): correction typo tableau"
git push -u origin hotfix/fix-typo-synthese
# Créer PR vers main
```
///

/// tab | Sync draft → main
```bash
git checkout main
git pull origin main
git merge draft --no-ff
git push origin main
# Déclenche déploiement production
```
///
///
```

### Paramètres tabs

| Paramètre | Description | Valeurs |
|-----------|-------------|---------|
| Tabs parent | Conteneur principal | `/// tabs` ... `///` |
| Tab enfant | Onglet individuel | `/// tab \| Titre` |
| Titre | Label de l'onglet | Texte (requis) |

### Accessibilité

Les onglets génèrent automatiquement :
- `role="tablist"` sur le conteneur
- `role="tab"` sur chaque onglet
- `aria-selected="true/false"` selon l'onglet actif
- Navigation clavier (flèches gauche/droite)

### Cas d'usage recommandés

- Exemples de code multi-langages
- Instructions alternatives (Docker vs local)
- Workflows Git différents (feature vs hotfix)
- Configurations environnements (dev, staging, prod)

---

## Références complémentaires

- **ADR-001** : [Choix thème DSFR](../adr/001-choix-theme-dsfr.md)
- **ADR-002** : [Format synthèse HTML](../adr/002-format-synthese-html.md) - Pourquoi HTML badges
- **ADR-004** : [Hooks Python](../adr/004-hooks-python-mkdocs.md) - Table wrapper
- **API Reference** : [Scripts Python](api-reference.md) - Génération badges dynamiques

---

**Note finale** : Ce guide est maintenu à jour avec chaque nouvelle utilisation de composant DSFR dans le projet. Pour proposer des ajouts, ouvrez une issue ou PR sur GitHub.
