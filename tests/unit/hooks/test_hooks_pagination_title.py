"""Tests unitaires pour hooks/pagination_title.py"""

from hooks.pagination_title import on_post_page


def test_fix_next_pagination_title():
    """Vérifie la correction du title pour lien 'Page suivante'."""
    html = '<a class="fr-pagination__link fr-pagination__link--next" href="/page2/" title="SPAN (SG)">Page suivante</a>'
    result = on_post_page(html, None, None)
    assert 'title="Page suivante : SPAN (SG)"' in result


def test_fix_prev_pagination_title():
    """Vérifie la correction du title pour lien 'Page précédente'."""
    html = '<a class="fr-pagination__link fr-pagination__link--prev" href="/page1/" title="Accueil">Page précédente</a>'
    result = on_post_page(html, None, None)
    assert 'title="Page précédente : Accueil"' in result


def test_preserve_next_and_prev_both():
    """Vérifie que les deux liens de pagination sont corrigés."""
    html = """
    <a class="fr-pagination__link fr-pagination__link--prev" href="/page1/" title="Intro">Page précédente</a>
    <a class="fr-pagination__link fr-pagination__link--next" href="/page3/" title="Conclusion">Page suivante</a>
    """
    result = on_post_page(html, None, None)
    assert 'title="Page précédente : Intro"' in result
    assert 'title="Page suivante : Conclusion"' in result


def test_preserve_other_attributes():
    """Vérifie que tous les attributs du lien sont préservés."""
    html = '<a class="fr-pagination__link fr-pagination__link--next custom-class" href="/page2/" title="SPAN" id="next-link" data-page="2">Page suivante</a>'
    result = on_post_page(html, None, None)
    assert 'href="/page2/"' in result
    assert 'id="next-link"' in result
    assert 'data-page="2"' in result
    assert 'custom-class' in result
    assert 'title="Page suivante : SPAN"' in result


def test_no_pagination_links():
    """Vérifie que le HTML sans pagination n'est pas modifié."""
    html = "<p>Pas de pagination</p><a href='/autre'>Lien normal</a>"
    result = on_post_page(html, None, None)
    assert result == html


def test_pagination_title_already_compliant():
    """Vérifie le traitement d'un title déjà conforme RGAA."""
    html = '<a class="fr-pagination__link fr-pagination__link--next" href="/page2/" title="Titre original">Page suivante</a>'
    result = on_post_page(html, None, None)
    # Le hook ajoute toujours le préfixe, même si déjà présent
    assert 'title="Page suivante : Titre original"' in result


def test_pagination_with_additional_classes():
    """Vérifie le traitement avec classes CSS supplémentaires."""
    html1 = '<a class="fr-pagination__link--next other-class" href="/p2/" title="Page 2">Page suivante</a>'
    html2 = '<a class="other-class fr-pagination__link--prev" href="/p1/" title="Page 1">Page précédente</a>'

    result1 = on_post_page(html1, None, None)
    result2 = on_post_page(html2, None, None)

    assert 'title="Page suivante : Page 2"' in result1
    assert 'title="Page précédente : Page 1"' in result2


def test_pagination_multiline():
    """Vérifie le traitement des liens sur plusieurs lignes."""
    html = """
    <a class="fr-pagination__link fr-pagination__link--next"
       href="/page2/"
       title="SPAN (SG)">
        Page suivante
    </a>
    """
    result = on_post_page(html, None, None)
    assert 'title="Page suivante : SPAN (SG)"' in result


def test_various_attribute_orders():
    """Vérifie que la classe fr-pagination__link peut être à différentes positions."""
    # Note: Le pattern regex nécessite class="..." avant title="..." pour matcher
    html1 = '<a class="fr-pagination__link--next" title="Page 2" href="/p2/">Page suivante</a>'
    html2 = '<a class="fr-pagination__link--next" href="/p2/" title="Page 2">Page suivante</a>'
    html3 = '<a href="/p2/" class="fr-pagination__link--next" title="Page 2">Page suivante</a>'

    result1 = on_post_page(html1, None, None)
    result2 = on_post_page(html2, None, None)
    result3 = on_post_page(html3, None, None)

    assert 'title="Page suivante : Page 2"' in result1
    assert 'title="Page suivante : Page 2"' in result2
    assert 'title="Page suivante : Page 2"' in result3


def test_pagination_with_special_chars_in_title():
    """Vérifie le traitement des caractères spéciaux dans les titres."""
    html1 = '<a class="fr-pagination__link--next" href="/p2/" title="L\'accessibilité">Page suivante</a>'
    html2 = '<a class="fr-pagination__link--next" href="/p2/" title="État & Services">Page suivante</a>'
    html3 = '<a class="fr-pagination__link--next" href="/p2/" title="Données (2025)">Page suivante</a>'

    result1 = on_post_page(html1, None, None)
    result2 = on_post_page(html2, None, None)
    result3 = on_post_page(html3, None, None)

    assert "title=\"Page suivante : L'accessibilité\"" in result1
    assert 'title="Page suivante : État & Services"' in result2
    assert 'title="Page suivante : Données (2025)"' in result3


def test_pagination_with_different_page_titles():
    """Vérifie le traitement de divers titres de pages."""
    html = """
    <a class="fr-pagination__link--prev" href="/intro/" title="Introduction générale">Page précédente</a>
    <a class="fr-pagination__link--next" href="/module-sircom/" title="SIRCOM - Services d'information">Page suivante</a>
    """
    result = on_post_page(html, None, None)
    assert 'title="Page précédente : Introduction générale"' in result
    assert 'title="Page suivante : SIRCOM - Services d\'information"' in result
