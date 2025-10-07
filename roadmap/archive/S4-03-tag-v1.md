---
bmad_phase: production
bmad_agent: dev
story_type: release
autonomous: false
validation: human-qa
---

# Story S4-03 : Tag version 1.0.0

**Phase** : Semaine 4 - Production
**Priorité** : Critique (jalonne v1.0)
**Estimation** : 1h

---

## Contexte projet

**Après S4-02** : GO concept Stéphane obtenu
- Présentation validée (6 éléments montrés)
- Décision GO documentée (fichier `roadmap/S4-02-decision-stephane.md` OU email Stéphane archivé)
- Ajustements post-feedback implémentés (si GO conditionnel)

**État codebase** :
- Branche `draft` avec contenus finalisés (S4-01)
- 2 modules validés (SIRCOM, SNUM)
- 4 modules en cours (SRH, SIEP, SAFI, BGS)
- Synthèse générée, CI 100% PASS

**Objectif S4-03** : Créer le tag sémantique **v1.0.0** marquant la première version production.

**Workflow** :
1. ✅ S4-00 → S4-01 → S4-02 (GO Stéphane)
2. **S4-03 : Tag v1.0.0** ⏳
3. S4-04 : Publication main + release GitHub

---

## Objectif

**Créer tag v1.0.0** sur branche `draft` avec :
- CHANGELOG mis à jour (section v1.0.0 détaillée)
- Tag Git annoté avec message standard
- Tag pushé vers remote

**Livrables** :
- `CHANGELOG.md` enrichi (section v1.0.0 ~50 lignes)
- Tag `v1.0.0` créé et pushé
- Validation tag bien formé (sémantique, annotation)

---

## Prérequis

- [x] S4-02 complété (GO Stéphane obtenu)
- [x] Branche `draft` à jour et pushée
- [x] CI draft 100% PASS (dernier commit)
- [x] Aucun commit pending (sauf CHANGELOG.md à modifier en Étape 1)

---

## Étapes d'implémentation

### Étape 1 - Préparer CHANGELOG v1.0.0 (30 min)

**Objectif** : Ajouter section v1.0.0 au CHANGELOG avec format hybrid (option b validée Q29).

#### Microtâches

**1.1 Lire CHANGELOG actuel** (5 min)

```bash
head -50 CHANGELOG.md
```

Identifier :
- Section v0.2.0 (dernière version)
- Format utilisé (sections thématiques, ✅ checkmarks)
- Ligne d'insertion (après titre, avant v0.2.0)

**1.2 Rédiger section v1.0.0** (20 min)

Ajouter en tête de CHANGELOG (après ligne 3) :

```markdown
## v1.0.0 – 2025-10-XX

**⚠️ VERSION HYBRID - Contenus partiellement validés**

### Modules RÉELS (mappés depuis SPAN officiels)
- ✅ **SIRCOM** : 24/31 points validés (77.4%) - source : span-sircom-sg.md
- ✅ **SNUM Portailpro.gouv** : 21/31 points validés (67.7%) - source : span-portail-pro.sg.md
- **Total validés : 45/62 (72.6%)**

### Modules EN COURS (structure framework)
- 🔄 SRH, SIEP, SAFI, BGS : Structure framework présente, contenus à renseigner (0/124 points)
- ⚠️ Disclaimer présent : README, homepage, PDF, modules, synthèse
- Prêts pour onboarding Phase 2 (référents services à identifier)

### Infrastructure production-ready
- ✅ Framework technique complet (31 points DINUM × 6 modules = 186 points)
- ✅ CI/CD 100% PASS (scoring + build + PDF + tests)
- ✅ Preview privée GitHub Pages (org-only, draft + main)
- ✅ Tests unitaires (18) + E2E (9 scénarios)
- ✅ Export PDF accessible avec métadonnées enrichies
- ✅ Scoring automatisé avec colonne État (✅ Validé / 🔄 En cours)
- ✅ Tests validation_status front-matter

### Documentation
- ✅ CONTRIBUTING.md (workflow contributeur, Option A GitHub web + Option B Git local)
- ✅ Template Pull Request
- ✅ 6 modules structurés (5 sections obligatoires + 31 points DINUM)
- ✅ Sources SPAN officielles documentées (span/README.md + métadonnées)
- ✅ Guide mapping détaillé (roadmap/S4-00-mapping-contenus.md, ~400 lignes)

### Roadmaps BMAD complétées (Semaine 4 - Production)
- S4-00 : Guide mapping assisté (~3h - tables correspondance + instructions)
- S4-01 : Review Bertrand/Alexandra (~8-10h - finalisation 6 modules)
- S4-02 : Présentation Stéphane → GO concept (~2h30)
- S4-03 : Tag v1.0.0 + CHANGELOG (~1h)
- S4-04 : Publication production (merge draft→main, release GitHub)

### Prochaines étapes (v1.1+)
- 🔜 Phase 2 : Onboarding 4 référents services (modules en cours → validés)
- 🔜 Semaine 5 : Audit RGAA externe (framework + SIRCOM/SNUM)
- 🔜 Amélioration continue contenus (compléter points non cochés SIRCOM/SNUM)
- 🔜 Communication interne SG (après validation Chef SNUM)
- 🔜 Extensions potentielles : autres services SNUM, modules directions support

---
```

