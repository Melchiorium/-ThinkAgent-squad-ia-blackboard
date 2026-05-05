# Lot 13 - UI de statut job et historique de session

## Objectif

Rendre les jobs web lisibles pour l'utilisateur : page de statut, refresh simple,
lien vers le run généré, et historique de session sur la page d'accueil.

Ce lot ne change pas la logique de génération. Il améliore l'expérience POC.

## Contexte projet utile

- Le lot 10 fournit `app/web_jobs.py`.
- Le lot 11 ajoute le formulaire et les routes jobs.
- Le lot 12 lance la génération en background.
- Le viewer sait déjà afficher un run généré via `/runs/<project>/<version>`.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/index.html`
- `app/templates/job_status.html` à créer
- `app/static/web.css`

## Fichiers à ne pas modifier

- `app/generation_service.py`
- `app/web_jobs.py`, sauf helper d'affichage très mineur
- `app/main.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/`
- `README.md`
- `outputs/tests/`

## Travail demandé

1. Créer `app/templates/job_status.html`.
2. Mettre à jour `GET /jobs/<job_id>` pour rendre ce template.
3. La page job doit afficher :
   - job id ;
   - status ;
   - date de création ;
   - date de mise à jour ;
   - brief preview ;
   - erreur si `failed` ;
   - lien vers le run si `done`.
4. Si `status` est `queued` ou `running`, ajouter un refresh HTML simple :

```html
<meta http-equiv="refresh" content="3">
```

5. Si le job est `done` et contient `run_project` + `run_version`, afficher un
   lien :

```text
/runs/<run_project>/<run_version>
```

6. Si le job n'existe pas, retourner 404.
7. Sur `/`, afficher une section "Mes jobs" avec les jobs de la session courante.
8. Pour chaque job, afficher :
   - status ;
   - brief preview ;
   - lien statut ;
   - lien résultat si `done`.

## Contrôle de session

Pour ce POC :

- un utilisateur peut accéder à un job par son URL directe ;
- la page d'accueil filtre seulement par cookie de session ;
- ne pas ajouter d'authentification.

Ne pas transformer ce lot en système de permissions.

## Comportements attendus

- Après soumission d'un brief, l'utilisateur arrive sur `/jobs/<job_id>`.
- La page se rafraîchit pendant `queued`/`running`.
- En `done`, elle propose un lien vers le run.
- En `failed`, elle affiche l'erreur.
- La page d'accueil montre les jobs de la session.

## Validation sans LLM

Utiliser des jobs JSON créés manuellement via `app.web_jobs` ou monkeypatcher le
runner comme au lot 12.

Exécuter :

```bash
python3 -m compileall app
python3 - <<'PY'
from app.web import app
from app.web_jobs import create_job, update_job

job = create_job("Project name: StatusTest\n\nBrief", "manual-session")
update_job(job["job_id"], {
    "status": "done",
    "project_name": "StatusTest",
    "run_project": "StatusTest",
    "run_version": "version 1",
    "output_dir": "/tmp/status-test",
})

client = app.test_client()
response = client.get(f"/jobs/{job['job_id']}")
body = response.data.decode()
print(response.status_code)
print("StatusTest" in body)
print("/runs/StatusTest/version%201" in body or "/runs/StatusTest/version+1" in body)
PY
```

Attendus :

```text
200
True
True
```

Nettoyer manuellement le job de test si nécessaire.

## Critères d'acceptation

- `job_status.html` existe.
- `/jobs/<job_id>` affiche tous les statuts utiles.
- Les jobs running/queued se rafraîchissent automatiquement.
- Les jobs done renvoient vers le viewer de run.
- La page d'accueil liste les jobs de session.
- Aucun appel LLM n'est nécessaire pour valider l'UI.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'interface simple.
- Ne pas ajouter d'authentification.
- Ne pas modifier les prompts.
- Ne pas modifier les outputs générés manuellement.
