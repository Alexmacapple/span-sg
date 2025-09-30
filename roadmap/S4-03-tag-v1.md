# Story S4-03 : Tag v1.0.0 et préparation release

**Phase** : Semaine 4 - Production
**Priorité** : Critique
**Estimation** : 1h
**Assigné** : Alexandra

---

## Contexte projet

Le **tag Git** est l'étape formelle de versioning qui marque une release. Pour SPAN SG v1.0.0, il :
- Fige l'état du code à un instant T
- Permet de référencer cette version précise
- Trigger des workflows CI (si configurés)
- Sert de base pour la release GitHub

Convention de versioning : **Semantic Versioning (semver)** `MAJOR.MINOR.PATCH`
- v1.0.0 = première release production
- v1.0.1 = correction bug
- v1.1.0 = nouvelle fonctionnalité
- v2.0.0 = breaking change

Cette story comprend :
1. Préparer `CHANGELOG.md`
2. Mettre à jour les versions dans les fichiers concernés
3. Créer le tag Git annoté
4. Pusher le tag
5. Préparer les assets pour la release GitHub

---

## Objectif

Créer et pusher le tag `v1.0.0`, préparer le CHANGELOG, et rassembler les assets nécessaires pour la release GitHub (S4-04).

---

## Prérequis

- [ ] Story S4-02 complétée (GO Yves obtenu)
- [ ] Branche `draft` à jour et stable
- [ ] PDF synthèse généré (artefact CI)
- [ ] Décision GO/NO-GO documentée

---

## Étapes d'implémentation

### Option automatique (recommandée) : Script release.sh

```bash
./scripts/release.sh v1.0.0
```

Le script automatise toutes les étapes ci-dessous :
- Vérifications prérequis
- Mise à jour CHANGELOG
- Test build et scoring
- Création tag annoté
- Préparation release notes

Passer à S4-04 (Publication) si succès.

---

### Option manuelle (si script non disponible)

### 1. Vérifier l'état actuel

```bash
git checkout draft
git pull origin draft
git status
# Attendu : working tree clean

# Vérifier dernier tag (si existant)
git tag -l
# Attendu : (vide) ou tags antérieurs
```

### 2. Créer/mettre à jour CHANGELOG.md

Si `CHANGELOG.md` n'existe pas, le créer :
```markdown
# Changelog SPAN SG

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [1.0.0] - 2025-09-30

### Ajouté
- 6 modules services initiaux (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- Template officiel avec 31 points DINUM
- Script de scoring automatique (`scripts/calculate_scores.py`)
- Génération synthèse globale (`docs/synthese.md`)
- CI/CD GitHub Actions (build + PDF + deploy)
- Export PDF avec fallback robuste (`mkdocs-pdf-export-plugin` + `mkdocs-with-pdf`)
- Preview privée GitHub Pages (org-only)
- Documentation contributeur (`CONTRIBUTING.md`)
- Guide formation Git (`docs/formation/git-basics.md`)
- Configuration MkDocs Material (strict mode)

### Conformité
- Déclarations d'accessibilité : 6/6 modules renseignés
- Analyse charge disproportionnée : Complétée
- Score global initial : [X/186] ([Y%])

### Infrastructure
- Repository GitHub avec branches `main` (production) et `draft` (preview)
- Protection branches configurée
- Artefacts CI : `site/` + `exports/span-sg.pdf`
- Déploiement automatique vers GitHub Pages

### Documentation
- `PRD-v3.3.md` : Product Requirements Document complet
- `CLAUDE.md` : Instructions pour Claude Code
- `Agents.md` : Instructions pour autres AI coding assistants
- `GO-CHECKLIST.md` : Checklist validation pré-production
- `.github/PAGES-ACCESS-CHECKLIST.md` : Configuration Pages org-only

### Décisions
- Preview privée : Option A (GitHub Pages org-only)
- PDF d'archive : Double stratégie (plugin + fallback)
- Workflow : feature → draft → main
- Périmètre v1 : 6 modules uniquement

---

## [Unreleased]
<!-- Futures modifications pour v1.1.0+ -->

---

[1.0.0]: https://github.com/span-sg/span-sg/releases/tag/v1.0.0
```

**Si CHANGELOG.md existe déjà**, ajouter section v1.0.0 en tête.

### 3. Mettre à jour les versions dans les fichiers

**PRD-v3.3.md** :
```markdown
**Version** 3.3 → **Version 3.3 (v1.0.0 release)**
**Date** 30 septembre 2025 → **Date** [date du jour]
```

**README.md** (ajouter badge version) :
```markdown
# SPAN SG

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Build Status](https://github.com/span-sg/span-sg/workflows/Build%20SPAN/badge.svg)

...
```

**docs/index.md** (optionnel) :
```markdown
*Version actuelle : 1.0.0 - Publié le [JJ/MM/AAAA]*
```

