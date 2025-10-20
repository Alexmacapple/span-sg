"""
Tests accessibilité SPAN SG (WCAG 2.1 AA / RGAA 4.1)

Catégories testées :
- Homepage WCAG (5 tests)
- Synthese table DSFR (4 tests)
- PDF metadata RGAA (3 tests)

Utilise axe-core via Selenium pour automatiser 60-65% des vérifications RGAA.
"""

from pathlib import Path

import pytest
from axe_selenium_python import Axe
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def site_dir():
    """Fixture: répertoire du site HTML généré."""
    site_path = Path("site")
    if not site_path.exists():
        pytest.skip("Site HTML non généré (mkdocs build requis)")
    return site_path


@pytest.fixture(scope="module")
def driver(site_dir):
    """Fixture: WebDriver Chrome headless pour tests."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Service avec timeout HTTP élevé pour CI
    service = Service()

    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(1920, 1080)

    # Augmenter timeouts pour CI (résout timeouts axe-core)
    driver.set_script_timeout(300)  # 300s (5min) pour scripts (axe.run())
    driver.implicitly_wait(30)  # 30s pour éléments DOM

    # Configurer timeout HTTP du client Selenium (urllib3)
    if hasattr(driver, "command_executor"):
        driver.command_executor._timeout = 300  # 300s pour requêtes HTTP

    yield driver

    driver.quit()


def load_page(driver, site_dir, page_path):
    """Charger une page HTML locale dans le navigateur."""
    file_url = f"file://{site_dir.resolve()}/{page_path}"
    driver.get(file_url)
    return file_url


# =============================================================================
# HOMEPAGE WCAG TESTS (5 scenarios)
# =============================================================================


def test_homepage_wcag_violations(driver, site_dir):
    """Vérifie que la homepage n'a aucune violation WCAG 2.1 AA critique."""
    load_page(driver, site_dir, "index.html")

    axe = Axe(driver)
    axe.inject()
    results = axe.run(options={"runOnly": ["wcag2a", "wcag2aa", "wcag21aa"]})

    violations = results["violations"]

    # Filtrer les violations critiques uniquement (impact: critical, serious)
    critical_violations = [
        v for v in violations if v.get("impact") in ["critical", "serious"]
    ]

    # WORKAROUND: Exclure search input label (bug upstream mkdocs-dsfr v0.17.0)
    # Le label est caché visuellement (CSS sr-only) mais axe-core le détecte comme violation.
    # Voir ADR-008 et issue GitLab mkdocs-dsfr pour résolution upstream.
    critical_violations = [
        v
        for v in critical_violations
        if not (
            v.get("id") == "label"
            and any(
                "#mkdocs-search-query" in str(node.get("target", []))
                for node in v.get("nodes", [])
            )
        )
    ]

    assert len(critical_violations) == 0, (
        f"Homepage a {len(critical_violations)} violation(s) WCAG critique(s) : "
        + ", ".join([v["id"] for v in critical_violations])
    )


def test_homepage_color_contrast(driver, site_dir):
    """Vérifie le contraste des couleurs (WCAG 2.1 - 1.4.3 Contrast)."""
    load_page(driver, site_dir, "index.html")

    axe = Axe(driver)
    axe.inject()
    results = axe.run(options={"runOnly": ["color-contrast"]})

    violations = results["violations"]
    assert (
        len(violations) == 0
    ), f"Contraste insuffisant détecté : {len(violations)} élément(s)"


def test_homepage_heading_hierarchy(driver, site_dir):
    """Vérifie la hiérarchie des titres <h1>-<h6> (WCAG 1.3.1)."""
    load_page(driver, site_dir, "index.html")

    # Vérifier présence h1 unique
    h1_elements = driver.find_elements(By.TAG_NAME, "h1")
    assert len(h1_elements) >= 1, "Au moins un <h1> requis sur homepage"

    axe = Axe(driver)
    axe.inject()
    results = axe.run(options={"runOnly": ["heading-order"]})

    violations = results["violations"]
    assert len(violations) == 0, "Hiérarchie des titres incorrecte"


def test_homepage_landmarks(driver, site_dir):
    """Vérifie présence des landmarks ARIA (navigation, main, footer)."""
    load_page(driver, site_dir, "index.html")

    axe = Axe(driver)
    axe.inject()
    results = axe.run(options={"runOnly": ["region", "landmark-one-main"]})

    violations = results["violations"]
    assert len(violations) == 0, "Landmarks ARIA manquants ou mal structurés"


def test_homepage_keyboard_navigation(driver, site_dir):
    """Vérifie que tous les éléments interactifs sont accessibles au clavier."""
    load_page(driver, site_dir, "index.html")

    axe = Axe(driver)
    axe.inject()
    results = axe.run(options={"runOnly": ["keyboard", "focus-order-semantics"]})

    violations = results["violations"]
    assert len(violations) == 0, "Éléments non accessibles au clavier détectés"


# =============================================================================
# SYNTHESE TABLE DSFR TESTS (4 scenarios)
# =============================================================================


