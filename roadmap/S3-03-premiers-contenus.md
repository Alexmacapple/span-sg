# Story S3-03 : Renseigner premiers contenus modules

**Phase** : Semaine 3 - Onboarding
**Priorité** : Moyenne
**Estimation** : Variable (2-5h par service)
**Assigné** : Référents services (SNUM, SIRCOM, SRH, SIEP, SAFI, BGS)

---

## Contexte projet

Après formation Git (S3-02), les référents services sont autonomes pour éditer leurs modules. Cette story consiste à :
- Renseigner les 5 sections obligatoires (Périmètre, État des lieux, Organisation, Plan d'action, Indicateurs)
- Cocher les premiers points DINUM (ceux déjà conformes)
- Compléter le plan d'actions prioritaires 2025
- Renseigner les blocs légaux (déclaration accessibilité, charge disproportionnée)

**Objectif de qualité** : Contenu minimal mais cohérent et exploitable (pas de placeholders "Lorem ipsum").

**Rythme** : Progressif. Pas besoin de tout remplir d'un coup. Les modules évoluent dans le temps.

---

## Objectif

Chaque service renseigne son module avec du contenu réel et initial (version 0.1), permettant d'avoir une première synthèse SPAN SG exploitable.

---

## Prérequis

- [ ] Story S3-01 complétée (modules vides créés)
- [ ] Story S3-02 complétée (référents formés à Git)
- [ ] Référents identifiés et engagés
- [ ] Accès aux données accessibilité de chaque service (audits, déclarations)

---

## Étapes d'implémentation (par service)

### Phase 1 : Collecte des informations

Chaque référent doit rassembler :
- Liste des applications/sites web du service
- Audits accessibilité existants (dates, scores)
- Nom du référent accessibilité et % ETP
- Budget annuel dédié accessibilité (si identifié)
- Actions prioritaires prévues 2025
- URL déclaration d'accessibilité (si existante)

### Phase 2 : Renseigner Section 1 - Périmètre

**Contenu minimal** :
```markdown
## 1. Périmètre

Le service [NOM] gère les applications et services numériques suivants :

### Applications métiers principales
- **[App 1]** : Description courte, audience (interne/externe), criticité
- **[App 2]** : Description courte, audience, criticité
- **[App 3]** : Description courte, audience, criticité

### Sites web et intranets
- **Site principal** : [URL], [X] visiteurs/jour
- **Intranet** : Usage interne, [X] agents

### Démarches essentielles
- [Démarche 1] : Description
- [Démarche 2] : Description
```

**Exemple SIRCOM** :
```markdown
## 1. Périmètre

Le service SIRCOM gère :
- Portail RH interne (5000 agents/jour)
- Application de formation en ligne
- Site carrières publiques (externe)
```

### Phase 3 : Renseigner Section 2 - État des lieux

**Contenu minimal** :
```markdown
## 2. État des lieux (synthèse)

### Audits réalisés
- **[App 1]** : Audit [interne/tiers], [date], score [XX%] conforme RGAA
- **[App 2]** : Audit [interne/tiers], [date], score [XX%] conforme RGAA
- Non audité : [App 3], [App 4]

### Points critiques identifiés
- Contraste couleurs insuffisant (niveau AA)
- Formulaires sans labels explicites
- Navigation clavier incomplète
```

### Phase 4 : Renseigner Section 3 - Organisation

**Contenu minimal** :
```markdown
## 3. Organisation

### Référent accessibilité
- **Nom** : [Prénom Nom]
- **ETP dédié** : [X%] (ex: 20%, soit 1 jour/semaine)
- **Contact** : [email]

### Équipe projet
- Chef de projet SI : [Nom]
- Développeurs sensibilisés : [X/Y]
- UX/UI : [Nom ou "Prestation externe"]

### Formations prévues
- T1 2025 : Sensibilisation large (tous agents)
- T2 2025 : Formation développeurs RGAA (5 jours)
```

### Phase 5 : Renseigner Section 4 - Plan d'action annuel

**Contenu minimal** : Tableau avec 3-5 actions prioritaires

```markdown
## 4. Plan d'action annuel

| Action | Échéance | Responsable | Budget | Statut |
|--------|----------|-------------|--------|--------|
| Audit RGAA complet site principal | T2 2025 | [Nom] | 8000€ | À commencer |
| Correction contraste couleurs | T2 2025 | Dev interne | 0€ | En cours |
| Formation équipe dev RGAA | T3 2025 | RH | 3000€ | À commencer |
| Mise en conformité formulaires | T4 2025 | [Nom] | 5000€ | À commencer |
```

### Phase 6 : Renseigner Section 5 - Indicateurs clés

**Contenu minimal** :
```markdown
## 5. Indicateurs clés

### Taux de conformité
- Sites web : [X%] conforme AA (cible 100% fin 2027)
- Applications métiers : [Y%] conforme AA

### Formations
- Agents sensibilisés : [X/Y] ([Z%])
- Équipe dev formée : [A/B] ([C%])

### Marchés avec clauses accessibilité
- [X] marchés sur [Y] intègrent clauses RGAA ([Z%])
```

### Phase 7 : Cocher les points DINUM conformes

Pour chaque point des 31, cocher `[x]` si déjà conforme :

**Exemple** :
```markdown
- [x] Stratégie numérique: accessibilité intégrée et publiée <!-- DINUM -->
- [ ] Politique d'inclusion des personnes handicapées formalisée <!-- DINUM -->
- [x] Référent accessibilité numérique officiellement désigné <!-- DINUM -->
- [x] Temps alloué et moyens du référent définis <!-- DINUM -->
```

**Prudence** : Ne cocher que si **vraiment conforme**. En cas de doute, laisser décoché.

### Phase 8 : Renseigner blocs légaux

**Déclaration d'accessibilité** :
```markdown
- Déclaration d'accessibilité: https://[service].gouv.fr/accessibilite
- Date de mise à jour : 15/09/2025
- Méthode : Audit externe par [organisme], septembre 2025
```

**Charge disproportionnée** (si applicable) :
```markdown
- Charge disproportionnée: Oui
  - Élément: Ancienne application legacy (refonte prévue 2026)
  - Justification: Coût correction > 50% valeur résiduelle application
  - Alternative: Assistance téléphonique dédiée (0800...)
  - Réévaluation: T1 2026 (post-refonte)
```

### Phase 9 : Créer la Pull Request

```bash
# Option A : Interface GitHub
1. Éditer docs/modules/[service].md
2. Commit : "feat([service]): renseigne contenu initial sections 1-5"
3. Create PR vers draft

# Option B : Git local
git checkout -b feature/update-[service]-initial
# ... éditer le module ...
git add docs/modules/[service].md
git commit -m "feat([service]): renseigne contenu initial sections 1-5"
git push -u origin feature/update-[service]-initial
# Créer PR sur GitHub
```

### Phase 10 : Revue et merge

**Revue par Bertrand/Alex** :
- Contenu cohérent et exploitable
- Pas de secrets/infos sensibles
- Front-matter à jour (date)
- 31 points DINUM présents (total inchangé)

**Merge vers draft** → Preview mise à jour automatiquement.

---

## Critères d'acceptation (par service)

- [ ] Sections 1-5 renseignées avec contenu réel (pas de placeholders)
- [ ] Tableau plan d'action contient 3-5 actions concrètes
- [ ] Au moins 1 point DINUM coché (ou justification si 0)
- [ ] URL déclaration d'accessibilité renseignée (ou TODO avec échéance)
- [ ] Analyse charge disproportionnée remplie (ou "Non applicable")
- [ ] Front-matter à jour (referent, updated)
- [ ] PR créée vers draft et validée
- [ ] Score module > 0% dans synthese.md

---

## Tests de validation (global)

```bash
# Test 1 : Les 6 modules ont du contenu (> 100 lignes hors template)
for module in snum sircom srh siep safi bgs; do
  lines=$(wc -l < docs/modules/$module.md)
  echo "$module: $lines lignes"
  test $lines -gt 100 || echo "WARN: $module peu rempli"
done

# Test 2 : Au moins 1 module > 0/31
python scripts/calculate_scores.py
grep -v "0/31" docs/synthese.md | grep -v "TOTAL" && echo "OK" || echo "WARN: tous modules vides"

# Test 3 : Toutes les URLs accessibilité renseignées ou TODO
for module in snum sircom srh siep safi bgs; do
  grep -q "Déclaration d'accessibilité:" docs/modules/$module.md && echo "$module: OK" || echo "$module: MANQUANT"
done

# Test 4 : Score global > 10%
score=$(grep "TOTAL" docs/synthese.md | grep -oP '\d+\.\d+%' | head -1)
echo "Score global : $score"
```

---

## Dépendances

**Bloque** :
- S4-01 (review contenus nécessite du contenu initial)

**Dépend de** :
- S3-01 (modules vides créés)
- S3-02 (référents formés et autonomes)

---

## Références

- **PRD v3.3** : Section 11 "Plan de mise en œuvre" → Semaine 3 Onboarding
- **docs/modules/_template.md** : Structure de référence
- **CONTRIBUTING.md** : Guide création PR

---

## Notes et risques

**Qualité variable**
Les 6 services n'avanceront pas au même rythme. Certains auront un contenu riche (audits existants), d'autres minimaliste (début démarche).

**Accepter l'itératif** : Version 0.1 ne sera pas parfaite. L'important est d'avoir une base pour la suite.

**Manque de données**
Si un service n'a aucun audit, aucun budget identifié :
- Renseigner "En cours d'analyse" dans les sections
- Cocher 0 points DINUM (normal en phase démarrage)
- Prévoir actions d'état des lieux dans le plan 2025

**Confidentialité**
Éviter de publier :
- Noms complets de prestataires sous contrat
- Budgets précis (arrondir : "~5K€")
- Vulnérabilités critiques non corrigées

**Cohérence globale**
Alexandra doit relire l'ensemble pour :
- Harmoniser les formats
- Vérifier cohérence inter-services
- Identifier doublons/synergies

**Délai réaliste**
Cette story peut prendre **2-4 semaines** (pas 1 semaine). Les référents ont d'autres activités. Prévoir :
- Relances hebdo
- Support individuel au besoin
- Date butoir souple

---

## Post-tâche

Générer un rapport d'avancement :
```bash
python scripts/calculate_scores.py

# Créer rapport
cat > docs/avancement-s3.md << 'EOF'
# Avancement renseignement modules (S3-03)

| Service | Score | Sections remplies | Statut |
|---------|-------|-------------------|--------|
| SNUM | 5/31 (16%) | 5/5 | ✅ Complet |
| SIRCOM | 31/31 (100%) | 5/5 | ✅ Complet |
| SRH | 0/31 (0%) | 3/5 | ⏳ En cours |
| SIEP | 2/31 (6%) | 5/5 | ✅ Complet |
| SAFI | 0/31 (0%) | 2/5 | ⏳ En cours |
| BGS | 1/31 (3%) | 4/5 | ⏳ En cours |

**Global** : 39/186 (21%)

## Prochaines étapes
- Relance SRH, SAFI, BGS : compléter sections manquantes
- Revue globale Alexandra : harmonisation formats
- PR draft → main si score global ≥ 30%
EOF
```

Communiquer avancement :
```
📧 À : Référents services + Bertrand, Alex, Yves
Objet : SPAN SG - Avancement S3 (Onboarding)

Statut renseignement modules après formation :
- ✅ 3 services complets (SNUM, SIRCOM, SIEP)
- ⏳ 3 services en cours (SRH, SAFI, BGS)

Score global actuel : 21% (39/186 points)

Voir détail : [lien docs/avancement-s3.md]

Prochaine échéance : S4-01 (Review contenus) prévue [date]
```