# Squad IA Blackboard

> **Note pour relecture humaine**
>
> Je m'attendais plutôt à une évaluation par agent ; pour une relecture humaine, le document le plus adapté pour comprendre le projet, ses choix et ses limites est [outputs/rapport_final.md](outputs/rapport_final.md).

Projet Python qui crée une petite squad de 3 agents IA spécialisés :
- `Product` : PRD, MVP, cadrage produit
- `Tech` : architecture, faisabilité, risques techniques
- `Growth` : go-to-market, acquisition, lancement

Les agents collaborent via une mémoire partagée appelée `blackboard`. Ils ne simulent pas un swarm autonome : l'orchestration est explicite, contrôlée et auditable.

## Lecture Rapide Pour L'Évaluation

Le challenge demande :
- 3 agents avec rôles distincts
- une collaboration / confrontation de l'idée sous plusieurs angles
- un PRD finalisé
- une architecture avec schéma
- un plan GTM
- une preuve d'orchestration

Les livrables générés se trouvent dans :

```text
outputs/tests/<ProjectName>/version 1/
```

Les derniers projets testés sont :
- `outputs/tests/CareSync/version 1/`
- `outputs/tests/LocalLoop/version 1/`
- `outputs/tests/Melody/version 1/`
- `outputs/tests/SkillBridge/version 1/`

Dans chaque dossier :
- `prd.md` : PRD finalisé
- `architecture.md` : architecture et faisabilité
- `architecture-diagram.png` : schéma d'architecture
- `architecture-diagram.mmd` : source Mermaid du schéma
- `gtm.md` : plan go-to-market
- `blackboard.md` : mémoire partagée, décisions, arbitrages, readiness
- `activity_log.txt` : trace d'exécution des agents
- `evaluation-CEO.md` : évaluation externe type CEO

## Preuve D'Orchestration

Il n'y a pas de MP4 ou de captures d'écran.

Le projet ne s'y prête pas vraiment : il s'agit de scripts Python, d'appels LLM/API et de génération de fichiers Markdown/PNG.

La preuve de concept est donc auditable directement dans :
- le code d'orchestration : `app/orchestrator.py`
- les agents : `app/agents/product_agent.py`, `app/agents/tech_agent.py`, `app/agents/growth_agent.py`
- la mémoire partagée : `app/blackboard.py`
- les prompts : `app/prompts V3/`
- les traces générées : `blackboard.md` et `activity_log.txt` dans les dossiers de run

## Architecture Du Repo

```text
app/
  main.py                  # point d'entrée
  orchestrator.py          # ordre d'exécution des agents
  blackboard.py            # mémoire partagée
  llm.py                   # couche d'appel modèle
  architecture_render.py   # rendu Mermaid vers PNG
  agents/
    product_agent.py
    tech_agent.py
    growth_agent.py
  prompts V3/
    product_prompt.md
    tech_prompt.md
    growth_prompt.md
  prompts V2/              # ancienne génération de prompts, conservée pour historique
  prompts/                 # prompts initiaux / historiques
  evaluations/
    evaluator_quality.md
    evaluator_prompt.md

dev-agents/                # prompts du système Architecte / Developer utilisé pour développer

outputs/
  projects/                # briefs des projets testés
  tests/                   # résultats générés par projet
  tests_preliminaires/     # traces des premiers essais, notamment avec Ollama
  dev-steps/               # historique des étapes de développement
  workflow.md              # documentation technique du workflow
  rapport_final.md         # récit synthétique du projet
  etude-qualitative-des-livrables.md
  architecte-dev.md        # système complémentaire utilisé pour développer

requirements.txt           # dépendances Python minimales
package.json               # dépendance Mermaid CLI pour générer les PNG
```

## Dans Le Périmètre Du Challenge

Ce qui répond directement au challenge :
- les 3 agents Product / Tech / Growth
- leur spécialisation par prompt
- l'orchestration via `app/orchestrator.py`
- le blackboard comme mémoire commune
- les livrables PRD / architecture / GTM
- les schémas d'architecture en PNG
- la trace d'orchestration via `blackboard.md` et `activity_log.txt`

## Hors Périmètre Direct

