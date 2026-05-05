# Lot 28 - Script de lancement local avec `.env`

## Objectif

Fournir une commande locale fiable pour lancer l'interface web avec les variables
du fichier `.env` chargées.

Le message `Missing required environment variable: OPENAI_API_KEY` existe déjà.
Ce lot ne doit pas le remplacer. Il doit éviter l'erreur en lançant l'app avec
le bon environnement.

## Contexte projet utile

- Le CLI est souvent lancé avec :

```bash
set -a; source .env; set +a; python3 app/main.py
```

- L'app web est lancée aujourd'hui avec :

```bash
python3 app/web.py
```

- Cette commande ne charge pas `.env`.
- À terme, Render utilisera ses propres variables d'environnement configurées en
ligne. Le `.env` local ne doit pas être présenté comme mécanisme de production.

## Fichiers autorisés à modifier

- `scripts/run_web.sh`
- `README.md`
- `.gitignore` seulement si nécessaire

## Fichiers à ne pas modifier

- `app/web.py`
- `app/llm.py`
- `app/generation_service.py`
- `requirements.txt`
- `Procfile`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Script attendu

Créer :

```text
scripts/run_web.sh
```

Comportement :

- être exécutable ;
- se placer à la racine du repo ;
- vérifier que `.env` existe ;
- charger `.env` avec export automatique ;
- définir des defaults locaux si absents :
  - `BLACKBOARD_PROMPT_VERSION=V3`
  - `WEB_HOST=127.0.0.1`
  - `WEB_PORT=8000`
  - `WEB_ACCESS_TOKEN=demo`
- vérifier que `OPENAI_API_KEY` est défini après chargement ;
- afficher l'URL locale à ouvrir ;
- lancer `python3 app/web.py`.

Commande cible :

```bash
./scripts/run_web.sh
```

## Message d'erreur attendu

Si `.env` est absent :

```text
Missing .env file. Create it or copy the expected environment variables before running the web app.
```

Si `OPENAI_API_KEY` reste absent :

```text
Missing OPENAI_API_KEY after loading .env.
```

Ne pas afficher la clé.

## Documentation README

Mettre à jour le lancement local web :

```bash
./scripts/run_web.sh
```

Expliquer brièvement :

- le script charge `.env` ;
- il met `BLACKBOARD_PROMPT_VERSION=V3` par défaut ;
- il met `WEB_ACCESS_TOKEN=demo` par défaut en local ;
- l'URL locale est `http://127.0.0.1:8000/?access_token=demo` si le token par
  défaut est conservé.

## Render / online

Documenter clairement que Render ne dépend pas du `.env` local.

Sur Render, les variables doivent être configurées dans le dashboard du service :

- `OPENAI_API_KEY`
- `BLACKBOARD_PROMPT_VERSION=V3`
- `WEB_ACCESS_TOKEN`
- `WEB_OUTPUTS_ROOT`
- `WEB_JOBS_ROOT`

Ne pas modifier `Procfile` dans ce lot.

## Critères d'acceptation

- `scripts/run_web.sh` existe.
- Le script est exécutable.
- Le script charge `.env`.
- Le script échoue clairement si `.env` ou `OPENAI_API_KEY` manque.
- Le README ne recommande plus `python3 app/web.py` comme commande principale
  pour une génération réelle locale.
- Le README distingue local `.env` et Render env vars.

## Commandes de validation

```bash
python3 -m compileall app
test -x scripts/run_web.sh
./scripts/run_web.sh
git diff -- scripts/run_web.sh README.md .gitignore
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Notes validation :

- `./scripts/run_web.sh` démarre un serveur long-running ; l'arrêter après avoir
  vérifié qu'il écoute.
- Si l'environnement de test ne doit pas lancer de serveur, utiliser :

```bash
zsh -n scripts/run_web.sh
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas ajouter `python-dotenv`.
- Ne pas modifier le client LLM.
- Ne pas exposer de secret dans les logs.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.

