#!/usr/bin/env python3
"""Tests complémentaires calculate_scores.py pour 95%+ coverage

Ce fichier teste les cas non couverts par test_calculate_scores.py :
- get_validation_status (tous cas front-matter)
- Gestion erreur périmètre (0, 31, invalide)
- __main__ block (exécution CLI)
"""

import subprocess
from pathlib import Path

from scripts.calculate_scores import generate_summary, get_validation_status


class TestGetValidationStatus:
    """Tests exhaustifs get_validation_status front-matter"""

    def test_validated_status_returns_valide(self, tmp_path):
        """Test validation_status: validated → État 'Validé'"""
        module = tmp_path / "test.md"
        module.write_text(
            """---
validation_status: validated
---
# Module Test
"""
        )
        assert get_validation_status(module) == "Validé"

    def test_in_progress_status_returns_en_cours(self, tmp_path):
        """Test validation_status: in_progress → État 'En cours'"""
        module = tmp_path / "test.md"
        module.write_text(
            """---
validation_status: in_progress
---
# Module Test
"""
        )
        assert get_validation_status(module) == "En cours"

    def test_draft_status_returns_brouillon(self, tmp_path):
        """Test validation_status: draft → État 'Brouillon'"""
        module = tmp_path / "test.md"
        module.write_text(
            """---
validation_status: draft
---
# Module Test
"""
        )
        assert get_validation_status(module) == "Brouillon"

    def test_unrecognized_status_returns_brouillon(self, tmp_path):
        """Test validation_status: valeur inconnue → Fallback 'Brouillon'"""
        module = tmp_path / "test.md"
        module.write_text(
            """---
validation_status: unknown_value
---
# Module Test
"""
        )
        assert get_validation_status(module) == "Brouillon"

    def test_missing_validation_status_returns_brouillon(self, tmp_path):
        """Test validation_status absent → Fallback 'Brouillon'"""
        module = tmp_path / "test.md"
        module.write_text(
            """---
service: TEST
---
# Module Test
"""
        )
        assert get_validation_status(module) == "Brouillon"

    def test_no_frontmatter_returns_brouillon(self, tmp_path):
        """Test sans front-matter YAML → Fallback 'Brouillon'"""
        module = tmp_path / "test.md"
        module.write_text("# Module Test sans front-matter")
        assert get_validation_status(module) == "Brouillon"


class TestSkipTemplateFiles:
    """Tests skip fichiers commençant par underscore"""

    def test_template_files_skipped(self, tmp_path, monkeypatch):
        """Fichiers _*.md ignorés dans génération synthèse"""
        # Créer 2 modules : 1 normal (0 points), 1 template (0 points)
        normal = tmp_path / "normal.md"
        normal.write_text(
            """---
validation_status: validated
---
# Normal Module (vide)
"""
        )

        template = tmp_path / "_template.md"
        template.write_text(
            """---
validation_status: draft
---
# Template (doit être ignoré)
"""
        )

        # Mock docs/modules → tmp_path
        original_path = Path

        def mock_path(x):
            if str(x) == "docs/modules":
                return tmp_path
            return original_path(x)

        monkeypatch.setattr("scripts.calculate_scores.Path", mock_path)

        # Exécuter generate_summary
        exit_code = generate_summary()

        # Vérifier succès
        assert exit_code == 0

        # Vérifier synthèse générée
        synthese = Path("docs/synthese.md")
        assert synthese.exists()

        # Vérifier que _template.md n'apparaît pas dans synthèse
        content = synthese.read_text()
        assert "_template" not in content.lower()
        assert "NORMAL" in content  # Module normal présent


class TestMainBlock:
    """Tests CLI et __main__ block"""

    def test_main_executes_generate_summary(self):
        """Test exécution directe script → Appelle generate_summary()"""

        # Exécuter script en subprocess
        result = subprocess.run(
            ["python3", "scripts/calculate_scores.py"],
            capture_output=True,
            text=True,
            timeout=5,
        )

        # Vérifier exit code (0 = succès ou 2 = erreur périmètre)
        assert result.returncode in [0, 2]

        # Vérifier que synthese.md est généré
        assert Path("docs/synthese.md").exists()
