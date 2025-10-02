---
bmad_phase: production
bmad_agent: dev
story_type: deployment
autonomous: false
validation: human-qa
---

# Story S4-04 : Publication production v1.0

**Phase** : Semaine 4 - Production
**Priorité** : Critique (mise en ligne)
**Estimation** : 1h30-2h

---

## Contexte projet

**Après S4-03** : Tag v1.0.0 créé
- CHANGELOG mis à jour (section v1.0.0 détaillée)
- Tag annoté pushé sur `draft`
- GO concept Stéphane obtenu (S4-02)

**État branches** :
- `draft` : Contenus finalisés + tag v1.0.0
- `main` : Production actuelle (v0.2.0)

**Objectif S4-04** : Publier v1.0.0 en production
1. Merge `draft` → `main`
2. Créer release GitHub v1.0.0 avec PDF
3. Valider déploiement GitHub Pages main
4. Communication interne minimale

**Stratégie déploiement** : Fluidité et souplesse (option validée Q30)
- **6 modules sur main** (2 validés + 4 en cours)
- Disclaimers transparents 5 emplacements
- Validation progressive assumée

---

## Objectif

**Déployer v1.0.0 en production** accessible via :
- GitHub Pages main : https://alexmacapple.github.io/span-sg-repo/ (racine)
- Release GitHub v1.0.0 avec PDF téléchargeable

**Livrables** :
- Branche `main` à jour (merge draft)
- Release GitHub v1.0.0 publiée (avec exports/span-sg.pdf)
- Pages production accessible (6 modules, disclaimers visibles)
- Communication Stéphane (confirmation mise en ligne)

---

## Prérequis

- [x] S4-03 complété (tag v1.0.0 créé et pushé)
- [x] GO Stéphane confirmé (S4-02)
- [x] CI draft 100% PASS (dernier commit)
- [x] Validation Chef SNUM obtenue OU délégation Stéphane confirmée
- [x] Working directory clean (aucun changement pending)

---

## Étapes d'implémentation

### Phase 1 - Pré-merge validation (30 min)

**Objectif** : Vérifier état `draft` avant merge critique vers `main`.

#### Microtâches

**1.1 Vérifier CI draft dernière exécution** (10 min)

```bash
# Lister dernières CI draft
gh run list --branch draft --limit 5

# Vérifier dernière CI = succès
gh run view --branch draft
# Attendu : ✓ Build and Deploy completed
```

**Checklist CI** :
- [ ] Status : ✅ Success (pas ❌ Failure)
- [ ] Jobs complétés : Calculate scores, Run tests, Build site, Generate PDF, Deploy
- [ ] Artefacts générés : `site`, `exports` (contenant span-sg.pdf)
- [ ] Durée < 5 min (performance normale)

**Si CI failed** : Corriger erreur sur draft avant merge (bloquer S4-04).

**1.2 Tester preview draft finalisée** (10 min)

Ouvrir : https://alexmacapple.github.io/span-sg-repo/draft/

**Checklist manuelle** :
- [ ] Homepage charge correctement
- [ ] Disclaimer visible en en-tête
- [ ] Navigation latérale : 6 modules listés
- [ ] Clic SIRCOM → module charge, 25/31 points visibles
- [ ] Clic Synthèse → tableau 6 modules, colonne État affichée
- [ ] Pas d'erreur 404, pas de markdown cassé

**1.3 Vérifier scores et validation_status** (10 min)

```bash
# Calculer scores localement (vérification)
python scripts/calculate_scores.py

# Afficher synthese.md
cat docs/synthese.md
```

**Vérifier** :
- [ ] SIRCOM, SNUM : État "✅ Validé"
- [ ] SRH, SIEP, SAFI, BGS : État "🔄 En cours"
- [ ] Total global cohérent (46/186 attendu si 25 SIRCOM + 21 SNUM)
- [ ] Front-matter modules : `validation_status: validated` ou `in_progress` présent

---

### Phase 2 - Merge draft → main (15 min)

**Objectif** : Merge propre sans conflit.

#### Microtâches

**2.1 Backup main actuel (tag)** (5 min)

```bash
# Créer tag backup sur main avant merge (sécurité)
git checkout main
git pull origin main

git tag -a v0.2.1-backup -m "Backup main avant merge draft v1.0.0"
git push origin v0.2.1-backup
```

**Justification** : Rollback facilité si problème critique post-merge.

**2.2 Merge draft dans main** (5 min)

