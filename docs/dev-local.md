# Développement local

## Démarrer le serveur MkDocs

### Avec Docker (recommandé)

```bash
# Démarrer le serveur (thème DSFR)
docker compose -f docker-compose-dsfr.yml up

# Ou en arrière-plan
docker compose -f docker-compose-dsfr.yml up -d
```

Accès : <http://localhost:8000/span-sg-repo/>

### Sans Docker

```bash
# Installer les dépendances
pip install -r requirements.txt

# Démarrer le serveur
mkdocs serve
```

Accès : <http://127.0.0.1:8000/>

## Commandes utiles

```bash
# Arrêter le serveur
docker compose -f docker-compose-dsfr.yml down

# Voir les logs
docker compose -f docker-compose-dsfr.yml logs -f

# Redémarrer
docker compose -f docker-compose-dsfr.yml restart

# Vérifier l'état
docker compose -f docker-compose-dsfr.yml ps
```

## Hooks DSFR

Le projet utilise des hooks Python MkDocs pour améliorer l'accessibilité DSFR :

- **`hooks/dsfr_table_wrapper.py`** : Encapsule automatiquement les tableaux Markdown dans `<div class="fr-table">` pour le responsive DSFR
- **`hooks/title_cleaner.py`** : Nettoie les titres HTML redondants (supprime `site_name` quand vide)

## Recalculer les scores

```bash
python scripts/calculate_scores.py
```

Génère automatiquement `docs/synthese.md` avec les scores agrégés.

## Build et validation

```bash
# Build site HTML
mkdocs build

# Mode strict (erreurs bloquantes)
mkdocs build --strict

# Générer PDF
mkdocs build --config-file mkdocs-pdf.yml
```

## URLs par environnement

| Environnement | URL |
|---|---|
| **Local** | http://localhost:8000/span-sg-repo/ |
| **Draft (preview)** | Désactivé — revue locale/PDF (voir `.github/PAGES-ACCESS-CHECKLIST.md`) |
| **Production** | https://alexmacapple.github.io/span-sg-repo/ |

## Revue locale et PDF (sans Pages)

Objectif: éviter toute exposition publique avant validation.

- Prévisualisation locale: `mkdocs serve -f mkdocs.yml -a 0.0.0.0:8000`
- Build strict local: `mkdocs build -f mkdocs.yml`
- PDF pour revue: `mkdocs build -f mkdocs-pdf.yml` ou récupérer l’artefact CI (`scripts/download_latest_pdf.sh`)
- Ne pas activer GitHub Pages tant que le contenu n’est pas validé. Consulter `.github/PAGES-ACCESS-CHECKLIST.md` (scénario B).
