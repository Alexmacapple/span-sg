---
bmad_phase: production
bmad_agent: dev
story_type: implementation
autonomous: false
validation: human-qa
---

# Story S4-00 : Mapping contenus réels SIRCOM/SNUM

**Phase** : Semaine 4 - Production
**Priorité** : Critique (bloque S4-01)
**Estimation** : 3h création guide

---

## Contexte projet

**Stratégie v1.0 Hybrid** :
- 2 modules **validés** : SIRCOM, SNUM (contenus réels mappés depuis SPAN officiels)
- 4 modules **en cours** : SRH, SIEP, SAFI, BGS (structure framework, contenus progressifs)
- **Validation** : Bertrand/Alexandra → Stéphane (concept) → Chef SNUM (GO final)

**Sources SPAN officielles découvertes** :
- `span/span-sircom-sg.md` (414 lignes) : SPAN 2024-2027 SIRCOM
- `span/span-portail-pro.sg.md` (106 lignes) : SPAN 2025-2027 Portailpro.gouv (SNUM/SG)

**Problématique** :
Ces documents sont des **politiques stratégiques**, pas des réponses directes aux 31 points DINUM. Le mapping nécessite interprétation et synthèse (estimation brute : 9h).

**Solution retenue** : Mapping assisté avec guide détaillé (ce PRD) contenant tables de correspondance, instructions guidées, exemples pré-rédigés → **gain 30-40% temps** (7h au lieu de 9h).

---

## Objectif

Créer un **guide de mapping détaillé** (tables de correspondance SPAN → DINUM 31 points) pour faciliter l'exécution du mapping en S4-01 par Bertrand/Alexandra.

**Livrables** :
- Tables SIRCOM complètes (31 points, 5 catégories)
- Tables SNUM complètes (31 points, références SIRCOM)
- 17-18 exemples pré-rédigés pour points complexes
- TODO S4-01 tracés pour points non mappables

---

## Prérequis

- [x] Sources SPAN présentes (`span/span-sircom-sg.md`, `span/span-portail-pro.sg.md`)
- [x] Template modules validé (31 points DINUM officiels)
- [x] Décisions stratégiques S4 finalisées (validation_status, disclaimers, badges)
- [x] Workflow validation défini (Bertrand/Alexandra → Stéphane → Chef SNUM)

---

## Méthodologie mapping assisté

### Principes

**Instructions guidées** (option b validée Q23) :
- Checklist 2-4 éléments par point
- Mots-clés à chercher dans sources
- Fallback si élément manquant (TODO S4-01)

**Exemples pré-rédigés** (option d validée Q23) :
- 17-18 exemples complets pour points stratégiques (1.x, 2.x) et difficiles
- Format réponse attendu pour homogénéité rédactionnelle

**TODO explicites** (option a validée Q22) :
- Points non mappables marqués "**→ S4-01**" avec instruction pour review
- Chaînage S4-00 → S4-01 automatique

**Organisation par catégories** (option b validée Q24) :
- 5 catégories DINUM officielles (fidélité checklist)
- Sous-totaux par catégorie (X/Y mappables, Z TODO)

**Séquence prioritaire** (option d validée Q25) :
- SIRCOM d'abord (priorité 1, guide complet)
- SNUM ensuite (priorité 2, références SIRCOM)

---

## Étapes d'implémentation

### Étape 1 : Tables de correspondance SIRCOM (priorité 1, ~4h30)

**Instructions préliminaires** :
- Lire `span/span-sircom-sg.md` intégralement (15 min)
- Identifier structure : §1 Contexte, §2 Politique, §3 Organisation, §4 Périmètre, §5 Plan annuel, Annexe 1 Sites
- Préparer fichier `docs/modules/sircom.md` pour édition

---

#### Catégorie 1 - Politique accessibilité (3 points, ~30 min)

