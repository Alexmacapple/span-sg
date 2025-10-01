---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S2-04 : Documentation contributeur (1 page)

**Phase** : Semaine 2 - Automatisation
**Priorité** : Moyenne
**Estimation** : 1h
**Assigné** : Alexandra

---

## Contexte projet

Le SPAN SG est un projet **collaboratif décentralisé** : chaque service édite son propre module. Pour faciliter l'adoption, il faut une documentation contributeur **ultra-simple** (1 page max) avec :
- **Option A** : Interface GitHub (débutants, pas de Git)
- **Option B** : Git local (avancés, avec preview locale)

Objectifs de la doc :
- Permettre à un référent service de cocher des cases sans formation
- Expliquer le workflow PR → draft → validation → main
- Éviter la sur-documentation (principe directeur : simple, fonctionnel, efficace)

Public cible :
- Référents accessibilité des 6 services (profil non-technique)
- Équipe IT (Bertrand, Alex) pour revues
- Yves (sponsor, lecture seule)

---

## Objectif

Créer un fichier `CONTRIBUTING.md` d'1 page avec les deux options de contribution (GitHub web, Git local), intégrer dans la navigation MkDocs, et valider auprès d'un utilisateur test.

---

## Prérequis

- [ ] Story S1-06 complétée (module SIRCOM comme exemple)
- [ ] Story S2-03 complétée (preview privée pour tester workflow)
- [ ] Connaissance du workflow Git simplifié (PRD section 4)

---

## Étapes d'implémentation

### 1. Créer CONTRIBUTING.md

```bash
cat > CONTRIBUTING.md << 'EOF'
# Guide de contribution SPAN SG

## Principe

Chaque service gère son propre module dans `docs/modules/[service].md`.
Les modifications passent par une **Pull Request** vers `draft` pour validation.

---

## Option A : Interface GitHub (recommandé pour débutants)

**Pas besoin de Git, tout se fait dans le navigateur.**

### 1. Aller sur le fichier de votre service

https://github.com/Alexmacapple/span-sg-repo/blob/draft/docs/modules/[votre-service].md

Exemple : `sircom.md`, `snum.md`, `srh.md`, etc.

### 2. Cliquer sur l'icône ✏️ (Edit this file)

En haut à droite du fichier.

### 3. Modifier le contenu

**Ce que vous pouvez faire** :
- ✅ Cocher des cases `[x]` dans les 31 points DINUM
- ✅ Compléter les sections 1-5 (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- ✅ Ajouter des actions au tableau "Plan d'actions prioritaires"
- ✅ Renseigner l'URL de déclaration d'accessibilité

**Ce que vous ne devez PAS faire** :
- ❌ Ajouter/supprimer des lignes `<!-- DINUM -->`
- ❌ Modifier la structure (titres des sections)
- ❌ Toucher au front-matter (section `---` en haut)

### 4. Sauvegarder et créer la Pull Request

En bas de la page :
- **Commit message** : `feat(sircom): ajoute 3 actions au plan 2025` (exemple)
- ☑ **Create a new branch** : `update-sircom-[date]`
- Cliquer **Propose changes**

Sur la page suivante :
- **Base** : `draft` (important !)
- **Compare** : votre branche
- Cliquer **Create Pull Request**

### 5. Validation

Bertrand ou Alex reviendra la PR et la mergera si OK.
Vous recevrez une notification par email.

La preview sera visible sur : https://alexmacapple.github.io/span-sg-repo/draft/

---

## Option B : Git local (avancés)

**Nécessite Git installé localement.**

### 1. Cloner le repo

```bash
git clone https://github.com/Alexmacapple/span-sg-repo.git
cd span-sg-repo
```

### 2. Créer une branche feature

```bash
git checkout draft
git pull origin draft
git checkout -b feature/update-[votre-service]
```

### 3. Éditer votre module

```bash
# Ouvrir dans votre éditeur
code docs/modules/[votre-service].md

