# Story S7-01 : Migration DSFR Complet

**Phase** : Sprint 7 - DSFR Migration
**Priorité** : P1 (après v1.0.0 stable)
**Estimation** : 30-56h (selon complexité PDF)
**Type** : Infrastructure (breaking change v2.0.0)

---

## Contexte Projet

**État actuel** : v1.0.2-poc
- Score qualité : 97/100
- Stack : MkDocs Material
- PDF : mkdocs-with-pdf (fonctionnel)
- Tests : 21 unitaires + 9 E2E automatisés
- Infrastructure : Production-ready

**Validation légale** : Projet sera sur domaine .gouv.fr à terme
**Conclusion** : Migration DSFR officiel légalement autorisée

---

## Objectif

**Migrer infrastructure MkDocs Material vers DSFR (Système de Design de l'État)**

Livrables :
1. Theme mkdocs-dsfr installé et configuré
2. Header DSFR avec logo République Française
3. Footer DSFR avec liens gouvernementaux
4. Police Marianne officielle
5. Export PDF DSFR-compatible maintenu
6. Scoring 31 points DINUM préservé
7. Tests E2E adaptés
8. Release v2.0.0 (breaking change)

---

## Analyse Contraintes Légales

### Licence Police Marianne
**Usage** : "Strictly prohibited for use outside of French government websites"
**Site actuel** : alexmacapple.github.io/span-sg-repo (domaine personnel)
**Site cible** : [À DÉFINIR].gouv.fr (domaine gouvernemental)

**Verdict** :
- [NON-FAIT] Migration DSFR INTERDITE sur domaine personnel
- [COMPLETE] Migration DSFR AUTORISÉE sur domaine .gouv.fr

### Assets DSFR Officiels
- CSS/JS @gouvfr/dsfr : Réservés services gouvernementaux
- Composants header/footer : Idem
- Logo République Française : Usage strictement encadré

**Prérequis absolu** : Domaine .gouv.fr confirmé et réservé

---

## Analyse Stack Actuelle

### Dependencies (requirements.txt)
```python
mkdocs-material>=9.5.0,<10.0.0  # Theme actuel
mkdocs-with-pdf>=0.9.3           # Export PDF
pikepdf>=8.0.0                   # Métadonnées PDF
```

### Configuration (mkdocs.yml)
```yaml
theme:
  name: material
  language: fr
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate

plugins:
  - search:
      lang: fr
```

### Assets Critiques (À Préserver)
1. **Scoring 31 points** : calculate_scores.py (indépendant thème)
2. **Export PDF** : mkdocs-with-pdf (RISQUE incompatibilité DSFR)
3. **Tests E2E** : 9 scénarios bash HTTP
4. **Synthèse auto** : generate_summary() (indépendant)
5. **CI/CD** : GitHub Actions workflows

---

## Analyse Risques Migration

### RISQUE CRITIQUE - Export PDF

**Problème** : mkdocs-with-pdf documente support Material uniquement
**Impact** : Export PDF actuel peut NE PAS fonctionner avec mkdocs-dsfr
**Probabilité** : Élevée (60-70%)
**Criticité** : BLOQUANT

**Mitigation** :
1. POC test PDF obligatoire Phase 1
2. Solution alternative si échec :
   - Option A : mkdocs-with-pdf + custom CSS DSFR (12-16h)
   - Option B : mkdocs-exporter (6-8h test)
   - Option C : Puppeteer/WeasyPrint custom (16-20h)

### RISQUE MOYEN - Tests E2E

**Tests HTTP basiques** : OK (pas de sélecteurs CSS Material-specific)
**Tests PDF** : À mettre à jour si changement plugin
**Estimation adaptation** : 2-4h

### RISQUE FAIBLE - Scoring

**Indépendance** : 100% (parse Markdown brut, pas HTML)
**Impact migration** : Aucun
**Tests** : Coverage 89.6% maintenu

### RISQUE FAIBLE - CI/CD

**Workflows** : À adapter (requirements, Dockerfile)
**Build time** : Peut augmenter (assets DSFR plus lourds)
**Estimation** : 2-4h adaptation

---

## Stack DSFR Cible

### Dependencies (requirements-dsfr.txt)
```python
# Theme DSFR officiel
mkdocs-dsfr>=0.11.0,<1.0.0

# Plugin structure DSFR (grille, composants)
# Installé automatiquement avec mkdocs-dsfr

# Plugin date révision (requis DSFR)
mkdocs-git-revision-date-localized-plugin>=1.2.0

# Métadonnées PDF (préservé)
pikepdf>=8.0.0

# Export PDF : À déterminer après POC Phase 1
# Option A : mkdocs-with-pdf + custom CSS
# Option B : mkdocs-exporter
```

### Configuration (mkdocs-dsfr.yml)
```yaml
site_name: SPAN SG
site_url: https://[À DÉFINIR].gouv.fr/span-sg/
repo_url: https://github.com/[organisation]/span-sg-repo
strict: true

theme:
  name: dsfr
  language: fr

  # Configuration header DSFR
  intitule: "République <br> française"
  header:
    titre: "SPAN SG"
    sous_titre: "Schéma Pluriannuel d'Accessibilité Numérique"
    logo_url: /

  # Configuration footer DSFR
  footer:
    description: "Secrétariat Général - Accessibilité Numérique 2025-2027"
    links:
      - name: legifrance.gouv.fr
        url: https://legifrance.gouv.fr
      - name: service-public.fr
        url: https://service-public.fr
      - name: data.gouv.fr
        url: https://data.gouv.fr
      - name: info.gouv.fr
        url: https://info.gouv.fr

  # Options affichage
  afficher_date_de_revision: true
  afficher_menu_lateral: true
  afficher_bouton_editer: true
  libelle_bouton_editer: "Éditer dans GitHub"

plugins:
  - search:
      lang: fr
  - dsfr_structure  # Plugin composants DSFR
  - git-revision-date-localized:
      enable_creation_date: true
      type: date
      fallback_to_build_date: true

# Édition GitHub
repo_url: https://github.com/Alexmacapple/span-sg-repo
edit_uri: blob/main/docs/

nav:
  - Accueil: index.md
  - Synthèse: synthese.md
  - Processus: processus.md
  - Guide contributeur: contributing.md
  - Développement local: dev-local.md
  - Modules Services:
    - SNUM: modules/snum.md
    - SIRCOM: modules/sircom.md
    - SRH: modules/srh.md
    - SIEP: modules/siep.md
    - SAFI: modules/safi.md
    - BGS: modules/bgs.md

markdown_extensions:
  - tables
  - toc:
      permalink: true
```

### Docker (Dockerfile-dsfr)
```dockerfile
# Migration depuis FROM squidfunk/mkdocs-material:latest
FROM python:3.11-slim

WORKDIR /docs

# Installer dépendances système (qpdf pour PDF)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    qpdf \
    git \
    && rm -rf /var/lib/apt/lists/*

# Installer dépendances Python DSFR
COPY requirements-dsfr.txt .
RUN pip install --no-cache-dir -r requirements-dsfr.txt

EXPOSE 8000

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
```

---

## Stratégies Migration

### Stratégie A - Big Bang (NON Recommandée)

**Approche** : Remplacer Material par DSFR en une fois

**Étapes** :
1. Remplacer requirements.txt (Material → DSFR)
2. Adapter mkdocs.yml (config DSFR complète)
3. Tester export PDF (RISQUE échec)
4. Adapter CI/CD
5. Retester tous E2E

**Risques** :
- [NON-FAIT] PDF peut NE PAS fonctionner (bloquant)
- [NON-FAIT] Rollback difficile (refonte complète)
- [NON-FAIT] Tests massivement impactés
- [NON-FAIT] Score 97/100 à reconquérir

**Estimation** : 20-30h
**Probabilité succès** : 40-50%
**Recommandation** : À ÉVITER

---

### Stratégie B - POC DSFR Parallèle (RECOMMANDÉE)

**Approche** : Branche feature/dsfr-poc POC pour validation AVANT migration

#### Phase 1 - POC Technique (8-12h)

**Objectif** : Valider faisabilité technique DSFR (PDF critique)

**Étapes** :
1. Créer branche feature/dsfr-poc
2. Setup minimal :
   - requirements-dsfr.txt
   - mkdocs-dsfr.yml (config test)
   - 1 module test (sircom.md copié)
3. Tests critiques :
   - Build MkDocs DSFR
   - Scoring fonctionne
   - **TEST PDF** : mkdocs-with-pdf + alternatives
   - Header/Footer DSFR affichés
4. Validation GO/NO-GO :
   - Si PDF OK → Phase 2
   - Si PDF KO → Phase 1bis (solution custom)

**Livrable** : POC validé OU solution PDF identifiée

#### Phase 1bis - Solution PDF Custom (si nécessaire, 12-16h)

**Triggers** : mkdocs-with-pdf incompatible avec DSFR

**Options** :
- Option A : Custom CSS mkdocs-with-pdf pour DSFR (12-16h)
- Option B : Intégrer mkdocs-exporter (6-8h)
- Option C : Script Python Puppeteer/WeasyPrint (16-20h, complexe)

**Livrable** : Export PDF DSFR fonctionnel

#### Phase 2 - Migration Complète (12-18h)

**Prérequis** : Phase 1 validée (GO)

**Étapes** :
1. Adapter tous modules (6 modules DSFR-compatibles)
2. Assets DSFR :
   - Header logo République Française
   - Footer liens gouvernementaux
   - Police Marianne (auto-incluse)
   - Grille DSFR (12 colonnes)
3. CI/CD adaptation :
   - .github/workflows/build.yml
   - Dockerfile-dsfr
   - requirements-dsfr.txt
4. Tests E2E :
   - Adapter sélecteurs si nécessaire
   - 9 scénarios PASS
   - Coverage 89.6%+ maintenu
5. Documentation :
   - README.md : Migration DSFR
   - MIGRATION.md : Guide v1.0.x → v2.0.0
   - CHANGELOG.md : Breaking changes

**Livrable** : Infrastructure DSFR complète

#### Phase 3 - Validation & Release (4-6h)

**Étapes** :
1. Review complète :
   - Build strict PASS
   - PDF généré et accessible
   - Score 97/100 maintenu
   - Tous tests PASS
2. PR feature/dsfr-poc → main :
   - Titre : "feat: migration DSFR v2.0.0 (breaking change)"
   - Breaking changes documentés
   - Migration guide fourni
3. Release v2.0.0 :
   - Tag annoté v2.0.0
   - GitHub Release avec PDF
   - CHANGELOG finalisé

**Livrable** : v2.0.0 DSFR en production

**Estimation Totale Stratégie B** :
- Scénario optimiste (PDF OK direct) : 24-36h
- Scénario réaliste (PDF custom requis) : 36-48h
- Scénario pessimiste (blocages) : 48-56h

**Probabilité succès** : 85-90%

**Recommandation** : STRATÉGIE RECOMMANDÉE

---

### Stratégie C - Hybrid Progressive (Alternative)

**Approche** : DSFR header/footer custom sur Material (transition)

**Principe** :
- Conserver theme Material
- Override header/footer avec HTML DSFR-like
- Custom CSS grille/couleurs DSFR

**Avantages** :
- [COMPLETE] Préserve infrastructure Material (PDF, tests)
- [COMPLETE] Visuel DSFR progressif
- [COMPLETE] Risque minimal

**Inconvénients** :
- [NON-FAIT] Pas 100% DSFR officiel (custom override)
- [NON-FAIT] Maintenance double (Material + custom DSFR)
- [NON-FAIT] Migration DSFR complet repoussée

**Estimation** : 12-18h
**Recommandation** : Si domaine .gouv.fr retardé >6 mois

---

## Plan Exécution POC Phase 1 (Recommandé)

### Jour 1 - Setup (4h)

**Matin (2h)** :
```bash
# 1. Créer branche POC
git checkout main
git pull origin main
git checkout -b feature/dsfr-poc

# 2. Créer requirements-dsfr.txt
cat > requirements-dsfr.txt << EOF
mkdocs-dsfr>=0.11.0,<1.0.0
mkdocs-git-revision-date-localized-plugin>=1.2.0
pikepdf>=8.0.0
EOF

# 3. Créer mkdocs-dsfr.yml
cp mkdocs.yml mkdocs-dsfr.yml
# Éditer : theme.name = dsfr, ajouter config header/footer DSFR
```

**Après-midi (2h)** :
```bash
# 4. Installer deps POC
pip install -r requirements-dsfr.txt

# 5. Copier 1 module test
cp docs/modules/sircom.md docs/modules/sircom-dsfr-test.md

# 6. Build test
mkdocs build -f mkdocs-dsfr.yml

# 7. Vérifier scoring
python scripts/calculate_scores.py
```

**Critères succès J1** :
- [ ] Build DSFR sans erreur
- [ ] Header DSFR affiché
- [ ] Footer DSFR affiché
- [ ] Scoring fonctionne

**Livrable J1** : Build DSFR minimal opérationnel

---

### Jour 2 - Test PDF Critique (4h)

**Test 1 - mkdocs-with-pdf (2h)** :

```yaml
# mkdocs-dsfr-pdf.yml
theme:
  name: dsfr
  # Config DSFR complète

plugins:
  - search
  - dsfr_structure
  - with-pdf:
      output_path: exports/span-sg-dsfr.pdf
      enabled_if_env: ENABLE_PDF_EXPORT
      cover: true
      cover_title: "SPAN SG"
      cover_subtitle: "Secrétariat Général"
```

```bash
# Build PDF test
ENABLE_PDF_EXPORT=1 mkdocs build -f mkdocs-dsfr-pdf.yml

# Vérifier PDF généré
ls -lh site/exports/span-sg-dsfr.pdf

# Enrichir métadonnées
python scripts/enrich_pdf_metadata.py site/exports/span-sg-dsfr.pdf

# Valider PDF
qpdf --check site/exports/span-sg-dsfr.pdf
```

**Critères succès Test 1** :
- [ ] PDF généré sans erreur
- [ ] Métadonnées enrichies OK
- [ ] Taille fichier >500KB
- [ ] Contenu complet (31 points visibles)

**Test 2 - mkdocs-exporter (si Test 1 échoue, 2h)** :

```bash
pip install mkdocs-exporter

# Config alternative
# mkdocs-dsfr-pdf.yml
plugins:
  - search
  - dsfr_structure
  - exporter:
      formats:
        pdf:
          enabled: true
          output: exports/span-sg-dsfr.pdf
```

**Livrable J2** : Solution PDF DSFR validée

**GO/NO-GO Decision Point** :
- [COMPLETE] GO : PDF fonctionne → Planifier Phase 2
- [NON-FAIT] NO-GO : PDF KO → Phase 1bis (custom PDF)

---

### Jour 3 - Header/Footer + Validation (4h)

**Matin (2h)** :

```yaml
# mkdocs-dsfr.yml - Configuration complète
theme:
  name: dsfr
  language: fr

  intitule: "République <br> française"

  header:
    titre: "SPAN SG"
    sous_titre: "Schéma Pluriannuel d'Accessibilité Numérique"
    logo_url: /

  footer:
    description: "Secrétariat Général - Accessibilité Numérique 2025-2027"
    links:
      - name: legifrance.gouv.fr
        url: https://legifrance.gouv.fr
      - name: service-public.fr
        url: https://service-public.fr
      - name: data.gouv.fr
        url: https://data.gouv.fr
      - name: info.gouv.fr
        url: https://info.gouv.fr

  afficher_date_de_revision: true
  afficher_menu_lateral: true
  afficher_bouton_editer: true
  libelle_bouton_editer: "Éditer dans GitHub"
```

**Après-midi (2h)** :

```bash
# Tests complets POC
mkdocs build -f mkdocs-dsfr.yml  # HTML
mkdocs build -f mkdocs-dsfr-pdf.yml  # PDF
python scripts/calculate_scores.py  # Scoring
python scripts/enrich_pdf_metadata.py site/exports/span-sg-dsfr.pdf

# Vérifications visuelles
open site/index.html  # Header DSFR visible ?
open site/modules/sircom-dsfr-test/index.html  # Module OK ?
open site/exports/span-sg-dsfr.pdf  # PDF accessible ?
```

**Livrable J3** : POC DSFR complet validé

---

## Checklist GO/NO-GO

### Critères Techniques (Bloquants)
- [ ] Build DSFR fonctionne sans erreur
- [ ] Export PDF généré (mkdocs-with-pdf OU alternative)
- [ ] Métadonnées PDF accessibles (pikepdf)
- [ ] Scoring 31 points préservé (calculate_scores.py)
- [ ] Header DSFR affiché (logo RF, titre service)
- [ ] Footer DSFR affiché (liens gouv.fr)
- [ ] Police Marianne chargée
- [ ] Grille DSFR responsive

### Critères Organisationnels (Prérequis)
- [ ] Domaine .gouv.fr confirmé/réservé
- [ ] Validation sponsor Stéphane OK
- [ ] Ressources disponibles (24-48h dev)
- [ ] Fenêtre de tir v2.0.0 planifiée (3-4 semaines)

### Critères Qualité (Maintenabilité)
- [ ] Tests E2E adaptables (4h max)
- [ ] Score 97/100 maintenable
- [ ] Documentation migration complète
- [ ] Rollback possible (branche isolée)
- [ ] Breaking changes documentés

**Décision** :
- [COMPLETE] GO : Tous critères validés → Lancer Phase 2
- [NON-FAIT] NO-GO : 1+ critère bloquant → Stop ou Phase 1bis

---

## Roadmap Globale (v1.0.0 → v2.0.0)

```
v1.0.0 (Semaine courante) - POC Production-Ready
│
├─ POC-FINALISATION.md
│  ├─ Merge draft → main
│  ├─ GitHub Release officielle
│  └─ CHANGELOG finalisé
│
│
v1.0.x (Optionnel, hotfixes mineurs)
│
├─ Corrections bugs post-v1.0.0
│
│
v2.0.0-alpha (Semaine +1-2) - POC DSFR Technique
│
├─ feature/dsfr-poc
│  ├─ Setup mkdocs-dsfr (Jour 1)
│  ├─ Test export PDF (Jour 2)
│  ├─ Header/Footer validation (Jour 3)
│  └─ GO/NO-GO Decision
│
│
[Phase 1bis si nécessaire] - Solution PDF Custom
│
├─ mkdocs-with-pdf custom CSS (12-16h)
│  OU mkdocs-exporter (6-8h)
│  OU Puppeteer custom (16-20h)
│
│
v2.0.0-beta (Semaine +3-4) - Migration Complète
│
├─ Migration tous modules (6 modules)
├─ CI/CD adapté (workflows + Dockerfile)
├─ Tests E2E OK (9 scénarios)
├─ Documentation complète (MIGRATION.md)
└─ Review sponsor
│
│
v2.0.0 (Semaine +4-5) - Release DSFR Officielle
│
├─ Merge feature/dsfr-poc → main
├─ GitHub Release v2.0.0
│  ├─ PDF DSFR attaché
│  ├─ Breaking changes documentés
│  └─ Migration guide publié
├─ Deploy sur [NOM].gouv.fr
└─ Communication interne
```

**Timeline optimiste** : 4-5 semaines après v1.0.0
**Timeline réaliste** : 6-8 semaines (si PDF custom)

---

## Estimation Détaillée

### Scénario Optimiste (PDF OK direct)
```
POC Phase 1 : 12h
  ├─ J1 Setup : 4h
  ├─ J2 PDF test : 4h (succès)
  └─ J3 Validation : 4h

Migration Phase 2 : 12h
  ├─ Modules + assets : 6h
  ├─ CI/CD : 3h
  └─ Tests E2E : 3h

Release Phase 3 : 6h
  ├─ Review : 2h
  ├─ PR + merge : 2h
  └─ Release v2.0.0 : 2h

TOTAL : 30h
```

### Scénario Réaliste (PDF custom requis)
```
POC Phase 1 : 12h
  └─ Idem optimiste

POC Phase 1bis : 16h
  ├─ mkdocs-with-pdf custom CSS : 12h
  └─ Tests validation : 4h

Migration Phase 2 : 14h
  ├─ Modules + assets : 6h
  ├─ CI/CD + PDF : 5h
  └─ Tests E2E : 3h

Release Phase 3 : 6h
  └─ Idem optimiste

TOTAL : 48h
```

### Scénario Pessimiste (blocages multiples)
```
POC + PDF custom complexe : 24h
  ├─ Phase 1 : 12h
  ├─ Phase 1bis échec option A : 12h
  └─ Option B (exporter) : +8h = 20h
  OU Option C (Puppeteer) : +20h = 32h

Migration + bugs : 20h
  ├─ Modules : 8h
  ├─ CI/CD debug : 8h
  └─ Tests corrections : 4h

Tests + corrections : 12h
  ├─ E2E adaptations : 6h
  ├─ Scoring debug : 2h
  └─ PDF finitions : 4h

TOTAL : 56h
```

---

## Critères d'Acceptation

### Fonctionnels
- [ ] Theme DSFR affiché (header, footer, navigation)
- [ ] Logo République Française visible
- [ ] Police Marianne chargée
- [ ] Grille DSFR 12 colonnes fonctionnelle
- [ ] Liens footer gouv.fr actifs
- [ ] Export PDF généré avec DSFR
- [ ] Scoring 31 points DINUM maintenu (45/186)

### Techniques
- [ ] Build strict PASS (mkdocs build --strict)
- [ ] Tests unitaires : 21 PASS
- [ ] Tests E2E : 9 PASS
- [ ] Coverage : 89.6%+ maintenu
- [ ] PDF métadonnées enrichies (pikepdf)
- [ ] CI/CD workflows adaptés
- [ ] Dockerfile-dsfr fonctionnel

### Documentation
- [ ] MIGRATION.md créé (guide v1.0.x → v2.0.0)
- [ ] CHANGELOG.md mis à jour (breaking changes v2.0.0)
- [ ] README.md adapté (stack DSFR)
- [ ] CONTRIBUTING.md vérifié (workflow inchangé)
- [ ] Roadmap S7-01 complétée

### Qualité
- [ ] Score qualité : 97/100 maintenu
- [ ] Accessibilité : 100% DSFR (RGAA natif)
- [ ] Performance : Build time <5 min
- [ ] Compatibilité : Chrome, Firefox, Safari, Edge

### Validation
- [ ] Review sponsor Stéphane OK
- [ ] Domaine .gouv.fr actif
- [ ] Release v2.0.0 publiée
- [ ] PDF téléchargeable GitHub Release

---

## Dépendances

### Bloquants (Prérequis absolus)
- [COMPLETE] v1.0.0 en production stable
- [NON-FAIT] Domaine .gouv.fr confirmé et réservé
- [NON-FAIT] POC Phase 1 validé (PDF fonctionne)
- [NON-FAIT] Validation sponsor Stéphane

### Recommandés
- [COMPLETE] POC-FINALISATION terminée
- [COMPLETE] Score 97/100 atteint
- [EN-COURS] Modules optionnels (S6-03 à S6-06) complétés

### Bloque
- Release v2.1.0 (évolutions post-DSFR)
- Migration organisation GitHub gouvernementale
- Communication production finale

---

## Risques & Mitigations

### Risque 1 : PDF incompatible DSFR
**Probabilité** : Élevée (60-70%)
**Impact** : Critique (bloquant)

**Mitigation** :
- POC Phase 1 obligatoire (test avant migration)
- 3 solutions alternatives prêtes (custom CSS, exporter, Puppeteer)
- Budget temps 12-20h solution custom

### Risque 2 : Domaine .gouv.fr retardé
**Probabilité** : Moyenne (30-40%)
**Impact** : Bloquant (licence Marianne)

**Mitigation** :
- Validation organisationnelle AVANT lancement POC
- Stratégie C (hybrid) possible si délai >6 mois
- Communication sponsor transparente

### Risque 3 : Tests E2E massivement impactés
**Probabilité** : Faible (20%)
**Impact** : Moyen (retard release)

**Mitigation** :
- Tests HTTP basiques (pas CSS Material-specific)
- Budget 4h adaptation scénarios
- Rollback possible (branche isolée)

### Risque 4 : Score qualité régresse
**Probabilité** : Faible (15%)
**Impact** : Moyen

**Mitigation** :
- Tests systématiques chaque phase
- Critères acceptation stricts
- Validation continue score 97/100

---

## Recommandation Finale

### Actions Immédiates (Cette Semaine)
1. **Terminer POC-FINALISATION v1.0.0** (priorité P0)
   - Stabiliser infrastructure actuelle
   - Release officielle GitHub
   - Ne PAS commencer migration DSFR

### Actions Court Terme (Semaine +1)
2. **Validation organisationnelle**
   - Confirmer domaine .gouv.fr (date obtention)
   - Validation sponsor Stéphane (calendrier)
   - Créer issue GitHub "POC Migration DSFR v2.0.0"

### Actions Moyen Terme (Semaine +2-3)
3. **Exécuter POC DSFR Phase 1** (12h)
   - Branche feature/dsfr-poc
   - Test PDF critique (GO/NO-GO)
   - Documentation decision

### Actions Long Terme (Semaine +4-5)
4. **Migration DSFR Complète** (si GO)
   - Phase 2 : Tous modules
   - Phase 3 : Release v2.0.0
   - Breaking change assumé

**Timing optimal** : v2.0.0 DSFR lancée 4-6 semaines après v1.0.0

**Conditions préalables** :
- [COMPLETE] v1.0.0 en production
- [NON-FAIT] Domaine .gouv.fr confirmé
- [NON-FAIT] POC Phase 1 OK (PDF)
- [NON-FAIT] Sponsor validé
- [NON-FAIT] Ressources 48h disponibles

---

**Date création** : 2025-10-07
**Auteur** : Claude Code (ultrathink)
**Status** : Planifiée (trigger : v1.0.0 + .gouv.fr)
**Version** : 1.0

Closes: Migration DSFR complet (v2.0.0 breaking change)
