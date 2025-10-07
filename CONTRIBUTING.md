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

## Tests et Coverage

### Exécuter tests localement

```bash
# Tests unitaires seuls
pytest scripts/test_*.py -v

# Tests avec coverage production (89%+ requis)
./scripts/check_coverage.sh

# Générer rapport HTML
pytest --cov=scripts --cov-report=html scripts/test_*.py
open tests/htmlcov/index.html
```

### Objectif Coverage

**Scripts production** : 89%+ obligatoire (calculate_scores, enrich_pdf_metadata)
- CI bloquée si coverage < 89%
- Configuration .coveragerc exclut scripts dev + __main__ blocks
- Rapport généré automatiquement dans Actions

**Scripts développement** : Non requis (add-bmad-headers, evaluate-bmad-final)
- Outils internes, non utilisés en production
- Tests optionnels

### Ajouter nouveaux tests

1. Créer fichier `test_[module].py` dans `scripts/`
2. Run coverage : `./scripts/check_coverage.sh`
3. Viser 89%+ pour modules production
4. Commit avec tests inclus

### Note Coverage ImportError

Les lignes 23-26 de `enrich_pdf_metadata.py` (ImportError pikepdf) ne sont pas testées :
- Import top-level difficile à mocker proprement
- pikepdf toujours installé (requirements.txt + CI + Docker)
- Edge case non critique (erreur claire si pikepdf absent)
- Coverage production scripts : 89.6% acceptable

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
Présentation Stéphane → Validation Chef SNUM → Production
```

---

## Besoin d'aide ?

- **Questions techniques** : Bertrand (@bertrand), Alex (@alex)
- **Questions contenu** : Alexandra (@alexandra)
- **Issues GitHub** : https://github.com/Alexmacapple/span-sg-repo/issues

---

**Principe directeur : Simple, fonctionnel, efficace.**

---

## Note sur les URLs

**URLs actuelles** : Ce projet est hébergé sur `Alexmacapple/span-sg-repo` (compte utilisateur).

**Migration prévue** : Lors de la mise en production, le dépôt sera transféré vers une organisation GitHub. Les URLs seront mises à jour à ce moment-là.
