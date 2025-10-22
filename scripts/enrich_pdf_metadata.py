#!/usr/bin/env python3
"""
Enrichissement des metadata PDF pour conformité et accessibilité.

Ce script ajoute des metadata XMP/PDF étendues au PDF généré par MkDocs,
incluant : keywords, langue, subject, description.

Usage:
    python scripts/enrich_pdf_metadata.py [input.pdf] [output.pdf]

    Par défaut : exports/span-sg.pdf (modifié sur place)

Dépendances:
    pip install pikepdf
"""

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import pikepdf
except ImportError:
    print("❌ Erreur: pikepdf non installé")
    print("   Installer avec: pip install pikepdf")
    sys.exit(1)


def enrich_pdf_metadata(input_path: Path, output_path: Optional[Path] = None):
    """
    Enrichit les metadata d'un PDF existant.

    Args:
        input_path: Chemin du PDF source
        output_path: Chemin du PDF enrichi (optionnel, modifie sur place si absent)
    """
    if not input_path.exists():
        print(f"❌ Fichier introuvable: {input_path}")
        sys.exit(1)

    if output_path is None:
        output_path = input_path

    print(f"📄 Enrichissement metadata: {input_path}")

    try:
        # Ouvrir PDF avec pikepdf
        with pikepdf.open(input_path, allow_overwriting_input=True) as pdf:
            # Ouvrir metadata XMP
            with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
                # Metadata Dublin Core (DC)
                meta["dc:title"] = "SPAN SG"
                meta["dc:language"] = "fr-FR"
                meta["dc:creator"] = ["Secrétariat Général"]
                meta["dc:subject"] = "Schéma Pluriannuel d'Accessibilité Numérique"
                meta["dc:description"] = (
                    "Plan d'accessibilité numérique du Secrétariat Général 2025-2027. "
                    "Suivi des 31 points de contrôle DINUM pour les 6 services : "
                    "SNUM, SIRCOM, SRH, SIEP, SAFI, BGS."
                )

                # Metadata PDF spécifiques
                meta["pdf:Keywords"] = "SPAN, accessibilité, SG, numérique, RGAA, DINUM"
                meta["pdf:Producer"] = "MkDocs Material + mkdocs-with-pdf + pikepdf"

                # Metadata XMP
                meta["xmp:CreatorTool"] = "MkDocs Material 9.x"
                meta["xmp:CreateDate"] = datetime.now(timezone.utc).isoformat()
                meta["xmp:MetadataDate"] = datetime.now(timezone.utc).isoformat()

            # Définir langue dans Root catalog (requis RGAA 13.3 - test_pdf_metadata_language)
            pdf.Root.Lang = "fr-FR"

            # Sauvegarder PDF enrichi
            pdf.save(output_path)

        print("✅ Metadata enrichies avec succès")
        print(f"   Output: {output_path}")

        # Afficher résumé metadata
        print("\n📋 Metadata ajoutées:")
        print("   - Titre       : SPAN SG")
        print("   - Langue      : fr-FR")
        print("   - Auteur      : Secrétariat Général")
        print("   - Subject     : Schéma Pluriannuel d'Accessibilité Numérique")
        print("   - Keywords    : SPAN, accessibilité, SG, numérique, RGAA, DINUM")
        print(f"   - Date        : {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}")

    except Exception as e:
        print(f"❌ Erreur lors de l'enrichissement: {e}")
        sys.exit(1)


def main() -> None:
    """Point d'entrée du script."""
    # Parser arguments
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
    else:
        input_path = Path("exports/span-sg.pdf")

    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path  # Modifier sur place

    enrich_pdf_metadata(input_path, output_path)


if __name__ == "__main__":
    main()
