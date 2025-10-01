---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: enhancement
autonomous: false
validation: human-qa
---

# Story S5-01 : PDF accessible (WCAG 2.1 AA)

**Phase** : Semaine 5+ (post-v1.0) – Améliorations continues
**Priorité** : Moyenne
**Estimation** : 3-5 jours
**Assigné** : Alexandra

---

## Contexte projet

Le PDF généré par `mkdocs-pdf-export-plugin` (ou `mkdocs-with-pdf`) n'est **pas accessible par défaut** :
- Pas de structure sémantique (balises PDF)
- Pas de texte alternatif sur images/graphiques
- Ordre de lecture non garanti
- Metadata incomplètes
- Contraste couleurs non vérifié

Cette story améliore l'accessibilité du PDF pour respecter les **critères WCAG 2.1 niveau AA**, conformément aux exigences RGAA du SPAN.

---

## Objectif

Produire un PDF **accessible** et **conforme WCAG 2.1 AA** :
- Structure sémantique correcte (titres H1-H6, listes, tableaux)
- Texte alternatif sur tous les éléments visuels
- Ordre de lecture logique
- Metadata complètes (titre, auteur, langue, mots-clés)
- Contraste couleurs ≥ 4.5:1 (texte normal) et ≥ 3:1 (texte large)
- Navigation par signets (bookmarks)
- Formulaires accessibles (si checkboxes interactives)

---

## Prérequis

- [ ] Story S2-02 complétée (export PDF fonctionnel)
- [ ] Story S4-04 complétée (première release publiée)
- [ ] Python 3.11+ avec `pikepdf` ou `PyPDF2`
- [ ] Outil de validation : Adobe Acrobat Pro, PAC 2024, ou axe DevTools
- [ ] Connaissance WCAG 2.1 niveau AA

---

## Étapes d'implémentation

### Phase 1 : Audit accessibilité du PDF actuel

#### 1.1 Générer le PDF de référence
```bash
mkdocs build --config-file mkdocs-pdf.yml
ls -lh exports/span-sg.pdf
```

#### 1.2 Tester avec PAC 2024 (PDF Accessibility Checker)
- Télécharger PAC : https://pac.pdf-accessibility.org/
- Ouvrir `exports/span-sg.pdf`
- Lancer l'analyse complète
- **Attendu** : Liste des erreurs WCAG

Erreurs typiques :
- ❌ Document non balisé (untagged)
- ❌ Langue non définie
- ❌ Titre manquant
- ❌ Images sans texte alternatif
- ❌ Ordre de lecture incorrect
- ❌ Contraste insuffisant

#### 1.3 Documenter les écarts
Créer `docs/audit/pdf-accessibility-report.md` :
```markdown
# Audit accessibilité PDF – SPAN SG

**Date** : AAAA-MM-JJ
**Outil** : PAC 2024
**Fichier** : exports/span-sg.pdf v1.0.0

## Résumé
- Erreurs WCAG AA : 42
- Avertissements : 18
- Conformité : ❌ Non conforme

## Détail des erreurs
| Critère WCAG | Description | Occurences |
|--------------|-------------|------------|
| 1.1.1 | Images sans texte alternatif | 8 |
| 1.3.1 | Structure sémantique absente | 15 |
| 1.4.3 | Contraste insuffisant | 3 |
| 2.4.2 | Titre du document manquant | 1 |
| 3.1.1 | Langue non définie | 1 |
...
```

---

### Phase 2 : Enrichir les metadata PDF

#### 2.1 Créer un script d'enrichissement
Le script `scripts/enrich_pdf_metadata.py` doit :
```python
#!/usr/bin/env python3
"""
Enrichit les metadata d'un PDF pour améliorer l'accessibilité.
Usage: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
"""

import sys
from pikepdf import Pdf

def enrich_metadata(pdf_path: str):
    pdf = Pdf.open(pdf_path)

    # Metadata de base
    with pdf.open_metadata() as meta:
        meta['dc:title'] = 'SPAN SG 2025-2027'
        meta['dc:creator'] = 'Secrétariat Général'
        meta['dc:subject'] = 'Schéma Pluriannuel d\'Accessibilité Numérique'
        meta['dc:description'] = 'Plan d\'action accessibilité numérique 2025-2027'
        meta['dc:language'] = 'fr-FR'
        meta['dc:date'] = '2025-01-01'
        meta['pdf:Keywords'] = 'SPAN, accessibilité, RGAA, DINUM, services numériques'

    # Marquer comme PDF/UA (Universal Accessibility)
    pdf.Root.MarkInfo = {
        '/Marked': True,
        '/UserProperties': False,
        '/Suspects': False
    }

    # Définir langue du document
    pdf.Root.Lang = 'fr-FR'

    # Définir titre pour la barre de titre
    pdf.Root.ViewerPreferences = {
        '/DisplayDocTitle': True
    }

    # Sauvegarder
    output_path = pdf_path.replace('.pdf', '-accessible.pdf')
    pdf.save(output_path)
    print(f"✓ PDF enrichi : {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python enrich_pdf_metadata.py <pdf-file>")
        sys.exit(1)
    enrich_metadata(sys.argv[1])
```

