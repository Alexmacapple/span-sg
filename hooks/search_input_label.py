"""
Hook MkDocs pour ajouter title au champ de recherche

Date: 2025-10-28
Contexte: Le champ de recherche mkdocs-dsfr n'a pas d'attribut title
Solution: Post-traiter le HTML complet pour ajouter title au champ input#mkdocs-search-query
Ticket: RGAA - Attribut title manquant sur champ de formulaire
"""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.config import Config
    from mkdocs.structure.pages import Page


def on_post_page(output: str, page: "Page", config: "Config") -> str:
    """
    Hook MkDocs appelé après génération HTML complète de la page.

    Ajoute l'attribut title au champ de recherche pour conformité RGAA.

    Contexte:
        Le thème mkdocs-dsfr génère un champ de recherche dans le header
        sans attribut title visible:
        <input id="mkdocs-search-query" placeholder="Rechercher" ...>

        L'attribut title est requis pour la conformité RGAA quand le label
        est caché visuellement.

    Args:
        output: HTML complet de la page après assemblage avec templates
        page: Instance de page MkDocs (non utilisé)
        config: Configuration MkDocs (non utilisé)

    Returns:
        HTML modifié avec title sur le champ de recherche

    Example:
        Input:  '<input id="mkdocs-search-query" placeholder="Rechercher" type="text">'
        Output: '<input id="mkdocs-search-query" title="Rechercher" placeholder="Rechercher" type="text">'

    Note:
        - Évite la duplication si title est déjà présent
        - Ne modifie que le champ avec id="mkdocs-search-query"
        - Utilise on_post_page() car le champ est dans le template header.html
    """
    # Pattern pour détecter le champ de recherche sans title
    # Capture l'input jusqu'au > final (avec ou sans / pour auto-fermeture)
    pattern = r'(<input[^>]*id="mkdocs-search-query"[^>]*)(\s*/?\s*>)'

    def add_title(match) -> str:
        """Ajoute title si pas déjà présent"""
        input_tag = match.group(1)
        closing = match.group(2)

        # Vérifier si title déjà présent
        if 'title=' in input_tag:
            return match.group(0)

        # Ajouter title avant le / ou le >
        # Nettoyer le closing pour avoir soit " />" soit ">"
        clean_closing = ' />' if '/' in closing else '>'
        return f'{input_tag} title="Rechercher"{clean_closing}'

    # Appliquer la transformation
    output = re.sub(pattern, add_title, output)

    return output
