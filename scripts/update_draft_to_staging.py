#!/usr/bin/env python3
"""Script pour remplacer draft par staging dans la documentation."""

import os
import re
from pathlib import Path

# Répertoire de base
BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / "docs"

# Motifs de remplacement
REPLACEMENTS = [
    (r"/draft/", "/staging/"),
    (r"→ draft →", "→ staging →"),
    (r"vers draft", "vers staging"),
    (r"sur draft", "sur staging"),
    (r"deploy_draft", "deploy_staging"),
    (r"\bdraft\b\s*\(staging\)", "staging"),  # "draft (staging)" -> "staging"
]


def should_process_file(filepath):
    """Vérifie si le fichier doit être traité."""
    path_str = str(filepath)
    # Exclure roadmap et archives
    if "/roadmap/" in path_str or "/archives/" in path_str:
        return False
    return filepath.suffix == ".md"


def update_file(filepath):
    """Met à jour un fichier avec les remplacements."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Appliquer les remplacements
        for pattern, replacement in REPLACEMENTS:
            content = re.sub(pattern, replacement, content)

        # Sauvegarder si modifié
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Erreur traitement {filepath}: {e}")
    return False


def main():
    """Traite tous les fichiers markdown."""
    updated_files = []

    # Parcourir tous les fichiers markdown
    for filepath in DOCS_DIR.rglob("*.md"):
        if should_process_file(filepath):
            if update_file(filepath):
                rel_path = filepath.relative_to(BASE_DIR)
                updated_files.append(str(rel_path))
                print(f"Updated: {rel_path}")

    print(f"\nTotal: {len(updated_files)} fichiers mis à jour")
    return len(updated_files)


if __name__ == "__main__":
    count = main()
    exit(0 if count >= 0 else 1)
