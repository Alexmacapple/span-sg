# Guide Labels GitHub SPAN SG

Ce document explique l'organisation des labels GitHub et leur usage recommande.

## Configuration initiale

Pour configurer tous les labels du projet :

```bash
./.github/scripts/setup_labels.sh
```

Prerequis : `gh` CLI installe et authentifie avec permissions `write:issues`.

---

## Taxonomie labels

### 1. Labels Modules (6 labels)

Identifient le service/module concerne par l'issue ou la PR.

| Label | Description | Couleur |
|-------|-------------|---------|
| `module:snum` | Service SNUM | Vert fonce `#0e8a16` |
| `module:sircom` | Service SIRCOM | Vert fonce `#0e8a16` |
| `module:srh` | Service SRH | Vert fonce `#0e8a16` |
| `module:siep` | Service SIEP | Vert fonce `#0e8a16` |
| `module:safi` | Service SAFI | Vert fonce `#0e8a16` |
| `module:bgs` | Service BGS | Vert fonce `#0e8a16` |

**Usage :**
- Issues de type `[Module]` (mise a jour contenu module)
- PRs modifiant `docs/modules/[service].md`

**Exemples :**
```
module:snum + status:in-progress + priority:high
module:sircom + bug + area:scoring
```

---

### 2. Labels Status (4 labels)

Indiquent l'etat d'avancement d'une issue ou PR.

| Label | Description | Couleur | Quand l'utiliser |
|-------|-------------|---------|------------------|
| `status:triage` | En attente de triage | Jaune `#fbca04` | Issue nouvellement creee (auto-applique) |
| `status:in-progress` | En cours de traitement | Violet clair `#d4c5f9` | Quelqu'un travaille activement dessus |
| `status:blocked` | Bloque par une dependance | Rouge `#d93f0b` | Bloque par issue externe ou decision |
| `status:review-needed` | En attente de review | Bleu `#0052cc` | PR prete, attend validation |

**Workflow type :**
```
status:triage → status:in-progress → status:review-needed → [merged/closed]
                        ↓
                  status:blocked (si necessaire)
```

---

### 3. Labels Priority (4 labels)

Niveau d'urgence ou d'importance.

| Label | Description | Couleur | SLA indicatif |
|-------|-------------|---------|---------------|
| `priority:low` | Priorite basse | Vert clair `#c2e0c6` | > 4 semaines |
| `priority:medium` | Priorite moyenne | Jaune `#fbca04` | 1-4 semaines |
| `priority:high` | Priorite haute | Orange `#d93f0b` | < 1 semaine |
| `priority:critical` | Priorite critique | Rouge fonce `#b60205` | < 24h (bloquant CI/deploy) |

**Usage recommande :**
- `critical` : CI cassee, deploiement bloque, bug securite
- `high` : Fonctionnalite bloquante pour une release
- `medium` : Amelioration planifiee
- `low` : Nice-to-have, backlog

---

### 4. Labels Area (5 labels)

Domaine technique concerne.

| Label | Description | Couleur |
|-------|-------------|---------|
| `area:ci-cd` | CI/CD pipeline et GitHub Actions | Violet `#5319e7` |
| `area:testing` | Tests unitaires, E2E, accessibilite | Bleu fonce `#1d76db` |
| `area:accessibility` | Accessibilite RGAA, DSFR | Bleu `#0075ca` |
| `area:pdf` | Generation PDF et metadonnees | Violet clair `#7057ff` |
| `area:scoring` | Calcul scores et synthese | Cyan fonce `#006b75` |

**Usage :**
- Aide au filtrage technique (ex: reviewer specialise accessibilite)
- Statistiques par domaine (nombre issues CI/CD resolues)

**Exemples :**
```
area:ci-cd + bug + priority:critical → "CI cassee, urgent"
area:pdf + enhancement → "Amelioration export PDF"
```

---

### 5. Labels Type (GitHub defaults)

Labels par defaut GitHub, conserves.

| Label | Description |
|-------|-------------|
| `bug` | Quelque chose ne fonctionne pas |
| `documentation` | Amelioration ou ajout de documentation |
| `enhancement` | Nouvelle fonctionnalite ou amelioration |
| `duplicate` | Issue ou PR deja existante |
| `wontfix` | Ne sera pas traite |
| `question` | Demande d'information |
| `good first issue` | Bon pour debuter |
| `help wanted` | Necessite attention externe |

---

## Combinaisons recommandees

### Issues modules

```bash
# Mise a jour module SNUM, haute priorite, en cours
module:snum + enhancement + priority:high + status:in-progress

# Bug scoring module SIRCOM, priorite critique
module:sircom + bug + area:scoring + priority:critical
```

### Issues infrastructure

```bash
# Bug CI bloquant (critical)
bug + area:ci-cd + priority:critical + status:triage

# Amelioration tests E2E
enhancement + area:testing + priority:medium + status:in-progress
```

### Issues documentation

```bash
# Doc manquante (triage)
documentation + priority:low + status:triage

# Correction ADR urgent
documentation + priority:high + status:review-needed
```

---

## Bonnes pratiques

### 1. Appliquer labels systematiquement

Chaque issue/PR doit avoir :
- **1 label type** (`bug`, `enhancement`, `documentation`)
- **1 label priority** (`low`, `medium`, `high`, `critical`)
- **1 label status** (`triage`, `in-progress`, `blocked`, `review-needed`)
- **0-1 label module** (si concerne un module specifique)
- **0-2 labels area** (si concerne domaine technique specifique)

### 2. Mettre a jour le status

```bash
# Issue creee → auto: status:triage
# Debut travail → changer en status:in-progress
# Bloque → ajouter status:blocked + commentaire expliquant pourquoi
# PR prete → status:review-needed
# Mergee → supprimer tous status
```

### 3. Ajuster priority au besoin

```bash
# Bug mineur decouvert → priority:low
# Devient bloquant pour release → passer priority:high
# Bloque CI production → passer priority:critical
```

### 4. Utiliser filtres GitHub

```bash
# Toutes issues SNUM en cours
is:issue is:open label:module:snum label:status:in-progress

# Bugs critiques CI/CD
is:issue is:open label:bug label:area:ci-cd label:priority:critical

# PRs en attente review
is:pr is:open label:status:review-needed

# Issues haute priorite non assignees
is:issue is:open label:priority:high no:assignee
```

---

## Maintenance labels

### Ajouter un label

```bash
gh label create "area:new-domain" \
  --repo Alexmacapple/span-sg \
  --color "5319e7" \
  --description "Description du nouveau domaine"
```

### Modifier un label

```bash
gh label edit "area:ci-cd" \
  --repo Alexmacapple/span-sg \
  --color "6a1b9a" \
  --description "Nouvelle description"
```

### Lister labels

```bash
gh label list --repo Alexmacapple/span-sg --limit 100
```

---

## Statistiques labels

### Issues par module

```bash
gh issue list --repo Alexmacapple/span-sg --label "module:snum" --limit 100
```

### Issues critiques

```bash
gh issue list --repo Alexmacapple/span-sg --label "priority:critical" --state all
```

### PRs en review

```bash
gh pr list --repo Alexmacapple/span-sg --label "status:review-needed"
```

---

## References

- [GitHub Labels Documentation](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
- [GitHub CLI Labels Reference](https://cli.github.com/manual/gh_label)
- Script configuration : `.github/scripts/setup_labels.sh`
- Issue templates : `.github/ISSUE_TEMPLATE/`