```bash
# Toujours sur main
git merge draft --no-ff -m "Merge draft v1.0.0 into main

Publication production v1.0.0 : framework hybrid
- 2 modules validés : SIRCOM (25/31), SNUM (21/31)
- 4 modules en cours : SRH, SIEP, SAFI, BGS
- Infrastructure production-ready
- GO concept Stéphane (2025-10-XX)
- Tag v1.0.0 présent

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Flags** :
- `--no-ff` : Force merge commit (traçabilité, même si fast-forward possible)
- Message commit détaillé (contexte merge)

**Gestion conflits** :
- **Attendu** : Aucun conflit (main = v0.2.0, draft = évolution linéaire)
- **Si conflit** : Résoudre manuellement (privilégier version draft pour fichiers modifiés S4)

**2.3 Push main** (5 min)

```bash
# Push main vers origin (déclenche CI + déploiement Pages)
git push origin main
```

**Vérifier** :
- Pas d'erreur Git
- Message : `Branch 'main' set up to track 'origin/main'`
- CI GitHub Actions démarre automatiquement

---

### Phase 3 - Release GitHub v1.0.0 (15 min)

**Objectif** : Créer release officielle avec PDF attaché.

#### Microtâches

**3.1 Attendre CI main complétée** (5-10 min)

```bash
# Suivre CI main en temps réel
gh run watch --branch main

# Ou lister pour vérifier
gh run list --branch main --limit 1
```

**Attendu** : ✅ Success (scoring + build + PDF + deploy).

**Si CI main failed** : Voir section Rollback (Annexe). Ne pas créer release avant fix.

**3.2 Télécharger PDF artefact CI main** (2 min)

```bash
# Récupérer run ID dernière CI main
RUN_ID=$(gh run list --branch main --limit 1 --json databaseId --jq '.[0].databaseId')

# Télécharger artefact exports
gh run download $RUN_ID --name exports

# Vérifier PDF présent
ls -lh exports/span-sg.pdf
# Attendu : fichier ~2-5 Mo
```

**3.3 Créer release GitHub** (5 min)

```bash
gh release create v1.0.0 \
  --title "SPAN SG v1.0.0 - Framework Production Hybrid" \
  --notes "$(cat <<'EOF'
## Version 1.0.0 - Framework Production Hybrid

**🎯 Milestone** : Première version production avec 2 modules services validés.

### Modules validés
- ✅ **SIRCOM** : 25/31 points (80.6%) - mappé depuis span-sircom-sg.md
- ✅ **SNUM Portailpro.gouv** : 21/31 points (67.7%) - mappé depuis span-portail-pro.sg.md

### Modules en cours
- 🔄 SRH, SIEP, SAFI, BGS : Structure framework, contenus à renseigner

### Infrastructure
- CI/CD 100% automatisé (tests unitaires + E2E)
- Export PDF accessible avec métadonnées
- Scoring automatisé avec colonne État (✅ Validé / 🔄 En cours)
- Preview privée GitHub Pages (org-only)

### Documentation
- CONTRIBUTING.md (workflow contributeur)
- Guide mapping détaillé (roadmap/S4-00, ~2700 lignes)
- 6 modules structurés (5 sections + 31 points DINUM)

### Validation
- GO concept Stéphane (Chef mission numérique SNUM-SG)
- Roadmaps BMAD S4-00 à S4-04 complétées

### Accès
- **Site** : https://alexmacapple.github.io/span-sg-repo/
- **PDF** : Téléchargeable ci-dessous (exports/span-sg.pdf)

### Prochaines étapes
- Phase 2 : Onboarding 4 référents services
- Semaine 5 : Audit RGAA externe

Voir [CHANGELOG.md](https://github.com/Alexmacapple/span-sg-repo/blob/main/CHANGELOG.md) pour détails complets.

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)" \
  exports/span-sg.pdf
