# Exemples de remplissage modules SPAN

Ce document fournit 3 exemples complets de remplissage de modules services pour aider les référents à renseigner leurs propres contenus.

---

## Exemple 1 : SIRCOM (module pilote - score élevé)

### Front-matter
```yaml
---
service: SIRCOM
referent: "Marie Dupont"
updated: "2025-09-30"
---
```

### Section 1 : Périmètre
```markdown
## 1. Périmètre

Le Service Interministériel des Ressources et des Compétences (SIRCOM) gère les applications et services numériques suivants :

### Applications métiers principales
- **Portail RH intranet** : Gestion des ressources humaines, 5000 agents/jour, criticité HAUTE
  - URL : https://rh-intranet.gouv.fr (accès restreint)
  - Public : Agents internes
  - Fonctions : Fiches de paie, congés, formations, mobilité

- **Application de formation en ligne** : E-learning accessible à tous les agents, 2000 utilisateurs actifs/mois, criticité MOYENNE
  - URL : https://formation.sircom.gouv.fr
  - Public : Agents internes + partenaires
  - Fonctions : Catalogues formations, inscriptions, suivi parcours

- **Site carrières publiques** : Site externe recrutement, 500 visiteurs/jour, criticité HAUTE
  - URL : https://carrieres-publiques.gouv.fr
  - Public : Grand public
  - Fonctions : Offres d'emploi, candidatures en ligne, suivi dossiers

### Sites web et intranets
- **Intranet SIRCOM** : Portail d'information interne, 3000 agents
- **Site institutionnel SIRCOM** : Présentation missions et actualités

### Démarches essentielles
- Candidature concours fonction publique (externe, niveau AA requis)
- Inscription formations continues (interne)
- Suivi carrière et mobilité (interne)
```

### Section 2 : État des lieux
```markdown
## 2. État des lieux (synthèse)

### Audits réalisés

- **Site carrières publiques** : Audit RGAA externe par AccessibilitéWeb SARL, juillet 2024, score 82% conforme AA
  - Rapport disponible : [Lien interne uniquement]
  - Taux conformité : 82/100 critères validés
  - Niveau : AA (partiellement conforme)

- **Portail RH intranet** : Audit interne, mars 2024, score 65% conforme AA
  - Audit réalisé par équipe interne formée RGAA
  - Points critiques identifiés : contraste, navigation clavier
  - Correction en cours (livraison T2 2025)

- **Application formation en ligne** : Non audité
  - Audit prévu T3 2025 (budget 5K€)

### Points critiques identifiés

**Contraste couleurs** :
- 12 pages Portail RH : ratio contraste < 4.5:1
- Correction en cours via nouvelle charte graphique

**Navigation clavier** :
- Formulaires Portail RH : focus invisible sur certains champs
- Menu carrières : Skip links absents
- Correction planifiée T2 2025

**Formulaires** :
- Labels manquants sur 8 formulaires Portail RH
- Correction immédiate (0€, développeurs internes)

**Alternatives textuelles** :
- 45 images décoratives mal balisées
- Formation équipe éditoriale prévue T1 2025

### Niveau de conformité actuel
- Global SIRCOM : 73% conforme AA (estimation)
- Cible fin 2025 : 90% conforme AA
- Cible fin 2027 : 100% conforme AA
```

### Section 3 : Organisation
```markdown
## 3. Organisation

### Référent accessibilité
- **Nom** : Marie Dupont
- **ETP dédié** : 40% (2 jours/semaine)
- **Contact** : marie.dupont@sircom.gouv.fr
- **Formations** : Certificat Accès-key (5 jours RGAA), 2023

### Équipe projet
- **Chef de projet SI** : Jean Martin (20% ETP accessibilité)
- **Développeurs sensibilisés** : 8/12 (formation RGAA 2 jours suivie)
- **UX/UI** : Prestation externe (Cabinet UXA, marché 2024-2026)
- **Rédacteurs web** : 4 agents (sensibilisation prévue T1 2025)

### Gouvernance
- **Comité accessibilité** : Réunion trimestrielle
  - Membres : Référent, DSI, Directeur SIRCOM, représentant usagers
  - Rôle : Validation plan d'action, arbitrage budgétaire
- **Point hebdomadaire** : Référent + développeurs (suivi corrections)

### Formations prévues
- T1 2025 : Sensibilisation large (tous agents, 2h visio)
- T2 2025 : Formation développeurs RGAA approfondie (3 jours)
- T3 2025 : Formation rédacteurs (création contenus accessibles, 1 jour)
```

