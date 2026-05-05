# Lot 27 - Champ titre projet dans l'interface web

## Objectif

Ajouter un champ `Titre du projet` dans l'interface web pour éviter les runs
créés sous `Untitled Project`.

Le titre saisi par l'utilisateur doit devenir la source de vérité pour le nom du
dossier de sortie web.

## Contexte projet utile

- `app/generation_service.py` supporte déjà `project_name_override`.
- `app/web.py` crée actuellement un job avec seulement `brief_text`.
- `app/web_jobs.py` stocke les jobs JSON.
- Le fallback actuel extrait uniquement une ligne `Project name:` du brief.
- Si cette ligne est absente, le projet devient `Untitled Project`.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_jobs.py`
- `app/templates/index.html`
- `app/templates/job_status.html`
- `app/static/web.css` seulement si nécessaire
- `README.md` seulement pour une note courte d'usage

## Fichiers à ne pas modifier

- `app/generation_service.py` sauf si un bug bloquant est découvert
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Interface attendue

Sur la home, le formulaire doit contenir :

```text
Titre du projet
Brief projet
[Lancer la génération]
```

Contraintes :

- `project_title` obligatoire ;
- longueur max recommandée : `120` caractères ;
- le brief reste obligatoire ;
- le placeholder du brief ne doit plus suggérer que l'utilisateur doit écrire
  `Project name: ...`.

## Backend attendu

Dans `POST /jobs` :

- lire `project_title = request.form.get("project_title", "").strip()` ;
- refuser si vide ;
- refuser si trop long ;
- refuser les titres invalides qui casseraient les chemins :
  - `/`
  - `\`
  - `..`
  - retours ligne et caractères de contrôle
- créer un job contenant `project_title`.

Dans `app/web_jobs.py` :

- ajouter `project_title` au JSON job ;
- ne pas casser les anciens jobs qui n'ont pas encore ce champ ;
- exposer `project_title` dans les vues job si présent.

Dans `_start_generation_job` / `_run_generation_runner` :

- appeler le runner avec `project_name_override=job["project_title"]` quand le
  runner le supporte ;
- continuer à passer `outputs_root` quand supporté ;
- garder la compatibilité avec les fake runners simples.

## Brief transmis aux agents

Pour que les agents voient aussi le titre, construire un brief effectif :

```text
Project name: <project_title>

<brief_text>
```

Règles :

- ne pas demander à l'utilisateur d'écrire lui-même `Project name:`;
- si le brief contient déjà une ligne `Project name:`, ne pas essayer de la
  parser dans ce lot ;
- le titre du champ web reste prioritaire pour le dossier de sortie.

## Comportements attendus

- Un titre `Yoyo` crée un run sous `outputs/tests/Yoyo/version X/`.
- Le job affiche le titre du projet dans la home et la page de suivi.
- Les nouveaux jobs ne deviennent plus `Untitled Project` quand le titre est
  renseigné.
- Les anciens jobs sans `project_title` restent lisibles.

## Critères d'acceptation

- Le formulaire contient un champ `project_title`.
- `POST /jobs` sans titre retourne `400`.
- `POST /jobs` sans brief retourne `400`.
- `POST /jobs` avec titre invalide retourne `400`.
- `POST /jobs` avec titre contenant un retour ligne retourne `400`.
- Le fake runner reçoit `project_name_override` quand il le supporte.
- Le dossier de sortie prend le nom du titre saisi.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); r=c.get('/'); text=r.get_data(as_text=True); print(r.status_code); print('Titre du projet' in text)"
python3 -c "from app.web import app; c=app.test_client(); print(c.post('/jobs', data={'brief':'Brief seul'}).status_code); print(c.post('/jobs', data={'project_title':'Yoyo'}).status_code)"
git diff -- app/web.py app/web_jobs.py app/templates/index.html app/templates/job_status.html app/static/web.css README.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Validation fake runner recommandée :

- remplacer `generation_runner` en test par un fake acceptant
  `project_name_override`;
- poster `project_title=Yoyo` et un brief ;
- vérifier que le job passe à `done` ;
- vérifier que le run pointe vers `Yoyo/version 1`.

Ne pas lancer de vraie génération LLM sans accord explicite.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la modification simple et modulaire.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux runs générés existants.
