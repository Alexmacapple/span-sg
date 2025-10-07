# Checklist démonstration S4-02

Support pour présentation Stéphane (15 min démo live)

## 6 points obligatoires

| Timing | Élément | URL/Action | Message clé |
|--------|---------|------------|-------------|
| 0-3 min | Homepage + disclaimer | Ouvrir https://alexmacapple.github.io/span-sg-repo/draft/ | "v1.0 hybrid : 2 modules validés (SIRCOM, SNUM), 4 en cours. Framework technique complet, transparence totale via disclaimers." |
| 3-7 min | Module SIRCOM (réel) | Cliquer navigation → SIRCOM, scroll vers 31 points | "24/31 points mappés depuis SPAN officiel. Sections obligatoires remplies. Points non cochés justifiés (budget annuel, tests utilisateurs)." |
| 7-10 min | Synthèse tableau de bord | Cliquer navigation → Synthèse | "Scoring automatisé (calculate_scores.py). Colonne État distingue modules validés vs en cours. Transparence : 24.2% global reflète stratégie hybrid." |
| 10-12 min | PDF export accessible | Montrer exports/span-sg.pdf (local ou télécharger) | "Export PDF automatisé. Métadonnées enrichies (Auteur: Secrétariat Général, Keywords: SPAN/RGAA). Disclaimer compliance en page de garde." |
| 12-14 min | Infrastructure CI/CD | Montrer https://github.com/Alexmacapple/span-sg-repo/actions | "CI/CD 100% PASS. Tests unitaires (18) + E2E (9). Déploiement automatique draft → /draft/, main → racine. Preview privée org-only." |
| 14-15 min | Architecture modulaire | Retour homepage, navigation latérale | "6 modules structurés. Cliquer SRH (en cours) : structure présente, prête pour onboarding. Framework scalable." |

## Points d'attention

- Transparent sur limitations (modules en cours)
- Montrer distinction visuelle : Badge "Validé" vs "En cours"
- Anticiper questions FAQ (voir docs/s4-02-faq.md)

## URLs à préparer avant démo

- Preview draft : https://alexmacapple.github.io/span-sg-repo/draft/
- GitHub Actions : https://github.com/Alexmacapple/span-sg-repo/actions
- PDF local : exports/span-sg.pdf

## Vérifications pré-démo

- [ ] Preview draft accessible (tester URL)
- [ ] Dernier CI 100% PASS (gh run list --branch draft --limit 1)
- [ ] PDF téléchargé et ouvrable (exports/span-sg.pdf)
- [ ] Navigation 6 modules fonctionnelle
- [ ] Disclaimer visible homepage
- [ ] Synthèse affichée avec colonne État
