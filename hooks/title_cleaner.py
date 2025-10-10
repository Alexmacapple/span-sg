"""Hook MkDocs pour nettoyer les titres HTML redondants."""

import re


def on_post_page(output, page, config):
    """
    Nettoie le titre HTML en supprimant les tirets et espaces superflus
    quand site_name est vide.

    Transforme <title>\n        SPAN (SG)\n        -\n        \n    </title>
    En <title>SPAN (SG)</title>
    """
    # Pattern pour matcher les titres avec tirets et espaces superflus
    pattern = r"<title>\s*(.*?)\s*-\s*\s*</title>"
    replacement = r"<title>\1</title>"

    output = re.sub(pattern, replacement, output, flags=re.DOTALL)

    return output
