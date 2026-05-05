# Lot 01 - Inventaire des runs existants

## Objectif

Créer une couche Python simple et lisible pour inventorier les runs déjà générés
dans `outputs/tests/<Project>/version X/`.

Ce lot ne crée pas d'interface web. Il prépare uniquement une API Python interne
qui sera utilisée par les lots suivants.

## Contexte projet utile

- Le projet est un pipeline Python local.
- Les runs générés sont des dossiers en lecture seule sous `outputs/tests/`.
- Le format normal d'un run est :

```text
outputs/tests/<Project>/version X/
```

- Les fichiers utilisateurs principaux sont :
  - `project-brief.md`
  - `prd.md`
  - `architecture.md`
  - `architecture-diagram.mmd`
  - `architecture-diagram.png`
  - `gtm.md`
  - `blackboard.md`
  - `activity_log.txt`

## Fichiers autorisés à modifier

- `app/web_runs.py` à créer.

## Fichiers à ne pas modifier

- `app/main.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `outputs/tests/`
- `docs/ai/`
- `README.md`
- `requirements.txt`

## Travail demandé

1. Créer `app/web_runs.py`.
2. Définir une constante lisible pour les fichiers attendus :

```python
EXPECTED_RUN_FILES = [
    "project-brief.md",
    "prd.md",
    "architecture.md",
    "architecture-diagram.mmd",
    "architecture-diagram.png",
    "gtm.md",
    "blackboard.md",
    "activity_log.txt",
]
```

3. Exposer la fonction publique suivante :

```python
from pathlib import Path


def list_runs(outputs_root: Path | None = None) -> list[dict]:
    ...
```

4. Quand `outputs_root` est `None`, utiliser le dossier `outputs/` du repo.
5. Lire uniquement `outputs/tests/<Project>/version X/`.
6. Ignorer les fichiers parasites comme `.DS_Store`.
7. Ignorer les dossiers qui ne respectent pas le format `version X`.
8. Trier les résultats par projet puis par numéro de version croissant.

## Structure attendue d'un run

Chaque élément retourné par `list_runs()` doit être un dictionnaire simple :

```python
{
    "project": "CareSync",
    "version": "version 1",
    "version_number": 1,
    "path": "/absolute/path/to/outputs/tests/CareSync/version 1",
    "files": {
        "prd.md": True,
        "architecture.md": True,
        ...
    },
    "missing_files": ["..."],
    "has_architecture_png": True,
}
```

Contraintes :
- `path` doit être une chaîne, pas un objet `Path`, pour rester facile à rendre
  dans des templates web.
- `files` doit contenir une clé pour chaque fichier de `EXPECTED_RUN_FILES`.
- `missing_files` doit contenir uniquement les fichiers attendus absents.
- `has_architecture_png` vaut `True` seulement si `architecture-diagram.png`
  existe et est un fichier.

## Comportements attendus

- Si `outputs/tests/` n'existe pas, retourner une liste vide.
- Si un projet ne contient aucun dossier `version X`, ne rien retourner pour ce
  projet.
- Ne jamais créer, modifier ou supprimer de fichiers dans `outputs/tests/`.
- Ne pas lire le contenu des fichiers Markdown. Ce lot inventorie seulement les
  chemins et présences de fichiers.

## Critères d'acceptation

- `list_runs()` retourne les runs existants du repo.
- Les projets actuels comme `CareSync`, `LocalLoop`, `Melody`, `SkillBridge`
  apparaissent si présents dans `outputs/tests/`.
- Les fichiers parasites ne provoquent pas d'erreur.
- Le module est suffisamment simple pour être relu par un développeur Python
  intermédiaire.

## Validation

Exécuter :

```bash
python3 -m compileall app
python3 -c "from app.web_runs import list_runs; print(list_runs())"
```

La deuxième commande doit afficher une liste de dictionnaires et ne doit pas
lever d'exception.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas scanner le repo aveuglément.
- Lire uniquement les fichiers utiles au lot.
- Garder le code simple, lisible et modulaire.
- Ne pas modifier les runs générés.
- Ne pas changer les contrats blackboard.
- Ne pas changer les prompts.
