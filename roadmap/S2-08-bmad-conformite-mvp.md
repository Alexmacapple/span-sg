# S2-08 – Conformité MVP (BMAD)

> Objectif: assurer la conformité stricte au périmètre MVP (MkDocs strict, scoring DINUM, preview privée) et cadrer les actions associées.

## BMAD — Besoins
- Garantir `strict: true` et URLs `site_url`/`repo_url` correctes dans `mkdocs.yml`.
- Assurer une preview GitHub Pages privée (org‑only) documentée.
- Harmoniser les modules: front‑matter, blocs légaux/TODO, 31 points DINUM sans ajout.
- Centraliser les consignes agent dans `AGENTS.md` (éviter duplications).

## BMAD — Mesures
- Build MkDocs passe sans erreurs: `mkdocs build -f mkdocs.yml` (0 erreurs bloquantes).
- Scoring: `python3 scripts/calculate_scores.py` s’exécute et met à jour la synthèse.
- Liens valides dans `docs/` (scan simple: liens relatifs non 404).
- Preview privée: checklist `.github/PAGES-ACCESS-CHECKLIST.md` complétée et publiée.

## BMAD — Actions
- [ ] Renseigner `site_url` et `repo_url` dans `mkdocs.yml` (owner: Docs) — DDJ: AAAA‑MM‑JJ.
- [ ] Vérifier `strict: true` et corriger warnings bloquants (owner: CI) — `mkdocs build`.
- [ ] Ajouter `.github/PAGES-ACCESS-CHECKLIST.md` (owner: Ops) — contenu: règles org‑only, tests d’accès.
- [ ] Audit modules `docs/modules/*.md` (owner: PO): front‑matter (`service`, `referent`, `updated`), blocs légaux/TODO, pas de nouvelles balises `<!-- DINUM -->`.
- [ ] Unifier les consignes dans `AGENTS.md` et référencer les doublons (owner: Docs).

## BMAD — Décisions
- Go publication `draft` si 4 mesures OK et aucune régression de scoring.
- Go `main` si preview privée validée par SNUM et build prod sans erreurs.

## Entrées
- `mkdocs.yml`, `.github/workflows/build.yml`, `scripts/calculate_scores.py`.
- `docs/modules/*.md`, `AGENTS.md`, `docs/synthese.md`.

## Livrables
- `AGENTS.md` finalisé, `.github/PAGES-ACCESS-CHECKLIST.md` présent.
- Modules conformes et synthèse régénérée par la CI.
