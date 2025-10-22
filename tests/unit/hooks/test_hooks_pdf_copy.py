"""Tests unitaires pour hooks/pdf_copy.py"""

from pathlib import Path
from unittest.mock import patch

import pytest

from hooks.pdf_copy import on_post_build


@pytest.fixture
def temp_config(tmp_path):
    """Fixture: configuration MkDocs avec répertoires temporaires."""
    site_dir = tmp_path / "site"
    docs_dir = tmp_path / "docs"
    site_dir.mkdir()
    docs_dir.mkdir()
    return {"site_dir": str(site_dir), "docs_dir": str(docs_dir)}


@pytest.fixture
def pdf_source(tmp_path):
    """Fixture: crée un PDF source factice dans exports/."""
    exports_dir = tmp_path / "exports"
    exports_dir.mkdir()
    pdf_file = exports_dir / "span-sg.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 fake content" * 5000)  # ~100KB
    return pdf_file


def test_copy_success(temp_config, pdf_source, tmp_path, capsys, monkeypatch):
    """Vérifie que le PDF est copié vers docs/ et site/ en cas de succès."""
    # Changer working directory vers tmp_path pour trouver exports/
    monkeypatch.chdir(tmp_path)

    on_post_build(temp_config)

    # Vérifier que les fichiers de destination existent
    site_dir = Path(temp_config["site_dir"])
    docs_dir = Path(temp_config["docs_dir"])

    pdf_dst_site = site_dir / "exports" / "span-sg.pdf"
    pdf_dst_docs = docs_dir / "exports" / "span-sg.pdf"

    assert pdf_dst_site.exists(), "PDF non copié vers site/exports/"
    assert pdf_dst_docs.exists(), "PDF non copié vers docs/exports/"

    # Vérifier le contenu copié
    assert pdf_dst_site.read_bytes() == pdf_source.read_bytes()
    assert pdf_dst_docs.read_bytes() == pdf_source.read_bytes()

    # Vérifier les messages de succès
    captured = capsys.readouterr()
    assert "PDF copié vers docs" in captured.out
    assert "PDF copié vers site" in captured.out
    assert "MB" in captured.out


def test_missing_pdf(temp_config, tmp_path, capsys, monkeypatch):
    """Vérifie le comportement quand le PDF source est absent."""
    # Pas de PDF créé, juste changer de répertoire
    monkeypatch.chdir(tmp_path)

    # Créer exports/ vide pour que le hook ne crash pas sur autre chose
    exports_dir = tmp_path / "exports"
    exports_dir.mkdir()

    on_post_build(temp_config)

    # Vérifier qu'aucun fichier n'est copié
    site_dir = Path(temp_config["site_dir"])
    docs_dir = Path(temp_config["docs_dir"])

    pdf_dst_site = site_dir / "exports" / "span-sg.pdf"
    pdf_dst_docs = docs_dir / "exports" / "span-sg.pdf"

    assert not pdf_dst_site.exists(), "PDF ne devrait pas être copié vers site/"
    assert not pdf_dst_docs.exists(), "PDF ne devrait pas être copié vers docs/"

    # Vérifier le message d'avertissement
    captured = capsys.readouterr()
    assert "PDF source absent" in captured.out
    assert "ENABLE_PDF_EXPORT" in captured.out


def test_missing_config_keys(pdf_source, tmp_path, monkeypatch):
    """Vérifie qu'une KeyError est levée si config incomplète."""
    monkeypatch.chdir(tmp_path)

    # Config sans site_dir
    config_no_site = {"docs_dir": str(tmp_path / "docs")}
    with pytest.raises(KeyError, match="site_dir"):
        on_post_build(config_no_site)

    # Config sans docs_dir
    config_no_docs = {"site_dir": str(tmp_path / "site")}
    with pytest.raises(KeyError, match="docs_dir"):
        on_post_build(config_no_docs)


def test_permissions_error(temp_config, pdf_source, tmp_path, monkeypatch):
    """Vérifie qu'une PermissionError lors de la copie est propagée."""
    monkeypatch.chdir(tmp_path)

    # Mock shutil.copy2 pour lever PermissionError
    with patch("hooks.pdf_copy.shutil.copy2") as mock_copy:
        mock_copy.side_effect = PermissionError("Permission denied")

        with pytest.raises(PermissionError, match="Permission denied"):
            on_post_build(temp_config)


def test_create_directories(temp_config, pdf_source, tmp_path, monkeypatch):
    """Vérifie que les répertoires de destination sont créés automatiquement."""
    monkeypatch.chdir(tmp_path)

    site_dir = Path(temp_config["site_dir"])
    docs_dir = Path(temp_config["docs_dir"])

    # Vérifier que exports/ n'existe pas encore dans site/ et docs/
    assert not (site_dir / "exports").exists()
    assert not (docs_dir / "exports").exists()

    on_post_build(temp_config)

    # Vérifier que les répertoires ont été créés
    assert (site_dir / "exports").exists(), "Répertoire site/exports/ non créé"
    assert (docs_dir / "exports").exists(), "Répertoire docs/exports/ non créé"

    # Vérifier que les PDFs sont copiés
    assert (site_dir / "exports" / "span-sg.pdf").exists()
    assert (docs_dir / "exports" / "span-sg.pdf").exists()


def test_file_size_display(temp_config, tmp_path, capsys, monkeypatch):
    """Vérifie que la taille du fichier est affichée correctement."""
    monkeypatch.chdir(tmp_path)

    # Créer un PDF de taille connue (1 MB exact)
    exports_dir = tmp_path / "exports"
    exports_dir.mkdir()
    pdf_file = exports_dir / "span-sg.pdf"
    pdf_file.write_bytes(b"0" * (1024 * 1024))  # 1 MB

    on_post_build(temp_config)

    captured = capsys.readouterr()
    # Devrait afficher ~1.0 MB
    assert "1.0 MB" in captured.out
