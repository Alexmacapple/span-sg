"""Tests unitaires pour hooks/fix_sidemenu_ids.py"""

from hooks.fix_sidemenu_ids import on_post_page


def test_fix_single_sidemenu_id():
    """Vérifie la correction d'un seul ID dupliqué dans le sidemenu."""
    html = """
    <button aria-controls="fr-sidemenu-wrapper">Section 1</button>
    <div id="fr-sidemenu-wrapper">Contenu</div>
    """
    result = on_post_page(html, None, None)
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result
    assert 'fr-sidemenu-wrapper"' not in result


def test_fix_multiple_sidemenu_ids():
    """Vérifie la correction de plusieurs IDs dupliqués."""
    html = """
    <button aria-controls="fr-sidemenu-wrapper">Section 1</button>
    <div id="fr-sidemenu-wrapper">Contenu 1</div>
    <button aria-controls="fr-sidemenu-wrapper">Section 2</button>
    <div id="fr-sidemenu-wrapper">Contenu 2</div>
    """
    result = on_post_page(html, None, None)
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result
    assert 'aria-controls="fr-sidemenu-wrapper-2"' in result
    assert 'id="fr-sidemenu-wrapper-2"' in result
    assert 'fr-sidemenu-wrapper"' not in result


def test_fix_aria_controls_and_id_pairs():
    """Vérifie que aria-controls et id sont tous deux numérotés."""
    html = """
    <button aria-controls="fr-sidemenu-wrapper">Titre</button>
    <div class="fr-collapse" id="fr-sidemenu-wrapper">Liste</div>
    """
    result = on_post_page(html, None, None)
    assert result.count('-1"') == 2  # aria-controls-1 et id-1


def test_preserve_other_attributes():
    """Vérifie que les autres attributs sont préservés."""
    html = """
    <button class="fr-sidemenu__btn" aria-controls="fr-sidemenu-wrapper" aria-expanded="false">Section</button>
    <div class="fr-collapse" id="fr-sidemenu-wrapper" data-section="intro">Contenu</div>
    """
    result = on_post_page(html, None, None)
    assert 'class="fr-sidemenu__btn"' in result
    assert 'aria-expanded="false"' in result
    assert 'class="fr-collapse"' in result
    assert 'data-section="intro"' in result
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result


def test_no_sidemenu():
    """Vérifie que le HTML sans sidemenu n'est pas modifié."""
    html = "<p>Pas de menu</p><div id='autre-id'>Contenu</div>"
    result = on_post_page(html, None, None)
    assert result == html


def test_sidemenu_with_different_id():
    """Vérifie que seuls les IDs fr-sidemenu-wrapper sont modifiés."""
    html = """
    <button aria-controls="fr-sidemenu-wrapper">Section</button>
    <div id="fr-sidemenu-wrapper">Menu</div>
    <button aria-controls="autre-id">Autre</button>
    <div id="autre-id">Autre contenu</div>
    """
    result = on_post_page(html, None, None)
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result
    assert 'aria-controls="autre-id"' in result  # Inchangé
    assert 'id="autre-id"' in result  # Inchangé


def test_three_or_more_sidemenus():
    """Vérifie le traitement de 3+ sections de menu."""
    html = """
    <button aria-controls="fr-sidemenu-wrapper">S1</button>
    <div id="fr-sidemenu-wrapper">C1</div>
    <button aria-controls="fr-sidemenu-wrapper">S2</button>
    <div id="fr-sidemenu-wrapper">C2</div>
    <button aria-controls="fr-sidemenu-wrapper">S3</button>
    <div id="fr-sidemenu-wrapper">C3</div>
    """
    result = on_post_page(html, None, None)
    assert 'wrapper-1"' in result
    assert 'wrapper-2"' in result
    assert 'wrapper-3"' in result
    assert result.count('aria-controls="fr-sidemenu-wrapper-') == 3
    assert result.count('id="fr-sidemenu-wrapper-') == 3


def test_sidemenu_structure_complete():
    """Vérifie le traitement d'une structure sidemenu DSFR complète."""
    html = """
    <nav class="fr-sidemenu" role="navigation">
        <div class="fr-sidemenu__inner">
            <button class="fr-sidemenu__btn" aria-controls="fr-sidemenu-wrapper" aria-expanded="false">
                Introduction
            </button>
            <div class="fr-collapse" id="fr-sidemenu-wrapper">
                <ul class="fr-sidemenu__list">
                    <li><a href="#section1">Section 1</a></li>
                </ul>
            </div>
        </div>
    </nav>
    """
    result = on_post_page(html, None, None)
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result
    assert 'class="fr-sidemenu"' in result
    assert 'class="fr-sidemenu__btn"' in result
    assert 'class="fr-collapse"' in result


def test_sidemenu_multiline():
    """Vérifie le traitement des éléments sur plusieurs lignes."""
    html = """
    <button
        class="fr-sidemenu__btn"
        aria-controls="fr-sidemenu-wrapper"
        aria-expanded="false">
        Titre
    </button>
    <div
        class="fr-collapse"
        id="fr-sidemenu-wrapper">
        Contenu
    </div>
    """
    result = on_post_page(html, None, None)
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result


def test_mismatched_aria_id_counts():
    """Vérifie le traitement avec nombres différents d'aria-controls et id (edge case)."""
    # Cas anormal mais le hook doit continuer sans crash
    html = """
    <button aria-controls="fr-sidemenu-wrapper">S1</button>
    <button aria-controls="fr-sidemenu-wrapper">S2</button>
    <div id="fr-sidemenu-wrapper">C1</div>
    """
    result = on_post_page(html, None, None)
    # Le hook traite quand même, même si la structure HTML est cassée
    assert 'aria-controls="fr-sidemenu-wrapper-1"' in result
    assert 'aria-controls="fr-sidemenu-wrapper-2"' in result
    assert 'id="fr-sidemenu-wrapper-1"' in result


def test_sidemenu_ids_sequential():
    """Vérifie que la numérotation est séquentielle et cohérente."""
    html = """
    <button aria-controls="fr-sidemenu-wrapper">S1</button>
    <div id="fr-sidemenu-wrapper">C1</div>
    <button aria-controls="fr-sidemenu-wrapper">S2</button>
    <div id="fr-sidemenu-wrapper">C2</div>
    <button aria-controls="fr-sidemenu-wrapper">S3</button>
    <div id="fr-sidemenu-wrapper">C3</div>
    """
    result = on_post_page(html, None, None)

    # Vérifier ordre séquentiel
    pos_aria_1 = result.find('aria-controls="fr-sidemenu-wrapper-1"')
    pos_id_1 = result.find('id="fr-sidemenu-wrapper-1"')
    pos_aria_2 = result.find('aria-controls="fr-sidemenu-wrapper-2"')
    pos_id_2 = result.find('id="fr-sidemenu-wrapper-2"')
    pos_aria_3 = result.find('aria-controls="fr-sidemenu-wrapper-3"')
    pos_id_3 = result.find('id="fr-sidemenu-wrapper-3"')

    # Ordre: aria-1 < id-1 < aria-2 < id-2 < aria-3 < id-3
    assert pos_aria_1 < pos_id_1 < pos_aria_2 < pos_id_2 < pos_aria_3 < pos_id_3
