# ADR-002: Migration synthèse Markdown → HTML DSFR

**Date**: 2025-10-08
**Statut**: ✅ Accepted
**Décideurs**: Alexandra, Alex
**Implémenté par**: calculate_scores.py

## Contexte

Initialement, `docs/synthese.md` utilisait tableau Markdown standard :
```markdown
| Service | Score | Statut | État |
|---------|-------|--------|------|
| SIRCOM  | 24/31 | Conforme | Validé |
```

**Problèmes:**
- ❌ Pas de bordures verticales (design limité)
- ❌ Non conforme composants DSFR
- ❌ Pas de classes accessibilité ARIA
- ❌ Responsive limité sur mobile

## Décision

Générer synthèse en **HTML DSFR natif** via `calculate_scores.py`.

**Format output:**
```html
<div class="fr-table fr-table--bordered" id="table-synthese-span">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table id="table-span-modules">
                    <caption>Synthèse modules SPAN</caption>
                    <thead><tr><th scope="col">Service</th>...</tr></thead>
                    <tbody>
                        <tr id="table-span-row-sircom" data-row-key="sircom">
                            <td>SIRCOM</td>
                            <td>24/31 (77.4%)</td>
                            ...
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

**Justification:** Conformité DSFR + accessibilité RGAA + design gouvernemental.

## Alternatives considérées

### Option A: Markdown table standard (rejeté)
- **Avantages**: Simple, lisible source
- **Inconvénients**: ❌ Non DSFR, ❌ Pas bordures, ❌ Accessibilité limitée
- **Rejeté**: Non conforme DSFR

### Option B: HTML avec hook post-processing (rejeté)
- **Avantages**: Génère Markdown, hook convertit HTML
- **Inconvénients**: ❌ Complexité double (Markdown + hook), ❌ Maintenance difficile
- **Rejeté**: Sur-ingénierie

### Option C: HTML DSFR direct (choisi)
- **Avantages**: ✅ Conforme DSFR natif, ✅ Bordures verticales, ✅ Accessibilité ARIA, ✅ IDs stables
- **Inconvénients**: ⚠️ HTML verbeux dans source
- **Choisi**: Conformité > Lisibilité source

## Conséquences

**Positives:**
- ✅ Tableau conforme DSFR (`fr-table`, `fr-table--bordered`)
- ✅ Accessibilité RGAA (`<caption>`, `scope="col"`, `data-row-key`)
- ✅ Bordures verticales design
- ✅ IDs stables pour tests E2E

**Négatives:**
- ⚠️ Source HTML verbeux (vs Markdown compact)
- ⚠️ Tests E2E adaptés nécessaires (voir fix 2025-10-11)

**Impact tests E2E:**
```bash
# AVANT (Markdown)
grep -q '| SIRCOM | 24/31' docs/synthese.md

# APRÈS (HTML)
grep -q '24/31 (' docs/synthese.md  # Pattern robuste
```

## Validation

**Critères:**
- [x] Tableau renderisé avec bordures verticales
- [x] Composants DSFR (`fr-table`, wrappers)
- [x] Accessibilité (`<caption>`, `scope`, ARIA)
- [x] Tests E2E adaptés et passent

**Vérification:**
```bash
grep -q 'fr-table--bordered' docs/synthese.md  # ✅ OK
grep -q 'scope="col"' docs/synthese.md          # ✅ OK
grep -q 'data-row-key' docs/synthese.md         # ✅ OK
```

## Références

- Commit: `ae2d30b` (feat: tableau DSFR avec bordures)
- Tests E2E fix: Commit `9d06298` (2025-10-11)
- DSFR Tables: https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/tableau/
- Script: `scripts/calculate_scores.py` (fonction `generate_summary()`)
