# S7-02 - Synchronisation synthèse.md : DSFR HTML en local et distant

**Date** : 2025-10-08
**Statut** : Approuvé
**Priorité** : P0 (Bloquant production)
**Type** : Fix technique

---

## Contexte

### Problème identifié

Après reset des modules à blanc (sauf SIRCOM), incohérence constatée entre environnements :

- **Local** (localhost:8000/span-sg-repo/synthese/) :
  - Tableau DSFR avec bordures (`fr-table--bordered`)
  - Disclaimer : "1 module validé (SIRCOM), 5 modules en cours"
  - Scores affichés : 0/31 (attendu après correction)

- **Distant** (alexmacapple.github.io/span-sg-repo/draft/synthese/) :
  - Tableau Markdown simple (sans DSFR)
  - Disclaimer : "2 modules validés" (obsolète)
  - Scores affichés : 0/0 (incorrect)

### Cause racine

Le script `scripts/calculate_scores.py` (ligne 87) **écrase** le fichier `docs/synthese.md` lors du build CI avec un contenu généré :

```python
Path("docs/synthese.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
```

**Conséquence** : modifications manuelles de synthèse.md en local non préservées à distant après déploiement CI.

### Contraintes MVP v1.0

1. **31 points DINUM obligatoires** : validation périmètre (`total ∈ {0, 31}`)
2. **Aucun module vide sans tags** : 0/0 invalide (erreur périmètre)
3. **DSFR obligatoire** : tableaux avec `fr-table fr-table--bordered`
4. **Strictement production-ready** : 1 module validé (SIRCOM 24/31)

---

## BMAD - Bénéfices, Metrics, Analyses, Décisions

### B - Bénéfices attendus

1. **Cohérence local/distant** : même contenu synthèse.md sur branche draft (localhost = GitHub Pages)
2. **Conformité DSFR** : tableau avec bordures verticales en production
3. **Validation périmètre** : respect règle 31 points DINUM (0/31 ou 31/31, jamais 0/0)
4. **Automatisation préservée** : script continue de générer synthèse.md (pas de maintenance manuelle)
5. **Disclaimer exact** : "1 module validé" (production-ready v1.0)

### M - Métriques de succès

| Métrique | Valeur cible | Validation |
|---|---|---|
| Score modules vides | 0/31 (0.0%) | `python3 scripts/calculate_scores.py` |
| Score SIRCOM | 24/31 (77.4%) | Préservé |
| Score total | 24/31 (77.4%) | Ligne TOTAL |
| Validation périmètre | Exit code 0 | Pas d'erreur "attendu 31 ou 0" |
| Classe CSS DSFR | `fr-table--bordered` | Présent dans synthèse.md |
| Disclaimer | "1 module validé (SIRCOM)" | Texte exact ligne 5 |
| Sync local/distant | 100% identique | `diff <(curl -s distant) <(cat local)` |

### A - Analyses des options

#### Option 1 : Désactiver génération automatique (REJETÉE)

**Description** : Commenter ligne 87 de calculate_scores.py, maintenir synthèse.md manuellement.

**Avantages** :
- Contrôle total du contenu DSFR

**Inconvénients** :
- Perte automatisation (maintenance manuelle à chaque modification module)
- Risque désynchronisation scores (oubli recalcul)
- Non-MVP (complexification workflow contributeurs)

**Décision** : REJETÉE (contradictoire avec automation CI/CD)

---

#### Option 2 : Restaurer 31 points DINUM non cochés dans modules vides (RECOMMANDÉE)

**Description** : Copier liste des 31 points de contrôle DINUM depuis `docs/modules/_template.md` vers les 5 modules vides (BGS, SAFI, SIEP, SRH, SNUM) avec cases non cochées `[ ]`.

**Avantages** :
- Respect validation périmètre (31 points présents)
- Scores corrects : 0/31 (0.0%) au lieu de 0/0
- Script continue de fonctionner sans modification
- Cohérence structurelle avec SIRCOM (même template)
- Facilite complétion future (cases à cocher progressivement)

**Inconvénients** :
- Légère augmentation taille fichiers modules vides (+150 lignes)
- Pas de refactoring script (dette technique reportée)

**Décision** : RECOMMANDÉE (MVP-compliant, zéro risque, déploiement immédiat)

---

#### Option 3 : Modifier script pour générer HTML DSFR + accepter total=0 (PARTIELLE)

