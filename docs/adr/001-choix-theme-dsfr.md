# ADR-001: Adoption du thème DSFR pour accessibilité RGAA

**Date**: 2025-10-08
**Statut**: ✅ Accepted
**Décideurs**: Alexandra, Bertrand, Alex
**Sponsor**: Stéphane (Chef mission numérique SNUM-SG)

## Contexte

Le projet SPAN SG nécessite conformité RGAA stricte pour déploiement gouvernemental. Le thème initial (MkDocs Material) offrait bon rendu mais ne garantissait pas conformité DSFR (Système de Design de l'État).

**Contraintes:**
- Accessibilité RGAA obligatoire (référentiel gouvernemental)
- Design cohérent avec autres sites gouv.fr
- Header/footer officiels avec Marianne
- Maintenance long terme garantie

## Décision

Adopter **mkdocs-dsfr v0.17.0** pour toutes pages HTML.

**Config:** `mkdocs-dsfr.yml`
```yaml
theme:
  name: dsfr
  language: fr
```

**Justification:** Conformité RGAA native + design gouvernemental officiel + maintenance DINUM.

## Alternatives considérées

### Option A: MkDocs Material (rejeté)
- **Avantages**: Rendu moderne, écosystème riche, documentation exhaustive
- **Inconvénients**: ❌ Non conforme DSFR, ❌ Customisation lourde pour RGAA, ❌ Pas header/footer gouv
- **Rejeté**: Non conforme exigences gouvernementales

### Option B: Thème custom from scratch (rejeté)
- **Avantages**: Contrôle total, optimisation performance
- **Inconvénients**: ❌ Coût >100h développement, ❌ Maintenance complexe, ❌ Risque non-conformité
- **Rejeté**: ROI négatif

### Option C: mkdocs-dsfr (choisi)
- **Avantages**: ✅ Conformité RGAA native, ✅ Design gouvernemental, ✅ Maintenance DINUM, ✅ Installation simple
- **Inconvénients**: ⚠️ Moins plugins que Material, ⚠️ Customisation limitée
- **Choisi**: Avantages > Inconvénients pour contexte gouvernemental

## Conséquences

**Positives:**
- ✅ Conformité RGAA garantie
- ✅ Design cohérent sites gouv.fr
- ✅ Composants accessibles (tables, nav, boutons)
- ✅ Validation automatique CI

**Négatives:**
- ⚠️ Migration depuis Material (1-2j travail)
- ⚠️ Hooks Python requis pour tables responsives (voir ADR-004)
- ⚠️ PDF nécessite thème différent (voir ADR-003)

**Risques atténués:**
- **Risque:** Thème non maintenu → **Mitigation:** Thème officiel DINUM, support LTS
- **Risque:** Bugs bloquants → **Mitigation:** Hooks Python pour corrections

## Validation

**Critères succès:**
- [x] Site génère avec DSFR
- [x] HTML contient `data-fr-scheme`
- [x] Tables wrappées `<div class="fr-table">`
- [x] Header/footer Marianne présents

**Tests:**
```bash
mkdocs build --config-file mkdocs-dsfr.yml --strict
grep -q "data-fr-scheme" site/index.html  # ✅ OK
grep -q 'class="fr-table"' site/index.html  # ✅ OK
```

## Références

- [DSFR Documentation](https://www.systeme-de-design.gouv.fr/)
- [mkdocs-dsfr PyPI](https://pypi.org/project/mkdocs-dsfr/)
- [RGAA 4.1](https://accessibilite.numerique.gouv.fr/)
- Commit: `ae2d30b` (feat: tableau DSFR)
- Production: v1.0.1-dsfr (2025-10-10)
