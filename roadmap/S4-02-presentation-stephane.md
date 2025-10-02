---
bmad_phase: production
bmad_agent: dev
story_type: validation
autonomous: false
validation: stephane-go-concept
---

# Story S4-02 : Présentation concept v1.0 à Stéphane

**Phase** : Semaine 4 - Production
**Priorité** : Critique (validation GO/NO-GO)
**Estimation** : 2h30-3h (Sprint 4)

---

## Contexte projet

**Après S4-01** : Contenus v1.0 finalisés
- SIRCOM : 25/31 points validés (mapping depuis span-sircom-sg.md)
- SNUM : 21/31 points validés (mapping depuis span-portail-pro.sg.md)
- 4 modules en cours validés (SRH, SIEP, SAFI, BGS avec disclaimers)
- Synthèse générée avec colonne État (✅ Validé / 🔄 En cours)
- 6 highlights identifiés pour démonstration

**Stéphane** : Chef mission numérique, référent Design SNUM-SG, N+2 Alexandra
- **Rôle** : Validation concept avant GO final Chef SNUM
- **Enjeu** : Vérifier maturité framework, cohérence stratégie hybrid, faisabilité déploiement

**Workflow validation** :
1. Bertrand/Alexandra → review interne (S4-01) ✅
2. **Stéphane → validation concept (S4-02)** ⏳
3. Chef SNUM → GO final production (après S4-03/S4-04)

---

## Objectif

**Obtenir le GO concept de Stéphane** pour :
- Valider approche hybrid (2 modules réels + 4 en cours)
- Confirmer qualité framework technique
- Autoriser passage à v1.0 (tag + publication)

**Livrables** :
- Présentation démo live 15 min (6 éléments clés)
- Réponses questions Stéphane (FAQ préparée)
- Décision GO/NO-GO documentée
- Ajustements post-feedback si nécessaires (buffer 1h)

---

## Prérequis

