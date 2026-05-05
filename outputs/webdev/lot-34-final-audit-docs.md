# Lot 34 - Documentation finale audit web

## Objectif

Aligner README, mémoire `docs/ai` et TODO après le premier test web Render
réussi.

Ce lot est le dernier lot de clôture du MVP web déployé.

## Contexte projet utile

- Le MVP web local est opérationnel.
- Le service Render est créé manuellement.
- Le disque persistant est configuré.
- Un smoke test réel doit avoir été exécuté.
- Le vocabulaire technique `job`, `run`, `outputs/tests` peut rester dans la
  documentation technique.

## Fichiers autorisés à modifier

- `README.md`
- `docs/render-poc-deployment.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une règle courte est utile
- `TODO.md`

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`
- `render.yaml`

## Travail README

Ajouter ou ajuster une courte section :

```text
Tester en ligne
```

Elle doit indiquer :

- l'app Render est accessible via l'URL du service ;
- l'accès initial utilise `?access_token=<token>` ;
- ne pas publier le token ;
- le test utilisateur consiste à saisir titre + brief et lire le résultat ;
- la checklist détaillée est dans `docs/render-poc-deployment.md`.

Ne pas écrire de secrets.

## Travail docs/render-poc-deployment.md

Vérifier que la doc contient :

- création service Render ;
- variables d'environnement ;
- disque persistant ;
- smoke test ;
- test de persistance ;
- limites POC :
  - pas d'auth complète ;
  - pas de comptes ;
  - pas de queue distribuée ;
  - un seul process/worker.

## Travail docs/ai

Mettre à jour si nécessaire :

- `docs/ai/flows.yaml`
  - préciser que `web_render_poc_deployment_flow` inclut un smoke test déployé ;
  - ajouter un flux `web_render_smoke_test_flow` si utile.

- `docs/ai/modules.yaml`
  - vérifier que `web`, `web_jobs`, `web_local_launcher` restent exacts ;
  - référencer `docs/render-poc-deployment.md` si la mémoire liste les docs clés.

- `docs/ai/rules.yaml`
  - ne pas ajouter de règle sauf risque nouveau.

## Travail TODO

Garder uniquement les suites hors MVP :

- granularité des étapes ;
- Growth et Tech en parallèle ;
- manipulation noeuds/prompts ;
- amélioration UI avancée si souhaitée ;
- risque résiduel sur chemins absolus dans certains `blackboard.md` générés si
  toujours applicable.

Retirer les TODO devenus faux ou clos.

## Critères d'acceptation

- README explique comment tester en ligne sans secret.
- `docs/render-poc-deployment.md` contient la checklist complète et le résultat
  du smoke test.
- `docs/ai` reflète le flux web déployé.
- TODO ne contient que les suites réellement restantes.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- README.md docs/render-poc-deployment.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml TODO.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs courtes, factuelles et utiles.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.

