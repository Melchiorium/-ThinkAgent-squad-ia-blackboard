# Lot 04 - Service securise des artefacts

## Objectif

Servir proprement les artefacts autorisés d'un run, notamment
`architecture-diagram.png`, sans exposer tout le dossier `outputs/`.

Ce lot ajoute l'affichage du PNG Mermaid dans la page détail.

## Contexte projet utile

- Le lot 03 affiche déjà les contenus texte.
- Les PNG Mermaid sont générés conditionnellement par `app/architecture_render.py`.
- Les fichiers de run sont sous `outputs/tests/<Project>/version X/`.
- L'app ne doit jamais accepter un chemin arbitraire fourni par l'utilisateur.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/run_detail.html`
- `app/static/web.css`
- `app/web_runs.py` uniquement si nécessaire pour centraliser la liste des
  fichiers autorisés.

## Fichiers à ne pas modifier

- `app/main.py`
- `app/orchestrator.py`
- `app/architecture_render.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `outputs/tests/`
- `docs/ai/`
- `README.md`

## Travail demandé

1. Ajouter une route Flask :

```text
GET /runs/<project>/<version>/artifacts/<filename>
```

2. Retrouver le run via l'inventaire, comme dans le lot 03.
3. Refuser tout `filename` qui contient :
   - `/`
   - `\`
   - `..`
4. Autoriser uniquement les fichiers attendus d'un run :

```text
project-brief.md
prd.md
architecture.md
architecture-diagram.mmd
architecture-diagram.png
gtm.md
blackboard.md
activity_log.txt
```

5. Refuser tout fichier absent ou non listé.
6. Servir les fichiers avec `send_from_directory()` ou une approche Flask
   équivalente qui reste confinée au dossier du run.
7. Ne pas déclarer `outputs/` comme dossier statique Flask.
8. Dans `run_detail.html`, afficher l'image `architecture-diagram.png` si elle
   est présente.
9. Si le PNG est absent, afficher une mention sobre :

```text
Image Mermaid absente.
```

## Comportements attendus

- Les artefacts autorisés d'un run peuvent être servis.
- Le PNG Mermaid s'affiche sur la page détail.
- Les chemins invalides sont refusés.
- Les extensions ou noms inconnus sont refusés.
- Une tentative de traversal ne doit jamais lire un fichier hors run.

## Critères d'acceptation

- Cette URL fonctionne si le fichier existe :

```text
/runs/CareSync/version%201/artifacts/architecture-diagram.png
```

- Cette tentative est refusée :

```text
/runs/CareSync/version%201/artifacts/../README.md
```

- Cette tentative est refusée :

```text
/runs/CareSync/version%201/artifacts/random.py
```

- La page détail affiche le PNG si `architecture-diagram.png` existe.

## Validation

Exécuter :

```bash
python3 -m compileall app
python3 app/web.py
```

Puis vérifier manuellement :

```text
http://127.0.0.1:8000/runs/CareSync/version%201
http://127.0.0.1:8000/runs/CareSync/version%201/artifacts/architecture-diagram.png
```

Vérifier aussi les cas refusés :

```text
http://127.0.0.1:8000/runs/CareSync/version%201/artifacts/random.py
http://127.0.0.1:8000/runs/CareSync/version%201/artifacts/..%2FREADME.md
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas exposer largement les dossiers générés.
- Ne pas modifier les fichiers dans `outputs/tests/`.
- Garder la sécurité chemin simple et explicite.
- Ne pas introduire de dépendance inutile.
- Ne pas toucher au pipeline de génération.
