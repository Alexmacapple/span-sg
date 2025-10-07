# Formation Git - SPAN SG (15 slides)

Template de présentation reveal.js pour Story S3-02

---

## Slide 1 : Titre

```markdown
# Formation Git
## Contribuer au SPAN SG

Formation pratique - 2 heures

Alexandra - SPAN SG Project
Date : [JJ/MM/AAAA]
```

---

## Slide 2 : Objectifs

```markdown
## Objectifs de la formation

À la fin de cette session, vous saurez :

- Éditer votre module via GitHub web
- Créer une Pull Request vers draft
- Prévisualiser vos modifications
- Répondre aux commentaires de review

**Focus : Pratique (80% hands-on)**
```

---

## Slide 3 : Agenda

```markdown
## Agenda (2h)

1. **Concepts de base** (15 min)
   - Qu'est-ce que Git ?
   - Workflow SPAN SG

2. **Exercices pratiques** (60 min)
   - Exercice 1 : Cocher une case (15 min)
   - Exercice 2 : Ajouter action au plan (20 min)
   - Exercice 3 : Réagir à commentaire review (15 min)
   - Exercice 4 : Vérifier preview (10 min)

3. **PAUSE** (10 min)

4. **Git local (optionnel)** (30 min)

5. **Bonnes pratiques + Q&A** (15 min)
```

---

## Slide 4 : Qu'est-ce que Git ?

```markdown
## Qu'est-ce que Git ?

**Système de versioning** : Chaque modification est tracée

**Avantages** :
- Historique complet des changements
- Collaboration sans conflits
- Retour arrière possible à tout moment
- Qui a modifié quoi et quand ?

**Pour SPAN SG** :
- 6 services éditent en parallèle
- Validation avant publication (review)
- Preview avant production
```

---

## Slide 5 : Workflow SPAN SG

```markdown
## Workflow SPAN SG

```
Votre module (branche feature)
        |
        v
   Pull Request ---> draft (preview)
        |
        v (après validation)
   main (production)
```

**Branches** :
- `main` : Production (public)
- `draft` : Preview privée (relecture)
- `feature/update-[service]` : Votre travail isolé
```

---

## Slide 6 : Vocabulaire minimal

```markdown
## Vocabulaire Git

**Repository (repo)** : Le projet complet

**Branch (branche)** : Version parallèle du code

**Commit** : Une sauvegarde de modifications avec message

**Pull Request (PR)** : Demande de fusion de modifications

**Merge** : Intégration de modifications dans branche cible

**CI/CD** : Tests automatiques à chaque commit
```

---

## Slide 7 : Exercice 1 - Cocher une case

```markdown
## Exercice 1 : Cocher une case (15 min)

**Objectif** : Modifier votre module et créer votre première PR

**Étapes** :
1. Aller sur : `docs/modules/[votre-service].md`
2. Cliquer Edit (crayon)
3. Changer `- [ ]` en `- [x]` pour le point #1
4. Commit message : `feat([service]): coche point #1 stratégie`
5. Create Pull Request vers **draft**

**Validation** : PR créée, CI passe (vert)

**Démo live maintenant...**
```

---

## Slide 8 : Exercice 2 - Ajouter action

```markdown
## Exercice 2 : Ajouter action au plan (20 min)

**Objectif** : Modifier section "Plan d'actions prioritaires"

**Étapes** :
1. Éditer votre module (section 4)
2. Ajouter ligne au tableau :
   ```markdown
   | Audit accessibilité site principal | T2 2025 | [Votre nom] | 5000€ | À commencer |
   ```
3. Commit message : `feat([service]): ajoute action audit T2`
4. Push dans la MÊME branche que l'exercice 1

**Résultat** : Les 2 commits apparaissent dans la même PR

**À vous de jouer !**
```

---

## Slide 9 : Exercice 3 - Commentaire review

```markdown
## Exercice 3 : Réagir à commentaire (15 min)

**Simulation** :
Alexandra ajoute commentaire sur votre PR :
> "Préciser le budget audit (interne ou externe ?)"

**Votre tâche** :
1. Éditer à nouveau le fichier
2. Changer "5000€" en "5000€ (externe)"
3. Commit message : `fix([service]): précise budget audit`

**Résultat** : Commentaire résolu, PR prête au merge

**Démo correction maintenant...**
```

---

## Slide 10 : Exercice 4 - Vérifier preview

```markdown
## Exercice 4 : Vérifier la preview (10 min)

**Après merge de votre PR** :