| # | Libellé DINUM | Source | Section | Type | Instructions | Exemple | Difficulté | Temps |
|---|---------------|--------|---------|------|--------------|---------|------------|-------|
| 1 | Stratégie numérique: accessibilité intégrée et publiée | span-sircom | §2.1 Engagement p.3 | Citation | Copier §2.1 "La stratégie numérique..." intégralement | **Exemple** : "La stratégie numérique du SG intègre l'accessibilité comme priorité transverse. Politique publiée sur intranet SG et site externe finances.gouv.fr/accessibilite." | Facile | 5 min |
| 2 | Politique d'inclusion des personnes handicapées formalisée | span-sircom | §2.2 Inclusion p.3-4 | Synthèse | Chercher mention "politique inclusion", "mission handicap", "référent handicap". Synthétiser en 1-2 phrases. Fallback : **→ S4-01** Vérifier existence politique RH inclusion | **Exemple** : "Le SG dispose d'une mission handicap rattachée à la DRH. Politique d'inclusion formalisée dans le plan d'action handicap 2024-2026." | Moyen | 15 min |
| 3 | Objectifs mesurables d'accessibilité définis (KPI) | span-sircom | §5 Plan annuel + Annexe 1 | Synthèse | Extraire 3 KPI chiffrés : 1) Taux conformité cible (%), 2) Nombre sites à auditer, 3) Nombre formations prévues. Format : "Objectifs 2025 : X% conformité, Y audits, Z formations." | **Exemple** : "Objectifs 2025 : 75% conformité RGAA 4.1 pour les 5 sites internet, 7 audits externes, 12 agents formés RGAA." | Moyen | 10 min |

**Sous-total Catégorie 1** : 3/3 mappables, 0 TODO, ~30 min

---

#### Catégorie 2 - Ressources (12 points, ~2h30)

| # | Libellé DINUM | Source | Section | Type | Instructions | Exemple | Difficulté | Temps |
|---|---------------|--------|---------|------|--------------|---------|------------|-------|
| 4 | Référent accessibilité numérique officiellement désigné | span-sircom | §3.1 Référent p.5 | Citation | Copier identité référent (fonction + rattachement). Chercher "Pôle web", "référent accessibilité". | **Exemple** : "Référent accessibilité : Pôle web SG/SIRCOM, rattaché à la Direction Communication." | Facile | 5 min |
| 5 | Temps alloué et moyens du référent définis | span-sircom | §3.1-3.2 p.5-6 | Synthèse | Extraire % ETP ou "temps dédié". Chercher "ETP", "0.5 ETP", "mi-temps", "temps partiel". Fallback : **→ S4-01** Préciser % ETP si non mentionné | **Exemple** : "Le référent accessibilité dispose de 0,5 ETP dédié (20h/semaine) sur ses missions." | Moyen | 10 min |
| 6 | Ressources humaines dédiées identifiées (ETP) | span-sircom | §3.2 Organisation | Synthèse | Lister toutes RH impliquées : référent, webmasters, développeurs, chefs de projet. Format : "X ETP référent + Y ETP support technique." | **Exemple** : "Équipe accessibilité : 0,5 ETP référent + 2 ETP webmasters sensibilisés + 1 chef de projet (10% temps)." | Moyen | 15 min |
| 7 | Budget annuel dédié/identifiable | span-sircom | §3.3 Moyens financiers p.6 | Extraction | Chercher montant en euros : "budget", "enveloppe", "€", "k€", "M€". Fallback : **→ S4-01** Demander budget si non précisé source | **Exemple** : "Budget annuel accessibilité : 50 k€ (audits externes 35 k€ + formations 10 k€ + outils 5 k€)." | Difficile | 20 min |
| 8 | Planification pluriannuelle des moyens (3 ans) | span-sircom | §5 Plan annuel 2024-2026 | Synthèse | Extraire budget/ETP par année (2024, 2025, 2026). Format tableau si détails, sinon phrase synthèse. | **Exemple** : "Planification 2024-2026 : budget constant 50 k€/an, montée en compétence progressive (0,5 → 1 ETP référent en 2026)." | Moyen | 15 min |
| 9 | Compétences accessibilité dans les fiches de poste | span-sircom | §3.4 Compétences | Validation | Chercher "fiche de poste", "compétences requises", "profil". Réponse Oui/Non + précision rôles concernés. Fallback : **→ S4-01** Vérifier avec RH | **Exemple** : "Compétences accessibilité intégrées dans fiches de poste : webmasters (RGAA niveau 2 requis), développeurs (sensibilisation), chefs de projet digital (pilotage audits)." | Moyen | 15 min |
| 10 | Grille de recrutement intégrant l'accessibilité | span-sircom | §3.4 ou N/A | Validation | Chercher "recrutement", "grille évaluation", "critères". Souvent non mentionné → **→ S4-01** À documenter avec RH | Pas d'exemple (TODO probable) | Difficile | 10 min |
| 11 | Plan de formation annuel pour les profils clés | span-sircom | §4 Formation p.7 | Liste | Lister formations prévues avec public cible. Chercher "formation RGAA", "sensibilisation", "public". Format tableau ou liste. | **Exemple** : "Plan formation 2025 : - Formation RGAA certifiante (2 webmasters, mars) - Sensibilisation développeurs (10 agents, avril) - Formation continue référent (1 colloque externe, juin)." | Facile | 10 min |
| 12 | Sensibilisation large (tous agents) planifiée | span-sircom | §4 Formation | Validation | Chercher "sensibilisation générale", "tous agents", "communication interne". Oui/Non + modalités (e-learning, réunions). Fallback : **→ S4-01** Planifier si absent | **Exemple** : "Sensibilisation large : e-learning accessibilité obligatoire pour tous agents SG (déploiement T2 2025, 30 min, suivi completion)." | Moyen | 15 min |
| 13 | Formations par rôle (développeurs, UX, éditorial) | span-sircom | §4 Formation | Tableau | Créer tableau : Rôle | Formation | Durée | Fréquence. Extraire depuis §4. | **Exemple tableau** : <br>Développeurs : RGAA technique (2j, annuel)<br>Webmasters : Certification RGAA (3j, initial)<br>Éditoriaux : Contenus accessibles (1j, bisannuel) | Moyen | 20 min |
| 14 | Outils de test/accessibilité référencés et disponibles | span-sircom | §3.5 Outils p.6 | Liste | Lister outils utilisés : Wave, Axe, Color Contrast, validateurs. Chercher "outils", "logiciels", "tests". | **Exemple** : "Outils référencés : Wave (extension navigateur), Axe DevTools (intégré CI), Color Contrast Analyzer (design), validateur W3C (HTML/CSS)." | Facile | 10 min |
| 15 | Procédure d'appel à expertise externe et budget associé | span-sircom | §3.3 Moyens + §5 Audits | Synthèse | Extraire budget audits externes + procédure appel (marché, prestataires référencés). | **Exemple** : "Procédure audits externes : marché à bons de commande avec 3 prestataires référencés (AccesSite, Temesis, Koena). Budget 2025 : 35 k€ (5 audits complets)." | Moyen | 15 min |