@pytest.mark.skip(
    reason="Tests obsolètes: table remplacé par cards DSFR (index.md:119-167)"
)
def test_synthese_table_dsfr_wrapper(driver, site_dir):
    """Vérifie que le tableau synthèse est wrappé avec classes DSFR."""
    load_page(driver, site_dir, "index.html")

    # Rechercher le tableau SPAN
    table = driver.find_element(By.ID, "table-span-modules")

    # Vérifier présence wrapper DSFR
    parent = table.find_element(By.XPATH, "..")
    parent_classes = parent.get_attribute("class")

    assert (
        "fr-table__content" in parent_classes
    ), "Tableau doit être wrappé dans div.fr-table__content (DSFR)"


@pytest.mark.skip(
    reason="Tests obsolètes: table remplacé par cards DSFR (index.md:119-167)"
)
def test_synthese_table_aria_labels(driver, site_dir):
    """Vérifie les labels ARIA du tableau synthèse."""
    load_page(driver, site_dir, "index.html")

    axe = Axe(driver)
    axe.inject()

    # Cibler spécifiquement le tableau SPAN
    context = {"include": [["#table-span-modules"]]}
    results = axe.run(
        context=context, options={"runOnly": ["table", "td-headers-attr"]}
    )

    violations = results["violations"]
    assert len(violations) == 0, f"Tableau a {len(violations)} violation(s) ARIA"


@pytest.mark.skip(
    reason="Tests obsolètes: table remplacé par cards DSFR (index.md:119-167)"
)
def test_synthese_table_caption(driver, site_dir):
    """Vérifie présence et pertinence du <caption>."""
    load_page(driver, site_dir, "index.html")

    table = driver.find_element(By.ID, "table-span-modules")
    caption = table.find_element(By.TAG_NAME, "caption")

    assert caption is not None, "Tableau doit avoir un <caption>"
    assert len(caption.text) > 10, "Caption trop court (doit décrire le contenu)"


@pytest.mark.skip(
    reason="Tests obsolètes: table remplacé par cards DSFR (index.md:119-167)"
)
def test_synthese_table_responsive(driver, site_dir):
    """Vérifie que le tableau est responsive (DSFR)."""
    load_page(driver, site_dir, "index.html")

    # Tester en largeur mobile (375px)
    driver.set_window_size(375, 667)

    table_wrapper = driver.find_element(By.CLASS_NAME, "fr-table__wrapper")

    # Vérifier que le wrapper est visible (pas hidden)
    assert table_wrapper.is_displayed(), "Tableau doit rester accessible en mode mobile"

    # Restaurer largeur desktop
    driver.set_window_size(1920, 1080)


# =============================================================================
# PDF METADATA RGAA TESTS (3 scenarios)
# =============================================================================


@pytest.fixture(scope="module")
def pdf_file():
    """Fixture: fichier PDF exports/span-sg.pdf."""
    pdf_path = Path("exports/span-sg.pdf")
    if not pdf_path.exists():
        pytest.skip("PDF non généré (mkdocs-dsfr-pdf.yml requis)")
    return pdf_path


def test_pdf_metadata_title(pdf_file):
    """Vérifie que le PDF a un titre metadata (RGAA 13.1)."""
    try:
        import pikepdf
    except ImportError:
        pytest.skip("pikepdf non installé")

    with pikepdf.open(pdf_file) as pdf:
        metadata = pdf.docinfo

        assert "/Title" in metadata, "PDF doit avoir metadata /Title"
        title = str(metadata.get("/Title", ""))
        assert len(title) > 5, f"Titre PDF trop court : '{title}'"


def test_pdf_metadata_language(pdf_file):
    """Vérifie que le PDF a une langue déclarée (RGAA 13.3)."""
    try:
        import pikepdf
    except ImportError:
        pytest.skip("pikepdf non installé")

    with pikepdf.open(pdf_file) as pdf:
        # Vérifier dans catalog root
        if "/Lang" in pdf.Root:
            lang = str(pdf.Root.get("/Lang", ""))
            assert lang.startswith(
                "fr"
            ), f"Langue PDF doit être 'fr-FR' (actuel: {lang})"
        else:
            pytest.fail("PDF doit avoir metadata /Lang dans Root")


def test_pdf_metadata_description(pdf_file):
    """Vérifie présence metadata Subject/Description."""
    try:
        import pikepdf
    except ImportError:
        pytest.skip("pikepdf non installé")

    with pikepdf.open(pdf_file) as pdf:
        metadata = pdf.docinfo

        # Subject ou Description acceptable
        has_subject = "/Subject" in metadata
        has_description = "/Description" in metadata

        assert has_subject or has_description, "PDF doit avoir /Subject ou /Description"

        if has_subject:
            subject = str(metadata["/Subject"])
            assert len(subject) > 10, f"Subject trop court : '{subject}'"


# =============================================================================
# CONFIGURATION PYTEST
# =============================================================================


def pytest_configure(config):
    """Configuration pytest pour marqueurs personnalisés."""
    config.addinivalue_line("markers", "accessibility: Tests accessibilité WCAG/RGAA")
