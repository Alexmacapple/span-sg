# Checklist SPAN 33 Critères (Format Markdown Cochable)

**Source:** SPAN-checklist-v2024-02-05-AAL.ots (extraction officielle)
**Format:** Markdown cochable avec balises `<!-- CHECKLIST -->`
**Total:** 33 critères

---

## Checklist de conformité (33 critères)

### 1. Vision (3 critères)

- [ ] Politique de l'entité en matière d'accessibilité numérique décrite dans le SPAN <!-- CHECKLIST -->
- [ ] Prise en compte de l'accessibilité numérique dans la stratégie numérique de l'entité <!-- CHECKLIST -->
- [ ] Prise en compte de l'accessibilité dans la politique d'intégration des personnes en situation de handicap <!-- CHECKLIST -->

### 2. RAN - Référent Accessibilité Numérique (7 critères)

- [ ] SPAN durée maximum 3 ans (conformité légale art. 47 loi handicap) <!-- CHECKLIST -->
- [ ] Position fonctionnelle du référent accessibilité numérique décrite <!-- CHECKLIST -->
- [ ] Missions du référent accessibilité numérique décrites <!-- CHECKLIST -->
- [ ] Bilan des plans d'actions annuels (si nécessaire) <!-- CHECKLIST -->
- [ ] Travaux de mise en conformité planifiés annuellement dans plans d'actions <!-- CHECKLIST -->
- [ ] SPAN et plan d'action année en cours disponibles en ligne sur site de l'entité <!-- CHECKLIST -->
- [ ] SPAN et plans d'actions publiés dans un format accessible <!-- CHECKLIST -->

### 3. Organisation (6 critères)

- [ ] Mise en œuvre des ressources et expertises externes décrite (si applicable) <!-- CHECKLIST -->
- [ ] Mise en œuvre des moyens techniques pour gérer et tester l'accessibilité décrite <!-- CHECKLIST -->
- [ ] Mise en œuvre de l'outillage pour gérer et tester l'accessibilité décrite <!-- CHECKLIST -->
- [ ] Organisation interne pour mettre en œuvre les obligations d'accessibilité décrite <!-- CHECKLIST -->
- [ ] Modalités de contrôle des services numériques décrites <!-- CHECKLIST -->
- [ ] Modalités d'organisation pour le traitement des demandes des usagers décrites <!-- CHECKLIST -->

### 4. Budget (2 critères)

- [ ] Ressources humaines affectées à l'accessibilité numérique décrites <!-- CHECKLIST -->
- [ ] Ressources financières affectées à l'accessibilité numérique décrites <!-- CHECKLIST -->

### 5. Gestion de projets (7 critères)

- [ ] Prise en compte de l'accessibilité numérique dans les nouveaux projets décrite <!-- CHECKLIST -->
- [ ] Prise en compte des personnes en situation de handicap dans les tests utilisateurs prévue <!-- CHECKLIST -->
- [ ] Évaluations (ou audits) de conformité prévues pour l'ensemble des services de communication <!-- CHECKLIST -->
- [ ] Mesures correctives pour traiter les contenus non accessibles décrites <!-- CHECKLIST -->
- [ ] Calendrier de mise en œuvre priorisé (contenus les plus consultés, services les plus utilisés) <!-- CHECKLIST -->
- [ ] Mesures d'accessibilité non obligatoires décrites (LSF, FALC, niveau AAA, si nécessaire) <!-- CHECKLIST -->
- [ ] Liens vers SPAN et plans d'actions présents dans déclarations d'accessibilité des services <!-- CHECKLIST -->

### 6. RH - Ressources Humaines (3 critères)

- [ ] Prise en compte des compétences/connaissances accessibilité dans les fiches de poste décrite <!-- CHECKLIST -->
- [ ] Prise en compte des compétences/connaissances accessibilité dans les processus de recrutement décrite <!-- CHECKLIST -->
- [ ] Actions de formation et de sensibilisation des agents décrites <!-- CHECKLIST -->

### 7. Achats (5 critères)

- [ ] Intégration de l'accessibilité numérique dans les clauses contractuelles (appels d'offres, devis) prévue <!-- CHECKLIST -->
- [ ] Intégration de l'accessibilité numérique dans les critères de notation des prestataires prévue <!-- CHECKLIST -->
- [ ] Intégration de l'accessibilité numérique dans les critères de sélection des prestataires prévue <!-- CHECKLIST -->
- [ ] Intégration de l'accessibilité numérique dans les procédures de recette prévue <!-- CHECKLIST -->
- [ ] Intégration de l'accessibilité dans les conventions avec opérateurs/délégataires/partenaires prévue (si nécessaire) <!-- CHECKLIST -->

---

## Validation Comptage

- Vision: 3
- RAN: 7
- Organisation: 6
- Budget: 2
- Gestion projets: 7
- RH: 3
- Achats: 5

**Total: 3 + 7 + 6 + 2 + 7 + 3 + 5 = 33 critères** ✓

---

## Instructions d'Intégration

### Dans docs/modules/_template.md

Remplacer la section `## points de contrôle officiels (31)` par:

```markdown
## Checklist de conformité (33 critères)

[Copier tout le contenu ci-dessus depuis "### 1. Vision" jusqu'à "### 7. Achats"]

**Score: 0/33 (0.0%)**
```

### Règles de Modification

1. **NE JAMAIS ajouter/supprimer de lignes `<!-- CHECKLIST -->`**
   - Total DOIT rester exactement 33
   - Script `calculate_scores.py` vérifie: `total in (0, 33)`

2. **Seules les coches `[ ]` → `[x]` sont modifiables**
   - Référent métier coche les critères conformes
   - MiWeb valide/ajuste lors de la validation

3. **Texte des critères peut être clarifié**
   - Améliorer formulation si nécessaire
   - MAIS balise `<!-- CHECKLIST -->` DOIT rester en fin de ligne

---

*Fichier prêt pour intégration Phase 3-4*