#### 2.2 Installer dépendances
```bash
pip install pikepdf
# ou
echo "pikepdf>=8.0.0" >> requirements.txt
```

#### 2.3 Tester l'enrichissement
```bash
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
# Attendu : exports/span-sg-accessible.pdf

# Vérifier metadata
pdfinfo exports/span-sg-accessible.pdf | grep -E "Title|Author|Language"
```

---

### Phase 3 : Ajouter les balises sémantiques (tagging)

**Problème** : `mkdocs-pdf-export-plugin` ne génère **pas de PDF balisé** (tagged PDF).

**Solutions** :

#### Option A : Post-traitement avec Adobe Acrobat Pro
1. Ouvrir `exports/span-sg.pdf` dans Acrobat Pro
2. Outils > Accessibilité > Ajouter des balises au document
3. Outils > Accessibilité > Ordre de lecture
4. Outils > Accessibilité > Vérifier l'accessibilité complète
5. Corriger manuellement les erreurs (texte alt, ordre de lecture)
6. Enregistrer sous `exports/span-sg-accessible.pdf`

**Avantages** : Contrôle total, résultats garantis
**Inconvénients** : Manuel, non reproductible, licence Acrobat Pro requise

#### Option B : Changer de plugin MkDocs
Alternatives avec meilleur support accessibilité :
- **mkdocs-print-site-plugin** + impression navigateur en PDF/A
- **WeasyPrint** (via `mkdocs-with-pdf`) : supporte CSS `@media print` et balises ARIA
- **Pandoc** : conversion Markdown → PDF via LaTeX (meilleur contrôle structure)

Exemple avec WeasyPrint :
```yaml
# mkdocs-pdf.yml
plugins:
  - with-pdf:
      author: Secrétariat Général
      copyright: © 2025 Secrétariat Général
      cover_title: SPAN SG
      cover_subtitle: Schéma Pluriannuel d'Accessibilité Numérique 2025-2027
      output_path: exports/span-sg.pdf
      enabled_if_env: ENABLE_PDF_EXPORT
      # Options accessibilité
      render_js: false
      headless_chrome_path: null
      # WeasyPrint génère des PDF mieux structurés
```

#### Option C : Pipeline Pandoc personnalisé
```bash
# Concaténer tous les Markdown
cat docs/index.md docs/synthese.md docs/modules/*.md > /tmp/span-combined.md

# Générer PDF avec Pandoc + LaTeX
pandoc /tmp/span-combined.md \
  -o exports/span-sg.pdf \
  --pdf-engine=xelatex \
  --metadata title="SPAN SG 2025-2027" \
  --metadata author="Secrétariat Général" \
  --metadata lang="fr-FR" \
  --toc --toc-depth=3 \
  --template=templates/span-pdf.latex
```

**Recommandation** : Tester Option B (WeasyPrint) d'abord, sinon Option A en post-traitement manuel.

---

### Phase 4 : Ajouter texte alternatif aux images

#### 4.1 Inventorier les images
```bash
grep -r "!\[" docs/ --include="*.md"
# Lister toutes les images Markdown
```

#### 4.2 Ajouter attributs alt manquants
Exemple dans `docs/index.md` :
```markdown
<!-- Avant -->
![Logo SG](assets/logo-sg.png)

<!-- Après -->
![Logo du Secrétariat Général représentant...](assets/logo-sg.png)
```

#### 4.3 Images décoratives
Si image purement décorative, utiliser alt vide :
```markdown
![](assets/decorative-border.png)
```

#### 4.4 Graphiques et diagrammes
Pour graphiques complexes, fournir description longue :
```markdown
![Diagramme de Gantt du planning SPAN 2025-2027](assets/gantt.png)

**Description détaillée** : Le diagramme présente 4 phases sur 4 semaines...
```

---

### Phase 5 : Vérifier contraste des couleurs

#### 5.1 Auditer le thème Material
Le thème `mkdocs-material` par défaut respecte WCAG AA, mais vérifier :
```bash
# Installer outil de vérification
npm install -g pa11y-ci

# Tester page synthèse
pa11y http://localhost:8000/span-sg-repo/synthese/ \
  --standard WCAG2AA \
  --reporter cli
```

