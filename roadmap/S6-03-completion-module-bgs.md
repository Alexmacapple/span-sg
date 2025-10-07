---
bmad_phase: content
bmad_agent: content
story_type: feature
autonomous: false
validation: human-qa
---

# Story S6-03 : Complétion Module BGS

**Phase** : Semaine 6 - Complétion Contenu
**Priorité** : Critique (P1 - bloquant production)
**Estimation** : 4-6h

---

## Contexte projet

**Après POC v1.0.0** : Score qualité 94/100
- ✅ Framework production-ready (scoring, CI/CD, docs)
- ✅ 2 modules validés : SIRCOM (24/31), SNUM (21/31)
- ❌ 4 modules vides : BGS, SAFI, SIEP, SRH (0/31 chacun)

**Score actuel** : 45/186 (24.2%)
**Score cible** : 186/186 (100%)

**Module BGS** :
- Service : Bureau de la Gestion et de la Stratégie (BGS)
- Fichier : `docs/modules/bgs.md`
- État : Template vide (31 cases non cochées)
- Référent : À définir

**Objectif S6-03** : Compléter module BGS → 31/31 points

---

## Objectif

**Renseigner les 31 points DINUM pour le module BGS** :
- Cocher cases applicables (minimum 20/31 pour "Conforme")
- Compléter 5 sections obligatoires
- Renseigner blocs légaux (déclaration accessibilité)
- Ajouter plan d'actions prioritaires 2025

**Livrables** :
- Module BGS complété (`docs/modules/bgs.md`)
- Front-matter mis à jour (referent, updated)
- Score recalculé : 45/186 → 76/186 (+31 points, 40.9%)
- Synthèse régénérée

---

## Prérequis

- [x] Template _template.md disponible
- [x] 2 modules exemples (SIRCOM, SNUM) pour référence
- [ ] Référent BGS identifié
- [ ] Données accessibilité BGS disponibles

---

## Étapes d'implémentation

### Phase 1 - Préparation & Audit (1h)

#### Microtâches

**1.1 Identifier référent BGS** (15 min)

**Sources** :
- Organigramme SG
- Contact Alexandra (owner projet)
- Équipe BGS

**Checklist** :
- [ ] Référent BGS identifié (nom + email)
- [ ] Validation référent obtenue
- [ ] Contact établi pour collecte données

**1.2 Collecter données accessibilité BGS** (30 min)

**Informations requises** :
```markdown
1. Périmètre
   - Sites web gérés par BGS
   - Applications métier BGS
   - Outils internes BGS

2. État des lieux
   - Audits accessibilité existants
   - Déclarations accessibilité publiées
   - Taux conformité actuel (estimation)

3. Organisation
   - Référent accessibilité BGS
   - Ressources dédiées (ETP)
   - Budget accessibilité

4. Plan d'action
   - Actions prioritaires 2025
   - Échéances clés
   - Indicateurs suivi

5. Conformité 31 points DINUM
   - Points déjà conformes (liste)
   - Points en cours (liste)
   - Points non applicables (liste)
```

**Sources** :
- Documentation interne BGS
- Audits accessibilité précédents
- Entretien référent BGS (30-45 min)

**Checklist** :
- [ ] Sites/applications BGS listés
- [ ] Audits accessibilité récupérés
- [ ] Référent accessibilité BGS identifié
- [ ] Actions prioritaires définies

**1.3 Analyser modules SIRCOM/SNUM (référence)** (15 min)

```bash
# Comparer structure modules validés
diff docs/modules/sircom.md docs/modules/snum.md

# Identifier patterns communs
grep -A 5 "## 1. Périmètre" docs/modules/sircom.md
grep -A 5 "## 1. Périmètre" docs/modules/snum.md
```

**Checklist** :
- [ ] Structure sections comprise
- [ ] Niveau détail attendu identifié
- [ ] Exemples actions prioritaires notés
- [ ] Format déclaration accessibilité compris

---

### Phase 2 - Rédaction Contenu (2-3h)

#### Microtâches

**2.1 Compléter front-matter** (10 min)

```yaml
---
service: BGS
referent: [Nom Référent]
email: [email@sg.gouv.fr]
updated: 2025-10-07
validation_status: in_progress
---
```

