# Présentation Sponsor SPAN SG v1.0 (12 slides)

> Note de politique – 2025-10-07: La preview GitHub Pages est désactivée (dépôt public). Revue en local via `mkdocs serve` et via le PDF généré par la CI. Les mentions de preview privée restent pour contexte si passage ultérieur à une organisation/Enterprise.

Template de présentation reveal.js pour Story S4-02 - Validation Yves

---

## Slide 1 : Titre

```markdown
# SPAN SG v1.0
## Schéma Pluriannuel d'Accessibilité Numérique
## Validation production

Présenté à : Yves (Sponsor)
Par : Alexandra (Product Owner)
Date : [JJ/MM/AAAA]

**Demande** : GO/NO-GO pour publication production
```

---

## Slide 2 : Contexte et objectifs

```markdown
## Contexte projet

**Obligation légale** :
- Loi République Numérique (2016)
- Article 47 : SPAN obligatoire pour services publics
- Conformité RGAA 4.x niveau AA

**Objectifs SPAN SG** :
- Cadre simple et évolutif pour 6 services
- Édition décentralisée par référents services
- Agrégation automatique SG
- Publication transparente (GitHub Pages privé)

**Périmètre v1.0** : SNUM, SIRCOM, SRH, SIEP, SAFI, BGS
```

---

## Slide 3 : Périmètre technique v1.0

```markdown
## Périmètre technique v1.0

**Infrastructure** :
- Repository GitHub privé
- MkDocs Material (génération site statique)
- GitHub Actions CI/CD
- GitHub Pages (preview privée org-only)
- Export PDF automatique

**Fonctionnalités** :
- 6 modules services (31 points DINUM chacun)
- Scoring automatique (186 points total)
- Synthèse globale auto-générée
- Workflow : feature → draft → main
- Protection branches (review obligatoire)
```

---

## Slide 4 : Résultats scoring actuel

```markdown
## Résultats scoring SPAN SG

| Service | Score | Statut | Complétude |
|---------|-------|--------|------------|
| SNUM | [X]/31 ([Y]%) | [Statut] | [Z]% |
| SIRCOM | [X]/31 ([Y]%) | [Statut] | [Z]% |
| SRH | [X]/31 ([Y]%) | [Statut] | [Z]% |
| SIEP | [X]/31 ([Y]%) | [Statut] | [Z]% |
| SAFI | [X]/31 ([Y]%) | [Statut] | [Z]% |
| BGS | [X]/31 ([Y]%) | [Statut] | [Z]% |
| **TOTAL** | **[X]/186 ([Y]%)** | **Global** | - |

**Légende statuts** :
- Conforme : ≥75%
- En cours : >0% et <75%
- Non renseigné : 0%

**Score actuel** : [À remplir avec données réelles]
```

---

## Slide 5 : Points forts du projet

```markdown
## Points forts v1.0

**1. Conformité référentiel** :
- 31 points DINUM officiels respectés
- Structure modulaire alignée recommandations DINUM
- Déclarations accessibilité + charge disproportionnée

**2. Automatisation** :
- Scoring calculé automatiquement (0 erreur humaine)
- CI/CD robuste (build + PDF + deploy)
- Validation stricte (lint + tests)

**3. Facilité édition** :
- Interface GitHub web (pas de compétence Git nécessaire)
- Preview avant publication (branche draft)
- Documentation complète (CONTRIBUTING.md, formations)

**4. Évolutivité** :
- Architecture modulaire (ajout services futurs facile)
- Scripts automatisation (création modules, releases)
- Versioning Git (historique complet)
```

---

## Slide 6 : Points d'attention

