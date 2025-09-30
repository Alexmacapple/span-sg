# Claude.md – Configuration d’agent pour Claude Code

Version: 1.0
Date: 2025-09-30

[system]
- Répondre en français, sans émojis, concision.
- Respecter strictement le MVP et le cahier des charges.
- Ne pas modifier la logique de scoring: 31 points balisés `<!-- DINUM -->` uniquement.
- Ne pas ajouter de dépendances ni de nouveaux plugins CI.

[goals]
- Maintenir le PRD, README, docs et modules.
- Garantir la cohérence MkDocs (strict) et la nav.
- Assurer la préparation de release (CHANGELOG, tags) sans toucher à la CI.

[constraints]
- Périmètre v1: 6 modules (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS).
- Aucune fonctionnalité hors périmètre (dashboard, API, notifications).
- Preview privée via GitHub Pages organisation uniquement.
- Respect de la structure et des blocs légaux.

[repository]
- CI: `.github/workflows/build.yml`
- Script: `scripts/calculate_scores.py`
- Docs: `docs/` (modules, index, processus)
- Config MkDocs: `mkdocs.yml` (+ fichiers PDF)
- PRD: `PRD-v3.3.md`

[actions-examples]
- Mettre à jour `docs/modules/sircom.md` (sections 5 obligatoires, ne pas toucher aux 31 lignes DINUM sauf [x]).
- Renseigner `site_url`/`repo_url` dans `mkdocs.yml`.
- Ajouter URL de déclaration d’accessibilité réelle dans un module.
- Rédiger `CHANGELOG.md` pour v0.1.1.

[safety]
- Ne jamais commiter de secrets.
- Ne jamais publier une preview publique.
- Garder des messages de commit explicites et limités au périmètre des fichiers modifiés.
