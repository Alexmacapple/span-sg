#!/usr/bin/env python3
"""
Analyse historique benchmarks SPAN SG.

Compare benchmarks JSON et détecte régressions performance.

Usage:
    python scripts/analyze_benchmarks.py benchmark-*.json
    python scripts/analyze_benchmarks.py --download-last 10  # Future: via gh artifacts
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, cast

REGRESSION_THRESHOLD = 0.20  # 20% regression threshold


def load_benchmark(path: Path) -> dict[str, Any]:
    """Charge un fichier benchmark JSON."""
    with path.open("r") as f:
        return cast(dict[str, Any], json.load(f))


def compare_benchmarks(
    current: dict[str, Any], baseline: dict[str, Any]
) -> dict[str, Any]:
    """
    Compare deux benchmarks et détecte régressions.

    Returns:
        dict avec comparaisons et alertes
    """
    current_timings = current["timings"]
    baseline_timings = baseline["timings"]

    comparisons = {}
    regressions = []

    for key in current_timings:
        if key == "total_seconds":
            continue

        current_val = current_timings[key]
        baseline_val = baseline_timings.get(key, 0)

        if baseline_val == 0:
            continue

        diff = current_val - baseline_val
        pct_change = (diff / baseline_val) * 100

        comparisons[key] = {
            "current": current_val,
            "baseline": baseline_val,
            "diff": round(diff, 2),
            "pct_change": round(pct_change, 1),
        }

        # Détecter régression
        if pct_change > (REGRESSION_THRESHOLD * 100):
            regressions.append(
                {
                    "metric": key,
                    "pct_change": round(pct_change, 1),
                    "current": current_val,
                    "baseline": baseline_val,
                }
            )

    return {
        "comparisons": comparisons,
        "regressions": regressions,
        "baseline_commit": baseline["metadata"]["commit_sha"],
        "current_commit": current["metadata"]["commit_sha"],
    }


def generate_report(benchmarks: list[dict[str, Any]]) -> str:
    """
    Génère rapport textuel analyse benchmarks.

    Args:
        benchmarks: Liste de benchmarks triés par date (plus récent en premier)

    Returns:
        Rapport formaté
    """
    if not benchmarks:
        return "No benchmarks to analyze"

    report_lines = [
        "=" * 60,
        "SPAN SG Performance Benchmark Analysis",
        "=" * 60,
        "",
    ]

    # Benchmark le plus récent
    latest = benchmarks[0]
    report_lines.extend(
        [
            f"Latest Benchmark ({latest['metadata']['commit_sha']})",
            f"Timestamp: {latest['metadata']['timestamp']}",
            "",
            "Timings:",
            f"  MkDocs build:    {latest['timings']['mkdocs_build_seconds']}s",
            f"  PDF generation:  {latest['timings']['pdf_generation_seconds']}s",
            f"  Score calc:      {latest['timings']['score_calculation_seconds']}s",
            f"  Total:           {latest['timings']['total_seconds']}s",
            "",
            "Sizes:",
            f"  Site directory:  {latest['sizes']['site_directory_mb']} MB",
            f"  PDF file:        {latest['sizes']['pdf_file_mb']} MB",
            "",
        ]
    )

    # Comparaison avec baseline (si plusieurs benchmarks)
    if len(benchmarks) > 1:
        baseline = benchmarks[-1]  # Plus ancien = baseline
        comparison = compare_benchmarks(latest, baseline)

        report_lines.extend(
            [
                f"Comparison vs Baseline ({comparison['baseline_commit']})",
                "-" * 40,
                "",
            ]
        )

        for metric, data in comparison["comparisons"].items():
            symbol = "+" if data["diff"] > 0 else ""
            report_lines.append(
                f"  {metric:30s} {symbol}{data['diff']:6.2f}s ({symbol}{data['pct_change']:5.1f}%)"
            )

        report_lines.append("")

        # Alertes régressions
        if comparison["regressions"]:
            report_lines.extend(
                [
                    "PERFORMANCE REGRESSIONS DETECTED:",
                    "-" * 40,
                ]
            )
            for reg in comparison["regressions"]:
                report_lines.append(
                    f"  {reg['metric']:30s} +{reg['pct_change']:5.1f}% "
                    f"({reg['baseline']:.2f}s → {reg['current']:.2f}s)"
                )
            report_lines.append("")
        else:
            report_lines.extend(
                [
                    "No performance regressions detected.",
                    "",
                ]
            )

    # Historique complet
    if len(benchmarks) > 2:
        report_lines.extend(
            [
                "Historical Trend:",
                "-" * 40,
            ]
        )
        for bench in benchmarks[:10]:  # Limiter à 10 derniers
            commit = bench["metadata"]["commit_sha"]
            total = bench["timings"]["total_seconds"]
            timestamp = bench["metadata"]["timestamp"][:10]
            report_lines.append(f"  {timestamp}  {commit}  {total:6.2f}s total")
        report_lines.append("")

    report_lines.append("=" * 60)

    return "\n".join(report_lines)


def main() -> None:
    """Point d'entrée du script."""
    parser = argparse.ArgumentParser(description="Analyze SPAN SG benchmarks")
    parser.add_argument(
        "files",
        nargs="*",
        help="Benchmark JSON files to analyze",
    )
    parser.add_argument(
        "--download-last",
        type=int,
        metavar="N",
        help="Download last N benchmarks from GitHub artifacts (future feature)",
    )

    args = parser.parse_args()

    if args.download_last:
        print("ERROR: --download-last not yet implemented", file=sys.stderr)
        print("  Use: gh run download <run-id> --name benchmark-*", file=sys.stderr)
        sys.exit(1)

    if not args.files:
        print("ERROR: No benchmark files specified", file=sys.stderr)
        print(
            "Usage: python scripts/analyze_benchmarks.py benchmark-*.json",
            file=sys.stderr,
        )
        sys.exit(1)

    # Charger benchmarks
    benchmarks = []
    for file_path in args.files:
        path = Path(file_path)
        if not path.exists():
            print(f"WARNING: {file_path} not found, skipping", file=sys.stderr)
            continue
        benchmarks.append(load_benchmark(path))

    if not benchmarks:
        print("ERROR: No valid benchmarks loaded", file=sys.stderr)
        sys.exit(1)

    # Trier par timestamp (plus récent en premier)
    benchmarks.sort(
        key=lambda b: b["metadata"]["timestamp"],
        reverse=True,
    )

    # Générer et afficher rapport
    report = generate_report(benchmarks)
    print(report)

    # Exit code basé sur régressions
    if len(benchmarks) > 1:
        latest = benchmarks[0]
        baseline = benchmarks[-1]
        comparison = compare_benchmarks(latest, baseline)
        if comparison["regressions"]:
            sys.exit(1)  # Échec si régressions détectées


if __name__ == "__main__":
    main()