**Format** : Aligner avec v0.2.0 du CHANGELOG (checkmarks ✅, sections thématiques, détails techniques).

**Ton** : Transparence disclaimers ⚠️ + valorisation framework mature ✅.

**1.3 Éditer CHANGELOG.md** (5 min)

```bash
# Ouvrir éditeur
nano CHANGELOG.md
# ou
code CHANGELOG.md
```

- Insérer section v1.0.0 après ligne 3 (avant v0.2.0)
- Remplacer `2025-10-XX` par date réelle du jour
- Vérifier formatage markdown (pas de ligne cassée)
- Sauvegarder

**1.4 Vérifier rendu CHANGELOG** (optionnel, 5 min)

```bash
# Tester rendu markdown si doute
mdcat CHANGELOG.md | head -100
# ou ouvrir preview VSCode
```

---

### Étape 2 - Créer tag v1.0.0 (15 min)

**Objectif** : Tag Git annoté sémantique.

#### Microtâches

**2.1 Vérifier état branche** (5 min)

```bash
# Vérifier branch actuelle
git branch --show-current
# Attendu : draft

# Vérifier working directory clean
git status
# Attendu : nothing to commit, working tree clean (SAUF CHANGELOG.md modifié)
```

**Si CHANGELOG.md modifié mais pas encore commité** :
```bash
git add CHANGELOG.md
git commit -m "docs(changelog): ajoute section v1.0.0 hybrid

- 2 modules validés SIRCOM/SNUM (45/62 points)
- 4 modules en cours (structure framework)
- Infrastructure production-ready (CI, PDF, scoring)
- Roadmaps S4 complétées
- Prochaines étapes Phase 2

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**2.2 Créer tag annotated** (5 min)

```bash
git tag -a v1.0.0 -m "Release SPAN SG v1.0.0 - Framework Production Hybrid

Version 1.0.0 : Framework technique complet + 2 modules services validés.

Modules validés :
- SIRCOM : 24/31 (77.4%)
- SNUM Portailpro.gouv : 21/31 (67.7%)

Modules en cours :
- SRH, SIEP, SAFI, BGS : Structure framework (0/124)

Infrastructure :
- CI/CD 100% automatisé
- Tests unitaires (18) + E2E (9)
- Export PDF accessible
- Scoring avec colonne État

Documentation :
- CONTRIBUTING.md
- Guide mapping (~400 lignes)
- 6 modules structurés

Validation :
- GO concept Stéphane (2025-10-XX)
- Attente validation Chef SNUM pour communication

Voir CHANGELOG.md pour détails complets.

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Format tag** :
- Première ligne : Titre court (≤60 caractères)
- Ligne vide
- Paragraphes descriptifs (contexte, modules, infra, validation)
- Ligne vide
- Renvoi CHANGELOG pour détails
- Signature Claude Code

**2.3 Vérifier tag créé** (5 min)