# OU
vim docs/modules/[votre-service].md
```

### 4. Prévisualiser en local (optionnel)

```bash
docker compose up
# Ouvrir http://localhost:8000/span-sg-repo/
```

### 5. Committer et pusher

```bash
git add docs/modules/[votre-service].md
git commit -m "feat(service): description des modifications"
git push -u origin feature/update-[votre-service]
```

### 6. Créer la Pull Request

Sur GitHub :
- Cliquer le lien affiché dans le terminal
- OU aller sur https://github.com/Alexmacapple/span-sg-repo/pulls → New Pull Request
- **Base** : `draft`
- **Compare** : votre branche

---

## Règles de validation des PR

Chaque PR est vérifiée automatiquement (CI) et manuellement (Bertrand/Alex) :

### Vérifications automatiques (CI)
- ✅ Exactement 31 points `<!-- DINUM -->` présents (ou 0 si module vide)
- ✅ Pas de liens cassés (mode strict MkDocs)
- ✅ Synthèse recalculée sans erreur

### Vérifications manuelles
- ✅ Front-matter à jour (service, referent, updated)
- ✅ Contenu cohérent et de qualité
- ✅ Blocs légaux remplis (déclaration accessibilité)
- ✅ Pas de secrets/informations sensibles

---

## Workflow complet

```
Service modifie son module
          ↓
   PR vers draft
          ↓
Revue Bertrand/Alex
          ↓
Merge dans draft → Preview privée
          ↓
PR draft → main (mensuel)
          ↓
Validation Yves → Production
```

---

## Besoin d'aide ?

- **Questions techniques** : Bertrand (@bertrand), Alex (@alex)
- **Questions contenu** : Alexandra (@alexandra)
- **Issues GitHub** : https://github.com/Alexmacapple/span-sg-repo/issues

---

**Principe directeur : Simple, fonctionnel, efficace.**
EOF
```

### 2. Ajouter CONTRIBUTING.md à la navigation MkDocs

**Solution retenue** : Copier dans docs/ (MkDocs ne supporte pas les liens relatifs hors de docs/)

```bash
cp CONTRIBUTING.md docs/contributing.md
```

Éditer `mkdocs.yml` :
```yaml
nav:
  - Accueil: index.md
  - Synthèse: synthese.md
  - Processus: processus.md
  - Guide contributeur: contributing.md
  - Modules Services:
    - SNUM: modules/snum.md
    - SIRCOM: modules/sircom.md
    # ...
```

**Note** : Garder CONTRIBUTING.md à la racine (standard GitHub) ET copie dans docs/

### 3. Tester le rendu

```bash
docker compose up
```

Ouvrir http://localhost:8000/span-sg-repo/contributing/ et vérifier :
- Sections Option A et Option B claires
- Code blocks formatés correctement
- Diagramme workflow lisible
- Liens fonctionnels

### 4. Créer un test utilisateur

**Scénario test débutant (Option A)** :
1. Envoyer le lien `CONTRIBUTING.md` à un collègue non-tech
2. Lui demander de cocher une case dans son module via GitHub web
3. Observer s'il bloque, où, et pourquoi
4. Ajuster la doc selon feedback

**Scénario test avancé (Option B)** :
1. Demander à Bertrand/Alex de cloner et créer une PR
2. Observer le temps nécessaire
3. Identifier les étapes confuses

### 5. Ajouter des captures d'écran (optionnel)

Si la doc textuelle ne suffit pas, ajouter screenshots :
```bash
mkdir docs/assets/contributing/
# Ajouter screenshots de l'interface GitHub
```

Intégrer dans CONTRIBUTING.md :
```markdown
### 2. Cliquer sur l'icône ✏️

![Bouton Edit](docs/assets/contributing/github-edit-button.png)
```

### 6. Créer un template de PR

`.github/PULL_REQUEST_TEMPLATE.md` :
```markdown
## Type de modification

- [ ] Mise à jour contenu module (coches, plan d'action)
- [ ] Correction erreur/typo
- [ ] Ajout URL déclaration accessibilité

## Module concerné

- [ ] SNUM
- [ ] SIRCOM
- [ ] SRH
- [ ] SIEP
- [ ] SAFI
- [ ] BGS

## Checklist

- [ ] J'ai testé en preview locale OU vérifié l'aperçu GitHub
- [ ] Je n'ai pas modifié les 31 lignes `<!-- DINUM -->` (sauf coches)
- [ ] J'ai mis à jour la date dans le front-matter
- [ ] Aucune information sensible/confidentielle

## Description

_(Décrire brièvement les modifications)_
```

### 7. Lier CONTRIBUTING.md depuis README

Ajouter dans `README.md` :
```markdown
## Contribution

Pour contribuer, consulter le [Guide contributeur](CONTRIBUTING.md).
```