### Section 4 : Plan d'action annuel
```markdown
## 4. Plan d'action annuel (2025)

| Action | Échéance | Responsable | Budget | Statut |
|--------|----------|-------------|--------|--------|
| Audit RGAA complet Application formation | T3 2025 | Marie Dupont | 5000€ | À commencer |
| Correction contraste couleurs Portail RH | T2 2025 | Dev interne (Jean Martin) | 0€ | En cours |
| Formation développeurs RGAA (3j) | T2 2025 | Marie + RH | 3000€ | À commencer |
| Mise en conformité formulaires Portail RH | T2 2025 | Dev interne | 0€ | En cours |
| Formation rédacteurs web (1j) | T3 2025 | Marie + Communication | 800€ | À commencer |
| Refonte charte graphique accessible | T4 2025 | Prestation UXA | 12000€ | Marché en cours |
| Audit RGAA Site carrières (contrôle) | T4 2025 | AccessibilitéWeb | 4000€ | À planifier |

**Budget total 2025** : 24800€
```

### Section 5 : Indicateurs clés
```markdown
## 5. Indicateurs clés

### Taux de conformité
- **Sites web** : 82% conforme AA (cible 95% fin 2025)
- **Applications métiers** : 69% conforme AA (cible 85% fin 2025)
- **Global SIRCOM** : 73% conforme AA

### Formations
- **Agents sensibilisés** : 45/3000 (1.5%) - Cible 50% fin 2025
- **Équipe dev formée** : 8/12 (67%) - Cible 100% fin 2025
- **Rédacteurs formés** : 0/4 (0%) - Cible 100% fin 2025

### Marchés avec clauses accessibilité
- **2024** : 3 marchés sur 8 intègrent clauses RGAA (37.5%)
- **2025 (objectif)** : 100% nouveaux marchés avec clauses RGAA obligatoires

### Budget
- **2024** : 18K€ (audits + formations)
- **2025 (prévisionnel)** : 24.8K€ (audits + formations + refonte)
- **2026 (estimation)** : 15K€ (maintien conformité + audits contrôle)
```

---

## Exemple 2 : SNUM (service en démarrage - score moyen)

### Front-matter
```yaml
---
service: SNUM
referent: "Paul Leroy"
updated: "2025-09-30"
---
```

### Section 1 : Périmètre
```markdown
## 1. Périmètre

Le Service du Numérique (SNUM) pilote 6 applications et services numériques :

### Applications métiers principales
- **Portail intranet SG** : Portail d'information générale, 8000 agents/jour, criticité HAUTE
- **Application gestion budgétaire** : Outil de suivi budgétaire ministériel, 200 utilisateurs, criticité HAUTE
- **Plateforme collaborative** : Espace de travail partagé (type SharePoint), 1500 utilisateurs actifs, criticité MOYENNE
- **Outil de ticketing support** : Helpdesk informatique, 500 tickets/mois, criticité MOYENNE

### Sites web et intranets
- **Site vitrine SG externe** : Présentation missions, 300 visiteurs/jour, criticité BASSE

### Démarches essentielles
- Demande assistance informatique (interne)
- Consultation budgets (interne, sensible)
```

### Section 2 : État des lieux
```markdown
## 2. État des lieux (synthèse)

### Audits réalisés

Aucun audit accessibilité RGAA n'a encore été réalisé sur les applications SNUM.

### État actuel
- **Sensibilisation accessibilité** : Limitée (1 formation sensibilisation DSI, 2024)
- **Conformité estimée** : Inconnue (probablement < 50%)
- **Action prioritaire 2025** : Audit RGAA complet Portail intranet (T2 2025)

### Points critiques présumés
Sur la base d'une première évaluation visuelle (non exhaustive) :
- **Contraste couleurs** : Plusieurs pages avec texte gris clair (à vérifier)
- **Navigation clavier** : Menus déroulants inaccessibles au clavier
- **Formulaires** : Labels potentiellement manquants
- **Images** : Alternatives textuelles absentes ou génériques

**Ces points nécessitent confirmation par audit professionnel.**

### Prochaines étapes
- **T1 2025** : État des lieux préliminaire interne (0€, Paul Leroy)
- **T2 2025** : Audit RGAA externe Portail intranet (8K€)
- **T3 2025** : Plan d'action corrections prioritaires
```

