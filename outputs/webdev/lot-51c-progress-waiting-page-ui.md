# Lot 51C - UI progression page d'attente

## Objectif

Afficher dans `/jobs/<job_id>` les blocs de progression et le journal
d'événements remplis par les lots 51A et 51B.

Ce lot est principalement frontend Flask/Jinja/JS/CSS. Il ne doit pas modifier
l'orchestration Product/Growth/Tech.

## Dépendances

À faire après :

1. lot 51A - stockage + API ;
2. lot 51B - instrumentation workflow.

Avant de commencer, vérifier que `GET /api/jobs/<job_id>` expose déjà :

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

- `app/templates/job_status.html` affiche la page d'attente.
- `app/static/web.js` poll déjà `/api/jobs/<job_id>`.
- `app/static/web.css` contient les styles du viewer.
- `app/web_presenters.py` construit le payload JSON et le view model job.
- Les résultats finaux sont déjà injectés dans `data-job-result-shell`.

## Fichiers autorisés à modifier

- `app/templates/job_status.html`
- `app/static/web.js`
- `app/static/web.css`
- `app/web_presenters.py` seulement si le view model serveur doit exposer des
  fallbacks
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/generation_service.py`
- `app/web_storage.py`
- `app/web_jobs.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `docs/supabase-schema.sql`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## UI attendue

Ajouter à la page d'attente :

1. une zone “Étape en cours” :
   - libellé courant ;
   - détail courant ;
   - compteur simple `X / Y` si disponible ;
   - indication “en cours depuis X s” calculée côté navigateur si possible.
2. une liste de blocs groupés :
   - Product ;
   - Growth / GTM ;
   - Tech ;
   - Finalisation.
3. un journal court des derniers événements :
   - horodatage ;
   - libellé ;
   - détail optionnel.
4. une zone d'alerte sobre si la progression signale une erreur :
   - timeout agent ;
   - erreur réseau/API ;
   - processus potentiellement bloqué ;
   - erreur inconnue.

## Règles de design

- Interface simple, dense et lisible.
- Pas de page marketing.
- Pas de grosse animation décorative.
- Pas de cartes imbriquées.
- Les textes doivent tenir sur mobile.
- Les statuts doivent être compréhensibles sans lire les logs Render.
- Les anciens jobs sans progression doivent afficher un fallback propre basé
  sur `queued/running/done/failed`.
- Les erreurs doivent être actionnables sans exposer de stacktrace complète,
  prompt, brief complet ou secret.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées liées à `web`,
   `web_presenters` et `web_unified_generation_ui_flow`.
2. Mettre à jour `job_status.html` :
   - ajouter des conteneurs `data-progress-current`,
     `data-progress-blocks`, `data-progress-events` ;
   - rendre une première version côté serveur pour le cas sans JavaScript ;
   - garder les résultats finaux existants.
3. Mettre à jour `web.js` :
   - lire `progress_*`, `progress_blocks`, `progress_events` depuis le payload ;
   - rafraîchir la zone courante ;
   - rafraîchir les blocs ;
   - rafraîchir le journal ;
   - conserver le comportement existant pour `done` et `failed`.
4. Ajouter un timer côté navigateur pour afficher la durée depuis le dernier
   événement ou depuis le début de l'étape active.
5. Ajouter un indicateur de blocage potentiel côté navigateur :
   - si le job est `running` ;
   - si aucun nouvel événement n'arrive depuis plus que
     `progress_timeout_seconds` ;
   - afficher un message du type `Cette étape prend plus de temps que prévu.`
     sans déclarer un échec tant que le backend ne l'a pas fait.
6. Si le payload contient `progress_error_type` ou
   `progress_error_message`, afficher une alerte courte au-dessus du journal.
7. Mettre à jour `web.css` :
   - styles pour bloc `pending`, `active`, `done`, `skipped`, `failed` ;
   - style d'alerte timeout/erreur ;
   - layout responsive ;
   - journal lisible.
8. Vérifier que l'ancien affichage `Génération en cours` reste disponible en
   fallback.
9. Mettre à jour `docs/ai/modules.yaml` et `docs/ai/flows.yaml` si l'UI web
   documentée change.

## Comportements attendus

- Quand un job est `queued`, la page affiche un état d'attente clair.
- Quand une génération est `running`, la page montre :
  - l'étape active ;
  - les blocs déjà terminés ;
  - les blocs à venir ;
  - les derniers événements.
- Quand une génération est `done`, la page garde la progression visible et
  affiche les résultats inline.
- Quand une génération échoue, la page montre le dernier bloc atteint et
  l'erreur existante.
- Quand un timeout agent est déclaré par le backend, la page affiche un message
  clair, par exemple `Product initial a dépassé 10 minutes.`
- Quand l'étape active dure trop longtemps sans nouvel événement, la page
  indique que l'étape prend plus de temps que prévu.
- Sans JavaScript, la page reste lisible après rechargement manuel.
- Les anciens jobs sans progression restent lisibles.

## Critères d'acceptation

- `/jobs/<job_id>` affiche les blocs de progression.
- Le polling met à jour les blocs sans rechargement complet.
- Le journal d'événements est lisible.
- Le résultat final continue de s'afficher à la fin.
- Les erreurs de timeout/processus bloqué sont visibles dans l'UI.
- Aucun runtime de génération n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
git diff -- app/templates/job_status.html app/static/web.js app/static/web.css app/web_presenters.py docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- app/orchestrator.py app/generation_service.py app/web_storage.py app/web_jobs.py app/agents "app/prompts V3" docs/ai/contracts.yaml docs/supabase-schema.sql
git status --short outputs/tests outputs/web-jobs
```

Validation manuelle :

1. ouvrir un job avec progression fake ou réelle ;
2. vérifier le rendu desktop ;
3. vérifier le rendu mobile ;
4. vérifier le cas ancien job sans progression ;
5. vérifier le cas `failed` ;
6. vérifier le cas `progress_error_type="timeout"` ;
7. vérifier le cas étape longue sans nouvel événement ;
8. vérifier que le résultat final apparaît toujours.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'UI simple et lisible.
- Ne pas modifier l'orchestration.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
