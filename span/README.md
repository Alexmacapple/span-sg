# Sources SPAN officielles

Ce répertoire contient les documents SPAN officiels utilisés comme sources pour mapper les modules du SPAN SG.

## Fichiers présents

### span-sircom-sg.md
- **Service** : SIRCOM (Service Interministériel des Ressources et des Compétences)
- **Organisme** : MEFSIN - SG/SIRCOM
- **Période couverte** : 2024-2027
- **Date document source** : 2024 (à préciser)
- **Module mappé** : `docs/modules/sircom.md`
- **Mapping effectué** : 2025-10 (S4-00, S4-01)
- **Résultat** : 25/31 points DINUM mappés (80.6%)
- **Mapping par** : Alexandra + Bertrand
- **Validation** : Stéphane (Chef mission numérique SNUM-SG, 2025-10-XX)

### span-portail-pro.sg.md
- **Service** : SNUM/SG - Portailpro.gouv (Mission France Recouvrement)
- **Organisme** : MEFSIN - SNUM/SG
- **Période couverte** : 2025-2027
- **Date document source** : 2025 (à préciser)
- **Module mappé** : `docs/modules/snum.md`
- **Mapping effectué** : 2025-10 (S4-00, S4-01)
- **Résultat** : 21/31 points DINUM mappés (67.7%)
- **Mapping par** : Alexandra + Bertrand
- **Validation** : Stéphane (Chef mission numérique SNUM-SG, 2025-10-XX)

## Usage

Ces fichiers sont **en lecture seule** et conservés pour traçabilité. Toute modification des modules SIRCOM/SNUM doit se faire dans `docs/modules/`.

**Processus de mapping** :
1. Analyse source SPAN (document politique stratégique)
2. Extraction contenus pertinents selon guide `roadmap/S4-00-mapping-contenus.md`
3. Synthèse et adaptation format 31 points DINUM
4. Rédaction dans module cible (`docs/modules/*.md`)
5. Validation et commit

## Provenance

**Documents transmis par** : [Source à documenter - Direction communication / Référent accessibilité]
**Date transmission** : [Date à documenter]
**Format original** : Markdown (édition manuelle depuis documents officiels)

## Nature des documents

**SPAN = Schéma Pluriannuel d'Accessibilité Numérique**

Ces documents décrivent la **politique et stratégie accessibilité** de chaque service pour la période 2024-2027 ou 2025-2027. Ils contiennent :
- Engagement de la direction
- Organisation (référents, moyens, budgets)
- Périmètre applicatif (sites web, intranets, applications)
- Plans annuels (audits, formations, corrections)
- Indicateurs de suivi

**⚠️ Important** : Ces documents SPAN sont des politiques stratégiques, PAS des réponses exhaustives aux 31 points de contrôle DINUM. Le mapping nécessite interprétation et synthèse. Certains points DINUM peuvent être absents des sources (ex: grille recrutement RH, tests utilisateurs) → documentés comme TODO dans modules.

## Confidentialité

**Visibilité** : Ces fichiers sont dans un dépôt GitHub **privé** (organisation uniquement). Pas de diffusion externe sans autorisation.

**Données sensibles** : Aucune donnée personnelle ou confidentielle sensible. Contenus = politique accessibilité publique ou interne SG.

## Historique modifications

| Date | Fichier | Modification | Auteur |
|------|---------|--------------|--------|
| 2025-10-XX | span-sircom-sg.md | Ajout métadonnées front-matter traçabilité | Claude Code |
| 2025-10-XX | span-portail-pro.sg.md | Ajout métadonnées front-matter traçabilité | Claude Code |
| 2025-09-XX | *.md | Import initial sources SPAN officielles | [À documenter] |

## Maintenance

**Responsable** : Alexandra + Bertrand

**Mise à jour** : Si nouveaux SPAN officiels disponibles (révision annuelle ou correctifs) :
1. Ajouter nouveau fichier `span/[service]-[année].md`
2. Mettre à jour métadonnées front-matter (date_source, mapping_date)
3. Re-mapper module cible si changements substantiels
4. Documenter historique dans ce README

**Archivage anciennes versions** : Conserver anciennes versions SPAN dans `span/archives/` si révision majeure (ex: SPAN 2027-2030).

---

*Dernière mise à jour : 2025-10-02*
