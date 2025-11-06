# Arbre de décision : FALC ou Langage Clair ?

## Source
- **Analyse du formulaire** : https://com-access.fr/falc-ou-lc/
- **Date** : 2025-11-06
- **Organisme** : Com'access

---

## Principe général

**RÈGLE D'OR** : Le formulaire utilise une **logique d'escalade irréversible** :

1. **Par défaut** : Langage Clair (LC)
2. **Si l'une des 3 conditions FALC est remplie** : FALC (décision finale)
3. **Une fois FALC recommandé** : impossible de revenir à LC

---

## Les 3 conditions qui déclenchent le FALC (définitif)

| # | Question | Condition FALC | Justification |
|---|----------|----------------|---------------|
| **Q3** | **Niveau scolaire ≤ 4ème** | "Oui, en majorité" | Faible niveau de scolarisation = besoin de simplification maximale |
| **Q5** | **Handicap mental/psychique/cognitif** | "Oui, en majorité" | Public cible principal du FALC selon norme européenne |
| **Q6** | **Non autonome pour lire** | "Non, ce n'est pas la majorité" | Besoin d'accompagnement = FALC obligatoire |

**Si AU MOINS UNE de ces 3 conditions est "OUI"** → ✅ **UTILISER LE FALC**

---

## Les 2 conditions d'avertissement (LC + envisager FALC)

| # | Question | Condition | Recommandation |
|---|----------|-----------|----------------|
| **Q2** | **Public âgé ≥ 70 ans** | "Oui, en majorité" | LC mais **envisager le FALC** |
| **Q4** | **Maîtrise faible du français** | "Non, ce n'est pas la majorité" | LC mais **envisager le FALC** |

**Si ces conditions sont remplies mais pas les 3 du dessus** → ⚠️ **Langage Clair + évaluer si FALC nécessaire**

---

## Arbre de décision complet

```
DÉBUT
  │
  ▼
┌─────────────────────────────────────────────────────┐
│ Q3: Public avec niveau scolaire ≤ 4ème (majorité) ? │
└──────────────────┬──────────────────────────────────┘
                   │
          ┌────────┴────────┐
          │                 │
        OUI                NON
          │                 │
          ▼                 ▼
    ✅ FALC         ┌─────────────────────────────────────────┐
    (FINAL)         │ Q5: Public avec handicap cognitif/     │
                    │     mental/psychique (majorité) ?       │
                    └──────────────┬──────────────────────────┘
                                   │
                          ┌────────┴────────┐
                          │                 │
                        OUI                NON
                          │                 │
                          ▼                 ▼
                    ✅ FALC         ┌──────────────────────────────────┐
                    (FINAL)         │ Q6: Public autonome pour lire ?  │
                                    │     (majorité)                    │
                                    └──────────┬───────────────────────┘
                                               │
                                      ┌────────┴────────┐
                                      │                 │
                                     NON               OUI
                              (non autonome)     (autonome)
                                      │                 │
                                      ▼                 ▼
                                ✅ FALC         ┌──────────────────────┐
                                (FINAL)         │ Vérifier Q2 et Q4    │
                                                └──────────┬───────────┘
                                                           │
                                                           ▼
                                            ┌──────────────────────────────┐
                                            │ Q2: Public âgé ≥70 ans ?     │
                                            │ OU                            │
                                            │ Q4: Maîtrise faible français ?│
                                            └──────────┬───────────────────┘
                                                       │
                                              ┌────────┴────────┐
                                              │                 │
                                            OUI               NON
                                     (au moins 1)       (aucune)
                                              │                 │
                                              ▼                 ▼
                                    ⚠️ LC + envisager     ✅ LC
                                       FALC              (simple)
```

---

## Règles simplifiées

### UTILISER LE FALC si :

✅ **Au moins 1 critère parmi** :
1. Niveau scolaire ≤ 4ème (majorité du public)
2. Handicap mental/psychique/cognitif (majorité du public)
3. Non autonome pour lire (majorité du public)

### UTILISER LE LANGAGE CLAIR si :

✅ **Aucun des 3 critères ci-dessus** n'est rempli

**Avec avertissement** (envisager le FALC) si :
- Public âgé ≥ 70 ans (majorité)
- OU Maîtrise faible du français (majorité)

---

## Tableaux de décision

### Scénario 1 : Critères FALC

