# Règles de calcul FALC vs Langage Clair

## Source

- **URL**: https://com-access.fr/falc-ou-lc/
- **Organisme**: Com'access
- **Date d'analyse**: 2025-11-06
- **Fichier JavaScript extrait**: `falc-lc-calculator.js`

## Description générale

Cet outil de décision aide à déterminer si un document doit être rédigé en **FALC** (Facile à Lire et à Comprendre) ou en **Langage Clair** en fonction de 10 questions sur le public cible et les caractéristiques du document.

## Principe de fonctionnement

### Logique d'escalade

Le système fonctionne avec une **logique d'escalade irréversible** :

- Par défaut, la recommandation est **Langage Clair**
- Certaines réponses déclenchent une **recommandation FALC**
- **Une fois le FALC recommandé, la recommandation ne change plus**
- Les questions restantes continuent à être posées pour collecter des informations

### Trois types de recommandations

1. **"Nous vous conseillons de rédiger votre document en Langage Clair."**
   - Recommandation par défaut

2. **"Nous vous conseillons de rédiger votre document en Langage Clair, mais il faudra peut-être envisager le FALC."**
   - Avertissement : LC recommandé mais FALC à considérer

3. **"Nous vous conseillons de rédiger votre document en FALC."**
   - Recommandation finale FALC (irréversible)

## Questions et règles

### Question 1 : Type d'organisme

**Question** : "Votre organisme est :"

**Options** :
- Un service public
- Un établissement médico-social
- Une entreprise
- Une association
- Autre

