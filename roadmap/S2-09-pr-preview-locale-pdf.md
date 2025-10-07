# S2-09 – PR: désactivation Pages et revue locale/PDF

Objectif
- Formaliser la PR alignant la politique “sans Pages” et la revue locale/PDF.

Détails PR
- Titre: docs: désactive la preview Pages et formalise la revue locale/PDF
- Base: draft
- Compare: feature/docs-preview-local-pdf
- Commit: docs: désactive la preview Pages et formalise la revue locale/PDF
- Lien direct (une fois la branche poussée):
  - https://github.com/Alexmacapple/span-sg-repo/compare/draft...feature/docs-preview-local-pdf?expand=1

Contenu modifié
- README.md, docs/dev-local.md, docs/contributing.md, CONTRIBUTING.md
- documentation/options-preview-privee.md
- .github/PAGES-ACCESS-CHECKLIST.md (Scénario B + Journal)
- mkdocs.yml (vérifications commentées, strict conservé)
- roadmap/S2-01-github-actions.md, roadmap/S2-03-preview-privee.md, roadmap/templates/presentation-sponsor-slides.md (note de politique)

Checklist PR
- [ ] 31 balises DINUM inchangées (ou 0 si module vide)
- [ ] Front-matter modules présent (service, referent, updated)
- [ ] Aucun lien public “/draft” restant dans la doc
- [ ] mkdocs build strict OK
- [ ] PDF disponible via build/artefact

Commandes
```bash
# Créer et pousser la branche
git checkout -b feature/docs-preview-local-pdf
git add -A
git commit -m "docs: désactive la preview Pages et formalise la revue locale/PDF"
git push -u origin feature/docs-preview-local-pdf

# Ouvrir la PR (UI) :
# https://github.com/Alexmacapple/span-sg-repo/compare/draft...feature/docs-preview-local-pdf?expand=1
```

Validation
- Review: Bertrand, Alex
- GO final contenu: Alexandra
