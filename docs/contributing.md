# Guide de contribution SPAN SG

## Principe

Chaque service gère son propre module dans `docs/modules/[service].md`.
Les modifications passent par une **Pull Request** vers `draft` pour validation.

---

## Option A : Interface GitHub (recommandé pour débutants)

**Pas besoin de Git, tout se fait dans le navigateur.**

### 1. Aller sur le fichier de votre service

https://github.com/Alexmacapple/span-sg-repo/blob/main/docs/modules/[votre-service].md

Exemple : `sircom.md`, `snum.md`, `srh.md`, etc.

### 2. Cliquer sur "Edit this file"

En haut à droite du fichier (icône crayon).

### 3. Modifier le contenu

**Ce que vous pouvez faire** :

- Cocher des cases `[x]` dans les 31 points DINUM
- Compléter les sections 1-5 (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- Ajouter des actions au tableau "Plan d'actions prioritaires"
- Renseigner l'URL de déclaration d'accessibilité

**Ce que vous ne devez PAS faire** :

- Ajouter/supprimer des lignes `<!-- DINUM -->`
- Modifier la structure (titres des sections)
- Toucher au front-matter (section `---` en haut)

### 4. Sauvegarder et créer la Pull Request

En bas de la page :

- **Commit message** : `feat(sircom): ajoute 3 actions au plan 2025` (exemple)
- Cocher **Create a new branch** : `update-sircom-[date]`
- Cliquer **Propose changes**

Sur la page suivante :

- **Base** : `draft` (important !)
- **Compare** : votre branche
- Cliquer **Create Pull Request**

### 5. Validation

Bertrand ou Alex reviendra la PR et la mergera si OK.
Vous recevrez une notification par email.

Preview désactivée : revue locale/PDF. Voir `docs/dev-local.md` et `.github/PAGES-ACCESS-CHECKLIST.md`.

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

## Qualité code Python

Si vous contribuez au code Python (`scripts/`), suivez ces règles :

### Tests unitaires

Le projet utilise pytest avec une structure organisée :

```
tests/
├── unit/              # Tests unitaires (scripts et hooks)
│   ├── scripts/       # Tests pour scripts/calculate_scores.py, enrich_pdf_metadata.py
│   └── hooks/         # Tests pour hooks MkDocs DSFR
├── e2e/               # Tests end-to-end (Selenium + accessibility)
└── test_*.py          # Tests d'intégration
```

**Commandes essentielles :**
```bash
# Tous les tests unitaires
pytest tests/unit/ -v

# Tests scripts avec coverage (89% requis)
pytest tests/unit/scripts/ --cov=scripts --cov-fail-under=89

# Tests hooks avec coverage strict (100% requis)
pytest tests/unit/hooks/ --cov=hooks --cov-config=.coveragerc-hooks --cov-fail-under=100
```

Voir `tests/README.md` pour la documentation complète.

### Pre-commit hooks (fortement recommandé)

Les pre-commit hooks **valident automatiquement votre code avant chaque commit**, évitant ainsi les erreurs CI.

**Configuration incluse :** `.pre-commit-config.yaml`

Hooks actifs :
1. **Bandit** : Détection failles sécurité (scripts/, hooks/)
2. **Safety** : Vérification vulnérabilités dépendances (CVE)
3. **Black** : Formatage code Python automatique
4. **Ruff** : Linting avec auto-fix activé

**Installation (une fois) :**
```bash
# Installer pre-commit
pip install pre-commit

# Activer les hooks dans votre clone local
pre-commit install

# Tester sur tous les fichiers
pre-commit run --all-files
```

**Utilisation :**
Une fois installé, les hooks s'exécutent automatiquement à chaque `git commit`.

Si un hook échoue :
- **Black** : Le code est reformaté automatiquement → Re-commiter
- **Ruff** : Les erreurs sont corrigées si possible → Re-commiter
- **Bandit** : Failles détectées → Corriger manuellement
- **Safety** : Vulnérabilités trouvées → Mettre à jour dépendances

**Bypass temporaire (déconseillé) :**
```bash
git commit --no-verify -m "message"
```

### Formatting et linting manuels

Si vous préférez valider manuellement avant commit :

```bash
# Formater avec Black
black scripts/ hooks/

# Vérifier avec Ruff
ruff check scripts/ hooks/

# Sécurité Bandit
bandit -r scripts/ hooks/ -ll

# Vulnérabilités Safety
safety check -r requirements-dsfr.txt
```

### Installation environnement dev
```bash
# Dépendances dev (pytest, coverage, etc.)
pip install -r requirements-dev.txt

# Dépendances sécurité (bandit, safety)
pip install -r requirements-security.txt

# Activer pre-commit
pre-commit install
```

---

## Règles de validation des PR

Chaque PR est vérifiée automatiquement (CI) et manuellement (Bertrand/Alex) :

### Vérifications automatiques (CI)
- Tests unitaires Python (pytest)
- Formatting Black et linting Ruff
- Exactement 31 points `<!-- DINUM -->` présents (ou 0 si module vide)
- Pas de liens cassés (mode strict MkDocs)
- Synthèse recalculée sans erreur

### Vérifications manuelles
- Front-matter à jour (service, referent, updated)
- Contenu cohérent et de qualité
- Blocs légaux remplis (déclaration accessibilité)
- Pas de secrets/informations sensibles

---

## Workflow complet

```
Service modifie son module
          ↓
   PR vers main
          ↓
Revue Bertrand/Alex
          ↓
Merge dans draft → Revue locale/PDF (sans Pages)
          ↓
PR main → main (mensuel)
          ↓
Validation Yves → Production
```

---

## Besoin d'aide ?

- **Questions techniques** : Bertrand (@bertrand), Alex (@alex)
- **Questions contenu** : Alexandra (@alexandra)
- **Issues GitHub** : <https://github.com/Alexmacapple/span-sg-repo/issues>

---

**Principe directeur : Simple, fonctionnel, efficace.**

---

## Note sur les URLs

**URLs actuelles** : Ce projet est hébergé sur `Alexmacapple/span-sg-repo` (compte utilisateur).

**Migration prévue** : Lors de la mise en production, le dépôt sera transféré vers une organisation GitHub. Les URLs seront mises à jour à ce moment-là.
