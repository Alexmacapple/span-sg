---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S4-02 : Validation Yves (sponsor)

**Phase** : Semaine 4 - Production
**Priorité** : Critique (bloquante pour release)
**Estimation** : 1h (présentation) + délai décision
**Assigné** : Alexandra (présentation) + Yves (validation)

---

## Contexte projet

Yves est le **sponsor** du projet SPAN SG. Son rôle :
- Validation stratégique (pas technique)
- GO/NO-GO pour bascule en production
- Représentation auprès de la direction
- Arbitrage si blocages majeurs

**Important** : Yves valide uniquement pour le **passage en production**. Il n'intervient pas sur les revues techniques (rôle de Bertrand/Alex).

Cette story consiste à présenter le SPAN SG v1.0 à Yves, recueillir son feedback, obtenir son GO formel, et documenter la décision.

---

## Objectif

Organiser une session de présentation avec Yves, démontrer la valeur du SPAN SG, obtenir sa validation formelle, et documenter la décision GO/NO-GO.

---

## Prérequis

- [ ] Story S4-01 complétée (reviews validées par Bertrand/Alex)
- [ ] Branche `draft` stable et prête
- [ ] Preview draft accessible pour démonstration
- [ ] PDF synthèse disponible (artefact CI)
- [ ] Slides présentation préparés

---

## Étapes d'implémentation

### 1. Préparer les livrables pour la présentation

**Livrable 1 : Slides de présentation (10-15 slides max)**

Structure recommandée :
```markdown
Slide 1 : Titre
- SPAN SG v1.0
- Présentation validation production
- Date, Alexandra

Slide 2 : Rappel objectifs
- Framework modulaire pour SPAN SG
- 6 services v1 (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- Scoring automatique 31 points DINUM
- Export HTML + PDF

Slide 3 : État d'avancement
- ✅ 6 modules créés et renseignés
- ✅ CI/CD opérationnelle
- ✅ Preview privée accessible
- ✅ Reviews techniques validées (Bertrand/Alex)

Slide 4 : Score global
[Graphique ou tableau]
- Score actuel : X/186 (Y%)
- Répartition par service
- Évolution depuis début projet

Slide 5-10 : Highlights par module
- 1 slide par service (ou regrouper 2x2)
- Périmètre, actions prioritaires 2025, score

Slide 11 : Conformité légale
- Déclarations accessibilité : 6/6 renseignées
- Analyse charge disproportionnée : X services concernés
- Respect RGAA et référentiel DINUM

Slide 12 : Bénéfices attendus
- Visibilité globale accessibilité SG
- Pilotage par données (scoring)
- Responsabilisation services
- Conformité réglementaire

Slide 13 : Prochaines étapes (post-GO)
- Tag v1.0.0
- Publication production (main)
- Communication interne
- Roadmap v1.1+ (si applicable)

Slide 14 : Décision demandée
🔴 Validation GO/NO-GO pour passage en production

Slide 15 : Contacts et questions
```

**Livrable 2 : PDF synthèse SPAN**
- Récupérer depuis artefacts CI (S2-02)
- Imprimer si besoin (version papier pour Yves)

**Livrable 3 : Accès preview**
- URL : https://[preview-url]/draft/
- Identifiants si nécessaire (GitHub org-only)

### 2. Planifier la session avec Yves

**Invitation** :
```
📧 À : Yves
CC : Alexandra, Bertrand, Alex
Objet : SPAN SG v1.0 - Validation pour production

Bonjour Yves,

Le SPAN SG v1.0 est prêt pour validation finale avant passage en production.

**Session de présentation**
- Date : [JJ/MM/AAAA], [HH:MM]
- Durée : 1h max
- Lieu : [Salle de réunion] ou [Lien visio]
- Participants : Toi (sponsor), Alexandra (PM), Bertrand et Alex (validateurs techniques)

**Objectif** : Présenter l'état d'avancement, démontrer la solution, et obtenir ton GO/NO-GO pour bascule en production.

**Préparation** (optionnel) :
- Preview : https://[URL] (accès org-only)
- PDF synthèse : [lien]

À bientôt,
Alexandra
```

**Format recommandé** :
- Présentiel si possible (meilleur engagement)
- Sinon visio avec partage d'écran
- Enregistrer (avec accord Yves) pour trace

### 3. Dérouler la présentation

