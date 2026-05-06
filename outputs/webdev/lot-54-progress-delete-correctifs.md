# Lot 54 - Correctifs progression et suppression de runs

## Objectif

Corriger trois findings introduits par les lots progression/suppression :

1. importer `re` avant d'utiliser `_sanitize_progress_error_message(...)` ;
2. éviter que le timeout agent libère le verrou de génération pendant que
   l'appel LLM continue en arrière-plan ;
3. éviter les liens `Ouvrir le résultat` obsolètes après suppression d'un run.

## Contexte projet utile

- `app/web.py` classe les erreurs de génération via
  `_classify_progress_error(...)`.
- `_sanitize_progress_error_message(...)` utilise `re.sub(...)`.
- `app/orchestrator.py` a ajouté un timeout par étape agent.
- Le serveur web garde un `generation_lock` pour éviter plusieurs générations
  concurrentes dans le même process.
- La suppression de run supprime les artefacts mais ne supprime pas les jobs.
- La home construit `job.run_url` depuis `run_project` / `run_version`.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/orchestrator.py`
- `app/web_storage.py` seulement si utile pour vérifier l'existence d'un run
- `app/web_presenters.py` seulement si le filtrage de lien est mieux placé là
- `scripts/check_web_storage.py` seulement si un test ciblé est utile
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si un garde-fou court est nécessaire

## Fichiers à ne pas modifier

- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `docs/supabase-schema.sql`, sauf nécessité stricte
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## Correctif 1 - Import `re`

### Attendu

- Ajouter `import re` dans `app/web.py`.
- Vérifier qu'une erreur de génération simulée passe bien par
  `_mark_generation_job_failed(...)` et met le job en `failed`.
- Ne pas exposer de stacktrace complète dans l'UI.

### Critère

Une exception déclenchée dans le runner ne doit jamais laisser le job bloqué en
`running` à cause d'un `NameError` dans le gestionnaire d'erreur.

## Correctif 2 - Timeout agent sans concurrence fantôme

### Problème

Le timeout actuel peut lancer l'appel agent dans un thread daemon, lever
`TimeoutError`, marquer le job en échec, puis libérer `generation_lock` alors
que l'appel LLM continue encore en arrière-plan. Un nouveau job peut alors
démarrer pendant que l'ancien appel consomme toujours des ressources.

### Attendus

Choisir une correction simple et sûre pour le POC :

Option recommandée :

- ne pas exécuter l'appel agent dans un thread séparé ;
- garder les événements de progression avant/après appel ;
- garder l'affichage “étape longue” côté UI ;
- si aucun mécanisme fiable d'annulation n'existe, documenter que
  `WEB_AGENT_STEP_TIMEOUT_SECONDS` est un seuil d'alerte UI et non un kill dur.

Option acceptable si conservée avec thread :

- ne pas libérer `generation_lock` tant que le thread agent n'est pas terminé ;
- ou ne pas accepter de nouveau job tant qu'un thread agent timed-out est encore
  vivant ;
- marquer clairement le job en `failed` seulement quand il n'y a plus de travail
  en arrière-plan qui peut encore modifier l'état.

À éviter :

- laisser un thread LLM continuer en arrière-plan après avoir marqué le job
  échoué et libéré le verrou ;
- créer un faux sentiment de cancellation.

### Critères

- Un timeout ou appel long ne permet pas deux générations concurrentes dans le
  même worker.
- Le CLI reste inchangé.
- L'UI garde un retour utile sur les étapes longues.

## Correctif 3 - Liens de résultat après suppression

### Problème

Après suppression d'un run, les jobs terminés peuvent encore contenir
`run_project` et `run_version`, donc la home peut afficher `Ouvrir le résultat`
vers une page désormais `404`.

### Attendus

Choisir l'une des approches :

1. au moment de construire `job.run_url`, vérifier que `get_run(...)` retourne
   encore un run existant ;
2. ou après suppression, nettoyer les jobs qui pointent vers ce run.

Approche recommandée pour ce POC :

- filtrer le lien au rendu de la home et du détail job ;
- ne pas supprimer ou modifier les jobs automatiquement dans ce lot ;
- conserver l'historique de job mais ne pas proposer de lien mort.

### Critères

- Après suppression d'un run, aucun lien `Ouvrir le résultat` ne pointe vers ce
  run sur la home.
- Un job terminé peut rester visible comme historique de session.
- La suppression de run ne supprime pas les jobs par surprise.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py
git diff -- app/web.py app/orchestrator.py app/web_storage.py app/web_presenters.py scripts/check_web_storage.py docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml
git diff -- app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

## Validations manuelles

1. Simuler un runner qui lève une exception :
   - le job doit passer en `failed` ;
   - `progress_error_type` doit être rempli ;
   - pas de `NameError`.
2. Simuler un appel long :
   - l'UI doit afficher que l'étape prend du temps ;
   - aucun nouveau job ne doit démarrer en parallèle dans le même worker si
     l'ancien appel continue.
3. Supprimer un run lié à un job terminé :
   - le run disparaît ;
   - le job reste visible ;
   - le lien `Ouvrir le résultat` n'apparaît plus pour ce job.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le correctif ciblé.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
- Ne pas introduire WebSocket, Redis, Celery ou queue distribuée.