- [x] S4-01 complété (contenus finalisés, highlights identifiés)
- [x] Preview privée draft accessible (https://alexmacapple.github.io/span-sg-repo/draft/)
- [x] PDF téléchargé depuis dernier artefact CI
- [x] Scores calculés (synthese.md à jour)
- [x] CI 100% PASS (badges verts)

---

## Étapes d'implémentation

### Préparation présentation (1h)

#### Microtâches

**1.1 Vérifier environnement technique** (20 min)

- [ ] Preview draft accessible et à jour :
  ```bash
  # Vérifier dernier commit draft déployé
  gh run list --branch draft --limit 1
  # Attendre CI terminée avant présentation
  ```
- [ ] URL preview : https://alexmacapple.github.io/span-sg-repo/draft/
- [ ] Navigation 6 modules fonctionnelle (tester manuellement)
- [ ] Disclaimer visible homepage
- [ ] Synthèse affichée avec colonne État

**1.2 Télécharger PDF artefact CI** (10 min)

```bash
# Récupérer PDF dernière CI draft
RUN_ID=$(gh run list --branch draft --limit 1 --json databaseId --jq '.[0].databaseId')
gh run download $RUN_ID --name exports

# Vérifier PDF accessible
open exports/span-sg.pdf
```

- [ ] PDF ouvre correctement
- [ ] Métadonnées visibles (propriétés document)
- [ ] 6 modules présents dans sommaire

**1.3 Préparer checklist démonstration** (20 min)

Créer support écrit (papier ou fichier) avec les **6 points obligatoires** + timing :

| Timing | Élément | URL/Action | Message clé |
|--------|---------|------------|-------------|
| 0-3 min | Homepage + disclaimer | Ouvrir https://.../draft/ | "v1.0 hybrid : 2 validés, 4 en cours, framework complet" |
| 3-7 min | Module SIRCOM (réel) | Cliquer SIRCOM → Scroll 31 points | "25/31 mappés depuis SPAN officiel, sections remplies" |
| 7-10 min | Synthèse tableau de bord | Cliquer Synthèse | "Scoring automatisé, colonne État, transparence totale" |
| 10-12 min | PDF accessible | Télécharger PDF (ou montrer local) | "Export conforme RGAA, métadonnées enrichies" |
| 12-14 min | CI/CD GitHub Actions | Montrer https://github.com/.../actions | "Tests automatisés 100% PASS, déploiement sécurisé" |
| 14-15 min | Navigation architecture | Retour homepage, montrer nav 6 modules | "Architecture modulaire, chaque service autonome" |

**1.4 Statistiques v1.0 à portée de main** (10 min)

Préparer fiche récap (lire depuis synthese.md ou calculer) :

```markdown
## Stats v1.0 SPAN SG

**Framework** :
- 31 points DINUM × 6 modules = 186 points total
- Architecture modulaire production-ready

**Modules validés (2)** :
- SIRCOM : 25/31 (80.6%)
- SNUM Portailpro.gouv : 21/31 (67.7%)
- **Total validés : 46/62 (74.2%)**

**Modules en cours (4)** :
- SRH, SIEP, SAFI, BGS : Structure framework, 0/124

**Taux global** : 46/186 (24.7%)

**Qualité** :
- CI/CD : 100% PASS
- Tests : 18 unitaires + 9 E2E
- Documentation : CONTRIBUTING.md, template PR, 6 modules structurés

**Déploiement** :
- Preview privée GitHub Pages (org-only)
- PDF accessible automatisé
- Scoring automatique (calculate_scores.py)
```

---

### Déroulé présentation (15-30 min)

**Format** : Démo live, navigation réelle dans preview draft.

**Ton** : Professionnel, pédagogique, transparent sur limitations (modules en cours).

#### Points obligatoires à montrer

**1. Homepage avec disclaimer (0-3 min)**

**Action** : Ouvrir https://alexmacapple.github.io/span-sg-repo/draft/

**Montrer** :
- Disclaimer visible : "⚠️ **État du déploiement v1.0** : 2 modules validés (SIRCOM, SNUM), 4 modules en cours..."
- Titre "SPAN SG - Schéma Pluriannuel Accessibilité Numérique"
- Navigation latérale avec 6 modules

**Message clé** :
> "v1.0 adopte une approche hybrid pragmatique : framework technique complet avec 2 modules services opérationnels (SIRCOM, SNUM), et 4 modules en structure (SRH, SIEP, SAFI, BGS) prêts pour onboarding progressif. Transparence totale via disclaimer 5 emplacements."

**2. Module SIRCOM réel (3-7 min)**

**Action** : Cliquer navigation → SIRCOM

**Montrer** :
- Badge "✅ Validé" dans synthèse (ou titre)
- Front-matter : service, référent, updated, validation_status
- 5 sections obligatoires remplies (Périmètre, État, Organisation, Plan, Indicateurs)
- **Scroll vers les 31 points DINUM** :
  - Points cochés `[x]` (25/31)
  - Points non cochés `[ ]` avec justification (6 TODO documentés, ex: "Budget annuel à documenter")
- Tableaux périmètre et plan d'action 2025 remplis

**Message clé** :
> "SIRCOM : 25/31 points validés, mappés depuis SPAN officiel (span-sircom-sg.md). Les 6 points non cochés sont justifiés (informations manquantes sources, à compléter Phase 2). Contenu professionnel, traçabilité complète."

**Anecdote si pertinent** : Montrer 1-2 exemples concrets de points validés (ex: "Référent désigné : Pôle web SG/SIRCOM").

**3. Synthèse tableau de bord (7-10 min)**

**Action** : Cliquer navigation → Synthèse (ou docs/synthese.md)

**Montrer** :
- Disclaimer en-tête (idem homepage)
- Tableau 6 modules :
  - Colonnes : Service | Score | Statut | **État**
  - SIRCOM, SNUM : ✅ Validé
  - SRH, SIEP, SAFI, BGS : 🔄 En cours
- Score global : 46/186 (24.7%)
- Date mise à jour

**Message clé** :
> "Scoring automatisé via CI (calculate_scores.py). Colonne État distingue modules validés vs en cours. Transparence totale : 24.7% global reflète stratégie hybrid (2/6 modules opérationnels). Progression trackable, ré-exécution automatique à chaque commit."

**4. PDF export accessible (10-12 min)**

**Action** : Montrer PDF téléchargé (local) ou télécharger depuis artefact CI

**Montrer** :
- Sommaire PDF avec 6 modules
- Page de garde avec disclaimer compliance :
  > "ℹ️ **Périmètre version 1.0** : Ce document couvre 2 services avec contenus validés (SIRCOM, SNUM) et 4 services avec structure présente (en cours de renseignement). Infrastructure conforme RGAA 4.1."
- Métadonnées enrichies (Propriétés document) :
  - Auteur : SG MEFSIN
  - Sujet : Schéma Pluriannuel Accessibilité Numérique
  - Mots-clés : SPAN, accessibilité, RGAA 4.1, DINUM
- Navigation PDF fonctionnelle (signets)

**Message clé** :
> "Export PDF automatisé (mkdocs-pdf-export + enrich_pdf_metadata.py). Métadonnées enrichies pour conformité RGAA. PDF/UA accessible. Généré systématiquement par CI, archivable pour audits."

**Si Stéphane questionne "Infrastructure conforme RGAA 4.1"** :
> "Objectif design basé sur MkDocs Material (thème accessible par conception, validé communauté). Audit externe S5 prévu pour certification officielle v1.1."

**5. Infrastructure CI/CD (12-14 min)**

**Action** : Ouvrir https://github.com/Alexmacapple/span-sg-repo/actions (ou montrer badges README)

**Montrer** :
- Workflow "Build and Deploy" : ✅ dernière exécution PASS
- Badges status :
  - ![Build](https://github.com/.../workflows/build/badge.svg)
  - ![Tests](https://github.com/.../workflows/tests/badge.svg)
- Steps workflow (si temps) :
  1. Calculate SPAN scores
  2. Run tests (pytest)
  3. Build site (mkdocs)
  4. Generate PDF
  5. Deploy to Pages

**Message clé** :
> "CI/CD 100% automatisé depuis S2 (Semaine 2 Automatisation). Tests unitaires (18) + E2E (9 scénarios) garantissent qualité. Déploiement conditionnel : draft → /draft/, main → racine. Preview privée org-only (sécurité)."

**6. Architecture modulaire (14-15 min)**

**Action** : Retour homepage, montrer navigation latérale

**Montrer** :
- Liste 6 modules dans nav
- Cliquer rapidement sur SRH (module en cours) :
  - Disclaimer "🔄 Module en cours de complétion"
  - Structure présente (5 sections + 31 points)
  - Placeholders professionnels (pas Lorem ipsum)
- Retour navigation

**Message clé** :
> "Architecture modulaire scalable : chaque service = module autonome. Modules en cours démontrent potentiel framework pour futurs référents. Structure claire, process rodé. Onboarding Phase 2 facilité par cette base."

---

### Questions anticipées Stéphane (FAQ préparée)

**Q1 : "Pourquoi seulement 2 modules validés dans v1.0 ? C'est suffisant ?"**

**Réponse préparée** :
> "**Contexte contributeurs** : Projet géré par 2 personnes (Bertrand + Alexandra), pas de référents services externes identifiés court terme. 2 modules validés démontrent la maturité du framework (mapping SPAN → DINUM fonctionnel) tout en maintenant un périmètre réaliste. Les 4 modules en cours illustrent le potentiel pour Phase 2 onboarding. **Qualité > quantité** : mieux vaut 2 modules professionnels que 6 modules bâclés. v1.0 = fondations solides pour croissance progressive."

**Argument complémentaire** : Framework technique 100% opérationnel (CI, scoring, PDF) = investissement rentabilisé dès maintenant.

---

**Q2 : "Les 6 points non cochés SIRCOM / 10 points SNUM, c'est un problème pour la conformité ?"**

**Réponse préparée** :
> "**Non, c'est transparent et acceptable pour v1.0**. Les points non cochés sont **justifiés** dans le contenu (ex: 'Budget annuel à documenter'). Sources SPAN sont des politiques stratégiques, pas des réponses exhaustives aux 31 points DINUM. Les gaps identifiés = feuille de route Phase 2 claire. **Approche pragmatique** : SPAN n'est pas une certification RGAA, mais un outil de pilotage. 25/31 SIRCOM (80%) démontre engagement sérieux. Points manquants = souvent administratifs (grille recrutement RH, tests utilisateurs à planifier) vs techniques."

**Argument complémentaire** : Scoring automatisé permet tracking progression facilement (re-cocher points quand info disponible).

---

**Q3 : "Risque de confusion publique avec modules 'en cours' visibles en production ?"**

**Réponse préparée** :
> "**Non, disclaimers explicites 5 emplacements** : README (ton positif), homepage (ton neutre), PDF (ton compliance), modules en cours (note courte), synthèse (colonne État). Preview privée GitHub Pages **org-only** = accès restreint membres organisation. Pas de communication externe prévue pour v1.0 (attente validation Chef SNUM). Modules en cours = **démonstration framework**, pas affirmation de conformité services. Badge État (✅ Validé vs 🔄 En cours) = distinction visuelle claire."

**Argument complémentaire** : Si vraiment préoccupant, possibilité de publier seulement SIRCOM/SNUM sur main et garder 4 autres sur draft uniquement (flexibilité technique).

---

**Q4 : "Quelle est la charge maintenance après v1.0 ?"**

**Réponse préparée** :
> "**Charge faible grâce à automatisation** : 2h/mois Bertrand/Alexandra estimé (hors enrichissement contenus). Scripts automatisés (scoring, PDF, CI) = 0 intervention manuelle. Mises à jour ponctuelles : corrections contenu modules (15 min), ajout nouveau module (1h avec script create-module.sh), réponse contributeur externe (30 min). **Évolutif** : si charge augmente (Phase 2 avec 4 référents services), process documenté (CONTRIBUTING.md) permet autonomie contributeurs."

**Argument complémentaire** : Infrastructure mature S2 (tests automatisés) = peu de bugs attendus.

---

**Q5 : "Quand audit RGAA externe prévu ?"**

**Réponse préparée** :
> "**Audit externe prévu S5** (Semaine 5 - PDF accessible, après v1.0). Budget à définir (estimation 5-8 k€ audit complet site MkDocs). Audit ciblera framework technique (site, navigation, PDF) + modules SIRCOM/SNUM. MkDocs Material = thème accessible par design (validé communauté). Auto-évaluation technique en cours (navigation clavier, contrastes, structure sémantique). **Priorisation** : v1.0 d'abord (fondations), puis audit certifiant pour v1.1. Audit externe donnera crédibilité et identifiera axes amélioration."

**Argument complémentaire** : MkDocs Material = thème accessible par design, risques conformité limités.

---

**Q6 : "Scope SNUM = Portailpro.gouv uniquement, pourquoi pas l'ensemble SNUM ?"**

**Réponse préparée** :
> "**Source SPAN disponible** = Portailpro.gouv (Mission France Recouvrement). Document `span-portail-pro.sg.md` couvre ce périmètre spécifique. Autres services SNUM non documentés dans sources actuelles. **Option 1 clarification** : Ajouter note module SNUM 'Périmètre v1.0 : Portailpro.gouv. Autres services SNUM à intégrer Phase 2.' **Option 2 extension** : Si d'autres SPAN SNUM disponibles, créer modules dédiés (ex: snum-intranet.md, snum-portail.md). **Quelle est votre préférence, Stéphane** ?"

**Argument complémentaire** : Architecture modulaire permet ajouts futurs sans refonte.

---

**Q7 : "Plan Phase 2 : comment onboarder les 4 référents services manquants ?"**

**Réponse préparée** :
> "**Processus rodé grâce à S3 (skippé mais documenté)** : roadmaps S3-02 Formation Git + S3-03 Premiers contenus existent. Workflow contributeur documenté (CONTRIBUTING.md). **Onboarding type** : 1) Désignation référent service, 2) Formation Git 2h (option A GitHub web OU option B local), 3) Remise template module (structure claire), 4) Accompagnement 1er commit (support Bertrand/Alexandra). Estimation 4h/référent. **Phase 2 timing** : Dépend identification référents (RH/directions). Framework prêt, attente décision organisationnelle."

**Argument complémentaire** : Modules fictifs actuels = démonstration concrète pour futurs référents (réassurance).

---

**Q8 : "Validation Chef SNUM : quand et comment ?"**

**Réponse préparée** :
> "**Après votre GO concept** : si Stéphane valide, passage à S4-03 (tag v1.0) + S4-04 (publication main). Communication Chef SNUM via Stéphane (vous [Stéphane] gérez remontée hiérarchique). Format validation Chef SNUM flexible : présentation 10 min OU email récap + lien production OU validation implicite si Stéphane sponsor. **Notre recommandation** : Présentation courte Chef SNUM (10 min, focus framework mature + 2 modules opérationnels) pour obtenir GO formel avant communication large. **Timing** : Semaine 4 fin si Stéphane GO aujourd'hui."

**Argument complémentaire** : v1.0 production peut rester org-only (Pages privé) jusqu'à GO Chef SNUM.

---

### Post-présentation : Décision et ajustements (1h buffer)

#### Microtâches

**1. Documenter décision Stéphane** (10 min)

Créer fichier `roadmap/S4-02-decision-stephane.md` :

```markdown
# Décision Stéphane - Présentation v1.0

**Date** : 2025-10-XX
**Participants** : Stéphane, Bertrand, Alexandra
**Durée** : X min

## Décision

- [ ] **GO concept** : Validation approche hybrid, autorisation tag v1.0
- [ ] **GO conditionnel** : Validation sous réserve ajustements (liste ci-dessous)
- [ ] **NO-GO temporaire** : Demande modifications avant re-présentation
- [ ] **NO-GO définitif** : Abandon stratégie actuelle (rare)

## Feedback Stéphane

[Notes verbatim ou synthèse]

- Point apprécié 1 : ...
- Point apprécié 2 : ...
- Préoccupation 1 : ...
- Préoccupation 2 : ...

## Ajustements demandés (si GO conditionnel)

- [ ] Ajustement 1 : Description + estimation temps
- [ ] Ajustement 2 : ...

## Actions immédiates

- [ ] Si GO : Passer à S4-03 (tag v1.0)
- [ ] Si GO conditionnel : Implémenter ajustements puis S4-03
- [ ] Si NO-GO : Analyse causes + roadmap correctif S4bis

## Validation Chef SNUM

- **Format retenu** : [Présentation 10 min / Email récap / Validation implicite]
- **Timing prévu** : [Date]
- **Responsable communication** : [Stéphane / Bertrand / Alexandra]
```

**2. Implémenter ajustements si nécessaires** (0-50 min selon feedback)

**Exemples ajustements possibles** :
- Reformuler disclaimer (ton, emplacement)
- Ajouter note périmètre SNUM Portailpro
- Modifier badge État (couleur, wording)
- Compléter 1-2 points DINUM bloquants identifiés

**Principe** : Ajustements légers uniquement (≤1h). Si feedback majeur (refonte), documenter dans roadmap S4bis.

**3. Validation GO obtenu** (5 min)

Si **GO concept** confirmé :
- [ ] Marquer S4-02 comme complétée
- [ ] Commit décision : `git commit -m "docs(s4-02): GO concept Stéphane obtenu"`
- [ ] Passer immédiatement à S4-03 (tag v1.0)

---

## Critères d'acceptation

### Présentation
- [ ] 6 éléments obligatoires montrés (homepage, SIRCOM, synthèse, PDF, CI, architecture)
- [ ] Timing respecté (~15 min démo)
- [ ] Environnement technique fonctionnel (preview draft accessible, PDF dispo)
- [ ] Statistiques v1.0 présentées (taux global, modules validés)

### Questions/Réponses
- [ ] FAQ préparée (8 questions anticipées + réponses)
- [ ] Réponses claires et factuelles données
- [ ] Préoccupations Stéphane adressées

### Décision
- [ ] **GO concept obtenu** OU GO conditionnel avec ajustements ≤1h
- [ ] Décision documentée (fichier S4-02-decision-stephane.md)
- [ ] Actions immédiates identifiées (S4-03 ou ajustements)

### Communication
- [ ] Validation Chef SNUM : format et timing définis
- [ ] Responsable communication identifié

---

## Dépendances

**Bloque** : S4-03 (tag v1.0 nécessite GO Stéphane)

**Dépend de** :
- S4-01 (contenus finalisés, highlights identifiés)
- Preview draft déployée et accessible
- CI 100% PASS

---

## Références

- **Highlights** : Identifiés en S4-01 Phase 4
- **Statistiques v1.0** : Calculées en S4-01 Phase 4
- **Preview draft** : https://alexmacapple.github.io/span-sg-repo/draft/
- **GitHub Actions** : https://github.com/Alexmacapple/span-sg-repo/actions

---

## Notes et risques

### Format présentation : Démo live vs Slides

**Décision retenue** : Démo live (navigation réelle preview draft).

**Avantages** :
- Authenticité (produit réel, pas captures statiques)
- Interaction possible (Stéphane peut demander zoom sur détail)
- Démontre maturité technique (site fonctionnel)

**Risque** : Problème technique (Internet, CI qui échoue). **Mitigation** : Backup PDF téléchargé + screenshots clés si besoin.

### Durée présentation variable

Estimation 15 min démo + 15-30 min Q&A = **30-45 min total**.

Si Stéphane peu disponible : focus 3 éléments clés (homepage, SIRCOM, synthèse) = 10 min minimum.

Si Stéphane très engagé : démonstration approfondie (navigation tous modules, détails CI) = 30 min démo.

**Flexibilité** : Adapter selon signaux Stéphane (intérêt, questions, timing).

### Ton présentation

**Professionnel et transparent** :
- Assumer limitations (modules en cours, points non cochés)
- Valoriser forces (framework mature, 2 modules opérationnels, tests automatisés)
- Éviter survente ("meilleur SPAN France") ou minimisation ("c'est juste un prototype")

**Positionnement** : v1.0 = fondations solides pour déploiement progressif.

### Décision NO-GO : que faire ?

Si Stéphane dit **NO-GO** (rare) :
1. Documenter causes objectives (feedback verbatim)
2. Identifier si problème technique (bugs) OU stratégique (approche hybrid refusée)
3. Créer roadmap correctif **S4bis** :
   - Si technique : corriger + re-présenter rapidement
   - Si stratégique : analyser alternatives (tout en draft ? attendre 6 modules ? autre périmètre ?)

**Principe** : NO-GO = apprentissage, pas échec. Roadmap BMAD itératif.

### Communication Chef SNUM déléguée à Stéphane

**Hypothèse** : Stéphane gère remontée Chef SNUM (hiérarchie N+2 → N+3).

Si Chef SNUM veut présentation directe Bertrand/Alexandra :
- Réutiliser même démo (éprouvée avec Stéphane)
- Adapter timing si contraint (version 10 min focus framework)

---

*Dernière mise à jour : 2025-10-02*
