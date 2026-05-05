# Lot 06 - Extraction de l'ecriture des artefacts

## Objectif

Extraire l'ecriture des artefacts de `app/main.py` vers un module reutilisable,
sans changer le comportement du CLI existant.

Ce lot prepare l'etape 2 : un futur service pourra generer un run depuis un
brief en memoire sans dupliquer la logique d'ecriture `prd.md`,
`architecture.md`, `gtm.md`, `blackboard.md` et `activity_log.txt`.

## Contexte projet utile

- `app/main.py` contient actuellement deux responsabilites :
  - selectionner le brief et lancer le workflow CLI ;
  - formatter/ecrire les artefacts de sortie.
- L'ecriture des artefacts est aujourd'hui centralisee dans
  `_write_run_artifacts(...)`.
- Le futur `app/generation_service.py` devra reutiliser cette ecriture.
- Ne pas modifier le workflow Product/Growth/Tech.
- Ne pas lancer d'appel LLM dans ce lot.

## Fichiers autorises a modifier

- `app/main.py`
- `app/artifact_writer.py` a creer

## Fichiers a ne pas modifier

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

## Travail demande

1. Creer `app/artifact_writer.py`.
2. Deplacer depuis `app/main.py` vers `app/artifact_writer.py` toute la logique
   strictement liee au rendu/ecriture des artefacts, notamment :
   - `_format_block`
   - `_format_list_block`
   - `_format_expert_contribution`
   - `_format_readiness_block`
   - `_format_readiness_section`
   - `_format_expert_decisions_section`
   - `_format_artifacts_section`
   - `_format_product_locking_section`
   - `_format_product_arbitration_section`
   - `_format_tagged_items_block`
   - `_format_correction_loop_section`
   - `_format_correction_tasks_section`
   - `_format_readiness_history_section`
   - `_format_revision_block`
   - `_format_second_pass_block` si encore utilisee par le rendu blackboard
   - `_format_blackboard_markdown`
   - `_format_second_pass_blackboard_markdown` si encore utilisee
   - `_tag_decision_items`
   - `_write_run_artifacts`
3. Renommer `_write_run_artifacts` en fonction publique :

```python
def write_run_artifacts(
    output_dir: Path,
    blackboard: dict,
    project_brief_text: str,
    evaluator_report_text: str = "",
) -> None:
    ...
```

4. Garder les helpers de formatting prives dans `artifact_writer.py`.
5. Importer dans `artifact_writer.py` :
   - `render_architecture_diagram` depuis `architecture_render`
   - `group_tagged_items` et `render_tagged_item` depuis `readiness`
6. Mettre a jour `app/main.py` pour importer `write_run_artifacts` et l'utiliser
   a la place de `_write_run_artifacts`.
7. Ne pas changer le contenu des fichiers generes.
8. Ne pas changer l'ordre d'ecriture des artefacts.

## Contraintes d'import

Le repo fonctionne aujourd'hui comme script local avec :

```bash
python3 app/main.py
```

Ne pas casser ce mode.

Utiliser des imports coherents avec l'existant. Si necessaire, garder les imports
script-style dans les modules runtime, par exemple :

```python
from architecture_render import render_architecture_diagram
from readiness import group_tagged_items, render_tagged_item
```

Ne pas lancer une refonte globale des imports package-style dans ce lot.

## Comportements attendus

- `app/main.py` reste le point d'entree CLI.
- Le comportement standard de generation reste identique.
- `app/artifact_writer.py` ne lance jamais le workflow LLM.
- `app/artifact_writer.py` ne selectionne pas de brief.
- `outputs/tests/` n'est pas modifie pendant ce lot.

## Criteres d'acceptation

- `app/main.py` ne contient plus les gros helpers de formatting blackboard.
- `app/main.py` appelle `write_run_artifacts(...)`.
- `app/artifact_writer.py` contient la logique de formatting/ecriture.
- `python3 app/main.py` reste importable/executable du point de vue syntaxique.
- Aucun contrat blackboard n'est modifie.
- Aucun prompt n'est modifie.

## Validation

Executer :

```bash
python3 -m compileall app
python3 -c "import sys; sys.path.insert(0, 'app'); import main; print('main import ok')"
python3 -c "import sys; sys.path.insert(0, 'app'); import artifact_writer; print('artifact_writer import ok')"
```

Ne pas lancer `python3 app/main.py` dans ce lot sauf demande explicite, car cela
appelle les LLM et cree un nouveau run.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les changements mecaniques et limites.
- Ne pas modifier les outputs generes.
- Ne pas changer les prompts.
- Ne pas changer le workflow Product/Growth/Tech.
- Ne pas introduire de dependance.
