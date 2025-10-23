# ADR-011 : Double approbation et renommage /staging/

**Statut** : Accepté
**Date** : 2025-10-23
**Décideurs** : Alexandra (Owner/Validateur)
**Référence** : [ADR-009](009-migration-github-environments.md)

## Contexte

Après la migration vers GitHub Environments (ADR-009), l'environnement `staging` était configuré en auto-deploy vers `/draft/` sans gate d'approbation. Seul l'environnement `production` nécessitait une validation manuelle.

Cette configuration présentait deux problèmes :
1. **Manque de contrôle** : Impossible de tester staging avant que les modifications soient publiquement accessibles
2. **Incohérence nomenclature** : Environment "staging" → URL "/draft/"

## Décision

### 1. Activation Required Reviewers sur staging

Configurer l'environnement GitHub "staging" avec Required Reviewers (Alexmacapple) pour forcer une approbation manuelle avant tout déploiement.

### 2. Renommage /draft/ → /staging/

Modifier toutes les références pour utiliser `/staging/` afin d'assurer la cohérence entre :
- Nom de l'environnement GitHub : `staging`
- URL publique : `https://alexmacapple.github.io/span-sg/staging/`

### 3. Architecture résultante

```
Workflow : Double approbation (3 niveaux de contrôle)

1. Local (Docker)
   ↓ git push vers main

2. build-and-test (automatique)
   ↓ CI passed

3. deploy-staging PAUSE → ATTENTE APPROVAL
   ↓ Approve staging

4. Déploiement /staging/ (recette)
   ↓ Tests manuels sur staging

5. deploy-production PAUSE → ATTENTE APPROVAL
   ↓ Approve production (Chef SNUM)

6. Déploiement / (production)
```

## Conséquences

### Positives

1. **Contrôle total** : 3 niveaux distincts (local, staging validé, production validée)
2. **Tests isolés** : Possibilité de valider staging sans impacter production
3. **Cohérence** : Nomenclature uniforme environment ↔ URL
4. **Traçabilité** : GitHub conserve l'historique des approbations
5. **Rollback sûr** : Si staging échoue, production reste intacte

### Négatives

1. **Processus plus lent** : 2 approbations manuelles par commit
2. **Charge opérationnelle** : Nécessite vigilance sur notifications GitHub

### Neutres

1. **Migration progressive** : Ancien dossier `/draft/` reste sur gh-pages jusqu'à nettoyage manuel
2. **Bookmarks** : URLs `/draft/` à mettre à jour vers `/staging/` (coexistence temporaire)

## Fichiers modifiés

### Infrastructure
- `.github/workflows/build.yml` :
  - `url: .../staging/` (environment staging)
  - Renommage dossiers `draft` → `staging`
  - Commentaires mis à jour

### Documentation
- `Claude.md` : 6 occurrences draft → staging, dates workflow actualisées
- `GO-CHECKLIST.md` : URL preview staging
- `docs/adr/009-migration-github-environments.md` : Référence à ADR-011
- `docs/guide-chef-snum-approvals.md` : URLs d'exemple

### Nouveau fichier
- `docs/adr/011-double-approval-workflow.md` (ce document)

## URLs finales

| Environnement | URL | Approbation |
|---------------|-----|-------------|
| Local | http://localhost:8000/span-sg/ | Aucune |
| Staging | https://alexmacapple.github.io/span-sg/staging/ | Alexmacapple |
| Production | https://alexmacapple.github.io/span-sg/ | Chef SNUM |

## Test de validation

Le workflow a été testé le 2025-10-23 (commit 6e50c65) :
- Job `build-and-test` : completed
- Job `deploy-staging` : waiting (pause correcte)
- Job `deploy-production` : waiting (pause correcte après approval staging)

Résultat : Configuration fonctionnelle validée

## Notes d'implémentation

### Configuration GitHub Environments

**Staging** :
```json
{
  "name": "staging",
  "protection_rules": [
    {"type": "branch_policy"},
    {"type": "required_reviewers", "reviewers": [{"login": "Alexmacapple"}]}
  ]
}
```

**Production** :
```json
{
  "name": "production",
  "protection_rules": [
    {"type": "branch_policy"},
    {"type": "required_reviewers", "reviewers": [{"login": "Alexmacapple"}]}
  ]
}
```

### Nettoyage futur (optionnel)

Pour supprimer l'ancien dossier `/draft/` de gh-pages :
```bash
git checkout gh-pages
rm -rf draft
git commit -m "cleanup: remove deprecated /draft/ directory"
git push origin gh-pages
```

## Références

- [ADR-009 : Migration GitHub Environments](009-migration-github-environments.md)
- [Guide Chef SNUM Approvals](../guide-chef-snum-approvals.md)
- [Documentation GitHub Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments)
