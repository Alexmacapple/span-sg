---
bmad_phase: content
bmad_agent: content
story_type: feature
autonomous: false
validation: human-qa
---

# Story S6-06 : Complétion Module SRH (Dernier Module)

**Phase** : Semaine 6 - Complétion Contenu
**Priorité** : Critique (P1 - bloquant production, DERNIER MODULE)
**Estimation** : 4-6h

---

## Contexte projet

**Après S6-05 (SIEP complété)** : Score 138/186 (74.2%)
- ✅ 5 modules validés : SIRCOM, SNUM, BGS, SAFI, SIEP
- ❌ **1 dernier module vide : SRH**

**Score actuel** : 138/186 (74.2%)
**Score cible S6-06** : **169/186 (90.9%)** ✅ **SCORE PRODUCTION**

**Module SRH** :
- Service : Service des Ressources Humaines (SRH)
- Fichier : `docs/modules/srh.md`
- État : Template vide (31 cases non cochées)
- Référent : À définir

**Objectif S6-06** : Compléter SRH → **169/186 (90.9%)** → **Conformité globale atteinte**

---

## Objectif

**Compléter le dernier module SRH** → Atteindre seuil production (90%+) :
- Cocher cases applicables (minimum 20/31 pour "Conforme")
- Compléter 5 sections obligatoires
- Renseigner blocs légaux
- Ajouter plan d'actions 2025

**Livrables** :
- Module SRH complété (`docs/modules/srh.md`)
- Score recalculé : **138/186 → 169/186 (+31 points, 90.9%)**
- **🎉 Conformité globale atteinte (objectif >80%)**
- Synthèse finale régénérée

---

## Prérequis

- [x] Méthodologie éprouvée (4ème itération)
- [x] 5 modules exemples pour référence
- [ ] Référent SRH identifié
- [ ] Données accessibilité SRH disponibles

---

## Étapes d'implémentation

**Structure standardisée identique S6-03/04/05** :

### Phase 1 - Préparation (1h)
- Identifier référent SRH (15 min)
- Préparer template pré-rempli (15 min)
- Entretien référent SRH (30 min)

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

## Particularités SRH

### Service Ressources Humaines
**Périmètre spécifique** :
- SIRH (Système Information RH)
- Portail agents (congés, paie, carrière)
- Recrutement (candidatures, concours)
- Formation (catalogue, inscriptions)
- Intranets RH

**Enjeux accessibilité** :
- Public : Tous agents SG (diversité handicaps)
- Applications métier critiques (paie, congés)
- Conformité légale stricte (égalité accès services RH)
- Volumes : Centaines/milliers d'agents

### Points DINUM probablement conformes
- Point 1 : Référent accessibilité nommé
- Point 3 : Ressources budget/humaines dédiées (RH = service support)
- Point 9 : Accompagnement agents handicapés (mission RH)
- Point 10 : Formation agents sensibilisation
- Point 12 : Tests utilisateurs handicapés (agents)
- Point 27 : Veille accessibilité (RH = conformité légale)

### Indicateurs spécifiques SRH
- Taux accessibilité SIRH/portail agents
- Satisfaction agents handicapés (enquête annuelle)
- Temps moyen traitement demandes accessibilité
- Agents formés accessibilité numérique (%)
- Demandes aménagements poste (accessibilité)

---

## Template Commit

```bash
git commit -m "feat(srh): complète module SRH - 100% modules (S6-06)

🎉 DERNIER MODULE COMPLÉTÉ - CONFORMITÉ GLOBALE ATTEINTE

- 31 points DINUM renseignés (X/31 conformes)
- 5 sections obligatoires complétées
- Blocs légaux remplis
- Plan d'actions prioritaires 2025
- Score: 138/186 → 169/186 (+31 points, 90.9%)

📊 6/6 modules complétés (100%)
✅ Seuil production atteint (>80% conformité)

Référent: [Nom Référent SRH]
Validation: [Date validation]

Closes: roadmap/S6-06-completion-module-srh.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## Template PR

```markdown
## 🎉 Objectif : DERNIER MODULE - CONFORMITÉ GLOBALE ATTEINTE

