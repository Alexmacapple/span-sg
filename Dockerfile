# Dockerfile
FROM squidfunk/mkdocs-material:latest
WORKDIR /docs

# Installer les outils de compilation nécessaires pour libsass
RUN apk add --no-cache gcc musl-dev g++ libffi-dev

# Installer dépendances Python depuis requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
