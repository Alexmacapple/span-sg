# S2-10 — PRD express: Actions prioritaires (rapides)

Objectif
- Garantir une mise au clair immédiate de la politique “sans Pages”, la qualité des modules et la reproductibilité build/PDF sans toucher à la CI.

Périmètre
- Documentation, configuration MkDocs et vérifications locales. Aucune modification de workflow CI.

Tâches prioritaires (Do Now)
- [ ] Vérifier le workflow CI (lecture seule): `.github/workflows/build.yml` — confirmer qu’aucun déploiement `gh-pages` inattendu n’est actif.
- [ ] Centraliser consignes agent: fusionner le contenu de `Agents.md` dans `AGENTS.md` et faire pointer l’ancien fichier vers `AGENTS.md` (redirection/notice).
- [ ] Contrôler chaque module (`docs/modules/*.md`):
  - [ ] Compter les balises DINUM par fichier (attendu: 31 ou 0)
  - [ ] Vérifier front‑matter minimal (`service`, `referent`, `updated`)
  - [ ] Passer un œil rapide sur les liens relatifs
- [ ] Valider build + PDF en local (strict):
  - [ ] `mkdocs build -f mkdocs.yml`
  - [ ] `mkdocs build -f mkdocs-pdf.yml`

Commandes de contrôle (à copier-coller)
```bash
# Compter les balises DINUM par module
rg -n "<!-- DINUM -->" docs/modules | awk -F: '{print $1}' | sort | uniq -c

# Vérifier front‑matter
rg -n "^---|service:|referent:|updated:" docs/modules

# Build strict
mkdocs build -f mkdocs.yml

# Génération PDF
mkdocs build -f mkdocs-pdf.yml
```

Critères d’acceptation
- CI: aucun job actif de déploiement `gh-pages` non souhaité.
- Agents: une seule source de vérité (`AGENTS.md`), l’autre fichier signale la redirection.
- Modules: pas de nouvelles balises DINUM; front‑matter présent; liens cohérents.
- Build: `mkdocs build` et PDF passent en local sans erreur.

Améliorations facultatives (Next)
- Ajouter un drapeau d’environnement (commentaire/README) documentant le non‑déploiement Pages.
- Unifier `CONTRIBUTING.md` et `docs/contributing.md` (garder un seul master et l’autre en alias).
