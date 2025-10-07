---
bmad_phase: content
bmad_agent: content
story_type: feature
autonomous: false
validation: human-qa
---

# Story S6-04 : Complétion Module SAFI

**Phase** : Semaine 6 - Complétion Contenu
**Priorité** : Critique (P1 - bloquant production)
**Estimation** : 4-6h

---

## Contexte projet

**Après S6-03 (BGS complété)** : Score 76/186 (40.9%)
- ✅ 3 modules validés : SIRCOM, SNUM, BGS
- ❌ 3 modules vides restants : SAFI, SIEP, SRH

**Score actuel** : 76/186 (40.9%)
**Score cible S6-04** : 107/186 (57.5%)

**Module SAFI** :
- Service : Service des Affaires Financières et Immobilières (SAFI)
- Fichier : `docs/modules/safi.md`
- État : Template vide (31 cases non cochées)
- Référent : À définir

**Objectif S6-04** : Compléter module SAFI → 31/31 points

---

## Objectif

**Renseigner les 31 points DINUM pour le module SAFI** :
- Cocher cases applicables (minimum 20/31 pour "Conforme")
- Compléter 5 sections obligatoires
- Renseigner blocs légaux (déclaration accessibilité)
- Ajouter plan d'actions prioritaires 2025

**Livrables** :
- Module SAFI complété (`docs/modules/safi.md`)
- Front-matter mis à jour (referent, updated)
- Score recalculé : 76/186 → 107/186 (+31 points, 57.5%)
- Synthèse régénérée

---

## Prérequis

- [x] Template _template.md disponible
- [x] 3 modules exemples (SIRCOM, SNUM, BGS) pour référence
- [x] Méthodologie S6-03 éprouvée
- [ ] Référent SAFI identifié
- [ ] Données accessibilité SAFI disponibles

---

## Étapes d'implémentation

### Phase 1 - Préparation & Collecte Données (1h)

#### Microtâches

**1.1 Identifier référent SAFI** (15 min)

**Méthode** :
- Contact Alexandra (owner projet)
- Organigramme SG → Service SAFI
- Email chef de service SAFI

**Checklist** :
- [ ] Référent SAFI identifié (nom + email)
- [ ] Validation référent obtenue
- [ ] Rendez-vous collecte données planifié (30-45 min)

**1.2 Préparer template pré-rempli** (15 min)

**Stratégie gain temps** :
Envoyer template avec structure 24h avant entretien

```bash
# Copier template vers draft SAFI
cp docs/modules/_template.md /tmp/draft-safi.md

# Ajouter questions guidées
cat >> /tmp/draft-safi.md <<'EOF'

# QUESTIONS PRÉPARATION ENTRETIEN (à remplir avant)

## 1. Périmètre
- [ ] Quels sites web gère le SAFI ? (URLs)
- [ ] Quelles applications métier ? (noms + utilisateurs)
- [ ] Outils internes exclus du périmètre ?

## 2. État des lieux
- [ ] Audits accessibilité réalisés ? (dates + rapports)
- [ ] Déclarations accessibilité publiées ? (URLs)
- [ ] Taux conformité estimé ? (%)

## 3. Organisation
- [ ] Référent accessibilité SAFI ? (nom + fonction)
- [ ] ETP dédiés accessibilité ? (nombre)
- [ ] Budget annuel accessibilité ? (estimation k€)

## 4. Plan d'action 2025
- [ ] 5 actions prioritaires ? (description + échéances)
- [ ] Jalons clés T1-T4 2025 ?
- [ ] Budget prévisionnel 2025 ? (k€)

## 5. Indicateurs
- [ ] Indicateurs actuels suivis ? (lesquels)
- [ ] Valeurs actuelles ? (chiffres)
- [ ] Cibles 2025/2026 ? (objectifs)
EOF

# Envoyer à référent SAFI
echo "Template envoyé : /tmp/draft-safi.md"
```

**Checklist** :
- [ ] Template pré-rempli créé
- [ ] Questions guidées ajoutées
- [ ] Envoyé à référent SAFI 24h avant entretien

**1.3 Entretien référent SAFI** (30 min)

**Agenda structuré** :
1. **Périmètre** (5 min) : Sites/apps SAFI + volumétrie
2. **État des lieux** (10 min) : Audits + déclarations + conformité
3. **Organisation** (5 min) : Référent accessibilité + ETP + budget
4. **Plan d'action** (5 min) : Actions 2025 + jalons
5. **Indicateurs** (5 min) : Valeurs actuelles + cibles

**Outils** :
- Visio + écran partagé (remplissage collaboratif)
- Enregistrement (si accord référent)
- Notes partagées (Google Docs, Notion)

**Checklist** :
- [ ] Entretien réalisé (30 min)
- [ ] Template pré-rempli complété
- [ ] Données chiffrées collectées
- [ ] URLs vérifiées (sites/déclarations)
- [ ] Actions prioritaires validées

---

### Phase 2 - Rédaction Contenu (2h)

#### Microtâches

**Structure identique S6-03 BGS** :

