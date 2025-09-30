# Checklist GO – SPAN SG v0.1.0

Date: 2025-09-30

## 1. Pages org-only (preview privée)
- [ ] Organisation → Settings → Pages → Restreindre l’accès aux **membres de l’organisation**
- [ ] Dépôt → Settings → Pages → Branche `gh-pages` (preview: `draft/`, prod: racine)
- [ ] Test d’accès externe: un compte non membre ne doit pas accéder à l’URL de preview

## 2. URLs réelles des déclarations (légal)
Pour chaque module (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS):
- [ ] Remplacer l’URL d’exemple « Déclaration d’accessibilité » par l’URL réelle
- [ ] Renseigner la section « Charge disproportionnée » si applicable (élément, justification, alternative, réévaluation)

## 3. Variables du repo
- [ ] `mkdocs.yml` → `site_url: https://[organisation].github.io/span-sg/`
- [ ] `mkdocs.yml` → `repo_url: https://github.com/[organisation]/span-sg`

## 4. Exécution CI initiale
- [ ] Pousser sur la branche `draft`
- [ ] Vérifier les artefacts: `site/` et `exports/span-sg.pdf` (PDF principal ou fallback)
- [ ] Corriger si besoin, relancer, puis valider la preview

## 5. Gouvernance des accès (publication & offboarding)
- [ ] Vérifier que seul le groupe autorisé peut déclencher le déploiement vers `gh-pages`
- [ ] Vérifier la liste des mainteneurs ayant accès aux secrets/tokens
- [ ] Offboarding: désactiver/supprimer l’accès des membres sortants (org + repo)
