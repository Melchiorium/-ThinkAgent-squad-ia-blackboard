# Supabase POC Storage

Cette note décrit le mode persistant recommandé pour le viewer web quand le
filesystem Render est éphémère.

## Règle de base

- `WEB_STORAGE_BACKEND` choisit le backend de stockage.
- La valeur par défaut reste `file`.
- `supabase` active Postgres côté serveur via `psycopg[binary]`.
- Il n'y a ni Supabase Auth ni Supabase Storage.
- `SUPABASE_DATABASE_URL` est la seule chaîne de connexion attendue.

## Schéma

Le schéma SQL à exécuter dans Supabase est dans :

```text
docs/supabase-schema.sql
```

Il crée :

- `web_jobs` pour la file des jobs web ;
- `web_run_artifacts` pour les artefacts persistés d'un run.

La migration reste additive. Les colonnes de progression sont ajoutées sans
supprimer les anciennes données et sans casser les jobs déjà présents :

- `progress_stage`
- `progress_label`
- `progress_detail`
- `progress_order`
- `progress_total`
- `progress_blocks`
- `progress_events`
- `progress_started_at`
- `progress_last_event_at`
- `progress_timeout_seconds`
- `progress_error_type`
- `progress_error_message`

## Procédure

1. créer un projet Supabase ;
2. ouvrir le SQL Editor ;
3. exécuter `docs/supabase-schema.sql` ;
4. récupérer la connection string Session Pooler ;
5. configurer Render avec :

```text
WEB_STORAGE_BACKEND=supabase
SUPABASE_DATABASE_URL=<connection string>
OPENAI_API_KEY=<secret>
BLACKBOARD_PROMPT_VERSION=V3
WEB_ACCESS_TOKEN=<token fort>
```

6. redeployer le service Render ;
7. lancer une génération courte ;
8. vérifier le résultat inline ;
9. redeployer à nouveau ;
10. vérifier que le run et ses artefacts restent visibles.

Avant redeploy, vérifier :

- `WEB_STORAGE_BACKEND=supabase` ;
- `SUPABASE_DATABASE_URL` ;
- `WEB_ACCESS_TOKEN` ;
- absence de `WEB_OUTPUTS_ROOT` ;
- absence de `WEB_JOBS_ROOT`.

Après redeploy, vérifier :

- `/readyz` avec token renvoie `200` ;
- le run récent reste listé ;
- les artefacts restent lisibles ;
- aucun secret n'apparaît dans l'UI ou les logs.

## Détails opérationnels

- Le backend fichier reste le comportement par défaut pour le local.
- En mode `supabase`, les jobs sont lus et écrits dans `web_jobs`.
- En mode `supabase`, les artefacts de run sont persister dans
  `web_run_artifacts`.
- `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT` ne sont pas requis pour le mode
  Render gratuit + Supabase.
- Pour les tests locaux ou éphémères, le backend fichier peut rester sur un
  répertoire temporaire ou `/tmp`.

## Validation sans LLM

Le script de vérification du backend est :

```text
scripts/check_web_storage.py
```

Il crée un job `Storage Check`, passe par les états `queued`, `running`, `done`,
sauve des artefacts fake et relit ensuite le job, les runs et un artefact.

## Préflight production

Avant un déploiement durable, vérifier dans cet ordre :

1. `WEB_STORAGE_BACKEND=supabase` est bien défini ;
2. `SUPABASE_DATABASE_URL` est présente ;
3. `python3 scripts/check_web_storage.py` renvoie `Storage validation passed.`
   ;
4. `GET /readyz` renvoie `200` avec le même `WEB_ACCESS_TOKEN` que
   l'application et confirme que `web_jobs` et `web_run_artifacts` sont
   accessibles ;
5. aucun secret n'apparaît dans les logs, dans la page de readiness ou dans la
   documentation.

## Avertissement RLS

Supabase affiche parfois le warning `New tables will not have Row Level
Security enabled` après la création des tables. C'est attendu pour ce POC
backend-only.

- l'application utilise une connexion Postgres serveur via
  `SUPABASE_DATABASE_URL` ;
- elle n'utilise pas les clés frontend `anon` ou `authenticated` ;
- `SUPABASE_DATABASE_URL` ne doit jamais être exposée au navigateur ;
- ne pas activer ni modifier RLS sans lot dédié et sans valider d'abord
  `/readyz` et `python3 scripts/check_web_storage.py`.

## Notes de sécurité

- Ne pas écrire la vraie connection string dans cette documentation.
- Ne pas committer de secret.
- Ne pas ajouter d'archivage automatique pour ce POC.
