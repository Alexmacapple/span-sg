# ADR-011 : Double approbation et renommage /staging/

**Statut** : Accepté
**Date** : 2025-10-23
**Décideurs** : Alexandra (Owner/Validateur)
**Référence** : [ADR-009](009-migration-github-environments.md)

## Contexte

Après la migration vers GitHub Environments (ADR-009), l'environnement `staging` était configuré en auto-deploy vers `/staging/` sans gate d'approbation. Seul l'environnement `production` nécessitait une validation manuelle.

Cette configuration présentait deux problèmes :
1. **Manque de contrôle** : Impossible de tester staging avant que les modifications soient publiquement accessibles
2. **Incohérence nomenclature** : Environment "staging" → URL "/staging/"

## Décision

### 1. Renommage /draft/ → /staging/

Modifier toutes les références pour utiliser `/staging/` afin d'assurer la cohérence entre :
- Nom de l'environnement GitHub : `staging`
- URL publique : `https://alexmacapple.github.io/span-sg/staging/`

### 2. Configuration hybride des approbations (Option C)

**Environnement staging** :
- Required Reviewers : Alexmacapple
- **Prevent self-review : NON** (auto-deploy pour tests rapides)
- Résultat : Push → Auto-approve → Deploy `/staging/` immédiat

**Environnement production** :
- Required Reviewers : Alexmacapple + Chef SNUM
- **Prevent self-review : OUI** (protection finale)
- Résultat : Push → Attente approbation Chef SNUM → Deploy `/` après validation

**Justification Option C** :
- Staging auto-deploy : Vélocité maximale pour tests et itérations
- Production gate manuel : Sécurité et gouvernance conformes au cahier des charges
- Équilibre optimal entre rapidité développement et contrôle qualité

### 3. Architecture résultante

```
Workflow : Approbation hybride (2 niveaux de contrôle)

1. Local (Docker)
   ↓ git push vers main

2. build-and-test (automatique)
   ↓ CI passed

3. deploy-staging (auto-approve Alexmacapple)
   ↓ Deploy immédiat

4. Déploiement /staging/ (recette)
   ↓ Tests manuels sur staging

5. deploy-production PAUSE → ATTENTE APPROVAL Chef SNUM
   ↓ Approve production (Chef SNUM uniquement)

6. Déploiement / (production)
```

## Conséquences

### Positives

1. **Vélocité développement** : Staging auto-deploy permet tests rapides sans friction
2. **Contrôle production** : Gate manuel Chef SNUM garantit validation finale
3. **Tests isolés** : Possibilité de valider staging sans impacter production
4. **Cohérence** : Nomenclature uniforme environment ↔ URL
5. **Traçabilité** : GitHub conserve l'historique des approbations production
6. **Équilibre optimal** : Rapidité en dev, sécurité en prod

### Négatives

1. **Staging public** : Auto-deploy expose `/staging/` sans validation (acceptable car org-only)
2. **Dépendance Chef SNUM** : Workflow production bloqué si Chef SNUM indisponible

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

**Staging** (auto-deploy) :
```json
{
  "name": "staging",
  "protection_rules": [
    {"type": "branch_policy"},
    {
      "type": "required_reviewers",
      "reviewers": [{"login": "Alexmacapple"}],
      "prevent_self_review": false
    }
  ]
}
```

Configuration manuelle requise :
1. Aller sur https://github.com/Alexmacapple/span-sg/settings/environments/staging
2. Vérifier que "Prevent self-review" est **décoché** (auto-approve Alexmacapple)

**Production** (gate manuel) :
```json
{
  "name": "production",
  "protection_rules": [
    {"type": "branch_policy"},
    {
      "type": "required_reviewers",
      "reviewers": [
        {"login": "Alexmacapple"},
        {"login": "Chef-SNUM"}
      ],
      "prevent_self_review": true
    }
  ]
}
```

Configuration manuelle requise :
1. Aller sur https://github.com/Alexmacapple/span-sg/settings/environments/production
2. Ajouter **Chef SNUM** comme Required Reviewer
3. **Cocher "Prevent self-review"** (Alexmacapple ne peut plus auto-approuver)
4. Résultat : Seul Chef SNUM peut approuver les déploiements production

### Nettoyage futur (optionnel)

Pour supprimer l'ancien dossier `/staging/` de gh-pages :
```bash
git checkout gh-pages
rm -rf draft
git commit -m "cleanup: remove deprecated /staging/ directory"
git push origin gh-pages
```

## Références

- [ADR-009 : Migration GitHub Environments](009-migration-github-environments.md)
- [Guide Chef SNUM Approvals](../guide-chef-snum-approvals.md)
- [Documentation GitHub Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments)
