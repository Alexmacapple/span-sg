# Story S2-02 : Export PDF avec fallback robuste

**Phase** : Semaine 2 - Automatisation
**Priorité** : Haute
**Estimation** : 1h30
**Assigné** : Alexandra

---

## Contexte projet

L'export PDF est un **livrable critique** pour chaque release SPAN SG. Il permet :
- Archive officielle du SPAN complet
- Distribution hors-ligne (réunions, audits)
- Annexe aux releases GitHub
- Conformité documentaire

Problème connu : Les plugins PDF MkDocs sont capricieux et peuvent échouer selon :
- Versions de dépendances
- Complexité CSS/HTML
- Taille des images
- Caractères spéciaux

**Solution robuste** : Double stratégie avec fallback automatique
1. Plugin principal : `mkdocs-pdf-export-plugin` (rapide, qualité élevée)
2. Fallback : `mkdocs-with-pdf` (plus lent, plus stable)
3. Filet de sécurité : Impression navigateur sur page Synthèse

Configurations séparées :
- `mkdocs.yml` : Config principale (sans PDF)
- `mkdocs-pdf.yml` : Config plugin principal
- `mkdocs-with-pdf.yml` : Config fallback

---

## Objectif

Tester les deux plugins PDF en local et dans la CI, valider le fallback automatique, garantir qu'un PDF est toujours généré, et documenter le processus.

---

## Prérequis

- [ ] Story S1-03 complétée (MkDocs configuré)
- [ ] Story S2-01 complétée (CI GitHub Actions fonctionnelle)
- [ ] Python 3.11+ avec pip
- [ ] Docker (pour tests isolés)

---

## Étapes d'implémentation

### 1. Vérifier les configurations PDF existantes

```bash
# Config principale (pas de PDF)
grep -A 5 "plugins:" mkdocs.yml
# Attendu : search + pdf-export (commenté ou retiré pour éviter conflit)

# Config plugin principal
cat mkdocs-pdf.yml

# Config fallback
cat mkdocs-with-pdf.yml
```

### 2. Installer les plugins PDF en local

```bash
pip install mkdocs-pdf-export-plugin mkdocs-with-pdf
```

### 3. Tester le plugin principal

```bash
# Build avec config PDF principale
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

### 4. Tester le plugin fallback

```bash
# Build avec config fallback
mkdocs build --config-file mkdocs-with-pdf.yml

# Vérifier génération
ls -lh exports/span-sg.pdf
# Attendu : Fichier PDF (possiblement plus lourd que principal)

# Comparer qualité
open exports/span-sg.pdf
```

Différences possibles :
- `mkdocs-pdf-export-plugin` : Plus rapide, CSS mieux rendu
- `mkdocs-with-pdf` : Plus lent, mise en page parfois différente

### 5. Simuler échec du plugin principal

Modifier `mkdocs-pdf.yml` pour forcer une erreur :
```yaml
plugins:
  - pdf-export:
      combined: true
      combined_output_path: /chemin/invalide/span-sg.pdf  # Chemin inaccessible
```

Tester :
```bash
mkdocs build --config-file mkdocs-pdf.yml
echo $?
# Attendu : exit code != 0
```

Restaurer la config correcte.

### 6. Tester le fallback automatique dans CI

Le workflow `.github/workflows/build.yml` contient :
```yaml
- name: Generate PDF (plugin principal)
  run: mkdocs build --config-file mkdocs-pdf.yml
  continue-on-error: true

- name: Generate PDF fallback (mkdocs-with-pdf si échec)
  if: failure()
  run: mkdocs build --config-file mkdocs-with-pdf.yml
```

Pour tester, forcer échec du principal :
```bash
git checkout draft

# Commenter plugin principal dans mkdocs-pdf.yml
sed -i '' 's/pdf-export:/#pdf-export:/' mkdocs-pdf.yml

git add mkdocs-pdf.yml
git commit -m "test: force PDF fallback"
git push origin draft
```

Observer CI :
- ⚠️ Step "Generate PDF (plugin principal)" échoue (continue-on-error)
- ✅ Step "Generate PDF fallback" s'exécute et réussit

Vérifier artefact contient bien `exports/span-sg.pdf`.

Puis restaurer :
```bash
git revert HEAD
git push origin draft
```

### 7. Optimiser les configurations PDF

**mkdocs-pdf.yml** (plugin principal) :
```yaml
site_name: SPAN SG
site_url: https://alexmacapple.github.io/span-sg-repo/
theme:
  name: material
  language: fr
plugins:
  - pdf-export:
      combined: true
      combined_output_path: exports/span-sg.pdf
      media_type: print
      enabled_if_env: ENABLE_PDF_EXPORT
nav:
  # Copier la nav de mkdocs.yml
```

**mkdocs-with-pdf.yml** (fallback) :
```yaml
site_name: SPAN SG
theme:
  name: material
plugins:
  - with-pdf:
      output_path: exports/span-sg.pdf
      cover_title: "SPAN SG"
      cover_subtitle: "Schéma Pluriannuel d'Accessibilité Numérique"
      toc_level: 2
      enabled_if_env: ENABLE_PDF_EXPORT
