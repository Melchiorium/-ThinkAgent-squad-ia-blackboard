# Lot 55D - UI schéma animé des échanges agents

## Objectif

Afficher dans `/jobs/<job_id>` un schéma animé simple montrant les blocs
`Product`, `Growth`, `Tech`, `Blackboard` et `Système / Artefacts`, avec les
flèches actives selon le `progress_graph` exposé par l'API.

Le schéma doit rendre visibles les échanges de la boucle de correction.

## Dépendance

À faire après le lot 55C.

Le payload `/api/jobs/<job_id>` doit exposer `progress_graph`.

## Contexte projet utile

- `app/templates/job_status.html` rend la page de suivi.
- `app/static/web.js` poll `/api/jobs/<job_id>` toutes les 3 secondes.
- `app/static/web.css` contient les styles de progression.
- La liste actuelle des blocs et des événements doit rester sous le nouveau
  schéma.
- Pas de framework frontend ni de dépendance JS.

## Fichiers autorisés à modifier

- `app/templates/job_status.html`
- `app/static/web.js`
- `app/static/web.css`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml` seulement si utile

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/web_progress.py`
- `app/web_presenters.py`
- `app/web_storage.py`
- `docs/supabase-schema.sql`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `app/templates/job_status.html`, `app/static/web.js` et
   `app/static/web.css`.
3. Ajouter dans `job_status.html`, au-dessus de `job-progress__blocks`, une zone
   de schéma :

   ```html
   <div class="agent-flow" data-agent-flow>
     ...
   </div>
   ```

4. Le HTML initial peut être rendu vide ou depuis `job.progress_graph` si déjà
   disponible côté template. Option simple recommandée :
   - rendre une structure statique Product/Growth/Tech/Blackboard/System ;
   - laisser `web.js` appliquer les états depuis `progress_graph`.
5. Afficher les nodes :
   - Product
   - Growth
   - Tech
   - Blackboard
   - Système / Artefacts
6. Afficher les flows directionnels :
   - System -> Product
   - Product -> Blackboard
   - Blackboard -> Growth
   - Growth -> Blackboard
   - Blackboard -> Tech
   - Tech -> Blackboard
   - Blackboard -> Product
   - Blackboard -> System
7. Utiliser des éléments HTML simples, pas de SVG complexe obligatoire.
8. Ajouter une zone texte sous le schéma :
   - tâche courante ;
   - numéro de boucle si `progress_graph.loop` est présent.
9. Dans `web.js`, ajouter une fonction `renderAgentFlow(progressGraph)`.
10. Appeler `renderAgentFlow(payload.progress_graph)` dans `applyPayload(...)`
    ou `renderProgress(...)`.
11. Si `progress_graph` est absent, afficher un état neutre compatible avec les
    anciens jobs.
12. Appliquer des classes CSS :
    - `agent-flow__node--active`
    - `agent-flow__node--done`
    - `agent-flow__node--failed`
    - `agent-flow__arrow--active`
    - `agent-flow__arrow--done`
    - `agent-flow__arrow--failed`
13. Animer seulement la flèche active avec un pulse discret.
14. Ajouter `@media (prefers-reduced-motion: reduce)` pour désactiver les
    animations.
15. Vérifier l'affichage mobile :
    - les blocs doivent passer sur plusieurs lignes ;
    - aucun texte ne doit déborder ;
    - les flèches peuvent devenir de simples connecteurs textuels si nécessaire.
16. Ne pas supprimer la liste actuelle des blocs détaillés.
17. Ne pas supprimer le journal `Derniers événements`.

## Comportements attendus

- Quand Product travaille, Product est surligné et une flèche liée à Product est
  active.
- Quand Growth travaille, Growth est surligné.
- Quand Tech travaille, Tech est surligné.
- Quand la boucle de correction relance Tech/Growth/Product, l'agent relancé est
  visible dans le schéma et la tâche mentionne la correction.
- Quand le job est terminé, le schéma est stable et non animé.
- Quand le job échoue, le dernier acteur/flux connu passe en état échec.
- Les anciens jobs sans `progress_graph` restent affichables.

## Critères d'acceptation

- Le schéma apparaît sur `/jobs/<job_id>`.
- Les états changent après chaque polling API.
- La tâche courante est visible sous le schéma.
- Le journal détaillé existant reste présent.
- Pas de dépendance frontend ajoutée.
- Pas de WebSocket.
- Pas de modification des prompts ou du workflow.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 scripts/check_web_storage.py
git diff -- app/templates/job_status.html app/static/web.js app/static/web.css docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- app/orchestrator.py app/web_progress.py app/web_presenters.py docs/supabase-schema.sql app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

## Validation manuelle sans appel LLM

Utiliser un payload mocké ou modifier temporairement dans DevTools la réponse
de `/api/jobs/<job_id>` pour vérifier les états suivants :

- `active_flow="product_to_blackboard"`
- `active_flow="blackboard_to_growth"`
- `active_flow="blackboard_to_tech"`
- `active_flow="blackboard_to_product"` avec `loop=1`
- job `failed`
- job `done`

## Validation réelle

1. Lancer une génération courte depuis le web.
2. Observer la page `/jobs/<job_id>`.
3. Vérifier que le schéma passe par Product, Growth, Tech puis finalisation.
4. Si une boucle de correction est déclenchée, vérifier que l'agent relancé est
   visible.
5. Vérifier mobile et desktop.

## Rappel contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'UI simple et lisible.
- Ne pas ajouter de framework frontend.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
