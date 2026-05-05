# Lot 35 - Schema et contrat storage Supabase

## Objectif

Créer la base documentaire et contractuelle pour utiliser Supabase Postgres
comme mémoire persistante du viewer web.

Ce lot ne doit pas brancher Flask sur Supabase. Il prépare le schéma, les
variables, les conventions et, si utile, un squelette de module storage.

## Contexte projet utile

- Le viewer web existe déjà dans `app/web.py`.
- Les jobs web sont actuellement stockés en JSON via `app/web_jobs.py`.
- Les runs sont actuellement découverts dans `outputs/tests/` via
  `app/web_runs.py`.
- Render gratuit peut exécuter le POC, mais son stockage fichier est éphémère.
- La mémoire long terme retenue est Supabase Postgres, sans Supabase Auth et
  sans Supabase Storage.
- Le dev n'a pas besoin de `SUPABASE_DATABASE_URL` pour ce lot.

## Fichiers autorisés à modifier

- `docs/supabase-schema.sql`
- `docs/supabase-poc-storage.md`
- `app/web_storage.py` seulement si un squelette contractuel aide les lots
  suivants

## Fichiers à ne pas modifier

- `app/web.py`
- `app/web_jobs.py`
- `app/web_runs.py`
- `app/generation_service.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules` et `flows`
   concernant `web`, `web_jobs`, `web_runs` et `generation_service`.
2. Créer `docs/supabase-schema.sql` avec le SQL obligatoire ci-dessous.
3. Créer `docs/supabase-poc-storage.md` pour expliquer la stratégie de
   persistance.
4. Si un squelette `app/web_storage.py` est créé, il doit uniquement définir le
   contrat prévu, sans remplacer le stockage actuel.
5. Ne pas ajouter de dépendance Python dans ce lot.
6. Ne pas modifier les routes Flask.

## SQL obligatoire

```sql
create table if not exists web_jobs (
  job_id text primary key,
  session_id text not null,
  status text not null,
  created_at timestamptz not null,
  updated_at timestamptz not null,
  brief_text text not null,
  brief_preview text not null,
  project_title text not null default '',
  project_name text not null default '',
  output_dir text not null default '',
  run_project text not null default '',
  run_version text not null default '',
  error text not null default ''
);

create table if not exists web_run_artifacts (
  run_project text not null,
  run_version text not null,
  version_number integer not null,
  filename text not null,
  content_text text,
  content_bytes bytea,
  content_type text not null,
  created_at timestamptz not null default now(),
  primary key (run_project, run_version, filename)
);

create index if not exists web_run_artifacts_run_idx
on web_run_artifacts (run_project, version_number);
```

## Comportements attendus

- `WEB_STORAGE_BACKEND=file|supabase` est la variable de sélection prévue.
- Si `WEB_STORAGE_BACKEND` est absent, le backend futur doit rester `file`.
- `SUPABASE_DATABASE_URL` est la seule variable de connexion Supabase prévue.
- Supabase est utilisé uniquement comme Postgres serveur-side.
- Pas de Supabase Auth.
- Pas de Supabase Storage.
- Pas d'archivage automatique.
- Aucun secret ne doit être écrit dans la documentation.

## Critères d'acceptation

- `docs/supabase-schema.sql` existe et contient le schéma complet.
- `docs/supabase-poc-storage.md` explique clairement comment Supabase sera
  utilisé.
- La documentation indique que les tests Supabase réels sont conditionnels à
  `SUPABASE_DATABASE_URL`.
- Le comportement web actuel n'est pas modifié par ce lot.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/supabase-schema.sql docs/supabase-poc-storage.md app/web_storage.py
git diff -- app/web.py app/web_jobs.py app/web_runs.py
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Utiliser la mémoire `docs/ai` pour cibler les fichiers utiles.
- Garder le design simple, lisible et modulaire.
- Ne pas deviner de secrets ou de paramètres Supabase.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Préserver les outputs générés.
