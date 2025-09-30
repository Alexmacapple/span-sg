#!/usr/bin/env python3
"""
Script d'ajout headers BMAD aux stories roadmap
Ajoute metadata YAML en début de chaque fichier story
"""

import os
from pathlib import Path

# Header BMAD à ajouter
BMAD_HEADER = """---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

"""

def add_bmad_header(file_path: Path):
    """Ajoute header BMAD à un fichier story s'il n'existe pas"""

    content = file_path.read_text(encoding='utf-8')

    # Vérifier si header BMAD déjà présent
    if content.startswith('---\nbmad_phase:'):
        print(f"⏭️  {file_path.name}: Header BMAD déjà présent, skip")
        return False

    # Ajouter header
    new_content = BMAD_HEADER + content
    file_path.write_text(new_content, encoding='utf-8')
    print(f"✅ {file_path.name}: Header BMAD ajouté")
    return True

def main():
    """Process tous les fichiers roadmap/*.md"""

    roadmap_dir = Path(__file__).parent.parent / 'roadmap'

    if not roadmap_dir.exists():
        print(f"❌ Répertoire roadmap non trouvé : {roadmap_dir}")
        return 1

    # Trouver tous les fichiers .md (sauf README, templates, etc.)
    story_files = [
        f for f in roadmap_dir.glob('*.md')
        if f.stem.startswith('S') and '-' in f.stem
    ]

    if not story_files:
        print("❌ Aucun fichier story trouvé dans roadmap/")
        return 1

    print(f"🔍 Trouvé {len(story_files)} fichiers story")
    print()

    modified_count = 0
    for story_file in sorted(story_files):
        if add_bmad_header(story_file):
            modified_count += 1

    print()
    print(f"✅ {modified_count} fichiers modifiés")
    print(f"⏭️  {len(story_files) - modified_count} fichiers déjà à jour")

    return 0

if __name__ == '__main__':
    exit(main())
