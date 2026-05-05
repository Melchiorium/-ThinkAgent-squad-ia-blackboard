# Lot 02 - Shell Flask du viewer

## Objectif

Créer l'application Flask minimale du viewer web avec une page d'accueil qui
liste les runs existants.

Ce lot ne doit pas encore afficher le contenu détaillé des fichiers d'un run.
Il doit seulement rendre une page d'accueil navigable.

## Contexte projet utile

- Le lot 01 doit fournir `app/web_runs.py` et `list_runs()`.
- L'étape 1 du POC est uniquement un viewer.
- Aucun appel LLM ne doit être lancé.
- Aucun formulaire de brief ne doit être ajouté.
- Les runs existants restent en lecture seule.

## Fichiers autorisés à modifier

- `requirements.txt`
- `app/web.py` à créer
- `app/templates/index.html` à créer
- `app/static/web.css` à créer

## Fichiers à ne pas modifier

- `app/main.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `outputs/tests/`
- `docs/ai/`
- `README.md`

## Travail demandé

1. Ajouter `flask` dans `requirements.txt`.
2. Créer `app/web.py`.
3. Créer le dossier `app/templates/` si nécessaire.
4. Créer `app/templates/index.html`.
5. Créer le dossier `app/static/` si nécessaire.
6. Créer `app/static/web.css`.
7. Dans `app/web.py`, exposer une app Flask nommée `app`.
8. Ajouter une route :

```text
GET /
```

9. La route `/` doit appeler `list_runs()` depuis `app/web_runs.py`.
10. La page doit afficher :
    - un titre clair ;
    - le nombre de runs disponibles ;
    - la liste des projets ;
    - la liste des versions ;
    - un lien vers la future page détail :

```text
/runs/<project>/<version>
```

11. Ajouter un bloc `if __name__ == "__main__":` pour lancer le serveur local.

## Configuration attendue

Le lancement local doit fonctionner avec :

```bash
python3 app/web.py
```

Variables d'environnement :

```text
WEB_HOST
WEB_PORT
```

Valeurs par défaut :

```text
WEB_HOST=127.0.0.1
WEB_PORT=8000
```

Le code doit permettre plus tard un lancement réseau avec :

```bash
WEB_HOST=0.0.0.0 python3 app/web.py
```

## Comportements attendus

- Si aucun run n'existe, afficher un message simple.
- Si des runs existent, afficher une liste lisible.
- La page doit rester sobre : HTML simple, CSS simple, pas de framework front.
- Ne pas créer de route de génération.
- Ne pas ajouter de formulaire de brief.
- Ne pas charger le contenu des fichiers Markdown à ce stade.

## Critères d'acceptation

- `python3 app/web.py` démarre le serveur.
- `GET /` répond sans erreur.
- Les runs détectés par le lot 01 sont visibles dans la page.
- Les liens de détail sont présents, même si la route détail sera implémentée
  dans le lot 03.
- Le style est lisible sur desktop sans chercher une finition produit.

## Validation

Exécuter :

```bash
python3 -m compileall app
python3 app/web.py
```

Puis ouvrir :

```text
http://127.0.0.1:8000/
```

Vérifier que les runs existants apparaissent.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Utiliser les fichiers ciblés, pas un scan large du repo.
- Garder l'interface simple et compréhensible.
- Ne pas changer le pipeline de génération.
- Ne pas modifier les outputs existants.
- Ne pas changer les contrats blackboard.
- Ne pas changer les prompts.