```bash
# Lister tags
git tag
# Attendu : v1.0.0 (premier tag du projet)

# Afficher annotation tag
git show v1.0.0
# Vérifier : message complet, commit associé correct (dernier commit draft)

# Vérifier tag pointe sur bon commit
git log --oneline -1 v1.0.0
# Attendu : hash + message dernier commit (CHANGELOG ou S4-01 final)
```

---

### Étape 3 - Push tag vers remote (10 min)

**Objectif** : Rendre tag accessible sur GitHub.

#### Microtâches

**3.1 Push tag uniquement** (5 min)

```bash
# Push tag v1.0.0 vers origin
git push origin v1.0.0
```

**Vérification** :
- Pas d'erreur Git
- Message : `* [new tag]         v1.0.0 -> v1.0.0`

**3.2 Vérifier tag sur GitHub** (5 min)

Ouvrir : https://github.com/Alexmacapple/span-sg-repo/tags

**Vérifier** :
- [ ] Tag v1.0.0 visible dans liste
- [ ] Date création = aujourd'hui
- [ ] Commit associé = dernier commit draft
- [ ] Annotation visible (clic sur tag → message complet)

**Alternative CLI** :
```bash
gh release list
# Si release pas encore créée (S4-04), tag visible mais pas de release

git ls-remote --tags origin
# Vérifier v1.0.0 présent dans output
```

---

### Étape 4 - Validation finale (5 min)

**Checklist complétude** :

- [ ] CHANGELOG.md contient section v1.0.0 (~50 lignes)
- [ ] Section v1.0.0 avec format hybrid (modules réels, en cours, infra, roadmaps, prochaines étapes)
- [ ] Date v1.0.0 = date réelle (pas placeholder)
- [ ] Tag v1.0.0 créé localement (`git tag` liste v1.0.0)
- [ ] Tag annoté avec message complet (>10 lignes)
- [ ] Tag pushé vers remote (`gh release list` ou GitHub web)
- [ ] Tag pointe sur dernier commit draft

**Commit final (si CHANGELOG commité séparément)** :
```bash
# Si CHANGELOG pas encore commité + pushé
git push origin draft
```

**Résultat attendu** :
- Branche draft avec tag v1.0.0
- CHANGELOG à jour
- Prêt pour S4-04 (merge draft→main + release GitHub)

---

## Critères d'acceptation

### CHANGELOG
- [ ] Section v1.0.0 ajoutée en tête (après titre, avant v0.2.0)
- [ ] Format hybrid avec disclaimers ⚠️ et checkmarks ✅
- [ ] Modules réels listés avec scores (SIRCOM 24/31, SNUM 21/31)
- [ ] Modules en cours listés (SRH, SIEP, SAFI, BGS)
- [ ] Infrastructure détaillée (CI, tests, PDF, scoring)
- [ ] Roadmaps S4 mentionnées (S4-00 à S4-04)
- [ ] Prochaines étapes Phase 2 (onboarding, audit RGAA)
- [ ] Date réelle (pas placeholder)