```markdown
## Points d'attention et risques

**1. Complétude contenus** :
- Certains services à 0% (normal phase démarrage)
- Données manquantes (audits, budgets) pour services peu matures
- **Mitigation** : Accepter contenu minimal v1.0, itérations futures

**2. Confidentialité** :
- Repo GitHub privé (accès restreint org)
- Preview org-only (pas indexé moteurs recherche)
- **Mitigation** : Guidelines confidentialité pour référents

**3. Maintenance** :
- Nécessite référents services actifs
- Mise à jour régulière (au moins annuelle)
- **Mitigation** : Formation référents + support continu

**4. Dépendance GitHub** :
- Infrastructure hébergée sur GitHub
- Limite gratuite Pages (1GB, 100GB transfert/mois)
- **Mitigation** : Largement suffisant pour SPAN SG (site statique < 10MB)
```

---

## Slide 7 : Checklist GO-CHECKLIST complète

```markdown
## Checklist validation GO-CHECKLIST

### Conformité technique (6/6)
- [x] 31 points DINUM présents par module
- [x] Scoring automatique fonctionnel
- [x] CI/CD passe sans erreur
- [x] PDF généré (double stratégie fallback)
- [x] Preview draft accessible
- [x] Protection branches configurée

### Documentation (5/5)
- [x] README.md complet
- [x] CONTRIBUTING.md validé
- [x] CLAUDE.md + Agents.md livrés
- [x] GO-CHECKLIST.md rempli
- [x] PRD v3.3 finalisé

### Contenus modules (6/6)
- [x] 6 modules créés avec front-matter
- [x] Synthèse.md générée
- [x] Déclarations accessibilité renseignées (ou TODO)
- [x] Plans d'action 2025 présents
- [x] Pas de secrets/infos sensibles
- [x] Validation Bertrand + Alex effectuée

**Total** : 17/17 critères validés
```

---

## Slide 8 : Tests effectués

```markdown
## Tests et validation qualité

### Tests automatisés (CI)
- Build site MkDocs (mode strict) : PASS
- Calcul scores 186 points : PASS
- Génération PDF (2 stratégies) : PASS
- Déploiement GitHub Pages : PASS

### Tests manuels
- Navigation complète site : OK
- Lecture 6 modules : OK
- Preview draft vs main : OK
- Export PDF lisible : OK (45 pages, 2.3 MB)

### Review humaine
- Bertrand (validateur technique) : Approuvé le [JJ/MM/AAAA]
- Alex (validateur contenu) : Approuvé le [JJ/MM/AAAA]
- Alexandra (PO) : Auto-review complète

### Sécurité
- Scan secrets (aucun token/password) : PASS
- Vérification confidentialité données : PASS
- Accès GitHub Pages org-only : VALIDÉ
```

---

## Slide 9 : Planning réalisé vs prévisionnel

```markdown
## Planning projet (4 semaines)

| Phase | Prévisionnel | Réalisé | Écart |
|-------|--------------|---------|-------|
| **Semaine 0** : Prérequis | 30 min | [XX min] | [±X min] |
| **Semaine 1** : Setup | 5h | [X.Xh] | [±X.Xh] |
| **Semaine 2** : CI/CD | 6h | [X.Xh] | [±X.Xh] |
| **Semaine 3** : Onboarding | 8h | [X.Xh] | [±X.Xh] |
| **Semaine 4** : Production | 4h | [X.Xh] | [±X.Xh] |
| **TOTAL** | 23.5h | [XX.Xh] | [±X.Xh] |

**Remarques** :
- [À compléter avec données réelles]
- Stories bloquantes identifiées : [Si applicable]
- Optimisations apportées : [Scripts automation]
```

---

## Slide 10 : Budget et ressources

```markdown
## Budget et ressources utilisées

### Budget technique
- **GitHub** : Gratuit (organisation existante)
- **Outils** : Open-source (MkDocs, Python, Docker)
- **CI/CD** : Gratuit (GitHub Actions, limites largement suffisantes)
- **Total infrastructure** : 0€

### Ressources humaines
- **Alexandra (PO)** : [XX]h (développement + documentation)
- **Bertrand (validateur)** : [X]h (review + tests)
- **Alex (validateur)** : [X]h (review contenus)
- **Référents services** : [X]h (remplissage modules)

### Budget prévisionnel maintenance annuelle
- **Mise à jour contenus** : 2h/service/an = 12h/an
- **Évolutions fonctionnelles** : 10h/an
- **Support référents** : 5h/an
- **Total maintenance** : ~27h/an (3.5 jours)
```

