# Déploiement Render POC

Document court pour créer et vérifier le viewer web sur Render.

## Checklist de création

- créer un `Web Service` Render ;
- connecter le dépôt GitHub ;
- définir la build command :

```bash
pip install -r requirements.txt
```

- définir la start command via le `Procfile` ;
- confirmer que le `Procfile` lance :

```text
gunicorn app.web:app --bind 0.0.0.0:$PORT --workers 1 --threads 4
```

- configurer le healthcheck sur :

```text
/healthz
```

- garder un seul process / worker pour ce POC ;
- ne pas activer de scaling horizontal ;
- ne pas créer de base de données ;
- ne pas créer de Redis ;
- ne pas ajouter de `render.yaml`.

## Variables d'environnement Render

Configurer uniquement dans le dashboard Render :

```text
OPENAI_API_KEY=<secret>
BLACKBOARD_PROMPT_VERSION=V3
WEB_ACCESS_TOKEN=<token fort>
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

Règles :

- ne jamais écrire la vraie clé API dans la doc ;
- utiliser un token fort pour `WEB_ACCESS_TOKEN` ;
- l'URL initiale d'accès est :

```text
https://<render-host>/?access_token=<WEB_ACCESS_TOKEN>
```

- `.env` reste réservé au lancement local.

## Disque persistant

Créer un persistent disk Render et le monter sur :

```text
/var/data
```

Configurer ensuite :

```text
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

Avec ce montage :

- les runs sont écrits sous `/var/data/outputs/tests/<Project>/version X/` ;
- les jobs sont écrits sous `/var/data/web-jobs/`.

### Vérification de persistance

Test manuel recommandé :

1. lancer une génération courte ;
2. ouvrir le résultat ;
3. redeployer ou redémarrer le service Render ;
4. rouvrir la home avec token ;
5. vérifier que le run reste listé ;
6. rouvrir le run et vérifier que PRD, Architecture et GTM restent visibles.

## Smoke test

Test exécuté le 2026-05-05 sur `https://squadia.onrender.com/`.

Résultats :

- `/healthz` : `200 OK` ;
- `/` sans token : refusé avec `403` ;
- `/` avec `?access_token=<token>` : home visible ;
- run créé : `Yoyo Web Test` ;
- job : `20260505-192718-6062fba6` ;
- statut final : `Terminé` ;
- résultat inline : PRD, Architecture, Mermaid, GTM, Brief, Blackboard et Activity Log visibles ;
- artefact Mermaid PNG : absent, avec source `.mmd` disponible ;
- le run apparaît dans la liste des générations de session et dans les dossiers générés existants.

## Limites POC

- pas d'authentification complète ;
- pas de comptes ;
- pas de queue distribuée ;
- pas de scaling horizontal ;
- un seul process / worker ;
- pas de `render.yaml`.
