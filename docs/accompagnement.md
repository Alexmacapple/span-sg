# Guide d'accompagnement SPAN

Ce guide accompagne les référents de service pour compléter leur module SPAN avec la checklist officielle de 33 critères DINUM/Arcom.

## Principe général

Chaque service du Secrétariat Général doit documenter son Schéma Pluriannuel d'Accessibilité Numérique (SPAN) en cochant les critères de conformité correspondant à sa situation réelle.

## Grille de conformité d'un SPAN (33 critères)

**Migration effectuée**: La grille a évolué de 31 points DINUM vers 33 critères officiels extraits du fichier de référence DINUM/Arcom (SPAN-checklist-v2024-02-05-AAL.ots).

**Source officielle**: Checklist validée conforme au référentiel DINUM pour l'élaboration des SPAN des entités publiques.

## Structure de la checklist

La checklist est organisée en 7 catégories thématiques:

### 1. Vision (3 critères)
- Politique d'accessibilité numérique formalisée dans le SPAN
- Intégration dans la stratégie numérique de l'entité
- Politique d'intégration des personnes en situation de handicap

### 2. RAN - Référent Accessibilité Numérique (7 critères)
- Durée du SPAN (maximum 3 ans - conformité légale art. 47 loi handicap)
- Position et missions du référent accessibilité
- Plans d'actions annuels et leur publication
- Accessibilité du SPAN lui-même (format accessible)

### 3. Organisation (6 critères)
- Ressources et expertises externes mobilisées
- Moyens techniques et outillage pour gérer l'accessibilité
- Organisation interne et modalités de contrôle
- Traitement des demandes des usagers

### 4. Budget (2 critères)
- Ressources humaines affectées (ETP identifiés)
- Ressources financières dédiées (ligne budgétaire)

### 5. Gestion de projets (7 critères)
- Intégration de l'accessibilité dès la conception
- Tests utilisateurs incluant personnes en situation de handicap
- Audits de conformité RGAA planifiés
- Calendrier de corrections priorisé (contenus les plus consultés)
- Mesures d'accessibilité non obligatoires (LSF, FALC, AAA)
- Liens vers SPAN dans les déclarations d'accessibilité

### 6. RH - Ressources Humaines (3 critères)
- Compétences accessibilité dans les fiches de poste
- Processus de recrutement intégrant l'accessibilité
- Actions de formation et sensibilisation des agents

### 7. Achats (5 critères)
- Clauses accessibilité dans les marchés publics
- Critères de notation et sélection incluant accessibilité
- Procédures de recette pour vérifier la conformité RGAA
- Conventions avec partenaires/opérateurs incluant exigences accessibilité

## Workflow de validation

**Processus hybride**: Référent métier → Validation MiWeb → Merge

### Étape 1: Autoévaluation par le référent

1. **Accéder à votre module**
   - Fichier: `docs/modules/[votre-service].md`
   - Section: "Checklist de conformité (33 critères)"

2. **Cocher les critères conformes**
   - Format: Remplacer `- [ ]` par `- [x]` pour chaque critère validé
   - Uniquement les critères effectivement réalisés
   - Ne pas cocher un critère "en cours" ou "prévu"

3. **Ajouter des justifications (recommandé)**
   ```markdown
   - [x] Politique d'accessibilité numérique formalisée <!-- CHECKLIST -->
     > Validé: SPAN 2024-2027 publié le [date]. [Description courte de la politique].
   ```

4. **Mettre à jour le front-matter**
   ```yaml
   ---
   service: [VOTRE-SERVICE]
   referent: "[Prénom Nom ou Entité]"
   updated: "2025-10-13"
   validation_status: in_progress  # draft | in_progress | validated
   ---
   ```

### Étape 2 : Validation par MiWeb

MiWeb effectue une revue technique et légale :

<ul class="fr-raw-list">
  <li>Vérification cohérence des critères cochés</li>
  <li>Validation des justifications fournies</li>
  <li>Ajustements si nécessaire (avec accord du référent)</li>
  <li>Changement du statut : <code>in_progress</code> → <code>validated</code></li>
