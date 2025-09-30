---
bmad_phase: context-engineered-development
bmad_agent: dev
story_type: implementation
autonomous: true
validation: human-qa
---

# Story S4-04 : Publication production

**Phase** : Semaine 4 - Production
**Priorité** : Critique
**Estimation** : 2h
**Assigné** : Alexandra

---

## Contexte projet

La **publication production** est l'aboutissement du projet SPAN SG v1. Elle comprend :
1. Merge `draft` → `main` (bascule production)
2. Création release GitHub avec assets (PDF)
3. Activation déploiement production (GitHub Pages racine)
4. Communication interne (direction, services)
5. Célébration équipe 🎉

Cette étape est **irréversible** (enfin, réversible mais avec impact). Elle marque le passage de "preview privée" à "production officielle accessible".

Après publication :
- URL production active : https://span-sg.github.io/span-sg/
- Release v1.0.0 publiée sur GitHub
- Équipes informées
- Suivi mensuel/trimestriel activé

---

## Objectif

Merger draft vers main, créer la release GitHub, vérifier le déploiement production, et communiquer la mise en ligne officielle du SPAN SG v1.0.0.

---

## Prérequis

- [ ] Story S4-02 complétée (GO Yves)
- [ ] Story S4-03 complétée (tag v1.0.0 créé)
- [ ] Artefacts CI disponibles (site/ + PDF)
- [ ] Release notes préparées
- [ ] Aucun bug bloquant identifié

---

## Étapes d'implémentation

### 1. Vérifier l'état pré-merge

```bash
# Checkout main
git checkout main
git pull origin main

# Vérifier différences draft vs main
git log main..draft --oneline
# Attendu : Liste des commits depuis début projet

# Vérifier pas de divergence
git log draft..main --oneline
# Attendu : (vide) si main n'a pas évolué séparément
```

### 2. Créer Pull Request draft → main

**Option A : Via GitHub Web UI**
1. Aller sur https://github.com/span-sg/span-sg/compare
2. **Base** : `main`
3. **Compare** : `draft`
4. Cliquer **Create Pull Request**
5. Titre : `Release v1.0.0 - SPAN SG première publication`
6. Description :
   ```markdown
   ## Release v1.0.0

   Première publication production du SPAN SG.

   ### Contenu
   - 6 modules services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)
   - Score global : [X/186] ([Y%])
   - Documentation complète
   - CI/CD opérationnelle

   ### Validations
   - ✅ Reviews techniques : Bertrand, Alex
   - ✅ Validation sponsor : Yves
   - ✅ Tag : v1.0.0

   ### Changelog
   Voir [CHANGELOG.md](CHANGELOG.md)

   ### Décision GO
   Voir [decisions/v1.0/DECISION-GO-NO-GO-v1.0.md](decisions/v1.0/DECISION-GO-NO-GO-v1.0.md)

   ---

   **Merge policy** : Squash ou Merge commit (à définir)
   ```

**Option B : Via ligne de commande**
```bash
gh pr create \
  --base main \
  --head draft \
  --title "Release v1.0.0 - SPAN SG première publication" \
  --body-file RELEASE-NOTES-v1.0.0.md
```

### 3. Revue finale de la PR

**Checklist avant merge** :
- [ ] CI passe (vert)
- [ ] Aucun conflit
- [ ] Tag v1.0.0 présent sur draft
- [ ] CHANGELOG.md à jour
- [ ] Reviews approuvées (Bertrand + Alex)
- [ ] GO Yves documenté

**Tests manuels (optionnel)** :
- Vérifier preview draft une dernière fois
- Cliquer tous les liens modules
- Télécharger PDF et vérifier intégrité

### 4. Merger vers main

**Stratégie de merge recommandée** : **Merge commit** (pas squash)
- Préserve l'historique complet
- Facilite future cherry-pick
- Plus transparent

Sur GitHub :
1. Cliquer **Merge pull request**
2. Sélectionner **Create a merge commit**
3. Confirmer

**Ou en ligne de commande** :
```bash
git checkout main
git merge draft --no-ff -m "Merge branch 'draft' - Release v1.0.0

Première publication production SPAN SG.
Score global: [X/186] ([Y%])
Validé par: Yves, Bertrand, Alex
"
git push origin main
```

### 5. Attendre déploiement production

Le workflow `.github/workflows/build.yml` contient :
```yaml
deploy_main:
  if: github.ref == 'refs/heads/main'
  needs: build
  ...
```

Observer GitHub Actions → Run sur `main` :
- ✅ Build
- ✅ Generate PDF
- ✅ deploy_main → déploiement vers `gh-pages/` (racine)

**Temps attendu** : 2-3 minutes

### 6. Vérifier URL production

Une fois déploiement terminé :
```bash
curl -I https://span-sg.github.io/span-sg/
# Attendu : HTTP 200 OK
```

