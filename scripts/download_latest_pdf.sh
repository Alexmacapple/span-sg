#!/bin/bash
# Télécharge le PDF depuis la dernière CI draft
set -e

BRANCH="${1:-draft}"
RUN_ID=$(gh run list --branch "$BRANCH" --limit 1 --json databaseId --jq '.[0].databaseId')

echo "📥 Téléchargement PDF depuis run #$RUN_ID (branche $BRANCH)..."
gh run download "$RUN_ID" --name exports --repo Alexmacapple/span-sg

echo "✅ PDF téléchargé : exports/span-sg.pdf"
ls -lh exports/span-sg.pdf
