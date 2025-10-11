"""Tests unitaires pour hooks/title_cleaner.py"""

from hooks.title_cleaner import on_post_page


def test_clean_title_with_dash_and_spaces():
    """Vérifie le nettoyage de tiret et espaces superflus."""
    output = "<title>\n        SPAN (SG)\n        -\n        \n    </title>"
    result = on_post_page(output, None, None)
    assert result == "<title>SPAN (SG)</title>"


def test_clean_title_simple_dash():
    """Vérifie le nettoyage d'un tiret simple."""
    output = "<title>Mon Titre -  </title>"
    result = on_post_page(output, None, None)
    assert result == "<title>Mon Titre</title>"


def test_clean_title_without_dash():
    """Vérifie qu'un titre sans tiret n'est pas modifié."""
    output = "<title>SPAN (SG) Module SNUM</title>"
    result = on_post_page(output, None, None)
    assert result == output


def test_no_title_tag():
    """Vérifie que le HTML sans balise title n'est pas modifié."""
    output = "<html><body>Pas de title</body></html>"
    result = on_post_page(output, None, None)
    assert result == output


def test_title_with_rich_content():
    """Vérifie que le contenu du titre est préservé."""
    output = "<title>SPAN (SG) - Module SNUM - Accueil - </title>"
    result = on_post_page(output, None, None)
    # Le regex doit supprimer le dernier " - " seulement
    assert "SPAN (SG) - Module SNUM - Accueil" in result
    assert not result.endswith(" - </title>")


def test_multiple_titles():
    """Vérifie le nettoyage de plusieurs balises title (cas limite)."""
    output = "<title>Titre 1 - </title><title>Titre 2 - </title>"
    result = on_post_page(output, None, None)
    assert "<title>Titre 1</title>" in result
    assert "<title>Titre 2</title>" in result
    # Vérifier qu'aucun " - " ne subsiste avant </title>
    assert " - </title>" not in result