### Tag Git
- [ ] Tag v1.0.0 créé (`git tag` liste)
- [ ] Tag annotated (message >10 lignes)
- [ ] Message tag contient : modules, infra, validation Stéphane, renvoi CHANGELOG
- [ ] Tag pointe sur dernier commit draft
- [ ] Tag pushé vers origin (`git ls-remote --tags` confirme)
- [ ] Tag visible sur GitHub web (https://github.com/.../tags)

### Versioning sémantique
- [ ] Format v1.0.0 respecté (MAJOR.MINOR.PATCH)
- [ ] v1.0.0 = premier release production (cohérent)
- [ ] Pas de suffixe -beta, -rc (version finale)

---

## Dépendances

**Bloque** : S4-04 (publication production nécessite tag v1.0.0 existant)

**Dépend de** :
- S4-02 (GO Stéphane requis avant tag)
- Branche draft finalisée (contenus S4-01)
- CI draft 100% PASS

---

## Références

- **CHANGELOG actuel** : `CHANGELOG.md` (v0.2.0 dernier)
- **Versioning sémantique** : https://semver.org/
- **Git tagging** : `git tag --help`, https://git-scm.com/book/en/v2/Git-Basics-Tagging
- **Format annotation** : Inspiré de Keep a Changelog (https://keepachangelog.com/)

---

## Notes et risques

### Versioning : pourquoi v1.0.0 et pas v0.3.0 ?

**Décision** : v1.0.0 = **première version production** (framework complet + modules opérationnels).

**Justification** :
- v0.x.x = développement/beta (v0.1.0 MVP, v0.2.0 Automatisation)
- **v1.0.0 = production-ready** : Infrastructure mature, GO validateur, déploiement main prévu
- Sémantique : MAJOR=1 = API stable (structure modules, 31 points DINUM, scoring)

**Alternative rejetée** : v0.3.0 sous-estime maturité (tests 100% PASS, CI rodé, documentation complète).

### CHANGELOG : niveau détail

Section v1.0.0 **détaillée** (~50 lignes) vs concise (10 lignes).

**Décision** : Détaillée (option b validée Q29).

**Justification** :
- v1.0.0 = milestone majeur (mérite documentation exhaustive)
- Cohérence avec v0.2.0 (59 commits, sections thématiques détaillées)
- Transparence disclaimers = essentielle pour contexte hybrid
- Traçabilité roadmaps S4 (S4-00 à S4-04 complétées)

### Tag annotation : utilité

**Tag annotated** (avec message) vs **tag lightweight** (pointeur simple).

**Décision** : Annotated requis.

**Justification** :
- Releases officielles = toujours annotated (best practice Git)
- Message tag = contexte v1.0.0 autonome (sans lire CHANGELOG)
- Signature + date dans Git metadata (traçabilité)
- GitHub affiche annotation dans UI tags

### Timing tag : avant ou après merge main ?

**Décision** : Tag sur `draft` (S4-03), AVANT merge main (S4-04).

**Justification** :
- Tag marque état code validé (draft finalisé = contenu stable)
- Merge draft→main préserve tag (Git suit le commit)
- Release GitHub (S4-04) référencera tag v1.0.0 déjà existant
- Rollback possible : si merge main échoue, tag draft reste valide

**Workflow** :
```
draft (S4-01 final) → tag v1.0.0 (S4-03) → merge draft→main (S4-04) → release GitHub v1.0.0
```

### Date CHANGELOG : jour création tag ou jour merge main ?

**Décision** : Date **jour création tag** (S4-03).

**Justification** :
- CHANGELOG documente état code taggé
- Tag v1.0.0 = jalonnement officiel
- Merge main (S4-04) peut être quelques jours après (validation Chef SNUM, timing)

**Format** : `## v1.0.0 – 2025-10-15` (exemple si tag créé le 15/10).

### Rollback tag : si erreur détectée après push

Si erreur critique détectée après `git push origin v1.0.0` (avant merge main) :

**Procédure correction** :
```bash
# 1. Supprimer tag local
git tag -d v1.0.0

# 2. Supprimer tag remote
git push origin :refs/tags/v1.0.0

# 3. Corriger erreur (commit fix)
git add [files]
git commit -m "fix: correction critique pour v1.0.0"

# 4. Re-créer tag v1.0.0 sur nouveau commit
git tag -a v1.0.0 -m "[message corrigé]"
git push origin v1.0.0
```

**Condition** : Seulement si tag **pas encore utilisé** (pas de release GitHub créée, pas de communication externe).

---

## Post-tâche

### Notification équipe (optionnel)

Informer Bertrand/Alexandra :
```
📧 Sujet : Tag v1.0.0 créé - Prêt pour publication

Le tag v1.0.0 a été créé sur draft.

Contenu :
- SIRCOM : 24/31 (77.4%)
- SNUM : 21/31 (67.7%)
- 4 modules en cours (SRH, SIEP, SAFI, BGS)

CHANGELOG mis à jour.
Prochaine étape : S4-04 publication production (merge draft→main).

Timing : Attente validation Chef SNUM via Stéphane.
```

### Backup tag (optionnel, si paranoïa)

Exporter annotation tag localement :
```bash
git show v1.0.0 > /tmp/tag-v1.0.0-annotation.txt
```

Utile si besoin re-créer tag identique après suppression accidentelle.

---

*Dernière mise à jour : 2025-10-02*