#### 5.2 Vérifier contraste PDF
Avec PAC 2024 ou axe DevTools :
- Texte normal : ratio ≥ 4.5:1
- Texte large (≥18pt) : ratio ≥ 3:1
- Éléments UI (boutons, liens) : ratio ≥ 3:1

Si contraste insuffisant, ajuster CSS dans `docs/stylesheets/extra.css`.

---

### Phase 6 : Ajouter signets de navigation (bookmarks)

Les signets PDF (table des matières interactive) améliorent la navigation.

#### 6.1 Vérifier génération auto
Certains plugins génèrent automatiquement les signets depuis les titres H1-H6.

Tester avec `pdfinfo` :
```bash
pdfinfo -meta exports/span-sg.pdf | grep Outlines
# Attendu : Outlines: yes
```

Si absents, post-traiter avec `pdftk` ou script Python :
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("exports/span-sg.pdf")
writer = PdfWriter()

# Copier pages
for page in reader.pages:
    writer.add_page(page)

# Ajouter signets
writer.add_outline_item("Accueil", 0)
writer.add_outline_item("Synthèse", 1)
writer.add_outline_item("Processus", 2)
writer.add_outline_item("Modules", 3)
# ...

with open("exports/span-sg-bookmarks.pdf", "wb") as f:
    writer.write(f)
```

---

### Phase 7 : Validation finale WCAG 2.1 AA

#### 7.1 Test PAC 2024
```bash
# Générer PDF final
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf

# Ouvrir dans PAC
open exports/span-sg-accessible.pdf
```

Checklist PAC :
- [ ] 0 erreur WCAG AA
- [ ] Document balisé (tagged)
- [ ] Langue définie
- [ ] Titre présent
- [ ] Images avec texte alt
- [ ] Ordre de lecture logique
- [ ] Contraste ≥ 4.5:1
- [ ] Signets présents

#### 7.2 Test lecteur d'écran
Tester avec NVDA (Windows) ou VoiceOver (Mac) :
```bash
# Mac
open exports/span-sg-accessible.pdf
# Activer VoiceOver : Cmd+F5
# Naviguer dans le PDF : touches fléchées
```

Vérifier :
- ✓ Titre du document annoncé
- ✓ Navigation par titres (H1-H6)
- ✓ Texte alt des images annoncé
- ✓ Tableaux navigables (en-têtes lus)
- ✓ Liens cliquables et identifiables

#### 7.3 Test conformité RGAA
Le SPAN doit être conforme à ses propres exigences.

Générer déclaration d'accessibilité pour le PDF :
```markdown
# Déclaration d'accessibilité – PDF SPAN SG

**Date** : AAAA-MM-JJ
**Fichier** : exports/span-sg-accessible.pdf v1.1.0

## Conformité
Ce document est **partiellement conforme** au RGAA 4.1 niveau AA.

## Résultats des tests
- Critères conformes : 48/50
- Critères non conformes : 2/50
- Taux de conformité : 96%

## Contenus non accessibles
### Non-conformités
- Critère 1.3.1 : Ordre de lecture tableau p.12 non optimal
- Critère 4.1.2 : Formulaire interactif (checkboxes) non accessible

### Dérogations
- Graphiques complexes (diagrammes Gantt) : description textuelle fournie en complément

## Voies de recours
Contact : accessibility@secretariat-general.gouv.fr
```

---

## Critères d'acceptation

- [ ] Audit accessibilité documenté (`docs/audit/pdf-accessibility-report.md`)
- [ ] Script `enrich_pdf_metadata.py` fonctionnel et intégré à la CI
- [ ] Metadata PDF complètes (titre, auteur, langue, mots-clés)
- [ ] PDF balisé (tagged) avec structure sémantique
- [ ] Toutes images ont un texte alternatif pertinent
- [ ] Contraste couleurs ≥ 4.5:1 vérifié
- [ ] Signets de navigation présents
- [ ] 0 erreur WCAG AA dans PAC 2024
- [ ] Test lecteur d'écran réussi (NVDA ou VoiceOver)
- [ ] Déclaration d'accessibilité PDF publiée
- [ ] Procédure documentée dans README.md

---

## Tests de validation

```bash
# Test 1 : Metadata présentes
pdfinfo exports/span-sg-accessible.pdf | grep -E "Title|Author|Language" && echo "OK" || echo "FAIL"
# Attendu : OK (3 lignes)

