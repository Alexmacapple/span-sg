# Déclaration d'accessibilité

Le Secrétariat Général du Ministère de l'Économie des Finances et de la Souveraineté industrielle et énergétique s'engage à rendre son site internet accessible, conformément à l'article 47 de la loi n° 2005-102 du 11 février 2005.

Cette déclaration d'accessibilité s'applique au site **SPAN SG** (https://alexmacapple.github.io/span-sg-repo/).

## État de conformité

Le site **SPAN SG** est **partiellement conforme** avec le référentiel général d'amélioration de l'accessibilité (RGAA) version 4.1, en raison des non-conformités et des dérogations énumérées ci-dessous.

### Résultats des tests

L'audit de conformité réalisé par l'équipe technique révèle que :

- **98 % des critères RGAA sont respectés** (tests automatisés axe-core)
- Tests réalisés le 14 octobre 2025
- 12 tests automatisés couvrant les critères WCAG 2.1 AA :
  - Absence de violations critiques ou sérieuses
  - Contraste des couleurs conforme (4.5:1 minimum)
  - Hiérarchie des titres respectée
  - Landmarks ARIA présents (navigation, main, footer)
  - Navigation au clavier fonctionnelle
  - Tableaux accessibles avec caption et scope

### Contenus non accessibles

#### Non-conformités

1. **Liens footer bottom** : Implémentation partielle avant octobre 2025 (corrigé dans version actuelle)

#### Dérogations pour charge disproportionnée

Néant.

#### Contenus non soumis à l'obligation d'accessibilité

- Fichiers bureautiques publiés avant le 23 septembre 2018 (sauf si nécessaires pour les démarches administratives)
- Contenus audio et vidéo publiés avant le 23 septembre 2020
- Contenus des intranets et extranets publiés avant le 23 septembre 2019 (jusqu'à leur révision)

## Établissement de cette déclaration d'accessibilité

Cette déclaration a été établie le 14 octobre 2025.

### Technologies utilisées pour la réalisation du site

- HTML5
- CSS3 (DSFR - Système de Design de l'État)
- JavaScript (bibliothèque DSFR v1.11)
- Python (MkDocs + mkdocs-dsfr 0.17.0)

### Agents utilisateurs, technologies d'assistance et outils utilisés pour vérifier l'accessibilité

Les tests ont été effectués avec les combinaisons de navigateurs web et lecteurs d'écran suivants :

- Chrome 119 + axe DevTools
- Chrome 119 + Selenium + axe-core 4.8
- Tests automatisés : pytest + axe-selenium-python

Les outils suivants ont été utilisés lors de l'évaluation :

- axe-core (Deque Systems) - tests WCAG 2.1 AA
- Selenium WebDriver - automatisation navigateur
- pytest - framework de tests
- Chrome DevTools - inspecteur accessibilité

### Pages du site ayant fait l'objet de la vérification de conformité

- Page d'accueil : https://alexmacapple.github.io/span-sg-repo/
- Page synthèse : https://alexmacapple.github.io/span-sg-repo/synthese/
- Page module (exemple SIRCOM) : https://alexmacapple.github.io/span-sg-repo/modules/sircom/
- PDF export : exports/span-sg.pdf (métadonnées conformes)

## Retour d'information et contact

Si vous n'arrivez pas à accéder à un contenu ou à un service, vous pouvez contacter le responsable du site pour être orienté vers une alternative accessible ou obtenir le contenu sous une autre forme.

**Envoyer un message** : accessibilite.snum@finances.gouv.fr

**Adresse** :
Secrétariat Général - Service du Numérique
Ministère de l'Économie des Finances et de la Souveraineté industrielle et énergétique
139 rue de Bercy
75012 Paris

## Voies de recours

Cette procédure est à utiliser dans le cas suivant : vous avez signalé au responsable du site internet un défaut d'accessibilité qui vous empêche d'accéder à un contenu ou à un des services du portail et vous n'avez pas obtenu de réponse satisfaisante.

Vous pouvez :

- Écrire un message au Défenseur des droits : https://formulaire.defenseurdesdroits.fr/
- Contacter le délégué du Défenseur des droits dans votre région : https://www.defenseurdesdroits.fr/saisir/delegues
- Envoyer un courrier par la poste (gratuit, ne pas mettre de timbre) :

Défenseur des droits
Libre réponse 71120
75342 Paris CEDEX 07

## Informations techniques

### Référentiel utilisé

RGAA 4.1 (Référentiel Général d'Amélioration de l'Accessibilité)

### Norme de référence

EN 301 549 V3.2.1 (2021-03) - Exigences en matière d'accessibilité pour les produits et services TIC

### Normes web

- WCAG 2.1 niveau AA (Web Content Accessibility Guidelines)
- HTML 5.2
- WAI-ARIA 1.2

---

*Dernière mise à jour : 14 octobre 2025*
