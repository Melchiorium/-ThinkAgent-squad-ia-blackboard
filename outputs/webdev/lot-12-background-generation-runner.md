# Lot 12 - Runner background pour generation

## Objectif

Brancher les jobs web à `run_generation_from_brief(...)` avec un thread Python
simple, en limitant l'exécution à un seul job à la fois.

Ce lot transforme un job `queued` en vraie génération, mais reste volontairement
minimal : pas de Redis, pas de Celery, pas de base de données.

## Contexte projet utile

- Le lot 10 fournit le store JSON des jobs.
- Le lot 11 crée les jobs depuis le formulaire.
- L'étape 2 fournit `app/generation_service.py`.
- Les générations appellent les LLM et peuvent durer longtemps.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_jobs.py` si nécessaire pour ajouter des helpers d'update

## Fichiers à ne pas modifier

- `app/generation_service.py`, sauf bug bloquant d'intégration
- `app/artifact_writer.py`
- `app/main.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `app/templates/`, sauf besoin minimal d'affichage du statut
- `docs/ai/`
- `README.md`
- `outputs/tests/` manuellement

## Travail demandé

1. Dans `app/web.py`, importer :

```python
from threading import Lock, Thread
```

2. Ajouter un verrou global :

```python
generation_lock = Lock()
```

3. Ajouter une fonction privée :

```python
def _start_generation_job(job_id: str) -> None:
    ...
```

4. `POST /jobs` doit créer le job puis démarrer un thread daemon :

```python
Thread(target=_start_generation_job, args=(job["job_id"],), daemon=True).start()
```

5. `_start_generation_job(...)` doit :
   - charger le job ;
   - si le job n'existe pas, arrêter ;
   - acquérir `generation_lock` ;
   - passer le job en `running` ;
   - appeler `run_generation_from_brief(...)` avec :

```python
brief_text=job["brief_text"]
project_brief_source=f"web://job/{job_id}"
```

   - à succès, passer le job en `done` avec :
     - `project_name`
     - `output_dir`
     - `run_project`
     - `run_version`
   - à erreur, passer le job en `failed` avec un message dans `error`.

## Dérivation run_project / run_version

Après succès, `GenerationResult.output_dir` pointe vers :

```text
outputs/tests/<Project>/version X/
```

Extraire :

```python
run_project = output_dir.parent.name
run_version = output_dir.name
```

Ces champs permettront de créer un lien vers :

```text
/runs/<run_project>/<run_version>
```

## Comportement du verrou

- Un seul job doit exécuter la génération à la fois dans le process Flask.
- Les autres jobs peuvent rester `queued` jusqu'à ce que leur thread obtienne le
  verrou.
- Ne pas implémenter une vraie queue persistante dans ce lot.

## Gestion d'erreur

En cas d'exception :

- ne pas planter le serveur Flask ;
- écrire `status = "failed"` ;
- écrire `error = str(error)` ;
- mettre à jour `updated_at`.

Ne pas masquer complètement l'erreur : le POC doit être auditable.

## Validation sans LLM

Pour éviter un vrai appel LLM, prévoir une manière de monkeypatcher ou injecter
le runner en test manuel simple.

Option attendue :

- dans `app/web.py`, définir une variable module :

```python
generation_runner = run_generation_from_brief
```

- `_start_generation_job(...)` appelle `generation_runner(...)`.

Validation :

```bash
python3 -m compileall app
python3 - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
import time

import app.web as web

with TemporaryDirectory() as tmp:
    def fake_runner(brief_text, project_brief_source):
        class Result:
            project_name = "Fake"
            output_dir = Path(tmp) / "outputs" / "tests" / "Fake" / "version 1"
        Result.output_dir.mkdir(parents=True)
        return Result()

    web.generation_runner = fake_runner
    client = web.app.test_client()
    client.get("/")
    response = client.post("/jobs", data={"brief": "Project name: Fake\n\nBrief"})
    print(response.status_code)
    location = response.headers["Location"]
    time.sleep(0.2)
    job_id = location.rsplit("/", 1)[-1]
    job = web.get_job(job_id)
    print(job["status"])
PY
```

Attendu :

```text
302
done
```

Si le test doit éviter d'écrire dans `outputs/web-jobs/`, ajuster le code pour
que `jobs_root` soit injectable proprement avant validation.

## Validation avec LLM

Ne pas lancer de vraie génération LLM sauf demande explicite du mainteneur.

## Critères d'acceptation

- Soumettre un brief démarre une génération en thread.
- Le job passe par `running`.
- À succès, le job finit en `done` avec `run_project` et `run_version`.
- À erreur, le job finit en `failed` avec `error`.
- Un seul job tourne à la fois dans le process.
- Le serveur Flask ne plante pas si la génération échoue.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le runner simple.
- Ne pas ajouter Redis/Celery/base de données.
- Ne pas modifier les prompts.
- Ne pas modifier le workflow Product/Growth/Tech.
