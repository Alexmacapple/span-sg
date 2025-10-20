#!/bin/bash
# Script de développement SPAN SG
# Lance le serveur MkDocs avec Docker après vérifications

set -e  # Arrêter en cas d'erreur

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🔍 Vérification de l'environnement Docker..."

# Vérifier que Docker est installé
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker n'est pas installé${NC}"
    echo "📖 Installation : https://docs.docker.com/get-docker/"
    exit 1
fi

# Vérifier que Docker Desktop est démarré
if ! docker ps &> /dev/null; then
    echo -e "${RED}❌ Docker Desktop n'est pas démarré${NC}"
    echo "🚀 Lancez Docker Desktop et attendez qu'il soit prêt"
    echo "   Vérifiez que l'icône Docker dans la barre de menu affiche 'Docker Desktop is running'"
    exit 1
fi

echo -e "${GREEN}✅ Docker est opérationnel${NC}"

# Vérifier si le conteneur tourne déjà
if docker compose ps | grep -q "Up"; then
    echo -e "${YELLOW}⚠️  Le serveur MkDocs est déjà en cours d'exécution${NC}"
    echo "📍 URL : http://localhost:8000/span-sg/"
    echo ""
    echo "Commandes disponibles :"
    echo "  - Voir les logs     : docker compose logs -f mkdocs"
    echo "  - Redémarrer        : docker compose restart"
    echo "  - Arrêter           : docker compose down"
    exit 0
fi

# Lancer le serveur
echo "🚀 Démarrage du serveur MkDocs..."
docker compose up -d

# Attendre que le serveur soit prêt (max 10 secondes)
echo "⏳ Attente du démarrage du serveur..."
for i in {1..10}; do
    if docker compose logs mkdocs 2>&1 | grep -q "Serving on"; then
        break
    fi
    sleep 1
done

# Vérifier que le serveur a démarré
if docker compose ps | grep -q "Up"; then
    echo -e "${GREEN}✅ Serveur démarré avec succès !${NC}"
    echo ""
    echo "📍 Accéder au site : ${GREEN}http://localhost:8000/span-sg/${NC}"
    echo ""
    echo "Commandes utiles :"
    echo "  - Voir les logs     : docker compose logs -f mkdocs"
    echo "  - Arrêter           : docker compose down"
    echo "  - Redémarrer        : docker compose restart"
else
    echo -e "${RED}❌ Échec du démarrage du serveur${NC}"
    echo "📋 Logs d'erreur :"
    docker compose logs mkdocs
    exit 1
fi