| Niveau ≤4e | Handicap cognitif | Non autonome | → Résultat |
|-----------|-------------------|--------------|-----------|
| ✅ OUI | - | - | **FALC** |
| NON | ✅ OUI | - | **FALC** |
| NON | NON | ✅ OUI | **FALC** |
| ✅ OUI | ✅ OUI | - | **FALC** |
| ✅ OUI | - | ✅ OUI | **FALC** |
| - | ✅ OUI | ✅ OUI | **FALC** |
| ✅ OUI | ✅ OUI | ✅ OUI | **FALC** |

**Si AU MOINS 1 case cochée** → **FALC obligatoire**

### Scénario 2 : Critères Langage Clair avec avertissement

| Niveau ≤4e | Handicap | Non autonome | Âge ≥70 | Français faible | → Résultat |
|-----------|----------|--------------|---------|----------------|-----------|
| NON | NON | NON | ✅ OUI | - | **LC + avertissement** |
| NON | NON | NON | - | ✅ OUI | **LC + avertissement** |
| NON | NON | NON | ✅ OUI | ✅ OUI | **LC + avertissement** |

### Scénario 3 : Langage Clair simple

| Niveau ≤4e | Handicap | Non autonome | Âge ≥70 | Français faible | → Résultat |
|-----------|----------|--------------|---------|----------------|-----------|
| NON | NON | NON | NON | NON | **LC** |

---

## Exemples concrets

### Exemple 1 : Service public - Démarches administratives

**Public cible** :
- Tout public
- Pas de handicap spécifique
- Autonome pour lire
- Niveau scolaire : secondaire
- Âge : mixte (pas majorité ≥70)
- Français : maîtrise correcte

**Critères FALC** :
- Q3 Niveau ≤4e : ❌ NON
- Q5 Handicap : ❌ NON
- Q6 Non autonome : ❌ NON

**Critères avertissement** :
- Q2 Âge ≥70 : ❌ NON
- Q4 Français faible : ❌ NON

**→ Résultat : ✅ LANGAGE CLAIR**

---

### Exemple 2 : ESAT - Règlement intérieur

**Public cible** :
- Travailleurs en ESAT
- **Handicap cognitif/mental : OUI (majorité)**
- Niveau scolaire : variable
- Autonome pour lire : variable

**Critères FALC** :
- Q3 Niveau ≤4e : Peut-être
- Q5 Handicap : ✅ **OUI (majorité)**
- Q6 Non autonome : Peut-être

**→ Résultat : ✅ FALC (déclenché par Q5)**

---

### Exemple 3 : Mairie - Info seniors

**Public cible** :
- Seniors ≥ 70 ans (majorité)
- Pas de handicap spécifique
- Autonome pour lire
- Niveau scolaire : secondaire terminé

**Critères FALC** :
- Q3 Niveau ≤4e : ❌ NON
- Q5 Handicap : ❌ NON
- Q6 Non autonome : ❌ NON

**Critères avertissement** :
- Q2 Âge ≥70 : ✅ **OUI (majorité)**

**→ Résultat : ⚠️ LANGAGE CLAIR + envisager FALC**

Recommandation : Commencer en LC, tester auprès du public, envisager FALC si retours négatifs.

---

### Exemple 4 : Association - Cours d'alphabétisation

**Public cible** :
- Adultes en alphabétisation
- **Niveau scolaire ≤ 4e : OUI (majorité)**
- **Français faible : OUI (majorité)**
- Autonome pour lire : en apprentissage

**Critères FALC** :
- Q3 Niveau ≤4e : ✅ **OUI (majorité)**
- Q5 Handicap : ❌ NON
- Q6 Non autonome : Peut-être

**→ Résultat : ✅ FALC (déclenché par Q3)**

---

### Exemple 5 : Entreprise - Communication interne

**Public cible** :
- Employés (tout niveau)
- Pas de handicap spécifique
- Autonome pour lire
- Niveau : Bac et plus
- Français : maîtrise professionnelle

**Critères FALC** :
- Q3 Niveau ≤4e : ❌ NON
- Q5 Handicap : ❌ NON
- Q6 Non autonome : ❌ NON

**Critères avertissement** :
- Q2 Âge ≥70 : ❌ NON
- Q4 Français faible : ❌ NON

**→ Résultat : ✅ LANGAGE CLAIR**

---

### Exemple 6 : Foyer d'hébergement - Livret d'accueil