```

**Format** :
- Titre : Court et descriptif
- Notes : Markdown avec sections (Modules, Infra, Validation, Accès, Prochaines étapes)
- Attachement : PDF depuis artefact CI main
- Signature Claude Code

**3.4 Vérifier release créée** (3 min)

Ouvrir : https://github.com/Alexmacapple/span-sg-repo/releases

**Checklist** :
- [ ] Release v1.0.0 visible en tête de liste
- [ ] Badge "Latest" affiché
- [ ] Notes markdown bien formatées (sections, checkmarks)
- [ ] PDF téléchargeable (clic "span-sg.pdf" fonctionne)
- [ ] Taille PDF cohérente (~2-5 Mo)
- [ ] Date release = aujourd'hui

---

### Phase 4 - Post-publication validation (20 min)

**Objectif** : Vérifier déploiement production fonctionnel.

#### Microtâches

**4.1 Tester GitHub Pages production** (10 min)

Ouvrir : https://alexmacapple.github.io/span-sg-repo/ (racine, SANS /draft/)

**Checklist exhaustive** :
- [ ] Homepage charge (pas 404, pas "Site coming soon")
- [ ] Disclaimer v1.0 visible :
  > "✅ **Version 1.0 en production** : Framework opérationnel avec 2 modules services validés (SIRCOM, SNUM). 4 modules additionnels en structure, enrichis progressivement."
- [ ] Navigation 6 modules fonctionnelle :
  - [ ] SIRCOM cliquable → page charge
  - [ ] SNUM cliquable → page charge
  - [ ] SRH, SIEP, SAFI, BGS cliquables → disclaimers "🔄 En cours" visibles
- [ ] Synthèse accessible :
  - [ ] Tableau 6 modules affiché
  - [ ] Colonne État présente (✅ Validé / 🔄 En cours)
  - [ ] Scores corrects (SIRCOM 25/31, SNUM 21/31, autres 0/31)
- [ ] PDF téléchargeable depuis site (si lien présent) OU depuis release

**Si 404 ou erreur** : Voir section Rollback. Pages peut prendre 2-5 min déploiement.

**4.2 Vérifier badges status main** (5 min)

Ouvrir : https://github.com/Alexmacapple/span-sg-repo

**Checklist README** :
- [ ] Badge "Build" : ![Build](https://img.shields.io/github/actions/workflow/status/.../build.yml?branch=main) → ✅ passing
- [ ] Badge "Release" : ![Release](https://img.shields.io/github/v/release/...) → v1.0.0
- [ ] Disclaimer README (ton positif) visible

**4.3 Validation scoring production** (5 min)

```bash
# Cloner main frais (ou pull si déjà local)
git checkout main
git pull origin main

# Recalculer scores localement (vérification cohérence)
python scripts/calculate_scores.py

