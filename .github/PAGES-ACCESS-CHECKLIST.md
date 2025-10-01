# Checklist accès GitHub Pages

**Configuration actuelle** : Option A - Compte utilisateur (preview publique)

---

## Configuration Pages

- [x] Settings → Pages activé
- [x] Visibility : **Public** (compte utilisateur, pas de restriction org)
- [x] Source : `gh-pages` / `/ (root)`
- [x] URL preview : https://alexmacapple.github.io/span-sg-repo/draft/
- [x] URL production : https://alexmacapple.github.io/span-sg-repo/

---

## État déploiement

- [x] Branche `gh-pages` créée par CI
- [x] Job `deploy_draft` fonctionnel (déploie vers `draft/`)
- [ ] Job `deploy_main` à tester (nécessite push sur `main`)

---

## URLs actives

| Environnement | URL | Statut |
|---------------|-----|--------|
| **Preview (draft)** | https://alexmacapple.github.io/span-sg-repo/draft/ | ✅ Accessible |
| **Production (main)** | https://alexmacapple.github.io/span-sg-repo/ | ⏳ En attente merge `main` |
| **PDF draft** | https://alexmacapple.github.io/span-sg-repo/draft/exports/span-sg.pdf | ✅ Généré (après HOTFIX-02) |

---

## Tests d'accès (Option A - Public)

### Test 1 : Accès avec navigateur authentifié
- [x] Ouvrir https://alexmacapple.github.io/span-sg-repo/draft/
- [x] **Attendu** : Site accessible (public)
- [x] **Résultat** : ✅ OK

### Test 2 : Accès en navigation privée
- [x] Ouvrir https://alexmacapple.github.io/span-sg-repo/draft/ (navigation privée)
- [x] **Attendu** : Site accessible (public)
- [x] **Résultat** : ✅ OK (comportement attendu pour Option A)

### Test 3 : Vérification contenu
- [x] Page d'accueil charge correctement
- [x] Navigation fonctionne
- [x] Synthèse accessible
- [x] Modules présents (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)

---

## Limitations connues (Option A)

⚠️ **Preview publique** : Toute personne ayant l'URL peut accéder au site draft.

**Acceptable pour** :
- Phase POC / développement initial
- Tests techniques
- Validation fonctionnelle

**Non acceptable pour** :
- Contenus confidentiels pré-publication
- Production finale

---

## Migration vers organisation (future)

Quand la restriction org-only sera nécessaire :

1. **Créer organisation GitHub** (ex: `span-sg`)
2. **Transférer le repo** : `Alexmacapple/span-sg-repo` → `span-sg/span-sg`
3. **Activer restriction Pages** : Settings → Pages → Visibility : Private (members only)
4. **Mettre à jour URLs** :
   - `mkdocs.yml` : `site_url`, `repo_url`
   - README : liens preview/production
   - Badges CI

**Coût** : Gratuit (organisation Free suffit)

**Impact** :
- URLs changent (ex: `span-sg.github.io/span-sg/`)
- Clones locaux à mettre à jour
- Preview devient privée (membres org uniquement)

---

## Dépannage

### Preview 404

Si `https://alexmacapple.github.io/span-sg-repo/draft/` retourne 404 :

1. Vérifier que Pages est activé : Settings → Pages
2. Vérifier source Pages : `gh-pages` / `/ (root)`
3. Vérifier branche gh-pages existe : `git ls-remote --heads origin gh-pages`
4. Vérifier dernier job `deploy_draft` : GitHub Actions → dernier run → job `deploy_draft`
5. Attendre 2-3 minutes (propagation DNS)

### Contenu obsolète

Si le site ne reflète pas les dernières modifications :

1. Vérifier que CI a tourné : GitHub Actions → dernier run
2. Vérifier job `deploy_draft` a réussi
3. Forcer rafraîchissement navigateur : Cmd+Shift+R (Mac) / Ctrl+F5 (Windows)
4. Vérifier timestamp dans footer du site

---

## Validation S2-03 (Option A)

- [x] GitHub Pages activé sur repo `Alexmacapple/span-sg-repo`
- [x] https://alexmacapple.github.io/span-sg-repo/draft/ accessible
- [x] Limitation "preview publique" documentée (README.md)
- [x] Plan de migration vers organisation défini (ce document)
- [x] `.github/PAGES-ACCESS-CHECKLIST.md` créé

**Story S2-03 : ✅ COMPLÈTE (Option A)**

---

## Références

- **Roadmap** : `roadmap/S2-03-preview-privee.md`
- **Workflow CI** : `.github/workflows/build.yml` (jobs `deploy_draft` et `deploy_main`)
- **Config MkDocs** : `mkdocs.yml` (lignes `site_url` et `repo_url`)
- **PRD v3.3** : Section 5.1 "Accès preview privé"
