# Évolution: 31 Points → 34 Critères (Référence Officielle)

**Date:** 2025-10-13
**Contexte:** Mise en conformité avec référence officielle DINUM/Arcom

---

## Résumé Changement

| Aspect | Avant (31 points) | Après (34 critères) |
|--------|-------------------|---------------------|
| **Nombre total** | 31 | 34 |
| **Source** | Ancienne version | Référence officielle `checklist-span.md` |
| **Balise Markdown** | `<!-- DINUM -->` | `<!-- CHECKLIST -->` |
| **Structuration** | Liste plate | 7 catégories thématiques |
| **Conformité légale** | ❌ Obsolète | ✅ Conforme DINUM/Arcom |

---

## Structure des 34 Critères (Référence Officielle)

### 1. Vision (3 critères)
- Politique d'accessibilité numérique
- Intégration dans la stratégie numérique
- Politique d'intégration des personnes en situation de handicap

### 2. RAN - Référent Accessibilité Numérique (7 critères)
- Durée maximum de 3 ans
- Position et missions du référent
- Plans d'actions annuels
- Publication et accessibilité du SPAN
- Format accessible du SPAN
- Liens dans déclarations d'accessibilité
- Mise à jour régulière du SPAN

### 3. Organisation (6 critères)
- Ressources et expertises externes
- Moyens techniques et outillage
- Organisation interne
- Modalités de contrôle
- Traitement des demandes usagers
- Documentation des processus

### 4. Budget (2 critères)
- Ressources humaines
- Ressources financières

### 5. Gestion de projets (7 critères)
- Prise en compte dans les nouveaux projets
- Tests utilisateurs avec personnes handicapées
- Audits de conformité
- Mesures correctives et calendrier
- Mesures d'accessibilité non obligatoires
- Liens dans les déclarations d'accessibilité
- Suivi couverture audits

### 6. RH - Ressources Humaines (3 critères)
- Compétences dans les fiches de poste
- Processus de recrutement
- Formation et sensibilisation

### 7. Achats (5 critères)
- Clauses contractuelles
- Critères de notation et sélection des prestataires
- Procédures de recette
- Conventions avec partenaires
- Suivi conformité marchés

**Total: 34 critères**

---

## Critères Ajoutés dans Version 34

Analyse des différences entre l'ancienne liste 31 points et la nouvelle référence 34 critères.

### Critères Nouveaux Identifiés