**2.1 Front-matter** (5 min)
```yaml
---
service: SAFI
referent: [Nom Référent]
email: [email@sg.gouv.fr]
updated: 2025-10-07
validation_status: in_progress
---
```

**2.2 Section 1 - Périmètre** (20 min)
- Tableau sites/applications SAFI
- Volumétrie (sites publics, apps métier, utilisateurs)
- Outils exclus périmètre

**2.3 Section 2 - État des lieux** (30 min)
- Tableau audits réalisés (dates, taux conformité, rapports)
- Déclarations accessibilité (URLs)
- Synthèse conformité (niveau moyen, points forts, axes)

**2.4 Section 3 - Organisation** (15 min)
- Référent accessibilité SAFI (nom, fonction, email)
- Équipe dédiée (ETP, formation, budget)
- Gouvernance (COPIL, reporting, décisions)

**2.5 Section 4 - Plan d'action** (30 min)
- Tableau actions prioritaires 2025 (action, responsable, échéance, statut, priorité)
- Jalons clés T1-T4 2025
- Budget prévisionnel (audits, corrections, formation)

**2.6 Section 5 - Indicateurs** (15 min)
- Tableau indicateurs quantitatifs (valeur actuelle, cible 2025, cible 2026)
- Indicateurs qualitatifs (satisfaction, retours, conformité légale)
- Reporting (fréquence, format, diffusion)

**Checklist globale Phase 2** :
- [ ] 5 sections complétées
- [ ] Données réelles (pas placeholder)
- [ ] Tableaux formatés markdown
- [ ] URLs valides
- [ ] Niveaux détail cohérent avec BGS/SIRCOM/SNUM

---

### Phase 3 - Conformité 31 Points DINUM (45 min)

#### Microtâches

**3.1 Parcours checklist 31 points avec référent** (30 min)

**Méthode collaborative** :
- Partage écran : fichier `docs/modules/safi.md`
- Lire chaque point DINUM un par un
- Référent SAFI indique : ✅ Conforme / ⏳ En cours / ❌ Non conforme
- Cocher `[x]` si ✅ Conforme

**Points souvent conformes (à valider SAFI)** :
- Point 1 : Référent accessibilité nommé
- Point 2 : Engagement direction formalisé
- Point 4 : Schéma pluriannuel publié (ce document)
- Point 10 : Formation agents sensibilisation
- Point 13 : Déclarations accessibilité publiées

**Cible** : Minimum 20/31 points cochés (statut "Conforme")

**Checklist** :
- [ ] 31 points DINUM parcourus avec référent
- [ ] X/31 points cochés (validation référent)
- [ ] Total confirmé : 31 lignes `<!-- DINUM -->` exactement
- [ ] Aucune ligne ajoutée/supprimée

**3.2 Compléter blocs légaux** (15 min)

```markdown
## 6. Conformité légale

### Déclaration d'accessibilité

**Sites avec déclaration publiée** :
- ✅ [Site SAFI 1] : [URL déclaration]
- ✅ [App SAFI 2] : [URL déclaration]

**Sites sans déclaration** :
- ⏳ [Site SAFI 3] : Publication T2 2025 (audit en cours)

### Dérogations pour charge disproportionnée

[Si applicable]
- **[Site SAFI X]** : Charge disproportionnée justifiée
  - **Motif** : Refonte complète prévue 2026, coût mise conformité > coût refonte
  - **Alternative** : Assistance utilisateur dédiée (email + téléphone)

[Sinon]
Aucune dérogation invoquée. Mise en conformité totale visée d'ici 2026.

### Schéma pluriannuel

Ce document constitue le schéma pluriannuel SAFI 2025-2027, conformément à l'article 47 de la loi du 11 février 2005.

**Validation** : [Date validation chef SAFI]
**Publication** : [URL si publié, sinon "Diffusion interne"]
```

**Checklist** :
- [ ] URLs déclarations accessibilité renseignées
- [ ] Dérogations justifiées (si applicables)
- [ ] Schéma pluriannuel mentionné
- [ ] Date validation chef SAFI

---

### Phase 4 - Intégration & Validation (30 min)

#### Microtâches

**4.1 Recalculer scores** (5 min)
```bash
python3 scripts/calculate_scores.py
# Attendu: SAFI X/31 (XX.X%)
# Score global: 107/186 (57.5%)
```

**4.2 Build & Preview** (10 min)
```bash
mkdocs build --strict
docker compose up
# http://localhost:8000/span-sg-repo/modules/safi/
```

**4.3 Validation référent SAFI** (15 min)
- Envoyer preview draft à référent
- Corrections mineures si nécessaires
- Validation formelle (email)

**Checklist** :
- [ ] Score SAFI recalculé
- [ ] Build strict OK
- [ ] Preview local OK
- [ ] Validation référent SAFI obtenue

---

### Phase 5 - Commit & PR (30 min)

#### Microtâches

