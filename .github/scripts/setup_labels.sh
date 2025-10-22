#!/usr/bin/env bash
# setup_labels.sh - Configuration labels GitHub pour SPAN SG
#
# Usage:
#   ./github/scripts/setup_labels.sh
#
# Prerequis:
#   - gh CLI installe et authentifie
#   - Permissions write:issues sur le repo

set -euo pipefail

REPO="Alexmacapple/span-sg"

echo "Configuration labels GitHub pour $REPO"
echo "========================================"
echo

# Fonction helper pour creer/mettre a jour un label
create_label() {
    local name="$1"
    local color="$2"
    local description="$3"

    if gh label list --repo "$REPO" --limit 1000 | grep -q "^${name}"; then
        echo "  MAJ: $name"
        gh label edit "$name" --repo "$REPO" --color "$color" --description "$description" 2>/dev/null || true
    else
        echo "  NEW: $name"
        gh label create "$name" --repo "$REPO" --color "$color" --description "$description"
    fi
}

# =============================================================================
# LABELS MODULES (6 labels - vert fonce)
# =============================================================================
echo "1. Labels modules (6)"
echo "--------------------"

create_label "module:snum" "0e8a16" "Service SNUM"
create_label "module:sircom" "0e8a16" "Service SIRCOM"
create_label "module:srh" "0e8a16" "Service SRH"
create_label "module:siep" "0e8a16" "Service SIEP"
create_label "module:safi" "0e8a16" "Service SAFI"
create_label "module:bgs" "0e8a16" "Service BGS"

echo

# =============================================================================
# LABELS STATUS (4 labels - jaune/orange)
# =============================================================================
echo "2. Labels status (4)"
echo "-------------------"

create_label "status:triage" "fbca04" "En attente de triage"
create_label "status:in-progress" "d4c5f9" "En cours de traitement"
create_label "status:blocked" "d93f0b" "Bloque par une dependance"
create_label "status:review-needed" "0052cc" "En attente de review"

echo

# =============================================================================
# LABELS PRIORITY (4 labels - rouge degrade)
# =============================================================================
echo "3. Labels priority (4)"
echo "---------------------"

create_label "priority:low" "c2e0c6" "Priorite basse"
create_label "priority:medium" "fbca04" "Priorite moyenne"
create_label "priority:high" "d93f0b" "Priorite haute"
create_label "priority:critical" "b60205" "Priorite critique"

echo

# =============================================================================
# LABELS AREA (5 labels - violet/bleu)
# =============================================================================
echo "4. Labels area (5)"
echo "-----------------"

create_label "area:ci-cd" "5319e7" "CI/CD pipeline et GitHub Actions"
create_label "area:testing" "1d76db" "Tests unitaires, E2E, accessibilite"
create_label "area:accessibility" "0075ca" "Accessibilite RGAA, DSFR"
create_label "area:pdf" "7057ff" "Generation PDF et metadonnees"
create_label "area:scoring" "006b75" "Calcul scores et synthese"

echo

# =============================================================================
# LABELS TYPE (conserver labels par defaut GitHub)
# =============================================================================
echo "5. Labels type (GitHub defaults conserves)"
echo "------------------------------------------"
echo "  Conserver: bug, documentation, enhancement, duplicate, wontfix, etc."

echo
echo "========================================"
echo "Configuration labels terminee"
echo "Total: 19 labels custom + labels GitHub par defaut"
echo
echo "Verification:"
gh label list --repo "$REPO" --limit 100 | grep -E "(module:|status:|priority:|area:)" | wc -l | xargs echo "  Labels custom:"

echo
echo "Documentation: Voir .github/LABELS.md pour guide usage"
