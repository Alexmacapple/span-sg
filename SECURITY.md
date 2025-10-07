# Politique de Sécurité SPAN SG

## Versions Supportées

Seule la dernière version stable de SPAN SG reçoit des correctifs de sécurité.

| Version | Support |
| ------- | ------- |
| 1.0.x   | ✅ Supportée |
| < 1.0   | ❌ Non supportée (POC) |

## Signaler une Vulnérabilité

### Responsible Disclosure

Si vous découvrez une vulnérabilité de sécurité dans SPAN SG, merci de **NE PAS** créer d'issue publique. Suivez cette procédure :

### 1. Contact Privé

Envoyez un email à **security@span-sg.local** (ou contactez directement les mainteneurs via GitHub) avec :
- Description détaillée de la vulnérabilité
- Étapes de reproduction
- Impact potentiel
- Version affectée
- Votre nom/pseudo (si vous souhaitez être crédité)

### 2. Délai de Réponse

- **Accusé réception** : < 48h
- **Analyse vulnérabilité** : < 7 jours
- **Correctif publié** : < 30 jours (selon gravité)

### 3. Coordination

Nous coordonnerons avec vous pour :
- Valider le correctif
- Planifier publication (disclosure coordonnée)
- Créditer votre découverte (si souhaité)

### 4. Gravité

Nous utilisons CVSS 3.1 pour évaluer la gravité :
- **Critique (9.0-10.0)** : Correctif < 7 jours
- **Haute (7.0-8.9)** : Correctif < 14 jours
- **Moyenne (4.0-6.9)** : Correctif < 30 jours
- **Faible (0.1-3.9)** : Correctif prochaine release

## Vulnérabilités Hors Périmètre

Ne sont **PAS** considérées comme vulnérabilités :
- Déni de service local (build MkDocs)
- Accès physique machine (scripts locaux)
- Social engineering
- Vulnérabilités dépendances tierces déjà publiques (Dependabot gère)

## Mesures de Sécurité Existantes

### Dépendances
- **Dependabot** : Scan automatique hebdomadaire (lundi 9h)
- **Security alerts** : Notifications CVE activées
- **Auto-updates** : PR automatiques pour vulnérabilités

### Code
- **Secrets** : Exclus via .gitignore
- **CI/CD** : Validation automatique (linter, tests)
- **Permissions** : Repo privé, accès restreint

### Git History
- **inspiration/** : Purgé de l'historique (BFG Repo-Cleaner)
- **Sensitive files** : Nettoyage historique effectué

## Historique Sécurité

### v1.0.0-poc (2025-10-07)
- Aucune vulnérabilité connue
- Audit informel réalisé (07/10/2025)
- Secrets exclus (.gitignore + untrack inspiration/)
- Dependabot configuré
- SECURITY.md créé

## Reconnaissance

Nous remercions les chercheurs en sécurité ayant signalé des vulnérabilités :
- [Aucun pour l'instant]

---

**Merci de contribuer à la sécurité de SPAN SG !**