**Checklist** :
- [ ] Service : BGS
- [ ] Référent renseigné
- [ ] Email référent
- [ ] Date updated (aujourd'hui)
- [ ] Status : in_progress

**2.2 Rédiger Section 1 - Périmètre** (20 min)

**Structure** :
```markdown
## 1. Périmètre d'application

### Sites et applications concernés

| Nom | URL | Type | Utilisateurs |
|-----|-----|------|--------------|
| [Site BGS 1] | https://... | Site institutionnel | Grand public |
| [App BGS 2] | Intranet | Application métier | Agents SG |
| [Outil BGS 3] | https://... | Outil interne | Équipe BGS |

**Total** : [X] sites/applications recensés.

### Outils de gestion exclus du périmètre SPAN

[Liste outils internes exclus, ex: outils dev, admin système]

### Volumétrie

- **Sites publics** : [X]
- **Applications métier** : [Y]
- **Utilisateurs** : ~[Z] agents
```

**Checklist** :
- [ ] Tableau sites/applications complété
- [ ] URLs accessibles vérifiées
- [ ] Volumétrie renseignée
- [ ] Exclusions périmètre justifiées

**2.3 Rédiger Section 2 - État des lieux** (30 min)

**Structure** :
```markdown
## 2. État des lieux accessibilité

### Audits réalisés

| Site/Application | Date audit | Taux conformité | Rapport |
|------------------|------------|-----------------|---------|
| [Site BGS 1] | 2024-XX-XX | XX% | [Lien rapport] |
| [App BGS 2] | 2024-XX-XX | XX% | [Lien rapport] |

### Déclarations d'accessibilité

- ✅ **[Site BGS 1]** : [URL déclaration]
- ⏳ **[App BGS 2]** : En cours de rédaction
- ❌ **[Outil BGS 3]** : Non publiée

### Synthèse conformité

**Niveau moyen** : [XX/100] (estimation)

**Points forts** :
- [Point fort 1]
- [Point fort 2]

**Axes d'amélioration** :
- [Axe 1]
- [Axe 2]
```

**Checklist** :
- [ ] Audits listés avec dates
- [ ] Déclarations accessibilité recensées
- [ ] Synthèse conformité rédigée
- [ ] Points forts/axes identifiés

**2.4 Rédiger Section 3 - Organisation** (20 min)

**Structure** :
```markdown
## 3. Organisation et ressources

### Référent accessibilité

**Nom** : [Nom Prénom]
**Fonction** : [Titre poste]
**Email** : [email@sg.gouv.fr]
**Depuis** : [Date prise fonction]

### Équipe dédiée

- **ETP accessibilité** : [X] ETP
- **Formation** : [X] agents formés RGAA
- **Budget annuel** : [X]k€ (estimation)

### Gouvernance

- **COPIL accessibilité** : Trimestriel
- **Reporting** : Chef de service BGS
- **Décisions** : [Instance décision]
```

**Checklist** :
- [ ] Référent accessibilité nommé
- [ ] ETP dédiés renseignés
- [ ] Budget estimé
- [ ] Gouvernance décrite

**2.5 Rédiger Section 4 - Plan d'action** (30 min)

**Structure** :
```markdown
## 4. Plan d'action 2025

### Actions prioritaires

| Action | Responsable | Échéance | Statut | Priorité |
|--------|-------------|----------|--------|----------|
| Audit RGAA Site BGS 1 | [Nom] | T1 2025 | En cours | Haute |
| Mise conformité App BGS 2 | [Nom] | T2 2025 | Planifié | Haute |
| Formation équipe RGAA | [Nom] | T1 2025 | En cours | Moyenne |
| Publication déclarations | [Nom] | T3 2025 | Planifié | Haute |
| Corrections défauts critiques | [Nom] | T4 2025 | Planifié | Haute |

### Jalons clés

- **T1 2025** : Audits sites prioritaires
- **T2 2025** : Corrections défauts critiques
- **T3 2025** : Publication déclarations
- **T4 2025** : Audit conformité global

### Budget prévisionnel

- **Audits** : [X]k€
- **Corrections** : [Y]k€
- **Formation** : [Z]k€
- **Total** : [X+Y+Z]k€
```

**Checklist** :
- [ ] 5+ actions prioritaires listées
- [ ] Responsables assignés
- [ ] Échéances réalistes (trimestres)
- [ ] Jalons clés définis
- [ ] Budget estimé

**2.6 Rédiger Section 5 - Indicateurs** (20 min)

**Structure** :
```markdown
## 5. Indicateurs de suivi

### Indicateurs quantitatifs

| Indicateur | Valeur actuelle | Cible 2025 | Cible 2026 |
|------------|-----------------|------------|------------|
| Taux conformité RGAA moyen | XX% | XX% | 90%+ |
| Sites avec déclaration publiée | X/Y | Y/Y | Y/Y |
| Agents formés RGAA | X | XX | XX |
| Défauts critiques résolus | XX% | 80% | 100% |

### Indicateurs qualitatifs

- **Satisfaction utilisateurs** : Enquête annuelle
- **Retours accessibilité** : [X] signalements/an
- **Conformité légale** : 100% sites déclarés

### Reporting

- **Fréquence** : Trimestriel
- **Format** : Tableau de bord (dashboard interne)
- **Diffusion** : COPIL accessibilité + Chef BGS
```

**Checklist** :
- [ ] 4+ indicateurs quantitatifs
- [ ] Valeurs actuelles renseignées
- [ ] Cibles 2025/2026 définies
- [ ] Indicateurs qualitatifs ajoutés
- [ ] Reporting décrit

---

### Phase 3 - Conformité 31 Points DINUM (1h)

#### Microtâches

**3.1 Cocher points conformes** (30 min)

**Méthode** :
1. Lire chaque point DINUM (`<!-- DINUM -->`)
2. Vérifier conformité BGS (données collectées Phase 1)
3. Cocher `[x]` si conforme, laisser `[ ]` sinon

**Points typiquement conformes (à valider)** :
- Point 1 : Référent accessibilité nommé
- Point 2 : Engagement direction formalisé
- Point 4 : Schéma pluriannuel publié
- Point 13 : Déclarations accessibilité publiées (si applicable)

**Attention** :
- ❌ Ne PAS ajouter/supprimer lignes `<!-- DINUM -->`
- ✅ Seulement modifier `[ ]` → `[x]`
- ⚠️ Total doit rester 31 points exactement

**Checklist** :
- [ ] 31 points DINUM parcourus
- [ ] Minimum 20/31 cochés (cible "Conforme")
- [ ] Validation référent BGS obtenue
- [ ] Total confirmé : 31 lignes `<!-- DINUM -->`

**3.2 Compléter blocs légaux** (15 min)

```markdown
## 6. Conformité légale

### Déclaration d'accessibilité

**Sites avec déclaration publiée** :
- ✅ [Site BGS 1] : [URL déclaration]
- ⏳ [App BGS 2] : Publication T1 2025

**Sites sans déclaration** :
- [Outil BGS 3] : Hors périmètre légal (outil interne)

### Dérogations pour charge disproportionnée

[Si applicable]
- **[Site/App]** : Charge disproportionnée justifiée
  - **Motif** : [Justification technique/financière]
  - **Alternative** : [Solution compensatoire proposée]

[Sinon]
Aucune dérogation invoquée. Mise en conformité totale visée d'ici 2026.

### Schéma pluriannuel

Ce document constitue le schéma pluriannuel BGS 2025-2027, conformément à l'article 47 de la loi du 11 février 2005.

**Validation** : [Date validation chef BGS]
**Publication** : [URL si publié]
```

**Checklist** :
- [ ] URLs déclarations accessibilité renseignées
- [ ] Dérogations justifiées (si applicables)
- [ ] Schéma pluriannuel mentionné
- [ ] Date validation ajoutée

**3.3 Valider avec référent BGS** (15 min)

**Revue** :
- Envoyer draft module BGS au référent
- Réunion validation (15-30 min)
- Corrections mineures si nécessaires

**Checklist** :
- [ ] Draft envoyé référent BGS
- [ ] Réunion validation tenue
- [ ] Corrections appliquées
- [ ] Validation référent obtenue (email)

---

### Phase 4 - Intégration & Tests (30 min)

#### Microtâches

**4.1 Mettre à jour fichier module** (10 min)

```bash
# Éditer module BGS
vim docs/modules/bgs.md
# OU
code docs/modules/bgs.md

# Copier contenu rédigé Phases 2-3
# Sauvegarder
```

**Checklist** :
- [ ] Contenu collé dans docs/modules/bgs.md
- [ ] Front-matter complet
- [ ] 5 sections remplies
- [ ] 31 points DINUM présents (dont X cochés)

**4.2 Recalculer scores** (5 min)

```bash
# Exécuter script scoring
python3 scripts/calculate_scores.py

# Vérifier sortie
# Attendu: "BGS: X/31 (XX.X%)"
# Erreur si ≠ 31 points total
```

**Checklist** :
- [ ] Script calculate_scores.py exécuté sans erreur
- [ ] Score BGS affiché (X/31)
- [ ] Synthèse docs/synthese.md régénérée
- [ ] Score global : 76/186 (40.9%)

**4.3 Tester build MkDocs** (10 min)

```bash
# Build strict (détecte liens cassés)
mkdocs build --strict

# Preview local
docker compose up
# Ouvrir http://localhost:8000/span-sg-repo/modules/bgs/

# Vérifications visuelles
# - Module BGS apparaît dans nav
# - Contenu bien formaté
# - Tableaux rendus correctement
# - Liens fonctionnels
```

**Checklist** :
- [ ] Build MkDocs réussi (--strict)
- [ ] Preview local OK
- [ ] Module BGS visible navigation
- [ ] Formatage markdown correct
- [ ] Pas de liens cassés

**4.4 Valider avec tests E2E** (5 min)

```bash
# Exécuter tests E2E (si S6-01 implémenté)
./tests/e2e/scenario_multi_modules.sh

# OU test manuel
grep -c "<!-- DINUM -->" docs/modules/bgs.md
# Attendu: 31
```

**Checklist** :
- [ ] 31 points DINUM confirmés (grep)
- [ ] Tests E2E passent (si disponibles)
- [ ] Pas d'erreur validation périmètre

---

### Phase 5 - Commit & PR (30 min)

#### Microtâches

**5.1 Créer branche feature** (5 min)

```bash
git checkout draft
git pull origin draft
git checkout -b feature/s6-03-completion-bgs
```

**5.2 Committer changements** (10 min)

```bash
git add docs/modules/bgs.md docs/synthese.md
git commit -m "feat(bgs): complète module BGS (S6-03)

- 31 points DINUM renseignés (X/31 conformes)
- 5 sections obligatoires complétées
- Blocs légaux remplis
- Plan d'actions prioritaires 2025
- Score: 45/186 → 76/186 (+31 points, 40.9%)

Référent: [Nom Référent BGS]
Validation: [Date validation]

Closes: roadmap/S6-03-completion-module-bgs.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push -u origin feature/s6-03-completion-bgs
```

**Checklist** :
- [ ] Commit message détaillé
- [ ] Score avant/après indiqué
- [ ] Référent mentionné
- [ ] Roadmap closée

**5.3 Créer Pull Request** (15 min)

```bash
gh pr create --base draft \
  --title "feat(bgs): Complétion Module BGS 31/31 (S6-03)" \
  --body "## Objectif
Compléter module BGS pour atteindre score 76/186 (40.9%).

## Changements
- ✅ Front-matter mis à jour (référent BGS)
- ✅ Section 1 : Périmètre (X sites/applications)
- ✅ Section 2 : État des lieux (audits, déclarations)
- ✅ Section 3 : Organisation (référent, ETP, gouvernance)
- ✅ Section 4 : Plan d'action 2025 (5+ actions prioritaires)
- ✅ Section 5 : Indicateurs (quantitatifs + qualitatifs)
- ✅ 31 points DINUM renseignés (X/31 conformes)
- ✅ Blocs légaux complétés
- ✅ Synthèse recalculée : 45/186 → 76/186

## Validation
- [x] Référent BGS validé contenu
- [x] Build MkDocs strict OK
- [x] Tests E2E passent
- [x] 31 points DINUM confirmés (grep)

## Preview
[Module BGS draft](https://alexmacapple.github.io/span-sg-repo/draft/modules/bgs/)

## Impact
**Score** : +31 points (24.2% → 40.9%)
**État** : BGS validé [ou En cours si < 20/31]

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

**Checklist PR** :
- [ ] PR créée vers `draft`
- [ ] Description complète
- [ ] Lien preview draft
- [ ] CI passe (build + tests)
- [ ] Revue Alexandra/Bertrand

---

## Critères d'acceptation

### Fonctionnels
- [ ] Module BGS complété (31 points DINUM présents)
- [ ] Minimum 20/31 points cochés (statut "Conforme")
- [ ] 5 sections obligatoires remplies
- [ ] Blocs légaux complétés (déclarations, dérogations)
- [ ] Plan d'actions 2025 avec 5+ actions

### Techniques
- [ ] Front-matter valide (service, referent, email, updated)
- [ ] Score recalculé : 45/186 → 76/186 (+31 points)
- [ ] Build MkDocs strict OK
- [ ] Pas de liens cassés
- [ ] 31 lignes `<!-- DINUM -->` exactement (validation périmètre)

### Contenu
- [ ] Données réelles BGS (pas de placeholder)
- [ ] URLs déclarations accessibilité valides
- [ ] Actions prioritaires réalistes (échéances T1-T4 2025)
- [ ] Indicateurs mesurables (valeurs actuelles + cibles)

### Validation
- [ ] Référent BGS identifié et validé contenu
- [ ] Revue Alexandra (owner projet)
- [ ] Preview draft accessible

---

## Risques & Solutions

### Risque 1 : Données accessibilité BGS indisponibles
**Probabilité** : Moyenne
**Impact** : Critique (bloque complétion)

**Solution** :
- Contacter référent BGS en amont (Phase 1)
- Si données partielles : remplir avec estimations + TODO explicites
- Marquer module "En cours" (< 20/31) si incomplet
- Planifier complétion différée (S7)

### Risque 2 : Référent BGS non identifié
**Probabilité** : Faible
**Impact** : Moyen (validation différée)

**Solution** :
- Demander à Alexandra (owner projet)
- Consulter organigramme SG
- Fallback : Alexandra référente provisoire
- Mettre à jour référent ultérieurement

### Risque 3 : Désaccord contenu avec référent BGS
**Probabilité** : Faible
**Impact** : Faible (itération)

**Solution** :
- Réunion validation (Phase 3.3)
- Corrections mineures en direct
- Si désaccord majeur : marquer module "Draft", itération S7

---

## Métriques succès

**Avant S6-03** :
- Module BGS : 0/31 (0.0%)
- Score global : 45/186 (24.2%)
- Modules validés : 2/6

**Après S6-03** :
- Module BGS : X/31 (XX.X%, cible ≥20/31 pour "Conforme")
- Score global : 76/186 (40.9%)
- Modules validés : 3/6

**Impact scoring** : 94/100 → 96/100 (+2 points Modules, progress 33% → 50%)

---

## Dépendances

**Bloquants** :
- Référent BGS identifié
- Données accessibilité BGS disponibles

**Facilitateurs** :
- Template _template.md
- Modules SIRCOM/SNUM (exemples)
- Script calculate_scores.py

**Bloque** :
- S6-07 (Sécurité) : Purge inspiration/ peut nécessiter référents tous modules

---

## Notes d'implémentation

### Niveau détail attendu
**Inspiration modules SIRCOM/SNUM** :
- Sections 1-3 : 100-200 mots/section (synthétique)
- Section 4 : Tableau 5-8 actions (détaillé)
- Section 5 : Tableau 4-6 indicateurs (chiffré)
- Blocs légaux : URLs + dates (factuel)

**Ne PAS faire** :
- Roman-fleuve (> 500 mots/section)
- Placeholder génériques ("À compléter", "TBD")
- Informations sensibles (budgets détaillés, noms agents)

### Collecte données efficace
**Entretien référent BGS (30-45 min)** :
1. Périmètre (10 min) : Sites/apps + volumétrie
2. État des lieux (10 min) : Audits + déclarations
3. Organisation (5 min) : Référent + ETP
4. Plan d'action (10 min) : Actions 2025 + jalons
5. Indicateurs (5 min) : Valeurs actuelles + cibles
6. Validation 31 points (10 min) : Parcours checklist

**Document pré-rempli** : Envoyer template avec sections à référent 24h avant (gain temps).
