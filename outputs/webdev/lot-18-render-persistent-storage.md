# Lot 18 - Racines de stockage configurables pour Render

## Objectif

Permettre au viewer web et aux jobs de génération d'utiliser un disque
persistant Render, au lieu d'écrire uniquement dans le dossier `outputs/` du
repo.

Ce lot reste un POC : stockage fichier, pas de base de données, pas de queue
externe.

## Contexte projet utile

- Les runs générés sont lus depuis `outputs/tests/<Project>/version X/`.
- `app/web_runs.py` accepte déjà un `outputs_root`.
- `app/generation_service.py` accepte déjà un `outputs_root`.
- `app/web_jobs.py` accepte déjà un `jobs_root`.
- `app/web.py` utilise aujourd'hui les defaults locaux pour l'inventaire et la
  génération.
- Sur Render, les fichiers écrits dans le repo ne doivent pas être considérés
  comme persistants. Il faut prévoir une racine configurable, typiquement
  `/var/data/outputs`.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_jobs.py` seulement si nécessaire pour clarifier le default
- `README.md` seulement si une note courte de configuration est nécessaire

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `Procfile`
- `requirements.txt`

## Variables d'environnement à supporter

Ajouter ou confirmer le support de :

```text
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

Règles :

- `WEB_OUTPUTS_ROOT` configure la racine qui contient `tests/`.
- Si `WEB_OUTPUTS_ROOT` est absent, garder le default local actuel :
  `<repo>/outputs`.
- `WEB_JOBS_ROOT` configure le dossier des jobs JSON.
- Si `WEB_JOBS_ROOT` est absent mais `WEB_OUTPUTS_ROOT` est défini, utiliser par
  défaut `<WEB_OUTPUTS_ROOT>/web-jobs`.
- Si les deux sont absents, garder le default local actuel :
  `<repo>/outputs/web-jobs`.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `docs/ai/modules.yaml` pour les modules `web`, `web_runs`,
   `web_jobs`, `generation_service`.
3. Ajouter dans `app/web.py` un helper simple :

```python
def _outputs_root() -> Path:
    configured_root = os.getenv("WEB_OUTPUTS_ROOT", "").strip()
    if configured_root:
        return Path(configured_root)
    return Path(__file__).resolve().parent.parent / "outputs"
```

4. Utiliser `_outputs_root()` pour :
   - `list_runs(outputs_root=_outputs_root())`
   - `get_run(project, version, outputs_root=_outputs_root())`
   - `generation_runner(..., outputs_root=_outputs_root())`

5. Adapter `_jobs_root()` pour dériver son default depuis `_outputs_root()` quand
   `WEB_JOBS_ROOT` n'est pas défini.
6. Garder les tests et validations sans appel LLM.
7. Ne pas créer de migration automatique d'anciens fichiers.

## Attention compatibilité tests

`generation_runner` peut être remplacé dans des tests par une fonction de
simulation. Si des tests existants ou nouveaux utilisent un fake runner simple,
ne pas casser inutilement cette possibilité.

Approche acceptable :

- appeler le runner avec `outputs_root=_outputs_root()` ;
- ou ajouter une petite fonction interne qui supporte proprement les runners
  compatibles et les fakes simples.

Garder le code lisible.

## Comportements attendus

- En local sans variable d'environnement, le comportement reste identique.
- Avec `WEB_OUTPUTS_ROOT=/tmp/demo-outputs`, le viewer lit
  `/tmp/demo-outputs/tests/`.
- Avec `WEB_OUTPUTS_ROOT=/tmp/demo-outputs`, les nouveaux runs sont créés sous
  `/tmp/demo-outputs/tests/<Project>/version X/`.
- Avec `WEB_JOBS_ROOT=/tmp/demo-jobs`, les jobs JSON sont écrits sous
  `/tmp/demo-jobs`.
- Si seul `WEB_OUTPUTS_ROOT` est défini, les jobs vont sous
  `<WEB_OUTPUTS_ROOT>/web-jobs`.

## Critères d'acceptation

- Aucun chemin Render n'est hardcodé dans le code.
- Le default local reste compatible avec les lots précédents.
- `WEB_OUTPUTS_ROOT` affecte l'inventaire, le détail run, les artefacts et la
  génération.
- `WEB_JOBS_ROOT` garde la priorité pour les jobs.
- Aucun contrat blackboard n'est modifié.
- Aucun prompt n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; print(app.test_client().get('/').status_code)"
WEB_OUTPUTS_ROOT=/tmp/squad-web-outputs python3 -c "from app.web import _outputs_root, _jobs_root; print(_outputs_root()); print(_jobs_root())"
WEB_OUTPUTS_ROOT=/tmp/squad-web-outputs WEB_JOBS_ROOT=/tmp/squad-web-jobs python3 -c "from app.web import _outputs_root, _jobs_root; print(_outputs_root()); print(_jobs_root())"
git diff -- app/web.py app/web_jobs.py
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Validation manuelle sans LLM :

1. Créer temporairement un dossier `/tmp/squad-web-outputs/tests/Demo/version 1/`.
2. Y placer au moins `prd.md`.
3. Lancer :

```bash
WEB_OUTPUTS_ROOT=/tmp/squad-web-outputs python3 app/web.py
```

4. Vérifier que le run `Demo / version 1` apparaît.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Utiliser les modules existants au lieu d'inventer une nouvelle couche.
- Garder le stockage fichier simple.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les prompts.
- Ne pas toucher à l'historique généré.
