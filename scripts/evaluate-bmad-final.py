#!/usr/bin/env python3
"""
Évaluation BMAD finale de la roadmap SPAN SG
Après toutes les améliorations (Phase 1-4)
"""

import re
from pathlib import Path
from datetime import datetime

# Poids par dimension
WEIGHTS = {
    'structure': 25,
    'commands': 20,
    'tests': 20,
    'errors': 15,
    'deps': 10,
    'automation': 5,
    'refs': 5,
    'risks': 5
}

def score_story(file_path: Path) -> dict:
    """Score une story selon critères BMAD"""

    content = file_path.read_text(encoding='utf-8')
    scores = {}

    # Structure BMAD (25 pts)
    has_context = bool(re.search(r'##\s+Contexte\s+projet', content, re.I))
    has_objective = bool(re.search(r'##\s+Objectif', content, re.I))
    has_prereqs = bool(re.search(r'##\s+Prérequis', content, re.I))
    has_steps = bool(re.search(r'##\s+Étapes\s+d[\'"]implémentation', content, re.I))
    has_acceptance = bool(re.search(r'##\s+Critères\s+d[\'"]acceptation', content, re.I))
    scores['structure'] = (has_context + has_objective + has_prereqs + has_steps + has_acceptance) * 5

    # Commands (20 pts)
    bash_blocks = len(re.findall(r'```bash', content))
    cmd_coverage = min(bash_blocks / 10, 1.0)
    scores['commands'] = cmd_coverage * 20

    # Tests (20 pts)
    has_tests = bool(re.search(r'##\s+Tests\s+de\s+validation', content, re.I))
    test_cases = len(re.findall(r'#\s+Test\s+\d+\s*:', content, re.I))
    scores['tests'] = (has_tests * 10) + min(test_cases, 10)

    # Error handling (15 pts) - CRITÈRE PRINCIPAL AMÉLIORÉ
    has_error_section = bool(re.search(r'##\s+(Messages\s+d[\'"]erreur|Problèmes.*fréquents|Dépannage)', content, re.I))
    error_count = len(re.findall(r'(Erreur\s+\d+|Problème\s+\d+)\s*:', content, re.I))

    if has_error_section and error_count >= 6:
        scores['errors'] = 15  # Excellent
    elif has_error_section and error_count >= 3:
        scores['errors'] = 12  # Bon
    elif has_error_section:
        scores['errors'] = 8   # Moyen
    else:
        scores['errors'] = 3   # Minimal

    # Dependencies (10 pts)
    has_deps = bool(re.search(r'##\s+Dépendances', content, re.I))
    has_blocks = bool(re.search(r'\*\*Bloque\*\*\s*:', content))
    has_depends = bool(re.search(r'\*\*Dépend\s+de\*\*\s*:', content))
    scores['deps'] = (has_deps * 4) + (has_blocks * 3) + (has_depends * 3)

    # Automation (5 pts) - CRITÈRE AMÉLIORÉ
    has_script_ref = bool(re.search(r'(scripts/|\.sh|Option\s+automatique)', content))
    auto_usage = bool(re.search(r'./scripts/\S+\.sh', content))
    scores['automation'] = (has_script_ref * 3) + (auto_usage * 2)

    # References (5 pts) - CRITÈRE AMÉLIORÉ
    has_refs = bool(re.search(r'##\s+Références', content, re.I))
    has_bmad_header = content.startswith('---\nbmad_phase:')
    ref_count = len(re.findall(r'\*\*[A-Z]', re.search(r'##\s+Références.*?(?=##|\Z)', content, re.DOTALL).group() if re.search(r'##\s+Références', content, re.I) else ''))
    scores['refs'] = (has_refs * 2) + (ref_count >= 3) * 2 + (has_bmad_header * 1)

    # Risks/Notes (5 pts)
    has_risks = bool(re.search(r'##\s+Notes\s+et\s+risques', content, re.I))
    has_post = bool(re.search(r'##\s+Post-tâche', content, re.I))
    risk_count = len(re.findall(r'\*\*[A-Z][a-z]+.*\*\*', re.search(r'##\s+Notes\s+et\s+risques.*?(?=##|\Z)', content, re.DOTALL).group() if re.search(r'##\s+Notes\s+et\s+risques', content, re.I) else ''))
    scores['risks'] = (has_risks * 2) + (has_post * 1) + min(risk_count / 3, 2)

    # Total
    total = sum(scores.values())

    return {
        **scores,
        'total': total,
        'grade': get_grade(total)
    }

def get_grade(score: float) -> str:
    """Convertit score en grade"""
    if score >= 98: return 'A++'
    if score >= 95: return 'A+'
    if score >= 90: return 'A'
    if score >= 85: return 'B+'
    if score >= 80: return 'B'
    if score >= 75: return 'C+'
    if score >= 70: return 'C'
    return 'D'

