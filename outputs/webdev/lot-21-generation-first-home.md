# Lot 21 - Page d'accueil centrée génération

## Objectif

Transformer la page d'accueil web en vraie interface de génération :

```text
écrire un brief -> lancer -> suivre le job -> voir le résultat
```

Le backend de jobs existe déjà. Ce lot doit surtout changer la structure et le
texte de la home pour que l'usage principal soit évident.

## Contexte projet utile

- `app/web.py` expose déjà :
  - `GET /`
  - `POST /jobs`
  - `GET /jobs/<job_id>`
  - `GET /runs/<project>/<version>`
- `app/templates/index.html` contient déjà un formulaire brief.
- L'interface actuelle parle encore beaucoup d'`inventory`, ce qui donne
  l'impression d'un viewer technique plutôt qu'un outil de génération.
- Le POC reste Flask + Jinja + CSS statique.

## Fichiers autorisés à modifier

- `app/templates/index.html`
- `app/static/web.css`
- `app/web.py` seulement si des variables de template simples sont nécessaires

## Fichiers à ne pas modifier

- `app/generation_service.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `requirements.txt`
- `Procfile`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `docs/ai/modules.yaml` pour le module `web`.
3. Lire `app/templates/index.html`, `app/templates/job_status.html` et
   `app/static/web.css`.
4. Renommer visuellement la page :
   - titre principal : `Générer un dossier projet`
   - zone formulaire : première section visible
   - texte du bouton : `Lancer la génération`
5. Réorganiser la home en trois zones :
   - formulaire brief ;
   - jobs de cette session ;
   - runs existants en section secondaire.
6. Garder les routes existantes.
7. Ne pas changer la logique de génération.

## Comportements attendus

- L'utilisateur comprend immédiatement qu'il peut coller un brief et lancer la
  génération.
- Le formulaire est la première action visible.
- Les jobs de session restent visibles après création.
- L'inventaire des anciens runs reste accessible, mais n'est plus le centre de
  la page.
- La page reste utilisable sans JavaScript.

## Critères d'acceptation

- La home ne s'appelle plus principalement `Run inventory`.
- Le formulaire brief est clairement l'action principale.
- Le bouton ne dit plus `Create job`.
- La liste des runs existants reste disponible.
- Aucun comportement backend n'est cassé.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); r=c.get('/'); print(r.status_code); print('Lancer la génération' in r.get_data(as_text=True))"
WEB_ACCESS_TOKEN=secret-test python3 -c "from app.web import app; c=app.test_client(); print(c.get('/').status_code); print(c.get('/?access_token=secret-test').status_code)"
git diff -- app/templates/index.html app/static/web.css app/web.py
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle :

1. Lancer `python3 app/web.py`.
2. Ouvrir `/`.
3. Vérifier que la première action évidente est d'écrire un brief.
4. Vérifier que les runs existants sont toujours accessibles plus bas.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'interface simple et lisible.
- Ne pas introduire React, Vite ou un build frontend.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux outputs générés.

