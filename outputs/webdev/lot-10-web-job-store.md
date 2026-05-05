# Lot 10 - Store de jobs web et sessions POC

## Objectif

Ajouter une couche simple de suivi des jobs web, persistée en fichiers JSON,
sans lancer encore de génération LLM.

Ce lot prépare l'étape 3 : chaque navigateur aura un `session_id`, et chaque
brief soumis créera un job traçable.

## Contexte projet utile

- Le viewer Flask existe dans `app/web.py`.
- Le service de génération existe dans `app/generation_service.py`.
- L'étape 3 ajoute le formulaire de brief et des jobs simples.
- Pas d'authentification ni de comptes utilisateurs.
- Les sessions servent seulement à séparer l'historique visible par navigateur.

## Fichiers autorisés à modifier

- `app/web_jobs.py` à créer

## Fichiers à ne pas modifier

- `app/web.py`
- `app/templates/`
- `app/static/`
- `app/generation_service.py`
- `app/main.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/`
- `README.md`
- `outputs/tests/`

## API publique attendue

Créer `app/web_jobs.py` avec ces constantes :

```python
JOB_STATUSES = {"queued", "running", "done", "failed"}
DEFAULT_WEB_JOBS_DIRNAME = "web-jobs"
```

Créer les fonctions suivantes :

```python
from pathlib import Path


def create_session_id() -> str:
    ...


def create_job(
    brief_text: str,
    session_id: str,
    jobs_root: Path | None = None,
) -> dict:
    ...


def get_job(job_id: str, jobs_root: Path | None = None) -> dict | None:
    ...


def update_job(job_id: str, updates: dict, jobs_root: Path | None = None) -> dict:
    ...


def list_jobs(
    session_id: str | None = None,
    jobs_root: Path | None = None,
) -> list[dict]:
    ...
```

## Structure JSON attendue

Chaque job doit être stocké dans :

```text
outputs/web-jobs/<job_id>.json
```

Structure minimale :

```json
{
  "job_id": "20260505-153000-abc12345",
  "session_id": "20260505-153000-def67890",
  "status": "queued",
  "created_at": "2026-05-05T15:30:00Z",
  "updated_at": "2026-05-05T15:30:00Z",
  "brief_text": "Project name: ...",
  "brief_preview": "Project name: ...",
  "project_name": "",
  "output_dir": "",
  "error": ""
}
```

Contraintes :
- `job_id` et `session_id` doivent être courts, lisibles et uniques.
- Utiliser UTC en ISO simple pour les timestamps.
- `brief_preview` doit être tronqué à 200 caractères.
- `status` doit toujours appartenir à `JOB_STATUSES`.
- `update_job(...)` doit refuser un status inconnu avec `ValueError`.

## Résolution des chemins

Par défaut, les jobs vont dans :

```text
<repo>/outputs/web-jobs/
```

Si `jobs_root` est fourni, l'utiliser directement. Cela permet les tests dans
un dossier temporaire.

Ne jamais écrire dans `outputs/tests/` dans ce lot.

## Comportements attendus

- Si `outputs/web-jobs/` n'existe pas, le créer.
- `create_job(...)` écrit immédiatement un fichier JSON.
- `get_job(...)` retourne `None` si le job n'existe pas.
- `list_jobs(session_id=...)` filtre les jobs de cette session.
- `list_jobs()` retourne les jobs triés par `created_at` décroissant.
- Ce module ne dépend pas de Flask.
- Ce module ne lance aucun thread et aucun appel LLM.

## Validation

Exécuter :

```bash
python3 -m compileall app
python3 - <<'PY'
from tempfile import TemporaryDirectory
from pathlib import Path
from app.web_jobs import create_job, get_job, list_jobs, update_job

with TemporaryDirectory() as tmp:
    root = Path(tmp)
    job = create_job("Project name: JobTest\n\nBrief", "session-1", jobs_root=root)
    print(job["status"])
    print(get_job(job["job_id"], jobs_root=root)["session_id"])
    update_job(job["job_id"], {"status": "running"}, jobs_root=root)
    print(get_job(job["job_id"], jobs_root=root)["status"])
    print(len(list_jobs("session-1", jobs_root=root)))
PY
```

Attendus :

```text
queued
session-1
running
1
```

## Critères d'acceptation

- `app/web_jobs.py` existe.
- Les jobs sont persistés en JSON.
- Les sessions peuvent être créées sans Flask.
- Le module est testable sans LLM.
- Aucun output de run n'est modifié.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le module autonome et simple.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux runs générés.