</ul>

### Étape 3 : Publication

Une fois validé, le module est intégré :

<ul class="fr-raw-list">
  <li>Génération automatique du tableau de bord (docs/synthese.md)</li>
  <li>Calcul du score global : X/33 critères (XX.X%)</li>
  <li>Détermination du statut :
    <ul>
      <li><strong>Conforme</strong> : ≥ 75% (≥ 25/33 critères)</li>
      <li><strong>En cours</strong> : > 0% et < 75%</li>
      <li><strong>Non renseigné</strong> : 0%</li>
    </ul>
  </li>
</ul>

## Règles strictes à respecter

**ATTENTION** : Ces règles sont critiques pour le bon fonctionnement du système.

### Règle 1 : Ne jamais modifier les balises
```markdown
<!-- CHECKLIST -->
```
Ces balises sont utilisées par le script de calcul automatique. Ne pas les supprimer, déplacer ou modifier.

### Règle 2 : Total de 33 critères exactement
Le script vérifie que chaque module contient exactement 0 ou 33 critères balisés. Tout autre nombre déclenchera une erreur en CI.

### Règle 3 : Format des cases à cocher
- Case décochée : `- [ ]` (espace entre les crochets)
- Case cochée : `- [x]` ou `- [X]` (x ou X, pas d'espace)
- Le tiret et l'espace avant `[` sont obligatoires

### Règle 4 : Préserver la structure
Ne pas ajouter, supprimer ou réorganiser les 7 catégories. La structure est normalisée.

## Conseils pratiques

### Pour démarrer
1. Lire l'intégralité de la checklist une première fois
2. Identifier les "quick wins" (critères déjà conformes)
3. Évaluer les critères nécessitant documentation complémentaire
4. Planifier les critères non conformes dans le plan d'actions

### Documentation attendue
Pour chaque critère coché, avoir disponible:
- **Preuve documentaire** (lien vers document, procédure, rapport)
- **Date de mise en œuvre** ou de publication
- **Responsable identifié** (personne ou entité)

### Cas particuliers

**Critère non applicable**:
Si un critère ne s'applique pas à votre service (ex: "si nécessaire"), le cocher avec une justification claire.

```markdown
- [x] Mesures d'accessibilité non obligatoires (LSF, FALC, AAA) <!-- CHECKLIST -->
  > Non applicable: Service sans contenus vidéo/audio institutionnels. Mesures AAA respectées via DSFR.
```

**Critère partiellement conforme**:
Ne cocher que si >75% du périmètre est conforme. Sinon, laisser décoché et planifier dans les actions.

**Critère "en cours"**:
Ne pas cocher. Documenter l'avancement dans la section "Plan d'actions prioritaires" avec échéance.

## Exemple de module complété

Voir le module SIRCOM (docs/modules/sircom.md) pour un exemple de module partiellement évalué avec justifications détaillées.

Note: SIRCOM est actuellement en réévaluation avec la nouvelle grille de 33 critères.

## Support et contact

**Questions techniques sur le SPAN**:
- Référent MiWeb: [contact à définir]
- Documentation: Ce guide + roadmap/migration-checklist-34.md

**Questions sur l'accessibilité numérique**:
- DINUM: accessibilite.numerique@modernisation.gouv.fr
- Arcom: accessibilite@arcom.fr

## Ressources complémentaires

- **Référentiel RGAA 4.x**: https://accessibilite.numerique.gouv.fr/
- **Système de Design de l'État (DSFR)**: https://www.systeme-de-design.gouv.fr/
- **Guide pratique SPAN DINUM**: https://accessibilite.numerique.gouv.fr/ressources/plan-annuel/
- **Formations IGPDE**: Accessibles via le catalogue interne

---

*Guide d'accompagnement SPAN v1.0 - Dernière mise à jour: 13 octobre 2025*
