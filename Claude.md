# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Version: 1.1
Date: 2025-09-30

## Langue et ton
- Répondre en français, sans émojis, concision.
- Respecter strictement le MVP et le cahier des charges.

## Commandes essentielles

### Développement local
```bash
# Démarrer le serveur MkDocs en local (Docker)
docker compose up
# → http://localhost:8000/span-sg-repo/

# Sans Docker
pip install mkdocs-material mkdocs-pdf-export-plugin
mkdocs serve
```

### Build et génération
```bash
# Build site HTML
mkdocs build

# Générer PDF
mkdocs build --config-file mkdocs-pdf.yml

# Calculer les scores SPAN et générer docs/synthese.md
python scripts/calculate_scores.py
```

### Tests et validation
```bash
# Vérifier la configuration MkDocs (mode strict)
mkdocs build --strict

# Tester localement le scoring
python scripts/calculate_scores.py
# Attendu: 0 ou 31 points par module, sinon erreur
```

### Workflow Git
```bash
# Créer une branche feature pour un service
git checkout -b feature/update-[service]

# Après modifications
git add docs/modules/[service].md
git commit -m "feat(service): description concise"
git push -u origin feature/update-[service]
# → créer PR vers draft
```

## Architecture technique

### Pipeline de scoring (31 points DINUM)
Le système repose sur un **comptage strict** des cases cochées marquées `<!-- DINUM -->`:
- `scripts/calculate_scores.py` scanne `docs/modules/*.md`
- Recherche les lignes: `- [x] ... <!-- DINUM -->`
- Compte checked/total par module
- Échoue si total ≠ 0 ou 31 (validation périmètre)
- Génère `docs/synthese.md` avec tableau agrégé

**Règle absolue**: Ne jamais ajouter/supprimer de balises `<!-- DINUM -->`. Seules les coches `[x]` peuvent être modifiées.

### Structure modulaire
```
docs/modules/
├── _template.md         # Template avec 31 points DINUM officiels
├── snum.md             # 6 modules services v1
├── sircom.md
├── srh.md
├── siep.md
├── safi.md
└── bgs.md
```

Chaque module contient:
1. **Front-matter YAML**: service, referent, updated
2. **5 sections obligatoires**: Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs
3. **31 points de contrôle DINUM**: liste fixe avec `<!-- DINUM -->`
4. **Blocs légaux**: déclaration accessibilité, charge disproportionnée

### Configuration MkDocs
- `mkdocs.yml`: config principale (strict mode, nav, theme Material)
- `mkdocs-pdf.yml`: génération PDF via `mkdocs-pdf-export-plugin`

**Mode strict activé**: toute erreur de lien/référence bloque le build.

### CI/CD GitHub Actions
Workflow `.github/workflows/build.yml`:
1. Install Python + dépendances MkDocs
2. Calcul scores (`python scripts/calculate_scores.py`)
3. Build site (`mkdocs build`)
4. Génération PDF (`mkdocs build --config-file mkdocs-pdf.yml`)
5. Upload artefacts (site/ + exports/)
6. Déploiement conditionnel:
   - `draft` → `gh-pages/draft/` (preview)
   - `main` → `gh-pages/` (production)

### Branches et déploiements
- `main`: production (déployé sur Pages racine)
- `draft`: preview privée (déployé sur Pages /draft/)
- `feature/*`: modifications par service (PR vers draft)
- `hotfix/*`: corrections urgentes (PR vers main)

**Preview privée**: GitHub Pages restreint aux membres de l'organisation (paramètre org-only).

## Règles de modification

### Contraintes strictes
- Ne pas modifier la logique de scoring: 31 points balisés `<!-- DINUM -->` uniquement.
- Ne pas ajouter de dépendances ni de nouveaux plugins CI.
- Périmètre v1: 6 modules (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS).
- Aucune fonctionnalité hors périmètre (dashboard, API, notifications).
- Préserver `strict: true` dans `mkdocs.yml`.

### Modifications autorisées
- Cocher/décocher les cases `[x]` des 31 points DINUM
- Compléter les 5 sections obligatoires des modules
- Ajouter actions au plan 2025 (tableau)
- Renseigner URLs de déclaration d'accessibilité
- Mettre à jour front-matter (dates, référents)
- Corriger orthographe dans docs/ et PRD
- Préparer CHANGELOG pour releases

## Processus de release

### Préparer une version
```bash
# 1. Éditer CHANGELOG.md
# Ajouter section: ## vX.Y.Z – AAAA-MM-JJ

# 2. Créer tag
git tag -a vX.Y.Z -m "Release SPAN SG vX.Y.Z"
git push origin vX.Y.Z

# 3. Récupérer artefact PDF depuis Actions
# 4. Créer release GitHub avec exports/span-sg.pdf joint
```

### Checklist validation
- [ ] 31 points DINUM présents (ou 0 si module vide)
- [ ] Front-matter complet (service, referent, updated)
- [ ] Blocs légaux remplis ou TODO explicite
- [ ] Liens valides, pas de secrets
- [ ] CI passe (build + scoring + PDF)
- [ ] Preview draft accessible (org-only)

## Contacts et gouvernance
- **Owner**: Alexandra (@alexandra)
- **Validateurs**: Bertrand (@bertrand), Alex (@alex)
- **Sponsor**: Yves (validation production uniquement)

## Références
- PRD complet: `PRD-v3.3.md`
- Checklist GO: `GO-CHECKLIST.md`
- Paramétrage Pages: `.github/PAGES-ACCESS-CHECKLIST.md`
- Instructions Agents (Cursor/Codex): `Agents.md`
