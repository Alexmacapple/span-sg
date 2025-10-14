# Issue upstream mkdocs-dsfr

Brouillon d'issue à soumettre sur le GitLab mkdocs-dsfr.

**Plateforme** : https://gitlab-forge.din.developpement-durable.gouv.fr/pub/numeco/mkdocs-dsfr/-/issues
**Référence** : ADR-008 (docs/adr/008-exclusion-search-label-tests-wcag.md)

---

## Titre

Search input label hidden causes WCAG axe-core violation (label rule)

---

## Description

### Problème

Le label du champ de recherche du header DSFR est caché visuellement (probablement via CSS sr-only ou clip), ce qui génère une violation WCAG 2.1 AA critique détectée par axe-core lors des tests d'accessibilité automatisés.

### Violation détectée

```
AssertionError: Homepage a 1 violation(s) WCAG critique(s) : label
Form element has explicit <label> that is hidden
Target: #mkdocs-search-query
```

**Détails axe-core** :
- Règle : `label`
- Impact : critical
- Standards violés :
  - WCAG 2.1 AA - 1.3.1 (Info and Relationships)
  - WCAG 2.1 AA - 3.3.2 (Labels or Instructions)
  - Section 508.22.n (Form controls)

### HTML généré (mkdocs-dsfr v0.17.0)

Template source : `.../site-packages/dsfr/header.html:81-86`

```html
<label class="fr-label" for="mkdocs-search-query">
    Rechercher
</label>
<input class="fr-input search_input search-query"
       id="mkdocs-search-query"
       placeholder="Rechercher"
       type="text">
```

**Cause probable** : Le CSS DSFR (`.fr-label` ou modal search) applique probablement une technique de masquage visuel comme :
- `clip: rect(0, 0, 0, 0)` + `position: absolute`
- `position: absolute; left: -9999px`
- Classe `.sr-only` avec overflow hidden

Bien que cette technique soit courante pour rendre le label accessible aux lecteurs d'écran, axe-core la considère comme une violation si le label est "hidden" au sens du DOM.

---

## Impact

### Sur les projets utilisant mkdocs-dsfr

- Tests RGAA automatisés (axe-core, Pa11y, Lighthouse) échouent systématiquement
- Impossible d'enforcer les tests d'accessibilité en CI sans workaround
- Score accessibilité réduit (-1 point sur tests automatisés)

### Sur l'accessibilité réelle

**Note importante** : Le label caché fonctionne correctement pour les lecteurs d'écran (NVDA, JAWS, VoiceOver testés). La violation axe-core est une fausse alerte sur une technique d'accessibilité standard, mais elle bloque néanmoins la validation automatisée.

---

## Environnement

- **mkdocs-dsfr** : 0.17.0
- **mkdocs** : 1.6.1
- **Python** : 3.11+
- **axe-core** : 3.1+ (via axe-selenium-python 2.1.6)
- **Chrome** : 140.0.7339.207
- **OS** : Ubuntu 22.04 (GitHub Actions CI)

---

## Workaround actuel

En attendant un fix upstream, nous avons implémenté un filtre POST-RUN dans nos tests pour exclure spécifiquement cette violation :

```python
# WORKAROUND: Exclure search input label (bug upstream mkdocs-dsfr v0.17.0)
# Le label est caché visuellement (CSS sr-only) mais axe-core le détecte comme violation.
critical_violations = [
    v
    for v in critical_violations
    if not (
        v.get("id") == "label"
        and any(
            "#mkdocs-search-query" in str(node.get("target", []))
            for node in v.get("nodes", [])
        )
    )
]
```

**Rationale du POST-RUN** : axe-core ne supporte pas l'exclusion par sélecteur au niveau d'une règle spécifique via `options.rules`. La syntaxe suivante ne fonctionne PAS :

```python
# Ne fonctionne PAS
results = axe.run(options={
    "runOnly": ["wcag2a", "wcag2aa", "wcag21aa"],
    "rules": {
        "label": {
            "selector": ":not(#mkdocs-search-query)"  # Non supporté
        }
    }
})
```

---

## Propositions de fix

### Option 1 : Rendre le label visible (recommandé)

Afficher visuellement le label au-dessus du champ de recherche. Avantages :
- Conforme WCAG sans ambiguïté
- Améliore l'UX pour tous les utilisateurs
- Passe axe-core sans workaround

Structure proposée :
```html
<div class="fr-search-bar">
    <label class="fr-label" for="mkdocs-search-query">
        Rechercher
    </label>
    <input class="fr-input" id="mkdocs-search-query" type="text">
</div>
```

### Option 2 : Utiliser aria-label au lieu de label caché

Remplacer le `<label>` caché par un `aria-label` sur l'input :

```html
<input class="fr-input search_input search-query"
       id="mkdocs-search-query"
       aria-label="Rechercher dans la documentation"
       placeholder="Rechercher"
       type="text">
```

Avantages :
- Passe axe-core (pas de label caché)
- Maintient l'accessibilité lecteurs d'écran
- Pas de changement visuel

Inconvénient :
- `aria-label` moins robuste que `<label>` explicite

### Option 3 : Utiliser aria-labelledby

Créer un label invisible avec technique approuvée par axe-core :

```html
<span id="search-label" class="fr-sr-only">Rechercher</span>
<input class="fr-input"
       id="mkdocs-search-query"
       aria-labelledby="search-label"
       placeholder="Rechercher"
       type="text">
```

---

## Tests pour valider le fix

### Test automatisé (axe-core)

```python
from axe_selenium_python import Axe
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

axe = Axe(driver)
axe.inject()
results = axe.run(options={"runOnly": ["wcag2a", "wcag2aa", "wcag21aa"]})

violations = [v for v in results["violations"] if v["id"] == "label"]
assert len(violations) == 0, f"Label violations détectées : {violations}"
```

### Test screen-reader

Vérifier avec NVDA/JAWS/VoiceOver que le champ de recherche est correctement annoncé avec son label.

---

## Références

### Standards WCAG

- [WCAG 2.1 - 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html)
- [WCAG 2.1 - 3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions.html)

### Axe-core documentation

- [axe-core rule: label](https://dequeuniversity.com/rules/axe/3.1/label?application=axeAPI)
- [Form labels best practices](https://www.w3.org/WAI/tutorials/forms/labels/)

### Notre documentation

- ADR-008 : docs/adr/008-exclusion-search-label-tests-wcag.md (documentation complète du workaround)
- Tests accessibilité : tests/test_accessibility.py:78-94

---

## Priorité

**Moyenne** : Le workaround permet de débloquer les tests RGAA en production, mais un fix upstream améliorerait la conformité de tous les projets mkdocs-dsfr et simplifierait les pipelines CI.

---

## Contact

Si besoin de logs complets, captures d'écran, ou tests sur environnements spécifiques, n'hésitez pas à demander.
