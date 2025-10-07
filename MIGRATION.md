# Guide de Migration SPAN SG

Ce document décrit les procédures de migration entre versions majeures de SPAN SG.

---

## Migration v0.x → v1.0

**Date** : 2025-10-07
**Type** : Stable (POC → Production)

### Breaking Changes

Aucun breaking change (v0.x était POC interne non publié).

### Nouvelles Fonctionnalités

Voir [CHANGELOG.md](CHANGELOG.md#v100-poc---2025-10-07) pour liste exhaustive.

### Procédure Migration

**Depuis v0.x (POC interne)** :

```bash
# 1. Backup données existantes
cp -r docs/modules /tmp/backup-modules-$(date +%Y%m%d)

# 2. Pull dernière version
git fetch origin
git checkout main
git pull origin main

# 3. Mettre à jour dépendances
pip install -r requirements.txt --upgrade

# 4. Vérifier configuration
mkdocs build --strict

# 5. Recalculer scores
python scripts/calculate_scores.py

# 6. Tester localement
docker compose up
# Ouvrir http://localhost:8000/span-sg-repo/
```

**Vérifications post-migration** :
- [ ] `mkdocs build --strict` passe sans erreur
- [ ] `python scripts/calculate_scores.py` génère `docs/synthese.md`
- [ ] CI passe (push vers draft)
- [ ] Preview locale accessible
- [ ] PDF généré (`exports/span-sg.pdf`)

---

## Migration v1.x → v2.0

**Date** : À déterminer
**Type** : Breaking (changements structure modules)

### Breaking Changes Prévus

#### 1. Structure Points DINUM

**Avant (v1.x)** : 31 points DINUM officiels
**Après (v2.0)** : 50 points DINUM étendus (hypothèse)

**Impact** :
- Scripts scoring : Adaptation nécessaire (`calculate_scores.py`)
- Modules existants : Ajout 19 nouveaux points
- Tests unitaires : Mise à jour assertions (31 → 50)

**Action requise** :
```bash
# Backup avant migration
cp -r docs/modules /tmp/backup-v1-modules

# Exécuter script migration automatique (fourni en v2.0)
python scripts/migrate_v1_to_v2.py

# Vérifier diff
git diff docs/modules/
```

#### 2. Front-matter YAML

**Avant (v1.x)** :
```yaml
---
service: SIRCOM
referent: Jean Dupont
updated: 2025-10-07
validation_status: validated
---
```

**Après (v2.0)** :
```yaml
---
service: SIRCOM
referent:
  name: Jean Dupont
  email: jean.dupont@sg.gouv.fr
updated: 2025-10-07
validation:
  status: validated
  date: 2025-10-07
  reviewer: Alexandra
---
```

**Action requise** :
- Script migration fourni : `scripts/migrate_frontmatter_v2.py`
- Validation manuelle front-matter après migration

#### 3. Structure Sections

**Avant (v1.x)** : 5 sections obligatoires
**Après (v2.0)** : 7 sections (ajout Budget + Gouvernance)

**Nouvelles sections** :
- Section 6 : Budget Accessibilité (k€, ETP)
- Section 7 : Gouvernance (comité, fréquence réunions)

**Action requise** :
```bash
# Ajouter templates nouvelles sections
python scripts/add_v2_sections.py docs/modules/*.md

# Compléter manuellement Budget + Gouvernance
```

### Procédure Migration v1 → v2

#### Étape 1 : Préparation (30 min)

```bash
# 1. Backup complet
cd /Users/alex/Desktop
cp -r span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts \
     span-sg-repo-BACKUP-v1-$(date +%Y%m%d)

# 2. Créer branche migration
cd span-sg-repo-skeleton-v3.3-GO-ready-plus-enrichissements-agents-prompts
git checkout -b migration/v1-to-v2

# 3. Télécharger release v2.0.0
git fetch origin
git checkout v2.0.0
```

#### Étape 2 : Migration Automatique (1h)

```bash
# 1. Exécuter script migration points DINUM (31 → 50)
python scripts/migrate_v1_to_v2.py \
  --input /tmp/backup-v1-modules \
  --output docs/modules

# 2. Migrer front-matter YAML
python scripts/migrate_frontmatter_v2.py docs/modules/*.md

# 3. Ajouter sections Budget + Gouvernance
python scripts/add_v2_sections.py docs/modules/*.md

# 4. Recalculer scores (nouveau système 50 points)
python scripts/calculate_scores.py

# 5. Vérifier build
mkdocs build --strict
```

#### Étape 3 : Validation Manuelle (2h)

```bash
# 1. Review diff modules
git diff /tmp/backup-v1-modules docs/modules/

# 2. Compléter manuellement 19 nouveaux points DINUM
# Éditer chaque module : docs/modules/*.md

# 3. Remplir nouvelles sections (Budget + Gouvernance)
# Section 6 : Budget (k€, ETP dédiés)
# Section 7 : Gouvernance (comité, fréquence)

# 4. Tester localement
docker compose up
# Ouvrir http://localhost:8000/span-sg-repo/

# 5. Vérifier synthèse
cat docs/synthese.md
# Attendu : Scores sur /50 points, /300 total (6 modules)
```

#### Étape 4 : Tests & Commit (30 min)

```bash
# 1. Tests unitaires (nouvelles assertions)
pytest scripts/test_*.py -v

# 2. Tests E2E
./tests/e2e/ci_runner.sh

# 3. Commit migration
git add docs/modules/*.md scripts/*.py
git commit -m "migrate: v1.0.x → v2.0.0 (31 → 50 points DINUM)

Breaking changes:
- Points DINUM: 31 → 50 (+19 points étendus)
- Front-matter: structure YAML étendue (referent.email, validation.reviewer)
- Sections: 5 → 7 (ajout Budget + Gouvernance)

Migration automatique:
- scripts/migrate_v1_to_v2.py (points DINUM)
- scripts/migrate_frontmatter_v2.py (YAML)
- scripts/add_v2_sections.py (Budget + Gouvernance)

Validation manuelle:
- 19 nouveaux points DINUM complétés
- Budget + Gouvernance renseignés (6 modules)
- Tests unitaires + E2E adaptés

Score migration:
- Avant: 45/186 (24.2%) sur 31 points
- Après: XX/300 (XX%) sur 50 points

Refs: roadmap/MIGRATION-v2.md"

# 4. Pusher branche migration
git push -u origin migration/v1-to-v2

# 5. Créer PR vers main
gh pr create --title "migrate: v1.0 → v2.0 (50 points DINUM)" \
  --body "Voir MIGRATION.md pour détails" \
  --base main
```

### Rollback v2 → v1 (si problèmes)

```bash
# 1. Restaurer backup
rm -rf docs/modules
cp -r /tmp/backup-v1-modules docs/modules

# 2. Downgrade dépendances
git checkout v1.0.x
pip install -r requirements.txt

# 3. Recalculer scores v1
python scripts/calculate_scores.py

# 4. Vérifier build
mkdocs build --strict
```

---

## FAQ Migration

### Q1 : Puis-je migrer progressivement module par module ?

**Réponse** : Non. Migration v1 → v2 est globale (31 → 50 points) car `calculate_scores.py` attend structure homogène. Migrer tous modules en une fois via `scripts/migrate_v1_to_v2.py`.

### Q2 : Les URLs modules changent-elles en v2 ?

**Réponse** : Non. Structure MkDocs et URLs identiques (`/modules/sircom/`, `/modules/snum/`, etc.). Seul contenu interne modules change (50 points au lieu de 31).

### Q3 : Dois-je refaire audits accessibilité après migration v2 ?

**Réponse** : Non si périmètre applicatif inchangé. Audits RGAA valides restent valides. Simplement ajouter 19 nouveaux points DINUM (organisationnels, pas techniques).

### Q4 : Migration cassera-t-elle ma CI ?

**Réponse** : Oui temporairement. Tests unitaires assertent `31 points` → Adapter à `50 points`. PR migration inclut mise à jour tests (`scripts/test_calculate_scores.py`).

### Q5 : Combien de temps prend migration v1 → v2 ?

**Réponse** :
- Automatique : 1h (scripts migration)
- Manuelle : 2h (compléter 19 nouveaux points × 6 modules)
- Tests : 30 min
- **Total : ~4h** pour 6 modules

### Q6 : Puis-je rester en v1.x indéfiniment ?

**Réponse** : Oui. v1.x supportée tant que 31 points DINUM officiels. Migrer v2 seulement si DINUM étend référentiel (annonce publique).

---

## Compatibilité Versions

| Version | Python | MkDocs Material | Docker | Status |
|---------|--------|-----------------|--------|--------|
| v0.x | 3.9+ | 9.0+ | 20+ | ❌ Obsolète |
| v1.0.x | 3.11+ | 9.5+ | 24+ | ✅ Stable |
| v2.0.x | 3.12+ | 10.0+ | 26+ | 🚧 Prévu |

---

## Support et Aide

**Problèmes migration** :
1. Consulter [CHANGELOG.md](CHANGELOG.md) (breaking changes détaillés)
2. Ouvrir issue GitHub : https://github.com/Alexmacapple/span-sg-repo/issues
3. Contacter mainteneurs : @Alexmacapple

**Documentation complémentaire** :
- [CONTRIBUTING.md](CONTRIBUTING.md) : Workflow contributeur
- [SECURITY.md](SECURITY.md) : Signaler vulnérabilités
- [README.md](README.md) : Installation + Quick Start

---

**Date document** : 2025-10-07
**Auteur** : Claude Code
**Version** : 1.0.0