### 4. Committer les modifications

```bash
git add CHANGELOG.md PRD-v3.3.md README.md docs/index.md
git commit -m "chore: prepare release v1.0.0

- Add CHANGELOG.md v1.0.0 entry
- Update version badges
- Update PRD date

Release notes: See CHANGELOG.md
Sponsor approval: decisions/v1.0/DECISION-GO-NO-GO-v1.0.md
"
git push origin draft
```

### 5. Attendre validation CI

Observer GitHub Actions :
- ✅ Build passe
- ✅ Scoring OK
- ✅ PDF généré
- ✅ Artefacts disponibles

### 6. Créer le tag Git annoté

```bash
# Tag annoté (recommandé pour releases)
git tag -a v1.0.0 -m "Release SPAN SG v1.0.0

Première release production du Schéma Pluriannuel d'Accessibilité Numérique.

Highlights:
- 6 modules services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- Score global: [X/186] ([Y%])
- CI/CD complète avec export PDF
- Preview privée org-only

Sponsor approval: Yves (30/09/2025)
Reviewers: Bertrand, Alex
"
```

**Vérifier le tag** :
```bash
git tag -l
# Attendu : v1.0.0

git show v1.0.0
# Affiche commit + message tag
```

### 7. Pusher le tag vers origin

```bash
git push origin v1.0.0
```

Observer sur GitHub :
- Tags : https://github.com/span-sg/span-sg/tags
- Le tag `v1.0.0` apparaît

### 8. Télécharger les artefacts CI pour release

Aller sur GitHub Actions → dernier run sur `draft` → Artifacts → Télécharger `span-site`

Extraire :
```bash
unzip span-site.zip
ls site/ exports/
# Attendu : site/ complet + exports/span-sg.pdf
```

### 9. Préparer les release notes détaillées

Créer `RELEASE-NOTES-v1.0.0.md` (fichier temporaire) :
```markdown
# SPAN SG v1.0.0 - Release Notes

**Date de publication** : [JJ/MM/AAAA]
**Tag** : `v1.0.0`

---

## 🎉 Première release production

Le Schéma Pluriannuel d'Accessibilité Numérique du Secrétariat Général est maintenant disponible en production.

---

## 📊 Vue d'ensemble

- **6 modules services** : SNUM, SIRCOM, SRH, SIEP, SAFI, BGS
- **Score global** : [X/186] ([Y%])
- **31 points DINUM** par module (référentiel officiel)
- **Génération automatique** de la synthèse
- **Export PDF** disponible en téléchargement

---

## ✨ Fonctionnalités principales

### Modules services
Chaque service dispose de son propre module avec :
- Périmètre (applications, sites, démarches)
- État des lieux (audits, scores RGAA)
- Organisation (référent, équipe, ETP)
- Plan d'action annuel (actions prioritaires 2025)
- Indicateurs clés (conformité, formations, marchés)

### Scoring automatique
- 31 points de contrôle officiels DINUM
- Calcul automatique checked/total par module
- Synthèse globale avec statuts (Conforme ≥75%, En cours, Non renseigné)
- Validation périmètre (0 ou 31 points requis)

### CI/CD robuste
- Build automatique à chaque push
- Export PDF avec fallback (2 plugins)
- Déploiement GitHub Pages
- Artefacts disponibles 90 jours

### Documentation
- Guide contributeur (interface web + Git local)
- Formation Git 2h
- Checklists validation
- PRD complet v3.3

---

## 📦 Assets disponibles

- **Site HTML** : https://span-sg.github.io/span-sg/
- **PDF d'archive** : [Lien ci-dessous]
- **Code source** : https://github.com/span-sg/span-sg

---

## 🔐 Conformité

- ✅ Déclarations d'accessibilité : 6/6 modules
- ✅ Analyse charge disproportionnée : Complétée
- ✅ Référentiel DINUM : 31 points respectés
- ✅ RGAA 4.x : Niveau AA cible

---

## 👥 Équipe

- **Product Owner** : Alexandra
- **Validateurs** : Bertrand, Alex
- **Sponsor** : Yves
- **Contributeurs** : Référents services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)

---

## 🚀 Prochaines étapes

- **v1.0.1** : Corrections mineures post-production
- **v1.1.0** : Ajout fonctionnalités (matrice priorisation étendue)
- **v2.0.0** : Extension à d'autres directions (phase 2)

---

## 📝 Changelog complet

Voir [CHANGELOG.md](CHANGELOG.md)

---

**Validé par** : Yves (Sponsor), Bertrand (Validateur), Alex (Validateur)
**Date de validation** : 30/09/2025
```

---

## Critères d'acceptation

