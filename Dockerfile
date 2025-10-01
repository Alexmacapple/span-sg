# Dockerfile
FROM squidfunk/mkdocs-material:latest
WORKDIR /docs
# Note: mkdocs-pdf-export-plugin non installé (nécessite dépendances système lourdes)
# Pour génération PDF locale, utiliser: pip install mkdocs-pdf-export-plugin
EXPOSE 8000
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
