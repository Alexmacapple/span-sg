"""
Hook MkDocs pour corriger les attributs title des liens de pagination

Date: 2025-10-28
Contexte: Les liens pagination mkdocs-dsfr ont un title qui ne contient pas le nom accessible
Solution: Post-traiter le HTML pour préfixer le title avec le nom accessible
Ticket: RGAA - Attribut title doit commencer par le nom accessible
"""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.config import Config
    from mkdocs.structure.pages import Page


def on_post_page(output: str, page: "Page", config: "Config") -> str:
    """
    Hook MkDocs appelé après génération HTML complète de la page.

    Corrige les attributs title des liens de pagination pour conformité RGAA.

    Contexte:
        Le thème mkdocs-dsfr génère des liens de pagination avec structure:
        <a class="fr-pagination__link fr-pagination__link--next"
           href="..." title="Titre page destination">
            Page suivante
        </a>

        Pour la conformité RGAA, le title doit COMMENCER par le nom accessible
        (le texte visible du lien), puis peut être enrichi avec le contexte.

    Args:
        output: HTML complet de la page après génération
        page: Instance de page MkDocs (non utilisé)
        config: Configuration MkDocs (non utilisé)

    Returns:
        HTML modifié avec title conforme RGAA sur les liens de pagination

    Example:
        Input:  '<a class="fr-pagination__link fr-pagination__link--next"
                    href="..." title="SPAN (SG)">Page suivante</a>'
        Output: '<a class="fr-pagination__link fr-pagination__link--next"
                    href="..." title="Page suivante : SPAN (SG)">Page suivante</a>'

    Note:
        - Gère à la fois les liens "Page suivante" (--next) et "Page précédente" (--prev)
        - Ne modifie que les liens de pagination DSFR
        - Préserve le title original comme information contextuelle
    """
    # Pattern pour détecter les liens pagination avec capture du contenu complet
    # Utilise [^>]* pour permettre n'importe quels attributs et classes supplémentaires
    pattern = r'(<a\s+[^>]*class="[^"]*fr-pagination__link--(next|prev)[^"]*"[^>]*title=")([^"]+)("[^>]*>)\s*([^<]+)\s*(</a>)'

    def fix_pagination_title(match) -> str:
        """Reconstruit le lien avec title RGAA-compliant"""
        opening = match.group(1)  # <a ... title="
        nav_type = match.group(2)  # next ou prev
        title_original = match.group(3)  # Titre page destination
        middle = match.group(4)  # ">
        text_visible = match.group(5).strip()  # "Page suivante" ou "Page précédente"
        closing = match.group(6)  # </a>

        # Construire le nouveau title: "[Nom accessible] : [Contexte]"
        # Format RGAA: commencer par le nom accessible, enrichir avec contexte
        new_title = f"{text_visible} : {title_original}"

        return f"{opening}{new_title}{middle}{text_visible}{closing}"

    # Appliquer la transformation
    output = re.sub(pattern, fix_pagination_title, output)

    return output
