# Story S4-01 : Review contenus (Bertrand/Alex)

**Phase** : Semaine 4 - Production
**Priorité** : Critique
**Estimation** : 4h
**Assigné** : Bertrand + Alex (validateurs)

---

## Contexte projet

Avant le passage en production (merge draft → main), une **review exhaustive** des 6 modules est nécessaire pour garantir :
- Qualité du contenu (cohérence, exactitude)
- Conformité au template (structure, 31 points)
- Respect des contraintes légales (déclarations accessibilité)
- Absence de secrets/infos sensibles
- Cohérence inter-services

Les validateurs (Bertrand, Alex) effectuent cette revue selon une checklist standardisée. Alexandra coordonne et consolide les retours.

---

## Objectif

Bertrand et Alex relisent les 6 modules, identifient les problèmes, demandent corrections si nécessaire, et donnent leur GO/NO-GO pour passage en production.

---

## Prérequis

- [ ] Story S3-03 complétée (contenus initiaux renseignés)
- [ ] Branche `draft` à jour et stable
- [ ] Preview draft accessible pour consultation
- [ ] Checklist de revue préparée

---

## Étapes d'implémentation

### 1. Préparer la checklist de revue

Créer `.github/REVIEW-CHECKLIST.md` :
```markdown
# Checklist de revue module SPAN

Module : `docs/modules/[service].md`
Reviewer : [Nom]
Date : [JJ/MM/AAAA]

---

## 1. Conformité structure

- [ ] Front-matter présent et valide (service, referent, updated)
- [ ] Exactement 31 tags `<!-- DINUM -->` présents
- [ ] 5 sections obligatoires présentes (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- [ ] Section "points de contrôle officiels (31)" présente
- [ ] Blocs légaux présents (déclaration accessibilité + charge disproportionnée)

## 2. Qualité contenu

- [ ] Section 1 (Périmètre) : Liste applications claire et exhaustive
- [ ] Section 2 (État des lieux) : Audits documentés avec dates et scores
- [ ] Section 3 (Organisation) : Référent identifié avec ETP et contact
- [ ] Section 4 (Plan d'action) : 3-5 actions concrètes avec échéances et budgets
- [ ] Section 5 (Indicateurs) : Métriques quantifiées (%, nombres)

## 3. Points DINUM

- [ ] Chaque point coché `[x]` est justifié (pas de sur-déclaration)
- [ ] Points non cochés sont cohérents avec l'état des lieux
- [ ] Score global du module cohérent (≥10% attendu pour modules actifs)

## 4. Blocs légaux

- [ ] URL déclaration d'accessibilité renseignée (ou TODO avec échéance)
- [ ] Date de mise à jour de la déclaration < 1 an
- [ ] Analyse charge disproportionnée remplie (ou "Non applicable")
- [ ] Si charge disproportionnée : justification + alternative + réévaluation

## 5. Sécurité et confidentialité

- [ ] Aucun secret (mots de passe, tokens, clés API)
- [ ] Aucune info sensible (vulnérabilités critiques non patchées)
- [ ] Budgets arrondis (pas de montants exacts sous contrat)
- [ ] Contacts : emails génériques (pas personnels)

## 6. Cohérence inter-services

- [ ] Pas de doublons d'actions entre services
- [ ] Terminologie cohérente (ex: "audit RGAA" partout)
- [ ] Niveau de détail homogène entre modules

## 7. Technique

- [ ] Liens valides (pas de 404)
- [ ] Tableaux bien formatés (pas de colonnes manquantes)
- [ ] Markdown valide (aperçu GitHub correct)
- [ ] Pas d'erreur de typo majeure

---

## Décision

- [ ] ✅ **GO** : Module validé pour production
- [ ] ⚠️ **CONDITIONNEL** : Corrections mineures nécessaires (détails ci-dessous)
- [ ] ❌ **NO-GO** : Corrections majeures nécessaires, repasser en revue

### Commentaires et corrections demandées

[Espace libre pour notes]

---

**Signature** : [Nom reviewer], [Date]
```

### 2. Assigner les modules aux reviewers

**Répartition recommandée** (2 reviewers pour redondance) :
- **Bertrand** : SNUM, SRH, SIEP
- **Alex** : SIRCOM, SAFI, BGS

