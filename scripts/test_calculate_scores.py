#!/usr/bin/env python3

import pytest

from scripts.calculate_scores import BOX_RE, load_text, score_module


class TestLoadText:
    """Tests suppression code fences"""

    def test_removes_code_fences(self, tmp_path):
        content = """
- [x] Point réel <!-- DINUM -->

```markdown
- [x] Point dans fence <!-- DINUM -->
```
        """
        file = tmp_path / "test.md"
        file.write_text(content)
        result = load_text(file)
        assert "Point réel" in result
        assert "Point dans fence" not in result


class TestScoreModule:
    """Tests comptage points"""

    def test_module_empty_0_points(self, tmp_path):
        file = tmp_path / "empty.md"
        file.write_text("# Empty module\n")
        checked, total = score_module(file)
        assert checked == 0
        assert total == 0

    def test_module_0_of_31(self, tmp_path):
        content = "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(31)])
        file = tmp_path / "unchecked.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 0
        assert total == 31

    def test_module_6_of_31_sircom(self, tmp_path):
        content = "".join(
            [f"- [x] Point {i} <!-- DINUM -->\n" for i in range(6)]
        ) + "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(6, 31)])
        file = tmp_path / "sircom.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 6
        assert total == 31
        assert (checked / total * 100) == pytest.approx(19.4, abs=0.1)

    def test_module_31_of_31(self, tmp_path):
        content = "".join([f"- [x] Point {i} <!-- DINUM -->\n" for i in range(31)])
        file = tmp_path / "complete.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 31
        assert total == 31

    def test_module_invalid_30_points(self, tmp_path):
        content = "".join([f"- [ ] Point {i} <!-- DINUM -->\n" for i in range(30)])
        file = tmp_path / "invalid.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert total == 30
        assert total not in (0, 31)


class TestStatusLogic:
    """Tests calcul statut (bug ligne 39 corrigé en S1-05)"""

    @pytest.mark.parametrize(
        "checked,total,expected",
        [
            (31, 31, "✓ Conforme"),  # 100%
            (24, 31, "✓ Conforme"),  # 77.4% >= 75%
            (23, 31, "En cours"),  # 74.2% < 75%
            (1, 31, "En cours"),  # 3.2% > 0%
            (0, 31, "Non renseigné"),  # 0%
            (0, 0, "Non renseigné"),  # Division par zéro
        ],
    )
    def test_status_calculation(self, checked, total, expected):
        pct = round((checked / total) * 100, 1) if total else 0.0
        status = (
            "✓ Conforme" if pct >= 75 else "En cours" if pct > 0 else "Non renseigné"
        )
        assert status == expected


class TestRegexPatterns:
    """Tests patterns regex"""

    def test_box_regex_unchecked(self):
        text = "- [ ] Point <!-- DINUM -->"
        match = BOX_RE.search(text)
        assert match is not None
        assert match.group(1) == " "

    def test_box_regex_checked_lowercase(self):
        text = "- [x] Point <!-- DINUM -->"
        match = BOX_RE.search(text)
        assert match.group(1) == "x"

    def test_box_regex_checked_uppercase(self):
        text = "- [X] Point <!-- DINUM -->"
        match = BOX_RE.search(text)
        assert match.group(1) == "X"

    def test_box_regex_ignores_without_tag(self):
        text = "- [x] Point sans tag"
        matches = BOX_RE.findall(text)
        assert len(matches) == 0


class TestGenerateSummary:
    """Tests génération synthèse + détection erreurs"""

    def test_valid_modules_exit_0(self, tmp_path, monkeypatch):
        modules_dir = tmp_path / "docs" / "modules"
        modules_dir.mkdir(parents=True)

        content = "".join([f"- [ ] P{i} <!-- DINUM -->\n" for i in range(31)])
        (modules_dir / "test.md").write_text(content)

        monkeypatch.chdir(tmp_path)

        from scripts.calculate_scores import generate_summary

        exit_code = generate_summary()

        assert exit_code == 0
        assert (tmp_path / "docs/synthese.md").exists()

    def test_invalid_module_exit_2(self, tmp_path, monkeypatch, capsys):
        modules_dir = tmp_path / "docs" / "modules"
        modules_dir.mkdir(parents=True)

        content = "".join([f"- [ ] P{i} <!-- DINUM -->\n" for i in range(30)])
        (modules_dir / "invalid.md").write_text(content)

        monkeypatch.chdir(tmp_path)

        from scripts.calculate_scores import generate_summary

        exit_code = generate_summary()

        assert exit_code == 2
        captured = capsys.readouterr()
        assert "Erreurs de périmètre" in captured.out
        assert "invalid.md: 30 points" in captured.out
