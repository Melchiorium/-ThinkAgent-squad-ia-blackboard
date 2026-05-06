# Lot 51B - Instrumentation workflow progression

## Objectif

Remplir les champs de progression créés par le lot 51A pendant l'exécution
réelle du workflow Product/Growth/Tech.

Ce lot ne doit pas créer de nouvelle UI avancée. Il doit faire évoluer les
données de progression pour que `/api/jobs/<job_id>` montre où en est la
génération.

Il doit aussi ajouter des retours d'erreur exploitables pour l'utilisateur :
processus bloqué, timeout par étape agent, erreur réseau ou erreur LLM.

## Dépendance

À faire après le lot 51A.

Le dev doit vérifier que les jobs exposent déjà :

- `progress_stage`
- `progress_label`
- `progress_detail`
- `progress_order`
- `progress_total`
- `progress_blocks`
- `progress_events`
- `progress_started_at`
- `progress_last_event_at`
- `progress_timeout_seconds`
- `progress_error_type`
- `progress_error_message`

## Contexte projet utile

- `app/web.py` lance `_start_generation_job(...)` en thread.
- `app/generation_service.py` appelle `run_v0_flow(...)`.
- `app/orchestrator.py` exécute :
  `Product -> Growth -> Tech -> Product revision -> readiness -> correction loop -> Product locking`.
- Le CLI `python3 app/main.py` doit continuer à fonctionner sans callback.
- Le besoin est un découpage par blocs métier préparés / confirmés, sans
  modifier les prompts ni multiplier les appels LLM.
- Le POC doit éviter qu'une page d'attente reste muette trop longtemps si un
  agent ou un appel réseau bloque.

## Fichiers autorisés à modifier

