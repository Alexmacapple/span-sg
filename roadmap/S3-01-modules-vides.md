---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S3-01 : Création modules vides + front-matter

**Phase** : Semaine 3 - Onboarding
**Priorité** : Haute
**Estimation** : 1h30
**Assigné** : Alexandra

---

## Contexte projet

Périmètre v1 : **6 modules services**
1. SNUM (Service du Numérique)
2. SIRCOM (Service Interministériel des Ressources et des Compétences)
3. SRH (Service des Ressources Humaines)
4. SIEP (Service de l'Innovation et de l'Évaluation des Politiques)
5. SAFI (Service des Affaires Financières et Immobilières)
6. BGS (Bureau de Gestion des Services)

État actuel :
- `_template.md` : Template officiel avec 31 points DINUM
- `sircom.md` : Module pilote (déjà créé)
- Autres modules : à créer

Objectif de cette story : Créer les 5 modules manquants (SNUM, SRH, SIEP, SAFI, BGS) avec :
- Structure complète à partir du template
- Front-matter renseigné (service, referent, updated)
- 31 points DINUM présents mais **non cochés** (0/31)
- Placeholders pour sections obligatoires
- Prêts à être édités par les référents services

---

## Objectif

Créer 5 fichiers modules vides conformes au template, renseigner le front-matter de base, valider avec le script de scoring, et committer dans `draft`.

---

## Prérequis

- [ ] Story S1-04 complétée (template validé)
- [ ] Story S1-05 complétée (script scoring fonctionnel)
- [ ] Story S1-06 complétée (SIRCOM comme référence)
- [ ] Informations de base sur les 5 services (noms complets, référents si connus)

---

## Étapes d'implémentation

### Option automatique (recommandée) : Script create-module.sh

**Pour créer les 5 modules** :
```bash
./scripts/create-module.sh SNUM
./scripts/create-module.sh SRH
./scripts/create-module.sh SIEP
./scripts/create-module.sh SAFI
./scripts/create-module.sh BGS
```

Le script automatise les étapes 2-7 ci-dessous. Passer à l'étape 8 (validation scoring) si succès.

---

### Option manuelle (si script non disponible)

### 1. Vérifier les modules existants

```bash
ls docs/modules/
# Attendu : _template.md, sircom.md, (+ possiblement autres)
```

### 2. Créer le module SNUM

```bash
cp docs/modules/_template.md docs/modules/snum.md
```

Éditer `docs/modules/snum.md` :
```yaml
---
service: SNUM
referent: "[À définir - Service du Numérique]"
updated: "2025-09-30"
---

# SPAN SNUM - Schéma Pluriannuel d'accessibilité numérique

**Période** 2025-2027
**Service** Service du Numérique (SNUM)
**Score global** 0/31 questions validées (0.0%)
**Dernière mise à jour** 30 septembre 2025
```

Garder les 31 points DINUM non cochés `- [ ]`.

### 3. Créer le module SRH

```bash
cp docs/modules/_template.md docs/modules/srh.md
```

Éditer front-matter :
```yaml
---
service: SRH
referent: "[À définir - Service des Ressources Humaines]"
updated: "2025-09-30"
---

# SPAN SRH - Schéma Pluriannuel d'accessibilité numérique

**Période** 2025-2027
**Service** Service des Ressources Humaines (SRH)
**Score global** 0/31 questions validées (0.0%)
**Dernière mise à jour** 30 septembre 2025
```

### 4. Créer le module SIEP

```bash
cp docs/modules/_template.md docs/modules/siep.md
```

Éditer front-matter :
```yaml
---
service: SIEP
referent: "[À définir - Service Innovation et Évaluation]"
updated: "2025-09-30"
---

# SPAN SIEP - Schéma Pluriannuel d'accessibilité numérique

**Période** 2025-2027
**Service** Service de l'Innovation et de l'Évaluation des Politiques (SIEP)
**Score global** 0/31 questions validées (0.0%)
**Dernière mise à jour** 30 septembre 2025
```