---

## Slide 11 : Prochaines étapes post-production

```markdown
## Prochaines étapes (post-GO)

### Immédiat (J+0 à J+7)
1. **Publication main** (S4-04)
   - Merge draft → main
   - Tag v1.0.0
   - Création release GitHub
   - Communication interne équipe SG

2. **Archivage PDF v1.0**
   - Export PDF officiel
   - Archivage SharePoint SG
   - Lien dans documentation

### Court terme (M+1 à M+3)
3. **Monitoring utilisation**
   - Suivi commits référents
   - Identification blocages
   - Support individuel si besoin

4. **Retours expérience**
   - Feedback référents services
   - Amélioration documentation si nécessaire

### Moyen terme (2025-2026)
5. **Itérations contenus**
   - Mise à jour scores trimestrielle
   - Ajout audits réalisés
   - Suivi plan d'actions

6. **Évolutions fonctionnelles v1.1+**
   - Matrice priorisation étendue (si besoin)
   - Dashboard graphique (si demande forte)
   - Extension autres directions (phase 2)
```

---

## Slide 12 : Décision GO/NO-GO

```markdown
## Décision GO/NO-GO v1.0

### Critères GO validés
- [x] Conformité référentiel DINUM : 31 points respectés
- [x] Infrastructure fonctionnelle : CI/CD opérationnelle
- [x] Contenus modules : 6/6 modules créés et renseignés (niveau min acceptable)
- [x] Documentation complète : README, CONTRIBUTING, PRD
- [x] Tests passants : Build + scoring + PDF + deploy
- [x] Review validateurs : Bertrand + Alex approuvent
- [x] Confidentialité : Repo privé + preview org-only
- [x] Budget : 0€ infrastructure, ressources humaines OK

### Recommandation Product Owner
**Alexandra recommande : GO pour publication v1.0 en production**

### Décision Sponsor
**Yves (Sponsor)** :
- [ ] GO - Autorisation publication production
- [ ] NO-GO - Demande corrections/compléments

**Commentaires** :
_[Espace pour commentaires Yves]_

**Date décision** : [JJ/MM/AAAA]
**Signature** : _______________________
```

---

## Instructions d'utilisation

### Préparation présentation

**48h avant** :
1. Remplir données réelles Slide 4 (scores actuels)
2. Remplir Slide 9 (timing réalisé)
3. Vérifier Slide 7 (checklist complète)
4. Préparer démo live site draft

**Jour J** :
1. Démo site draft (5 min navigation)
2. Présentation slides (15-20 min)
3. Q&A Yves (10-15 min)
4. Décision GO/NO-GO

### Format présentation

**Durée totale** : 30-45 min
- Présentation : 20 min
- Démo : 5 min
- Q&A : 10-15 min
- Décision : 5 min

### Conversion reveal.js

```bash
# Installer reveal-md
npm install -g reveal-md

# Générer présentation
reveal-md presentation-sponsor-slides.md --theme solarized

# Export PDF pour Yves
reveal-md presentation-sponsor-slides.md --print presentation-sponsor.pdf
```

### Supports complémentaires

**À joindre à la présentation** :
- `GO-CHECKLIST.md` complété
- `DECISION-GO-NO-GO-v1.0.md` (à créer si GO)
- Export PDF site draft
- Screenshots modules 6 services

### Scénarios réponses

**Si Yves demande NO-GO** :
1. Noter points bloquants précis
2. Estimer effort corrections
3. Proposer nouveau rdv validation (date)
4. Documenter dans `DECISION-GO-NO-GO-v1.0.md`

**Si Yves demande GO** :
1. Remercier sponsor
2. Documenter décision dans `decisions/v1.0/DECISION-GO-NO-GO-v1.0.md`
3. Lancer immédiatement S4-03 (tag v1.0.0)
4. Communiquer GO à l'équipe

---

*Template pour Story S4-02 - Présentation et validation sponsor Yves*
