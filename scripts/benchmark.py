#!/usr/bin/env python3
"""
Benchmark script pour collecter métriques performance SPAN SG.

Collecte :
- Temps build MkDocs
- Temps génération PDF
- Temps calcul scores
- Taille site/ et exports/
- Métadonnées build (commit, date)

Usage:
    python scripts/benchmark.py > benchmark-{sha}.json
"""

import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def get_git_sha() -> str:
    """Récupère le SHA du commit actuel."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()[:8]
    except subprocess.CalledProcessError:
        return "unknown"


def get_dir_size(path: Path) -> int:
    """Calcule taille totale d'un répertoire en bytes."""
    if not path.exists():
        return 0
    total = 0
    for item in path.rglob("*"):
        if item.is_file():
            total += item.stat().st_size
    return total


def benchmark_mkdocs_build() -> tuple[float, float]:
    """
    Benchmark build MkDocs DSFR.

    Returns:
        (duration_seconds, site_size_mb)
    """
    site_dir = Path("site")

    # Clean site/ avant build
    if site_dir.exists():
        subprocess.run(["rm", "-rf", "site"], check=False)

    # Mesurer temps build
    start = time.time()
    subprocess.run(
        ["mkdocs", "build", "--config-file", "mkdocs-dsfr.yml"],
        capture_output=True,
        check=True,
    )
    duration = time.time() - start

    # Mesurer taille site/
    size_bytes = get_dir_size(site_dir)
    size_mb = round(size_bytes / (1024 * 1024), 2)

    return duration, size_mb


def benchmark_pdf_generation() -> tuple[float, float]:
    """
    Benchmark génération PDF.

    Returns:
        (duration_seconds, pdf_size_mb)
    """
    pdf_path = Path("exports/span-sg.pdf")

    # Clean exports/ avant génération
    if pdf_path.exists():
        pdf_path.unlink()

    # Mesurer temps génération PDF
    start = time.time()
    subprocess.run(
        ["mkdocs", "build", "--config-file", "mkdocs-dsfr-pdf.yml"],
        capture_output=True,
        check=True,
        env={"ENABLE_PDF_EXPORT": "1", **os.environ},
    )
    duration = time.time() - start

    # Mesurer taille PDF
    size_mb = 0.0
    if pdf_path.exists():
        size_mb = round(pdf_path.stat().st_size / (1024 * 1024), 2)

    return duration, size_mb


def benchmark_score_calculation() -> tuple[float, int]:
    """
    Benchmark calcul scores SPAN.

    Returns:
        (duration_seconds, num_modules)
    """
    # Mesurer temps calcul
    start = time.time()
    subprocess.run(
        ["python", "scripts/calculate_scores.py"],
        capture_output=True,
        check=True,
    )
    duration = time.time() - start

    # Compter modules
    modules_dir = Path("docs/modules")
    num_modules = len(
        [f for f in modules_dir.glob("*.md") if not f.name.startswith("_")]
    )

    return duration, num_modules


def collect_benchmarks() -> dict[str, Any]:
    """
    Collecte toutes les métriques benchmark.

    Returns:
        dict avec métriques complètes
    """
    print("Collecting benchmarks...", flush=True)

    # Métadonnées build
    metadata = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "commit_sha": get_git_sha(),
        "python_version": subprocess.run(
            ["python", "--version"], capture_output=True, text=True
        ).stdout.strip(),
    }

    # Benchmark MkDocs build
    print("Benchmarking MkDocs build...", flush=True)
    mkdocs_time, site_size = benchmark_mkdocs_build()

    # Benchmark PDF generation
    print("Benchmarking PDF generation...", flush=True)
    pdf_time, pdf_size = benchmark_pdf_generation()

    # Benchmark score calculation
    print("Benchmarking score calculation...", flush=True)
    score_time, num_modules = benchmark_score_calculation()

    # Assembler résultats
    results = {
        "metadata": metadata,
        "timings": {
            "mkdocs_build_seconds": round(mkdocs_time, 2),
            "pdf_generation_seconds": round(pdf_time, 2),
            "score_calculation_seconds": round(score_time, 2),
            "total_seconds": round(mkdocs_time + pdf_time + score_time, 2),
        },
        "sizes": {
            "site_directory_mb": site_size,
            "pdf_file_mb": pdf_size,
        },
        "content": {
            "num_modules": num_modules,
        },
    }

    return results


def main() -> None:
    """Point d'entrée du script."""
    try:
        benchmarks = collect_benchmarks()
        print(json.dumps(benchmarks, indent=2))
    except Exception as e:
        print(f"Error during benchmarking: {e}", flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
