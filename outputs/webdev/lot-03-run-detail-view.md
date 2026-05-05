# Lot 03 - Page detail d'un run

## Objectif

Afficher dans le navigateur le contenu lisible d'un run existant :
brief, PRD, architecture, Mermaid, GTM, blackboard et activity log.

Ce lot transforme le viewer en outil d'audit simple, sans ajouter de génération.

## Contexte projet utile

- Le lot 01 fournit l'inventaire des runs.
- Le lot 02 fournit le shell Flask et la page d'accueil.
- Les routes doivent retrouver un run depuis l'inventaire, pas depuis un chemin
  brut fourni par l'utilisateur.
- Les fichiers générés doivent rester en lecture seule.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/index.html`
- `app/templates/run_detail.html` à créer
- `app/static/web.css`
- `app/web_runs.py` uniquement si une petite fonction de recherche de run est
  nécessaire.

## Fichiers à ne pas modifier

- `app/main.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `outputs/tests/`
- `docs/ai/`
- `README.md`
- `requirements.txt`, sauf si Flask n'a pas encore été ajouté au lot 02.

## Travail demandé

1. Ajouter une route Flask :

```text
GET /runs/<project>/<version>
```

2. La route doit retrouver le run correspondant via l'inventaire de
   `app/web_runs.py`.
3. Ne pas construire un chemin directement à partir des paramètres URL sans
   vérifier qu'il correspond à un run inventorié.
4. Créer `app/templates/run_detail.html`.
5. Afficher les sections suivantes :
   - `Brief`
   - `PRD`
   - `Architecture`
   - `Diagramme Mermaid`
   - `GTM`
   - `Blackboard`
   - `Activity Log`
6. Lire les fichiers suivants si présents :

```text
project-brief.md
prd.md
architecture.md
architecture-diagram.mmd
gtm.md
blackboard.md
activity_log.txt
```

7. Si un fichier est absent, afficher :

```text
Fichier absent.
```

8. Utiliser un rendu simple avec `<pre>` pour préserver la lisibilité et éviter
   d'ajouter une dépendance Markdown.
9. Mettre à jour la page d'accueil pour que les liens vers les détails
   fonctionnent.

## Comportements attendus

- Un run existant s'affiche sans erreur.
- Un run inconnu retourne une page 404 propre ou une erreur Flask 404.
- Les contenus Markdown sont affichés lisiblement.
- Les longs fichiers comme `blackboard.md` restent scrollables et lisibles.
- Le viewer ne doit jamais modifier un fichier de run.

## Critères d'acceptation

- Depuis `/`, cliquer sur `CareSync / version 1` ouvre la page détail.
- `prd.md`, `architecture.md`, `gtm.md` et `blackboard.md` sont visibles.
- `architecture-diagram.mmd` est visible sous forme de texte.
- Un fichier manquant n'entraîne pas d'erreur serveur.
- Les paramètres URL ne permettent pas de lire un fichier hors d'un run
  inventorié.

## Validation

Exécuter :

```bash
python3 -m compileall app
python3 app/web.py
```

Puis vérifier manuellement :

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/runs/CareSync/version%201
```

Vérifier que les sections principales sont remplies.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas scanner `outputs/` largement.
- Lire uniquement les fichiers du run demandé.
- Garder le code simple et facile à relire.
- Ne pas changer le workflow Product/Growth/Tech.
- Ne pas changer les prompts ou les contrats parser.