**Description** :
1. Modifier calculate_scores.py lignes 42-145 pour générer HTML DSFR au lieu de Markdown
2. Modifier ligne 70 pour accepter `total == 0` comme valide (pas d'erreur périmètre)

**Avantages** :
- Génération DSFR automatique (pas de maintenance manuelle)
- Modules vides possibles sans tags

**Inconvénients** :
- **Incohérence structurelle** : modules vides sans template ≠ modules remplis avec template
- **Complexité future** : contributeurs doivent copier template manuellement au moment de remplir
- **Validation périmètre contournée** : total=0 acceptable mais perte de garde-fou (erreur si oubli tags)
- **Modification script critique** : risque régression, tests unitaires à adapter

**Décision** : PARTIELLE - Appliquer refactoring HTML DSFR uniquement (lignes 42-145), **mais conserver validation total ∈ {0,31}** (ne pas accepter 0). Combiné avec Option 2 pour respecter périmètre.

---

#### Option 4 : Template dynamique en front-matter (HORS PÉRIMÈTRE)

**Description** : Ajouter `template: empty` dans front-matter modules vides, script génère contenu conditionnel.

**Avantages** :
- Flexibilité maximale (modules vides possibles)
- Pas de duplication template

**Inconvénients** :
- **Hors périmètre MVP** : nouvelle fonctionnalité (logique conditionnelle front-matter)
- **Complexification script** : +50 lignes, tests unitaires à créer
- **Délai** : estimation 2-3h développement + validation
- **Risque** : dette technique (maintenance conditionnelle)

**Décision** : REJETÉE (post-MVP, suringénierie)

---

### D - Décision finale

**Stratégie hybride Option 2 + Option 3 (HTML uniquement)** :

1. **Script calculate_scores.py** : Refactoring lignes 42-145 pour générer HTML DSFR (déjà implémenté localement, à commiter)
2. **Modules vides** : Restaurer 31 points DINUM non cochés depuis `_template.md` (sections "31 points de contrôle DINUM" uniquement)
3. **Validation périmètre** : Conserver règle stricte `total ∈ {0, 31}` (ligne 70)
4. **Disclaimer** : Mise à jour "1 module validé (SIRCOM)" (déjà dans script modifié)

**Justification** :
- Respect périmètre MVP v1.0 (31 points obligatoires)
- Zéro modification logique validation (sécurité)
- Cohérence structurelle (tous modules basés sur template)
- Automatisation DSFR (génération HTML)
- Déploiement immédiat possible

---

## Plan d'implémentation

### Étape 1 : Restaurer template dans modules vides

**Fichiers concernés** : 5 modules (BGS, SAFI, SIEP, SRH, SNUM)

**Action** : Copier depuis `docs/modules/_template.md` lignes 60-150 (31 points DINUM) vers chaque module vide après le titre.

**Structure cible** :
```markdown
---
service: [SERVICE]
referent: À définir
updated: 2025-10-08
validation_status: draft
---

# SPAN [SERVICE]

## 31 points de contrôle DINUM

### Stratégie

- [ ] 1. Le plan d'action de mise en conformité RGAA est établi, chiffré et arbitré <!-- DINUM -->
- [ ] 2. Les arbitrages sur les dérogations pour charge disproportionnée sont effectués <!-- DINUM -->
[... 29 autres points non cochés ...]

### Déclaration d'accessibilité

- [ ] 31. La déclaration d'accessibilité est publiée et régulièrement mise à jour <!-- DINUM -->
```

**Commandes** :
```bash
# Pour chaque module (BGS, SAFI, SIEP, SRH, SNUM)
# Éditer manuellement ou utiliser Edit tool pour insérer section 31 points
```

**Validation** : Chaque module doit contenir exactement 31 lignes `<!-- DINUM -->` non cochées.

---

### Étape 2 : Régénérer synthèse.md avec script modifié

**Prérequis** : Script calculate_scores.py déjà modifié en local (lignes 42-145 HTML DSFR + disclaimer à jour).

**Action** :
```bash
python3 scripts/calculate_scores.py
```

**Résultat attendu** :
- Exit code 0 (pas d'erreur périmètre)
- `docs/synthese.md` généré avec :
  - HTML DSFR `<div class="fr-table fr-table--bordered">`
  - Disclaimer "1 module validé (SIRCOM), 5 modules en cours"
  - Scores : BGS 0/31, SAFI 0/31, SIEP 0/31, SIRCOM 24/31, SNUM 0/31, SRH 0/31
  - Total : 24/31 (77.4%)

**Validation** :
```bash
grep -c '<!-- DINUM -->' docs/modules/{bgs,safi,siep,snum,srh}.md
# Attendu: 31 par module

grep 'fr-table--bordered' docs/synthese.md
# Attendu: présent

grep '1 module validé' docs/synthese.md
# Attendu: présent
```

---

### Étape 3 : Commit atomique

**Fichiers modifiés** :
1. `scripts/calculate_scores.py` (refactoring HTML DSFR)
2. `docs/modules/bgs.md` (31 points DINUM ajoutés)
3. `docs/modules/safi.md` (31 points DINUM ajoutés)
4. `docs/modules/siep.md` (31 points DINUM ajoutés)
5. `docs/modules/snum.md` (31 points DINUM ajoutés)
6. `docs/modules/srh.md` (31 points DINUM ajoutés)
7. `docs/synthese.md` (régénéré avec HTML DSFR)

**Commit message** :
```
fix(synthese): sync local/distant avec DSFR HTML + 31 points modules vides

Correction désynchronisation localhost ≠ GitHub Pages draft.

Modifications :
- scripts/calculate_scores.py : génération HTML DSFR (fr-table--bordered) au lieu de Markdown
- Disclaimer : "1 module validé (SIRCOM)" (v1.0 production-ready)
- Modules vides : 31 points DINUM non cochés (validation périmètre 0/31)
- docs/synthese.md : régénéré automatiquement

Scores v1.0 :
- BGS 0/31, SAFI 0/31, SIEP 0/31, SIRCOM 24/31, SNUM 0/31, SRH 0/31
- TOTAL 24/31 (77.4%)

Critères acceptation S7-02 :
- ✓ Validation périmètre (total=31 pour 6 modules)
- ✓ DSFR bordures verticales (fr-table--bordered)
- ✓ Disclaimer exact (1 module validé)
- ✓ Script auto-génération préservé
```

**Commande** :
```bash
git add scripts/calculate_scores.py docs/modules/{bgs,safi,siep,snum,srh}.md docs/synthese.md
git commit -m "fix(synthese): sync local/distant avec DSFR HTML + 31 points modules vides"
```

---

### Étape 4 : Push et vérification CI

**Action** :
```bash
git push origin draft
```

**Vérification workflow** :
1. GitHub Actions `.github/workflows/build.yml` se déclenche
2. Job `build` :
   - Ligne 46 : `python scripts/calculate_scores.py` (doit réussir, exit code 0)
   - Ligne 49 : `mkdocs build --config-file mkdocs-dsfr.yml --strict` (doit passer)
3. Job `e2e-tests` : **SKIPPED** (condition `if: github.ref != 'refs/heads/draft'` ligne 79)
4. Job `deploy_draft` :
   - Ligne 136-143 : Déploiement vers `gh-pages/draft/`

**Monitoring** :
```bash
gh run watch
```

**Validation CI** :
- Build job : PASSED (vert)
- E2E tests job : SKIPPED (gris)
- Deploy draft job : PASSED (vert)
- Artefacts uploadés : `span-site`, `exports`

---

### Étape 5 : Test synchronisation local/distant

**Local** :
```bash
# Ouvrir localhost:8000/span-sg-repo/synthese/
# Hard refresh : Cmd+Shift+R
```

**Distant** :
```bash
# Attendre 2-3 min après déploiement CI
# Ouvrir https://alexmacapple.github.io/span-sg-repo/draft/synthese/
# Hard refresh : Cmd+Shift+R
```

**Vérifications identiques** (local = distant) :
1. Titre : "Tableau de bord SPAN SG"
2. Disclaimer : "1 module validé (SIRCOM), 5 modules en cours de complétion"
3. Tableau DSFR avec bordures verticales visibles
4. Scores :
   - BGS : 0/31 (0.0%) - Non renseigné - Brouillon
   - SAFI : 0/31 (0.0%) - Non renseigné - Brouillon
   - SIEP : 0/31 (0.0%) - Non renseigné - Brouillon
   - SIRCOM : 24/31 (77.4%) - Conforme - Validé
   - SNUM : 0/31 (0.0%) - Non renseigné - Brouillon
   - SRH : 0/31 (0.0%) - Non renseigné - Brouillon
   - **TOTAL** : 24/31 (77.4%) - Global
5. Attributs HTML présents : `id="table-synthese-span"`, `data-row-key="sircom"`, `<th scope="col">`

**Test automatisé** :
```bash
# Comparer source HTML local vs distant
curl -s https://alexmacapple.github.io/span-sg-repo/draft/synthese/ | grep -o 'fr-table--bordered'
# Attendu: fr-table--bordered

curl -s https://alexmacapple.github.io/span-sg-repo/draft/synthese/ | grep -o '1 module validé'
# Attendu: 1 module validé

curl -s https://alexmacapple.github.io/span-sg-repo/draft/synthese/ | grep -o '0/31'
# Attendu: 5 occurrences (modules vides)
```

---

## Critères d'acceptation

| ID | Critère | Validation |
|---|---|---|
| AC1 | Tous les modules ont exactement 31 points DINUM | `grep -c '<!-- DINUM -->' docs/modules/*.md` retourne 31 pour BGS, SAFI, SIEP, SNUM, SRH |
| AC2 | Script génère HTML DSFR avec bordures | `grep 'fr-table--bordered' docs/synthese.md` retourne match |
| AC3 | Disclaimer exact "1 module validé (SIRCOM)" | `grep '1 module validé (SIRCOM)' docs/synthese.md` retourne match |
| AC4 | Scores corrects 0/31 pour modules vides | `grep '0/31 (0.0%)' docs/synthese.md` retourne 5 occurrences |
| AC5 | Score SIRCOM préservé 24/31 | `grep '24/31 (77.4%)' docs/synthese.md` retourne 2 occurrences (ligne + total) |
| AC6 | Validation périmètre réussie | `python3 scripts/calculate_scores.py` exit code 0 |
| AC7 | Build CI passe sans erreur | GitHub Actions build job PASSED |
| AC8 | Déploiement draft réussi | GitHub Actions deploy_draft job PASSED |
| AC9 | Contenu identique local/distant | Vérification visuelle + `curl` tests |
| AC10 | Tableau responsive DSFR | Inspecter HTML : `<div class="fr-table__wrapper">` présent |

---

## Risques et mitigations

| Risque | Impact | Probabilité | Mitigation |
|---|---|---|---|
| Erreur copie template (oubli tag DINUM) | Bloquant (validation périmètre) | Faible | Validation automatique par script (exit code 2 si total ≠ 31) |
| Régression script (génération HTML cassée) | Critique (syntaxe HTML invalide) | Faible | Test local avant commit + MkDocs strict mode |
| CI timeout (charge serveur GitHub) | Moyen (délai déploiement) | Très faible | Aucun changement infra, jobs inchangés |
| Cache navigateur (utilisateur voit ancien contenu) | Mineur (UX temporaire) | Moyen | Hard refresh documenté (Cmd+Shift+R) |
| Conflit merge si modif concurrente | Moyen (résolution manuelle) | Très faible | Commit atomique, communication équipe |

---

## Plan de rollback

Si problème bloquant après déploiement :

### Rollback rapide (< 2 min)

```bash
# Revenir commit précédent sur branche draft
git reset --hard HEAD~1
git push --force origin draft

# CI redéploie automatiquement version précédente
```

### Rollback partiel (modules uniquement)

```bash
# Restaurer modules vides sans les 31 points
git checkout HEAD~1 -- docs/modules/{bgs,safi,siep,snum,srh}.md
python3 scripts/calculate_scores.py
git commit -m "rollback: modules vides sans template"
git push origin draft
```

### Rollback script (conserver modules)

```bash
# Restaurer ancienne version script
git checkout HEAD~1 -- scripts/calculate_scores.py
python3 scripts/calculate_scores.py
git commit -m "rollback: script génération Markdown"
git push origin draft
```

**Critère rollback** : Exit code 2 du script (erreur périmètre) ou build CI failed après 2 tentatives.

---

## Post-implémentation

### Monitoring (J+7)

1. **Métriques GitHub Pages** : Vérifier analytics (aucune 404 sur /draft/synthese/)
2. **Feedback contributeurs** : Confirmer workflow compréhensible (31 points visibles dans modules vides)
3. **Performance build** : Vérifier temps CI inchangé (~3-4 min)

### Améliorations futures (post-MVP)

1. **Tests unitaires script** : Ajouter test génération HTML DSFR (pytest)
2. **Hook pre-commit** : Validation 31 points DINUM avant commit
3. **Template dynamique** : Option 4 (front-matter `template: empty`) si besoin récurrent modules vides

---

## Références

- Issue tracking : S7-02
- Commit related : À venir (fix(synthese): sync local/distant)
- Documentation : CLAUDE.md lignes 15-25 (règle stricte 31 points)
- Script source : `scripts/calculate_scores.py` lignes 6-8, 42-145
- Template référence : `docs/modules/_template.md` lignes 60-150

---

## Validation

- **Auteur** : Claude Code
- **Reviewer** : Alexandra (owner)
- **Approuvé** : 2025-10-08
- **Implémentation** : En cours (étape 1/5)
