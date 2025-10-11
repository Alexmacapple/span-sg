# ADR-003: Isolation build PDF avec --site-dir pdf-temp

**Date**: 2025-10-10
**Statut**: ✅ Accepted
**Décideurs**: Claude Code, Alexandra
**Contexte**: Bug déploiement DSFR (ReadTheDocs écrasait HTML)

## Contexte

Le workflow CI générait 2 builds séquentiels:
1. HTML DSFR: `mkdocs build --config-file mkdocs-dsfr.yml` → `site/`
2. PDF: `mkdocs build --config-file mkdocs-dsfr-pdf.yml` → `site/` (ÉCRASE!)

**Problème:** Build PDF (thème ReadTheDocs) écrasait build HTML (thème DSFR), déployant ReadTheDocs sur GitHub Pages au lieu de DSFR.

**Symptômes:**
- Local: DSFR fonctionne ✅
- CI validation: HTML contient DSFR ✅
- GitHub Pages: ReadTheDocs déployé ❌

**Root cause:** Deux builds utilisent même répertoire output `site/`, le second écrase le premier.

## Décision

Isoler build PDF dans répertoire temporaire distinct avec `--site-dir pdf-temp`.

**Modification:** `.github/workflows/build.yml`
```yaml
# AVANT
- name: Generate PDF (DSFR)
  run: |
    mkdir -p exports
    mkdocs build --config-file mkdocs-dsfr-pdf.yml

# APRÈS
- name: Generate PDF (DSFR)
  run: |
    mkdir -p exports
    mkdocs build --config-file mkdocs-dsfr-pdf.yml --site-dir pdf-temp
```

**Justification:** Build HTML et PDF utilisent thèmes différents, doivent être isolés. PDF final copié vers `exports/`, pas `site/`.

## Alternatives considérées

### Option A: Même thème (DSFR) pour HTML et PDF (rejeté)
- **Problème**: mkdocs-with-pdf ne supporte pas mkdocs-dsfr
- **Rejeté**: Incompatibilité technique

### Option B: Build PDF en premier (rejeté)
- **Problème**: HTML DSFR écrasé quand même, ordre inversé ne change rien
- **Rejeté**: Ne résout pas le problème

### Option C: --site-dir pdf-temp (choisi)
- **Avantages**: ✅ Isolation complète, ✅ Change 1 ligne, ✅ Rétrocompatible, ✅ Aucune refonte
- **Choisi**: Solution élégante et minimale

## Conséquences

**Positives:**
- ✅ `site/` contient toujours DSFR
- ✅ `pdf-temp/` isolé (ajouté à .gitignore)
- ✅ Déploiement DSFR fonctionne
- ✅ Build time inchangé

**Négatives:**
- ⚠️ Nouveau répertoire temporaire (pdf-temp/)
- ⚠️ Ajout .gitignore requis

## Validation

**Tests locaux:**
```bash
# Build HTML
mkdocs build --config-file mkdocs-dsfr.yml
grep -q "data-fr-scheme" site/index.html  # ✅ DSFR

# Build PDF
mkdocs build --config-file mkdocs-dsfr-pdf.yml --site-dir pdf-temp
grep -q "data-fr-scheme" site/index.html  # ✅ TOUJOURS DSFR
test -f exports/span-sg.pdf                # ✅ PDF généré
```

**Résultat:** Draft GitHub Pages déploie DSFR ✅

## Leçons apprises

**Ce qui a bien fonctionné:**
- Tests locaux reproductibles (Docker)
- Validation HTML à chaque étape
- Solution minimale (1 paramètre)

**Ce qui aurait aidé:**
- ADR documenté lors première décision thème
- Tests E2E validant thème déployé
- CI validation post-déploiement

## Références

- Debug session: 2025-10-10 (5h intensive)
- Commit fix: `e7a5b7c` (fix: isoler build PDF)
- Tests: Draft Pages déploie DSFR ✅
- Production: v1.0.1-dsfr
