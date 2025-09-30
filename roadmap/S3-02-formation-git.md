# Story S3-02 : Formation Git basique (2h)

**Phase** : Semaine 3 - Onboarding
**Priorité** : Haute
**Estimation** : 2h (préparation) + 2h (session)
**Assigné** : Alexandra

---

## Contexte projet

Les 6 référents accessibilité des services ont des niveaux techniques variables :
- Certains connaissent Git/GitHub
- D'autres n'ont jamais utilisé de versioning
- Tous doivent être autonomes pour modifier leur module

Objectif de la formation :
- **Pas** devenir experts Git (hors scope)
- **Oui** pouvoir éditer leur module et créer des PR
- Comprendre le workflow draft → main
- Savoir où demander de l'aide

Format : **2 heures max**, hybride (visio + async), focus pratique (80% hands-on).

---

## Objectif

Concevoir et délivrer une formation Git basique de 2h permettant aux référents services de contribuer au SPAN SG de manière autonome.

---

## Prérequis

- [ ] Story S2-04 complétée (CONTRIBUTING.md disponible)
- [ ] Story S3-01 complétée (6 modules créés)
- [ ] Liste des 6 référents accessibilité avec emails
- [ ] Outil visio accessible (Teams, Zoom, Meet)

---

## Étapes d'implémentation

### 1. Préparer le support de formation

Créer `docs/formation/git-basics.md` :
```markdown
# Formation Git - SPAN SG

## Objectifs (5 min)

À la fin de cette session, vous saurez :
✅ Éditer votre module via GitHub web
✅ Créer une Pull Request vers draft
✅ Prévisualiser vos modifications
✅ Répondre aux commentaires de review

---

## Partie 1 : Concepts de base (15 min)

### Qu'est-ce que Git ?
Système de versioning : chaque modification est tracée, réversible.

### Workflow SPAN SG
```
Votre module (branche feature)
        ↓
   Pull Request → draft (preview)
        ↓
   Validation → main (production)
```

### Vocabulaire minimal
- **Repository (repo)** : Le projet complet
- **Branch (branche)** : Version parallèle
- **Commit** : Une sauvegarde de modifications
- **Pull Request (PR)** : Demande de fusion de modifications

---

## Partie 2 : Exercice pratique Option A (60 min)

### Exercice 1 : Cocher une case (15 min)

1. Aller sur votre module : https://github.com/.../docs/modules/[votre-service].md
2. Cliquer ✏️ Edit
3. Changer `- [ ]` en `- [x]` pour le point #1
4. Commit message : `feat([service]): coche point #1 stratégie`
5. Create Pull Request vers **draft**

**Validation** : PR créée, CI passe (vert)

### Exercice 2 : Ajouter une action au plan (20 min)

1. Éditer votre module (section "Plan d'actions prioritaires")
2. Ajouter une ligne au tableau :
   ```markdown
   | Audit accessibilité site principal | T2 2025 | [Votre nom] | 5000€ | À commencer |
   ```
3. Commit message : `feat([service]): ajoute action audit T2`
4. Push dans la même branche que l'exercice 1

**Validation** : Les 2 commits apparaissent dans la même PR

### Exercice 3 : Réagir à un commentaire de review (15 min)

1. Alexandra ajoute un commentaire sur votre PR : "Préciser le budget audit"
2. Vous éditez à nouveau le fichier
3. Changer "5000€" en "5000€ (externe)"
4. Commit message : `fix([service]): précise budget audit`

**Validation** : Commentaire résolu, PR mergée

### Exercice 4 : Vérifier la preview (10 min)

1. Après merge, attendre 2-3 min (CI)
2. Ouvrir https://[preview-url]/draft/modules/[service]/
3. Vérifier que vos modifications apparaissent

---

## Partie 3 : Option B (Git local) - Optionnel (30 min)

### Prérequis
- Git installé : `git --version`
- Compte GitHub configuré

### Exercice 5 : Clone et branche (10 min)

```bash
git clone https://github.com/.../span-sg.git
cd span-sg
git checkout draft
git checkout -b feature/update-[service]-[date]
```

### Exercice 6 : Édition locale (10 min)

```bash
# Éditer avec votre éditeur préféré
code docs/modules/[service].md

# Prévisualiser
docker compose up
# → http://localhost:8000
```

### Exercice 7 : Push et PR (10 min)

