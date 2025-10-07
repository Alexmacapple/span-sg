# S2-11 — PRD détaillé: Évaluation dépôt et actions prioritaires

## Contexte
- Dépôt public personnel (Alexmacapple/span-sg-repo). Objectif: éviter toute exposition publique avant validation.
- Site MkDocs strict, 6 modules v1 (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS), scoring DINUM (31 points), PDF.
- Décision: preview GitHub Pages désactivée; revue locale + PDF CI.

## Objectifs
- Sécuriser la livraison documentaire (strict, sans Pages) et la qualité modules.
- Centraliser les consignes agent et éviter les divergences.
- Valider la reproductibilité (build HTML + PDF) sans modifier la CI.

## Périmètre (IN/OUT)
- IN: Documentation, configuration MkDocs, vérifications locales, consolidation des guides.
- OUT: Ajout de dépendances, modification de workflows CI (lecture seule uniquement).

## Actions prioritaires (Do Now)
1) Vérification CI (lecture seule)
- Fichier: `.github/workflows/build.yml`
- But: confirmer qu’aucun déploiement non désiré vers `gh-pages` n’est actif.

2) Centralisation consignes agent
- Fusionner le contenu de `Agents.md` → `AGENTS.md` (source unique).
- Laisser `Agents.md` avec un court message de redirection vers `AGENTS.md`.

3) Contrôle qualité modules
- Vérifier balises DINUM (31 exactes ou 0 si vide), front‑matter, liens.
- Commandes:
```bash
# Compter les balises DINUM par module
rg -n "<!-- DINUM -->" docs/modules | awk -F: '{print $1}' | sort | uniq -c
# Vérifier front‑matter minimal
rg -n "^---|^service:|^referent:|^updated:" docs/modules
```

4) Validation build + PDF (local)
- Commandes:
```bash
mkdocs build -f mkdocs.yml              # strict déjà activé
mkdocs build -f mkdocs-pdf.yml          # génération PDF
```

## Exigences et garde‑fous
- Ne pas modifier la règle DINUM ni le comptage (31 cases existantes uniquement).
- Préserver `strict: true` dans `mkdocs.yml`.
- Pas de nouvelles dépendances ni scripts.
- Aucune activation de GitHub Pages.

## Critères d’acceptation
- CI vérifiée: aucun job `gh-pages` actif non souhaité.
- `AGENTS.md` = source unique; `Agents.md` pointe vers `AGENTS.md`.
- Modules: 0 anomalie critique (DINUM correct, front‑matter présent, liens valides).
- Builds locaux HTML + PDF passent sans erreur.

## Améliorations facultatives (Next)
- Documenter dans README un drapeau/section “Preview désactivée (sans Pages)” pour rappel équipe.
- Unifier `CONTRIBUTING.md` et `docs/contributing.md` (un master, l’autre redirige).

## Rôles et validation
- Owner: Alexandra
- Revue/validation technique: Bertrand, Alex
- Sponsor: Stéphane (validation conceptuelle)
- GO production: Chef SNUM

## Planification (indicative)
- J0: Vérifs CI + consolidation AGENTS
- J1: Audit modules + corrections minimes
- J2: Builds de validation + PR vers `draft`
