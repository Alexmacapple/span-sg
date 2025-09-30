---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S2-03 : Configuration preview privée GitHub Pages (org-only)

**Phase** : Semaine 2 - Automatisation
**Priorité** : Critique
**Estimation** : 1h
**Assigné** : Alexandra

---

## Contexte projet

La **preview privée** est une contrainte MVP du PRD v3.3 :
> "Preview privée via GitHub Pages organisation uniquement"

Elle permet à l'équipe de :
- Prévisualiser les modifications sur `draft` avant merge vers `main`
- Partager un lien avec les validateurs (Bertrand, Alex)
- Tester le rendu final dans un environnement proche de la production
- Garder le contenu confidentiel (accès restreint org)

**Architecture** :
- Branche `draft` → Déploiement CI vers `gh-pages/draft/`
- Branche `main` → Déploiement CI vers `gh-pages/` (racine)
- Accès GitHub Pages restreint aux "membres de l'organisation"

**Limitation importante** :
L'option "org-only" n'existe QUE pour les **organisations GitHub**, pas les comptes utilisateurs.

Si le repo reste sur un compte utilisateur (`Alexmacapple/span-sg-repo`), les seules options sont :
- Public (tout le monde)
- Private (personne, même avec GitHub Pages activé)

---

## Objectif

Activer GitHub Pages sur le repo, configurer la branche `gh-pages` comme source, et si possible migrer vers une organisation GitHub pour activer la restriction "org-only".

---

## Prérequis

- [ ] Story S1-01 complétée (repo créé avec branches)
- [ ] Story S2-01 complétée (CI déploie vers gh-pages)
- [ ] Branche `gh-pages` créée par le premier run CI
- [ ] Décision : rester sur compte utilisateur OU migrer vers organisation

---

## Étapes d'implémentation

### Option A : Configuration sur compte utilisateur (Alexmacapple)

**Limitation : Preview sera publique ou inaccessible**

#### 1. Activer GitHub Pages

Sur GitHub → `Alexmacapple/span-sg-repo` → Settings → Pages :
- **Source** : Deploy from a branch
- **Branch** : `gh-pages` / `/ (root)`
- **Custom domain** : (vide)

Sauvegarder.

#### 2. Vérifier l'URL générée

Après quelques minutes, l'URL apparaît :
```
https://alexmacapple.github.io/span-sg-repo/
```

Tester :
- https://alexmacapple.github.io/span-sg-repo/ → Production (main)
- https://alexmacapple.github.io/span-sg-repo/draft/ → Preview (draft)

#### 3. Limites et décision

**Problème** : Pas d'option "Private to organization members" sur compte utilisateur.

**Solutions possibles** :
1. **Accepter que la preview soit publique** (compromis)
2. **Migrer vers une organisation** (recommandé, voir Option B)
3. **Utiliser une solution alternative** (Netlify, Vercel avec auth)

Si décision = accepter preview publique (temporaire) :
- Documenter dans README
- Prévoir migration vers organisation avant production v1.0
- Avertir l'équipe

#### 4. Documenter les URLs

Ajouter dans README.md :
```markdown
## URLs

- **Production** : https://alexmacapple.github.io/span-sg-repo/
- **Preview (draft)** : https://alexmacapple.github.io/span-sg-repo/draft/

⚠️ **Note** : Preview actuellement publique. Migration vers organisation prévue pour restriction org-only.
```

---

### Option B : Migration vers organisation GitHub (RECOMMANDÉ)

**Avantage : Accès "Private to organization members" disponible**

#### 1. Créer une organisation GitHub

Sur GitHub → https://github.com/organizations/new :
- **Organization name** : `span-sg` (ou autre nom disponible)
- **Contact email** : alexandra.guiderdoni@gmail.com
- **Plan** : Free (suffisant)

#### 2. Inviter les membres

Dans l'organisation → People → Invite member :
- Bertrand (@bertrand)
- Alex (@alex)
- Yves (si compte GitHub disponible)

#### 3. Transférer le repository