**Sous-total Catégorie 2** : 10/12 mappables, 2 TODO (points 10, 12 possibles), ~2h30

---

#### Catégorie 3 - Conception accessible (8 points, ~1h30)

| # | Libellé DINUM | Source | Section | Type | Instructions | Exemple | Difficulté | Temps |
|---|---------------|--------|---------|------|--------------|---------|------------|-------|
| 16 | Processus internes documentés (intégration accessibilité) | span-sircom | §6 Processus p.8 | Synthèse | Chercher "processus", "workflow", "intégration RGAA". Décrire en 2-3 phrases comment accessibilité intégrée dans cycle projet. | **Exemple** : "Processus documenté : checkpoint accessibilité obligatoire à chaque phase (cahier des charges, maquettes, recette). Fiche réflexe RGAA disponible sur intranet projet." | Moyen | 15 min |
| 17 | Modalités de contrôle périodique définies | span-sircom | §5 Plan + §7 Suivi | Synthèse | Extraire fréquence contrôles (mensuel, trimestriel, annuel) et responsable. | **Exemple** : "Contrôles périodiques : audit léger interne trimestriel (référent), audit complet externe annuel (prestataire), comité pilotage accessibilité semestriel." | Moyen | 15 min |
| 18 | Process de traitement des demandes usagers (accès/retour) | span-sircom | §8 Médiation p.9 | Citation/Synthèse | Chercher "contact accessibilité", "demande usager", "médiation", "email". Décrire canal + délai réponse. | **Exemple** : "Process demandes usagers : email accessibilite.communication@finances.gouv.fr (délai réponse 5 jours ouvrés). Médiation Défenseur des Droits mentionnée déclaration accessibilité." | Facile | 10 min |
| 19 | Clauses accessibilité dans marchés/commandes | span-sircom | §9 Marchés p.10 | Validation | Chercher "clause RGAA", "CCTP", "cahier des charges". Oui/Non + type clause (conformité obligatoire, pénalités). | **Exemple** : "Clauses accessibilité : obligatoires dans tous CCTP depuis 2023. Exigence conformité RGAA 4.1 niveau AA + livraison rapport accessibilité prestataire." | Moyen | 15 min |
| 20 | Critères de sélection/pondération incluant accessibilité | span-sircom | §9 Marchés | Extraction | Chercher "critères évaluation", "pondération", "notation". Extraire % ou points attribués accessibilité. Fallback : **→ S4-01** Préciser si absent | **Exemple** : "Critères sélection : accessibilité pondérée 15% note technique. Prestataires notés sur : expérience RGAA (5%), méthodologie tests (5%), livrables accessibilité (5%)." | Difficile | 15 min |
| 21 | Exigence de livrables conformes et preuves de conformité | span-sircom | §9 Marchés | Synthèse | Lister livrables obligatoires : rapport audit, grille RGAA, déclaration. | **Exemple** : "Livrables obligatoires : rapport audit RGAA complet, grille 106 critères, déclaration accessibilité pré-remplie, fichiers sources (HTML/CSS) validés W3C." | Facile | 10 min |
| 22 | Accessibilité intégrée dès la conception (projets neufs) | span-sircom | §6 Processus + §10 Projets | Validation | Chercher "design accessible", "maquettes", "phase conception". Oui/Non + modalités (checklist design, revue UX). | **Exemple** : "Accessibilité dès conception : checklist UX obligatoire phase maquettage (contraste, zones cliquables, navigation clavier). Revue référent avant développement." | Moyen | 10 min |
| 23 | Tests incluant des personnes handicapées | span-sircom | §10 Tests utilisateurs | Validation | Chercher "tests usagers", "personnes handicapées", "utilisateurs". Oui/Non + fréquence. Fallback : **→ S4-01** Planifier si absent | **Exemple** : "Tests utilisateurs : 2 sessions annuelles avec panel 5 personnes (déficients visuels, mobilité réduite, cognitifs). Partenariat association Valentin Haüy." | Difficile | 15 min |