### 5. Créer le module SAFI

```bash
cp docs/modules/_template.md docs/modules/safi.md
```

Éditer front-matter :
```yaml
---
service: SAFI
referent: "[À définir - Service Affaires Financières]"
updated: "2025-09-30"
---

# SPAN SAFI - Schéma Pluriannuel d'accessibilité numérique

**Période** 2025-2027
**Service** Service des Affaires Financières et Immobilières (SAFI)
**Score global** 0/31 questions validées (0.0%)
**Dernière mise à jour** 30 septembre 2025
```

### 6. Créer le module BGS

```bash
cp docs/modules/_template.md docs/modules/bgs.md
```

Éditer front-matter :
```yaml
---
service: BGS
referent: "[À définir - Bureau Gestion Services]"
updated: "2025-09-30"
---

# SPAN BGS - Schéma Pluriannuel d'accessibilité numérique

**Période** 2025-2027
**Service** Bureau de Gestion des Services (BGS)
**Score global** 0/31 questions validées (0.0%)
**Dernière mise à jour** 30 septembre 2025
```

### 7. Valider avec le script de scoring

```bash
python scripts/calculate_scores.py
```

Vérifier `docs/synthese.md` généré :
```markdown
| Service | Score | Statut |
|---------|-------|--------|
| BGS | 0/31 (0.0%) | Non renseigné |
| SAFI | 0/31 (0.0%) | Non renseigné |
| SIEP | 0/31 (0.0%) | Non renseigné |
| SIRCOM | X/31 (X.X%) | [Statut SIRCOM] |
| SNUM | 0/31 (0.0%) | Non renseigné |
| SRH | 0/31 (0.0%) | Non renseigné |
| **TOTAL** | **X/186 (X.X%)** | **Global** |
```

**Points de validation** :
- 6 modules listés (ordre alphabétique)
- 5 nouveaux modules = 0/31 (Non renseigné)
- SIRCOM conserve son score actuel
- Total = 186 points (6 modules × 31)

### 8. Tester la preview locale

```bash
docker compose up
```

Vérifier http://localhost:8000/span-sg-repo/ :
- Navigation affiche les 6 modules
- Chaque module est accessible
- Pas d'erreur 404
- Checkboxes visibles (toutes vides)

### 9. Vérifier la navigation MkDocs

```bash
cat mkdocs.yml | grep -A 10 "nav:"
```

S'assurer que les 6 modules sont bien listés :
```yaml
nav:
  - Modules Services:
    - SNUM: modules/snum.md
    - SIRCOM: modules/sircom.md
    - SRH: modules/srh.md
    - SIEP: modules/siep.md
    - SAFI: modules/safi.md
    - BGS: modules/bgs.md
```

### 10. Committer les nouveaux modules

```bash
git checkout draft
git add docs/modules/*.md docs/synthese.md
git commit -m "feat: crée 5 modules vides (SNUM, SRH, SIEP, SAFI, BGS) avec front-matter"
git push origin draft
```

### 11. Vérifier la CI

Attendre le run GitHub Actions et vérifier :
- ✅ Calculate SPAN scores : succès (5 modules à 0/31 acceptés)
- ✅ Build site : succès
- ✅ Artefact contient les 6 modules

---

## Critères d'acceptation

- [ ] 5 nouveaux fichiers créés : snum.md, srh.md, siep.md, safi.md, bgs.md
- [ ] Chaque fichier contient exactement 31 tags `<!-- DINUM -->`
- [ ] Toutes les checkboxes non cochées `- [ ]`
- [ ] Front-matter valide avec service, referent, updated
- [ ] `python scripts/calculate_scores.py` affiche 6 modules (186 points total)
- [ ] Synthese.md contient les 6 modules
- [ ] Navigation MkDocs fonctionne pour les 6 modules
- [ ] CI passe sans erreur
- [ ] Preview draft accessible avec les 6 modules

---

## Tests de validation

