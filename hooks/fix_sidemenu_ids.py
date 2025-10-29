"""
Hook MkDocs pour corriger les IDs dupliqués dans le menu latéral DSFR

Date: 2025-10-28
Contexte: mkdocs-dsfr v0.17.0 génère le même ID "fr-sidemenu-wrapper"
          pour toutes les sections du sidemenu
Solution: Post-traiter le HTML pour rendre les IDs uniques
Ticket: Bug duplicate-id-aria sur pages avec nombreuses sections H2
"""

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.config import Config
    from mkdocs.structure.pages import Page


def on_post_page(output: str, page: "Page", config: "Config") -> str:
    """
    Hook MkDocs appelé après génération HTML complète de la page.

    Corrige les IDs dupliqués dans le menu latéral DSFR en ajoutant
    un suffixe unique basé sur un compteur.

    Contexte:
        Le thème mkdocs-dsfr génère un menu latéral avec structure:
        <div class="fr-sidemenu__inner">
            <button aria-controls="fr-sidemenu-wrapper">Titre</button>
            <div class="fr-collapse" id="fr-sidemenu-wrapper">...</div>
        </div>

        Problème: Toutes les sections ont le MÊME ID "fr-sidemenu-wrapper",
        ce qui casse le JavaScript DSFR et viole les règles RGAA.

    Args:
        output: HTML complet de la page après génération
        page: Instance de page MkDocs (non utilisé)
        config: Configuration MkDocs (non utilisé)

    Returns:
        HTML modifié avec IDs uniques dans le sidemenu

    Example:
        Input:  '<button aria-controls="fr-sidemenu-wrapper">Intro</button>
                 <div id="fr-sidemenu-wrapper">...</div>'
        Output: '<button aria-controls="fr-sidemenu-wrapper-1">Intro</button>
                 <div id="fr-sidemenu-wrapper-1">...</div>'

    Note:
        - Utilise un compteur pour générer des IDs uniques
        - Met à jour à la fois les IDs et les aria-controls
        - S'applique uniquement au sidemenu DSFR
    """
    # Approche simplifiée: remplacer séparément aria-controls et id
    # en maintenant la cohérence avec un compteur partagé

    # D'abord, compter combien de paires aria-controls/id on a
    aria_controls_count = len(re.findall(r'aria-controls="fr-sidemenu-wrapper"', output))
    id_count = len(re.findall(r'id="fr-sidemenu-wrapper"', output))

    # Vérifier que nous avons le même nombre (sinon structure HTML cassée)
    if aria_controls_count != id_count:
        # Log un warning mais continue quand même
        print(f"Warning: Mismatch entre aria-controls ({aria_controls_count}) et id ({id_count}) counts")

    # Remplacer tous les aria-controls
    counter = [0]
    def replace_aria_controls(match):
        counter[0] += 1
        return f'aria-controls="fr-sidemenu-wrapper-{counter[0]}"'

    output = re.sub(
        r'aria-controls="fr-sidemenu-wrapper"',
        replace_aria_controls,
        output
    )

    # Remplacer tous les id avec le même compteur (reset à 0)
    counter = [0]
    def replace_id(match):
        counter[0] += 1
        return f'id="fr-sidemenu-wrapper-{counter[0]}"'

    output = re.sub(
        r'id="fr-sidemenu-wrapper"',
        replace_id,
        output
    )

    return output
