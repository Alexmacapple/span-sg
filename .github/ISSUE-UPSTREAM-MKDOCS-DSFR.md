# Issue upstream mkdocs-dsfr

Brouillon d'issue à soumettre sur le GitLab mkdocs-dsfr.

**Plateforme** : https://gitlab-forge.din.developpement-durable.gouv.fr/pub/numeco/mkdocs-dsfr
**Référence** : ADR-007 (docs/adr/007-mkdocs-dsfr-language-divergence.md)

---

## Titre

Documentation recommends `locale: fr` but generates MkDocs warning

---

## Description

The official documentation recommends using `theme.locale: fr` but MkDocs core doesn't recognize this key and emits:

```
WARNING - Config value 'theme.locale': Unrecognised configuration key
```

Using `theme.language: fr` works without warnings and produces identical HTML output (`<html lang="fr">`).

Is `locale` an intentional alias that should be documented differently, or should the docs recommend `language` instead?

---

## Versions

- mkdocs-dsfr: 0.17.0
- mkdocs: 1.6.1
- Python: 3.11+

---

## Configuration actuelle (qui fonctionne)

```yaml
theme:
  name: dsfr
  language: fr  # Pas de warning, HTML correct
```

---

## Configuration documentée (qui génère warning)

```yaml
theme:
  name: dsfr
  locale: fr  # WARNING: Unrecognised configuration key
```

---

## Impact

- Cosmétique (build fonctionne dans les deux cas)
- HTML généré identique (`<html lang="fr">`)
- Recherche française active
- Dates localisées correctement

---

## Demande

Clarifier la documentation officielle pour recommander `language` au lieu de `locale`, ou documenter explicitement que les deux sont supportés avec leurs différences.

---

## Références

- [MkDocs Configuration - theme.language](https://www.mkdocs.org/user-guide/configuration/#language)
- [mkdocs-dsfr Documentation officielle](https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/)