**OU** : Chaque reviewer fait les 6 modules (plus long mais exhaustif).

### 3. Effectuer la revue (Bertrand + Alex)

Pour chaque module :

**Étape 1 : Lecture preview**
- Ouvrir https://[preview-url]/draft/modules/[service]/
- Lire l'intégralité du module
- Prendre notes mentales des problèmes

**Étape 2 : Remplir checklist**
- Copier `.github/REVIEW-CHECKLIST.md` → `reviews/[service]-[reviewer]-[date].md`
- Cocher chaque item
- Noter commentaires détaillés

**Étape 3 : Vérifier scoring**
```bash
# Cloner draft localement
git checkout draft
git pull origin draft

# Recalculer scores
python scripts/calculate_scores.py

# Vérifier cohérence
cat docs/synthese.md
```

**Étape 4 : Valider liens**
```bash
# Test liens (optionnel, automatisable)
mkdocs build --strict
# Si erreur de lien cassé, noter dans checklist
```

**Étape 5 : Décision GO/NO-GO**
- GO : Module prêt
- CONDITIONNEL : Corrections mineures (typos, liens)
- NO-GO : Problèmes majeurs (contenu insuffisant, erreurs scoring)

### 4. Consolider les retours (Alexandra)

Créer un document de synthèse `reviews/SYNTHESE-REVIEW.md` :
```markdown
# Synthèse review modules SPAN SG

Date : [JJ/MM/AAAA]
Reviewers : Bertrand, Alex

---

## Statut global

| Module | Bertrand | Alex | Statut final |
|--------|----------|------|--------------|
| SNUM | ✅ GO | ✅ GO | ✅ **VALIDÉ** |
| SIRCOM | ✅ GO | ✅ GO | ✅ **VALIDÉ** |
| SRH | ⚠️ COND | ✅ GO | ⚠️ **CORRECTIONS MINEURES** |
| SIEP | ✅ GO | ✅ GO | ✅ **VALIDÉ** |
| SAFI | ❌ NO-GO | ❌ NO-GO | ❌ **CORRECTIONS MAJEURES** |
| BGS | ⚠️ COND | ⚠️ COND | ⚠️ **CORRECTIONS MINEURES** |

---

## Corrections demandées

### SRH (mineures)
- Corriger typo "accessibilitée" → "accessibilité" (ligne 45)
- Ajouter échéance action #3 (actuellement vide)

### SAFI (majeures)
- Section 2 (État des lieux) : Aucun audit documenté → Ajouter au moins 1 audit ou préciser "En cours"
- Plan d'action : Seulement 1 action → Ajouter 2-3 actions supplémentaires
- Points DINUM : 15 cochés mais non justifiés → Revoir avec référent SAFI

### BGS (mineures)
- URL déclaration accessibilité : Lien 404 → Vérifier/corriger URL
- Tableau plan d'action : Colonne "Budget" manquante pour action #2

---

## Actions

1. **Alexandra** : Créer issues GitHub pour chaque correction
2. **Référents SRH/SAFI/BGS** : Appliquer corrections sous 48h
3. **Bertrand/Alex** : Re-revue modules corrigés
4. **Décision finale** : GO/NO-GO global pour S4-02

---

**Date butoir corrections** : [JJ/MM/AAAA + 2 jours]
```

### 5. Créer issues GitHub pour corrections

Pour chaque correction demandée :
```bash
# Exemple issue SRH
gh issue create \
  --title "[SRH] Corrections mineures review" \
  --body "Suite à la review, corrections nécessaires :
- [ ] Corriger typo ligne 45
- [ ] Ajouter échéance action #3

Assigné : @referent-srh
Échéance : [date]"
```

### 6. Suivre les corrections

Tableau de suivi (Google Sheet, Notion, ou GitHub Project) :
```
| Module | Issue | Assigné | Statut | Re-review |
|--------|-------|---------|--------|-----------|
| SRH | #12 | @ref-srh | ✅ Corrigé | ✅ Validé |
| SAFI | #13 | @ref-safi | ⏳ En cours | - |
| BGS | #14 | @ref-bgs | ✅ Corrigé | ✅ Validé |
```

### 7. Re-revue modules corrigés