**Sous-total Catégorie 3** : 6/8 mappables, 2 TODO (points 20, 23 possibles), ~1h30

---

#### Catégorie 4 - Suivi et amélioration (3 points, ~30 min)

| # | Libellé DINUM | Source | Section | Type | Instructions | Exemple | Difficulté | Temps |
|---|---------------|--------|---------|------|--------------|---------|------------|-------|
| 24 | Évaluations/audits planifiés pour tous les services | span-sircom | §5 Plan annuel + Annexe 1 | Tableau | Créer planning audits 2025-2027 par site/service. Colonnes : Service | Type audit | Date | Prestataire. | **Exemple tableau** :<br>Site finances.gouv.fr : Audit complet (T2 2025, AccesSite)<br>Intranet SG : Audit simplifié (T4 2025, interne)<br>Portail agents : Audit complet (T1 2026, Temesis) | Moyen | 15 min |
| 25 | Calendrier de corrections priorisé sur usages/volumétrie | span-sircom | §5 Plan + §11 Priorisation | Synthèse | Extraire critères priorisation (audience, criticité) + planning corrections. Format : "Priorisation selon [critères]. Corrections : critiques <3 mois, majeures <6 mois." | **Exemple** : "Priorisation selon matrice : audience × criticité RGAA. Services >10k usagers/mois = priorité 1. Planning : bloquants <1 mois, critiques <3 mois, majeurs <6 mois, mineurs <12 mois." | Moyen | 10 min |
| 26 | Suivi de couverture (audités vs total) et périodicité des évaluations | span-sircom | §5 Plan + Annexe 1 | Calcul | Calculer taux couverture : (sites audités / sites total) × 100. Préciser périodicité (ex: audit complet tous les 3 ans). | **Exemple** : "Couverture 2025 : 5/7 sites audités (71%). Périodicité : audit complet tous les 3 ans, contrôle léger annuel pour sites critiques." | Facile | 5 min |

**Sous-total Catégorie 4** : 3/3 mappables, 0 TODO, ~30 min

---

#### Catégorie 5 - Audits et conformité (5 points, ~45 min)