# Test 2 : PDF balisé
pdfinfo exports/span-sg-accessible.pdf | grep "Tagged:" | grep -q "yes" && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : Signets présents
pdfinfo exports/span-sg-accessible.pdf | grep "Outlines:" | grep -q "yes" && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : Taille raisonnable
test $(du -k exports/span-sg-accessible.pdf | cut -f1) -lt 10240 && echo "OK" || echo "WARN: PDF > 10 MB"
# Attendu : OK

# Test 5 : Validation PAC automatique (si outil CLI disponible)
# pac-cli exports/span-sg-accessible.pdf --standard WCAG2AA && echo "OK" || echo "FAIL"
```

---

## Dépendances

**Bloque** :
- Aucune (amélioration post-release)

**Dépend de** :
- S2-02 (export PDF fonctionnel)
- S4-04 (première release publiée)

---

## Références

- **WCAG 2.1** : https://www.w3.org/WAI/WCAG21/quickref/
- **PDF/UA** : https://pdfa.org/resource/pdfua-in-a-nutshell/
- **PAC 2024** : https://pac.pdf-accessibility.org/
- **RGAA 4.1** : https://accessibilite.numerique.gouv.fr/
- **pikepdf docs** : https://pikepdf.readthedocs.io/

---

## Notes et risques

### Plugin MkDocs limité
`mkdocs-pdf-export-plugin` et `mkdocs-with-pdf` ne génèrent **pas de PDF balisés** nativement.

**Solutions** :
1. Post-traitement manuel avec Acrobat Pro (coûteux, non reproductible)
2. Migration vers WeasyPrint ou Pandoc (refonte partielle)
3. Hybride : génération auto + enrichissement script Python

**Recommandation** : Commencer par enrichissement metadata (Phase 2), puis évaluer ROI du tagging complet (Phase 3).

### Coût de maintenance
Chaque modification de contenu nécessite re-validation accessibilité.

**Mitigation** :
- Automatiser tests PAC en CI (si version CLI disponible)
- Checklist validation dans PR template
- Formation équipe aux bonnes pratiques accessibilité

### Alternatives légères
Si accessibilité complète trop coûteuse, **alternatives** :
- **Version HTML accessible** (prioritaire) + PDF informatif
- **PDF simplifié** (texte brut) + lien vers site web
- **Déclaration de dérogation** (charge disproportionnée) + contact support

### Charge disproportionnée ?
Selon RGAA, une charge disproportionnée peut être invoquée si :
- Coût de mise en conformité > 10% budget projet
- Ressources humaines insuffisantes
- Alternative accessible fournie (site web)

Documenter dans `docs/index.md` section "Charge disproportionnée".

---

## Post-tâche

### Intégrer enrichissement à la CI
Modifier `.github/workflows/build.yml` :
```yaml
- name: Generate PDF
  run: mkdocs build --config-file mkdocs-pdf.yml

- name: Enrich PDF metadata
  run: python scripts/enrich_pdf_metadata.py exports/span-sg.pdf

- name: Validate PDF accessibility (optional)
  run: |
    # Si outil CLI disponible
    # pac-cli exports/span-sg-accessible.pdf --standard WCAG2AA
    echo "Manual PAC validation required"
```

### Documenter dans README
Ajouter section :
```markdown
## Accessibilité du PDF

Le PDF généré respecte les critères WCAG 2.1 niveau AA :
- Metadata complètes (titre, auteur, langue)
- Structure sémantique (titres, listes, tableaux)
- Texte alternatif sur images
- Contraste couleurs ≥ 4.5:1
- Signets de navigation

**Génération** :
```bash
mkdocs build --config-file mkdocs-pdf.yml
python scripts/enrich_pdf_metadata.py exports/span-sg.pdf
```

**Validation** :
- Télécharger PAC 2024 : https://pac.pdf-accessibility.org/
- Ouvrir `exports/span-sg-accessible.pdf`
- Lancer analyse complète
- Attendu : 0 erreur WCAG AA
```

### Commiter
```bash
git add scripts/enrich_pdf_metadata.py
git add docs/audit/pdf-accessibility-report.md
git add README.md
git commit -m "feat(pdf): amélioration accessibilité WCAG 2.1 AA"
git push origin feature/pdf-accessible
```

---

## Métriques de succès

- **Conformité** : 0 erreur WCAG AA dans PAC 2024
- **Utilisabilité** : Test lecteur d'écran réussi (NVDA/VoiceOver)
- **Performance** : Génération PDF + enrichissement < 60s
- **Maintenabilité** : Script automatisé, reproductible en CI
- **Documentation** : Procédure complète dans README + déclaration accessibilité
