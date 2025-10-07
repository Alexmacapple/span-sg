---
bmad_phase: content
bmad_agent: content
story_type: feature
autonomous: false
validation: human-qa
---

# Story S6-05 : Complétion Module SIEP

**Phase** : Semaine 6 - Complétion Contenu
**Priorité** : Critique (P1 - bloquant production)
**Estimation** : 4-6h

---

## Contexte projet

**Après S6-04 (SAFI complété)** : Score 107/186 (57.5%)
- ✅ 4 modules validés : SIRCOM, SNUM, BGS, SAFI
- ❌ 2 modules vides restants : SIEP, SRH

**Score actuel** : 107/186 (57.5%)
**Score cible S6-05** : 138/186 (74.2%)

**Module SIEP** :
- Service : Service de l'Innovation et de l'Évaluation des Politiques (SIEP)
- Fichier : `docs/modules/siep.md`
- État : Template vide (31 cases non cochées)
- Référent : À définir

**Objectif S6-05** : Compléter module SIEP → 31/31 points

---

## Objectif

**Renseigner les 31 points DINUM pour le module SIEP** :
- Cocher cases applicables (minimum 20/31 pour "Conforme")
- Compléter 5 sections obligatoires
- Renseigner blocs légaux
- Ajouter plan d'actions 2025

**Livrables** :
- Module SIEP complété (`docs/modules/siep.md`)
- Front-matter mis à jour
- Score recalculé : 107/186 → 138/186 (+31 points, 74.2%)
- Synthèse régénérée

---

## Prérequis

- [x] Méthodologie éprouvée (S6-03 BGS, S6-04 SAFI)
- [x] 4 modules exemples pour référence
- [ ] Référent SIEP identifié
- [ ] Données accessibilité SIEP disponibles

---

## Étapes d'implémentation

**Structure standardisée identique S6-03/S6-04** :

### Phase 1 - Préparation (1h)
- Identifier référent SIEP (15 min)
- Préparer template pré-rempli (15 min)
- Entretien référent SIEP (30 min)

### Phase 2 - Rédaction (2h)
- Front-matter (5 min)
- Section 1 : Périmètre (20 min)
- Section 2 : État des lieux (30 min)
- Section 3 : Organisation (15 min)
- Section 4 : Plan d'action (30 min)
- Section 5 : Indicateurs (15 min)

### Phase 3 - Conformité 31 Points (45 min)
- Parcours checklist avec référent (30 min)
- Compléter blocs légaux (15 min)

### Phase 4 - Intégration (30 min)
- Recalculer scores (5 min)
- Build & Preview (10 min)
- Validation référent (15 min)

### Phase 5 - Commit & PR (30 min)
- Branche + Commit (15 min)
- Pull Request (15 min)

---

## Particularités SIEP

### Service Innovation & Évaluation
**Périmètre spécifique** :
- Plateformes innovation (lab, incubateurs)
- Outils évaluation politiques publiques
- Dashboards data/métriques
- Plateformes consultation citoyenne

**Enjeux accessibilité** :
- Public large (citoyens, chercheurs, agents)
- Données visualisées (graphiques, cartes)
- Interfaces participatives (formulaires, votes)
- Open data (accessibilité datasets)

### Points DINUM probablement conformes
- Point 1 : Référent accessibilité nommé
- Point 8 : Prise en compte accessibilité dès conception (innovation)
- Point 10 : Formation agents sensibilisation
- Point 15 : Consultation utilisateurs (évaluation)
- Point 20 : Accessibilité contenus multimédia

### Indicateurs spécifiques SIEP
- Taux accessibilité plateformes innovation
- Satisfaction utilisateurs handicapés (consultations)
- Datasets conformes WCAG (open data)
- Visualisations accessibles (alternatives textuelles)

---

## Template Commit

```bash
git commit -m "feat(siep): complète module SIEP (S6-05)

- 31 points DINUM renseignés (X/31 conformes)
- 5 sections obligatoires complétées
- Blocs légaux remplis
- Plan d'actions prioritaires 2025
- Score: 107/186 → 138/186 (+31 points, 74.2%)

Référent: [Nom Référent SIEP]
Validation: [Date validation]

Closes: roadmap/S6-05-completion-module-siep.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Template PR

```markdown
## Objectif
Compléter module SIEP pour atteindre score 138/186 (74.2%).

## Changements
- ✅ Front-matter mis à jour (référent SIEP)
- ✅ Section 1 : Périmètre (X sites/applications innovation/évaluation)
- ✅ Section 2 : État des lieux (audits, déclarations)
- ✅ Section 3 : Organisation (référent, ETP, gouvernance)
- ✅ Section 4 : Plan d'action 2025 (5+ actions prioritaires)
- ✅ Section 5 : Indicateurs (quantitatifs + qualitatifs)
- ✅ 31 points DINUM renseignés (X/31 conformes)
- ✅ Blocs légaux complétés
- ✅ Synthèse recalculée : 107/186 → 138/186

