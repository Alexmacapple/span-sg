# Dockerfile
FROM squidfunk/mkdocs-material:latest
WORKDIR /docs

# Installer dépendances Python depuis requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