### Section 3 : Organisation
```markdown
## 3. Organisation

### Référent accessibilité
- **Nom** : Paul Leroy
- **ETP dédié** : 20% (1 jour/semaine)
- **Contact** : paul.leroy@snum.gouv.fr
- **Formations** : Formation RGAA 2 jours (prévue T1 2025)

### Équipe projet
- **Chef de projet SI** : Sophie Dubois
- **Développeurs sensibilisés** : 2/15 (13%) - Formations à planifier
- **UX/UI** : Aucune ressource dédiée actuellement
- **Rédacteurs web** : 3 agents (sensibilisation à prévoir)

### Gouvernance (à structurer)
- **Comité accessibilité** : Création prévue T2 2025
  - Membres pressentis : Référent, DSI, représentant utilisateurs
  - Rythme envisagé : Trimestriel
- **Points de suivi** : À définir après premier audit

### Formations prévues
- **T1 2025** : Formation référent RGAA (2 jours, Paul Leroy)
- **T2 2025** : Sensibilisation DSI et développeurs (2h, tous agents)
- **T3 2025** : Formation développeurs avancée (3 jours, 5 devs prioritaires)
```

### Section 4 : Plan d'action annuel
```markdown
## 4. Plan d'action annuel (2025)

| Action | Échéance | Responsable | Budget | Statut |
|--------|----------|-------------|--------|--------|
| Formation référent RGAA (2j) | T1 2025 | Paul Leroy + RH | 1200€ | À commencer |
| État des lieux préliminaire interne | T1 2025 | Paul Leroy | 0€ | À commencer |
| Audit RGAA Portail intranet | T2 2025 | Paul + Prestataire externe | 8000€ | Budget validé |
| Sensibilisation DSI (2h) | T2 2025 | Paul Leroy | 0€ | À planifier |
| Formation 5 développeurs RGAA (3j) | T3 2025 | Paul + RH | 3500€ | À budgéter |
| Corrections critiques Portail intranet | T4 2025 | Dev interne + prestation | 10000€ | À budgéter |

**Budget total 2025** : 22700€ (dont 10K€ à valider)
```

### Section 5 : Indicateurs clés
```markdown
## 5. Indicateurs clés

### Taux de conformité
- **Sites web** : Non mesuré (audit T2 2025)
- **Applications métiers** : Non mesuré
- **Cible fin 2025** : 60% conforme AA (Portail intranet)
- **Cible fin 2027** : 90% conforme AA (toutes applications)

### Formations
- **Agents sensibilisés** : 2/8000 (0.02%) - Cible 10% fin 2025
- **Équipe dev formée** : 2/15 (13%) - Cible 50% fin 2025
- **Référent formé** : 0/1 (formation T1 2025)

### Marchés avec clauses accessibilité
- **2024** : 0 marché sur 5 avec clauses RGAA (0%)
- **2025 (objectif)** : 100% nouveaux marchés > 25K€ avec clauses RGAA

### Budget
- **2024** : 1.2K€ (sensibilisation uniquement)
- **2025 (prévisionnel)** : 22.7K€ (audits + formations + corrections)
- **2026 (estimation)** : 30K€ (extension audits + corrections continues)

### Notes
Le service SNUM est en phase de démarrage accessibilité. Les indicateurs actuels reflètent un point de départ bas, avec engagement fort d'amélioration en 2025-2027.
```

---

## Exemple 3 : SRH (service minimaliste - données limitées)

### Front-matter
```yaml
---
service: SRH
referent: "[À nommer]"
updated: "2025-09-30"
---
```

### Section 1 : Périmètre
```markdown
## 1. Périmètre

Le Service des Ressources Humaines (SRH) gère 3 applications principales :

### Applications métiers principales
- **SIRH (Système Informations RH)** : Gestion paie et carrières, 150 utilisateurs RH, criticité HAUTE
- **Portail agent** : Consultation fiches paie et demandes congés, 4000 agents, criticité HAUTE
- **Outil recrutement** : Gestion candidatures et entretiens, 30 utilisateurs RH, criticité MOYENNE

### Sites web et intranets
- Pas de site web externe SRH (intégré au site SG général)

### Démarches essentielles
- Consultation bulletin de paie (4000 agents mensuels)
- Demande congés et absences (1500 demandes/mois)
```