Sur `Alexmacapple/span-sg-repo` → Settings → Danger Zone → Transfer ownership :
- **New owner** : `span-sg` (nom de l'organisation)
- **Repository name** : `span-sg` (ou garder `span-sg-repo`)

Confirmer le transfert.

#### 4. Mettre à jour les URLs

Après transfert, les URLs changent :
- Repo : `https://github.com/span-sg/span-sg`
- Pages : `https://span-sg.github.io/span-sg/`

Mettre à jour `mkdocs.yml` :
```yaml
site_url: https://span-sg.github.io/span-sg/
repo_url: https://github.com/span-sg/span-sg
```

Committer :
```bash
git remote set-url origin https://github.com/span-sg/span-sg.git
git add mkdocs.yml
git commit -m "chore: update URLs after org transfer"
git push origin draft
```

#### 5. Activer GitHub Pages avec restriction org

Sur `https://github.com/span-sg/span-sg` → Settings → Pages :
- **Visibility** : ☑ Private (only members of span-sg organization)
- **Source** : `gh-pages` / `/ (root)`

Sauvegarder.

#### 6. Tester l'accès restreint

**Test 1 : Accès avec compte membre organisation**
- Se connecter avec compte membre (@alexandra, @bertrand, @alex)
- Ouvrir https://span-sg.github.io/span-sg/draft/
- Attendu : ✓ Page accessible

**Test 2 : Accès avec compte externe (ou navigation privée)**
- Déconnexion GitHub
- Ouvrir https://span-sg.github.io/span-sg/draft/
- Attendu : ❌ Page 404 ou demande d'authentification

#### 7. Documenter la preview privée

Ajouter dans README.md :
```markdown
## Preview privée (org-only)

La preview `draft` est accessible uniquement aux membres de l'organisation GitHub `span-sg` :
- **Preview** : https://span-sg.github.io/span-sg/draft/
- **Production** : https://span-sg.github.io/span-sg/

Pour accéder, votre compte GitHub doit être membre de l'organisation.
```

Créer `.github/PAGES-ACCESS-CHECKLIST.md` :
```markdown
# Checklist accès GitHub Pages org-only

## Configuration Pages
- [ ] Settings → Pages activé
- [ ] Visibility : Private (members only)
- [ ] Source : gh-pages / (root)

## Membres organisation
- [ ] Alexandra (owner)
- [ ] Bertrand (member)
- [ ] Alex (member)

## Tests d'accès
- [ ] Membre org : accès OK
- [ ] Compte externe : accès refusé
- [ ] Navigation privée : accès refusé

## URLs
- Production : https://span-sg.github.io/span-sg/
- Preview : https://span-sg.github.io/span-sg/draft/
```

---

## Critères d'acceptation

### Option A (compte utilisateur)
- [ ] GitHub Pages activé
- [ ] https://alexmacapple.github.io/span-sg-repo/ accessible
- [ ] https://alexmacapple.github.io/span-sg-repo/draft/ accessible
- [ ] Limitation "preview publique" documentée
- [ ] Plan de migration vers organisation défini

### Option B (organisation - RECOMMANDÉ)
- [ ] Organisation GitHub créée
- [ ] Repo transféré vers organisation
- [ ] Membres invités et acceptés
- [ ] GitHub Pages activé avec "Private to organization members"
- [ ] Preview draft accessible uniquement aux membres org
- [ ] URLs mises à jour dans mkdocs.yml
- [ ] `.github/PAGES-ACCESS-CHECKLIST.md` créé

---

## Tests de validation

```bash
# Test 1 : Branche gh-pages existe
git ls-remote --heads origin gh-pages && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : URLs cohérentes dans mkdocs.yml
grep -q "site_url:" mkdocs.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : CI déploie vers gh-pages
# Vérifier dernier run GitHub Actions → job deploy_draft réussi

# Test 4 : Preview accessible
curl -I https://[URL-PAGES]/draft/ | grep "200 OK" && echo "OK" || echo "FAIL"
# Attendu : OK (si public) ou 404 (si org-only sans auth)

# Test 5 : Restriction org active (si Option B)
# Test manuel : navigation privée → 404
```

---

## Dépendances

**Bloque** :
- S3-02 (formation Git utilise la preview pour démonstration)
- S4-02 (validation Yves nécessite accès preview)

**Dépend de** :
- S1-01 (repo doit exister)
- S2-01 (CI doit déployer vers gh-pages)

---

## Références

- **PRD v3.3** : Section 5.1 "Accès preview privé (Option A figée)"
- **PRD v3.3** : Section 10 "Décisions MVP" → Preview privée org-only
- **.github/PAGES-ACCESS-CHECKLIST.md** : Checklist à créer
- **GO-CHECKLIST.md** : Point "Pages org-only configuré"
- **CLAUDE.md** : Section "Branches et déploiements"

---

## Notes et risques

**Coût organisation GitHub**
L'organisation Free suffit pour :
- Repos publics illimités
- 1 repo privé avec Pages org-only
- 2000 min Actions/mois

Si besoin > 1 repo privé, passer à Team ($4/user/mois).

**Alternative si pas d'organisation**
Si impossible de créer organisation :
1. **Netlify** : Deploy preview avec password protection
2. **Vercel** : Deploy preview avec Basic Auth
3. **Cloudflare Pages** : Access control avec CF Access

Ces solutions nécessitent modifications CI et config supplémentaire.

**Impact du transfert d'organisation**
- URLs changent (casser liens existants)
- Clones locaux à mettre à jour (`git remote set-url`)
- Webhooks/integrations à reconfigurer
- Badges CI à mettre à jour

**Accès Yves**
Si Yves n'a pas de compte GitHub, créer un compte invité temporaire ou :
- Lui créer un compte avec email temporaire
- Utiliser un token d'accès temporaire (GitHub Apps)
- Lui envoyer artefacts PDF par email (compromis)

---

## Post-tâche

Tester le workflow complet :
```bash
# 1. Modifier un fichier sur draft
git checkout draft
echo "Test preview" >> docs/index.md
git add docs/index.md
git commit -m "test: vérifier déploiement preview"
git push origin draft

# 2. Attendre CI (2-3 min)
# 3. Vérifier preview mise à jour
curl https://[URL-PAGES]/draft/ | grep "Test preview"

# 4. Nettoyer
git revert HEAD
git push origin draft
```

Communiquer les URLs à l'équipe :
```
📧 À : Bertrand, Alex, Yves
Objet : SPAN SG - Preview privée disponible

La preview privée est maintenant accessible :
- Preview (draft) : https://span-sg.github.io/span-sg/draft/
- Production : https://span-sg.github.io/span-sg/

Accès restreint aux membres de l'organisation GitHub.
```