- `app/orchestrator.py`
- `app/generation_service.py`
- `app/web.py`
- `app/web_storage.py` seulement si un helper de progression manque
- `app/web_jobs.py` seulement si nécessaire
- `app/web_progress.py` si créé au lot 51A ou utile ici
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`

## Fichiers à ne pas modifier

- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `app/templates/`
- `app/static/`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## Blocs métier minimum

Faire avancer au minimum ces blocs :

```text
brief_received              Brief reçu
product_brief_analysis      Product analyse le brief
product_problem             Product formule le problème cible
product_users_goals         Product structure utilisateurs et objectifs MVP
product_user_stories        Product prépare les user stories
growth_segments             Growth analyse les segments
growth_positioning          Growth travaille le positionnement
growth_channels             Growth prépare les canaux GTM
growth_objections           Growth identifie objections et risques marché
tech_constraints            Tech analyse les contraintes
tech_components             Tech prépare les composants
tech_mermaid                Tech prépare le diagramme Mermaid
tech_risks                  Tech vérifie les risques techniques
product_revision            Product consolide le PRD
readiness_check             Vérification readiness
correction_loop             Corrections ciblées si nécessaires
product_locking             Product verrouille la version finale
artifacts_persistence       Écriture et persistance des artefacts
done                        Génération terminée
```

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées liées à
   `generation_service`, `orchestrator`, `web`, `web_jobs` et `web_storage`.
2. Ajouter un paramètre optionnel `progress_callback` à
   `run_generation_from_brief(...)`.
3. Ajouter un paramètre optionnel `progress_callback` à `run_v0_flow(...)`.
4. Ne rien changer au comportement si `progress_callback is None`.
5. Définir un petit format d'appel callback, par exemple :

   ```python
   progress_callback(
       stage="product_initial",
       label="Product structure le PRD initial",
       detail="Analyse du brief, problème cible, utilisateurs, objectifs MVP.",
       active_blocks=["product_brief_analysis", "product_problem"],
       done_blocks=["brief_received"],
   )
   ```

6. Dans `app/web.py`, créer un callback qui convertit ces appels en
   `update_job(...)`.
7. Émettre un événement juste avant chaque appel LLM bloquant.
8. Émettre un événement juste après chaque appel LLM bloquant.
9. Ne pas essayer de streamer le texte du LLM.
10. Ne pas découper les prompts.
11. Ne pas multiplier les appels LLM.
12. Après `_finalize_readiness`, ajouter un détail avec le statut global si
    disponible : `READY`, `LIMITED`, `INSUFFICIENT`.
13. Après `_run_targeted_correction_loop`, indiquer si la boucle a été déclenchée
    ou non.
14. Avant `persist_run_artifacts(...)`, activer `artifacts_persistence`.
15. Après persistance réussie, marquer `artifacts_persistence` et `done` comme
    terminés.
16. En cas d'exception dans `_start_generation_job(...)`, marquer le bloc actif
    en `failed` et ajouter un événement d'échec sans secret.
17. Ajouter un timeout de 10 minutes par étape agent côté orchestration web :
    - Product initial ;
    - Growth / GTM ;
    - Tech ;
    - Product revision ;
    - correction loop si elle appelle un agent ;
    - Product locking.
18. Le timeout doit être configurable par variable d'environnement, par exemple
    `WEB_AGENT_STEP_TIMEOUT_SECONDS`, avec défaut `600`.
19. Si une étape dépasse le timeout :
    - mettre le job en `failed` ;
    - marquer le bloc actif en `failed` ;
    - ajouter un événement `timeout` ;
    - remplir `progress_error_type="timeout"` ;
    - remplir `progress_error_message` avec un message court, par exemple
      `Product initial a dépassé 10 minutes.` ;
    - ne pas exposer de prompt, brief complet ou secret.
20. Si une exception ressemble à un problème réseau/API LLM :
    - garder `status="failed"` ;
    - remplir `progress_error_type` avec `network` ou `llm` si la classification
      est fiable, sinon `unknown` ;
    - garder un message actionnable et court.
21. Ne pas introduire de kill brutal non maîtrisé du process. Si Python ne peut
    pas interrompre proprement un appel bloquant, documenter la limite et faire
    en sorte que l'UI indique au minimum l'étape en cours et le temps écoulé.
22. Mettre à jour `docs/ai/modules.yaml` et `docs/ai/flows.yaml` si le flow de
    génération web documenté change.

## Comportements attendus

- Dès la création, le job indique que le brief est reçu.
- Quand Product démarre, les blocs Product deviennent actifs.
- Quand Growth démarre, les blocs Growth deviennent actifs.
- Quand Tech démarre, les blocs Tech deviennent actifs.
- Plusieurs blocs peuvent passer à `done` après un appel LLM.
- Pendant un appel long, le dernier bloc actif reste visible.
- Si une étape dépasse 10 minutes, le job échoue avec une erreur claire.
- Si un appel réseau/LLM échoue, la progression expose une erreur claire.
- En cas d'échec, le dernier bloc atteint est visible.
- Le CLI continue de fonctionner normalement.

## Critères d'acceptation

- `GET /api/jobs/<job_id>` montre des blocs qui évoluent pendant une génération.
- Le statut global `queued/running/done/failed` continue de fonctionner.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun agent Product/Growth/Tech n'est modifié.
- Aucun output généré n'est modifié.
- Le CLI standard continue de fonctionner.
- Les timeouts web ne changent pas le comportement CLI.
- Un processus bloqué ou une erreur réseau ne laisse pas l'utilisateur sans
  retour exploitable.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py
git diff -- app/orchestrator.py app/generation_service.py app/web.py app/web_storage.py app/web_jobs.py app/web_progress.py docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

Validation manuelle sans appel LLM :

- utiliser un fake runner ou monkeypatch local pour simuler plusieurs appels
  `progress_callback` ;
- vérifier que `/api/jobs/<job_id>` expose les changements de blocs.

Validation réelle :

- lancer une génération courte depuis le web ;
- surveiller `/api/jobs/<job_id>` ;
- vérifier que les blocs Product/Growth/Tech évoluent.
- simuler une exception dans le runner et vérifier que `progress_error_type` et
  le bloc `failed` sont exposés.
- si possible, simuler un timeout avec une valeur basse de
  `WEB_AGENT_STEP_TIMEOUT_SECONDS`.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'instrumentation simple et optionnelle.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les agents sauf nécessité explicite.
- Ne pas introduire WebSocket, Redis, Celery ou queue distribuée.
- Ne jamais stocker de secrets ou prompts bruts dans la progression.
- Timeout web par étape agent : 10 minutes par défaut, configurable, sans casser
  le CLI.