## Validation
- [x] Référent SIEP validé contenu
- [x] Build MkDocs strict OK
- [x] 31 points DINUM confirmés

## Preview
[Module SIEP draft](https://alexmacapple.github.io/span-sg-repo/draft/modules/siep/)

## Impact
**Score** : +31 points (57.5% → 74.2%)
**Progress** : 5/6 modules complétés (83%)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

---

## Critères d'acceptation

### Fonctionnels
- [ ] Module SIEP complété (31 points DINUM)
- [ ] Minimum 20/31 points cochés
- [ ] 5 sections remplies
- [ ] Blocs légaux complétés

### Techniques
- [ ] Front-matter valide
- [ ] Score : 107/186 → 138/186
- [ ] Build strict OK
- [ ] 31 lignes `<!-- DINUM -->` exactement

### Contenu
- [ ] Données réelles SIEP
- [ ] URLs valides
- [ ] Actions réalistes (T1-T4 2025)
- [ ] Indicateurs mesurables

### Validation
- [ ] Référent SIEP validé
- [ ] Revue Alexandra

---

## Risques & Solutions

### Risque 1 : Périmètre SIEP flou (innovation)
**Probabilité** : Moyenne
**Impact** : Moyen (délai collecte données)

**Solution** :
- Clarifier périmètre avec référent (10 min supplémentaires)
- Distinguer : Plateformes production vs Expérimentations
- Exclure POC/prototypes du SPAN
- Documenter exclusions explicitement

### Risque 2 : Visualisations accessibles (complexité technique)
**Probabilité** : Moyenne
**Impact** : Faible (documentation)

**Solution** :
- Documenter enjeux accessibilité data viz (Section 2)
- Ajouter action prioritaire "Audit accessibilité dashboards" (Section 4)
- Référencer guidelines accessibilité dataviz (W3C, ARIA)

### Risque 3 : Open data accessibilité (nouveauté)
**Probabilité** : Faible
**Impact** : Faible (hors périmètre strict)

**Solution** :
- Mentionner dans Section 1 (Périmètre) : datasets exclus SPAN (données brutes)
- Si interfaces data (portails) : inclure périmètre
- Clarifier distinction données/interfaces

---

## Métriques succès

**Avant S6-05** :
- Module SIEP : 0/31 (0.0%)
- Score global : 107/186 (57.5%)
- Modules validés : 4/6

**Après S6-05** :
- Module SIEP : X/31 (XX.X%, cible ≥20/31)
- Score global : 138/186 (74.2%)
- Modules validés : 5/6

**Impact scoring** : 94/100 → 100/100 (+6 points Modules, progress 67% → 83%)

---

## Dépendances

**Bloquants** :
- Référent SIEP identifié
- Données accessibilité SIEP

**Facilitateurs** :
- S6-03, S6-04 : Méthodologie éprouvée (3ème itération)
- Template pré-rempli standardisé

**Bloque** :
- S6-06 (SRH) : Dernier module, calcul score 100%

---

## Notes d'implémentation

### Gains productivité cumulés
**3ème itération méthodologie** :
- Template pré-rempli : -30 min (standardisé)
- Structure sections maîtrisée : -20 min (copier-coller adapté)
- Entretien optimisé : -10 min (questions ciblées)
- **Total gain** : -1h vs S6-03 BGS (estimation 3-5h au lieu de 4-6h)

### Checklist référent pré-entretien
**Envoyer 48h avant (SIEP spécifique)** :
```markdown
# PRÉPARATION ENTRETIEN MODULE SIEP

Merci de remplir ce document avant notre entretien (30 min).

## 1. Périmètre Innovation & Évaluation
- [ ] Plateformes innovation gérées par SIEP (URLs + utilisateurs)
- [ ] Outils évaluation politiques publiques (noms + types)
- [ ] Dashboards/visualisations data (URLs accessibles)
- [ ] Plateformes consultation citoyenne (si applicable)
- [ ] Exclusions périmètre (POC, prototypes, datasets bruts)

## 2. État des lieux
- [ ] Audits accessibilité réalisés (dates + rapports)
- [ ] Déclarations publiées (URLs)
- [ ] Taux conformité estimé (%)
- [ ] Enjeux spécifiques dataviz accessibles

## 3. Organisation
- [ ] Référent accessibilité SIEP (nom + fonction)
- [ ] ETP dédiés (nombre)
- [ ] Budget annuel (k€)

## 4. Plan d'action 2025
- [ ] 5 actions prioritaires (dont accessibilité dashboards/dataviz)
- [ ] Jalons T1-T4 2025
- [ ] Budget prévisionnel

## 5. Indicateurs
- [ ] Indicateurs actuels
- [ ] Valeurs actuelles
- [ ] Cibles 2025/2026
- [ ] Satisfaction utilisateurs handicapés (consultations)
```

### Parallélisation S6-05 + S6-06
Si 2 contributeurs disponibles :
- S6-05 (SIEP) + S6-06 (SRH) simultanés
- Gain : 2 jours → 1 jour
- Merge séquentiel (éviter conflits synthese.md)
