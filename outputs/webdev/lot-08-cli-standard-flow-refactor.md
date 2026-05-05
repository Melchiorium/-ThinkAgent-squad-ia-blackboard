# Lot 08 - Refactor du CLI vers le service de generation

## Objectif

Faire utiliser `app/generation_service.py` par le chemin CLI standard de
`app/main.py`, tout en preservant le comportement existant.

Ce lot reduit la duplication entre CLI et futur web, sans toucher au second pass
experimental.

## Contexte projet utile

- Le lot 06 a extrait `write_run_artifacts(...)`.
- Le lot 07 a cree `run_generation_from_brief(...)`.
- `app/main.py` selectionne encore les briefs depuis `outputs/projects/`.
- Le mode second pass est historique/experimental et ne doit pas etre refondu
  ici.

## Fichiers autorises a modifier

- `app/main.py`
- `app/generation_service.py` seulement si un ajustement mineur est necessaire

## Fichiers a ne pas modifier

- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `app/web.py`
- `app/web_runs.py`
- `app/artifact_writer.py`, sauf si une incoherence bloquante est decouverte
- `outputs/tests/`
- `docs/ai/`
- `README.md`
- `requirements.txt`

## Travail demande

1. Dans `app/main.py`, conserver :
   - `_load_project_brief`
   - `_select_project_brief_path`
   - `_extract_project_name` si encore utile pour la selection CLI
   - `_normalize_name`
   - `_outputs_root`
   - `_load_second_pass_sources`
   - `_load_evaluator_report_if_any`
   - `_read_text_file`
   - `main`
2. Dans le chemin standard de `main()`, remplacer la sequence :

```python
project_brief, project_name, project_brief_source = _load_project_brief()
blackboard = run_v0_flow(project_brief, project_brief_source)
outputs_dir = _next_project_version_outputs_dir(project_name)
evaluator_report_text = _load_evaluator_report_if_any()
_write_run_artifacts(outputs_dir, blackboard, project_brief, evaluator_report_text)
```

par un appel a :

```python
run_generation_from_brief(
    project_brief,
    project_brief_source=project_brief_source,
    outputs_root=_outputs_root(),
    evaluator_report_text=evaluator_report_text,
)
```

3. Ne pas utiliser le `project_name` retourne par `_load_project_brief` pour
   creer le dossier si le service extrait deja le nom projet de la meme maniere.
4. Si necessaire pour conserver exactement le comportement CLI, ajuster le
   service pour accepter un `project_name_override: str | None = None`.
   Dans ce cas, `main.py` doit passer le `project_name` existant.
5. Ne pas modifier la branche second pass :

```python
if second_pass_sources is not None:
    ...
```

Elle peut continuer a utiliser `run_v2_flow(...)` et `write_run_artifacts(...)`
directement.

## Point d'attention important

Le CLI existant extrait le nom projet avec :

- premiere ligne `Project name:`
- sinon stem du fichier brief

Pour ne pas changer le comportement, preferer l'option suivante :

```python
run_generation_from_brief(..., project_name_override=project_name)
```

si le service du lot 07 ne reproduit pas exactement ce fallback fichier.

## Comportements attendus

- `python3 app/main.py` reste le point d'entree CLI.
- Le mode standard cree toujours une nouvelle version sous `outputs/tests/`.
- Le mode second pass n'est pas generalise dans ce lot.
- Le CLI ne duplique plus la sequence workflow + output dir + artifact writing.
- Aucun nouveau formulaire web n'est ajoute.

## Validation sans LLM

Executer :

```bash
python3 -m compileall app
python3 -c "import sys; sys.path.insert(0, 'app'); import main; print('main import ok')"
python3 -c "from app.generation_service import run_generation_from_brief; print('service import ok')"
```

Ne pas lancer `python3 app/main.py` sauf demande explicite, car cela cree un
nouveau run et appelle les LLM.

## Validation optionnelle avec LLM

Seulement si le mainteneur demande explicitement une validation runtime :

```bash
set -a; source .env; export BLACKBOARD_PROMPT_VERSION=V3; export BLACKBOARD_PROJECT_NAME=CareSync; set +a; python3 app/main.py
```

Cette commande cree un nouveau dossier `outputs/tests/CareSync/version X/`.

## Criteres d'acceptation

- Le chemin standard de `main()` utilise `run_generation_from_brief(...)`.
- Le second pass reste isole et non refondu.
- Les imports restent compatibles avec `python3 app/main.py`.
- Aucun prompt n'est modifie.
- Aucun contrat blackboard n'est modifie.
- `outputs/tests/` n'est pas modifie pendant les validations sans LLM.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Respecter le statut experimental du second pass.
- Ne pas changer les prompts.
- Ne pas modifier les outputs generes.
- Garder le refactor petit et reversible.