### 8. Tester le workflow de bout en bout

Simulation complète :
```bash
# 1. Créer branche test
git checkout -b test/doc-contributeur

# 2. Modifier SIRCOM
sed -i '' 's/- \[ \] Stratégie/- [x] Stratégie/' docs/modules/sircom.md

# 3. Committer
git add docs/modules/sircom.md CONTRIBUTING.md
git commit -m "docs: ajoute guide contributeur + test SIRCOM"

# 4. Push
git push -u origin test/doc-contributeur

# 5. Créer PR via GitHub
# 6. Vérifier que CI passe
# 7. Merger dans draft
# 8. Vérifier preview mise à jour
```

---

## Critères d'acceptation

- [ ] `CONTRIBUTING.md` créé (< 200 lignes)
- [ ] Option A (GitHub web) documentée avec étapes numérotées
- [ ] Option B (Git local) documentée avec commandes
- [ ] Règles "À faire" et "Ne pas faire" claires
- [ ] Workflow complet expliqué (Service → draft → main)
- [ ] CONTRIBUTING.md accessible dans nav MkDocs
- [ ] Template PR créé (`.github/PULL_REQUEST_TEMPLATE.md`)
- [ ] Test utilisateur réussi (débutant peut créer PR)

---

## Tests de validation

```bash
# Test 1 : CONTRIBUTING.md existe
test -f CONTRIBUTING.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : Taille raisonnable (< 500 lignes)
test $(wc -l < CONTRIBUTING.md) -lt 500 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : Contient les deux options
grep -q "## Option A" CONTRIBUTING.md && grep -q "## Option B" CONTRIBUTING.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : Template PR existe
test -f .github/PULL_REQUEST_TEMPLATE.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 5 : Lien dans README
grep -q "CONTRIBUTING.md" README.md && echo "OK" || echo "FAIL"
# Attendu : OK
```

---

## Dépendances

**Bloque** :
- S3-02 (formation Git utilise CONTRIBUTING.md comme support)

**Dépend de** :
- S1-06 (module SIRCOM comme exemple)
- S2-03 (preview privée pour workflow complet)

---

## Références

- **PRD v3.3** : Section 7 "Guide contributeur (1 page)"
- **PRD v3.3** : Section 4 "Workflow Git simplifié"
- **CONTRIBUTING.md** : Fichier à créer
- **.github/PULL_REQUEST_TEMPLATE.md** : Template à créer

---

## Notes et risques

**URLs actuelles vs migration future**
- URLs actuelles : `Alexmacapple/span-sg-repo` (compte utilisateur)
- Migration prévue : Vers organisation GitHub lors de la mise en production
- Note ajoutée dans CONTRIBUTING.md pour informer les contributeurs

**Éviter la sur-documentation**
Résister à la tentation d'ajouter :
- Explications Git avancées (rebase, cherry-pick)
- Conventions de code détaillées
- Process de release (réservé à l'équipe core)

Garder focus : **comment un référent service modifie son module**.

**Barrière d'entrée GitHub**
Même avec Option A (web), certains utilisateurs peuvent :
- Ne pas avoir de compte GitHub
- Ne pas comprendre le concept de PR
- Avoir peur de "casser" quelque chose

Solutions :
- Session onboarding 30 min (S3-02)
- Vidéo screencast de 3 min (optionnel)
- Support 1-to-1 au besoin

**Maintenance de la doc**
CONTRIBUTING.md doit évoluer avec le projet. Prévoir revue trimestrielle.

**Langue**
Doc en français (contrainte projet). Si futurs contributeurs anglophones, créer `CONTRIBUTING.en.md`.

---

## Post-tâche

Créer un "premier contributeur" fictif pour tester :
1. Créer un compte GitHub test
2. Lui donner accès lecture seule au repo
3. Lui demander de suivre CONTRIBUTING.md et créer une PR
4. Noter les blocages et améliorer la doc

Annoncer la doc à l'équipe :
```
📧 À : Référents services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
Objet : SPAN SG - Guide de contribution disponible

Le guide de contribution est maintenant disponible :
https://github.com/Alexmacapple/span-sg-repo/blob/draft/CONTRIBUTING.md

Deux méthodes selon votre niveau :
- Option A : Interface web GitHub (recommandé, pas de Git)
- Option B : Git local (si à l'aise avec terminal)

Formation prévue : [date S3-02]
```