| # | Libellé DINUM | Source | Section | Type | Instructions | Exemple | Difficulté | Temps |
|---|---------------|--------|---------|------|--------------|---------|------------|-------|
| 27 | Accès LSF/vidéo pour contenus concernés | span-sircom | §12 Contenus spécifiques | Validation | Chercher "LSF", "langue des signes", "vidéo", "sous-titres". Oui/Non + périmètre (vidéos institutionnelles, webinaires). Fallback : **→ S4-01** Définir périmètre si absent | **Exemple** : "LSF/vidéo : sous-titres obligatoires pour toutes vidéos institutionnelles. LSF prévu pour vidéos >5 min ou contenu essentiel (ex: allocutions ministre). Périmètre 2025 : 8 vidéos prioritaires." | Difficile | 15 min |
| 28 | Traduction FALC pour contenus concernés | span-sircom | §12 Contenus spécifiques | Validation | Chercher "FALC", "facile à lire", "simplifié". Oui/Non + contenus concernés (démarches essentielles). Fallback : **→ S4-01** Identifier contenus prioritaires | **Exemple** : "FALC : traduction prévue pour 3 démarches essentielles (demande aide sociale, inscription concours, réclamation). Partenariat UNAPEI pour validation FALC." | Difficile | 15 min |
| 29 | Prise en compte de critères AAA pertinents | span-sircom | §13 Niveau conformité | Validation | Chercher "niveau AAA", "au-delà AA", "bonnes pratiques". Lister critères AAA appliqués. Fallback : Réponse "Non, niveau AA cible" acceptable | **Exemple** : "Critères AAA appliqués : contraste renforcé 7:1 pour texte important, liens externes explicites, pas de limite temps stricte. Approche pragmatique au-delà AA." | Moyen | 10 min |
| 30 | Bilan annuel réalisé et publié | span-sircom | §14 Reporting | Validation | Chercher "bilan annuel", "rapport", "publication". Oui/Non + URL ou modalité publication. | **Exemple** : "Bilan annuel publié sur finances.gouv.fr/accessibilite/bilan-2024. Format PDF accessible. Contenu : audits réalisés, taux conformité, formations, budget consommé, actions 2025." | Facile | 5 min |
| 31 | Plan d'action annuel publié (format accessible) | span-sircom | §5 Plan annuel + §14 | Validation | Vérifier publication plan annuel. URL + format (PDF accessible, HTML). Peut être intégré au bilan (point 30). | **Exemple** : "Plan d'action annuel publié : finances.gouv.fr/accessibilite/plan-action-2025 (HTML + PDF/UA). Mise à jour trimestrielle statuts actions." | Facile | 5 min |

**Sous-total Catégorie 5** : 3/5 mappables, 2 TODO (points 27, 28 possibles), ~45 min

---

**🎯 TOTAL SIRCOM : 25/31 mappables, 6 TODO S4-01, ~4h30**

---

### Étape 2 : Tables de correspondance SNUM (priorité 2, ~3h)

**Instructions adaptées** :
- Suivre la même méthodologie que SIRCOM ci-dessus
- Source : `span/span-portail-pro.sg.md` (106 lignes, document plus court)
- Logique identique mais moins de détails → plus de TODO probables
- Référencer les exemples SIRCOM pour format réponse

**Instructions préliminaires** :
- Lire `span/span-portail-pro.sg.md` intégralement (10 min)
- Identifier structure : Portailpro.gouv, Mission France Recouvrement, coordinateur RGAA
- Préparer fichier `docs/modules/snum.md` pour édition

---

#### Catégorie 1 - Politique accessibilité (3 points, ~25 min)

| # | Libellé DINUM | Source SNUM | Instructions (référence SIRCOM) | Temps |
|---|---------------|-------------|--------------------------------|-------|
| 1 | Stratégie numérique intégrée | span-portail §1 Engagement | **Voir SIRCOM 1** : Copier §1 politique accessibilité Portailpro.gouv | 5 min |
| 2 | Politique inclusion formalisée | span-portail ou N/A | **Voir SIRCOM 2** : Chercher mention politique RH inclusion. Fallback : **→ S4-01** Documenter si absent (probable) | 10 min |
| 3 | Objectifs mesurables (KPI) | span-portail §4 Plan annuel | **Voir SIRCOM 3** : Extraire KPI chiffrés (taux conformité, audits, formations). Peut être moins détaillé que SIRCOM. | 10 min |

**Sous-total Catégorie 1** : 2/3 mappables, 1 TODO probable (point 2)

---