Compléter module SRH pour atteindre **169/186 (90.9%)** → **Seuil production**.

## Changements
- ✅ Front-matter mis à jour (référent SRH)
- ✅ Section 1 : Périmètre (SIRH, portail agents, recrutement, formation)
- ✅ Section 2 : État des lieux (audits, déclarations)
- ✅ Section 3 : Organisation (référent, ETP, gouvernance)
- ✅ Section 4 : Plan d'action 2025 (5+ actions prioritaires)
- ✅ Section 5 : Indicateurs (quantitatifs + qualitatifs)
- ✅ 31 points DINUM renseignés (X/31 conformes)
- ✅ Blocs légaux complétés
- ✅ Synthèse recalculée : **138/186 → 169/186**

## Validation
- [x] Référent SRH validé contenu
- [x] Build MkDocs strict OK
- [x] 31 points DINUM confirmés
- [x] Tous modules complétés (6/6)

## Preview
[Module SRH draft](https://alexmacapple.github.io/span-sg-repo/draft/modules/srh/)

## Impact 🚀
**Score** : +31 points (74.2% → **90.9%**)
**Progress** : **6/6 modules complétés (100%)**
**Statut** : ✅ **CONFORMITÉ GLOBALE ATTEINTE** (>80%)

## Next Steps
- [ ] Revue finale Alexandra
- [ ] Présentation Stéphane (validation concept)
- [ ] Merge draft → main
- [ ] Tag v1.0.0 (production)
- [ ] Publication GitHub Pages

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

---

## Critères d'acceptation

### Fonctionnels
- [ ] Module SRH complété (31 points DINUM)
- [ ] Minimum 20/31 points cochés
- [ ] 5 sections remplies
- [ ] Blocs légaux complétés

### Techniques
- [ ] Front-matter valide
- [ ] Score : **138/186 → 169/186 (90.9%)**
- [ ] Build strict OK
- [ ] 31 lignes `<!-- DINUM -->` exactement

### Contenu
- [ ] Données réelles SRH
- [ ] URLs valides
- [ ] Actions réalistes (T1-T4 2025)
- [ ] Indicateurs mesurables

### Validation
- [ ] Référent SRH validé
- [ ] Revue Alexandra
- [ ] **6/6 modules complétés**

### Milestone 🎉
- [ ] **Conformité globale atteinte (90.9% > 80%)**
- [ ] Seuil production validé
- [ ] Prêt présentation Stéphane

---

## Risques & Solutions

### Risque 1 : Pression "dernier module" (précipitation)
**Probabilité** : Moyenne
**Impact** : Moyen (qualité contenu)

**Solution** :
- Maintenir même rigueur que S6-03/04/05
- Checklist validation stricte
- Relecture Alexandra obligatoire
- Accepter délai supplémentaire si nécessaire (qualité > vitesse)

### Risque 2 : SIRH legacy (accessibilité difficile)
**Probabilité** : Moyenne
**Impact** : Moyen (score SRH <20/31)

**Solution** :
- Documenter honnêtement état accessibilité SIRH
- Dérogations justifiées si applicable (charge disproportionnée)
- Plan d'action ambitieux 2025-2026 (refonte/mise conformité)
- Alternatives compensatoires (assistance humaine)

### Risque 3 : Données RH sensibles (confidentialité)
**Probabilité** : Faible
**Impact** : Faible (anonymisation)

**Solution** :
- Anonymiser données agents (pas de noms/prénoms)
- Indicateurs agrégés uniquement (%, moyennes)
- Valider avec référent SRH sections publiques vs internes
- Exclure données nominatives schéma SPAN

---

## Métriques succès

**Avant S6-06** :
- Module SRH : 0/31 (0.0%)
- Score global : 138/186 (74.2%)
- Modules validés : 5/6

**Après S6-06** :
- Module SRH : X/31 (XX.X%, cible ≥20/31)
- Score global : **169/186 (90.9%)**
- Modules validés : **6/6 (100%)**

**Impact scoring** : 94/100 → **100/100** (+6 points Modules)

---

## Dépendances

**Bloquants** :
- Référent SRH identifié
- Données accessibilité SRH

**Facilitateurs** :
- S6-03/04/05 : Méthodologie parfaitement maîtrisée (4ème itération)
- Template standardisé
- Motivation "dernier module" (milestone symbolique)

**Bloque** :
- Tag v1.0.0 production
- Présentation Stéphane (validation concept)
- Publication main (conformité totale)

---

## Notes d'implémentation

### Célébration milestone 🎉
**Actions post-S6-06** :
1. Annoncer dans Slack `#span-sg-ci` : "🎉 6/6 modules complétés - 90.9% conformité"
2. Mettre à jour README.md : Badge "Coverage 90.9%" vert
3. Préparer CHANGELOG.md : Section v1.0.0 (6 modules complétés)
4. Screenshot synthèse 169/186 (artefact milestone)

### Checklist référent pré-entretien (SRH spécifique)
```markdown
# PRÉPARATION ENTRETIEN MODULE SRH

## 1. Périmètre RH
- [ ] SIRH principal (nom + URL/intranet + utilisateurs)
- [ ] Portail agents (congés, paie, carrière)
- [ ] Plateforme recrutement (candidatures externes)
- [ ] Catalogue formation + inscriptions
- [ ] Intranets RH (actualités, docs)
- [ ] Exclusions périmètre (outils admin, back-office)

## 2. État des lieux
- [ ] Audits accessibilité SIRH/portail (dates + rapports)
- [ ] Déclarations publiées (URLs, si applicables intranets)
- [ ] Taux conformité estimé (%)
- [ ] Remontées agents handicapés (nombre/an, types)

## 3. Organisation
- [ ] Référent accessibilité SRH (nom + fonction)
- [ ] ETP dédiés accessibilité (nombre)
- [ ] Budget annuel (k€)
- [ ] Mission handicap SG (coordination)

## 4. Plan d'action 2025
- [ ] 5 actions prioritaires (dont SIRH accessible, formation agents)
- [ ] Jalons T1-T4 2025
- [ ] Budget prévisionnel
- [ ] Aménagements postes agents handicapés (si lié accessibilité numérique)

## 5. Indicateurs
- [ ] Satisfaction agents handicapés (enquête annuelle %)
- [ ] Temps traitement demandes accessibilité (jours)
- [ ] Agents formés accessibilité numérique (nombre)
- [ ] Cibles 2025/2026
```

### Post-complétion SRH
**Prochaines étapes projet** :
1. **S6-07** : Renforcement Sécurité (Dependabot, BFG)
2. **S6-08** : Documentation Maintenabilité (CHANGELOG, Migration)
3. **S6-01** : Tests E2E CI (si priorisé)
4. **S6-02** : Notifications CI (si priorisé)
5. **Tag v1.0.0** : Release production
6. **Présentation Stéphane** : Validation concept GO production

### Variabilité score final
**Score 169/186 (90.9%) = hypothèse 20/31 par module minimum**

**Scénarios réalistes** :
- **Optimiste** : 25/31 moyens → 175/186 (94.1%)
- **Réaliste** : 22/31 moyens → 172/186 (92.5%)
- **Pessimiste** : 18/31 moyens → 163/186 (87.6%)

**Seuil production** : >80% (149/186) → Largement atteint même scénario pessimiste

### Optimisation parallèle (si applicable)
**Si S6-06 bloqué (référent SRH indisponible)** :
- Décaler S6-06 après S6-07/S6-08 (technique)
- Travailler modules techniques en attendant
- Publier v0.9.0 (5/6 modules) si deadline urgente
- Compléter SRH en v1.1.0 (patch)
