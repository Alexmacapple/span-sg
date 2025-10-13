#!/usr/bin/env python3
import re
from datetime import datetime
from pathlib import Path

CHECK_TAG = "DINUM"
FENCE_RE = re.compile(r"```.*?```", re.S)
BOX_RE = re.compile(r"- \[(x|X| )\].*?<!--\s*%s\s*-->" % CHECK_TAG)


def load_text(p: Path) -> str:
    return FENCE_RE.sub("", p.read_text(encoding="utf-8"))


def score_module(p: Path):
    boxes = BOX_RE.findall(load_text(p))
    total = len(boxes)
    checked = sum(1 for b in boxes if b.lower() == "x")
    return checked, total


def get_validation_status(p: Path) -> str:
    """Extract validation_status from front-matter YAML."""
    content = p.read_text(encoding="utf-8")
    # Match validation_status in front-matter (between --- delimiters)
    match = re.search(r"^---\s*\n(.*?)\n---", content, re.MULTILINE | re.DOTALL)
    if match:
        frontmatter = match.group(1)
        status_match = re.search(r"validation_status:\s*(\w+)", frontmatter)
        if status_match:
            status = status_match.group(1).lower()
            if status == "validated":
                return "Validé"
            elif status == "in_progress":
                return "En cours"
            elif status == "draft":
                return "Brouillon"
    # Fallback if validation_status not found or unrecognized
    return "Brouillon"


def generate_summary():
    modules_dir = Path("docs/modules")

    # Disclaimer en-tête (option e Q35 : ton neutre pour synthèse)
    disclaimer = (
        "**État du déploiement v1.0** : 1 module validé (SIRCOM), "
        "5 modules en cours de complétion. Framework production-ready, contenus enrichis progressivement."
    )

    rows = [
        "# Tableau de bord SPAN SG",
        "",
        f"*Mis à jour le {datetime.now():%d/%m/%Y}*",
        "",
        disclaimer,
        "",
        '<div class="fr-table fr-table--bordered" id="table-synthese-span">',
        '    <div class="fr-table__wrapper">',
        '        <div class="fr-table__container">',
        '            <div class="fr-table__content">',
        '                <table id="table-span-modules">',
        "                    <caption>",
        "                        Synthèse des modules SPAN par service",
        "                    </caption>",
        "                    <thead>",
        "                        <tr>",
        '                            <th scope="col">',
        "                                Service",
        "                            </th>",
        '                            <th scope="col">',
        "                                Score",
        "                            </th>",
        '                            <th scope="col">',
        "                                Statut",
        "                            </th>",
        '                            <th scope="col">',
        "                                État",
        "                            </th>",
        "                        </tr>",
        "                    </thead>",
        "                    <tbody>",
    ]

    total_checked = 0
    total_items = 0
    errors = []
    module_rows = []

    for module in sorted(modules_dir.glob("*.md")):
        if module.name.startswith("_"):
            continue
        checked, total = score_module(module)
        validation_state = get_validation_status(module)

        if total not in (0, 31):
            errors.append(
                f"{module.name}: {total} points tagués <!-- {CHECK_TAG} --> (attendu 31 ou 0)"
            )
        pct = round((checked / total) * 100, 1) if total else 0.0
        status = "Conforme" if pct >= 75 else "En cours" if pct > 0 else "Non renseigné"

        service_key = module.stem.lower()
        module_rows.append(
            f'                        <tr id="table-span-row-{service_key}" data-row-key="{service_key}">'
        )
        module_rows.append("                            <td>")
        module_rows.append(f"                                {module.stem.upper()}")
        module_rows.append("                            </td>")
        module_rows.append("                            <td>")
        module_rows.append(
            f"                                {checked}/{total} ({pct}%)"
        )
        module_rows.append("                            </td>")
        module_rows.append("                            <td>")
        module_rows.append(f"                                {status}")
        module_rows.append("                            </td>")
        module_rows.append("                            <td>")
        module_rows.append(f"                                {validation_state}")
        module_rows.append("                            </td>")
        module_rows.append("                        </tr>")

        total_checked += checked
        total_items += total

    rows.extend(module_rows)

    global_pct = round((total_checked / total_items) * 100, 1) if total_items else 0.0
    rows.extend(
        [
            '                        <tr id="table-span-row-total" data-row-key="total">',
            "                            <td>",
            "                                <strong>TOTAL</strong>",
            "                            </td>",
            "                            <td>",
            f"                                <strong>{total_checked}/{total_items} ({global_pct}%)</strong>",
            "                            </td>",
            "                            <td>",
            "                                <strong>Global</strong>",
            "                            </td>",
            "                            <td>",
            "                            </td>",
            "                        </tr>",
            "                    </tbody>",
            "                </table>",
            "            </div>",
            "        </div>",
            "    </div>",
            "</div>",
        ]
    )

    Path("docs/synthese.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

    if errors:
        print("Erreurs de périmètre:")
        for e in errors:
            print(" -", e)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(generate_summary())
