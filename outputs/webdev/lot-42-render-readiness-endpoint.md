# Lot 42 - Readiness endpoint Render/Supabase

## Objectif

Ajouter un contrôle de readiness distinct du healthcheck Render pour vérifier
que la configuration de production est réellement exploitable.

`/healthz` doit rester simple et disponible. Le nouveau contrôle doit être
utilisé manuellement avant audit ou après déploiement.

## Contexte projet utile

- `/healthz` répond actuellement `{"status": "ok"}`.
- Render peut utiliser `/healthz` comme healthcheck léger.
- Supabase peut être configuré via :
  - `WEB_STORAGE_BACKEND=supabase`
  - `SUPABASE_DATABASE_URL`
- Il faut pouvoir vérifier la persistance sans lancer de génération LLM.
- Le backend `file` reste accepté pour le local/smoke test éphémère.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_storage.py`
- `docs/supabase-poc-storage.md`
- `docs/render-poc-deployment.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules`, `flows` et
   `rules` liées à `web` et `web_storage`.
2. Conserver `/healthz` comme endpoint minimal, sans requête Supabase.
3. Ajouter un endpoint `GET /readyz`.
4. Pour `WEB_STORAGE_BACKEND=file`, `/readyz` doit vérifier que le backend est
   résolu et répondre clairement que la persistance est locale/éphémère.
5. Pour `WEB_STORAGE_BACKEND=supabase`, `/readyz` doit vérifier :
   - présence de `SUPABASE_DATABASE_URL` sans l'afficher ;
   - connexion Postgres ;
   - existence/accessibilité des tables `web_jobs` et `web_run_artifacts`.
6. Retourner un JSON court, lisible et sans secret.
7. Ne pas lancer de génération LLM.
8. Documenter l'usage manuel de `/readyz`.

## Comportements attendus

- `/healthz` reste rapide et ne dépend pas de Supabase.
- `/readyz` retourne `200` si le backend actif est prêt.
- `/readyz` retourne un statut d'erreur clair si Supabase est mal configuré.
- Aucun secret n'est renvoyé.
- Le message distingue `file` et `supabase`.

## Critères d'acceptation

- Render peut continuer à utiliser `/healthz`.
- Un auditeur/dev peut ouvrir `/readyz` pour vérifier le mode de stockage actif.
- Le backend Supabase mal configuré est détectable avant une génération.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 - <<'PY'
from app.web import app
client = app.test_client()
print(client.get("/healthz").status_code)
print(client.get("/readyz").status_code)
print(client.get("/readyz").json)
PY
WEB_STORAGE_BACKEND=supabase python3 - <<'PY'
from app.web import app
client = app.test_client()
response = client.get("/readyz")
print(response.status_code)
print(response.json)
PY
```

La dernière commande doit échouer proprement si `SUPABASE_DATABASE_URL` est
absent, sans afficher de secret.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder `/healthz` simple.
- Ne pas écrire de secret.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
