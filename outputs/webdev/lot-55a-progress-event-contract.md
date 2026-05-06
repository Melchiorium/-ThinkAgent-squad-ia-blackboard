# Lot 55A - Contrat événements d'échange agents

## Objectif

Enrichir les événements de progression existants pour représenter les échanges
entre agents et blackboard, sans modifier le stockage SQL ni le workflow métier.

Ce lot ne doit pas créer d'UI. Il prépare seulement un contrat JSON stable que
les lots suivants pourront exploiter.

## Contexte projet utile

- `app/web_progress.py` centralise le contrat de progression web.
- Les jobs stockent déjà `progress_events` en JSON côté fichier et JSONB côté
  Supabase.
- `build_progress_event(...)` produit aujourd'hui les champs de base :
  `timestamp`, `stage`, `label`, `detail`, `kind`.
- `normalize_progress_events(...)` doit rester compatible avec les anciens
  événements déjà persistés.
- Il ne faut pas modifier `docs/supabase-schema.sql` : aucun champ SQL dédié ne
  doit être ajouté.

## Fichiers autorisés à modifier

- `app/web_progress.py`
- `docs/ai/modules.yaml` seulement si le contrat documenté de `web_progress`
  change de manière utile pour les agents futurs
- `docs/ai/flows.yaml` seulement si une note courte est nécessaire

## Fichiers à ne pas modifier

- `docs/supabase-schema.sql`
- `app/web_storage.py`
- `app/web.py`
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
2. Lire l'entrée `web_progress` dans `docs/ai/modules.yaml`.
3. Inspecter `app/web_progress.py`, notamment :
   - `build_progress_event(...)`
   - `normalize_progress_events(...)`
   - `_clean_event_payload(...)`
4. Ajouter un helper pur :

   ```python
   def build_agent_exchange_event(
       *,
       stage: str,
       label: str,
       detail: str = "",
       actor: str = "",
       target: str = "",
       flow: str = "",
       task: str = "",
       loop: int | None = None,
       timestamp: str | None = None,
       kind: str = "agent_exchange",
   ) -> dict:
       ...
   ```

5. Le helper doit réutiliser `build_progress_event(...)` ou produire le même
   format de base.
6. Ajouter les champs optionnels uniquement quand ils ont une valeur utile :
   - `actor`
   - `target`
   - `flow`
   - `task`
   - `loop`
7. Normaliser les valeurs texte avec les helpers existants.
8. Normaliser `loop` en entier positif quand fourni.
9. Adapter `_clean_event_payload(...)` si nécessaire pour conserver ces champs
   lors de l'écriture dans `progress_events`.
10. Ne pas casser les anciens événements sans ces champs.
11. Ne pas ajouter de dépendance.
12. Ne pas modifier la taille max des événements.

## Comportements attendus

- Un event enrichi reste un event de progression valide.
- Un ancien event sans `actor`, `target`, `flow`, `task`, `loop` reste lisible.
- Les champs vides ne polluent pas le JSON.
- Aucun secret, brief complet, prompt ou contenu LLM brut n'est ajouté dans ces
  champs.

## Critères d'acceptation

- `build_agent_exchange_event(...)` existe dans `app/web_progress.py`.
- `normalize_progress_events(...)` conserve les champs enrichis.
- `normalize_progress_events(...)` continue d'accepter les anciens events.
- Aucun changement SQL.
- Aucun changement UI.
- Aucun changement de workflow agents.

## Commandes de validation

```bash
python3 -m compileall app
python3 - <<'PY'
from app.web_progress import build_agent_exchange_event, normalize_progress_events

event = build_agent_exchange_event(
    stage="product_initial",
    label="Product écrit au blackboard",
    detail="PRD initial prêt.",
    actor="product",
    target="blackboard",
    flow="product_to_blackboard",
    task="Écriture du PRD initial",
    loop=1,
)
events = normalize_progress_events([event, {"stage": "legacy", "label": "Ancien event"}])
assert events[0]["actor"] == "product"
assert events[0]["target"] == "blackboard"
assert events[0]["flow"] == "product_to_blackboard"
assert events[0]["task"] == "Écriture du PRD initial"
assert events[0]["loop"] == 1
assert events[1]["stage"] == "legacy"
assert "actor" not in events[1] or events[1]["actor"] == ""
print("ok")
PY
git diff -- app/web_progress.py docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- docs/supabase-schema.sql app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

## Rappel contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le contrat simple et lisible.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
- Ne pas introduire de migration Supabase.