### Section 2 : État des lieux
```markdown
## 2. État des lieux (synthèse)

### Audits réalisés

Aucun audit accessibilité réalisé.

### État actuel

**Situation** :
- Aucune démarche accessibilité initiée à ce jour
- Conformité estimée : Inconnue
- Pas de référent accessibilité nommé officiellement

**Action immédiate** :
- Nomination référent SRH : T1 2025
- État des lieux préliminaire : T2 2025
- Premier audit RGAA : T3 2025 (Portail agent, prioritaire)

### Points critiques
Non identifiés à ce stade. Audit nécessaire pour diagnostic.
```

### Section 3 : Organisation
```markdown
## 3. Organisation

### Référent accessibilité
**Statut** : Nomination en cours (T1 2025)

**Profil recherché** :
- Agent SRH connaissance SI
- Disponibilité : 20% ETP (1 jour/semaine)
- Formation RGAA à prévoir

**Porteur intérimaire** : Directrice SRH (coordination SPAN uniquement)

### Équipe projet (à constituer)
- **Chef de projet SI** : Identifié (Jean Dupuis, DSI)
- **Développeurs** : À sensibiliser (0/6 formés actuellement)
- **Support externe** : Possible recours prestataire accessibilité

### Gouvernance
Non structurée. À définir après nomination référent.

### Formations prévues
- **T2 2025** : Formation référent RGAA (2 jours)
- **T3 2025** : Sensibilisation équipe DSI SRH (2h)
```

### Section 4 : Plan d'action annuel
```markdown
## 4. Plan d'action annuel (2025)

| Action | Échéance | Responsable | Budget | Statut |
|--------|----------|-------------|--------|--------|
| Nomination référent accessibilité officiel | T1 2025 | Direction SRH | 0€ | En cours |
| Formation référent RGAA (2j) | T2 2025 | Référent + RH | 1200€ | À planifier |
| État des lieux préliminaire 3 applications | T2 2025 | Référent | 0€ | À commencer |
| Audit RGAA Portail agent (prioritaire) | T3 2025 | Prestataire externe | 6000€ | À budgéter |
| Sensibilisation équipe DSI SRH (2h) | T3 2025 | Référent | 0€ | À planifier |

**Budget total 2025** : 7200€ (à valider par DAF)
```

### Section 5 : Indicateurs clés
```markdown
## 5. Indicateurs clés

### Taux de conformité
- **Non mesuré** (aucun audit réalisé)
- **Cible fin 2025** : Audit réalisé + plan d'action défini
- **Cible fin 2027** : 75% conforme AA (applications critiques)

### Formations
- **Agents sensibilisés** : 0/4000 (0%)
- **Équipe dev formée** : 0/6 (0%)
- **Référent nommé** : Non (T1 2025)

### Marchés avec clauses accessibilité
- **2024** : Données non disponibles
- **2025** : À intégrer dans tous nouveaux marchés SI

### Budget
- **2024** : 0€ (aucune action accessibilité)
- **2025 (prévisionnel)** : 7.2K€ (audit + formation)
- **2026 (estimation)** : 15K€ (corrections + audits complémentaires)

### Notes
Le service SRH est en phase de démarrage total. Priorité 2025 : structurer la démarche et nommer un référent.
```

---

## Conseils d'utilisation

### Pour les services avec audits existants
- Utiliser **Exemple 1 (SIRCOM)** comme modèle
- Renseigner scores précis, dates audits, prestataires
- Détailler plan d'action avec budgets validés

### Pour les services en démarrage
- Utiliser **Exemple 2 (SNUM)** comme modèle
- Être transparent sur l'absence de données ("Non mesuré", "À définir")
- Prévoir actions d'état des lieux en priorité

### Pour les services sans référent nommé
- Utiliser **Exemple 3 (SRH)** comme modèle minimaliste
- Indiquer clairement "Nomination en cours"
- Plan d'action focus sur structuration démarche

### Règle d'or
**Mieux vaut un contenu honnête et minimaliste qu'un contenu inventé ou sur-optimiste.**

---

*Document de référence pour Story S3-03 - Renseigner premiers contenus modules*