```bash
git add docs/modules/[service].md
git commit -m "feat([service]): ajout contenu section 1"
git push -u origin feature/update-[service]-[date]
# Cliquer le lien affiché pour créer PR
```

---

## Partie 4 : Bonnes pratiques (10 min)

### Dos
✅ Commit messages clairs (`feat`, `fix`, `docs`)
✅ PR petites (1 module, 1-3 modifications max)
✅ Tester la preview avant de valider

### Don'ts
❌ Jamais modifier les 31 lignes `<!-- DINUM -->` (hors coches)
❌ Pas de secrets/infos sensibles
❌ Pas de commit directement sur draft/main

---

## Partie 5 : Support et ressources (5 min)

### Aide
- Doc : `CONTRIBUTING.md`
- Questions : @bertrand, @alex, @alexandra
- Issues : https://github.com/.../issues

### Références
- Guide GitHub : https://guides.github.com/
- Markdown : https://www.markdownguide.org/

---

## Quiz final (5 min)

1. Quelle branche cible pour vos PR ? → **draft**
2. Comment cocher un point DINUM ? → Changer `[ ]` en `[x]`
3. Où voir la preview ? → https://[preview-url]/draft/

*Formation terminée. Questions ?*
```

### 2. Préparer l'environnement de formation

**Créer un repo de test (optionnel)** :
```bash
# Dupliquer le repo pour éviter pollution du vrai
# Les participants s'entraînent sur span-sg-training
```

**Préparer les accès** :
- Inviter les 6 référents au repo (ou org)
- Leur envoyer le lien CONTRIBUTING.md avant la session
- Vérifier qu'ils ont tous un compte GitHub

### 3. Planifier la session

**Format recommandé** :
- Date/heure : [À définir, coord avec les 6 services]
- Durée : 2h max (pause 10 min à mi-parcours)
- Outils : Visio + partage d'écran
- Enregistrement : Oui (pour replay)

**Agenda détaillé** :
```
09h00-09h15 : Accueil + tour de table (niveaux Git)
09h15-09h30 : Partie 1 (concepts)
09h30-10h30 : Partie 2 (exercices pratiques Option A)
10h30-10h40 : Pause
10h40-11h10 : Partie 3 (Option B, optionnelle selon groupe)
11h10-11h25 : Partie 4 (bonnes pratiques)
11h25-11h30 : Partie 5 (ressources + quiz)
```

### 4. Créer des supports visuels

**Slides (optionnel mais recommandé)** :
- 10-15 slides max
- Schéma workflow (draft → main)
- Captures d'écran interface GitHub
- Checklist "Créer une PR en 5 étapes"

**Screencast vidéo (optionnel)** :
- Enregistrer un exemple complet (3-5 min)
- "Cocher une case et créer une PR"
- Publier sur drive interne ou YouTube (unlisted)

### 5. Envoyer l'invitation

```
📧 À : Référents SNUM, SIRCOM, SRH, SIEP, SAFI, BGS
CC : Bertrand, Alex
Objet : Formation Git SPAN SG - [Date]

Bonjour,

