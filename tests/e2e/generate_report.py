#!/usr/bin/env python3
"""Génère rapport HTML tests E2E"""
import sys
from datetime import datetime
from pathlib import Path


def parse_log(log_file):
    """Parse log scénario et extrait résultat"""
    content = log_file.read_text()

    # Détection status
    if "✅" in content or "SUCCESS" in content:
        status = "PASS"
    elif "⏭️" in content or "SKIP" in content:
        status = "SKIP"
    else:
        status = "FAIL"

    return {
        "name": log_file.stem.replace("scenario_", "")
        .replace("test_", "")
        .replace("_", " ")
        .title(),
        "status": status,
        "log": content,
    }


def generate_html(report_dir):
    """Génère rapport HTML depuis logs"""
    report_path = Path(report_dir)
    logs = sorted(report_path.glob("*.log"))

    if not logs:
        print("⚠️  Aucun fichier log trouvé")
        return

    results = [parse_log(log) for log in logs]

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    skipped = sum(1 for r in results if r["status"] == "SKIP")
    total = len(results)

    # Génération HTML
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tests E2E SPAN SG</title>
    <style>
        body {{
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            margin: 20px;
            background: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 10px;
        }}
        .summary {{
            background: #e8f4f8;
            padding: 15px;
            margin: 20px 0;
            border-left: 4px solid #0066cc;
            border-radius: 4px;
        }}
        .summary-stats {{
            display: flex;
            gap: 30px;
            margin-top: 10px;
        }}
        .stat {{
            font-size: 18px;
            font-weight: bold;
        }}
        .stat.pass {{ color: #28a745; }}
        .stat.fail {{ color: #dc3545; }}
        .stat.skip {{ color: #6c757d; }}
        .scenario {{
            border: 1px solid #ddd;
            margin: 15px 0;
            border-radius: 4px;
            overflow: hidden;
        }}
        .scenario-header {{
            padding: 12px 15px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .scenario-header.pass {{
            background: #d4edda;
            border-left: 4px solid #28a745;
        }}
        .scenario-header.fail {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
        }}
        .scenario-header.skip {{
            background: #e2e3e5;
            border-left: 4px solid #6c757d;
        }}
        .status-badge {{
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
        }}
        .status-badge.pass {{
            background: #28a745;
            color: white;
        }}
        .status-badge.fail {{
            background: #dc3545;
            color: white;
        }}
        .status-badge.skip {{
            background: #6c757d;
            color: white;
        }}
        .scenario-log {{
            background: #f8f9fa;
            padding: 15px;
            margin: 0;
            overflow-x: auto;
            font-size: 13px;
            line-height: 1.4;
            max-height: 400px;
            overflow-y: auto;
        }}
        .timestamp {{
            color: #6c757d;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🧪 Tests E2E SPAN SG</h1>

        <div class="summary">
            <strong>📊 Résumé</strong>
            <div class="summary-stats">
                <span class="stat pass">✅ Passés: {passed}</span>
                <span class="stat fail">❌ Échoués: {failed}</span>
                <span class="stat skip">⏭️ Skippés: {skipped}</span>
                <span class="stat">📦 Total: {total}</span>
            </div>
            <div class="timestamp">
                🕒 Généré le {datetime.now().strftime("%Y-%m-%d à %H:%M:%S")}
            </div>
        </div>
"""

    for result in results:
        status_lower = result["status"].lower()
        status_text = {"pass": "✅ PASS", "fail": "❌ FAIL", "skip": "⏭️ SKIP"}.get(
            status_lower, result["status"]
        )

        html += f"""
        <div class="scenario">
            <div class="scenario-header {status_lower}">
                <span>{result["name"]}</span>
                <span class="status-badge {status_lower}">{status_text}</span>
            </div>
            <pre class="scenario-log">{result["log"]}</pre>
        </div>
"""

    html += """
    </div>
</body>
</html>
"""

    report_file = report_path / "e2e-report.html"
    report_file.write_text(html, encoding="utf-8")
    print(f"✅ Rapport généré : {report_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_report.py <report_dir>")
        sys.exit(1)

    generate_html(sys.argv[1])
