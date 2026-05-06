# Lot 55C - Presenter et API du schéma de progression

## Objectif

Transformer les événements enrichis en modèle de schéma consommable par l'UI,
puis exposer ce modèle dans `/api/jobs/<job_id>`.

Ce lot ne doit pas créer l'interface visuelle finale. Il prépare uniquement la
donnée `progress_graph`.

## Dépendance

À faire après les lots 55A et 55B.

Les événements enrichis doivent pouvoir contenir :

- `actor`
- `target`
- `flow`
- `task`
- `loop`

## Contexte projet utile

- `app/web_presenters.py` construit déjà le payload API via
  `build_job_status_payload(...)`.
- `app/web_progress.py` contient les helpers purs de progression.
- `app/static/web.js` consomme actuellement le payload JSON du job.
- Les anciens jobs peuvent ne pas avoir d'événements enrichis.

## Fichiers autorisés à modifier

- `app/web_progress.py`
- `app/web_presenters.py`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml` seulement si utile

## Fichiers à ne pas modifier

- `docs/supabase-schema.sql`
- `app/web_storage.py`
- `app/orchestrator.py`
- `app/templates/`
- `app/static/`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `app/web_progress.py` et `app/web_presenters.py`.
3. Ajouter dans `app/web_progress.py` un helper pur :

   ```python
   def build_progress_graph(job: dict | None) -> dict:
       ...
   ```

4. Le helper doit retourner un dictionnaire stable :

   ```python
   {
       "nodes": [...],
       "flows": [...],
       "active_actor": "",
       "active_target": "",
       "active_flow": "",
       "current_task": "",
       "loop": None,
   }
   ```

5. Nodes attendus :

   ```text
   system          Système / Artefacts
   product         Product
   growth          Growth
   tech            Tech
   blackboard      Blackboard
   ```

6. Chaque node doit contenir :
   - `id`
   - `label`
   - `status`: `idle | active | done | failed`
7. Flows attendus :
   - `system_to_product`
   - `product_to_blackboard`
   - `blackboard_to_growth`
   - `growth_to_blackboard`
   - `blackboard_to_tech`
   - `tech_to_blackboard`
   - `blackboard_to_product`
   - `blackboard_to_system`
8. Chaque flow doit contenir :
   - `id`
   - `from`
   - `to`
   - `label`
   - `status`: `idle | active | done | failed`
9. Déduire le dernier événement enrichi depuis `progress_events`.
10. Si le job est `failed`, marquer le dernier node/flow actif en `failed`.
11. Si le job est `done`, marquer les nodes et flows déjà vus en `done`.
12. Si aucun événement enrichi n'existe, retourner un graph idle avec une tâche
    issue de `progress_label` ou `progress_stage`.
13. Ne pas lever d'exception si un event contient un `actor`, `target` ou `flow`
    inconnu : ignorer ou laisser idle.
14. Ajouter `progress_graph` dans le payload de
    `build_job_status_payload(...)`.
15. Ne pas changer les clés existantes du payload.

## Comportements attendus

- L'API reste compatible avec l'UI actuelle.
- Les jobs anciens restent lisibles.
- Le schéma peut être reconstruit depuis `progress_events` sans accès au
  blackboard métier.
- La boucle correction expose la valeur `loop` si disponible.

## Critères d'acceptation

- `build_progress_graph(...)` existe.
- `build_job_status_payload(...)` inclut `progress_graph`.
- Les anciens payloads restent valides.
- Aucun changement SQL.
- Aucun changement UI dans ce lot.

## Commandes de validation

```bash
python3 -m compileall app
python3 - <<'PY'
from app.web_progress import build_agent_exchange_event, build_progress_graph

job = {
    "status": "running",
    "progress_label": "Tech travaille",
    "progress_stage": "correction_loop_1_tech",
    "progress_events": [
        build_agent_exchange_event(
            stage="correction_loop_1_tech",
            label="Tech corrige",
            actor="blackboard",
            target="tech",
            flow="blackboard_to_tech",
            task="Correction ciblée Tech",
            loop=1,
        )
    ],
}
graph = build_progress_graph(job)
assert graph["active_actor"] == "blackboard"
assert graph["active_target"] == "tech"
assert graph["active_flow"] == "blackboard_to_tech"
assert graph["current_task"] == "Correction ciblée Tech"
assert graph["loop"] == 1

failed = build_progress_graph({**job, "status": "failed"})
assert any(flow["status"] == "failed" for flow in failed["flows"])
print("ok")
PY
python3 - <<'PY'
from app.web_presenters import build_job_status_payload

payload = build_job_status_payload(
    {
        "job_id": "job-1",
        "status": "running",
        "created_at": "now",
        "updated_at": "now",
        "brief_preview": "brief",
        "progress_events": [],
    }
)
assert "progress_graph" in payload
assert "nodes" in payload["progress_graph"]
print("ok")
PY
git diff -- app/web_progress.py app/web_presenters.py docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- docs/supabase-schema.sql app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

## Rappel contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les helpers purs.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas introduire de migration SQL.
- Ne pas changer les clés API existantes.