**Public cible** :
- Personnes avec déficience intellectuelle
- **Handicap cognitif : OUI (majorité)**
- **Non autonome pour lire : OUI (majorité)**
- **Niveau ≤ 4e : OUI (majorité)**

**Critères FALC** :
- Q3 Niveau ≤4e : ✅ **OUI (majorité)**
- Q5 Handicap : ✅ **OUI (majorité)**
- Q6 Non autonome : ✅ **OUI (majorité)**

**→ Résultat : ✅✅✅ FALC OBLIGATOIRE (3/3 critères)**

---

## Matrice de décision rapide

| Public cible | Niveau ≤4e | Handicap cognitif | Non autonome lecture | → Décision |
|-------------|-----------|-------------------|---------------------|-----------|
| **ESAT, IME, Foyers spécialisés** | Souvent | Souvent | Souvent | **FALC** |
| **Services sociaux, CAF, Pôle Emploi** | Variable | Parfois | Rarement | **LC** (ou **FALC** selon public) |
| **Associations insertion** | Souvent | Parfois | Parfois | **FALC** |
| **Seniors (≥70)** | Rarement | Rarement | Rarement | **LC + envisager FALC** |
| **Migrants/FLE** | Variable | Rarement | Variable | **LC** ou **FALC** (selon niveau) |
| **Grand public** | Rarement | Rarement | Rarement | **LC** |
| **Professionnels** | Rarement | Rarement | Rarement | **LC** |

---

## Questions fréquentes

### Q : Si mon public est mixte (certains avec handicap, d'autres non), que choisir ?

**R :** Si le handicap cognitif concerne la **majorité** du public → FALC.
Si c'est une minorité → LC, et prévoir une version FALC en complément.

---

### Q : Mon public a 65 ans en moyenne, dois-je utiliser le FALC ?

**R :** Non. Le critère âge est ≥70 ans ET en **majorité**.
À 65 ans → LC recommandé.
Entre 70-75 ans → LC + envisager FALC selon retours.

---

### Q : Le public maîtrise mal le français, mais est diplômé (≥Bac). FALC ou LC ?

**R :** Critères :
- Q3 Niveau ≤4e : ❌ NON (diplômé Bac)
- Q4 Français faible : ✅ OUI

**→ LC + envisager FALC** (avertissement uniquement)

---

### Q : Puis-je utiliser FALC même si aucun critère n'est rempli ?

**R :** Oui ! Le FALC est **plus accessible que le LC**. Vous pouvez toujours choisir FALC.
L'arbre indique le **minimum requis**, pas le maximum autorisé.

---

### Q : Mon document fait 50 pages, quel impact ?

**R :** La taille du document (Q8) ne change pas la recommandation.
Par contre :
- **FALC** : Privilégier documents courts (<32 pages) pour faciliter lecture
- **LC** : Peut gérer documents plus longs

---

### Q : Le format de publication (web, papier) change-t-il la décision ?

**R :** Non. Les questions Q9 (publication) et Q10 (format) sont pour **info uniquement**.
La décision FALC/LC dépend uniquement du **public cible** (Q2-Q6).

---

## Recommandations Com'access

D'après le formulaire, **Com'access recommande** :

### Utiliser le FALC pour :
- ✅ Public avec handicap cognitif/mental/psychique (majorité)
- ✅ Public avec niveau scolaire ≤ 4ème (majorité)
- ✅ Public non autonome pour lire (majorité)

### Utiliser le Langage Clair pour :
- ✅ Tout le reste (grand public, professionnels, etc.)
- ⚠️ Avec vigilance pour : seniors ≥70 ans, maîtrise faible du français

### Le FALC n'est PAS obligatoire pour :
- ❌ Grand public (même si on peut l'utiliser)
- ❌ Professionnels
- ❌ Personnes autonomes sans handicap cognitif

---

## Résumé en 3 points

1. **FALC obligatoire si** : handicap cognitif OU niveau ≤4e OU non autonome (majorité)

2. **LC recommandé sinon**, avec avertissement si : âgé ≥70 ans OU français faible (majorité)

3. **FALC toujours possible** : même si pas obligatoire, le FALC est plus accessible

---

## Licence

Analyse basée sur le formulaire Com'access (https://com-access.fr/falc-ou-lc/)
Com'access : SARL spécialisée en FALC, Accessibilité numérique et Langage clair
