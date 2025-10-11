"""Hook MkDocs pour nettoyer les titres HTML redondants."""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.config import Config
    from mkdocs.structure.pages import Page


def on_post_page(output: str, page: "Page", config: "Config") -> str:
    """
    Hook MkDocs appelé après génération HTML complète de la page.

    Nettoie le titre HTML en supprimant les tirets et espaces superflus
    quand site_name est vide (cas du thème DSFR).

    Contexte:
        Lorsque site_name est vide dans mkdocs.yml, MkDocs génère des titres
        avec des tirets orphelins et espaces superflus : "<title>Page - </title>".
        Ce hook nettoie ces artefacts pour améliorer le SEO et l'accessibilité.

    Args:
        output: HTML complet de la page après génération
        page: Instance de page MkDocs (non utilisé)
        config: Configuration MkDocs (non utilisé)

    Returns:
        HTML modifié avec titre nettoyé

    Example:
        Input:  '<title>\n        SPAN (SG)\n        -\n        \n    </title>'
        Output: '<title>SPAN (SG)</title>'

    Note:
        Utilise un regex avec DOTALL pour gérer les titres multilignes.
    """
    # Pattern pour matcher les titres avec tirets et espaces superflus
    pattern = r"<title>\s*(.*?)\s*-\s*\s*</title>"
    replacement = r"<title>\1</title>"

    output = re.sub(pattern, replacement, output, flags=re.DOTALL)

    return output
