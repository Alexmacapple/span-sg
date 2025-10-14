# ADR-007: Divergence mkdocs-dsfr - locale vs language

**Date**: 2025-10-14
**Statut**: ✅ Accepted
**Décideurs**: Équipe technique SPAN SG
**Sponsor**: Chef SNUM

## Contexte

La documentation officielle du thème mkdocs-dsfr v0.17.0 recommande l'utilisation du paramètre `locale: fr` pour définir la langue du site :

```yaml
theme:
  name: dsfr
  locale: fr
```

Cependant, lors de l'implémentation, l'utilisation de `locale` génère un warning Python :

```
WARNING - Config value 'theme.locale': Unrecognised configuration key
```

Ce warning provient de MkDocs core qui ne reconnaît pas `locale` comme paramètre valide de `theme`.

### Problème

- Documentation officielle : https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/
- Paramètre recommandé : `locale: fr`
- Résultat : warning à chaque build, pollution des logs CI/CD

### Impact

- Builds fonctionnels mais logs "sales" avec warnings
- Confusion pour contributeurs suivant doc officielle
- Risque d'ignorer vrais warnings noyés dans le bruit

## Décision

**Utiliser `language: fr` au lieu de `locale: fr`**

```yaml
theme:
  name: dsfr
  language: fr  # Paramètre MkDocs natif, équivalent fonctionnel
```

Ajouter un commentaire inline explicatif :

```yaml
language: fr  # Note: Doc officielle dit "locale" mais génère warning. "language" fonctionne.
```

## Alternatives considérées

### Option A : Conserver `locale: fr` (doc officielle)

**Avantages :**
- Conforme à la documentation officielle mkdocs-dsfr
- Cohérence avec exemples officiels

**Inconvénients :**
- Warning Python à chaque build
- Logs CI/CD pollués
- Risque de masquer vrais warnings
- Mauvaise expérience contributeur

**Rejeté** : Les warnings génèrent du bruit technique inacceptable en production.

---

### Option B : Utiliser `language: fr` (choisi)

**Avantages :**
- Paramètre natif MkDocs (pas de warning)
- Builds propres et silencieux
- Équivalent fonctionnel exact (attribut `lang="fr"` dans HTML)
- Compatible avec tous plugins MkDocs (search, git-revision-date, etc.)

**Inconvénients :**
- Divergence mineure avec doc officielle (justifiée et documentée)
- Nécessite commentaire inline pour expliciter le choix

**Choisi** : Équilibre optimal entre propreté technique et pragmatisme.

---

### Option C : Soumettre issue au projet mkdocs-dsfr

**Avantages :**
- Correction upstream bénéficierait à tous
- Documentation officielle alignée avec implémentation

**Inconvénients :**
- Délai de réponse/correction incertain
- Bloque le projet en attendant
- Peut-être comportement intentionnel (alias non documenté)

**Rejeté** : Peut être fait en parallèle, mais ne doit pas bloquer le projet.

## Conséquences

### Positives

1. **Builds propres** : Plus de warnings dans logs CI/CD
2. **Maintenabilité** : Logs exploitables, vrais warnings visibles
3. **Standards MkDocs** : Utilisation paramètre documenté officiellement dans MkDocs core
4. **Compatibilité** : Fonctionne avec tous plugins MkDocs sans ajustement
5. **Accessibilité** : Attribut `lang="fr"` correctement injecté dans HTML (RGAA conforme)

### Négatives

1. **Divergence doc** : Commentaire inline requis pour expliquer le choix
2. **Maintenance** : Vérifier à chaque mise à jour mkdocs-dsfr si divergence corrigée
3. **Contributeurs** : Doivent lire commentaire inline pour comprendre

### Mitigations

- Commentaire inline explicite dans `mkdocs-dsfr.yml`
- ADR-007 documente la décision (vous lisez actuellement)
- Mention dans README.md et guide contributeur

## Validation

### Critères de succès

- [x] Builds MkDocs sans warnings `locale` non reconnu
- [x] Attribut HTML `<html lang="fr">` présent
- [x] Plugin search fonctionne avec stemmer français
- [x] Plugin git-revision-date-localized affiche dates en français
- [x] Tests CI/CD passent sans warnings

### Tests de validation

```bash
# Build local sans warnings
mkdocs build --config-file mkdocs-dsfr.yml --strict

# Vérifier attribut lang dans HTML généré
grep '<html lang="fr"' site/index.html

# Vérifier recherche française active
grep 'lang: fr' mkdocs-dsfr.yml
```

### Résultats validation (2025-10-14)

```
✅ Build propre : 0 warnings
✅ HTML conforme : <html lang="fr" data-fr-scheme="light">
✅ Recherche FR : Plugin search lang: fr actif
✅ Dates FR : Plugin git-revision-date-localized affiche "14 octobre 2025"
✅ CI/CD : Workflow #18504738491 succès
```

## Impact sur le projet

### Fichiers concernés

- `mkdocs-dsfr.yml` : Configuration principale (ligne 16)
- `mkdocs-dsfr-pdf.yml` : Configuration PDF (ligne 16)

### Commits de référence

- Initial : `678f3f2` - fix(dsfr): conformité parfaite documentation officielle v0.17.0
- ADR : `[à compléter lors du commit]` - docs(100): documentation complète composants DSFR + ADR-007

### Versions impactées

- mkdocs-dsfr : v0.17.0
- MkDocs : v1.6.1+
- Python : 3.11+

## Action future

**À vérifier lors de la prochaine mise à jour mkdocs-dsfr (v0.18.0+) :**

1. Tester si `locale: fr` ne génère plus de warning
2. Si corrigé upstream → Migrer vers `locale` et marquer ADR-007 comme 🔄 Superseded
3. Si toujours warning → Conserver `language` et mettre à jour ADR-007

**Issue upstream suggérée :**

```markdown
Title: Documentation recommends `locale: fr` but generates MkDocs warning

Description:
The official documentation recommends using `theme.locale: fr` but MkDocs
core doesn't recognize this key and emits:
"WARNING - Config value 'theme.locale': Unrecognised configuration key"

Using `theme.language: fr` works without warnings and produces identical
HTML output (`<html lang="fr">`).

Is `locale` an intentional alias that should be documented differently,
or should the docs recommend `language` instead?

Versions:
- mkdocs-dsfr: 0.17.0
- mkdocs: 1.6.1
```

## Références

- [MkDocs Configuration - theme.language](https://www.mkdocs.org/user-guide/configuration/#language)
- [mkdocs-dsfr Documentation officielle](https://pub.gitlab-pages.din.developpement-durable.gouv.fr/numeco/mkdocs-dsfr-doc/)
- [ADR-001: Adoption thème DSFR](001-choix-theme-dsfr.md) - Contexte choix DSFR
- Instructions projet : Voir fichier CLAUDE.md à la racine (lignes 15-17 : configuration language vs locale)

---

**Note finale** : Cette divergence est **cosmétique** (paramètre équivalent) et ne compromet en rien la conformité DSFR ou RGAA du site. Le choix de `language` est une **best practice MkDocs** standard.
