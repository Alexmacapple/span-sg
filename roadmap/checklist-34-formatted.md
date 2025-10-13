# Checklist SPAN 34 Critères (Format Markdown Cochable)

**Source:** Référence officielle DINUM/Arcom
**Version:** 2024-02-05
**Format:** Markdown cochable avec balises `<!-- CHECKLIST -->`

---

## Checklist de conformité (34 critères)

### 1. Vision (3 critères)

- [ ] Politique d'accessibilité numérique formalisée et publiée <!-- CHECKLIST -->
- [ ] Accessibilité intégrée dans la stratégie numérique de l'entité <!-- CHECKLIST -->
- [ ] Politique d'intégration des personnes en situation de handicap documentée <!-- CHECKLIST -->

### 2. RAN - Référent Accessibilité Numérique (7 critères)

- [ ] SPAN durée maximum 3 ans (conformité légale art. 47 loi handicap) <!-- CHECKLIST -->
- [ ] Position fonctionnelle et missions du référent accessibilité définies <!-- CHECKLIST -->
- [ ] Plans d'actions annuels publiés (minimum année en cours) <!-- CHECKLIST -->
- [ ] SPAN publié et accessible en ligne sur site de l'entité <!-- CHECKLIST -->
- [ ] SPAN disponible dans un format accessible (PDF/A ou HTML conforme RGAA) <!-- CHECKLIST -->
- [ ] Liens vers SPAN présents dans les déclarations d'accessibilité des services <!-- CHECKLIST -->
- [ ] Bilan annuel d'accessibilité réalisé et publié <!-- CHECKLIST -->

### 3. Organisation (7 critères)

- [ ] Recours à des ressources et expertises externes documenté (budget, procédures) <!-- CHECKLIST -->
- [ ] Moyens techniques et outillage accessibilité identifiés et disponibles <!-- CHECKLIST -->
- [ ] Organisation interne définie (équipe accessibilité, rôles, responsabilités) <!-- CHECKLIST -->
- [ ] Modalités de contrôle des services numériques définies (audits internes/externes) <!-- CHECKLIST -->
- [ ] Processus de traitement des demandes des usagers établi (contact, délai réponse) <!-- CHECKLIST -->
- [ ] Processus internes documentés (intégration accessibilité dans projets) <!-- CHECKLIST -->
- [ ] Révision et mise à jour régulière du SPAN (annuellement minimum) <!-- CHECKLIST -->

### 4. Budget (2 critères)

- [ ] Ressources humaines dédiées identifiées (ETP alloués à l'accessibilité) <!-- CHECKLIST -->
- [ ] Ressources financières affectées (budget annuel accessibilité identifiable) <!-- CHECKLIST -->

### 5. Gestion de projets (7 critères)

- [ ] Prise en compte de l'accessibilité dès la conception des nouveaux projets <!-- CHECKLIST -->
- [ ] Tests utilisateurs incluant des personnes en situation de handicap <!-- CHECKLIST -->
- [ ] Audits de conformité RGAA planifiés pour tous les services du périmètre <!-- CHECKLIST -->
- [ ] Mesures correctives définies avec calendrier de mise en conformité <!-- CHECKLIST -->
- [ ] Calendrier de corrections priorisé sur usages et volumétrie (services les plus utilisés) <!-- CHECKLIST -->
- [ ] Mesures d'accessibilité non obligatoires prévues (niveau AAA, FALC, LSF) <!-- CHECKLIST -->
- [ ] Suivi de couverture des audits (services audités vs total, périodicité) <!-- CHECKLIST -->

### 6. RH - Ressources Humaines (3 critères)

- [ ] Compétences accessibilité intégrées dans les fiches de poste concernées <!-- CHECKLIST -->
- [ ] Processus de recrutement intégrant l'accessibilité (critères sélection) <!-- CHECKLIST -->
- [ ] Plan de formation et sensibilisation des agents (tous profils) <!-- CHECKLIST -->

### 7. Achats (5 critères)

- [ ] Clauses accessibilité obligatoires dans marchés et commandes publiques <!-- CHECKLIST -->
- [ ] Critères de notation et sélection des prestataires incluant accessibilité <!-- CHECKLIST -->
- [ ] Procédures de recette des livrables (vérification conformité RGAA) <!-- CHECKLIST -->
- [ ] Conventions avec partenaires/opérateurs incluant exigences accessibilité <!-- CHECKLIST -->
- [ ] Suivi de la conformité des marchés (contrôle effectif des livrables) <!-- CHECKLIST -->

---

## Validation Comptage

- Vision: 3
- RAN: 7
- Organisation: 7
- Budget: 2
- Gestion projets: 7
- RH: 3
- Achats: 5

**Total: 3 + 7 + 7 + 2 + 7 + 3 + 5 = 34 critères** ✓

---

## Instructions d'Intégration

### Dans docs/modules/_template.md

Remplacer la section `## points de contrôle officiels (31)` par:

```markdown
## Checklist de conformité (34 critères)

[Copier tout le contenu ci-dessus depuis "### 1. Vision" jusqu'à "### 7. Achats"]

**Score: 0/34 (0.0%)**
```

### Dans docs/modules/{service}.md

Même procédure pour chaque module (BGS, SAFI, SIEP, SIRCOM, SNUM, SRH).

---

## Règles de Modification

**IMPORTANT:** Une fois intégrée dans les modules:

1. **NE JAMAIS ajouter/supprimer de lignes `<!-- CHECKLIST -->`**
   - Total DOIT rester exactement 34
   - Script `calculate_scores.py` vérifie cette contrainte

2. **Seules les coches `[ ]` → `[x]` sont modifiables**
   - Référent métier coche les critères conformes
   - MiWeb valide/ajuste lors de la validation

3. **Texte des critères peut être clarifié**
   - Améliorer formulation si nécessaire (ex: "ETP alloués" → "ETP alloués explicitement")
   - MAIS balise `<!-- CHECKLIST -->` DOIT rester en fin de ligne

---

## Exemples Utilisation

### Module vide (SNUM)
```markdown
### 1. Vision (3 critères)

- [ ] Politique d'accessibilité numérique formalisée <!-- CHECKLIST -->
- [ ] Accessibilité intégrée stratégie numérique <!-- CHECKLIST -->
- [ ] Politique intégration personnes handicapées <!-- CHECKLIST -->

**Score: 0/34 (0.0%)**
```

### Module partiellement complété (SIRCOM réévalué)
```markdown
### 1. Vision (3 critères)

- [x] Politique d'accessibilité numérique formalisée <!-- CHECKLIST -->
  > Validé: SPAN 2024-2027 publié 18/03/2024
- [x] Accessibilité intégrée stratégie numérique <!-- CHECKLIST -->
  > Validé: Accessibilité définie comme préoccupation majeure
- [x] Politique intégration personnes handicapées <!-- CHECKLIST -->
  > Validé: Loi 2005-102 mentionnée explicitement

**Score: 26/34 (76.5%)**
```

---

*Fichier prêt pour intégration Phase 4*
