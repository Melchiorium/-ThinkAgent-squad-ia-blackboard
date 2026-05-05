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

## Notes de sécurité

- Ne pas écrire la vraie connection string dans cette documentation.
- Ne pas committer de secret.
- Ne pas ajouter d'archivage automatique pour ce POC.