```bash
# Test 1 : 6 modules existent (+ template)
test $(ls docs/modules/*.md | grep -v "_template" | wc -l) -eq 6 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : Chaque nouveau module = 31 DINUM
for module in snum srh siep safi bgs; do
  count=$(grep -c "<!-- DINUM -->" docs/modules/$module.md)
  echo "$module: $count"
  test $count -eq 31 || echo "FAIL: $module"
done
# Attendu : 5x "31"

# Test 3 : Aucune checkbox cochée dans nouveaux modules
for module in snum srh siep safi bgs; do
  grep "\[x\].*<!-- DINUM -->" docs/modules/$module.md && echo "FAIL: $module a des cases cochées" || echo "OK: $module"
done
# Attendu : 5x "OK"

# Test 4 : Front-matter valide
for module in snum srh siep safi bgs; do
  python -c "
import yaml
content = open('docs/modules/$module.md').read()
fm = content.split('---')[1]
data = yaml.safe_load(fm)
assert 'service' in data, '$module: service manquant'
print('$module: OK')
  "
done
# Attendu : 5x "OK"

# Test 5 : Scoring global
python scripts/calculate_scores.py && grep -q "186" docs/synthese.md && echo "OK" || echo "FAIL"
# Attendu : OK (total 186 points)

# Test 6 : Navigation cohérente
test $(grep -c "modules/" mkdocs.yml) -eq 6 && echo "OK" || echo "FAIL"
# Attendu : OK
```

---

## Dépendances

**Bloque** :
- S3-02 (formation Git utilise les 6 modules)
- S3-03 (premiers contenus à ajouter dans ces modules)

**Dépend de** :
- S1-04 (template doit être validé)
- S1-05 (script scoring fonctionnel)
- S1-06 (SIRCOM comme référence)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 3 Onboarding
- **PRD v3.3** : Clarification périmètre v1 (6 modules)
- **docs/modules/_template.md** : Template à dupliquer
- **CLAUDE.md** : Section "Structure modulaire"

---

## Notes et risques

**Référents non identifiés**
Si les noms des référents ne sont pas encore connus, laisser placeholders :
```yaml
referent: "[À définir]"
```

Ils seront complétés lors de S3-02 (formation) ou ultérieurement.

**Ordre alphabétique vs logique métier**
Les modules sont affichés par ordre alphabétique dans la synthèse (script Python `sorted()`). Si un ordre spécifique est souhaité (ex: par importance), modifier le script ou la nav MkDocs.

**Modules vides = normal**
Le statut "Non renseigné" (0/31) est attendu à ce stade. Le contenu sera ajouté progressivement lors de S3-03 et après formation.

**Périmètre futur**
Seuls 6 modules en v1. Si d'autres directions demandent leur inclusion, créer leurs modules en phase 2+ selon le même process.

**Template évolutif**
Si le template `_template.md` évolue après cette story, penser à mettre à jour les 6 modules pour maintenir la cohérence.

---

## Post-tâche

Créer un fichier de suivi des référents :
```bash
cat > docs/referents.md << 'EOF'
# Référents accessibilité par service

| Service | Référent | Email | Date formation |
|---------|----------|-------|----------------|
| SNUM | [À définir] | | |
| SIRCOM | [Nom] | [email] | 2025-09-30 |
| SRH | [À définir] | | |
| SIEP | [À définir] | | |
| SAFI | [À définir] | | |
| BGS | [À définir] | | |

*Mis à jour : 2025-09-30*
EOF
```

Ajouter dans la nav MkDocs (optionnel) :
```yaml
nav:
  - Référents: referents.md
```

Informer les services :
```
📧 À : Directeurs SNUM, SRH, SIEP, SAFI, BGS
Objet : SPAN SG - Module de votre service créé

Votre module SPAN est maintenant disponible (structure vide) :
- SNUM : https://[repo]/blob/draft/docs/modules/snum.md
- SRH : https://[repo]/blob/draft/docs/modules/srh.md
- ...

Formation prévue : [date S3-02]
Merci de désigner un référent accessibilité d'ici là.
```