# Comparer avec synthese.md production
diff docs/synthese.md <(curl -s https://alexmacapple.github.io/span-sg-repo/synthese/)
# Attendu : aucune différence (ou différences mineures formatage HTML)
```

**Vérifier** :
- [ ] Script scoring fonctionne sans erreur
- [ ] Scores identiques production vs local
- [ ] Aucune régression (ex: module disparu, score changé)

---

### Phase 5 - Communication interne (10 min)

**Objectif** : Informer Stéphane et Bertrand/Alexandra de la mise en ligne.

#### Microtâches

**5.1 Email Stéphane** (5 min)

```
📧 À : Stéphane
Cc : Bertrand, Alexandra
Objet : ✅ SPAN SG v1.0.0 en production

Bonjour Stéphane,

Suite à votre validation (présentation 2025-10-XX), la version 1.0.0 du SPAN SG est désormais en production.

**Accès** :
- Site : https://alexmacapple.github.io/span-sg-repo/
- Release GitHub : https://github.com/Alexmacapple/span-sg-repo/releases/tag/v1.0.0
- PDF accessible : téléchargeable depuis release

**Contenu v1.0** :
- 2 modules validés : SIRCOM (25/31), SNUM Portailpro.gouv (21/31)
- 4 modules en structure : SRH, SIEP, SAFI, BGS (prêts onboarding Phase 2)
- Infrastructure complète : CI/CD, scoring automatisé, export PDF

**Visibilité** :
- GitHub Pages privé (org-only) maintenu
- Pas de communication externe à ce stade
- Attente validation Chef SNUM pour communication large

Merci pour votre accompagnement et validation.

Cordialement,
[Bertrand / Alexandra]
```

**Ton** : Professionnel, factuel, remerciements.

**5.2 Message Bertrand/Alexandra (si applicable)** (2 min)

```
📨 Message interne

v1.0.0 publiée en production 🎉

- Site : https://alexmacapple.github.io/span-sg-repo/
- Release : https://github.com/.../releases/tag/v1.0.0

Prochaines étapes :
- Attente feedback Stéphane/Chef SNUM
- Phase 2 onboarding (timing à définir)
- Semaine 5 audit RGAA (si budget validé)
```

**5.3 Pas de communication services externes** (note)

- ~~Pas d'email directions services (SRH, SIEP, SAFI, BGS)~~
- ~~Pas d'annonce organisation large~~
- **Attente validation Chef SNUM** pour communication officielle
- Strategy: déploiement discret, validation progressive

---

## Critères d'acceptation

### Merge et déploiement
- [ ] Branche `main` mergée depuis `draft` (merge commit avec message détaillé)
- [ ] Tag v0.2.1-backup créé (sécurité rollback)
- [ ] CI main exécutée : ✅ Success (scoring + build + PDF + deploy)
- [ ] Aucun conflit merge non résolu

### Release GitHub
- [ ] Release v1.0.0 créée et publiée
- [ ] Badge "Latest" affiché
- [ ] Notes release détaillées (modules, infra, validation, accès)
- [ ] PDF span-sg.pdf attaché (téléchargeable, ~2-5 Mo)
- [ ] Lien site production dans notes

### Production accessible
- [ ] GitHub Pages main accessible (https://.../span-sg-repo/)
- [ ] Homepage charge sans erreur
- [ ] Disclaimer v1.0 visible (ton positif README, ton neutre homepage)
- [ ] Navigation 6 modules fonctionnelle
- [ ] Synthèse affichée avec colonne État
- [ ] Scores cohérents (SIRCOM 25/31, SNUM 21/31)

### Validation technique
- [ ] Badges README à jour (Build passing, Release v1.0.0)
- [ ] Script scoring fonctionne localement sur main
- [ ] Aucune régression vs draft (modules, scores, navigation)
- [ ] PDF téléchargeable depuis release fonctionnel

### Communication
- [ ] Email Stéphane envoyé (confirmation mise en ligne)
- [ ] Message Bertrand/Alexandra (si équipe)
- [ ] Pas de communication externe (stratégie discrète respectée)

---

## Dépendances

**Bloque** : Rien (S4-04 = dernière story production, ouvre Phase 2)

**Dépend de** :
- S4-03 (tag v1.0.0 créé)
- S4-02 (GO Stéphane obtenu)
- Validation Chef SNUM (obtenue OU délégation Stéphane confirmée)

---

## Références

- **GitHub Pages deployment** : https://docs.github.com/en/pages/getting-started-with-github-pages
- **GitHub Releases** : https://docs.github.com/en/repositories/releasing-projects-on-github
- **gh CLI release** : `gh release create --help`
- **Workflow CI** : `.github/workflows/build.yml`

---

## Notes et risques

### Timing déploiement GitHub Pages

**Délai normal** : 2-5 min après push main pour Pages rafraîchies.

**Si >10 min** : Vérifier Actions → Deploy job terminé ✅. Si oui, caching CDN GitHub (patience).

**Commande force refresh** (si vraiment bloqué, rare) :
```bash
# Re-déclencher deploy manuellement
gh workflow run build.yml --ref main
```

### Visibilité org-only maintenue

**Configuration GitHub Pages** : Privé (org-only) maintenu en production.

**Vérification** : Settings → Pages → "Visibility" = Private.

**Changement visibilité** : Si décision ultérieure rendre public (après Chef SNUM), modifier Settings manuellement.

### Merge --no-ff justifié

`--no-ff` force merge commit même si fast-forward possible.

**Avantages** :
- Traçabilité : commit merge explicite ("Merge draft v1.0.0 into main")
- Rollback facilité : revert merge commit = annule tout draft
- Historique Git clair (visualisation branches GitGraph)

**Alternative rejetée** : Fast-forward (perd traçabilité merge).

### Communication Chef SNUM déléguée

**Hypothèse** : Stéphane gère communication ascendante Chef SNUM.

**Si Chef SNUM demande présentation directe** :
- Réutiliser démo S4-02 (éprouvée)
- Format court 10 min (focus framework + 2 modules)

**Si Chef SNUM valide par email** :
- Stéphane transfère email confirmation à Bertrand/Alexandra
- Autorisation communication large (directions services)

---

## Annexe - Plan de rollback (si problème critique)

### Conditions déclenchement rollback

Rollback SI :
- CI main échoue (scoring, build, tests)
- GitHub Pages production inaccessible >15 min
- Corruption contenus modules (SIRCOM/SNUM illisibles)
- Erreur critique détectée par Stéphane/Chef SNUM (rare)

**Ne PAS rollback pour** :
- Typo mineure détectée (corriger par commit fix sur main)
- Feedback cosmétique Stéphane (ajuster progressivement)

### Procédure rollback complète

**Étape 1 : Restaurer main à v0.2.0** (2 min)

```bash
# Sur branche main
git checkout main

# Reset hard au tag backup
git reset --hard v0.2.1-backup

# Force push main (⚠️ DESTRUCTIF)
git push origin main --force
```

**Conséquence** : Main revient à état pré-merge. Pages redéployées sur v0.2.0 (2-5 min).

**Étape 2 : Supprimer release GitHub** (1 min)

```bash
# Supprimer release v1.0.0
gh release delete v1.0.0 --yes

# Vérifier suppression
gh release list
# Attendu : v1.0.0 disparue
```

**Étape 3 : Supprimer tag v1.0.0** (optionnel si tag corrompu)

```bash
# Supprimer tag local
git tag -d v1.0.0

# Supprimer tag remote
git push origin :refs/tags/v1.0.0

# Vérifier suppression
git ls-remote --tags origin
# Attendu : v1.0.0 disparue
```

**Note** : Tag peut être conservé si problème = déploiement (pas contenu tag).

**Étape 4 : Notification rollback** (5 min)

```
📧 À : Stéphane
Objet : ⚠️ Rollback v1.0.0 effectué

Bonjour Stéphane,

Un problème critique a nécessité un rollback de la version 1.0.0.

**Cause** : [Décrire : CI échec, Pages inaccessible, corruption contenu]

**Action** : Production restaurée à v0.2.0 (état stable précédent).

**Prochaines étapes** :
1. Analyse cause racine
2. Correction sur draft
3. Re-validation avant nouvelle tentative publication

Site production actuel : https://alexmacapple.github.io/span-sg-repo/ (v0.2.0)

Je vous tiens informé de la résolution.

Cordialement,
[Bertrand / Alexandra]
```

**Étape 5 : Diagnostic et correction** (variable)

Analyser cause :
- **CI main failed** : Lire logs Actions, identifier erreur (tests, scoring, build)
- **Pages inaccessible** : Vérifier Settings Pages, re-déclencher deploy
- **Corruption contenu** : Comparer `git diff v0.2.1-backup..draft` pour identifier commit problématique

**Correction** :
- Fixer sur draft
- Re-tester preview draft
- Re-présenter à Stéphane si changement majeur (ou GO implicite si fix mineur)
- Retenter S4-04 (merge + release)

**Durée rollback total** : 10-15 min (+ temps correction variable).

---

### Rollback partiel (si problème mineur)

**Alternative au rollback complet** : Correction en avant (forward fix).

**Applicable si** :
- Pages production accessible mais bug cosmétique
- CI passe mais scoring affiche erreur mineure
- Feedback Stéphane = ajustement léger (reformulation disclaimer)

**Procédure** :
```bash
# Sur draft : corriger erreur
git checkout draft
[... éditer fichiers ...]
git commit -m "fix: correction [problème]"
git push origin draft

# Merger correction dans main
git checkout main
git merge draft
git push origin main

# Attendre redéploy Pages (2-5 min)
```

**Avantage** : Pas de rollback destructif, historique Git propre.

**Inconvénient** : Commit fix après release (version "sale"). Acceptable si mineur.

---

## Post-tâche

### Monitoring post-publication

**J+1 après publication** : Vérifier stabilité

```bash
# Vérifier dernières CI main (24h)
gh run list --branch main --limit 10

# Vérifier Pages toujours accessible
curl -I https://alexmacapple.github.io/span-sg-repo/
# Attendu : HTTP/2 200
```

**Anomalie** : Si CI échoue soudainement ou Pages indisponible → investiguer immédiatement.

### Archivage artefacts v1.0

**Optionnel** : Sauvegarder PDF v1.0 localement (archivage long terme)

```bash
# Télécharger PDF release
wget https://github.com/Alexmacapple/span-sg-repo/releases/download/v1.0.0/span-sg.pdf \
  -O ~/Archives/span-sg-v1.0.0-$(date +%Y%m%d).pdf
```

**Justification** : Si release supprimée accidentellement, PDF récupérable.

### Préparation Phase 2

**Après v1.0 stabilisée (J+7)** : Planifier onboarding 4 référents

Actions :
1. Identifier référents services (RH/directions SRH, SIEP, SAFI, BGS)
2. Planifier formations Git (roadmap S3-02 réutilisable)
3. Préparer templates modules personnalisés (copie _template.md)
4. Définir timeline Phase 2 (ex: 1 module/mois)

**Roadmap Phase 2** : Créer `roadmap/Phase-2-onboarding.md` (hors scope S4-04).

---

*Dernière mise à jour : 2025-10-02*
