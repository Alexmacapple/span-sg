# Architecture Decision Records (ADR)

Historique des décisions techniques majeures du projet SPAN SG.

Format: [MADR (Markdown Any Decision Records)](https://adr.github.io/madr/)

Version: 1.0.1-dsfr
Dernière mise à jour: 2025-10-11

---

## Index

| ADR | Titre | Date | Statut |
|-----|-------|------|--------|
| [001](001-choix-theme-dsfr.md) | Adoption thème DSFR vs Material | 2025-10-08 | ✅ Accepted |
| [002](002-format-synthese-html.md) | Migration synthèse Markdown → HTML DSFR | 2025-10-08 | ✅ Accepted |
| [003](003-isolation-pdf-build.md) | Isolation build PDF avec --site-dir | 2025-10-10 | ✅ Accepted |
| [004](004-hooks-python-mkdocs.md) | Architecture hooks Python vs JavaScript | 2025-10-08 | ✅ Accepted |
| [005](005-coverage-89-percent.md) | Seuil coverage 89%+ enforced | 2025-10-10 | ✅ Accepted |
| [006](006-migration-checklist-33-criteres.md) | Migration 31 → 33 critères DINUM officiels | 2025-10-11 | ✅ Accepted |
| [007](007-mkdocs-dsfr-language-divergence.md) | Divergence mkdocs-dsfr locale vs language | 2025-10-14 | ✅ Accepted |

---

## Légende statuts

- ✅ **Accepted**: Décision adoptée et implémentée en production
- ⏳ **Proposed**: En discussion, pas encore implémentée
- ❌ **Deprecated**: Remplacée, ne plus utiliser
- 🔄 **Superseded**: Remplacée par ADR-XXX (voir lien)

---

## Template ADR

Pour créer un nouveau ADR, copier `template.md` et suivre la structure MADR :

```markdown
# ADR-XXX: [Titre court]

**Date**: YYYY-MM-DD
**Statut**: ⏳ Proposed / ✅ Accepted / ❌ Deprecated / 🔄 Superseded
**Décideurs**: [Noms]
**Sponsor**: [Chef projet/Sponsor]

## Contexte

[Problème à résoudre, contraintes, contexte métier]

## Décision

[Solution choisie, justification courte]

## Alternatives considérées

### Option A: [Nom]
- Avantages: ...
- Inconvénients: ...
- **Rejeté**: [Raison]

### Option B: [Nom choisi]
- Avantages: ...
- Inconvénients: ...
- **Choisi**: [Raison]

## Conséquences

**Positives:**
- [Bénéfices]

**Négatives:**
- [Coûts, limitations]

## Validation

- [Critères succès]
- [Tests validation]

## Références

- [Commits, issues, docs]
```

---

## Principes ADR

1. **Immutables**: Un ADR ne se modifie pas après acceptation
2. **Traçables**: Chaque décision technique majeure → ADR
3. **Contextuels**: Expliquer le "pourquoi", pas seulement le "quoi"
4. **Concis**: 1-2 pages maximum
5. **Datés**: Date décision pour historique chronologique

---

## Quand créer un ADR ?

**Créer un ADR pour:**
- ✅ Choix technologiques structurants (frameworks, libs majeures)
- ✅ Changements architecture (formats, workflows, CI/CD)
- ✅ Standards projet (coverage, conventions, process)
- ✅ Décisions impactant > 20% du code

**Ne pas créer pour:**
- ❌ Petits bugfixes
- ❌ Refactoring localisés
- ❌ Ajout features mineures
- ❌ Changements réversibles facilement

---

## Process validation

1. Rédiger ADR avec statut `⏳ Proposed`
2. Discussion équipe (review, alternatives)
3. Décision validée → Statut `✅ Accepted`
4. Implémentation (commits référencent ADR-XXX)
5. Si déprécié plus tard → Créer nouvel ADR + statut `🔄 Superseded by ADR-YYY`

---

## Références

- [MADR Documentation](https://adr.github.io/madr/)
- [ADR GitHub Organization](https://adr.github.io/)
- [Thoughtworks Technology Radar - ADR](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)