1. Attendre 2-3 min (CI déploie)
2. Ouvrir : `https://[preview-url]/draft/modules/[service]/`
3. Vérifier que vos modifications apparaissent

**Vérifications** :
- Case cochée visible
- Action ajoutée dans tableau
- Budget corrigé

**Si pas visible** : Vider cache navigateur (Ctrl+Shift+R)
```

---

## Slide 11 : Git local (optionnel)

```markdown
## Git local - Pour les avancés (30 min)

**Prérequis** :
- Git installé : `git --version`
- Compte GitHub configuré

**Workflow** :
```bash
# Clone repo
git clone https://github.com/.../span-sg.git
cd span-sg

# Créer branche
git checkout draft
git checkout -b feature/update-[service]-[date]

# Éditer fichier
code docs/modules/[service].md

# Preview local
docker compose up  # http://localhost:8000/span-sg-repo/

# Commit + Push
git add docs/modules/[service].md
git commit -m "feat([service]): ajout contenu"
git push -u origin feature/update-[service]-[date]
```

**Démo si temps disponible...**
```

---

## Slide 12 : Bonnes pratiques - Dos

```markdown
## Bonnes pratiques : Dos

**Commit messages clairs** :
- feat([service]): ajoute section périmètre
- fix([service]): corrige score indicateurs
- docs([service]): met à jour déclaration accessibilité

**PR petites** :
- 1 module à la fois
- 1-3 modifications maximum
- Plus facile à reviewer

**Tester preview avant validation** :
- Toujours vérifier rendu final
- Pas de surprise en production
```

---

## Slide 13 : Bonnes pratiques - Don'ts

```markdown
## Bonnes pratiques : Don'ts

**Ne JAMAIS modifier** :
- Les 31 lignes `<!-- DINUM -->` (hors coches)
- Front-matter des autres services
- Fichiers hors de votre module

**Ne JAMAIS publier** :
- Secrets (mots de passe, tokens)
- Infos sensibles (vulnérabilités non corrigées)
- Données personnelles (emails, téléphones)

**Ne PAS commit directement** :
- Jamais sur draft ou main
- Toujours passer par PR
- Protection branche activée
```

---

## Slide 14 : Support et ressources

```markdown
## Support et ressources

**Documentation** :
- `CONTRIBUTING.md` : Guide complet contributeur
- `docs/formation/git-basics.md` : Support formation détaillé
- `roadmap/templates/module-content-examples.md` : Exemples remplissage

**Aide** :
- Questions : @bertrand, @alex, @alexandra
- Issues GitHub : https://github.com/.../issues
- Office hours Git : Jeudis 14h-15h [lien visio]

**Références externes** :
- Guide GitHub : https://guides.github.com/
- Markdown : https://www.markdownguide.org/
- RGAA : https://accessibilite.numerique.gouv.fr/
```

---

## Slide 15 : Quiz final + Fin

```markdown
## Quiz final (5 min)

**Question 1** : Quelle branche cible pour vos PR ?
→ **draft**

**Question 2** : Comment cocher un point DINUM ?
→ Changer `- [ ]` en `- [x]`

**Question 3** : Où voir la preview de vos modifications ?
→ https://[preview-url]/draft/

**Question 4** : Combien de temps pour voir changements après merge ?
→ 3-4 minutes (CI + déploiement)

---

## Formation terminée

**Questions ?**

**Prochaine étape** : Renseigner contenu de votre module (S3-03)

Merci et bon courage !
```

---

## Instructions d'utilisation

### Conversion reveal.js

Pour générer présentation HTML interactive :

```bash
# Installer reveal-md
npm install -g reveal-md

# Générer présentation
reveal-md formation-git-slides.md --theme white

# Ou export PDF
reveal-md formation-git-slides.md --print formation-git-slides.pdf
```

### Personnalisation

**Remplacer** :
- `[JJ/MM/AAAA]` : Date de la formation
- `[preview-url]` : URL preview GitHub Pages
- `[org]` : Organisation GitHub
- `[service]` : Nom du service (SNUM, SIRCOM, etc.)

### Animations recommandées

- Slide 5 (Workflow) : Animation transition branches
- Slide 7-10 (Exercices) : Screencast vidéo intégré
- Slide 12-13 (Dos/Don'ts) : Révélation progressive bullets

### Variantes

**Formation courte (1h)** : Slides 1-10 + 15 uniquement
**Formation avancée (3h)** : Ajouter slides Git local détaillées
**Formation anglaise** : Traduire textes (structure identique)

---

*Template pour Story S3-02 - Formation Git basique*
