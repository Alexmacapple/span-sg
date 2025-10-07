# Preview privée GitHub Pages — Checklist

Contexte
- GitHub.com sans Enterprise Cloud: pas de Pages privées. Toute page publiée est publique.
- Seules les organisations Enterprise Cloud peuvent activer "Private Pages" (visibilité org-only).
- Si Private Pages indisponible: ne pas activer Pages; utiliser artefacts Actions/PDF pour la preview interne.

## Scénario A — Private Pages disponible (Enterprise)
- [ ] Org: Settings > Pages > activer Private Pages (org-only)
- [ ] Repo: Settings > Pages > Source = GitHub Actions
- [ ] Déploiement: branche `gh-pages`, répertoire racine, site sous `/draft/`
- [ ] Test externe (compte hors org): accès refusé (403/404)
- [ ] Test interne (membre org): accès OK à `/draft/`

## Scénario B — Pas de Private Pages (par défaut sur GitHub.com)
- [ ] Désactiver Pages (aucune publication publique du site)
- [ ] CI: conserver le build, publier les artefacts du site (zip) accessibles aux membres ayant accès au dépôt
- [ ] Partage: fournir le PDF généré par la CI comme fallback de lecture
- [ ] Local: reviewers exécutent `mkdocs serve` ou ouvrent l’artefact `index.html` en local

## Contrôles communs
- [ ] `mkdocs build -f mkdocs.yml` OK (`strict: true`)
- [ ] `python3 scripts/calculate_scores.py` OK, pas de modification des règles DINUM
- [ ] Liens valides, absence de secrets, front-matter modules présent

## Journal
- Date du contrôle: 2025-10-07
- Contrôleur: à renseigner
- Scénario: B (Sans Pages — revue locale/PDF)
- Notes: Pages désactivé; reviewers utilisent `mkdocs serve` en local et le PDF généré par la CI pour lecture/partage. Aucune publication publique avant validation.
