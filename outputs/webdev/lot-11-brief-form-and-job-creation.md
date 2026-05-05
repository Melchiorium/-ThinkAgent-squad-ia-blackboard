# Lot 11 - Formulaire de brief et creation de job

## Objectif

Ajouter un formulaire web pour coller un brief et créer un job `queued`, sans
lancer encore la génération en arrière-plan.

Ce lot branche l'UI à `app/web_jobs.py`, mais ne lance pas encore
`run_generation_from_brief(...)`.

## Contexte projet utile

- Le lot 10 fournit `app/web_jobs.py`.
- Le viewer existe déjà dans `app/web.py`.
- La page d'accueil liste les runs existants.
- L'étape 3 vise un POC simple, sans auth ni comptes.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/index.html`
- `app/static/web.css`

## Fichiers à ne pas modifier

- `app/generation_service.py`
- `app/web_jobs.py`, sauf ajustement mineur découvert pendant intégration
- `app/main.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/`
- `README.md`
- `outputs/tests/`

## Travail demandé

1. Importer dans `app/web.py` :
   - `create_job`
   - `create_session_id`
   - `list_jobs`
2. Ajouter une gestion simple du `session_id` par cookie.
3. Le cookie doit s'appeler :

```text
web_session_id
```

4. Si le cookie n'existe pas, générer un nouveau `session_id` et le poser dans
   la réponse.
5. Ajouter un formulaire sur `/` avec :
   - un `<textarea name="brief">`
   - un bouton de soumission
6. Ajouter une route :

```text
POST /jobs
```

7. `POST /jobs` doit :
   - récupérer le brief ;
   - faire `.strip()` ;
   - valider la taille ;
   - créer un job via `create_job(...)` ;
   - rediriger vers `/jobs/<job_id>`.
8. Ajouter une route provisoire :

```text
GET /jobs/<job_id>
```

Elle peut afficher seulement le statut du job et un lien retour. Le rendu
complet sera amélioré au lot 13.

## Validation du brief

Définir dans `app/web.py` :

```python
MAX_BRIEF_CHARACTERS = 50_000
```

Règles :

- brief vide : retourner `400` avec un message lisible ;
- brief au-delà de 50 000 caractères : retourner `400` ;
- aucun appel LLM ;
- aucun thread ;
- aucun fichier dans `outputs/tests/`.

## Interface attendue

Sur la page `/`, afficher :

- le formulaire de brief ;
- les runs existants ;
- une section "Mes jobs" listant les jobs de la session courante si présents.

Pour chaque job de session, afficher :

- job id ;
- status ;
- date de création ;
- lien vers `/jobs/<job_id>`.

L'interface peut rester simple et sobre.

## Comportements attendus

- Un navigateur sans cookie reçoit un `web_session_id`.
- Soumettre un brief crée un fichier JSON sous `outputs/web-jobs/`.
- Le job reste en status `queued`.
- La page d'accueil affiche les jobs de la session courante.
- Les autres sessions ne voient pas ces jobs dans "Mes jobs".

## Validation

Exécuter :

```bash
python3 -m compileall app
python3 - <<'PY'
from app.web import app

client = app.test_client()
home = client.get("/")
print(home.status_code)
print("web_session_id" in str(home.headers))

created = client.post("/jobs", data={"brief": "Project name: WebJob\n\nBrief"})
print(created.status_code)
print(created.headers.get("Location", ""))

empty = client.post("/jobs", data={"brief": "   "})
print(empty.status_code)
PY
```

Attendus :

```text
200
True
302
/jobs/<job_id>
400
```

## Critères d'acceptation

- `/` affiche un formulaire de brief.
- `POST /jobs` crée un job mais ne lance pas de génération.
- `GET /jobs/<job_id>` existe.
- Les jobs sont filtrés par session sur la page d'accueil.
- Aucun appel LLM n'est nécessaire pour valider ce lot.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas ajouter d'authentification.
- Ne pas brancher la génération dans ce lot.
- Ne pas modifier les prompts.
- Ne pas modifier les outputs générés.
