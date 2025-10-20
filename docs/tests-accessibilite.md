# Tests d'accessibilité SPAN SG

Version: 1.1
Date: 2025-10-20
Statut: Actif (bloquant en CI - Phase 2)

## Vue d'ensemble

Le projet SPAN SG intègre une suite complète de tests d'accessibilité automatisés conformes aux standards WCAG 2.1 AA et RGAA 4.1. Ces tests utilisent axe-core via Selenium pour automatiser 60-65% des vérifications RGAA.

## Tests implémentés

### 1. Homepage WCAG (5 tests)

- **test_homepage_wcag_violations** : Aucune violation WCAG 2.1 AA critique
- **test_homepage_color_contrast** : Contraste des couleurs (WCAG 1.4.3)
- **test_homepage_heading_hierarchy** : Hiérarchie des titres h1-h6 (WCAG 1.3.1)
- **test_homepage_landmarks** : Présence landmarks ARIA (navigation, main, footer)
- **test_homepage_keyboard_navigation** : Accessibilité clavier complète

### 2. Synthese Table DSFR (4 tests)

- **test_synthese_table_dsfr_wrapper** : Classes DSFR (fr-table)
- **test_synthese_table_aria_labels** : Labels ARIA corrects
- **test_synthese_table_caption** : Présence et pertinence du caption
- **test_synthese_table_responsive** : Responsive design mobile (375px)

### 3. PDF Metadata RGAA (3 tests)

- **test_pdf_metadata_title** : Metadata /Title présent (RGAA 13.1)
- **test_pdf_metadata_language** : Langue fr-FR déclarée (RGAA 13.3)
- **test_pdf_metadata_description** : Metadata Subject/Description présent

## Installation

```bash
# Installer dépendances accessibilité
pip install -r requirements-accessibility.txt

# Chrome/ChromeDriver requis pour Selenium
# - macOS: brew install chromedriver
# - Linux CI: automatique via browser-actions/setup-chrome@v1
```

## Usage local

### Prérequis
1. Générer le site HTML : `mkdocs build --config-file mkdocs-dsfr.yml`
2. Chrome/ChromeDriver disponible dans PATH

### Exécuter les tests

```bash
# Tous les tests accessibilité
pytest tests/test_accessibility.py -v

# Tests homepage uniquement
pytest tests/test_accessibility.py -k homepage -v

# Tests table DSFR uniquement
pytest tests/test_accessibility.py -k synthese_table -v

# Tests PDF uniquement (nécessite exports/span-sg.pdf)
pytest tests/test_accessibility.py -k pdf_metadata -v

# Générer rapport HTML
pytest tests/test_accessibility.py \
  --html=accessibility-report.html \
  --self-contained-html
```

## Intégration CI/CD

Les tests d'accessibilité s'exécutent automatiquement dans GitHub Actions (branche main uniquement) :

```yaml
- name: Run accessibility tests (RGAA)
  run: pytest tests/test_accessibility.py -v --html=accessibility-report.html
```

**Statut actuel** : Bloquant (Phase 2 activée)
- Les échecs bloquent le déploiement (fail-fast)
- Seuil de tolérance : 0 violations critiques WCAG 2.1 AA
- Rapport HTML uploadé comme artefact (30 jours rétention)
- Phase 3 (Certification RGAA) prévue pour v1.2.0

## Couverture RGAA

Les tests automatisés couvrent environ 60-65% des critères RGAA 4.1 :

### Automatisables (60-65%)
- Contraste des couleurs (1.4.3)
- Hiérarchie des titres (1.3.1)
- Labels formulaires (3.3.2)
- Navigation clavier (2.1.1)
- Landmarks ARIA (1.3.1)
- PDF metadata (13.1, 13.3)

### Non automatisables (35-40%)
- Pertinence des alternatives textuelles
- Transcriptions audio/vidéo
- Clarté du langage
- Tests utilisateurs handicapés

## Roadmap

### Phase 1 : Monitoring ✅ (terminé le 2025-10-20)
- Tests non-bloquants en CI
- Rapports HTML pour analyse
- Corrections progressives

### Phase 2 : Enforcement 🚀 (actuel - v1.1.0)
- Tests bloquants en CI
- Seuil tolérance 0 violations critiques
- Revue manuelle 35% restants

### Phase 3 : Certification (v1.2.0)
- Audit RGAA complet par expert
- Tests utilisateurs handicapés
- Déclaration accessibilité conforme

## Références

- WCAG 2.1 : https://www.w3.org/TR/WCAG21/
- RGAA 4.1 : https://www.numerique.gouv.fr/publications/rgaa-accessibilite/
- axe-core : https://github.com/dequelabs/axe-core
- DSFR Accessibilité : https://www.systeme-de-design.gouv.fr/utilisation-et-organisation/accessibilite

## Support

Questions : alexandre@span-sg.gouv.fr
Issues : https://github.com/Alexmacapple/span-sg-repo/issues