#### Catégorie 2 - Ressources (12 points, ~2h)

| # | Libellé DINUM | Source SNUM | Instructions (référence SIRCOM) | Temps |
|---|---------------|-------------|--------------------------------|-------|
| 4 | Référent désigné | span-portail §2 Coordinateur | **Voir SIRCOM 4** : Copier identité coordinateur RGAA + rattachement Mission France Recouvrement | 5 min |
| 5 | Temps alloué référent | span-portail §2 | **Voir SIRCOM 5** : Extraire % ETP coordinateur. Fallback : **→ S4-01** Préciser si absent | 10 min |
| 6 | RH dédiées (ETP) | span-portail §2-3 | **Voir SIRCOM 6** : Lister équipe accessibilité (coordinateur + support technique) | 15 min |
| 7 | Budget annuel | span-portail §3 Moyens ou N/A | **Voir SIRCOM 7** : Chercher budget. **→ S4-01** Probable TODO (document court, info souvent absente) | 15 min |
| 8 | Planification pluriannuelle | span-portail §4 Plan 2025-2027 | **Voir SIRCOM 8** : Synthétiser plan 3 ans (budget/ETP si précisé) | 15 min |
| 9 | Compétences fiches de poste | span-portail ou N/A | **Voir SIRCOM 9** : Chercher mention compétences RGAA dans profils. **→ S4-01** Probable TODO | 10 min |
| 10 | Grille recrutement | N/A probable | **Voir SIRCOM 10** : **→ S4-01** TODO attendu (rarement dans SPAN sources) | 5 min |
| 11 | Plan formation annuel | span-portail §5 Formation | **Voir SIRCOM 11** : Lister formations prévues 2025 (public + dates) | 10 min |
| 12 | Sensibilisation large | span-portail §5 ou N/A | **Voir SIRCOM 12** : Chercher sensibilisation tous agents. **→ S4-01** Probable TODO | 10 min |
| 13 | Formations par rôle | span-portail §5 Formation | **Voir SIRCOM 13** : Tableau formations par rôle (dev, éditorial, etc.) | 15 min |
| 14 | Outils de test référencés | span-portail §6 Outils ou N/A | **Voir SIRCOM 14** : Lister outils utilisés. Fallback : **→ S4-01** Documenter si absent | 10 min |
| 15 | Procédure expertise externe | span-portail §3 + §4 Audits | **Voir SIRCOM 15** : Extraire budget audits + procédure appel prestataires | 15 min |

**Sous-total Catégorie 2** : 7/12 mappables, 5 TODO probables (points 7, 9, 10, 12, 14)

---

#### Catégorie 3 - Conception accessible (8 points, ~1h15)

| # | Libellé DINUM | Source SNUM | Instructions (référence SIRCOM) | Temps |
|---|---------------|-------------|--------------------------------|-------|
| 16 | Processus documentés | span-portail §7 Processus | **Voir SIRCOM 16** : Décrire intégration accessibilité cycle projet | 15 min |
| 17 | Contrôle périodique | span-portail §4 Plan + §8 Suivi | **Voir SIRCOM 17** : Fréquence contrôles + responsable | 10 min |
| 18 | Process demandes usagers | span-portail §9 Contact | **Voir SIRCOM 18** : Email contact + délai réponse. Contact : mfr.rgaa@finances.gouv.fr | 10 min |
| 19 | Clauses marchés | span-portail §10 Marchés | **Voir SIRCOM 19** : Validation clauses RGAA dans CCTP | 15 min |
| 20 | Critères sélection | span-portail §10 ou N/A | **Voir SIRCOM 20** : Pondération accessibilité. **→ S4-01** Probable TODO | 10 min |
| 21 | Livrables conformes | span-portail §10 Marchés | **Voir SIRCOM 21** : Lister livrables obligatoires (rapport, grille, déclaration) | 10 min |
| 22 | Accessibilité dès conception | span-portail §7 Processus | **Voir SIRCOM 22** : Validation checkpoint design accessible | 10 min |
| 23 | Tests personnes handicapées | span-portail §11 Tests ou N/A | **Voir SIRCOM 23** : Tests usagers. **→ S4-01** Probable TODO | 10 min |

**Sous-total Catégorie 3** : 6/8 mappables, 2 TODO probables (points 20, 23)

---