Tester navigateur :
- https://span-sg.github.io/span-sg/ → Page d'accueil
- https://span-sg.github.io/span-sg/synthese/ → Tableau de bord
- https://span-sg.github.io/span-sg/modules/sircom/ → Module SIRCOM

**Vérifications** :
- ✅ Toutes pages accessibles (pas de 404)
- ✅ Navigation fonctionne
- ✅ Synthèse à jour
- ✅ PDF téléchargeable (si lien présent)

### 7. Créer la release GitHub

Aller sur https://github.com/span-sg/span-sg/releases/new

**Configuration** :
- **Tag** : `v1.0.0` (existant)
- **Release title** : `SPAN SG v1.0.0 - Première release production`
- **Description** : Copier contenu de `RELEASE-NOTES-v1.0.0.md`
- **Assets** : Joindre `exports/span-sg.pdf` (renommer en `span-sg-v1.0.0.pdf`)
- **Pre-release** : ❌ Non coché (release stable)
- **Latest release** : ✅ Coché

Cliquer **Publish release**

**Résultat** : Release visible sur https://github.com/span-sg/span-sg/releases

### 8. Mettre à jour README avec badge release

```markdown
# SPAN SG

![Version](https://img.shields.io/github/v/release/span-sg/span-sg)
![Build Status](https://github.com/span-sg/span-sg/workflows/Build%20SPAN/badge.svg)

...
```

Commit :
```bash
git add README.md
git commit -m "docs: add release badge to README"
git push origin main
```

### 9. Communication officielle

**Email direction** :
```
📧 À : Direction SG + Directeurs services
CC : Yves (Sponsor)
Objet : 🚀 SPAN SG v1.0 - Nouvel outil de pilotage accessibilité numérique

Bonjour,

Nous avons le plaisir de vous annoncer la mise en ligne du SPAN SG (Schéma Pluriannuel d'Accessibilité Numérique du Secrétariat Général).

🔗 **URL** : https://span-sg.github.io/span-sg/

## Qu'est-ce que le SPAN SG ?

Outil de pilotage permettant de :
- Suivre l'état d'avancement de l'accessibilité numérique de nos services
- Visualiser le score global et par service (31 points DINUM)
- Identifier les actions prioritaires 2025
- Assurer la conformité réglementaire

## Périmètre v1.0

6 services suivis :
- SNUM (Service du Numérique)
- SIRCOM (Service Interministériel des Ressources et Compétences)
- SRH (Service des Ressources Humaines)
- SIEP (Service de l'Innovation et de l'Évaluation)
- SAFI (Service des Affaires Financières et Immobilières)
- BGS (Bureau de Gestion des Services)

**Score global actuel** : [X/186] ([Y%])

## Documents

- Site web : https://span-sg.github.io/span-sg/
- PDF d'archive : [Lien release GitHub]
- Documentation : Voir section "Processus" sur le site

## Maintenance

Le SPAN SG est mis à jour en continu par les services.
Rapport mensuel d'avancement prévu.

Bravo à l'équipe projet (Alexandra, Bertrand, Alex) et aux référents accessibilité des 6 services pour ce travail collaboratif !

Cordialement,
[Nom Direction]
```

**Email équipe** :
```
📧 À : Équipe SPAN (Alexandra, Bertrand, Alex, 6 référents)
CC : Yves
Objet : 🎉 SPAN SG v1.0 - C'est en ligne !

Félicitations à toute l'équipe !

Le SPAN SG v1.0 est maintenant en production :
🔗 https://span-sg.github.io/span-sg/

Un grand merci à :
- **Alexandra** : Pilotage projet
- **Bertrand & Alex** : Reviews et validation technique
- **Yves** : Sponsorship et validation stratégique
- **Référents services** : Renseignement modules et contribution continue

## Prochaines étapes

- Suivi mensuel : Évolution scores
- Revue trimestrielle : Bilan et ajustements
- v1.1 : Améliorations continues (à définir)

🎊 Bravo et merci pour votre engagement !

Alexandra
```

### 10. Clôturer le projet (administratif)

**Actions post-publication** :
- [ ] Archiver décisions et documents (`decisions/v1.0/`)
- [ ] Mettre à jour Project board (si utilisé)
- [ ] Clôturer milestone v1.0 sur GitHub
- [ ] Planifier rétrospective équipe (1h, bilan + amélioration)
- [ ] Initialiser backlog v1.1 (issues futures)

