# Lot 19 - Healthcheck et configuration d'environnement Render

## Objectif

Ajouter le minimum nécessaire pour vérifier que l'application web est vivante
sur Render et clarifier les variables d'environnement indispensables.

Ce lot ne doit pas lancer de vraie génération et ne doit pas transformer le POC
en service public.

## Contexte projet utile

- Le lot 15 protège les routes applicatives avec `WEB_ACCESS_TOKEN`.
- Render peut avoir besoin d'une route simple pour vérifier que le service web
  répond.
- Le healthcheck ne doit pas exposer les runs, les jobs, les secrets ou la
  configuration.
- L'app reste sans comptes utilisateurs et sans auth complète.

## Fichiers autorisés à modifier

- `app/web.py`
- `README.md` seulement si une note courte de configuration est nécessaire
- `docs/ai/rules.yaml` seulement si une règle courte est nécessaire

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `requirements.txt`
- `Procfile`

## Route à ajouter

Ajouter :

```text
GET /healthz
```

Réponse attendue :

```json
{"status":"ok"}
```

Comportement :

- retourne `200`;
- ne dépend pas d'un job;
- ne lit pas les outputs;
- ne révèle aucune variable d'environnement;
- reste accessible même si `WEB_ACCESS_TOKEN` est défini.

## Variables d'environnement à documenter

Préparer une liste courte pour Render :

```text
OPENAI_API_KEY=<secret>
OPENAI_BASE_URL=<optionnel selon provider>
OPENAI_MODEL=<optionnel selon provider>
BLACKBOARD_PROMPT_VERSION=V3
WEB_ACCESS_TOKEN=<token partagé POC>
WEB_OUTPUTS_ROOT=/var/data/outputs
WEB_JOBS_ROOT=/var/data/web-jobs
```

Notes :

- `WEB_ACCESS_TOKEN` doit être défini sur Render pour éviter une app ouverte.
- `WEB_OUTPUTS_ROOT` et `WEB_JOBS_ROOT` doivent pointer vers un disque persistant
  Render.
- `WEB_HOST` et `WEB_PORT` servent au lancement local `python3 app/web.py`; le
  lancement Render via Gunicorn utilise `$PORT`.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `docs/ai/flows.yaml` pour `web_secret_link_access_flow`.
3. Ajouter la route `healthz` dans `app/web.py`.
4. Adapter `_guard_secret_access` pour laisser passer `healthz`, comme `static`.
5. Vérifier que la route ne dépend pas de l'état session ou d'un run.
6. Ajouter uniquement une note documentaire courte si nécessaire.

## Comportements attendus

- `GET /healthz` retourne `200` sans token.
- `GET /healthz` retourne `200` avec `WEB_ACCESS_TOKEN` défini.
- `GET /` reste protégé quand `WEB_ACCESS_TOKEN` est défini.
- Aucune donnée sensible n'apparaît dans `/healthz`.
- Les routes métier ne changent pas.

## Critères d'acceptation

- La route `/healthz` existe.
- Elle retourne une réponse JSON minimale.
- Elle reste accessible sans cookie d'accès.
- La protection `WEB_ACCESS_TOKEN` reste active sur `/`, `/jobs`, `/runs/...`.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); r=c.get('/healthz'); print(r.status_code, r.get_json())"
WEB_ACCESS_TOKEN=secret-test python3 -c "from app.web import app; c=app.test_client(); print(c.get('/healthz').status_code); print(c.get('/').status_code)"
git diff -- app/web.py README.md docs/ai/rules.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Ne pas lancer de vraie génération LLM pour ce lot.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le healthcheck minimal.
- Ne pas exposer de secrets ou de chemins serveur.
- Ne pas introduire de nouvelle architecture d'authentification.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les prompts.
