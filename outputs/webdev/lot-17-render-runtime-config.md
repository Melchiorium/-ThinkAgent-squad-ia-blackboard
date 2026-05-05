# Lot 17 - Configuration runtime Render minimale

## Objectif

Préparer le POC web Flask pour être lancé sur Render avec un runtime Python
standard.

Ce lot ne doit pas changer les routes métier, les templates, la génération, ni
la logique de sessions. Il prépare uniquement le démarrage de l'application hors
localhost.

## Contexte projet utile

- L'étape 5 correspond au déploiement Render du POC.
- L'app web existe dans `app/web.py`.
- En local, l'app peut encore être lancée avec :

```bash
python3 app/web.py
```

- Sur Render, l'application doit être servie par un serveur WSGI, pas par le
  serveur de développement Flask.
- La file de génération actuelle repose sur un `threading.Lock` et un thread
  background dans le process Flask. Pour ce POC, il faut donc rester sur un seul
  worker applicatif.

## Fichiers autorisés à modifier

- `requirements.txt`
- `Procfile`
- `README.md` seulement si une note de démarrage très courte est nécessaire

## Fichiers à ne pas modifier

- `app/web.py`
- `app/web_jobs.py`
- `app/web_runs.py`
- `app/generation_service.py`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Vérifier que `app/web.py` expose bien l'objet Flask nommé `app`.
3. Ajouter `gunicorn` dans `requirements.txt`.
4. Créer un `Procfile` à la racine avec une commande web Render compatible.
5. Utiliser une commande WSGI qui bind sur `0.0.0.0:$PORT`.
6. Garder un seul worker pour respecter la file POC en mémoire.
7. Ne pas créer de `Dockerfile` ni de `render.yaml` dans ce lot.

## Commande attendue dans Procfile

Utiliser une commande proche de :

```text
web: gunicorn app.web:app --bind 0.0.0.0:$PORT --workers 1 --threads 4
```

Raisons :

- `app.web:app` pointe vers l'objet Flask existant.
- `$PORT` est fourni par Render.
- `--workers 1` évite plusieurs process concurrents avec des locks et jobs
  non partagés.
- `--threads 4` permet de garder une app un peu réactive pendant qu'un job tourne
  dans un thread background.

## Comportements attendus

- Le lancement local `python3 app/web.py` continue de fonctionner.
- Render peut démarrer l'app via le `Procfile`.
- Aucune route web n'est ajoutée ou modifiée.
- Aucun comportement de génération n'est modifié.
- Aucune dépendance lourde n'est ajoutée.

## Critères d'acceptation

- `requirements.txt` contient `gunicorn`.
- `Procfile` existe à la racine.
- `Procfile` lance `app.web:app`.
- `Procfile` utilise `$PORT`.
- `Procfile` force un seul worker.
- Aucun fichier généré sous `outputs/tests/` n'est modifié.
- Aucun prompt n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; print(app.name)"
python3 -m pip show gunicorn
gunicorn --check-config app.web:app
git diff -- requirements.txt Procfile
git diff -- "app/prompts V3"
git diff -- docs/ai/contracts.yaml
```

Si `gunicorn` n'est pas installé dans l'environnement local, installer les
dépendances du projet avant la validation :

```bash
python3 -m pip install -r requirements.txt
```

Ne pas lancer de vraie génération LLM pour ce lot.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la modification minimale et lisible.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les prompts.
- Ne pas toucher à l'historique généré.
- Ne pas introduire Redis, Celery, base de données ou authentification.