Quelques éléments existent autour du challenge, mais ne sont pas le coeur de la demande :
- `outputs/rapport_final.md` : rapport narratif sur la construction du projet
- `outputs/workflow.md` : documentation détaillée du fonctionnement interne
- `outputs/etude-qualitative-des-livrables.md` : analyse qualitative utile pour comprendre la valeur réelle des documents produits
- `outputs/dev-steps/` : historique de développement
- `outputs/projects/` : briefs utilisés pour tester le système
- `outputs/tests_preliminaires/` : traces des premiers essais, notamment avec Ollama
- `outputs/architecte-dev.md` : système agentique complémentaire Architecte / Developer utilisé pour construire le projet
- `dev-agents/` : prompts et contexte des agents de développement Architecte / Developer
- `app/prompts V2/` et `app/prompts/` : anciennes générations de prompts, conservées pour expliquer l'évolution du système
- `app/evaluations/` : prompts d'évaluation externes, utiles pour juger les sorties mais distincts de la squad Product / Tech / Growth

Le système Architecte / Developer est presque un projet à part. Il a aidé à construire proprement ce repo, mais le challenge principal porte sur la squad Product / Tech / Growth.

## Projets Et Prompts De Test

Les briefs utilisés pour tester le système sont dans :

```text
outputs/projects/
```

Ils servent de matière d'entrée pour les runs CareSync, LocalLoop, Melody et SkillBridge.

Les prompts actifs recommandés sont dans :

```text
app/prompts V3/
```

Les dossiers `app/prompts/` et `app/prompts V2/` sont conservés comme historique. Ils montrent l'évolution du projet, mais ne représentent pas le meilleur état actuel.

## Exécution

Le projet utilise des variables d'environnement pour choisir le modèle et le projet.

Installation Python minimale :

```bash
pip install -r requirements.txt
```

Pour générer les schémas PNG à partir de Mermaid, installer aussi les dépendances npm :

```bash
npm install
```

Exemple :

```bash
export BLACKBOARD_PROMPT_VERSION=V3
export BLACKBOARD_PROJECT_NAME=CareSync
python3 app/main.py
```

Selon le modèle utilisé, il faut aussi configurer les variables de connexion LLM attendues par `app/llm.py`.

## Viewer Web POC

Le viewer web POC permet de consulter les runs existants sous
`outputs/tests/<Project>/version X/` depuis un navigateur.

Il permet aussi de soumettre un brief depuis le navigateur. La génération se
lance ensuite en background, avec un statut accessible sur `/jobs/<job_id>`.
Les jobs sont séparés par cookie `web_session_id` pour garder un historique par
session navigateur.

Il n'y a pas d'authentification, pas de comptes et pas de déploiement public
prévu à ce stade.

Le CLI standard continue de fonctionner avec `python3 app/main.py`, et la
logique de génération standard reste exposée par `app/generation_service.py`
pour réutilisation interne.

Si `WEB_ACCESS_TOKEN` est défini, ouvrir le viewer avec
`/?access_token=<token>` sur l'hôte visé. Après validation, l'application pose
un cookie local `web_access_granted`. Ce mécanisme n'est pas une authentification
complète et le lien ne doit pas être partagé publiquement.

### Déploiement Render POC

Render démarre l'app via `Procfile` et Gunicorn, avec un seul worker.
Le disque persistant doit fournir `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT`.
Si `WEB_ACCESS_TOKEN` est défini, l'URL d'accès initiale est
`https://<render-host>/?access_token=<token>`.
Ce POC reste en accès partagé, sans comptes ni authentification complète.

Pour le démarrer localement :

```bash
python3 app/web.py
```

Par défaut, le serveur écoute sur `http://127.0.0.1:8000`.
Pour un POC contrôlé sur le réseau local, utiliser :

```bash
WEB_HOST=0.0.0.0 python3 app/web.py
```

## Documents À Lire En Priorité

Pour auditer rapidement :
1. `README.md`
2. `outputs/tests/CareSync/version 1/prd.md`
3. `outputs/tests/CareSync/version 1/architecture.md`
4. `outputs/tests/CareSync/version 1/architecture-diagram.png`
5. `outputs/tests/CareSync/version 1/gtm.md`
6. `outputs/tests/CareSync/version 1/blackboard.md`
7. `app/orchestrator.py`

Pour comprendre le projet en profondeur :
- `outputs/rapport_final.md`
- `outputs/workflow.md`
- `outputs/dev-steps/step-final-codex.md`
