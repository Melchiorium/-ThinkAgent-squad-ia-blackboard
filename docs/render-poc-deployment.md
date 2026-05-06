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

- utiliser `GET /readyz` pour le contrôle manuel de readiness avant audit ;
- quand `WEB_ACCESS_TOKEN` est défini, ouvrir `/readyz` avec le même token que
  l'application ;

- garder un seul process / worker pour ce POC ;
- ne pas activer de scaling horizontal ;
- ne pas créer de base de données ;
- ne pas créer de Redis ;
- ne pas ajouter de `render.yaml`.

## Mode Render éphémère

Ce mode sert au smoke test et au POC gratuit sans mémoire persistante.

Configurer uniquement dans le dashboard Render :

```text
OPENAI_API_KEY=<secret>
BLACKBOARD_PROMPT_VERSION=V3
WEB_ACCESS_TOKEN=<token fort>
```

Options de stockage :

- `WEB_STORAGE_BACKEND=file` ;
- `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT` peuvent rester absentes ;
- si besoin, les chemins locaux temporaires peuvent rester éphémères.

Règles :

- ne jamais écrire la vraie clé API dans la doc ;
- utiliser un token fort pour `WEB_ACCESS_TOKEN` ;
- l'URL initiale d'accès est :

```text
https://<render-host>/?access_token=<WEB_ACCESS_TOKEN>
```

- `.env` reste réservé au lancement local.

## Mode Render gratuit + Supabase

C'est le mode persistant recommandé quand on ne veut pas de disque Render
payant.

Configurer :

```text
OPENAI_API_KEY=<secret>
BLACKBOARD_PROMPT_VERSION=V3
WEB_ACCESS_TOKEN=<token fort>
WEB_STORAGE_BACKEND=supabase
SUPABASE_DATABASE_URL=<connection string>
```

- `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT` ne sont pas requis ;
- ne pas définir `WEB_OUTPUTS_ROOT` ;
- ne pas définir `WEB_JOBS_ROOT` ;
- les jobs vivent dans `web_jobs` ;
- les artefacts vivent dans `web_run_artifacts` ;
- la procédure complète est dans
  [docs/supabase-poc-storage.md](docs/supabase-poc-storage.md).

### Avant redeploy

1. vérifier que `WEB_STORAGE_BACKEND=supabase` est bien défini ;
2. vérifier que `SUPABASE_DATABASE_URL` pointe vers la Session Pooler ;
3. vérifier que `WEB_ACCESS_TOKEN` est présent ;
4. vérifier que `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT` ne sont pas définis ;
5. lancer `python3 scripts/check_web_storage.py` si un contrôle local est
   nécessaire.

### Après redeploy

1. ouvrir `/healthz` ;
2. ouvrir `/readyz` avec le token configuré ;
3. vérifier que le run le plus récent reste listé ;
4. rouvrir le run et vérifier que le contenu inline reste lisible ;
5. noter tout écart sans documenter de secret.

## Disque persistant Render

Ce mode est payant et n'est pas retenu comme chemin de base du POC gratuit.
Si on l'utilise malgré tout, monter le disque sur :

```text
/var/data
```

Puis configurer :

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

Test exécuté le 2026-05-05 sur `https://squadia.onrender.com/` avec le mode
Render éphémère.

Résultats :

- `/healthz` : `200 OK` ;
- `/readyz` : `200 OK` avec backend `file` ;
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
