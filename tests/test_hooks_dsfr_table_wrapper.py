"""Tests unitaires pour hooks/dsfr_table_wrapper.py"""

from hooks.dsfr_table_wrapper import on_page_content


def test_wrap_simple_table():
    """Vérifie qu'une table simple est wrappée avec div DSFR."""
    html = "<table><tr><td>Test</td></tr></table>"
    result = on_page_content(html, None, None, None)
    assert '<div class="fr-table">' in result
    assert "<table>" in result
    assert "</div>" in result


def test_wrap_multiple_tables():
    """Vérifie que plusieurs tables sont wrappées individuellement."""
    html = "<table>A</table><p>texte</p><table>B</table>"
    result = on_page_content(html, None, None, None)
    assert result.count('<div class="fr-table">') == 2


def test_already_wrapped_table():
    """Vérifie qu'une table déjà wrappée n'est pas re-wrappée."""
    html = '<div class="fr-table"><table>Test</table></div>'
    result = on_page_content(html, None, None, None)
    # Ne doit pas ajouter de div supplémentaire
    assert result.count('<div class="fr-table">') == 1


def test_no_table():
    """Vérifie que le HTML sans table n'est pas modifié."""
    html = "<p>Pas de table ici</p><div>Contenu</div>"
    result = on_page_content(html, None, None, None)
    assert result == html


def test_complex_table_multiline():
    """Vérifie le wrapping d'une table complexe multiligne."""
    html = """
    <table>
        <thead>
            <tr><th>Colonne 1</th><th>Colonne 2</th></tr>
        </thead>
        <tbody>
            <tr><td>Données</td><td>Autres</td></tr>
        </tbody>
    </table>
    """
    result = on_page_content(html, None, None, None)
    assert '<div class="fr-table">' in result
    assert "<thead>" in result
    assert "</tbody>" in result


def test_table_with_attributes():
    """Vérifie que les attributs de table sont préservés."""
    html = '<table id="my-table" class="custom-class"><tr><td>Data</td></tr></table>'
    result = on_page_content(html, None, None, None)
    assert '<div class="fr-table">' in result
    assert 'id="my-table"' in result
    assert 'class="custom-class"' in result


def test_malformed_html_graceful():
    """Vérifie le comportement avec HTML malformé."""
    # HTML avec table non fermée (cas limite)
    html = "<table><tr><td>Incomplete"
    result = on_page_content(html, None, None, None)
    # Le hook ne doit pas crasher, retourne l'input
    assert result == html or '<div class="fr-table">' in result
