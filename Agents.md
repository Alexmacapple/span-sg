# Agents.md – Configuration d’agent pour Codex / Cursor / Builder.io

Version: 1.0
Date: 2025-09-30

## Objet
Fournir des instructions d’agent standardisées pour travailler sur le repo SPAN SG en “vibe coding” tout en respectant le MVP et le cahier des charges.

## Langue par défaut
- Français uniquement
- Pas d’émojis
- Ton concis, orienté action
- Ne pas sur-ingénierie

## Périmètre MVP à respecter
- 6 modules v1: SNUM, SIRCOM, SRH, SIEP, SAFI, BGS
- Scoring strict sur 31 points balisés `<!-- DINUM -->`
- Pas de dashboard, pas d’API, pas de notifications, pas de métriques automatiques
- MkDocs + GitHub Actions + GitHub Pages (preview org-only) + PDF avec fallback
- Preview privée: membres de l’organisation seulement

## Responsabilités agent
- Mettre à jour la documentation (PRD, README, docs/)
- Éditer les modules Markdown côté `docs/modules/` en respectant le template
- Lancer/adapter `scripts/calculate_scores.py` si besoin (sans modifier la règle DINUM)
- Préparer les releases (CHANGELOG, tags) sans modifier la CI
- Vérifier que `mkdocs.yml` reste strict et que la nav est cohérente

## Rôles
- Product Owner: Alexandra
- Validateurs: Bertrand, Alex
- Sponsor: Stéphane (Chef mission numérique SNUM-SG, validation conceptuelle)
- Validation finale production: Chef SNUM

## Conventions de branches
- `draft`: preview
- `main`: production
- `feature/update-<service>`: changements par service
- `hotfix/…`: urgences vers `main`

## Checklist PR minimale
- 31 points DINUM présents (ou 0 pour module vide)
- Front-matter présent (service, referent, updated)
- Blocs légaux remplis ou placeholder TODO
- Liens valides, pas de secrets
- `docs/synthese.md` regénéré par CI

## Garde-fous
- Ne jamais introduire de nouvelles cases `<!-- DINUM -->` hors des 31 points
- Ne pas ajouter de dépendances ni scripts supplémentaires
- Ne pas exposer d’identifiants génériques
- Préserver `strict: true` dans `mkdocs.yml`

## Tâches types (prompts)
- “Mettre à jour le plan d’action 2025 de SIRCOM en gardant les 31 points inchangés”
- “Ajouter l’URL réelle de déclaration d’accessibilité pour SAFI”
- “Corriger une faute dans docs/index.md sans modifier la nav”
- “Préparer le changelog v0.1.1 et tag”

## Cartographie des fichiers utiles
- PRD: `PRD-v3.3.md`
- CI: `.github/workflows/build.yml`
- Script scoring: `scripts/calculate_scores.py`
- MkDocs: `mkdocs.yml`, `mkdocs-pdf.yml`, `mkdocs-with-pdf.yml`
- Modules: `docs/modules/*.md`
- Processus: `docs/processus.md`

## Sorties attendues
- Commits atomiques, messages clairs
- PR vers `draft` avec checklist PR
- Aucun changement sur le comptage DINUM hormis checks [x]


## Prompts types (à copier-coller)

### Mise à jour d’un module (contenu sans toucher au scoring)
Objectif: mettre à jour le plan d’action 2025 d’un service sans modifier les 31 points DINUM.
Prompt:
> Mets à jour `docs/modules/SERVICE.md` en complétant les sections **1. Périmètre**, **2. État des lieux**, **3. Organisation**, **4. Plan d’action annuel**, **5. Indicateurs clés**.  
> Ne modifie pas les 31 lignes balisées `<!-- DINUM -->` hors des coches `[x]`.  
> Conserve la structure du tableau et ajoute 3 actions prioritaires réalistes avec statuts.

### Renseigner l’URL de déclaration d’accessibilité
> Dans `docs/modules/SERVICE.md`, remplace le placeholder de “Déclaration d’accessibilité” par l’URL réelle.  
> Si non disponible, laisse le placeholder et ajoute un TODO avec la date du jour.

### Compléter “Analyse charge disproportionnée” (si applicable)
> Dans `docs/modules/SERVICE.md`, complète la section **Analyse charge disproportionnée** pour l’élément X avec: justification, alternative, date de révision.  
> Ne pas cocher de nouvelles cases DINUM.

### Ajouter une “Matrice de priorisation”
> Dans `docs/modules/SERVICE.md`, renseigne la **Matrice de priorisation** avec 3 lignes max (services/applications critiques).  
> Ne change pas les 31 points DINUM.

### Corriger orthographe/typos (docs/index.md ou PRD)
> Corrige les fautes typographiques dans `docs/index.md` (ou `PRD-v3.3.md`) sans modifier la structure de la nav MkDocs ni ajouter de dépendances.

### Préparer une micro-release v0.1.1 (sans CI nouvelle)
> Crée la section `## v0.1.1 – AAAA-MM-JJ` dans `CHANGELOG.md` (3 puces max: ajout/correctif).  
> Ne modifie pas `.github/workflows/build.yml`.  
> Propose le tag et le message: `git tag -a v0.1.1 -m "Release SPAN SG v0.1.1"`.

### Renseigner site_url et repo_url
> Dans `mkdocs.yml`, remplace les placeholders de `site_url` et `repo_url` par les URLs de l’organisation.  
> Ne touche pas aux plugins ni à `strict: true`.

### Vérifier la preview privée (Pages org-only)
> Vérifie `.github/PAGES-ACCESS-CHECKLIST.md`.  
> Confirme que la preview `draft/` est servie depuis `gh-pages` et inaccessible à un compte externe.

### Hotfix critique vers production
> Crée une branche `hotfix/<résumé>` à partir de `main`.  
> Fais la correction minimale dans le fichier `docs/modules/SERVICE.md`.  
> PR vers `main` avec validation Bertrand/Alex.  
> Ne modifie pas les 31 points DINUM hors coches `[x]`.

### Checklist PR automatique (rappel)
> Vérifie 31 points DINUM (ou 0 si module vide), front-matter, blocs légaux, liens valides, pas de secrets, et laisse la synthèse à la CI.

### Modèle de message de commit
> `feat(service): ajoute 2 actions au plan 2025 sans changer le scoring`  
> `fix(orthographe): corrige coquille dans index.md`  
> `chore(release): prépare CHANGELOG v0.1.1`
