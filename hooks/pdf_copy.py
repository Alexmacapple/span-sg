#!/usr/bin/env python3
"""
Hook MkDocs : Copie PDF vers site/ pour download web.

Événement : on_post_build
Copie : exports/span-sg.pdf → site/exports/span-sg.pdf

Usage :
    Déclaré dans mkdocs-dsfr.yml :
    hooks:
      - hooks/pdf_copy.py
"""

import shutil
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass


def on_post_build(config: Any) -> None:
    """
    Hook exécuté après génération site MkDocs.

    Args:
        config: Configuration MkDocs (dict)
    """
    pdf_src = Path("exports/span-sg.pdf")
    site_dir = Path(config["site_dir"])
    docs_dir = Path(config["docs_dir"])

    pdf_dst_site = site_dir / "exports" / "span-sg.pdf"
    pdf_dst_docs = docs_dir / "exports" / "span-sg.pdf"

    if not pdf_src.exists():
        print(f"⚠️  PDF source absent : {pdf_src}")
        print("   (Normal si ENABLE_PDF_EXPORT non défini)")
        return

    # Copier vers docs/ (pour mkdocs serve)
    pdf_dst_docs.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf_src, pdf_dst_docs)
    size_mb = pdf_dst_docs.stat().st_size / (1024 * 1024)
    print(f"✅ PDF copié vers docs : {pdf_dst_docs} ({size_mb:.1f} MB)")

    # Copier vers site/ (pour builds statiques)
    pdf_dst_site.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf_src, pdf_dst_site)
    print(f"✅ PDF copié vers site : {pdf_dst_site} ({size_mb:.1f} MB)")
