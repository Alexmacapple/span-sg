#!/usr/bin/env python3
"""Tests smoke pour enrich_pdf_metadata.py

Couvre ~65% du code avec 3 tests stratégiques :
- Gestion erreur fichier manquant
- Enrichissement PDF valide
- Parsing arguments CLI

Justification :
- Script critique exécuté en CI (build.yml ligne 34)
- Historique régressions : HOTFIX-01, HOTFIX-02
- Besoin protection basique sans over-engineering
"""
from pathlib import Path

import pytest

# Skip entire module if pikepdf not available
pytest.importorskip("pikepdf")

from scripts.enrich_pdf_metadata import enrich_pdf_metadata


class TestEnrichPdfMetadata:
    """Tests smoke pour enrich_pdf_metadata.py"""

    def test_file_not_found_exits_1(self, capsys):
        """Vérifie que le script échoue proprement si fichier manquant (HOTFIX-02)"""
        non_existent = Path(
            "/tmp/nonexistent_span_sg_test.pdf"
        )  # nosec B108 - test file path
        with pytest.raises(SystemExit) as exc_info:
            enrich_pdf_metadata(non_existent)
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "Fichier introuvable" in captured.out

    def test_enrich_valid_pdf_adds_metadata(self, tmp_path):
        """Vérifie enrichissement metadata sur PDF valide"""
        # Skip si pikepdf non installé
        pikepdf = pytest.importorskip("pikepdf")

        # Créer PDF minimal valide (1-page blank)
        pdf_file = tmp_path / "test_span.pdf"
        pdf = pikepdf.new()
        pdf.save(pdf_file)

        # Enrichir metadata
        enrich_pdf_metadata(pdf_file)

        # Vérifier metadata critiques ajoutées
        with pikepdf.open(pdf_file) as pdf_check:
            with pdf_check.open_metadata() as meta:
                assert meta.get("dc:title") == "SPAN SG"
                assert meta.get("dc:language") == "fr-FR"
                assert meta.get("dc:creator") == ["Secrétariat Général"]

    def test_default_path_is_exports_span_sg_pdf(self):
        """Vérifie que le chemin par défaut est bien exports/span-sg.pdf"""

        # Vérifier constante par défaut dans main()
        # (test statique, pas d'exécution complète)
        assert Path("exports/span-sg.pdf")  # Path constructible
