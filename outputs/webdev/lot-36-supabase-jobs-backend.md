# Lot 36 - Backend Supabase pour jobs

## Objectif

Rendre la persistance des jobs web compatible Supabase Postgres, tout en
gardant le backend fichier comme comportement par défaut.

Ce lot concerne uniquement les jobs. Il ne doit pas encore persister les
artefacts de run.

## Contexte projet utile

- `app/web.py` crée, lit et met à jour les jobs web.
- `app/web_jobs.py` stocke actuellement les jobs dans des fichiers JSON.
- Le backend `file` doit rester inchangé pour le local et pour les tests sans
  Supabase.
- Le backend `supabase` doit utiliser la table `web_jobs` définie dans
  `docs/supabase-schema.sql`.
- Le dev n'a pas besoin de `SUPABASE_DATABASE_URL` pour coder. Les tests réels
  Supabase sont conditionnels à la présence de cette variable.

## Fichiers autorisés à modifier

- `requirements.txt`
- `app/web_jobs.py`
- `app/web_storage.py`
- `app/web.py` seulement pour injecter ou résoudre le backend
- `docs/supabase-poc-storage.md` seulement si un détail d'usage doit être
  corrigé

## Fichiers à ne pas modifier

- `app/generation_service.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules` et `flows`
   concernant `web`, `web_jobs` et `web_generation_job_flow`.
2. Ajouter `psycopg[binary]` dans `requirements.txt`.
3. Introduire une résolution de backend basée sur `WEB_STORAGE_BACKEND`.
4. Conserver `file` comme défaut quand `WEB_STORAGE_BACKEND` est absent.
5. Implémenter les opérations jobs côté Supabase :
   - `create_job`
   - `get_job`
   - `update_job`
   - `list_jobs`
6. Lire uniquement `SUPABASE_DATABASE_URL` pour se connecter à Supabase.
7. Si `WEB_STORAGE_BACKEND=supabase` et que `SUPABASE_DATABASE_URL` manque,
   lever une erreur claire.
8. Ne pas afficher la connection string dans les erreurs ou logs.

## Comportements attendus

- `WEB_STORAGE_BACKEND=file` garde le comportement JSON actuel.
- `WEB_STORAGE_BACKEND` absent équivaut à `file`.
- `WEB_STORAGE_BACKEND=supabase` utilise la table `web_jobs`.
- Les champs actuels du job sont conservés :
  - `job_id`
  - `session_id`
  - `status`
  - `created_at`
  - `updated_at`
  - `brief_text`
  - `brief_preview`
  - `project_title`
  - `project_name`
  - `output_dir`
  - `run_project`
  - `run_version`
  - `error`
- Les statuts acceptés restent :
  - `queued`
  - `running`
  - `done`
  - `failed`
- Les jobs listés par session doivent respecter `session_id`.
- Les timestamps restent lisibles par l'interface existante.

## Critères d'acceptation

- Le backend fichier passe toujours les validations existantes.
- Le backend Supabase est sélectionnable par variable d'environnement.
- L'absence de `SUPABASE_DATABASE_URL` en mode Supabase produit une erreur
  explicite et sans secret.
- Aucun artefact de run n'est encore persisté dans ce lot.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
WEB_STORAGE_BACKEND=file python3 -m gunicorn --check-config app.web:app
git diff -- requirements.txt app/web_jobs.py app/web_storage.py app/web.py docs/supabase-poc-storage.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Validation Supabase réelle seulement si la variable est disponible :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 -m gunicorn --check-config app.web:app
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas demander de secret à l'utilisateur pour implémenter.
- Ne pas committer de secret.
- Garder le backend fichier opérationnel.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Préserver les outputs générés.