```

### 8. Tester en local avec variables d'environnement

```bash
# Activer génération PDF
export ENABLE_PDF_EXPORT=1

mkdocs build --config-file mkdocs-pdf.yml
ls exports/span-sg.pdf

# Désactiver
unset ENABLE_PDF_EXPORT

mkdocs build --config-file mkdocs-pdf.yml
# Attendu : Pas de PDF généré (plugin désactivé)
```

### 9. Documenter le filet de sécurité manuel

Si les deux plugins échouent, méthode manuelle :

```bash
# Démarrer serveur local
docker compose up

# Ouvrir navigateur
open http://localhost:8000/synthese/

# Imprimer en PDF (Cmd+P / Ctrl+P)
# Destination : Enregistrer au format PDF
# Nom fichier : span-sg-synthese.pdf
```

Documenter dans README.md :
```markdown
## Génération PDF manuelle

Si les plugins échouent :
1. `docker compose up`
2. Ouvrir http://localhost:8000/synthese/
3. Imprimer en PDF (raccourci d'impression navigateur)
```

### 10. Vérifier taille et performance PDF

```bash
# Taille du PDF
du -h exports/span-sg.pdf
# Attendu : < 5 MB (si > 10 MB, optimiser images)

# Temps de génération plugin principal
time mkdocs build --config-file mkdocs-pdf.yml
# Attendu : < 30s

# Temps de génération fallback
time mkdocs build --config-file mkdocs-with-pdf.yml
# Attendu : < 60s
```

---

## Critères d'acceptation

- [ ] `mkdocs-pdf.yml` et `mkdocs-with-pdf.yml` existent
- [ ] `mkdocs build --config-file mkdocs-pdf.yml` génère `exports/span-sg.pdf`
- [ ] `mkdocs build --config-file mkdocs-with-pdf.yml` génère `exports/span-sg.pdf` (fallback)
- [ ] PDF contient : page de garde, table des matières, toutes les pages
- [ ] Tableaux et checkboxes lisibles dans le PDF
- [ ] CI GitHub Actions génère PDF (principal ou fallback)
- [ ] Artefacts CI contiennent `exports/span-sg.pdf`
- [ ] Taille PDF < 5 MB
- [ ] Temps génération < 60s (fallback)

---

## Tests de validation

```bash
# Test 1 : Configs PDF existent
test -f mkdocs-pdf.yml && test -f mkdocs-with-pdf.yml && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : Plugin principal fonctionne
mkdocs build --config-file mkdocs-pdf.yml >/dev/null 2>&1 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 3 : Fallback fonctionne
mkdocs build --config-file mkdocs-with-pdf.yml >/dev/null 2>&1 && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 4 : PDF généré et non vide
test -s exports/span-sg.pdf && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 5 : Taille PDF raisonnable
test $(du -k exports/span-sg.pdf | cut -f1) -lt 5120 && echo "OK" || echo "WARN: PDF > 5 MB"
# Attendu : OK

# Test 6 : PDF lisible (vérifier nombre de pages)
pdfinfo exports/span-sg.pdf 2>/dev/null | grep "Pages:" && echo "OK" || echo "SKIP"
# Attendu : Pages: 15-30 (variable selon contenu)
```

---

## Dépendances

**Bloque** :
- S4-04 (publication nécessite PDF pour la release)

**Dépend de** :
- S1-03 (MkDocs configuré)
- S2-01 (CI pour tester fallback automatique)

---

## Références

- **PRD v3.3** : Section 3.3 "Export PDF avec fallback robuste"
- **mkdocs-pdf.yml** : Config plugin principal
- **mkdocs-with-pdf.yml** : Config fallback
- **CLAUDE.md** : Section "Configuration MkDocs triple"

---

## Notes et risques

**Plugins PDF instables**
Les deux plugins ont des limitations connues :
- CSS complexe mal rendu
- Images SVG parfois ignorées
- Emojis et caractères Unicode problématiques
- Liens externes cassés dans le PDF

Si problèmes persistants, envisager alternatives :
- `weasyprint` (plus robuste mais dépendances lourdes)
- Pandoc (conversion Markdown → PDF via LaTeX)
- Service externe (DocRaptor, Prince XML)

**Performance avec gros volumes**
Actuellement ~20 pages. Si futur > 100 pages :
- Envisager PDF par module (1 PDF par service)
- Ou PDF allégé (sans images)

**Watermark et metadata**
Ajouter metadata au PDF :
```yaml
plugins:
  - with-pdf:
      output_path: exports/span-sg.pdf
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

Ajouter section dans README :
```markdown
## Export PDF

Deux méthodes disponibles :

**Automatique (CI)** :
Chaque build génère `exports/span-sg.pdf` (disponible dans Artifacts).

**Manuel (local)** :
```bash
mkdocs build --config-file mkdocs-pdf.yml
```

En cas d'échec, utiliser fallback :
```bash
mkdocs build --config-file mkdocs-with-pdf.yml
```
```

Commiter les configurations finales :
```bash
git add mkdocs-pdf.yml mkdocs-with-pdf.yml
git commit -m "feat: configure export PDF avec fallback robuste"
git push origin draft
```