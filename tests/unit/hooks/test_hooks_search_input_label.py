"""Tests unitaires pour hooks/search_input_label.py"""

from hooks.search_input_label import on_post_page


def test_add_title_to_search_input_without_title():
    """Vérifie l'ajout de title au champ de recherche sans title."""
    html = '<input id="mkdocs-search-query" placeholder="Rechercher" type="text">'
    result = on_post_page(html, None, None)
    assert 'title="Rechercher"' in result
    assert '<input id="mkdocs-search-query" placeholder="Rechercher" type="text" title="Rechercher">' in result


def test_preserve_existing_title():
    """Vérifie que title existant n'est pas modifié."""
    html = '<input id="mkdocs-search-query" title="Champ de recherche" placeholder="Rechercher" type="text">'
    result = on_post_page(html, None, None)
    assert result == html
    assert result.count('title=') == 1


def test_self_closing_input_tag():
    """Vérifie le traitement des balises auto-fermantes."""
    html = '<input id="mkdocs-search-query" placeholder="Rechercher" type="text" />'
    result = on_post_page(html, None, None)
    assert 'title="Rechercher"' in result
    # Note: Le pattern regex capture le / dans le groupe 1, donc title vient après
    assert 'title="Rechercher">' in result


def test_regular_closing_input_tag():
    """Vérifie le traitement des balises avec fermeture classique."""
    html = '<input id="mkdocs-search-query" placeholder="Rechercher" type="text">'
    result = on_post_page(html, None, None)
    assert 'title="Rechercher"' in result
    assert result.endswith('>')
    assert ' />' not in result


def test_preserve_all_attributes():
    """Vérifie que tous les attributs du champ sont préservés."""
    html = '<input id="mkdocs-search-query" class="search-field" placeholder="Rechercher" type="text" autocomplete="off" aria-label="Recherche">'
    result = on_post_page(html, None, None)
    assert 'class="search-field"' in result
    assert 'placeholder="Rechercher"' in result
    assert 'type="text"' in result
    assert 'autocomplete="off"' in result
    assert 'aria-label="Recherche"' in result
    assert 'title="Rechercher"' in result


def test_no_search_input():
    """Vérifie que le HTML sans champ de recherche n'est pas modifié."""
    html = "<p>Pas de recherche</p><input id='autre-input' type='text'>"
    result = on_post_page(html, None, None)
    assert result == html


def test_multiple_search_inputs():
    """Vérifie le traitement de plusieurs champs de recherche (edge case)."""
    html = """
    <input id="mkdocs-search-query" placeholder="Rechercher">
    <p>Contenu</p>
    <input id="mkdocs-search-query" placeholder="Rechercher">
    """
    result = on_post_page(html, None, None)
    assert result.count('title="Rechercher"') == 2


def test_various_attribute_orders():
    """Vérifie que l'ID peut être à différentes positions dans la balise."""
    html1 = '<input id="mkdocs-search-query" type="text">'
    html2 = '<input type="text" id="mkdocs-search-query">'
    html3 = '<input placeholder="Rechercher" id="mkdocs-search-query" type="text">'

    result1 = on_post_page(html1, None, None)
    result2 = on_post_page(html2, None, None)
    result3 = on_post_page(html3, None, None)

    assert 'title="Rechercher"' in result1
    assert 'title="Rechercher"' in result2
    assert 'title="Rechercher"' in result3


def test_search_input_multiline():
    """Vérifie le traitement des champs sur plusieurs lignes."""
    html = """
    <input
        id="mkdocs-search-query"
        placeholder="Rechercher"
        type="text"
    >
    """
    result = on_post_page(html, None, None)
    assert 'title="Rechercher"' in result
    assert 'id="mkdocs-search-query"' in result