**Impact sur la recommandation** : ❌ AUCUN (collecte d'information uniquement)

---

### Question 2 : Public âgé

**Question** : "Votre public est-il âgé de 70 ans ou plus ?"

**Options** :
- Oui, en majorité
- Non, ce n'est pas la majorité
- Je ne sais pas

**Impact sur la recommandation** : ⚠️ AVERTISSEMENT

| Réponse | Recommandation |
|---------|----------------|
| **"Oui, en majorité"** | ⚠️ **LC avec avertissement FALC** |
| Autres réponses | Pas de changement (reste LC) |

**Code** :
```javascript
if (reponse === "Oui, en majorité") {
  resultat.textContent = "Nous vous conseillons de rédiger votre document en Langage Clair, mais il faudra peut-être envisager le FALC.";
}
```

---

### Question 3 : Niveau scolaire

**Question** : "Votre public a-t-il un niveau scolaire de collège, égal ou inférieur à la 4ème ?"

**Options** :
- Oui, en majorité
- Non, ce n'est pas la majorité
- Je ne sais pas

**Impact sur la recommandation** : ✅ DÉCISION FINALE FALC

| Réponse | Recommandation |
|---------|----------------|
| **"Oui, en majorité"** | ✅ **FALC (décision finale)** |
| Autres réponses | Pas de changement |

**Code** :
```javascript
if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
  if (reponse === "Oui, en majorité") {
    resultat.textContent = "Nous vous conseillons de rédiger votre document en FALC.";
  }
}
```

**Note** : Cette question ne modifie la recommandation que si FALC n'a pas déjà été recommandé.

---

### Question 4 : Maîtrise du français

**Question** : "Votre public maîtrise-t-il la langue française ?"

**Options** :
- Oui, en majorité
- Non, ce n'est pas la majorité
- Je ne sais pas

**Impact sur la recommandation** : ⚠️ AVERTISSEMENT

| Réponse | Recommandation |
|---------|----------------|
| **"Non, ce n'est pas la majorité"** | ⚠️ **LC avec avertissement FALC** |
| Autres réponses | Pas de changement |

**Code** :
```javascript
if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
  if (reponse === "Non, ce n'est pas la majorité") {
    resultat.textContent = "Nous vous conseillons de rédiger votre document en Langage Clair, mais il faudra peut-être envisager le FALC.";
  }
}
```

**Note** : Ne s'applique que si FALC n'a pas déjà été recommandé.

---

### Question 5 : Handicap

**Question** : "Votre public est-il en situation de handicap mental, psychique ou cognitif ?"

**Options** :
- Oui, en majorité
- Non, ce n'est pas la majorité
- Je ne sais pas

**Impact sur la recommandation** : ✅ DÉCISION FINALE FALC

| Réponse | Recommandation |
|---------|----------------|
| **"Oui, en majorité"** | ✅ **FALC (décision finale)** |
| Autres réponses | Pas de changement |

**Code** :
```javascript
if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
  if (reponse === "Oui, en majorité") {
    resultat.textContent = "Nous vous conseillons de rédiger votre document en FALC.";
  }
}
```

**Note** : Cette question ne modifie la recommandation que si FALC n'a pas déjà été recommandé.

---

### Question 6 : Autonomie de lecture

**Question** : "Vos lecteurs sont-ils autonomes pour lire ?"

**Options** :
- Oui, en majorité
- Non, ce n'est pas la majorité
- Je ne sais pas

**Impact sur la recommandation** : ✅ DÉCISION FINALE FALC

| Réponse | Recommandation |
|---------|----------------|
| **"Non, ce n'est pas la majorité"** | ✅ **FALC (décision finale)** |
| Autres réponses | Pas de changement |

**Code** :
```javascript
if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
  if (reponse === "Non, ce n'est pas la majorité") {
    resultat.textContent = "Nous vous conseillons de rédiger votre document en FALC.";
  }
}
```

**Note** : Cette question ne modifie la recommandation que si FALC n'a pas déjà été recommandé.

---

### Question 7 : Connaissance du sujet

**Question** : "Vos lecteurs connaissent-ils déjà le sujet ?"

**Options** :
- Oui, en majorité
- Non, ce n'est pas la majorité
- Je ne sais pas

**Impact sur la recommandation** : ❌ AUCUN (collecte d'information uniquement)

---

### Question 8 : Taille du document

**Question** : "Selon vous quelle sera la taille de votre document final ?"

**Options** :
- Moins de 32 pages
- Plus de 32 pages
- Je ne sais pas

**Impact sur la recommandation** : ❌ AUCUN (collecte d'information uniquement)

---

### Question 9 : Mode de publication

**Question** : "Comment souhaitez-vous publier votre document ?"

**Options** (choix multiples) :
- Web
- Papier
- Mail
- Réseaux sociaux
- Écran vidéo
- Autre

**Impact sur la recommandation** : ❌ AUCUN (collecte d'information uniquement)

---

### Question 10 : Format/Mise en page

**Question** : "Comment souhaitez-vous mettre en page votre document ?"

**Options** :
- Simple (format : Word, Powerpoint, …)
- Graphique (InDesign, Canva, …)
- Je ne sais pas

**Impact sur la recommandation** : ❌ AUCUN (collecte d'information uniquement)

---

## Résumé des règles de décision

### Questions qui déclenchent une recommandation FALC définitive :

| Question | Condition | Recommandation |
|----------|-----------|----------------|
| **Q3 - Niveau scolaire** | "Oui, en majorité" (≤ 4ème) | ✅ FALC |
| **Q5 - Handicap** | "Oui, en majorité" | ✅ FALC |
| **Q6 - Autonomie** | "Non, ce n'est pas la majorité" | ✅ FALC |

### Questions qui déclenchent un avertissement FALC :

| Question | Condition | Recommandation |
|----------|-----------|----------------|
| **Q2 - Public âgé** | "Oui, en majorité" (≥ 70 ans) | ⚠️ LC + avertissement FALC |
| **Q4 - Français** | "Non, ce n'est pas la majorité" | ⚠️ LC + avertissement FALC |

### Questions sans impact sur la recommandation :

- Q1 - Type d'organisme
- Q7 - Connaissance du sujet
- Q8 - Taille du document
- Q9 - Mode de publication
- Q10 - Format/Mise en page

## Organigramme de décision

```
┌─────────────────┐
│   Q1: Organisme │ (collecte info)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Q2: Âge ≥70   │
└────────┬────────┘
         │
         ├─→ "Oui" ──→ LC + avertissement FALC
         └─→ Autre ──→ Continue (LC)
         │
         ▼
┌─────────────────┐
│  Q3: Niveau ≤4e │
└────────┬────────┘
         │
         ├─→ "Oui" ──→ ✅ FALC (final)
         └─→ Autre ──→ Continue
         │
         ▼
┌─────────────────┐
│  Q4: Français   │
└────────┬────────┘
         │
         ├─→ "Non majorité" ──→ LC + avertissement FALC (si pas déjà FALC)
         └─→ Autre ──→ Continue
         │
         ▼
┌─────────────────┐
│  Q5: Handicap   │
└────────┬────────┘
         │
         ├─→ "Oui" ──→ ✅ FALC (final) (si pas déjà FALC)
         └─→ Autre ──→ Continue
         │
         ▼
┌─────────────────┐
│  Q6: Autonomie  │
└────────┬────────┘
         │
         ├─→ "Non majorité" ──→ ✅ FALC (final) (si pas déjà FALC)
         └─→ Autre ──→ Continue
         │
         ▼
┌─────────────────┐
│ Q7-10: Collecte │ (info uniquement, pas d'impact)
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   RÉSULTAT      │
│   FINAL         │
└─────────────────┘
```

## Implémentation technique

### Variable de contrôle

```javascript
const currentResult = resultat.textContent;
```

Cette variable vérifie le texte actuel de la recommandation. Elle est utilisée pour vérifier si FALC a déjà été recommandé.

### Condition de garde

```javascript
if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
  // Vérifier si cette question déclenche FALC
}
```

Cette condition empêche de modifier la recommandation une fois que FALC a été conseillé.

## Cas d'usage

### Exemple 1 : FALC déclenché immédiatement

**Réponses** :
1. Organisme : Service public
2. Âge : Non
3. Niveau scolaire : **Oui, en majorité** ← FALC déclenché ici
4. Français : Oui
5. Handicap : Non
6. Autonomie : Oui
7-10. (collecte d'info)

**Résultat** : ✅ FALC (déclenché à Q3, ne change plus après)

---

### Exemple 2 : LC avec avertissements

**Réponses** :
1. Organisme : Entreprise
2. Âge : **Oui, en majorité** ← Avertissement LC+FALC
3. Niveau scolaire : Non
4. Français : **Non, ce n'est pas la majorité** ← Avertissement LC+FALC
5. Handicap : Non
6. Autonomie : Oui
7-10. (collecte d'info)

**Résultat** : ⚠️ LC avec avertissement FALC (jamais déclenché définitivement)

---

### Exemple 3 : LC sans avertissement

**Réponses** :
1. Organisme : Association
2. Âge : Non
3. Niveau scolaire : Non
4. Français : Oui
5. Handicap : Non
6. Autonomie : Oui
7-10. (collecte d'info)

**Résultat** : LC (aucune condition déclenchée)

## Notes importantes

1. **Irréversibilité** : Une fois FALC recommandé, impossible de revenir à LC
2. **Questions 7-10** : Servent uniquement à collecter des informations contextuelles
3. **Question 9** : Seule question à choix multiples (checkboxes)
4. **Accessibilité** : Le formulaire utilise `focusSurSectionSuivante()` pour améliorer la navigation au clavier

## Applications possibles

Ces règles peuvent être implémentées dans :
- Un système de recommandation automatique
- Un chatbot d'assistance à la décision
- Un outil d'audit de contenu
- Un système de classification de documents
- Une API de recommandation FALC/LC

## Licence et attribution

Source : Com'access (https://com-access.fr)
Organisme spécialisé en FALC, Accessibilité numérique et Langage clair
