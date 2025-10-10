# Hook MkDocs pour wrapper automatiquement les <table> avec <div class="fr-table">
# Date: 2025-10-08
# Contexte: mkdocs-dsfr supprime les divs HTML lors du preprocessing
# Solution: post-traiter le HTML pour réinjecter le wrapper DSFR

import re


def on_page_content(html, page, config, files):
    """
    Hook appelé après conversion Markdown → HTML.
    Wrappe tous les <table> avec <div class="fr-table">.
    """
    # Pattern pour détecter les tables non wrappées
    pattern = r'(?<!<div class="fr-table">)\s*(<table>.*?</table>)'

    # Remplacement: wrapper avec div DSFR
    def wrap_table(match):
        table_html = match.group(1)
        return f'<div class="fr-table">\n{table_html}\n</div>'

    # Appliquer le wrapper (DOTALL pour multiline)
    html = re.sub(pattern, wrap_table, html, flags=re.DOTALL)

    return html
