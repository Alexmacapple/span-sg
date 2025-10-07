---
bmad_phase: production
bmad_agent: dev
story_type: implementation
autonomous: false
validation: human-qa
---

# Story S4-01 : Review et finalisation contenus modules

**Phase** : Semaine 4 - Production
**Priorité** : Critique (bloque S4-02)
**Estimation** : 8-10h (Sprint 2-3)

---

## Contexte projet

**Après S4-00** : Guide de mapping disponible (`roadmap/S4-00-mapping-contenus.md`)
- Tables correspondance SIRCOM (25/31 mappables, 6 TODO)
- Tables correspondance SNUM (21/31 mappables, 10 TODO)
- Instructions guidées + 17 exemples pré-rédigés

**Objectif S4-01** : Exécuter le mapping complet des 2 modules réels + valider les 4 modules en cours + préparer éléments présentation Stéphane.

**Stratégie v1.0 Hybrid** :
- 2 modules **validés** : SIRCOM, SNUM (contenus réels finalisés, `validation_status: validated`)
- 4 modules **en cours** : SRH, SIEP, SAFI, BGS (structure framework, `validation_status: in_progress`)

**Workflow** : Bertrand/Alexandra exécutent mapping → validation interne → préparation S4-02 présentation Stéphane.

---

## Objectif

**Finaliser les contenus pour v1.0** :
1. Compléter mapping SIRCOM (31/31 points traités)
2. Compléter mapping SNUM (31/31 points traités)
3. Valider cohérence modules fictifs (SRH, SIEP, SAFI, BGS)
4. Générer synthèse globale (scores, highlights pour présentation)

**Livrables** :
- `docs/modules/sircom.md` finalisé (X/31 points cochés, validation_status: validated)
- `docs/modules/snum.md` finalisé (Y/31 points cochés, validation_status: validated)
- `docs/modules/{srh,siep,safi,bgs}.md` validés (structure, disclaimers, validation_status: in_progress)
- `docs/synthese.md` généré avec scores finaux + colonne État
- Liste 6 highlights pour présentation Stéphane (S4-02)

---

## Prérequis

- [x] S4-00 complété (guide mapping disponible)
- [x] Sources SPAN lisibles (`span/span-sircom-sg.md`, `span/span-portail-pro.sg.md`)
- [x] Script `calculate_scores.py` modifié (colonne État avec validation_status)
- [x] Branche `draft` à jour
- [ ] Coordination Bertrand/Alexandra décidée (Option A Séquentiel / B Parallèle / C Pair programming Phase 1)

---

## Étapes d'implémentation

### Phase 1 - Finaliser mapping SIRCOM (3h)

**Objectif** : SIRCOM 31/31 points traités (mappés OU justifiés N/A).

#### Microtâches

**1.1 Lire guide S4-00 SIRCOM** (15 min)
- Parcourir tables Catégories 1-5 SIRCOM
- Identifier 6 TODO S4-01 tracés :
  - Point 5 : Temps référent (préciser % ETP)
  - Point 7 : Budget annuel (demander montant)
  - Point 10 : Grille recrutement (documenter avec RH)
  - Point 20 : Critères sélection marchés (préciser pondération)
  - Point 23 : Tests utilisateurs handicapés (planifier)
  - Point 27 : Accès LSF (définir périmètre vidéos)
  - Point 28 : FALC (identifier contenus prioritaires)

**1.2 Exécuter mapping points faciles/moyens (1h30)**

Suivre guide S4-00, exécuter les **25 points mappables** :
- Catégorie 1 : Points 1, 2, 3 (3/3 mappables)
- Catégorie 2 : Points 4, 5, 6, 8, 9, 11, 12, 13, 14, 15 (10/12 mappables, skip 7, 10)
- Catégorie 3 : Points 16, 17, 18, 19, 21, 22 (6/8 mappables, skip 20, 23)
- Catégorie 4 : Points 24, 25, 26 (3/3 mappables)
- Catégorie 5 : Points 29, 30, 31 (3/5 mappables, skip 27, 28)