def main():
    roadmap_dir = Path(__file__).parent.parent / 'roadmap'

    stories = sorted([
        f for f in roadmap_dir.glob('*.md')
        if f.stem.startswith('S') and '-' in f.stem
    ])

    if not stories:
        print("❌ Aucune story trouvée")
        return 1

    print(f"📊 Évaluation BMAD finale - {len(stories)} stories")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("="*100)
    print(f"{'Story':<25} {'Struct':<8} {'Cmd':<6} {'Test':<6} {'Err':<6} {'Deps':<6} {'Auto':<6} {'Refs':<6} {'Risk':<6} {'Total':<8} {'Grade':<6}")
    print("="*100)

    all_scores = []

    for story in stories:
        scores = score_story(story)
        all_scores.append(scores)

        print(f"{story.stem:<25} "
              f"{scores['structure']:>6.1f}  "
              f"{scores['commands']:>4.1f}  "
              f"{scores['tests']:>4.1f}  "
              f"{scores['errors']:>4.1f}  "
              f"{scores['deps']:>4.1f}  "
              f"{scores['automation']:>4.1f}  "
              f"{scores['refs']:>4.1f}  "
              f"{scores['risks']:>4.1f}  "
              f"{scores['total']:>6.1f}  "
              f"{scores['grade']:<6}")

    print("="*100)

    # Moyennes
    avg_structure = sum(s['structure'] for s in all_scores) / len(all_scores)
    avg_commands = sum(s['commands'] for s in all_scores) / len(all_scores)
    avg_tests = sum(s['tests'] for s in all_scores) / len(all_scores)
    avg_errors = sum(s['errors'] for s in all_scores) / len(all_scores)
    avg_deps = sum(s['deps'] for s in all_scores) / len(all_scores)
    avg_automation = sum(s['automation'] for s in all_scores) / len(all_scores)
    avg_refs = sum(s['refs'] for s in all_scores) / len(all_scores)
    avg_risks = sum(s['risks'] for s in all_scores) / len(all_scores)
    avg_total = sum(s['total'] for s in all_scores) / len(all_scores)

    print(f"{'MOYENNE':<25} "
          f"{avg_structure:>6.1f}  "
          f"{avg_commands:>4.1f}  "
          f"{avg_tests:>4.1f}  "
          f"{avg_errors:>4.1f}  "
          f"{avg_deps:>4.1f}  "
          f"{avg_automation:>4.1f}  "
          f"{avg_refs:>4.1f}  "
          f"{avg_risks:>4.1f}  "
          f"{avg_total:>6.1f}  "
          f"{get_grade(avg_total):<6}")
    print("="*100)

    # Distribution grades
    grades_count = {}
    for s in all_scores:
        grade = s['grade']
        grades_count[grade] = grades_count.get(grade, 0) + 1

    print()
    print("📈 Distribution grades :")
    for grade in ['A++', 'A+', 'A', 'B+', 'B', 'C+', 'C', 'D']:
        count = grades_count.get(grade, 0)
        percent = count / len(all_scores) * 100
        if count > 0:
            print(f"  {grade:<4} : {count:>2} stories ({percent:>5.1f}%)")

    print()
    print("="*100)
    print(f"🎯 SCORE GLOBAL FINAL : {avg_total:.1f}/100 - Grade {get_grade(avg_total)}")
    print("="*100)

    # Analyse amélioration par dimension
    print()
    print("📊 Amélioration par dimension (vs baseline 90.7) :")
    print(f"  Structure BMAD    : {avg_structure:.1f}/25 (inchangé - déjà parfait)")
    print(f"  Commands          : {avg_commands:.1f}/20 (inchangé)")
    print(f"  Tests             : {avg_tests:.1f}/20 (inchangé)")
    print(f"  Error handling    : {avg_errors:.1f}/15 (+9.1 attendu)")
    print(f"  Dependencies      : {avg_deps:.1f}/10 (inchangé)")
    print(f"  Automation        : {avg_automation:.1f}/5  (+2.6 attendu)")
    print(f"  References        : {avg_refs:.1f}/5   (+1.2 attendu)")
    print(f"  Risks/Notes       : {avg_risks:.1f}/5  (inchangé)")

    print()
    improvement = avg_total - 90.7
    if avg_total >= 99.9:
        print(f"✅ OBJECTIF ATTEINT : 100/100 ({improvement:+.1f} points)")
        print("🏆 Roadmap BMAD PARFAITE")
    elif avg_total >= 99.0:
        print(f"🎯 OBJECTIF PRESQUE ATTEINT : {avg_total:.1f}/100 ({improvement:+.1f} points)")
        print(f"   Manque {100 - avg_total:.1f} points pour perfection")
    else:
        print(f"⚠️  Objectif non atteint : {avg_total:.1f}/100 ({improvement:+.1f} points)")
        print(f"   Manque {100 - avg_total:.1f} points")

    return 0

if __name__ == '__main__':
    exit(main())