#### Catégorie 4 - Suivi et amélioration (3 points, ~25 min)

| # | Libellé DINUM | Source SNUM | Instructions (référence SIRCOM) | Temps |
|---|---------------|-------------|--------------------------------|-------|
| 24 | Audits planifiés tous services | span-portail §4 Plan annuel | **Voir SIRCOM 24** : Planning audits 2025-2027 pour Portailpro.gouv (peut être 1 seul site) | 10 min |
| 25 | Calendrier corrections priorisé | span-portail §4 Plan + §12 Priorisation | **Voir SIRCOM 25** : Critères priorisation + délais corrections par criticité | 10 min |
| 26 | Suivi couverture audits | span-portail §4 | **Voir SIRCOM 26** : Taux couverture + périodicité (peut être 1/1 = 100% si 1 seul site) | 5 min |

**Sous-total Catégorie 4** : 3/3 mappables, 0 TODO

---

#### Catégorie 5 - Audits et conformité (5 points, ~35 min)

| # | Libellé DINUM | Source SNUM | Instructions (référence SIRCOM) | Temps |
|---|---------------|-------------|--------------------------------|-------|
| 27 | Accès LSF/vidéo | span-portail §13 Contenus ou N/A | **Voir SIRCOM 27** : LSF pour vidéos. **→ S4-01** Probable TODO (contenu technique, peu vidéo Portailpro?) | 10 min |
| 28 | Traduction FALC | span-portail §13 ou N/A | **Voir SIRCOM 28** : FALC démarches essentielles. **→ S4-01** Probable TODO | 10 min |
| 29 | Critères AAA pertinents | span-portail §14 Niveau | **Voir SIRCOM 29** : Critères AAA appliqués au-delà AA. Fallback : "Non, AA cible" acceptable | 5 min |
| 30 | Bilan annuel publié | span-portail §15 Reporting | **Voir SIRCOM 30** : URL bilan annuel + format accessible | 5 min |
| 31 | Plan annuel publié | span-portail §4 Plan + §15 | **Voir SIRCOM 31** : URL plan action annuel (HTML + PDF/UA) | 5 min |

**Sous-total Catégorie 5** : 3/5 mappables, 2 TODO probables (points 27, 28)

---

**🎯 TOTAL SNUM : 21/31 mappables, 10 TODO S4-01, ~3h**

---

## Critères d'acceptation

### Livrables
- [ ] `roadmap/S4-00-mapping-contenus.md` créé (~2500 lignes)
- [ ] Branche `feature/s4-00-mapping-guide` créée
- [ ] Commit avec message BMAD standard

### Contenu (qualité guide)
- [ ] Tables SIRCOM complètes (31 points, 5 catégories)
- [ ] Tables SNUM complètes (31 points, références SIRCOM)
- [ ] 17 exemples pré-rédigés fournis (Catégorie 1-2 SIRCOM + points difficiles)
- [ ] Récapitulatif priorisation en annexe
- [ ] TODO S4-01 tracés (16 identifiés : 6 SIRCOM + 10 SNUM)

### Validation technique
- [ ] 62 lignes tableau minimum (31×2, aucun point DINUM oublié)
- [ ] Markdown valide (pas de tableau cassé)
- [ ] Instructions cohérentes avec méthodologie (guidées + exemples)
- [ ] Temps estimés réalistes par point

---

## Dépendances

**Bloque** : S4-01 (review Bertrand/Alexandra utilise ce guide pour exécution mapping)

**Dépend de** :
- Sources SPAN présentes et lisibles
- Décisions stratégiques S4 finalisées (validation_status, disclaimers, workflow Stéphane)

---

## Références

