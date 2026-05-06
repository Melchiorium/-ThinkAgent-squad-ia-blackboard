# Lot 45 - Correctif sécurité et readiness `/readyz`

## Objectif

Corriger deux findings d'audit sur le readiness endpoint :

1. protéger `/readyz` derrière le guard `WEB_ACCESS_TOKEN` quand un token est
   configuré ;
2. rendre le probe Supabase plus utile en vérifiant l'accès réel aux tables,
   pas seulement leur existence.

## Contexte projet utile

- `/healthz` doit rester public et léger pour Render.
- `/readyz` est un contrôle manuel avant audit ou après déploiement.
- `/readyz` peut ouvrir une connexion Supabase et révéler l'état du backend.
- `WEB_ACCESS_TOKEN` est le guard POC partagé déjà utilisé par l'application.
- `app/web_storage.py` contient `check_storage_readiness`.
- Le backend `file` reste valide pour les tests locaux et smoke tests
  éphémères.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_storage.py`
- `docs/render-poc-deployment.md`
- `docs/supabase-poc-storage.md`
- `docs/production-audit-runbook.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une règle courte est nécessaire

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
   `rules` liées à `web`, `web_storage` et `web_readiness_probe_flow`.
2. Modifier le guard Flask pour que seuls `static` et `healthz` restent
   accessibles sans token quand `WEB_ACCESS_TOKEN` est configuré.
3. Vérifier que `/readyz` sans token retourne `403` quand `WEB_ACCESS_TOKEN`
   est défini.
4. Vérifier que `/readyz?access_token=<token>` fonctionne et pose le cookie
   d'accès comme les autres routes.
5. Modifier `_supabase_check_storage_readiness` pour vérifier l'accès réel aux
   tables :
   - `select 1 from web_jobs limit 1`
   - `select 1 from web_run_artifacts limit 1`
6. Garder le check d'existence des tables ou remplacer par des requêtes qui
   distinguent proprement schema absent/inaccessible.
7. Ne pas créer, modifier ou supprimer de données dans `/readyz`.
8. Ne jamais exposer `SUPABASE_DATABASE_URL`, token ou mot de passe dans les
   payloads JSON ou logs.
9. Mettre à jour la documentation pour indiquer que `/readyz` est protégé par
   le même token que l'application.

## Comportements attendus

- `/healthz` reste public.
- `/readyz` est public uniquement si `WEB_ACCESS_TOKEN` est absent.
- Si `WEB_ACCESS_TOKEN` est défini :
  - `/readyz` sans token retourne `403` ;
  - `/readyz?access_token=<token>` retourne le readiness JSON ;
  - `/readyz` avec cookie valide retourne le readiness JSON.
- En mode `file`, `/readyz` continue de renvoyer un statut clair de backend
  local/éphémère.
- En mode `supabase`, `/readyz` vérifie :
  - configuration ;
  - dépendance `psycopg` ;
  - connexion ;
  - existence/accessibilité des tables ;
  - capacité de lecture minimale.
- `/readyz` ne lance jamais de génération LLM.

## Critères d'acceptation

- Le finding P2 sur `/readyz` public est corrigé.
- Le finding P3 sur le probe Supabase trop faible est corrigé.
- Les erreurs restent actionnables sans exposer de secrets.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 scripts/check_web_storage.py
WEB_ACCESS_TOKEN=test-token python3 - <<'PY'
from app.web import app
client = app.test_client()
print(client.get("/healthz").status_code)
print(client.get("/readyz").status_code)
print(client.get("/readyz?access_token=test-token").status_code)
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
absent.

Validation Supabase réelle seulement si configurée :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 scripts/check_web_storage.py
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder `/healthz` simple.
- Protéger les checks manuels sensibles avec le guard POC existant.
- Ne pas écrire ou afficher de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
