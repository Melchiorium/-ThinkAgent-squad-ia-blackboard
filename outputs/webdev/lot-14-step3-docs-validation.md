# Lot 14 - Documentation et validation de l'etape 3

## Objectif

Documenter l'étape 3 : soumission de brief depuis le web, jobs simples,
session navigateur et génération background.

Ce lot doit rester documentaire. Il ne modifie pas le code applicatif.

## Contexte projet utile

- Le viewer web existe depuis l'étape 1.
- Le service de génération existe depuis l'étape 2.
- L'étape 3 ajoute :
  - formulaire de brief ;
  - jobs JSON sous `outputs/web-jobs/` ;
  - cookie `web_session_id` ;
  - thread background ;
  - page de statut job.
- Il n'y a toujours pas d'authentification, pas de comptes et pas de déploiement
  Render dans cette étape.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une nouvelle règle de prévention est
  vraiment nécessaire

## Fichiers à ne pas modifier

- `app/`
- `docs/ai/contracts.yaml`
- `app/prompts V3/`
- `outputs/tests/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`
- `requirements.txt`

## Travail demandé - README

Mettre à jour la section `Viewer Web POC` pour refléter l'état réel :

- le viewer permet toujours de consulter les runs existants ;
- il permet maintenant de soumettre un brief ;
- la génération se lance en background ;
- le statut est visible sur `/jobs/<job_id>` ;
- les jobs sont séparés par session navigateur via cookie ;
- il n'y a pas d'authentification ni de comptes ;
- ce n'est pas encore une version déployée publiquement.

Ne pas réécrire le README complet.

## Travail demandé - modules.yaml

Ajouter le module :

```yaml
- name: web_jobs
  path: app/web_jobs.py
  role: >
    File-backed job store for the POC web generation flow. Persists submitted
    briefs, statuses, session ids, output links, and errors under outputs/web-jobs/.
  read_when:
    - changing web job persistence
    - changing session job history
    - debugging queued/running/done/failed state
  key_functions:
    - create_session_id
    - create_job
    - get_job
    - update_job
    - list_jobs
```

Mettre à jour l'entrée `web` pour mentionner aussi :

- formulaire de brief ;
- `POST /jobs` ;
- page `/jobs/<job_id>` ;
- lancement background simple ;
- historique de session.

Ne pas enlever les informations déjà présentes sur le viewer et les artefacts.

## Travail demandé - flows.yaml

Ajouter un flux :

```yaml
web_generation_job_flow:
  owner: app/web.py and app/web_jobs.py
  status: poc_generation
  steps:
    - ensure a browser session id cookie exists
    - accept a project brief from the web form
    - create a queued JSON job under outputs/web-jobs/
    - start a daemon thread for generation
    - run one generation at a time with a process-local lock
    - update the job to running, done, or failed
    - link done jobs to /runs/<project>/<version>
  limitations:
    - no authentication
    - no user accounts
    - no persistent distributed queue
    - no retry system
    - one-process POC only
```

Mettre à jour `web_viewer_flow` seulement si nécessaire pour clarifier qu'il est
la partie lecture du web POC.

## Travail demandé - rules.yaml

Ne modifier `docs/ai/rules.yaml` que si une règle est nécessaire. Si oui, ajouter
une règle courte du type :

```yaml
- Web generation jobs are a POC mechanism. Do not replace them with Redis,
  Celery, auth, or a database unless explicitly requested.
```

Si ce niveau de règle semble trop lourd, ne pas modifier `rules.yaml`.

## Validation

Exécuter :

```bash
python3 -m compileall app
git diff -- README.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Attendus :

- compile OK ;
- README modifié de façon ciblée ;
- `web_jobs` documenté dans `modules.yaml` ;
- `web_generation_job_flow` documenté dans `flows.yaml` ;
- aucun diff sur `contracts.yaml` ;
- aucun diff sur les prompts V3.

## Vérification manuelle recommandée

Si les lots 10 à 13 sont implémentés :

```bash
python3 app/web.py
```

Puis vérifier :

1. ouvrir `/` ;
2. soumettre un brief court ;
3. voir `/jobs/<job_id>` ;
4. observer le passage vers `done` ou `failed` ;
5. si `done`, ouvrir le run généré ;
6. vérifier que les runs existants restent visibles.

Ne lancer cette vérification que si les variables LLM sont configurées et si le
mainteneur accepte la création d'un nouveau run.

## Critères d'acceptation

- La documentation correspond à l'état réel de l'étape 3.
- Elle ne promet pas d'authentification.
- Elle ne promet pas un déploiement Render.
- Elle ne décrit pas une architecture Redis/Celery.
- Elle garde le POC simple et auditable.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs factuelles.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
