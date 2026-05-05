# Lot 07 - Service de generation reutilisable

## Objectif

Creer `app/generation_service.py`, un service Python reutilisable capable de
lancer le workflow standard depuis un brief texte en memoire.

Ce lot ne branche pas encore le service a l'interface web. Il cree seulement
l'API interne qui sera utilisee par les etapes suivantes.

## Contexte projet utile

- Le lot 06 doit avoir extrait `write_run_artifacts(...)` dans
  `app/artifact_writer.py`.
- Le workflow standard valide est `run_v0_flow(...)` dans `app/orchestrator.py`.
- Les sorties normales vont dans :

```text
outputs/tests/<Project Name>/version X/
```

- Le service doit eviter de passer par `outputs/projects/`.
- Le service recoit un brief deja en memoire.

## Fichiers autorises a modifier

- `app/generation_service.py` a creer

## Fichiers a ne pas modifier

- `app/main.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `app/web.py`
- `app/web_runs.py`
- `outputs/tests/`
- `docs/ai/`
- `README.md`
- `requirements.txt`

## API publique attendue

Creer une dataclass :

```python
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GenerationResult:
    project_name: str
    project_brief_source: str
    output_dir: Path
    blackboard: dict
```

Creer la fonction principale :

```python
from collections.abc import Callable
from pathlib import Path


def run_generation_from_brief(
    brief_text: str,
    project_brief_source: str = "web://brief",
    outputs_root: Path | None = None,
    evaluator_report_text: str = "",
    flow_runner: Callable[[str, str], dict] | None = None,
) -> GenerationResult:
    ...
```

## Comportement attendu

`run_generation_from_brief(...)` doit :

1. Normaliser `brief_text` avec `.strip()`.
2. Lever `ValueError("Project brief is empty.")` si le brief est vide.
3. Extraire le nom projet depuis la premiere ligne commencant par
   `Project name:`.
4. Si aucun nom projet n'est trouve, utiliser `"Untitled Project"`.
5. Creer le prochain dossier de version sous :

```text
<outputs_root or repo outputs>/tests/<Project Name>/version X/
```

6. Appeler le workflow standard :

```python
blackboard = flow_runner(brief_text, project_brief_source)
```

Si `flow_runner` vaut `None`, utiliser `run_v0_flow`.

7. Ecrire les artefacts via :

```python
write_run_artifacts(output_dir, blackboard, brief_text, evaluator_report_text)
```

8. Retourner `GenerationResult`.

## Helpers internes attendus

Ajouter des helpers simples :

```python
def extract_project_name(brief_text: str) -> str:
    ...

def next_project_version_outputs_dir(project_name: str, outputs_root: Path | None = None) -> Path:
    ...
```

`next_project_version_outputs_dir(...)` doit reprendre le comportement de
`app/main.py` :

- creer `outputs/tests/<Project Name>/` si necessaire ;
- detecter les dossiers `version X` ;
- creer `version <max + 1>` ;
- retourner le `Path` cree.

## Securite minimale du nom projet

Pour ce lot, rester simple :

- retirer les espaces en debut/fin ;
- interdire `/`, `\` et `..` dans le nom projet ;
- si le nom devient vide, utiliser `"Untitled Project"`.

Si un nom projet contient un separateur de chemin ou `..`, lever `ValueError`.

Ne pas ajouter de slugification complexe dans ce lot.

## Contraintes d'import

Le repo est encore script-oriented. Pour ne pas casser `python3 app/main.py`,
ne pas refondre tous les imports.

Dans `generation_service.py`, utiliser le meme style que `app/web.py` si
necessaire pour permettre l'import depuis la racine :

```python
if __package__ in {None, ""}:
    ...
else:
    ...
```

L'objectif est que ces deux commandes fonctionnent :

```bash
python3 -c "from app.generation_service import run_generation_from_brief; print(run_generation_from_brief)"
python3 -c "import sys; sys.path.insert(0, 'app'); import generation_service; print(generation_service.run_generation_from_brief)"
```

## Validation sans LLM

Ne pas lancer de vraie generation LLM dans ce lot.

Valider avec un `flow_runner` fake et un dossier temporaire sous `/private/tmp`
ou le dossier temporaire disponible :

```bash
python3 - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from app.generation_service import run_generation_from_brief

def fake_flow(brief, source):
    return {
        "project_brief": brief,
        "project_brief_source": source,
        "workflow_stage": "test",
        "source_version": "",
        "executive_evaluation": "",
        "artifacts": {},
        "readiness": {
            "product": {"status": "READY", "blocking_gaps": [], "required_improvements": []},
            "tech": {"status": "READY", "blocking_gaps": [], "required_improvements": []},
            "growth": {"status": "READY", "blocking_gaps": [], "required_improvements": []},
            "global": {"status": "READY", "blocking_gaps": [], "required_improvements": []},
            "known_tags": [],
            "loop_triggered": False,
            "loop_count": 0,
            "max_loops": 2,
            "history": [],
            "correction_tasks": [],
            "final_outcome": "READY",
        },
        "expert_decisions": {"tech": [], "growth": []},
        "product_locking": {"applied": False},
        "expert_contributions": {
            "tech": {"summary": "", "decisions": [], "recommendations": [], "risks": [], "open_questions": []},
            "growth": {"summary": "", "decisions": [], "recommendations": [], "risks": [], "open_questions": []},
        },
        "arbitration": {"source": "", "retained": [], "deferred": [], "rejected": [], "open_points": [], "rationales": [], "reconciliation_notes": [], "reconciled": {"warnings": []}},
        "source_artifacts": {"prd": ""},
        "revision_trace": {"initial_prd_draft": "", "tech_input": "", "growth_input": "", "revision_summary": ""},
        "retained_decisions": [],
        "deferred_decisions": [],
        "rejected_changes": [],
        "unresolved_tensions": [],
        "applied_changes": [],
        "open_points": [],
        "risks": [],
        "open_questions": [],
        "prd_draft": "# Test PRD",
        "architecture_notes": "# Test Architecture",
        "mermaid_diagram": "",
        "gtm_notes": "# Test GTM",
        "decisions": [],
        "conflicts": [],
        "activity_log": [],
    }

with TemporaryDirectory() as tmp:
    result = run_generation_from_brief(
        "Project name: ServiceTest\n\nBrief",
        outputs_root=Path(tmp),
        flow_runner=fake_flow,
    )
    print(result.project_name)
    print(result.output_dir.exists())
    print((result.output_dir / "prd.md").exists())
PY
```

Puis executer :

```bash
python3 -m compileall app
```

## Criteres d'acceptation

- `app/generation_service.py` existe.
- La fonction `run_generation_from_brief(...)` est importable.
- Une generation fake ecrit les artefacts dans un dossier temporaire.
- Aucun appel LLM n'est requis pour valider ce lot.
- `outputs/tests/` du repo n'est pas modifie pendant la validation.
- Aucun prompt n'est modifie.
- Aucun contrat blackboard n'est modifie.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le service petit et lisible.
- Ne pas brancher le web dans ce lot.
- Ne pas modifier les outputs generes.
- Ne pas changer le workflow Product/Growth/Tech.
- Ne pas introduire de dependance.
