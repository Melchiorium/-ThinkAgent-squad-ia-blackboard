# Lot 05 - Documentation et validation de l'etape 1

## Objectif

Documenter le viewer web POC et mettre à jour la mémoire projet pour que les
futurs agents sachent que l'étape 1 existe.

Ce lot ne doit pas ajouter de nouvelle fonctionnalité web. Il documente l'état
réel après les lots 01 à 04.

## Contexte projet utile

- Le viewer web POC est uniquement un lecteur de runs existants.
- Il ne lance aucun appel LLM.
- Il ne propose aucun formulaire de brief.
- Il ne crée aucun job background.
- Les fichiers générés restent sous `outputs/tests/<Project>/version X/`.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`

## Fichiers à ne pas modifier

- `app/main.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `outputs/tests/`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`, sauf si une vraie nouvelle règle de prévention est
  nécessaire.

## Travail demandé

1. Mettre à jour `README.md` avec une section courte :

```text
## Viewer Web POC
```

2. Cette section doit expliquer :
   - le viewer sert à consulter les runs existants ;
   - il ne lance pas de génération ;
   - il se démarre avec `python3 app/web.py` ;
   - il écoute par défaut sur `http://127.0.0.1:8000` ;
   - `WEB_HOST=0.0.0.0` permet une utilisation réseau pour un POC contrôlé.

3. Mettre à jour `docs/ai/modules.yaml` pour ajouter :
   - `web`
   - `web_runs`

4. Pour `web`, documenter :
   - chemin : `app/web.py`
   - rôle : serveur Flask du viewer POC
   - quand lire : changement des routes web, templates, affichage artefacts.

5. Pour `web_runs`, documenter :
   - chemin : `app/web_runs.py`
   - rôle : inventaire des runs sous `outputs/tests/`
   - quand lire : changement de la découverte de runs ou fichiers affichés.

6. Mettre à jour `docs/ai/flows.yaml` avec un flux :

```yaml
web_viewer_flow:
  owner: app/web.py
  status: poc_viewer
  steps:
    - list generated runs from outputs/tests/
    - render run list on /
    - render selected run artifacts on /runs/<project>/<version>
    - serve only allowlisted artifacts from the selected run
  limitations:
    - no brief submission
    - no LLM generation
    - no background jobs
    - no authentication
```

7. Ne pas modifier `docs/ai/contracts.yaml`, car le blackboard contract ne
   change pas.
8. Ne pas documenter la future génération web dans cette étape.

## Comportements attendus

- La documentation décrit uniquement ce qui existe après l'étape 1.
- La mémoire `docs/ai` permet à un agent de trouver les modules web sans scanner
  le repo.
- Le README reste lisible pour un humain qui veut lancer le POC.
- La documentation ne promet pas de fonctionnalité non implémentée.

## Critères d'acceptation

- `README.md` contient une section claire sur le viewer web POC.
- `docs/ai/modules.yaml` référence `app/web.py` et `app/web_runs.py`.
- `docs/ai/flows.yaml` contient `web_viewer_flow`.
- Aucun contrat blackboard n'a été modifié.
- Aucun prompt n'a été modifié.

## Validation

Exécuter :

```bash
python3 -m compileall app
```

Vérification manuelle :

```text
1. La page d'accueil est accessible.
2. Les runs existants sont listés.
3. Le détail d'un run est lisible.
4. Le PNG Mermaid s'affiche si présent.
5. Un chemin invalide est refusé.
6. README.md correspond au comportement réel.
7. docs/ai/modules.yaml et docs/ai/flows.yaml sont cohérents.
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Mettre à jour la mémoire projet quand un nouveau module ou flux existe.
- Ne pas changer les contrats si les données blackboard ne changent pas.
- Ne pas documenter une fonctionnalité future comme si elle existait.
- Garder les explications claires, concises et pratiques.