**Checklist exécution** :
- [ ] Ouvrir `docs/modules/sircom.md` en édition
- [ ] Suivre instructions S4-00 point par point
- [ ] Cocher `[x]` les points validés avec contenu renseigné
- [ ] Copier exemples fournis et adapter selon source réelle
- [ ] Laisser `[ ]` les points TODO (traités à l'étape 1.3)

**1.3 Traiter TODO difficiles (1h)**

Pour les **6 points TODO**, appliquer stratégie selon disponibilité info :

**Point 5 - Temps référent** :
- Chercher dans `span-sircom-sg.md` mentions "ETP", "temps dédié", "mi-temps"
- Si absent : renseigner "Référent accessibilité à temps partiel (% ETP à préciser)"
- Laisser `[ ]` non coché si info manquante

**Point 7 - Budget annuel** :
- Chercher montant budget (€, k€)
- Si absent : renseigner "Budget annuel dédié accessibilité (montant à documenter)"
- Laisser `[ ]` non coché

**Point 10 - Grille recrutement** :
- Probable absent source SPAN
- Renseigner "Grille de recrutement à documenter avec RH (compétences accessibilité à intégrer)"
- Laisser `[ ]` non coché

**Point 20 - Critères sélection** :
- Chercher pondération accessibilité dans marchés
- Si absent : "Pondération accessibilité dans critères sélection à préciser (recommandation : 10-15%)"
- Laisser `[ ]` non coché

**Point 23 - Tests utilisateurs** :
- Chercher mention tests avec personnes handicapées
- Si absent : "Tests utilisateurs avec personnes handicapées à planifier (recommandation : 2 sessions/an)"
- Laisser `[ ]` non coché

**Point 27 - LSF** :
- Définir périmètre vidéos concernées
- Renseigner "Accessibilité LSF à définir pour [X] vidéos institutionnelles prioritaires"
- Laisser `[ ]` non coché si périmètre flou

**Point 28 - FALC** :
- Identifier démarches essentielles
- Renseigner "Traduction FALC à prévoir pour [X] démarches prioritaires (à identifier avec métier)"
- Laisser `[ ]` non coché

**Résultat attendu Phase 1** :
- SIRCOM : 25/31 points cochés `[x]` (mappés depuis source)
- 6/31 points `[ ]` non cochés (TODO documentés avec justification)
- Fichier `docs/modules/sircom.md` complet et cohérent

**1.4 Validation interne SIRCOM** (15 min)
- [ ] Relire module SIRCOM intégralement
- [ ] Vérifier cohérence rédactionnelle (pas de "TODO" ou "[...]" oubliés)
- [ ] Vérifier front-matter : `service: SIRCOM`, `validation_status: validated`
- [ ] Commit intermédiaire : `git commit -m "feat(sircom): finalise mapping module SIRCOM (25/31 validés)"`

---

### Phase 2 - Finaliser mapping SNUM (2h30)

**Objectif** : SNUM 31/31 points traités.

#### Microtâches

**2.1 Lire guide S4-00 SNUM** (10 min)
- Parcourir tables Catégories 1-5 SNUM (références SIRCOM)
- Identifier 10 TODO S4-01 probables (points absents source courte)

**2.2 Exécuter mapping points mappables (1h30)**

Suivre guide S4-00 SNUM, exécuter les **21 points mappables** :
- Catégorie 1 : Points 1, 3 (2/3, skip 2 probable TODO)
- Catégorie 2 : Points 4, 5, 6, 8, 11, 13, 15 (7/12, skip 7, 9, 10, 12, 14 probables TODO)
- Catégorie 3 : Points 16, 17, 18, 19, 21, 22 (6/8, skip 20, 23 probables TODO)
- Catégorie 4 : Points 24, 25, 26 (3/3 mappables)
- Catégorie 5 : Points 29, 30, 31 (3/5, skip 27, 28 probables TODO)

**Astuce** : Réutiliser format réponses SIRCOM pour homogénéité (adapter service/dates/montants).

**2.3 Traiter TODO SNUM (30 min)**

Pour les **10 points TODO probables**, appliquer même stratégie que Phase 1.3 :
- Chercher info dans `span-portail-pro.sg.md` (document court, 106 lignes)
- Si absent : renseigner justification + laisser `[ ]` non coché
- Documenter avec note "À compléter Phase 2" si info nécessite source externe

**Résultat attendu Phase 2** :
- SNUM : 21/31 points cochés `[x]` (mappés depuis source)
- 10/31 points `[ ]` non cochés (TODO documentés)
- Fichier `docs/modules/snum.md` complet

**Note périmètre SNUM** : Le module couvre **Portailpro.gouv** (Mission France Recouvrement), pas l'ensemble SNUM.
- Option : Ajouter note en intro module "Périmètre v1.0 : Portailpro.gouv. Autres services SNUM à intégrer Phase 2."

**2.4 Validation interne SNUM** (20 min)
- [ ] Relire module SNUM intégralement
- [ ] Vérifier cohérence avec SIRCOM (format similaire)
- [ ] Vérifier front-matter : `service: SNUM`, `validation_status: validated`
- [ ] Commit : `git commit -m "feat(snum): finalise mapping module SNUM Portailpro.gouv (21/31 validés)"`

---

### Phase 3 - Valider modules fictifs (1h30)

**Objectif** : Vérifier cohérence des 4 modules en cours (SRH, SIEP, SAFI, BGS).

#### Microtâches

**3.1 Audit final structure et disclaimers** (30 min)

Pour chaque module `{srh.md, siep.md, safi.md, bgs.md}` :
- [ ] Structure complète (5 sections obligatoires présentes)
- [ ] 31 points DINUM présents `<!-- DINUM -->` (tous non cochés `[ ]`)
- [ ] Front-matter complet :
  ```yaml
  service: [SRH|SIEP|SAFI|BGS]
  referent: "[À définir]"
  updated: "2025-10-XX"
  validation_status: in_progress
  ```
- [ ] Disclaimer ajouté en intro :
  ```markdown
  > 🔄 **Module en cours de complétion** : Structure framework présente, contenus à renseigner (référent service à identifier).
  ```

**3.2 Homogénéiser contenu placeholder** (30 min)

Vérifier que les 5 sections obligatoires contiennent placeholders cohérents :
- **Section 1 - Périmètre** : Lister types applications attendus (ex: "Applications RH" pour SRH)
- **Section 2 - État des lieux** : Placeholder "Audits à réaliser"
- **Section 3 - Organisation** : "Référent à désigner"
- **Section 4 - Plan d'action** : Tableau vide ou 1 ligne exemple
- **Section 5 - Indicateurs** : Placeholder KPI types

**Objectif** : Modules fictifs doivent être **professionnels** (pas de "Lorem ipsum"), illustrer structure framework.

**3.3 Validation navigation MkDocs** (15 min)
- [ ] Vérifier `mkdocs.yml` liste les 6 modules
- [ ] Tester navigation locale `mkdocs serve` : 6 modules accessibles
- [ ] Pas d'erreur 404, checkboxes visibles

**3.4 Commit modules fictifs** (15 min)
- [ ] Commit : `git commit -m "chore(modules): valide 4 modules en cours (SRH, SIEP, SAFI, BGS) avec disclaimers"`

---

### Phase 4 - Synthèse et préparation présentation (1h)

**Objectif** : Générer scores finaux + identifier highlights pour présentation Stéphane (S4-02).

#### Microtâches

**4.1 Générer scores avec colonne État** (15 min)

```bash
# Calculer scores finaux
python scripts/calculate_scores.py
```

**Vérifier `docs/synthese.md` généré** :
- [ ] 6 modules listés (ordre alphabétique)
- [ ] Scores corrects :
  - SIRCOM : X/31 (attendu ~22-25/31)
  - SNUM : Y/31 (attendu ~18-21/31)
  - SRH, SIEP, SAFI, BGS : 0/31 (Non renseigné)
- [ ] Colonne **État** affichée :
  - SIRCOM, SNUM : ✅ Validé
  - SRH, SIEP, SAFI, BGS : 🔄 En cours
- [ ] Disclaimer en-tête :
  ```markdown
  ⚠️ **État du déploiement v1.0** : 2 modules validés (SIRCOM, SNUM), 4 modules en cours de complétion. Framework production-ready, contenus enrichis progressivement.
  ```

**4.2 Identifier 6 highlights présentation** (20 min)

Préparer **6 éléments clés** à montrer à Stéphane (S4-02) :

1. **Homepage avec disclaimer** : Contexte v1.0 hybrid clair dès l'accueil
2. **Navigation 6 modules** : Framework complet, architecture modulaire
3. **Module SIRCOM (réel)** : Démonstration contenu mappé (25/31 points, sections remplies)
4. **Synthèse tableau de bord** : Scores agrégés, colonne État, transparence
5. **PDF export accessible** : Métadonnées enrichies, conforme RGAA
6. **CI/CD GitHub Actions** : Workflow 100% PASS, tests automatisés

**Pour chaque highlight**, noter :
- **Élément à montrer** (URL ou capture)
- **Message clé** (1 phrase pitch)
- **Temps démo** (~2 min par élément)

**Validation** : Vérifier que S4-02 PRD contient les 6 highlights identifiés (homepage, synthèse, SIRCOM, PDF, CI, architecture) dans sa section "Présentation".

**4.3 Statistiques v1.0 pour présentation** (15 min)

Calculer statistiques à présenter :
- **Framework** : 31 points DINUM × 6 modules = 186 points total
- **Modules validés** : 2 (SIRCOM X/31, SNUM Y/31) = Z/62 points (~40-46/62 attendu sur base S4-00)
- **Modules en cours** : 4 (structure framework, 0/124 points)
- **Taux global** : 46/186 (24.7%) sur base estimations S4-00 (25 SIRCOM + 21 SNUM)
- **Tests** : 18 unitaires + 9 E2E (100% PASS)
- **Documentation** : 6 modules structurés, CONTRIBUTING.md, template PR

**4.4 Validation finale globale** (10 min)
- [ ] 6 modules finalisés (SIRCOM, SNUM validés, 4 en cours cohérents)
- [ ] Synthese.md généré avec colonne État
- [ ] Highlights identifiés (6 éléments)
- [ ] Statistiques calculées
- [ ] Branche draft à jour et pushée

**4.5 Commit final S4-01** (5 min)
```bash
git add docs/modules/*.md docs/synthese.md
git commit -m "feat(s4-01): finalise review contenus v1.0

- SIRCOM : 25/31 validés (mapping depuis span-sircom-sg.md)
- SNUM : 21/31 validés (mapping depuis span-portail-pro.sg.md)
- 4 modules en cours validés (disclaimers, validation_status)
- Synthèse générée avec colonne État
- Highlights présentation Stéphane identifiés

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin draft
```

---

## Critères d'acceptation

### Modules réels (SIRCOM, SNUM)
- [ ] SIRCOM : 31/31 points traités (25 cochés, 6 justifiés N/A avec TODO)
- [ ] SNUM : 31/31 points traités (21 cochés, 10 justifiés N/A avec TODO)
- [ ] Front-matter complet avec `validation_status: validated`
- [ ] Contenu cohérent et professionnel (pas de placeholder vide)
- [ ] Sources SPAN tracées (mentions sections sources dans contenu)

### Modules en cours (SRH, SIEP, SAFI, BGS)
- [ ] Structure framework complète (5 sections + 31 points)
- [ ] Disclaimer "Module en cours" présent
- [ ] Front-matter avec `validation_status: in_progress`
- [ ] Placeholders professionnels (pas de Lorem ipsum)

### Synthèse globale
- [ ] `docs/synthese.md` généré avec script
- [ ] 6 modules listés, scores corrects
- [ ] Colonne État affichée (✅ Validé, 🔄 En cours)
- [ ] Disclaimer v1.0 en en-tête

### Préparation présentation
- [ ] 6 highlights identifiés (homepage, navigation, SIRCOM, synthèse, PDF, CI)
- [ ] Statistiques v1.0 calculées (taux global, modules validés)
- [ ] Fichier highlights créé pour S4-02

### Qualité technique
- [ ] Navigation MkDocs fonctionnelle (6 modules accessibles)
- [ ] Pas d'erreur markdown (build --strict OK)
- [ ] Commits atomiques (1 par phase)
- [ ] Branche draft pushée

---

## Dépendances

**Bloque** : S4-02 (présentation Stéphane nécessite contenus finalisés + highlights)

**Dépend de** :
- S4-00 (guide mapping utilisé pour exécution)
- Script `calculate_scores.py` modifié (colonne État)
- Tests E2E validant `validation_status` (si exécutés avant S4-02)

---

## Références

- **Guide mapping** : `roadmap/S4-00-mapping-contenus.md`
- **Sources SPAN** : `span/span-sircom-sg.md`, `span/span-portail-pro.sg.md`
- **Template** : `docs/modules/_template.md`
- **Script scoring** : `scripts/calculate_scores.py`

---

## Notes et risques

### Durée variable par contributeur

Estimation 8-10h basée sur :
- Bertrand : expérience projet, connaît sources → plutôt 8h
- Alexandra : découverte sources SPAN → plutôt 10h

**Flexibilité** : Pas de deadline stricte, privilégier qualité vs vitesse.

### Points non cochés acceptables

**v1.0 hybrid assume** que certains points resteront `[ ]` non cochés :
- SIRCOM : ~6 points non cochés (info manquante sources) = **25/31 OK**
- SNUM : ~10 points non cochés (source courte) = **21/31 OK**

**Message présentation Stéphane** : "v1.0 = framework complet + 2 modules opérationnels partiels (en enrichissement continu)."

### Scope SNUM = Portailpro.gouv uniquement

Le module SNUM couvre **Portailpro.gouv** (Mission France Recouvrement), pas l'ensemble des services SNUM.

**Clarification pour Stéphane** : Si d'autres applications SNUM doivent être intégrées, prévoir Phase 2 ou module dédié.

**Décision Phase 4.2** : Ajouter note clarification dans module OU renommer `snum.md` → `snum-portailpro.md` (selon préférence Stéphane, voir S4-02 FAQ Q6).

### Modules fictifs = démonstration framework

Les 4 modules en cours (SRH, SIEP, SAFI, BGS) sont des **démonstrateurs** du framework, pas du contenu métier réel.

**Objectif présentation** : Montrer potentiel framework pour futurs référents services (structure claire, process rodé).

### Coordination Bertrand/Alexandra

Si travail collaboratif :
- **Option A** : Séquentiel (Bertrand SIRCOM → Alexandra SNUM)
- **Option B** : Parallèle (Bertrand SIRCOM, Alexandra modules fictifs en ///)
- **Option C** : Pair programming (les 2 sur SIRCOM ensemble, apprentissage)

**Recommandation** : Option C pour Phase 1 (SIRCOM), puis autonomie Phase 2-4.

---

## Annexe - TODO S4-01 complets (16 points)

### SIRCOM (6 TODO identifiés S4-00)

| # | Point DINUM | Action S4-01 | Statut attendu |
|---|-------------|--------------|----------------|
| 5 | Temps référent | Chercher "% ETP" dans source, sinon laisser "à préciser" | `[ ]` si absent |
| 7 | Budget annuel | Chercher montant €, sinon laisser "à documenter" | `[ ]` si absent |
| 10 | Grille recrutement | Probable absent, renseigner "à documenter avec RH" | `[ ]` probable |
| 20 | Critères sélection | Chercher pondération marchés, sinon "recommandation 10-15%" | `[ ]` si absent |
| 23 | Tests utilisateurs | Chercher mention tests handicapés, sinon "à planifier 2/an" | `[ ]` si absent |
| 27 | LSF vidéo | Définir périmètre vidéos, sinon "X vidéos prioritaires" | `[ ]` si flou |
| 28 | FALC | Identifier démarches, sinon "X démarches à identifier" | `[ ]` si flou |

### SNUM (10 TODO probables S4-00)

| # | Point DINUM | Action S4-01 | Statut attendu |
|---|-------------|--------------|----------------|
| 2 | Politique inclusion | Chercher dans source courte, probable absent | `[ ]` probable |
| 5 | Temps référent | Idem SIRCOM | `[ ]` si absent |
| 7 | Budget annuel | Probable absent (doc court), renseigner "à documenter" | `[ ]` probable |
| 9 | Compétences fiches poste | Probable absent, "à documenter avec RH" | `[ ]` probable |
| 10 | Grille recrutement | Idem SIRCOM, "à documenter" | `[ ]` attendu |
| 12 | Sensibilisation large | Probable absent, "à planifier" | `[ ]` probable |
| 14 | Outils test | Chercher liste outils, sinon "à référencer" | `[ ]` si absent |
| 20 | Critères sélection | Idem SIRCOM, "recommandation 10-15%" | `[ ]` probable |
| 23 | Tests utilisateurs | Idem SIRCOM, "à planifier 2/an" | `[ ]` probable |
| 27 | LSF | Probable peu vidéos Portailpro, "périmètre à définir" | `[ ]` probable |
| 28 | FALC | Idem SIRCOM, "démarches prioritaires à identifier" | `[ ]` probable |

**Principe** : Laisser `[ ]` non coché avec justification = **TRANSPARENT** pour v1.0. Mieux qu'une fausse conformité.

---

*Dernière mise à jour : 2025-10-02*