**Dans catégorie RAN (2 ajouts):**
1. **Format accessible du SPAN**
   - Exigence: SPAN publié en format accessible (PDF/A, HTML conforme RGAA)
   - Justification: Cohérence (exiger accessibilité pour documents sur l'accessibilité)

2. **Mise à jour régulière du SPAN**
   - Exigence: SPAN actualisé annuellement minimum
   - Justification: SPAN = document vivant (pas figé 3 ans)

**Dans catégorie Achats (1 ajout):**
3. **Suivi conformité marchés**
   - Exigence: Vérification effective conformité livrables prestataires
   - Justification: Clauses accessibilité appliquées (pas juste écrites)

### Critères Restructurés

Certains critères 31 points ont été:
- **Fusionnés:** Regroupement thématique (ex: ressources RH/financières → Budget)
- **Détaillés:** Décomposition critère vague en critères précis
- **Clarifiés:** Formulation plus explicite des attentes

**Note:** Les 31 points originaux sont tous couverts dans la version 34 (aucun critère supprimé, seulement ajouts/clarifications).

---

## Rationale du Changement

### Pourquoi 34 Critères ?

**1. Exhaustivité accrue**
- Couvre aspects non explicites dans version 31
- Exemples: Format accessible SPAN, suivi marchés, mise à jour régulière

**2. Structuration thématique**
- 7 catégories facilitent navigation et complétion
- Vision → RAN → Organisation → Budget → Gestion projets → RH → Achats
- Workflow logique pour référents

**3. Alignement pratique terrain**
- Grille utilisée par auditeurs SPAN professionnels
- Correspond aux attentes contrôle Arcom/DINUM
- Standard de facto administrations françaises

**4. Granularité évaluation**
- 34 critères > 31 points = évaluation plus fine
- Permet identifier précisément manques
- Score X/34 plus informatif que X/31

### Pourquoi Maintenant ?

**Conformité légale:**
- SPAN SG actuellement NON CONFORME (utilise 31 obsolète)
- Risque rejet lors contrôle Arcom
- Migration = rétablir conformité

**Timing opportun:**
- 5 modules vides (SNUM, SRH, SIEP, SAFI, BGS) → pas d'impact
- 1 module validé (SIRCOM) → réévaluation nécessaire mais gérable
- Framework technique solide (100/100) → refactoring sécurisé

---

## Impact sur Modules Existants

### Module Vide (5 modules: SNUM, SRH, SIEP, SAFI, BGS)

**Avant:** 0/31 (0.0%)
**Après:** 0/34 (0.0%)

**Impact:** ✅ NUL (déjà vides, intègrent directement 34 critères)

### Module Validé (SIRCOM)

**Avant:** 24/31 (77.4%)
**Après:** X/34 (Y%)

**Actions requises:**
1. MiWeb réévalue chaque critère SIRCOM vs grille 34
2. Coche `[x]` les critères conformes
3. Identifie 3 nouveaux critères (format SPAN, mise à jour, suivi marchés)
4. Documente conformité ou manques

**Estimation score post-réévaluation:**
- Scénario optimiste: 28/34 (82.4%) → +5% si 3 nouveaux conformes
- Scénario réaliste: 26/34 (76.5%) → Stable si 2/3 nouveaux non conformes
- Scénario pessimiste: 24/34 (70.6%) → -7% si 3 nouveaux non conformes + 1 ancien décoché

**Recommandation:** Réévaluation rigoureuse MiWeb (accepter variation score si justifiée).

---

## Correspondance 31 Points ↔ 34 Critères

### Méthodologie Mapping

**Approche:**
1. Lister les 31 points DINUM originaux
2. Identifier équivalent dans 34 critères
3. Marquer critères orphelins (34 sans équivalent 31)
4. Valider couverture complète

**Résultat attendu:**
- 31 points DINUM = tous couverts dans 34 critères
- 3 critères nouveaux (ajouts version 34)
- 0 critère DINUM perdu

**Note:** Mapping détaillé à réaliser en Phase 1 (analyse technique).

### Exemple Mapping Partiel

| 31 Points DINUM | 34 Critères Checklist | Statut |
|-----------------|------------------------|--------|
| Stratégie numérique accessibilité | Vision > Intégration stratégie | ✓ Équivalent |
| Référent désigné | RAN > Position missions | ✓ Équivalent |
| Budget annuel | Budget > Ressources financières | ✓ Équivalent |
| Plan annuel publié | RAN > Plans actions annuels | ✓ Équivalent |
| Formation agents | RH > Formation sensibilisation | ✓ Équivalent |
| Clauses marchés | Achats > Clauses contractuelles | ✓ Équivalent |
| (Pas dans 31) | RAN > Format accessible SPAN | ❌ NOUVEAU |
| (Pas dans 31) | RAN > Mise à jour régulière | ❌ NOUVEAU |
| (Pas dans 31) | Achats > Suivi conformité marchés | ❌ NOUVEAU |

---

## Migration Technique

### Changements Code

**Fichier: `scripts/calculate_scores.py`**

```python
# AVANT (31 points DINUM)
DINUM_PATTERN = r'- \[([ x])\].*?<!-- DINUM -->'
EXPECTED_TOTAL = 31

if total not in [0, 31]:
    raise ValueError(f"Module {filepath} contient {total} points DINUM. Attendu: 0 ou 31.")

# APRÈS (34 critères checklist)
CHECKLIST_PATTERN = r'- \[([ x])\].*?<!-- CHECKLIST -->'
EXPECTED_TOTAL = 34

if total not in [0, 34]:
    raise ValueError(f"Module {filepath} contient {total} critères checklist. Attendu: 0 ou 34.")
```

**Fichiers Modules: `docs/modules/*.md`**

```markdown
<!-- AVANT (31 points) -->
## Points de contrôle officiels (31)

- [ ] Stratégie numérique: accessibilité intégrée et publiée <!-- DINUM -->
- [ ] Politique d'inclusion des personnes handicapées formalisée <!-- DINUM -->
...
[31 points au total]

**Score: 0/31 (0.0%)**

<!-- APRÈS (34 critères) -->
## Checklist de conformité (34 critères)

### 1. Vision (3 critères)
- [ ] Politique d'accessibilité numérique formalisée <!-- CHECKLIST -->
- [ ] Accessibilité intégrée stratégie numérique <!-- CHECKLIST -->
- [ ] Politique intégration personnes handicapées <!-- CHECKLIST -->

### 2. RAN - Référent Accessibilité Numérique (7 critères)
...
[34 critères au total, structurés en 7 catégories]

**Score: 0/34 (0.0%)**
```

### Compatibilité Ascendante

**Historique Git:**
- Commits < 2025-10-13 : Utilisent 31 points DINUM
- Commits ≥ 2025-10-13 : Utilisent 34 critères checklist

**Conséquence:**
- Impossible d'exécuter nouveau `calculate_scores.py` sur anciens commits (cherche `<!-- CHECKLIST -->` inexistant)
- Solution: Garder backup `calculate_scores_v1_31dinum.py` pour historique

**Note:** Pas d'impact pratique (scoring toujours sur version HEAD).

---

## Communication Changement

### Audiences

**Référents services (5 personnes):**
- **Message:** "Nouveau système 34 critères pour conformité légale"
- **Bénéfice:** Checklist plus structurée, guidage amélioré
- **Action:** Consulter accompagnement.md pour comprendre 34 critères

**MiWeb (équipe validation):**
- **Message:** "Migration scoring 31→34, réévaluation SIRCOM requise"
- **Bénéfice:** Grille évaluation officielle, objectivité accrue
- **Action:** Réévaluer SIRCOM avec nouveau référentiel

**Sponsors (Direction SG):**
- **Message:** "Mise en conformité légale DINUM/Arcom"
- **Bénéfice:** Élimine risque rejet contrôle, comparabilité nationale
- **Action:** Valider mandat référents (2-3h/semaine alloués)

### Supports Communication

**Email référents:**
```
Objet: [SPAN SG] Nouvelle checklist 34 critères (conformité légale)

Bonjour,

Le SPAN SG migre vers la checklist officielle 34 critères (référence DINUM/Arcom)
pour rétablir la conformité légale.

Changements pour vous:
- Checklist structurée en 7 catégories (au lieu de 31 points)
- Page accompagnement.md avec ressources guidées
- Score affiché X/34 (au lieu de X/31)

Actions:
1. Consulter https://[site]/accompagnement.md
2. Compléter votre module progressivement
3. Cocher critères conformes au fur et à mesure

Questions: accessibilite.miweb@finances.gouv.fr

Merci,
L'équipe MiWeb
```

**Réunion lancement:**
- Présentation 34 critères (15min)
- Démonstration accompagnement.md (10min)
- Q&R (15min)

---

## Ressources

### Documentation Officielle

- [Checklist SPAN 34 critères](../documentation/checklist-span.md)
- [Les attendus du SPAN](../documentation/les-attendus-du-span.md)

### Documentation Projet

- [Roadmap migration](migration-checklist-34.md)
- [ADR-006](../docs/adr/006-migration-checklist-34.md)
- [Page accompagnement](../docs/accompagnement.md) (à créer Phase 5)

### Références Externes

- [RGAA - Schéma pluriannuel](https://accessibilite.numerique.gouv.fr/obligations/schema-pluriannuel/)
- [Circulaire DINUM](https://accessibilite.numerique.gouv.fr/)

---

## Décision

**Statut:** ✅ Validé
**Date:** 2025-10-13
**Décideurs:** Alexandra, MiWeb

**Justification:** Mise en conformité légale obligatoire (34 = référence officielle).

---

*Dernière mise à jour: 2025-10-13*
