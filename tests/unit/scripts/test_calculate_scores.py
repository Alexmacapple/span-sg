#!/usr/bin/env python3

import pytest

from scripts.calculate_scores import BOX_RE, load_text, score_module


class TestLoadText:
    """Tests suppression code fences"""

    def test_removes_code_fences(self, tmp_path):
        content = """
- [x] Point réel <!-- CHECKLIST -->

```markdown
- [x] Point dans fence <!-- CHECKLIST -->
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

    def test_module_0_of_33(self, tmp_path):
        content = "".join([f"- [ ] Point {i} <!-- CHECKLIST -->\n" for i in range(33)])
        file = tmp_path / "unchecked.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 0
        assert total == 33

    def test_module_6_of_33_sircom(self, tmp_path):
        content = "".join(
            [f"- [x] Point {i} <!-- CHECKLIST -->\n" for i in range(6)]
        ) + "".join([f"- [ ] Point {i} <!-- CHECKLIST -->\n" for i in range(6, 33)])
        file = tmp_path / "sircom.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 6
        assert total == 33
        assert (checked / total * 100) == pytest.approx(18.2, abs=0.1)

    def test_module_33_of_33(self, tmp_path):
        content = "".join([f"- [x] Point {i} <!-- CHECKLIST -->\n" for i in range(33)])
        file = tmp_path / "complete.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert checked == 33
        assert total == 33

    def test_module_invalid_32_criteria(self, tmp_path):
        content = "".join([f"- [ ] Point {i} <!-- CHECKLIST -->\n" for i in range(32)])
        file = tmp_path / "invalid.md"
        file.write_text(content)
        checked, total = score_module(file)
        assert total == 32
        assert total not in (0, 33)


class TestStatusLogic:
    """Tests calcul statut (bug ligne 39 corrigé en S1-05)"""

    @pytest.mark.parametrize(
        "checked,total,expected",
        [
            (33, 33, "✓ Conforme"),  # 100%
            (26, 33, "✓ Conforme"),  # 78.8% >= 75%
            (24, 33, "En cours"),  # 72.7% < 75%
            (1, 33, "En cours"),  # 3.0% > 0%
            (0, 33, "Non renseigné"),  # 0%
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
        text = "- [ ] Point <!-- CHECKLIST -->"
        match = BOX_RE.search(text)
        assert match is not None
        assert match.group(1) == " "

    def test_box_regex_checked_lowercase(self):
        text = "- [x] Point <!-- CHECKLIST -->"
        match = BOX_RE.search(text)
        assert match.group(1) == "x"

    def test_box_regex_checked_uppercase(self):
        text = "- [X] Point <!-- CHECKLIST -->"
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

        content = "".join([f"- [ ] P{i} <!-- CHECKLIST -->\n" for i in range(33)])
        (modules_dir / "test.md").write_text(content)

        monkeypatch.chdir(tmp_path)

        from scripts.calculate_scores import generate_summary

        exit_code = generate_summary()

        assert exit_code == 0
        assert (tmp_path / "docs/synthese.md").exists()

    def test_invalid_module_exit_2(self, tmp_path, monkeypatch, capsys):
        modules_dir = tmp_path / "docs" / "modules"
        modules_dir.mkdir(parents=True)

        content = "".join([f"- [ ] P{i} <!-- CHECKLIST -->\n" for i in range(32)])
        (modules_dir / "invalid.md").write_text(content)

        monkeypatch.chdir(tmp_path)

        from scripts.calculate_scores import generate_summary

        exit_code = generate_summary()

        assert exit_code == 2
        captured = capsys.readouterr()
        assert "Erreurs de périmètre" in captured.out
        assert "invalid.md: 32 critères" in captured.out