- [ ] `CHANGELOG.md` créé avec section v1.0.0
- [ ] Versions mises à jour dans PRD, README, docs/index.md
- [ ] Commit "prepare release v1.0.0" poussé sur draft
- [ ] CI passe sans erreur
- [ ] Tag `v1.0.0` créé (annoté)
- [ ] Tag poussé vers origin
- [ ] Tag visible sur GitHub : https://github.com/.../tags
- [ ] Artefacts CI téléchargés (site/ + PDF)
- [ ] `RELEASE-NOTES-v1.0.0.md` préparées

---

## Tests de validation

```bash
# Test 1 : CHANGELOG existe et contient v1.0.0
grep -q "## \[1.0.0\]" CHANGELOG.md && echo "OK" || echo "FAIL"

# Test 2 : Tag existe localement
git tag | grep -q "v1.0.0" && echo "OK" || echo "FAIL"

# Test 3 : Tag existe sur origin
git ls-remote --tags origin | grep -q "v1.0.0" && echo "OK" || echo "FAIL"

# Test 4 : Tag annoté (pas lightweight)
git cat-file -t v1.0.0 | grep -q "tag" && echo "OK" || echo "FAIL"

# Test 5 : Artefacts PDF disponibles
test -f exports/span-sg.pdf && test -s exports/span-sg.pdf && echo "OK" || echo "FAIL"

# Test 6 : Release notes préparées
test -f RELEASE-NOTES-v1.0.0.md && echo "OK" || echo "FAIL"
```

---

## Dépendances

**Bloque** :
- S4-04 (publication utilise le tag v1.0.0)

**Dépend de** :
- S4-02 (GO Yves nécessaire avant tag)

---

## Références

- **PRD v3.3** : Section 9 "Release en 5 étapes"
- **CHANGELOG.md** : Fichier à créer/mettre à jour
- **CLAUDE.md** : Section "Processus de release"
- **Semantic Versioning** : https://semver.org/

---

## Notes et risques

**Erreur après tag**
Si découverte d'un bug critique après push du tag :
- Ne PAS supprimer le tag (mauvaise pratique)
- Créer tag v1.0.1 avec correction
- Documenter dans CHANGELOG.md

**Tag lightweight vs annoté**
Toujours utiliser tag **annoté** (`-a`) pour releases :
- Contient metadata (auteur, date, message)
- Signable GPG (si nécessaire)
- Meilleures pratiques Git

**Versioning futur**
Conventions pour versions suivantes :
- v1.0.1, v1.0.2 : Patches (bugs, typos)
- v1.1.0, v1.2.0 : Features (nouveaux modules, améliorations)
- v2.0.0 : Breaking changes (changement structure, nouveau référentiel)

**CHANGELOG maintenance**
Tenir à jour CHANGELOG.md pour chaque release :
- Section `[Unreleased]` pour travaux en cours
- Migrer vers `[X.Y.Z]` lors du tag
- Liens vers releases GitHub en bas

**Date dans CHANGELOG**
Utiliser format ISO : `AAAA-MM-JJ` (tri chronologique facile).

---

## Post-tâche

Créer un script helper pour futures releases :
```bash
cat > scripts/release.sh << 'EOF'
#!/bin/bash
set -e

VERSION=$1

if [ -z "$VERSION" ]; then
  echo "Usage: ./scripts/release.sh vX.Y.Z"
  exit 1
fi

echo "🚀 Preparing release $VERSION"

# 1. Update CHANGELOG
echo "- Update CHANGELOG.md with version $VERSION"
# (manuel pour v1.0, automatiser avec changelog-cli pour v1.1+)

# 2. Commit
git add CHANGELOG.md README.md
git commit -m "chore: prepare release $VERSION"
git push origin draft

# 3. Wait CI
echo "⏳ Waiting for CI... (check GitHub Actions manually)"
read -p "Press Enter when CI is green..."

# 4. Tag
git tag -a "$VERSION" -m "Release SPAN SG $VERSION"
git push origin "$VERSION"

echo "✅ Release $VERSION tagged and pushed!"
echo "Next: Create GitHub release at https://github.com/.../releases/new"
EOF

chmod +x scripts/release.sh
```

Documenter le process :
```markdown
## Release process

1. Mettre à jour `CHANGELOG.md`
2. Commit : `git commit -m "chore: prepare release vX.Y.Z"`
3. Attendre CI vert
4. Tag : `git tag -a vX.Y.Z -m "Release SPAN SG vX.Y.Z"`
5. Push : `git push origin vX.Y.Z`
6. Créer release GitHub (S4-04)

OU utiliser : `./scripts/release.sh vX.Y.Z`
```

Notifier l'équipe :
```
📧 À : Équipe SPAN
Objet : SPAN SG v1.0.0 - Tag créé

Le tag v1.0.0 a été créé et poussé !

🏷️ Tag : https://github.com/span-sg/span-sg/releases/tag/v1.0.0

Prochaine étape : Publication production (S4-04)

Alexandra
```