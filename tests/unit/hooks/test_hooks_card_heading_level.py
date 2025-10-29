"""Tests unitaires pour hooks/card_heading_level.py"""

from hooks.card_heading_level import on_page_content


def test_transform_simple_card():
    """Vérifie la transformation basique h5 → h3 pour une carte DSFR."""
    html = '<h5 class="fr-card__title" id="sircom">SIRCOM</h5>'
    result = on_page_content(html, None, None, None)
    assert '<h3 class="fr-card__title" id="sircom">SIRCOM</h3>' in result
    assert '<h5' not in result


def test_transform_multiple_cards():
    """Vérifie que plusieurs cartes sont transformées."""
    html = """
    <h5 class="fr-card__title" id="card1">Carte 1</h5>
    <p>Contenu</p>
    <h5 class="fr-card__title" id="card2">Carte 2</h5>
    """
    result = on_page_content(html, None, None, None)
    assert result.count('<h3 class="fr-card__title"') == 2
    assert '<h5' not in result


def test_preserve_card_title_attributes():
    """Vérifie que tous les attributs des titres de cartes sont préservés."""
    html = '<h5 class="fr-card__title custom-class" id="test" data-attr="value">Titre</h5>'
    result = on_page_content(html, None, None, None)
    assert '<h3 class="fr-card__title custom-class" id="test" data-attr="value">Titre</h3>' in result


def test_only_transform_card_titles():
    """Vérifie que seuls les h5 avec fr-card__title sont transformés."""
    html = """
    <h5>Titre normal H5</h5>
    <h5 class="other-class">Autre H5</h5>
    <h5 class="fr-card__title">Carte</h5>
    """
    result = on_page_content(html, None, None, None)
    assert '<h3 class="fr-card__title">Carte</h3>' in result


def test_no_card_titles():
    """Vérifie que le HTML sans titres de cartes n'est pas modifié."""
    html = "<p>Pas de cartes</p><div>Contenu</div>"
    result = on_page_content(html, None, None, None)
    assert result == html


def test_card_title_with_rich_content():
    """Vérifie que le contenu riche du titre est préservé."""
    html = '<h5 class="fr-card__title"><strong>SIRCOM</strong> - <em>Service</em></h5>'
    result = on_page_content(html, None, None, None)
    assert '<h3 class="fr-card__title"><strong>SIRCOM</strong> - <em>Service</em></h3>' in result


def test_card_title_multiline():
    """Vérifie le traitement des titres sur plusieurs lignes."""
    html = """
    <h5 class="fr-card__title" id="card">
        Titre multiligne
    </h5>
    """
    result = on_page_content(html, None, None, None)
    assert '<h3 class="fr-card__title" id="card">' in result
    assert '</h3>' in result
    assert '<h5' not in result


def test_card_title_with_various_class_orders():
    """Vérifie que la classe fr-card__title est détectée quelle que soit sa position."""
    html = """
    <h5 class="fr-card__title">Ordre 1</h5>
    <h5 class="custom fr-card__title">Ordre 2</h5>
    <h5 class="fr-card__title custom other">Ordre 3</h5>
    """
    result = on_page_content(html, None, None, None)
    assert result.count('<h3') == 3
    assert '<h5' not in result
