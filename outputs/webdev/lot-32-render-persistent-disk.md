# Lot 32 - Disque persistant Render

## Objectif

Documenter la configuration du disque persistant Render pour que les runs et les
jobs survivent aux redémarrages ou redeploys.

Ce lot ne doit pas changer le stockage fichier actuel.

## Contexte projet utile

- `WEB_OUTPUTS_ROOT` configure la racine des outputs web.
- `WEB_JOBS_ROOT` configure le stockage JSON des jobs web.
- L'app supporte déjà :

```text
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

- Le POC reste sans base de données, sans Redis et sans queue distribuée.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md`
- `README.md` seulement si un renvoi court est nécessaire
- `docs/ai/flows.yaml`

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `requirements.txt`
- `Procfile`
- `render.yaml`

## Travail demandé

Dans `docs/render-poc-deployment.md`, ajouter une section :

```text
Disque persistant
```

Elle doit indiquer :

- créer un persistent disk Render ;
- mount path recommandé :

```text
/var/data
```

- variables à configurer :

```text
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

- les runs seront écrits sous :

```text
/var/data/outputs/tests/<Project>/version X/
```

- les jobs seront écrits sous :

```text
/var/data/web-jobs/
```

## Vérification de persistance

Documenter un test manuel :

1. lancer une génération courte ;
2. ouvrir le résultat ;
3. redeploy ou restart le service Render ;
4. rouvrir la home avec token ;
5. vérifier que le run reste listé ;
6. rouvrir le run et vérifier que PRD/Architecture/GTM sont encore visibles.

## Critères d'acceptation

- La doc indique clairement le mount path `/var/data`.
- La doc indique les deux variables `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT`.
- La doc explique le test de persistance après restart/redeploy.
- Aucun changement de code applicatif.
- Aucun stockage externe ajouté.
- Aucun prompt ou contrat blackboard modifié.

## Commandes de validation

```bash
python3 -m compileall app
grep -n "/var/data" docs/render-poc-deployment.md
grep -n "WEB_OUTPUTS_ROOT=/var/data/outputs" docs/render-poc-deployment.md
grep -n "WEB_JOBS_ROOT=/var/data/web-jobs" docs/render-poc-deployment.md
test ! -f render.yaml
git diff -- docs/render-poc-deployment.md README.md docs/ai/flows.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas modifier le stockage fichier existant.
- Ne pas ajouter Redis, Celery ou base de données.
- Ne pas créer de `render.yaml`.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.