**Timing détaillé** :
```
00:00-00:05 : Accueil + contexte (slides 1-2)
00:05-00:15 : État d'avancement (slides 3-4)
00:15-00:35 : Tour des 6 modules (slides 5-10, 3 min/module)
00:35-00:45 : Conformité + bénéfices (slides 11-12)
00:45-00:50 : Prochaines étapes (slide 13)
00:50-00:55 : Décision GO/NO-GO (slide 14)
00:55-01:00 : Questions + clôture
```

**Tips présentation** :
- Adapter niveau de détail selon intérêt Yves
- Focus stratégie > technique
- Démontrer valeur business (pilotage, conformité)
- Anticiper questions : coûts, ressources, risques

**Démonstration live (optionnel)** :
- Ouvrir preview draft
- Naviguer dans un module (ex: SIRCOM)
- Montrer synthèse globale
- Montrer PDF généré

### 4. Recueillir le feedback et la décision

**Questions possibles de Yves** :
- "Quel est le niveau de conformité actuel ?" → Réponse : Score global X%
- "Combien de temps pour atteindre 100% ?" → Réponse : Horizon 2027 (SPAN = 3 ans)
- "Quels risques si on publie maintenant ?" → Réponse : Aucun (preview validée, CI robuste)
- "Quelle charge pour les services ?" → Réponse : Référent dédié X%, formations assurées
- "Peut-on ajouter d'autres services ?" → Réponse : Phase 2, architecture scalable

**Décision attendue** :
- ✅ **GO** : Publication autorisée
- ⚠️ **GO CONDITIONNEL** : Publication avec réserves (ex: corriger module X avant)
- ❌ **NO-GO** : Blocage (raison à documenter)

Si NO-GO : Comprendre raisons, plan d'action, nouvelle date.

### 5. Documenter la décision

Créer `DECISION-GO-NO-GO-v1.0.md` :
```markdown
# Décision GO/NO-GO SPAN SG v1.0

**Date** : [JJ/MM/AAAA]
**Session** : Présentation validation production
**Sponsor** : Yves
**Participants** : Alexandra (PM), Bertrand (validateur), Alex (validateur)

---

## Contexte

Présentation du SPAN SG v1.0 comprenant :
- 6 modules services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- Score global : [X/186] ([Y%])
- CI/CD opérationnelle
- Reviews techniques validées

---

## Résultat

### Décision : ✅ **GO POUR PRODUCTION**

Le sponsor Yves valide le passage en production du SPAN SG v1.0.

### Conditions (si applicable)
- [Condition 1, ex: Corriger URL SAFI avant tag]
- [Condition 2]

### Échéance publication
[JJ/MM/AAAA] (date cible pour S4-04)

---

## Feedback Yves

[Notes verbatim ou synthétisées]

Exemples :
- "Bon travail d'équipe, bravo pour le respect du planning"
- "Attention à la qualité module SAFI, à surveiller"
- "Prévoir communication large aux services post-publication"

---

## Prochaines étapes

1. S4-03 : Tag v1.0.0 et CHANGELOG
2. S4-04 : Publication production (merge draft → main)
3. Communication interne (email direction)
4. Suivi trimestriel avancement (scores)

---

**Signatures**

- **Yves (Sponsor)** : ✅ GO, [date]
- **Alexandra (PM)** : ✅ Noté, [date]
- **Bertrand (Validateur)** : ✅ Noté, [date]
- **Alex (Validateur)** : ✅ Noté, [date]
```

### 6. Archiver les supports

```bash
mkdir -p decisions/v1.0/
mv DECISION-GO-NO-GO-v1.0.md decisions/v1.0/
cp [slides].pdf decisions/v1.0/slides-presentation-yves.pdf
cp exports/span-sg.pdf decisions/v1.0/span-sg-v1.0.pdf

git add decisions/
git commit -m "docs: archive décision GO v1.0 et supports présentation"
git push origin draft
```

### 7. Communiquer la décision

**Si GO** :
```
📧 À : Équipe SPAN (Alexandra, Bertrand, Alex, 6 référents services)
Objet : ✅ SPAN SG v1.0 - GO pour production !

Excellente nouvelle : Yves a validé le passage en production du SPAN SG v1.0 !

**Prochaines étapes** :
- Tag v1.0.0 : [date S4-03]
- Publication : [date S4-04]
- Communication direction : [date post-S4-04]

Félicitations à toute l'équipe pour ce travail collaboratif 🎉

Alexandra
```

