# Repository Guidelines

Ce dépôt documente SPAN SG avec MkDocs. Suivre ces règles pour des contributions rapides et sûres.

## Structure du projet et modules
- `docs/` contenus publiés; `docs/modules/*.md` (6 services: SNUM, SIRCOM, SRH, SIEP, SAFI, BGS).
- `PRD-v3.3.md`, `docs/processus.md` référentiels produit/processus.
- `scripts/calculate_scores.py` calcul du scoring (31 points DINUM).
- `mkdocs.yml`, `mkdocs-with-pdf.yml`, `mkdocs-pdf.yml` configuration site/PDF.
- `.github/workflows/build.yml` CI; `gh-pages` pour la preview.

## Build, preview et utilitaires
- `mkdocs serve -f mkdocs.yml -a 0.0.0.0:8000` prévisualisation locale.
- `mkdocs build -f mkdocs.yml` build strict (doit passer sans warnings bloquants).
- `python3 scripts/calculate_scores.py` recalcul des scores (ne pas changer la règle DINUM).
- `mkdocs build -f mkdocs-with-pdf.yml` génération PDF (fallback prévu).

## Style et conventions
- Markdown clair, titres hiérarchisés, listes courtes; pas d’émojis.
- Indentation 2 espaces. Liens relatifs valides uniquement.
- Modules: front‑matter requis (`service`, `referent`, `updated: AAAA-MM-JJ`).
- Ne pas créer de nouvelles balises `<!-- DINUM -->`; cocher uniquement les 31 existantes.

## Vérifications et tests
- Pas de tests unitaires; valider: build MkDocs OK, scoring OK, liens OK.
- La CI regénère `docs/synthese.md`. Ne pas modifier les workflows.

## Commits et Pull Requests
- Branches: `draft` (preview), `main` (prod), `feature/update-<service>`, `hotfix/<résumé>`.
- Messages: `feat(service): …`, `fix(orthographe): …`, `chore(release): …`.
- PR vers `draft` avec description courte et checklist: 31 points (ou 0 si vide), front‑matter, blocs légaux/TODO, liens valides, aucun secret.
- Release: éditer `CHANGELOG.md`; tag proposé `git tag -a vX.Y.Z -m "Release SPAN SG vX.Y.Z"`.

## Garde‑fous sécurité & configuration
- Aucune nouvelle dépendance ni script additionnel. Préserver `strict: true` dans `mkdocs.yml`.
- Preview GitHub Pages privée (org‑only) — vérifier `.github/PAGES-ACCESS-CHECKLIST.md`.
- N’exposez aucun identifiant générique ni donnée sensible.