Formation Git pour contribuer au SPAN SG :
- **Date** : [JJ/MM/AAAA], 09h00-11h00
- **Lien visio** : [URL]
- **Prérequis** :
  - Compte GitHub (créer sur https://github.com/signup si besoin)
  - Lecture préalable : [lien CONTRIBUTING.md]

Objectif : Vous rendre autonome pour éditer votre module.

Format : 80% pratique, apportez votre laptop.

À bientôt,
Alexandra
```

### 6. Dérouler la session

**Tips animation** :
- Partager écran + narration
- Faire pause après chaque exercice : "Des questions ?"
- Encourager mise en pratique immédiate (hands-on)
- Utiliser le chat visio pour questions async
- Bertrand/Alex en support pour débogage individuel

**Adaptation tempo** :
- Si groupe débutant : focus Option A uniquement
- Si groupe avancé : accélérer partie 1, plus de temps partie 3

### 7. Collecter le feedback

Questionnaire post-formation (Google Form, TypeForm) :
```markdown
## Feedback Formation Git

1. Niveau de départ : Débutant / Intermédiaire / Avancé
2. Clarté explications : 1-5 ⭐
3. Utilité exercices pratiques : 1-5 ⭐
4. Durée formation : Trop courte / OK / Trop longue
5. Vous sentez-vous capable de créer une PR seul·e ? Oui / Non / Avec aide
6. Suggestions d'amélioration : [texte libre]
```

### 8. Créer les ressources persistantes

**Cheatsheet** :
```markdown
# Cheatsheet Git - SPAN SG

## Créer une PR (Option A)
1. Éditer fichier sur GitHub
2. Commit changes → Create new branch
3. Create Pull Request vers **draft**

## Commandes Git (Option B)
```bash
git checkout draft && git pull        # MAJ draft
git checkout -b feature/mon-update    # Créer branche
# ... éditer fichiers ...
git add docs/modules/[service].md
git commit -m "feat: description"
git push -u origin feature/mon-update
```

## Urgence
- Bug/problème : Créer issue GitHub
- Contact : @alexandra, @bertrand, @alex
```

### 9. Suivi post-formation

**J+1** : Email récap
```
Merci d'avoir participé à la formation Git SPAN !

Récap :
- Support : [lien docs/formation/git-basics.md]
- Replay vidéo : [lien]
- Cheatsheet : [lien]

Prochaine étape : Renseigner le contenu de votre module (S3-03).
Date limite première version : [JJ/MM]

Questions ? Répondez à ce mail.
```

**J+7** : Check-in individuel
- Contacter chaque référent
- "As-tu pu créer ta première PR ?"
- Offrir session 1-to-1 si besoin (30 min)

---

## Critères d'acceptation

- [ ] Support `docs/formation/git-basics.md` créé
- [ ] Session 2h planifiée avec les 6 référents
- [ ] Invitation envoyée avec prérequis
- [ ] Exercices pratiques préparés (PRs tests)
- [ ] Session délivrée avec minimum 80% présence
- [ ] Enregistrement disponible pour replay
- [ ] Feedback collecté (≥4/5 satisfaction moyenne)
- [ ] 100% participants capables de créer une PR (avec ou sans aide)

---

## Tests de validation

```bash
# Test 1 : Support formation existe
test -f docs/formation/git-basics.md && echo "OK" || echo "FAIL"
# Attendu : OK

# Test 2 : 6 référents ont accès au repo
# Vérifier manuellement sur GitHub → Settings → Collaborators

# Test 3 : Tous ont créé au moins 1 PR (post-formation)
# Vérifier : https://github.com/.../pulls?q=is:pr+author:[referent]

# Test 4 : Enregistrement vidéo disponible
test -f videos/formation-git-2025-09-30.mp4 && echo "OK" || echo "SKIP"
```

---

## Dépendances

**Bloque** :
- S3-03 (premiers contenus dépendent de l'autonomie des référents)

**Dépend de** :
- S2-04 (CONTRIBUTING.md comme support)
- S3-01 (modules créés pour exercices)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 3 Onboarding
- **PRD v3.3** : Section 7 "Guide contributeur" → Formation Git
- **CONTRIBUTING.md** : Support principal
- **docs/formation/git-basics.md** : Support formation à créer

---

## Notes et risques

**Barrière psychologique Git**
Même avec formation, certains auront peur de "casser" quelque chose. Rassurer :
- Impossible de casser main (protection branche)
- Toutes les modifs réversibles
- Support disponible 24/7

**Hétérogénéité niveaux**
Si écart trop grand, envisager 2 sessions :
- Session débutants (Option A uniquement)
- Session avancés (Option B, workflow complet)

**Absents**
Pour ceux qui ratent la session :
- Replay vidéo obligatoire
- Session 1-to-1 de 30 min offerte
- Buddy system (binôme avec collègue formé)

**Maintenance formation**
Mettre à jour le support si :
- Interface GitHub change
- Workflow SPAN SG évolue
- Feedback identifie points confus

**Langue**
Formation en français (contrainte projet). Si futurs contributeurs anglophones, préparer version anglaise.

---

## Post-tâche

Créer calendrier récurrent "Office hours Git" :
```
Tous les jeudis 14h-15h : Questions Git SPAN
Lien visio permanent : [URL]
Pas d'agenda, venez avec vos questions
```

Documenter dans README :
```markdown
## Formation et support

Formation Git initiale : Voir `docs/formation/git-basics.md`
Replay vidéo : [lien]
Office hours : Jeudis 14h-15h [lien visio]
```

Célébrer les premières PR :
```
📧 À : Équipe SPAN
Objet : 🎉 Première PR de [Service] !

Félicitations à [Nom] (service [X]) pour sa première Pull Request !

[Lien vers la PR]

Continuons l'élan 🚀
```