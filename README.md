# SPAN SG – Repo

Ce dépôt contient le SPAN SG (MkDocs), les modules services et la CI de build/deploy.

## Démarrage rapide
1. Installer Docker (facultatif pour dev local)
2. Cloner le dépôt et créer deux branches: `main` et `draft`
3. Renseigner `site_url` et `repo_url` dans `mkdocs.yml`

## Checklist « première release v0.1 »
1. Configurer GitHub Pages au niveau de l’organisation et restreindre l’accès aux membres
2. Créer les branches `main` (production) et `draft` (preview)
3. Paramétrer les secrets nécessaires (si besoin) et vérifier les permissions `GITHUB_TOKEN`
4. Mettre à jour `docs/index.md` (blocs légaux) et `docs/modules/*` (front-matter)
5. Mapper les 31 points officiels dans `docs/modules/_template.md` et dans le module pilote (SIRCOM)
6. Lancer la CI sur `draft` et vérifier: build site OK, `exports/span-sg.pdf` présent
7. Revue par Bertrand/Alex puis merge dans `draft` pour la preview privée
8. Préparer `CHANGELOG.md`, tagger `v0.1.0` et pousser le tag
   ```bash
   git tag -a v0.1.0 -m "Release SPAN SG v0.1.0"
   git push origin v0.1.0
   ```
9. Lancer le déploiement de `main` et créer la release GitHub en joignant `exports/span-sg.pdf`
10. Notifier Yves pour validation production et consigner la décision GO/NO-GO

## Commandes utiles
- Dev local: `docker compose up` puis http://localhost:8000
- Build manuel PDF principal: `mkdocs build --config-file mkdocs-pdf.yml`
- Build manuel PDF fallback: `mkdocs build --config-file mkdocs-with-pdf.yml`
- Calcul synthèse: `python scripts/calculate_scores.py`

## Dépannage rapide
- PDF manquant: vérifier fallback `mkdocs-with-pdf` ou utiliser l’impression navigateur sur « Synthèse »
- Scores incohérents: s’assurer que seuls les 31 points portent `<!-- DINUM -->`
- Preview inaccessible: vérifier restriction GitHub Pages à l’organisation et branche `gh-pages`

## Contacts
- Owner: Alexandra (@alexandra)
- Validateurs: Bertrand (@bertrand), Alex (@alex)
- Sponsor: Yves


## règles de validation
- Validation de contenu: Bertrand et Alex
- Yves: validation uniquement pour la bascule en production


## preview privée (Pages organisation GitHub)
- Restreindre l’accès aux membres de l’organisation dans les paramètres Pages
- Déploiement `draft` vers `gh-pages` sous `draft/`
- Pas d’identifiants génériques; seuls les comptes org sont autorisés


## Checklist GO
- Voir `GO-CHECKLIST.md` pour valider Pages org-only, URLs légales, variables `site_url`/`repo_url`, exécution CI initiale, et gouvernance des accès.
- Voir `.github/PAGES-ACCESS-CHECKLIST.md` pour le détail du paramétrage Pages (organisation uniquement).



## Vibe coding
- Utiliser `Agents.md` (Codex/Cursor/Builder.io) pour les instructions d’agent standardisées
- Utiliser `Claude.md` pour Claude Code (format spécifique Anthropic)
- Conserver le périmètre MVP, ne pas modifier la logique des 31 points DINUM

