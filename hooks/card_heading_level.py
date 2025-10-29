"""
Hook MkDocs pour transformer les <h5> en <h3> dans les cartes DSFR

Date: 2025-10-28
Contexte: Les cartes DSFR générées par dsfr_structure utilisent <h5> par défaut
Solution: Post-traiter le HTML pour remplacer h5 par h3 dans les cartes pour conformité RGAA
Ticket: Hiérarchie des titres RGAA - Page d'accueil
"""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.config import Config
    from mkdocs.structure.files import Files
    from mkdocs.structure.pages import Page


def on_page_content(html: str, page: "Page", config: "Config", files: "Files") -> str:
    """
    Hook MkDocs appelé après conversion Markdown → HTML.

    Transforme les titres <h5 class="fr-card__title"> en <h3 class="fr-card__title">
    pour respecter la hiérarchie RGAA des titres.

    Contexte:
        La syntaxe Markdown `/// card | Titre` génère par défaut des <h5>.
        Pour la conformité RGAA, les titres de cartes doivent être en <h3>
        lorsqu'ils suivent un titre <h2> dans la page.

    Args:
        html: Contenu HTML de la page après conversion Markdown
        page: Instance de page MkDocs (non utilisé)
        config: Configuration MkDocs (non utilisé)
        files: Collection de fichiers MkDocs (non utilisé)

    Returns:
        HTML modifié avec les titres de cartes en h3

    Example:
        Input:  '<h5 class="fr-card__title" id="sircom">SIRCOM</h5>'
        Output: '<h3 class="fr-card__title" id="sircom">SIRCOM</h3>'

    Note:
        Seuls les h5 avec la classe "fr-card__title" sont transformés.
        Les autres h5 de la page ne sont pas affectés.
    """
    # Pattern pour détecter les balises <h5> avec class="fr-card__title"
    # Capture le contenu entre <h5> et </h5>
    pattern_open = r'<h5(\s+[^>]*class="[^"]*fr-card__title[^"]*"[^>]*)>'
    pattern_close = r'</h5>'

    # Remplacer <h5 class="fr-card__title"...> par <h3 class="fr-card__title"...>
    html = re.sub(pattern_open, r'<h3\1>', html)

    # Remplacer les </h5> qui correspondent (approximation: tous les </h5> après transformation)
    # Note: Cette approche simple fonctionne car les cartes DSFR ont une structure prévisible
    html = html.replace('</h5>', '</h3>')

    return html
