# Lot 15 - Acces par lien secret

## Objectif

Ajouter une protection POC par lien secret, sans créer de vraie authentification,
sans comptes utilisateurs et sans base de données.

Le but est d'éviter qu'une personne qui trouve l'URL publique du POC puisse
consulter les runs ou lancer des générations LLM.

## Contexte projet utile

- L'app Flask existe dans `app/web.py`.
- L'étape 3 a ajouté :
  - formulaire de brief ;
  - jobs JSON ;
  - cookie `web_session_id` ;
  - génération en background.
- Le POC doit rester simple.
- Il n'y a pas d'authentification utilisateur.
- Le mécanisme attendu est un lien partagé contenant un token.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/access_denied.html` à créer si utile
- `app/static/web.css`

## Fichiers à ne pas modifier

- `app/web_jobs.py`
- `app/web_runs.py`
- `app/generation_service.py`
- `app/artifact_writer.py`
- `app/main.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/`
- `README.md`
- `outputs/tests/`

## Configuration attendue

Ajouter une variable d'environnement :

```text
WEB_ACCESS_TOKEN
```

Comportement :

- si `WEB_ACCESS_TOKEN` est absent ou vide, l'app reste ouverte ;
- si `WEB_ACCESS_TOKEN` est défini, l'accès est accordé avec :

```text
/?access_token=<token>
```

- après un accès valide, poser un cookie pour éviter de remettre le token à
  chaque navigation ;
- le cookie ne doit pas contenir le token brut.

Nom de cookie attendu :

```text
web_access_granted
```

## Routes à protéger

Quand `WEB_ACCESS_TOKEN` est défini, protéger toutes les routes applicatives :

- `/`
- `POST /jobs`
- `/jobs/<job_id>`
- `/runs/<project>/<version>`
- `/runs/<project>/<version>/artifacts/<filename>`

La route Flask `static` peut rester accessible pour servir le CSS.

## Comportement d'accès

Dans `app/web.py`, ajouter un `before_request` dédié.

Règles :

1. Si `WEB_ACCESS_TOKEN` est vide : laisser passer.
2. Si l'endpoint Flask est `static` : laisser passer.
3. Si `request.args["access_token"]` correspond au token : laisser passer et
   demander la pose du cookie.
4. Si le cookie `web_access_granted` est valide : laisser passer.
5. Sinon : retourner `403`.

Utiliser `hmac.compare_digest(...)` pour comparer les tokens.

Pour éviter de stocker le token brut dans le cookie :

- calculer une empreinte SHA-256 du token ;
- stocker cette empreinte dans `web_access_granted` ;
- comparer le cookie à l'empreinte attendue.

Helpers conseillés :

```python
def _access_token() -> str:
    ...


def _access_cookie_value(token: str) -> str:
    ...


def _has_valid_access_cookie(token: str) -> bool:
    ...


def _has_valid_access_query_token(token: str) -> bool:
    ...
```

## Réponse 403

La réponse peut rester simple.

Option minimale acceptable :

```text
Accès refusé.
```

Option préférable :

- créer `app/templates/access_denied.html` ;
- afficher un message court ;
- ne pas afficher le token attendu ;
- ne pas mentionner de détails internes.

## Sécurité POC attendue

Ce n'est pas une authentification robuste. Ne pas ajouter :

- compte utilisateur ;
- login/password ;
- OAuth ;
- base de données ;
- gestion de rôles ;
- reset de mot de passe.

Le but est uniquement de protéger un POC audité par quelques personnes.

## Validation sans LLM

Exécuter :

```bash
python3 -m compileall app
```

Puis tester avec le client Flask :

```bash
python3 - <<'PY'
import os
from app.web import app

os.environ["WEB_ACCESS_TOKEN"] = "secret-test"
client = app.test_client()

blocked = client.get("/")
print("blocked", blocked.status_code)

wrong = client.get("/?access_token=wrong")
print("wrong", wrong.status_code)

allowed = client.get("/?access_token=secret-test")
print("allowed", allowed.status_code)
print("cookie", "web_access_granted" in str(allowed.headers))

followup = client.get("/")
print("followup", followup.status_code)

empty_brief = client.post("/jobs", data={"brief": "   "})
print("post_protected_but_reached", empty_brief.status_code)
PY
```

Attendus :

```text
blocked 403
wrong 403
allowed 200
cookie True
followup 200
post_protected_but_reached 400
```

Tester aussi le mode ouvert :

```bash
python3 - <<'PY'
import os
from app.web import app

os.environ.pop("WEB_ACCESS_TOKEN", None)
client = app.test_client()
print(client.get("/").status_code)
PY
```

Attendu :

```text
200
```

## Critères d'acceptation

- `WEB_ACCESS_TOKEN` absent : l'app fonctionne comme avant.
- `WEB_ACCESS_TOKEN` défini : `/` retourne `403` sans token.
- `/?access_token=<token>` donne accès.
- Un cookie `web_access_granted` est posé après accès valide.
- Le cookie ne contient pas le token brut.
- Les routes de job et de run sont protégées.
- La route `static` reste utilisable.
- Aucun appel LLM n'est nécessaire pour valider ce lot.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le mécanisme simple et explicite.
- Ne pas ajouter d'authentification complète.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
