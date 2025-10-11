"""
Hook MkDocs pour wrapper automatiquement les <table> avec <div class="fr-table">

Date: 2025-10-08
Contexte: mkdocs-dsfr supprime les divs HTML lors du preprocessing
Solution: post-traiter le HTML pour réinjecter le wrapper DSFR
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

    Wrappe automatiquement tous les <table> avec <div class="fr-table">
    pour assurer la compatibilité avec le Système de Design de l'État (DSFR).

    Contexte:
        Le thème mkdocs-dsfr supprime les divs HTML lors du preprocessing Markdown.
        Ce hook post-traite le HTML pour réinjecter le wrapper DSFR requis
        pour l'accessibilité et le responsive design RGAA.

    Args:
        html: Contenu HTML de la page après conversion Markdown
        page: Instance de page MkDocs (non utilisé)
        config: Configuration MkDocs (non utilisé)
        files: Collection de fichiers MkDocs (non utilisé)

    Returns:
        HTML modifié avec toutes les tables wrappées dans <div class="fr-table">

    Example:
        Input:  '<table><tr><td>Data</td></tr></table>'
        Output: '<div class="fr-table">
                 <table><tr><td>Data</td></tr></table>
                 </div>'

    Note:
        Les tables déjà wrappées ne sont pas re-wrappées (lookahead négatif regex).
    """
    # Pattern pour détecter les tables non wrappées (avec ou sans attributs)
    pattern = r'(?<!<div class="fr-table">)\s*(<table[^>]*>.*?</table>)'

    # Remplacement: wrapper avec div DSFR
    def wrap_table(match) -> str:
        table_html = match.group(1)
        return f'<div class="fr-table">\n{table_html}\n</div>'

    # Appliquer le wrapper (DOTALL pour multiline)
    html = re.sub(pattern, wrap_table, html, flags=re.DOTALL)

    return html