**Rétrospective (1h)** :
```markdown
# Rétrospective SPAN SG v1.0

Date : [JJ/MM]
Participants : Alexandra, Bertrand, Alex, (+ référents si dispo)

## 🎯 Objectifs v1.0
- [Liste objectifs initiaux]
- Atteints ? Oui/Non

## ✅ Ce qui a bien fonctionné
- [Point 1]
- [Point 2]
- ...

## ❌ Ce qui n'a pas bien fonctionné
- [Point 1]
- [Point 2]
- ...

## 💡 Apprentissages
- [Leçon 1]
- [Leçon 2]
- ...

## 🚀 Actions pour v1.1+
- [Action 1 : Responsable + Échéance]
- [Action 2]
- ...
```

---

## Critères d'acceptation

- [ ] PR `draft → main` créée et mergée
- [ ] CI deploy_main exécutée avec succès
- [ ] https://span-sg.github.io/span-sg/ accessible et fonctionnelle
- [ ] Release GitHub v1.0.0 publiée avec PDF joint
- [ ] README badge release ajouté
- [ ] Communication direction envoyée
- [ ] Communication équipe envoyée
- [ ] Documents archivés
- [ ] Rétrospective planifiée

---

## Tests de validation

```bash
# Test 1 : Main à jour avec draft
git checkout main && git pull
git log -1 --oneline | grep -q "Merge.*draft" && echo "OK" || echo "FAIL"

# Test 2 : Tag v1.0.0 sur main
git tag --contains HEAD | grep -q "v1.0.0" && echo "OK" || echo "FAIL"

# Test 3 : Production accessible
curl -s https://span-sg.github.io/span-sg/ | grep -q "SPAN SG" && echo "OK" || echo "FAIL"

# Test 4 : Release GitHub existe
gh release view v1.0.0 >/dev/null 2>&1 && echo "OK" || echo "FAIL"

# Test 5 : PDF attaché à la release
gh release view v1.0.0 --json assets | grep -q "span-sg.*pdf" && echo "OK" || echo "FAIL"
```

---

## Dépendances

**Bloque** : Aucune (dernière story du projet v1.0)

**Dépend de** :
- S4-01 (reviews validées)
- S4-02 (GO Yves)
- S4-03 (tag créé)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 4 Production
- **PRD v3.3** : Section 9 "Release en 5 étapes"
- **CLAUDE.md** : Section "Processus de release"

---

## Notes et risques

**Rollback si problème**
Si bug critique détecté post-publication :
1. **Hotfix immédiat** : Créer branche `hotfix/issue-X`
2. Corriger + tester
3. PR vers `main`
4. Tag `v1.0.1`
5. Re-release

Ne PAS rollback le merge (complexe et confus).

**GitHub Pages cache**
Si changements pas visibles immédiatement :
- Attendre 1-2 min (propagation CDN)
- Hard refresh navigateur (Cmd+Shift+R / Ctrl+F5)
- Vérifier branche `gh-pages` à jour

**Communication timing**
Envoyer emails **après** vérification production OK (pas avant merge).

**Accès production**
Si restriction org-only activée sur production (comme preview) :
- Vérifier que tous destinataires ont accès
- Sinon, passer en public ou créer comptes invités

**Suivi post-production**
Planifier dès maintenant :
- Rapport mensuel (évolution scores)
- Revue trimestrielle (bilan + roadmap)
- Support continu référents

**Backup**
Avant merge, créer backup local :
```bash
git archive --format=zip --output=../span-sg-v1.0-backup.zip draft
```

---

## Post-tâche

Créer tableau de suivi post-production :
```markdown
# Suivi post-production SPAN SG

| Date | Score global | Événement | Actions |
|------|--------------|-----------|---------|
| 30/09/2025 | [X%] | Publi v1.0 | - |
| 30/10/2025 | [Y%] | Rapport M+1 | Relance SAFI |
| 30/11/2025 | [Z%] | Rapport M+2 | - |
```

Initialiser backlog v1.1 :
```markdown
# Backlog v1.1

## Fonctionnalités
- [ ] Matrice priorisation étendue (volumétrie + ROI)
- [ ] Export Excel synthèse
- [ ] Graphiques évolution temporelle

## Améliorations
- [ ] Recherche full-text dans modules
- [ ] Liens inter-modules (actions partagées)
- [ ] Templates actions type (réutilisables)

## Corrections
- [ ] (Aucune pour l'instant)
```

Planifier célébration équipe :
```
🎉 Déjeuner/apéro équipe SPAN v1.0
Date : [JJ/MM]
Lieu : [Restaurant / Bureau]
Participants : Équipe + Yves (si dispo)
Budget : [X€]

Ordre du jour :
- Célébration lancement 🥳
- Rétrospective informelle
- Perspectives v1.1+
```

Mettre à jour statut projet :
```markdown
# SPAN SG - Statut Projet

**Phase** : ✅ Production (v1.0 live)
**Prochaine milestone** : v1.1 (T1 2026)

## Historique
- S1 : Setup ✅
- S2 : Automatisation ✅
- S3 : Onboarding ✅
- S4 : Production ✅

**Mission accomplie ! 🚀**
```