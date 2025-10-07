# Développement local

## Démarrer le serveur MkDocs

### Avec Docker (recommandé)

```bash
# Démarrer le serveur
docker compose up

# Ou en arrière-plan
docker compose up -d
```

Accès : http://localhost:8000/span-sg-repo/

### Sans Docker

```bash
# Installer les dépendances
pip install -r requirements.txt

# Démarrer le serveur
mkdocs serve
```

Accès : http://127.0.0.1:8000/

## Commandes utiles

```bash
# Arrêter le serveur
docker compose down

# Voir les logs
docker compose logs -f

# Redémarrer
docker compose restart

# Vérifier l'état
docker compose ps
```

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
| **Draft (preview)** | https://alexmacapple.github.io/span-sg-repo/draft/ |
| **Production** | https://alexmacapple.github.io/span-sg-repo/ |
