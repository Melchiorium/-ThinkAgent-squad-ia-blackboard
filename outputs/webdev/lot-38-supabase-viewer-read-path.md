# Lot 38 - Lecture viewer depuis Supabase

## Objectif

Faire lire l'interface web depuis Supabase quand
`WEB_STORAGE_BACKEND=supabase`, tout en conservant le backend fichier actuel.

Ce lot raccorde la home, le suivi de job, le détail de run et les artefacts au
backend storage actif.

## Contexte projet utile

- `app/web.py` contient les routes Flask du viewer.
- `app/web_runs.py` liste actuellement les runs à partir du filesystem.
- `app/web_jobs.py` ou `app/web_storage.py` gère les jobs selon les lots
  précédents.
- Les templates affichent déjà les sections via `_run_result.html`.
- La sécurité artefact existe déjà via allowlist de filename.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_storage.py`
- `app/web_jobs.py` si nécessaire
- `app/web_runs.py` si nécessaire
- `app/templates/` seulement si le format de données l'impose

## Fichiers à ne pas modifier

- `app/generation_service.py`
- `app/artifact_writer.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules` et `flows`
   concernant `web`, `web_jobs`, `web_runs` et `web_unified_generation_ui_flow`.
2. Ajouter dans le storage actif les opérations nécessaires pour :
   - lister les runs ;
   - retrouver un run précis ;
   - lire les sections d'un run ;
   - lire un artefact autorisé.
3. Modifier `app/web.py` pour utiliser ces opérations en mode Supabase.
4. Garder le chemin fichier actuel en mode `file`.
5. Conserver les routes publiques existantes.
6. Ne pas exposer `outputs/` comme dossier statique global.

## Comportements attendus

- `/` liste les jobs et les runs depuis Supabase en mode `supabase`.
- `/jobs/<job_id>` affiche le statut et le résultat inline depuis Supabase.
- `/api/jobs/<job_id>` lit le job depuis Supabase.
- `/runs/<project>/<version>` lit les sections depuis Supabase.
- `/runs/<project>/<version>/artifacts/<filename>` sert l'artefact depuis
  Supabase.
- Les fichiers texte sont rendus comme avant.
- Le PNG Mermaid est servi avec `image/png` s'il existe.
- Si le PNG est absent, afficher le message existant d'image absente.
- En mode `file`, le viewer fonctionne comme avant.

## Règles de sécurité à conserver

- Autoriser uniquement les fichiers attendus.
- Refuser tout filename contenant `/`.
- Refuser tout filename contenant `\`.
- Refuser tout filename contenant `..`.
- Ne jamais servir un chemin brut fourni par l'utilisateur.
- Ne jamais exposer `outputs/` comme dossier statique global.

## Critères d'acceptation

- Backend `file` inchangé.
- Backend `supabase` lit jobs, runs et artefacts depuis Postgres.
- Le détail d'un run Supabase affiche PRD, Architecture, Mermaid, GTM,
  Blackboard et Activity Log quand ils existent.
- Les artefacts inconnus ou dangereux sont refusés.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
WEB_STORAGE_BACKEND=file python3 -m gunicorn --check-config app.web:app
git diff -- app/web.py app/web_storage.py app/web_jobs.py app/web_runs.py app/templates
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Validation Supabase réelle seulement si la variable est disponible :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 -m gunicorn --check-config app.web:app
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas réécrire l'interface au-delà du besoin de lecture Supabase.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
- Ne pas écrire ou afficher de secret.
