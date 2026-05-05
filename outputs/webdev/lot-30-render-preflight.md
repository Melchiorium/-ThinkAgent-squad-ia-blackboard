# Lot 30 - Préflight local avant déploiement Render

## Objectif

Vérifier que le repo est prêt avant de créer le service Render.

Ce lot ne doit pas déployer l'application. Il doit produire une validation
locale reproductible et documenter les commandes de préflight utiles pour
l'agent suivant.

## Contexte projet utile

- Le MVP web est implémenté côté Flask.
- Le lancement local passe par `scripts/run_web.sh`.
- Render utilisera `Procfile`.
- Les jobs web sont des fichiers runtime sous `outputs/web-jobs/` et doivent
  rester ignorés par git.
- Le flow web principal est :

```text
titre projet -> brief -> génération -> résultat inline
```

## Fichiers autorisés à modifier

- `outputs/webdev/lot-30-render-preflight.md` si ce lot doit être affiné
- `README.md` seulement si une commande de préflight critique manque vraiment
- `docs/ai/flows.yaml` seulement si le préflight devient un flux documenté

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `Procfile`
- `requirements.txt`
- `scripts/run_web.sh`

## Travail demandé

Exécuter et vérifier les prérequis locaux suivants :

1. `Procfile` existe et lance `app.web:app` via Gunicorn.
2. `requirements.txt` contient `Flask` et `gunicorn`.
3. `scripts/run_web.sh` existe, est exécutable, et passe une validation shell.
4. `/healthz` répond via le client Flask.
5. `outputs/web-jobs/` est présent dans `.gitignore`.
6. `git status --short outputs/web-jobs` ne montre rien.
7. Le flow titre + brief fonctionne avec un fake runner, sans appel LLM.
8. Gunicorn accepte la configuration WSGI.

## Commandes de validation

```bash
python3 -m compileall app
zsh -n scripts/run_web.sh
test -x scripts/run_web.sh
python3 -m gunicorn --check-config app.web:app
python3 -c "from app.web import app; c=app.test_client(); print(c.get('/healthz').status_code)"
grep -n "outputs/web-jobs/" .gitignore
git status --short outputs/web-jobs
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

## Validation fake runner obligatoire

Créer un test inline sans LLM qui :

- configure `WEB_OUTPUTS_ROOT=/tmp/squad-render-preflight-outputs`;
- configure `WEB_JOBS_ROOT=/tmp/squad-render-preflight-jobs`;
- remplace `app.web.generation_runner` par un fake runner ;
- poste `project_title=Yoyo Render Preflight` et un brief court ;
- attend le statut `done` ;
- vérifie que l'API retourne un `run_url` ;
- vérifie que le HTML `/jobs/<job_id>` contient PRD, Architecture et GTM ;
- vérifie que l'API ne retourne pas `brief_text`.

## Critères d'acceptation

- Tous les checks locaux passent.
- Aucun fichier runtime sous `outputs/web-jobs/` n'est visible dans git.
- Le fake runner crée un run nommé avec le titre projet.
- Le résultat est visible inline dans `/jobs/<job_id>`.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas lancer de vraie génération LLM dans ce lot.
- Ne pas créer de service Render.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux runs générés existants.

