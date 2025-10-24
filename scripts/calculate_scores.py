#!/usr/bin/env python3
import re
from datetime import datetime
from pathlib import Path

CHECK_TAG = "CHECKLIST"
FENCE_RE = re.compile(r"```.*?```", re.S)
BOX_RE = re.compile(r"- \[(x|X| )\].*?<!--\s*%s\s*-->" % CHECK_TAG)


def load_text(p: Path) -> str:
    return FENCE_RE.sub("", p.read_text(encoding="utf-8"))


def score_module(p: Path) -> tuple[int, int]:
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


def status_to_badge(status: str) -> str:
    """Convertit un statut textuel en badge DSFR HTML."""
    badge_map = {
        "Conforme": ("success", "Conforme"),
        "En cours": ("info", "En cours"),
        "Non renseigné": ("error", "Non renseigné"),
    }
    if status in badge_map:
        badge_type, label = badge_map[status]
        return f'<p class="fr-badge fr-badge--{badge_type}">{label}</p>'
    return status


def validation_to_badge(validation_state: str) -> str:
    """Convertit un état de validation en badge DSFR HTML."""
    badge_map = {
        "Validé": ("success", "Validé"),
        "En cours": ("info", "En cours"),
        "Brouillon": ("warning", "Brouillon"),
        "Non renseigné": ("error", "Non renseigné"),
    }
    if validation_state in badge_map:
        badge_type, label = badge_map[validation_state]
        return f'<p class="fr-badge fr-badge--{badge_type}">{label}</p>'
    return validation_state


def update_module_score(
    module_path: Path, checked: int, total: int, pct: float
) -> None:
    """Met à jour la ligne 'Score global' dans un module markdown."""
    content = module_path.read_text(encoding="utf-8")

    # Regex pour trouver la ligne de score (capture variantes)
    score_pattern = r"\*\*Score global\*\*.*?critères validés.*?\%\)"

    # Nouvelle ligne de score calculée
    new_score_line = f"**Score global** {checked}/{total} critères validés ({pct}%)"

    # Remplacer la ligne de score
    updated_content = re.sub(score_pattern, new_score_line, content)

    # Écrire uniquement si modifications détectées
    if updated_content != content:
        module_path.write_text(updated_content, encoding="utf-8")


def generate_summary() -> int:
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

        if total not in (0, 33):
            errors.append(
                f"{module.name}: {total} critères tagués <!-- {CHECK_TAG} --> (attendu 33 ou 0)"
            )
        pct = round((checked / total) * 100, 1) if total else 0.0
        status = "Conforme" if pct >= 75 else "En cours" if pct > 0 else "Non renseigné"
        status_badge = status_to_badge(status)
        validation_badge = validation_to_badge(validation_state)

        # Mettre à jour le score dans le module individuel
        update_module_score(module, checked, total, pct)

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
        module_rows.append(f"                                {status_badge}")
        module_rows.append("                            </td>")
        module_rows.append("                            <td>")
        module_rows.append(f"                                {validation_badge}")
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