**5.1 Branche + Commit** (15 min)
```bash
git checkout draft
git pull origin draft
git checkout -b feature/s6-04-completion-safi

git add docs/modules/safi.md docs/synthese.md
git commit -m "feat(safi): complète module SAFI (S6-04)

- 31 points DINUM renseignés (X/31 conformes)
- 5 sections obligatoires complétées
- Blocs légaux remplis
- Plan d'actions prioritaires 2025
- Score: 76/186 → 107/186 (+31 points, 57.5%)

Référent: [Nom Référent SAFI]
Validation: [Date validation]

Closes: roadmap/S6-04-completion-module-safi.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push -u origin feature/s6-04-completion-safi
```

**5.2 Pull Request** (15 min)
```bash
gh pr create --base draft \
  --title "feat(safi): Complétion Module SAFI 31/31 (S6-04)" \
  --body "## Objectif
Compléter module SAFI pour atteindre score 107/186 (57.5%).

## Changements
- ✅ Front-matter mis à jour (référent SAFI)
- ✅ Section 1 : Périmètre (X sites/applications)
- ✅ Section 2 : État des lieux (audits, déclarations)
- ✅ Section 3 : Organisation (référent, ETP, gouvernance)
- ✅ Section 4 : Plan d'action 2025 (5+ actions prioritaires)
- ✅ Section 5 : Indicateurs (quantitatifs + qualitatifs)
- ✅ 31 points DINUM renseignés (X/31 conformes)
- ✅ Blocs légaux complétés
- ✅ Synthèse recalculée : 76/186 → 107/186

## Validation
- [x] Référent SAFI validé contenu
- [x] Build MkDocs strict OK
- [x] 31 points DINUM confirmés

## Preview
[Module SAFI draft](https://alexmacapple.github.io/span-sg-repo/draft/modules/safi/)

## Impact
**Score** : +31 points (40.9% → 57.5%)
**Progress** : 4/6 modules complétés (67%)

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

**Checklist** :
- [ ] PR créée vers `draft`
- [ ] CI passe
- [ ] Revue Alexandra/Bertrand

---

## Critères d'acceptation

### Fonctionnels
- [ ] Module SAFI complété (31 points DINUM présents)
- [ ] Minimum 20/31 points cochés (statut "Conforme")
- [ ] 5 sections obligatoires remplies
- [ ] Blocs légaux complétés

### Techniques
- [ ] Front-matter valide
- [ ] Score recalculé : 76/186 → 107/186 (+31 points)
- [ ] Build MkDocs strict OK
- [ ] 31 lignes `<!-- DINUM -->` exactement

### Contenu
- [ ] Données réelles SAFI (pas placeholder)
- [ ] URLs déclarations accessibilité valides
- [ ] Actions prioritaires réalistes (T1-T4 2025)
- [ ] Indicateurs mesurables

### Validation
- [ ] Référent SAFI identifié et validé contenu
- [ ] Revue Alexandra

---

## Risques & Solutions

### Risque 1 : Référent SAFI indisponible
**Solution** :
- Décaler S6-04 après S6-05 (SIEP) ou S6-06 (SRH)
- Paralléliser avec autre module si ressources disponibles

### Risque 2 : Données partielles SAFI
**Solution** :
- Remplir avec estimations + TODO explicites
- Marquer module "En cours" (< 20/31)
- Planifier complétion S7

### Risque 3 : Redondance rédaction (fatigue)
**Solution** :
- Réutiliser structure BGS (copier-coller sections puis adapter)
- Template pré-rempli gain temps 30-40%
- Pause entre modules (1 jour)

---

## Métriques succès

**Avant S6-04** :
- Module SAFI : 0/31 (0.0%)
- Score global : 76/186 (40.9%)
- Modules validés : 3/6

**Après S6-04** :
- Module SAFI : X/31 (XX.X%, cible ≥20/31)
- Score global : 107/186 (57.5%)
- Modules validés : 4/6

**Impact scoring** : 94/100 → 98/100 (+4 points Modules, progress 50% → 67%)

---

## Dépendances

**Bloquants** :
- Référent SAFI identifié
- Données accessibilité SAFI disponibles

**Facilitateurs** :
- S6-03 (BGS complété) : Méthodologie éprouvée
- Template pré-rempli : Gain temps 30-40%

**Bloque** : Aucune story

---

## Notes d'implémentation

### Optimisation temps
**Réutilisation structure BGS** :
1. Copier `docs/modules/bgs.md` → `/tmp/safi-draft.md`
2. Rechercher-remplacer "BGS" → "SAFI"
3. Adapter données spécifiques SAFI (30 min vs 2h)
4. Valider avec référent

**Gain** : 1-2h sur Phase 2 (rédaction)

### Particularités SAFI
**Service Affaires Financières + Immobilières** :
- Périmètre mixte : Finance (apps métier) + Immobilier (sites publics)
- Potentiellement plus de dérogations (systèmes legacy finance)
- Indicateurs spécifiques : Satisfaction agents (apps métier) + Grand public (immobilier)

### Parallélisation possible
Si 2+ contributeurs disponibles :
- S6-04 (SAFI) + S6-05 (SIEP) en parallèle
- Référents différents, aucune dépendance
- Gain : 2 jours → 1 jour (4-6h chacun)
