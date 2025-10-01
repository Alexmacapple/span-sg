---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S2-02 : Export PDF automatique

**Phase** : Semaine 2 - Automatisation
**Priorité** : Haute
**Estimation** : 45min
**Assigné** : Alexandra

---

## Contexte projet

L'export PDF est un **livrable critique** pour chaque release SPAN SG. Il permet :
- Archive officielle du SPAN complet
- Distribution hors-ligne (réunions, audits)
- Annexe aux releases GitHub
- Conformité documentaire

**Stratégie simplifiée** :
1. Plugin principal : `mkdocs-pdf-export-plugin`
2. Méthode manuelle de secours : impression navigateur sur page Synthèse

Configuration unique :
- `mkdocs.yml` : Config principale (sans PDF)
- `mkdocs-pdf.yml` : Config export PDF

---

## Objectif

Tester le plugin PDF en local et dans la CI, garantir qu'un PDF est généré à chaque build, et documenter la méthode manuelle de secours.

---

## Prérequis

- [ ] Story S1-03 complétée (MkDocs configuré)
- [ ] Story S2-01 complétée (CI GitHub Actions fonctionnelle)
- [ ] Python 3.11+ avec pip
- [ ] Docker (pour tests isolés)

---

## Étapes d'implémentation

### 1. Vérifier la configuration PDF existante

```bash
# Config principale (sans PDF)
grep -A 5 "plugins:" mkdocs.yml

# Config export PDF
cat mkdocs-pdf.yml
```

Contenu attendu de `mkdocs-pdf.yml` :
```yaml
site_name: SPAN SG
theme:
  name: material
plugins:
  - pdf-export:
      combined: true
      combined_output_path: exports/span-sg.pdf
```

### 2. Installer le plugin PDF en local

```bash
pip install mkdocs-pdf-export-plugin
```

### 3. Tester la génération PDF

```bash
# Build avec config PDF
mkdocs build --config-file mkdocs-pdf.yml

# Vérifier génération
ls -lh exports/span-sg.pdf
# Attendu : Fichier PDF ~500KB-2MB

# Ouvrir et vérifier contenu
open exports/span-sg.pdf  # Mac
# OU
xdg-open exports/span-sg.pdf  # Linux
```

Points à vérifier dans le PDF :
- ✓ Page de garde "SPAN SG"
- ✓ Table des matières
- ✓ Accueil, Synthèse, Processus
- ✓ 6 modules (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
- ✓ Tableaux bien formatés
- ✓ Checkboxes lisibles
- ✓ Navigation/liens internes fonctionnels

### 4. Tester la génération dans Docker

```bash
# Build image Docker (inclut mkdocs-pdf-export-plugin)
docker compose build

# Générer PDF via Docker
docker compose run --rm mkdocs build --config-file mkdocs-pdf.yml

# Vérifier
ls -lh exports/span-sg.pdf
```

### 5. Vérifier la CI GitHub Actions

Le workflow `.github/workflows/build.yml` contient :
```yaml
- name: Install dependencies
  run: |
    pip install mkdocs-material
    pip install mkdocs-pdf-export-plugin

- name: Generate PDF
  run: mkdocs build --config-file mkdocs-pdf.yml
```

Pousser un commit sur `draft` et vérifier :
- ✅ Step "Generate PDF" réussit
- ✅ Artefact contient `exports/span-sg.pdf`

### 6. Documenter la méthode manuelle de secours

Si le plugin échoue, méthode manuelle :

```bash
# Démarrer serveur local
docker compose up

# Ouvrir navigateur
open http://localhost:8000/synthese/

# Imprimer en PDF (Cmd+P / Ctrl+P)
# Destination : Enregistrer au format PDF
# Nom fichier : span-sg-synthese.pdf
```

Cette méthode est documentée dans README.md section "Dépannage rapide".

### 7. Vérifier taille et performance PDF

```bash
# Taille du PDF
du -h exports/span-sg.pdf
# Attendu : < 5 MB (si > 10 MB, optimiser images)

# Temps de génération
time mkdocs build --config-file mkdocs-pdf.yml
# Attendu : < 30s
```

---

## Critères d'acceptation

- [ ] `mkdocs-pdf.yml` existe et fonctionne
- [ ] `mkdocs build --config-file mkdocs-pdf.yml` génère `exports/span-sg.pdf`
- [ ] PDF contient : page de garde, table des matières, toutes les pages
- [ ] Tableaux et checkboxes lisibles dans le PDF
- [ ] CI GitHub Actions génère PDF automatiquement
- [ ] Artefacts CI contiennent `exports/span-sg.pdf`
- [ ] Taille PDF < 5 MB
- [ ] Temps génération < 30s
- [ ] Méthode manuelle documentée

---

## Tests de validation

```bash
# Test 1 : Config PDF existe
test -f mkdocs-pdf.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : Plugin fonctionne
mkdocs build --config-file mkdocs-pdf.yml >/dev/null 2>&1 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : PDF généré et non vide
test -s exports/span-sg.pdf && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : Taille PDF raisonnable
test $(du -k exports/span-sg.pdf | cut -f1) -lt 5120 && echo "OK" || echo "WARN: PDF > 5 MB"
# Attendu : OK

# Test 5 : PDF lisible (vérifier nombre de pages)
pdfinfo exports/span-sg.pdf 2>/dev/null | grep "Pages:" && echo "OK" || echo "SKIP"
# Attendu : Pages: 15-30 (variable selon contenu)
```

---

## Dépendances

**Bloque** :
- S4-04 (publication nécessite PDF pour la release)

**Dépend de** :
- S1-03 (MkDocs configuré)
- S2-01 (CI pour tester génération automatique)

---

## Références

- **PRD v3.3** : Section 3.3 "Export PDF simplifié"
- **mkdocs-pdf.yml** : Config plugin principal
- **CLAUDE.md** : Section "Configuration MkDocs"

---

## Notes et risques

**Plugin PDF instable**
`mkdocs-pdf-export-plugin` a des limitations connues :
- CSS complexe mal rendu
- Images SVG parfois ignorées
- Emojis et caractères Unicode problématiques
- Liens externes cassés dans le PDF

Si problèmes persistants, utiliser méthode manuelle (impression navigateur).

**Performance avec gros volumes**
Actuellement ~20 pages. Si futur > 100 pages :
- Envisager PDF par module (1 PDF par service)
- Ou PDF allégé (sans images)

**Metadata PDF**
Possibilité d'ajouter metadata au PDF :
```yaml
plugins:
  - pdf-export:
      combined: true
      combined_output_path: exports/span-sg.pdf
      author: "Secrétariat Général"
      copyright: "© 2025 SG"
```

**Compression PDF**
Si taille excessive, post-traiter avec Ghostscript :
```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH \
   -sOutputFile=exports/span-sg-compressed.pdf exports/span-sg.pdf
```

---

## Post-tâche

Vérifier que la section dans README est à jour :
```markdown
## Commandes utiles
- Build manuel PDF: `mkdocs build --config-file mkdocs-pdf.yml`

## Dépannage rapide
- PDF manquant: utiliser l'impression navigateur sur « Synthèse » (Cmd+P / Ctrl+P)
```

Commiter la configuration finale :
```bash
git add mkdocs-pdf.yml
git commit -m "feat: configure export PDF automatique"
git push origin draft
```
