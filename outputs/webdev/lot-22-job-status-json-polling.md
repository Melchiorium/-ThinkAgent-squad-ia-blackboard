# Lot 22 - Statut de job en JSON et polling léger

## Objectif

Permettre à l'interface web de suivre un job sans recharger toute la page.

Ce lot ajoute une petite API JSON et un JavaScript minimal. Il ne doit pas
changer la mécanique de génération.

## Contexte projet utile

- `POST /jobs` crée déjà un job JSON dans le stockage fichier.
- `GET /jobs/<job_id>` affiche déjà une page de statut.
- La page de statut actuelle utilise un meta refresh.
- Pour afficher la génération dans une interface plus fluide, il faut pouvoir
  interroger le statut courant depuis le navigateur.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/job_status.html`
- `app/templates/index.html` si nécessaire pour exposer un job actif
- `app/static/web.js`
- `app/static/web.css`

## Fichiers à ne pas modifier

- `app/web_jobs.py` sauf bug bloquant découvert pendant le lot
- `app/generation_service.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Route à ajouter

Ajouter une route JSON :

```text
GET /jobs/<job_id>.json
```

ou :

```text
GET /api/jobs/<job_id>
```

Choisir une seule convention et rester cohérent.

Réponse minimale attendue :

```json
{
  "job_id": "...",
  "status": "queued|running|done|failed",
  "created_at": "...",
  "updated_at": "...",
  "brief_preview": "...",
  "error": "",
  "run_url": "/runs/Project/version%201"
}
```

Règles :

- `run_url` vaut `null` tant que le job n'est pas `done`.
- Ne pas renvoyer `brief_text` complet dans l'API.
- Ne pas renvoyer de chemins filesystem.
- La route reste protégée par `WEB_ACCESS_TOKEN` comme les autres routes métier.

## JavaScript attendu

Créer `app/static/web.js`.

Comportement :

- si la page contient un élément avec `data-job-status-url`, poller toutes les 3
  secondes ;
- mettre à jour le badge de statut ;
- arrêter le polling quand le job est `done` ou `failed` ;
- si `done`, afficher un lien vers le résultat ;
- si `failed`, afficher l'erreur ;
- garder un fallback sans JavaScript avec la page HTML actuelle.

Ne pas ajouter de framework frontend.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `app/web.py`, `app/templates/job_status.html`, `app/static/web.css`.
3. Ajouter une fonction interne de construction de payload JSON depuis un job.
4. Ajouter la route JSON.
5. Ajouter `web.js` avec polling minimal.
6. Charger `web.js` dans les templates utiles avec `defer`.
7. Remplacer ou conserver le meta refresh seulement comme fallback.
8. Tester avec un fake job ou un fake runner, sans appel LLM.

## Comportements attendus

- La page statut se met à jour sans refresh complet quand JavaScript est actif.
- Sans JavaScript, l'utilisateur peut encore voir le statut via reload/meta
  refresh.
- La route JSON ne fuit pas le brief complet.
- La route JSON ne fuit pas de chemin serveur.

## Critères d'acceptation

- Une route de statut JSON existe.
- `job_status.html` utilise cette route pour le polling.
- `web.js` est simple, sans dépendance.
- La page reste fonctionnelle sans JS.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; print([rule.rule for rule in app.url_map.iter_rules() if 'job' in rule.rule])"
python3 -c "from app.web import app; c=app.test_client(); print(c.get('/').status_code)"
git diff -- app/web.py app/templates/index.html app/templates/job_status.html app/static/web.js app/static/web.css
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle recommandée :

1. Créer un job depuis la home.
2. Ouvrir la page statut.
3. Vérifier que le statut évolue sans reload complet visible.
4. Vérifier que le lien résultat apparaît quand le job est terminé.

Ne pas lancer une vraie génération LLM sauf accord explicite du mainteneur.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le JavaScript minimal et lisible.
- Ne pas ajouter de build frontend.
- Ne pas exposer le brief complet dans l'API JSON.
- Ne pas exposer de chemin filesystem.
- Ne pas modifier les prompts ou contrats blackboard.