- **Sources** : `span/span-sircom-sg.md` (414 lignes), `span/span-portail-pro.sg.md` (106 lignes)
- **Template** : `docs/modules/_template.md` (31 points DINUM officiels lignes 36-66)
- **Checklist DINUM** : [Accessibilité numérique - Référentiel général](https://www.numerique.gouv.fr/publications/rgaa-accessibilite/)
- **CLAUDE.md** : Section "Architecture technique" → "Pipeline de scoring (31 points DINUM)"

---

## Notes et risques

### Nature stratégique des sources SPAN

**Risque** : Les documents SPAN sont des politiques stratégiques, PAS des réponses directes aux 31 points DINUM.
- Certains points nécessitent synthèse de plusieurs sections
- D'autres peuvent être totalement absents (ex: grille recrutement, tests utilisateurs)
- Interprétation requise → risque d'écart par rapport à réalité terrain

**Mitigation** : TODO S4-01 explicites permettent traçabilité des gaps. Review Bertrand/Alexandra en S4-01 validera ou complétera via sources complémentaires (entretiens référents, documents RH, etc.).

### Équilibre guidage vs autonomie

Les instructions sont détaillées mais Bertrand/Alexandra sont autonomes. Si instructions trop lourdes, elles peuvent être allégées lors exécution (pragmatisme).

### Durée réelle vs estimation

Estimation 4h30 SIRCOM + 3h SNUM = 7h30 total. Peut varier selon :
- Complexité réelle des sources (paragraphes longs à synthétiser)
- Blocages sur points ambigus
- Qualité rédactionnelle souhaitée (synthèse rapide vs rédaction soignée)

Buffer : prévoir 8-9h au lieu de 7h30 pour confort.

### Scope SNUM = Portailpro.gouv

Le fichier source `span-portail-pro.sg.md` couvre **Portailpro.gouv** (Mission France Recouvrement), pas l'ensemble du service SNUM.

**Clarification** : Le module `snum.md` sera donc spécifique à Portailpro.gouv. Si d'autres applications SNUM doivent être intégrées ultérieurement (ex: autres services SNUM), prévoir Phase 2.

**Alternative** : Renommer module `snum.md` en `snum-portailpro.md` pour précision ? À valider en S4-01.

---

## Annexes

### Récapitulatif priorisation (Quick wins)

**SIRCOM - Points faciles (<10 min)** :
- 1.1 Stratégie publiée : citation directe (5 min)
- 4 Référent désigné : copie identité (5 min)
- 11 Plan formation : liste formations (10 min)
- 14 Outils test : liste outils (10 min)
- 18 Process demandes usagers : email + délai (10 min)
- 21 Livrables conformes : liste documents (10 min)
- 26 Suivi couverture : calcul taux (5 min)
- 30 Bilan annuel : URL publication (5 min)
- 31 Plan annuel publié : URL plan (5 min)

**Total quick wins SIRCOM** : 9 points, ~1h

**SIRCOM - Points moyens (10-20 min)** :
- 2, 3, 5, 6, 8, 9, 12, 13, 16, 17, 19, 22, 24, 25, 29

**Total moyens SIRCOM** : 15 points, ~2h30

**SIRCOM - Points difficiles (>20 min)** :
- 7 Budget annuel : recherche montant (20 min)
- 10 Grille recrutement : TODO probable (10 min)
- 15 Expertise externe : budget + procédure (15 min)
- 20 Critères sélection : pondération (15 min)
- 23 Tests utilisateurs : TODO probable (15 min)
- 27 LSF/vidéo : TODO probable (15 min)
- 28 FALC : TODO probable (15 min)

**Total difficiles SIRCOM** : 7 points, ~1h45

---

### TODO S4-01 prévisionnels (16 points identifiés)

**SIRCOM (6 TODO possibles)** :
- 5 Temps référent : Préciser % ETP si non mentionné source
- 7 Budget annuel : Demander montant si non précisé
- 10 Grille recrutement : Documenter avec RH (souvent absent SPAN)
- 20 Critères sélection marchés : Préciser pondération si absente
- 23 Tests utilisateurs handicapés : Planifier si absent source
- 27 Accès LSF : Définir périmètre vidéos si non précisé
- 28 FALC : Identifier contenus prioritaires si non mentionné

**SNUM (10 TODO probables)** :
- 2 Politique inclusion : Documenter si absent (probable)
- 5 Temps référent : Préciser % ETP
- 7 Budget annuel : Probable TODO (doc court)
- 9 Compétences fiches poste : Probable TODO
- 10 Grille recrutement : TODO attendu
- 12 Sensibilisation large : Probable TODO
- 14 Outils test : Documenter si absent
- 20 Critères sélection : Probable TODO
- 23 Tests utilisateurs : Probable TODO
- 27 LSF : Probable TODO (peu vidéo Portailpro)
- 28 FALC : Probable TODO

**Ces TODO deviendront la checklist de S4-01 Phase 1-2 (finaliser SIRCOM/SNUM).**

---

*Dernière mise à jour : 2025-10-02*