**Si NO-GO** :
```
📧 À : Équipe SPAN
Objet : SPAN SG v1.0 - Ajustements demandés

Suite à la présentation à Yves, quelques ajustements sont nécessaires avant publication :
- [Raison 1]
- [Raison 2]

Plan d'action : [détails]
Nouvelle date de validation : [JJ/MM]

On continue, on y est presque !
Alexandra
```

---

## Critères d'acceptation

- [ ] Slides présentation créés (10-15 slides)
- [ ] PDF synthèse disponible
- [ ] Session avec Yves planifiée et réalisée
- [ ] Décision GO/NO-GO obtenue et documentée
- [ ] `DECISION-GO-NO-GO-v1.0.md` créé et signé
- [ ] Feedback Yves capturé et archivé
- [ ] Équipe informée de la décision
- [ ] Si GO : Déblocage S4-03 (tag) et S4-04 (publication)

---

## Tests de validation

```bash
# Test 1 : Décision documentée
test -f decisions/v1.0/DECISION-GO-NO-GO-v1.0.md && echo "OK" || echo "FAIL"

# Test 2 : Décision est GO
grep -q "GO POUR PRODUCTION" decisions/v1.0/DECISION-GO-NO-GO-v1.0.md && echo "OK" || echo "WARN: NO-GO ou conditionnel"

# Test 3 : Supports archivés
test -f decisions/v1.0/slides-presentation-yves.pdf && test -f decisions/v1.0/span-sg-v1.0.pdf && echo "OK" || echo "FAIL"

# Test 4 : Signatures présentes
grep -c "✅" decisions/v1.0/DECISION-GO-NO-GO-v1.0.md
# Attendu : 4 (Yves + 3 participants)
```

---

## Dépendances

**Bloque** :
- S4-03 (tag nécessite GO Yves)
- S4-04 (publication nécessite GO Yves)

**Dépend de** :
- S4-01 (reviews doivent être validées)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 4 Production
- **PRD v3.3** : Section 12 "Contacts" → Yves (Sponsor)
- **PRD v3.3** : Section 13 "Décision GO/NO-GO"
- **DECISION-GO-NO-GO-v1.0.md** : Document à créer

---

## Notes et risques

**Yves non disponible**
Si impossible de planifier session rapidement :
- Option 1 : Présentation async (vidéo + slides envoyés)
- Option 2 : Délégation à son N-1
- Option 3 : Reporter publication (pas idéal)

**NO-GO inattendu**
Si Yves bloque pour raison non anticipée :
- Comprendre root cause
- Évaluer si bloquant technique ou politique
- Plan d'action avec échéances
- Re-présentation si nécessaire

**Décision conditionnelle**
Si GO avec réserves :
- Documenter précisément les conditions
- Assigner responsables et échéances
- Validation finale après levée conditions (mini-GO)

**Niveau de détail**
Adapter selon appétit Yves :
- S'il veut détails techniques → impliquer Bertrand/Alex
- S'il veut vision macro → focus stratégie/ROI

**Absence signatures formelles**
Si signatures physiques impossibles (visio) :
- Email de confirmation de Yves = signature
- Archiver l'email dans `decisions/v1.0/`

---

## Post-tâche

Créer un template réutilisable pour futures validations :
```bash
cp decisions/v1.0/DECISION-GO-NO-GO-v1.0.md .github/DECISION-TEMPLATE.md
# Remplacer valeurs spécifiques par [PLACEHOLDERS]
```

Planifier suivi post-production :
```markdown
## Suivi post-GO

- J+7 : Vérifier pas de régression post-publication
- J+30 : Premier rapport mensuel à Yves (évolution scores)
- T+1 trimestre : Revue trimestrielle + roadmap v1.1
```

Préparer communication direction (si GO) :
```
📧 À : Direction SG
CC : Yves
Objet : Nouveau : SPAN SG - Pilotage accessibilité numérique

Le Secrétariat Général dispose maintenant d'un outil de pilotage de l'accessibilité numérique :
- URL : https://[production-url]
- 6 services suivis (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- Scoring automatique sur 31 critères DINUM
- Mise à jour continue par les services

[Détails...]
```