# Lot 31 - Checklist création service Render

## Objectif

Créer une checklist opérationnelle pour créer manuellement le service Render.

Render n'existe pas encore. Ce lot doit permettre à un humain ou à un agent
d'accompagner la création du service sans décision restante.

## Contexte projet utile

- Le déploiement Render est manuel via dashboard.
- Ne pas créer de `render.yaml`.
- Le repo contient déjà un `Procfile`.
- L'app doit rester un POC à un seul process/worker.
- Le `.env` local ne sert pas en ligne.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md`
- `README.md`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml` seulement si un nouveau document doit être référencé

## Fichiers à ne pas modifier

- `app/`
- `Procfile`
- `requirements.txt`
- `scripts/run_web.sh`
- `render.yaml`
- `Dockerfile`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Travail demandé

Créer ou mettre à jour :

```text
docs/render-poc-deployment.md
```

La doc doit contenir une checklist courte couvrant :

- créer un `Web Service` Render ;
- connecter le repo GitHub ;
- build command :

```bash
pip install -r requirements.txt
```

- start command : utiliser le `Procfile` ;
- confirmer que le `Procfile` lance :

```text
gunicorn app.web:app --bind 0.0.0.0:$PORT --workers 1 --threads 4
```

- healthcheck path :

```text
/healthz
```

- instance : un seul process/worker pour ce POC ;
- ne pas activer de scaling horizontal ;
- ne pas créer de base de données ;
- ne pas créer de Redis ;
- ne pas créer de `render.yaml`.

## Variables Render obligatoires

Documenter les variables suivantes :

```text
OPENAI_API_KEY=<secret>
BLACKBOARD_PROMPT_VERSION=V3
WEB_ACCESS_TOKEN=<token fort>
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

Règles :

- ne jamais écrire la vraie clé API dans la doc ;
- recommander un token fort pour `WEB_ACCESS_TOKEN` ;
- expliquer que l'URL initiale sera :

```text
https://<render-host>/?access_token=<WEB_ACCESS_TOKEN>
```

## README

Ajouter un lien court depuis la section `Viewer Web POC` vers
`docs/render-poc-deployment.md`.

Ne pas dupliquer toute la checklist dans le README.

## Critères d'acceptation

- `docs/render-poc-deployment.md` existe.
- La checklist permet de créer le service Render sans choix implicite.
- Le README référence la checklist.
- La doc distingue clairement `.env` local et variables Render.
- Aucun `render.yaml` n'est ajouté.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
test -f docs/render-poc-deployment.md
grep -n "WEB_ACCESS_TOKEN" docs/render-poc-deployment.md
grep -n "/healthz" docs/render-poc-deployment.md
test ! -f render.yaml
git diff -- README.md docs/render-poc-deployment.md docs/ai/flows.yaml docs/ai/modules.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la documentation courte et actionnable.
- Ne pas créer de `render.yaml`.
- Ne pas modifier le code applicatif.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.