Une fois corrections appliquées :
- Re-exécuter checklist pour modules concernés
- Si OK → Changer statut à **VALIDÉ**
- Si encore KO → Nouvelle itération

### 8. Décision GO/NO-GO globale

Quand les 6 modules sont **VALIDÉ** :
```markdown
# Décision GO/NO-GO SPAN SG v1.0

Date : [JJ/MM/AAAA]
Décideurs : Bertrand, Alex, Alexandra

## Résultat : ✅ **GO POUR PRODUCTION**

Les 6 modules ont été revus et validés.
Score global : [X/186] ([Y%])

Prochaines étapes :
- S4-02 : Validation Yves (sponsor)
- S4-03 : Tag v1.0.0
- S4-04 : Publication production

---

Signatures :
- Bertrand : ✅
- Alex : ✅
- Alexandra : ✅
```

---

## Critères d'acceptation

- [ ] Checklist `.github/REVIEW-CHECKLIST.md` créée
- [ ] 6 modules revus par au moins 1 reviewer (idéalement 2)
- [ ] Checklists remplies et archivées dans `reviews/`
- [ ] Synthèse consolidée (`reviews/SYNTHESE-REVIEW.md`)
- [ ] Issues GitHub créées pour corrections
- [ ] Corrections appliquées et re-validées
- [ ] Décision GO/NO-GO documentée
- [ ] Si GO : branche draft prête pour S4-02

---

## Tests de validation

```bash
# Test 1 : Checklist existe
test -f .github/REVIEW-CHECKLIST.md && echo "OK" || echo "FAIL"

# Test 2 : Reviews complétées (6 fichiers minimum)
test $(ls reviews/*-review-*.md 2>/dev/null | wc -l) -ge 6 && echo "OK" || echo "FAIL"

# Test 3 : Synthèse existe
test -f reviews/SYNTHESE-REVIEW.md && echo "OK" || echo "FAIL"

# Test 4 : Scoring cohérent (pas d'erreur périmètre)
python scripts/calculate_scores.py && echo "OK" || echo "FAIL"

# Test 5 : Tous modules validés
grep -c "VALIDÉ" reviews/SYNTHESE-REVIEW.md
# Attendu : 6
```

---

## Dépendances

**Bloque** :
- S4-02 (validation Yves nécessite GO de cette story)

**Dépend de** :
- S3-03 (contenus doivent être renseignés)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 4 Production
- **PRD v3.3** : Section 4 "Checklist de revue PR"
- **.github/REVIEW-CHECKLIST.md** : Checklist à créer
- **reviews/** : Répertoire pour archives reviews

---

## Notes et risques

**Temps de revue sous-estimé**
4h pour 6 modules = 40 min/module. Si modules très riches, prévoir plus (jusqu'à 8h total).

**Désaccord entre reviewers**
Si Bertrand dit GO et Alex dit NO-GO :
- Discussion tripartite (+ Alexandra)
- Décision à la majorité
- En cas de blocage : escalade Yves

**Corrections qui traînent**
Si un service ne corrige pas sous 48h :
- Relance +24h
- Si toujours pas → NO-GO temporaire
- Passage en prod différé pour ce module (merge 5/6 modules)

**Sur-qualité**
Éviter perfectionnisme excessif. Accepter "bon enough" pour v1.0 (principe MVP).

**Biais reviewer**
Bertrand/Alex peuvent avoir des visions différentes de "qualité suffisante". Harmoniser critères avant début revue.

---

## Post-tâche

Archiver les reviews :
```bash
mkdir -p reviews/archive-v1.0/
mv reviews/*-review-*.md reviews/archive-v1.0/
git add reviews/
git commit -m "docs: archive reviews v1.0"
```

Remercier les reviewers :
```
📧 À : Bertrand, Alex
Objet : Merci pour la review SPAN v1.0 !

Merci pour votre relecture exhaustive des 6 modules.

Résultat : 6/6 validés après corrections.
Score global : [X%]

Prochaine étape : Validation Yves (S4-02).

Bravo pour le travail d'équipe 🎉
Alexandra
```

Préparer présentation pour Yves (S4-02) :
- Slides récap : 6 modules, score global, actions prioritaires
- Version PDF synthèse (depuis artefacts CI)
- Highlights : Progrès depuis début projet