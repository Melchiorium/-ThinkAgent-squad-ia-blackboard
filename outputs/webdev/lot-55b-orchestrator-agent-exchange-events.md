# Lot 55B - Instrumentation des échanges agents

## Objectif

Émettre des événements enrichis pendant `run_v0_flow(...)` pour rendre visibles
les échanges entre `Product`, `Growth`, `Tech`, `Blackboard` et le système,
y compris pendant la boucle de correction.

Ce lot ne doit pas changer le comportement métier du workflow. Il ajoute
uniquement de la télémétrie de progression.

## Dépendance

À faire après le lot 55A.

Le helper `build_agent_exchange_event(...)` doit exister dans
`app/web_progress.py`.

## Contexte projet utile

- `app/orchestrator.py` exécute le workflow :
  `Product -> Growth -> Tech -> Product revision -> readiness -> correction loop -> Product locking`.
- `_run_stage(...)` émet déjà des updates avant/après chaque étape.
- `_emit_progress(...)` transmet les updates au callback web.
- `_run_targeted_correction_loop(...)` peut relancer Tech, Growth et Product
  selon les gaps readiness.
- Le CLI doit continuer à fonctionner quand `progress_callback is None`.

## Fichiers autorisés à modifier

- `app/orchestrator.py`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml` seulement si la description de l'orchestrateur ou du
  flow de progression change

## Fichiers à ne pas modifier

- `app/agents/`
- `app/prompts V3/`
- `app/blackboard.py`
- `docs/ai/contracts.yaml`
- `docs/supabase-schema.sql`
- `app/templates/`
- `app/static/`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `docs/ai/flows.yaml` pour confirmer le workflow validé.
3. Lire `app/orchestrator.py`.
4. Importer `build_agent_exchange_event(...)` depuis `app/web_progress.py`.
5. Adapter `_emit_progress(...)` pour accepter un champ optionnel `event`.
6. Quand `event` est fourni, le transmettre au `progress_callback(...)`.
7. Ne pas changer le format existant des appels callback :
   les champs `stage`, `label`, `detail`, `active_blocks`, `done_blocks`,
   `skipped_blocks`, `failed_blocks` doivent continuer à fonctionner.
8. Ajouter un petit helper local si utile, par exemple :

   ```python
   def _emit_agent_exchange(...):
       ...
   ```

9. Émettre au minimum les échanges suivants :

   ```text
   system -> product              Brief transmis à Product
   product -> blackboard          PRD initial écrit
   blackboard -> growth           Growth lit le PRD
   growth -> blackboard           GTM écrit
   blackboard -> tech             Tech lit le PRD
   tech -> blackboard             Architecture écrite
   blackboard -> product          Product consolide les retours
   product -> blackboard          PRD révisé écrit
   blackboard -> system           Readiness vérifiée
   blackboard -> product          Product verrouille la version finale
   product -> blackboard          PRD final verrouillé
   blackboard -> system           Artefacts prêts à persister
   ```

10. Pour la boucle de correction, émettre des événements séparés :
    - `blackboard -> tech` puis `tech -> blackboard` si Tech est relancé ;
    - `blackboard -> growth` puis `growth -> blackboard` si Growth est relancé ;
    - `blackboard -> product` puis `product -> blackboard` si Product est
      relancé.
11. Inclure `loop=<numéro>` pour les événements de correction.
12. Inclure `task` avec un texte court et non sensible :
    - `Analyse du brief`
    - `Relecture GTM`
    - `Relecture architecture`
    - `Correction ciblée Tech`
    - etc.
13. Ne pas inclure le brief complet, les prompts ou les réponses LLM complètes.
14. Ne pas modifier l'ordre des appels agents.
15. Ne pas multiplier les appels LLM.

## Comportements attendus

- Le flux Product/Growth/Tech standard produit des événements enrichis.
- La boucle de correction ne se résume plus à un seul bloc finalisation :
  l'agent réellement relancé est visible dans les events.
- Sans `progress_callback`, le CLI fonctionne comme avant.
- En cas d'erreur pendant une étape, les events précédents restent exploitables.

## Critères d'acceptation

- `run_v0_flow(...)` émet des events enrichis quand un callback est fourni.
- Les events de correction contiennent `loop`.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun ordre métier n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 - <<'PY'
from app import orchestrator

def fake_agent(name):
    def _runner(blackboard, tasks=None):
        if name == "product":
            blackboard["prd_draft"] = "prd"
        elif name == "growth":
            blackboard["gtm_notes"] = "gtm"
        elif name == "tech":
            blackboard["architecture_notes"] = "arch"
            blackboard["mermaid_diagram"] = "graph LR\\nA-->B"
        elif name == "revision":
            blackboard["prd_draft"] = "revised"
        elif name == "lock":
            blackboard["prd_draft"] = "locked"
        return blackboard
    return _runner

orchestrator.run_product_agent = fake_agent("product")
orchestrator.run_growth_agent = fake_agent("growth")
orchestrator.run_tech_agent = fake_agent("tech")
orchestrator.run_product_revision = fake_agent("revision")
orchestrator.run_product_locking_pass = fake_agent("lock")
orchestrator.aggregate_global_readiness = lambda readiness: {"status": "READY", "known_tags": []}

events = []
orchestrator.run_v0_flow(
    "Project name: Test\\n\\nBrief",
    "test://brief",
    progress_callback=lambda **payload: events.append(payload),
)
enriched = [event for payload in events for event in [payload.get("event")] if event]
assert any(event.get("actor") == "product" and event.get("target") == "blackboard" for event in enriched)
assert any(event.get("actor") == "growth" and event.get("target") == "blackboard" for event in enriched)
assert any(event.get("actor") == "tech" and event.get("target") == "blackboard" for event in enriched)
print("ok")
PY
git diff -- app/orchestrator.py docs/ai/flows.yaml docs/ai/modules.yaml
git diff -- app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

## Validation manuelle

- Lancer une génération web courte.
- Observer `/api/jobs/<job_id>`.
- Vérifier que `progress_events` contient des champs `actor`, `target`, `flow`
  et `task`.
- Si une boucle de correction est déclenchée, vérifier que l'agent relancé est
  visible dans les événements.

## Rappel contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Respecter le workflow validé.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les agents sauf nécessité explicite.
- Garder l'instrumentation optionnelle.
