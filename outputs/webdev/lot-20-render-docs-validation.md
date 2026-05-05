# Lot 20 - Documentation et validation du déploiement Render POC

## Objectif

Documenter l'étape 5 de façon courte et vérifiable : comment déployer le POC web
sur Render avec un disque persistant et un lien secret.

Ce lot est principalement documentaire. Il ne doit pas modifier le comportement
applicatif sauf mini-correction évidente découverte pendant la validation.

## Contexte projet utile

- L'étape 5 vient après :
  - viewer des runs existants ;
  - génération depuis un brief web ;
  - jobs JSON par session ;
  - accès par lien secret `WEB_ACCESS_TOKEN`.
- Le POC reste sans comptes utilisateurs.
- La file de génération reste process-local.
- Le stockage reste fichier.
- Render sert uniquement à permettre un audit par 2 ou 3 personnes.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `TODO.md` seulement si un risque résiduel doit être conservé

## Fichiers à ne pas modifier

- `app/` sauf mini-correction de cohérence bloquante
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`

## Travail demandé - README

Mettre à jour la section `Viewer Web POC` ou ajouter une sous-section courte :

```text
### Déploiement Render POC
```

La section doit expliquer :

- Render lance l'app via `Procfile` et Gunicorn ;
- un seul worker est attendu pour ce POC ;
- le disque persistant doit être monté et référencé par les variables web ;
- `WEB_ACCESS_TOKEN` doit être défini ;
- le lien d'accès initial est :

```text
https://<render-host>/?access_token=<token>
```

- ce n'est pas une authentification complète ;
- le POC n'est pas prévu pour un déploiement grand public.

Garder la section courte. Ne pas réécrire le README complet.

## Travail demandé - modules.yaml

Mettre à jour seulement les entrées utiles :

- `web` :
  - mentionner Gunicorn/Render seulement comme mode de lancement possible ;
  - mentionner `/healthz` si le lot 19 l'a ajouté ;
  - mentionner les racines configurables si le lot 18 les a ajoutées.

- `web_runs` :
  - mentionner que l'inventaire peut recevoir une racine outputs configurable.

- `web_jobs` :
  - mentionner le stockage JSON configurable.

- `generation_service` :
  - mentionner que `outputs_root` permet d'écrire vers un disque persistant.

Ne pas ajouter de module Render séparé sauf si du code Render dédié a vraiment
été ajouté, ce qui n'est pas attendu.

## Travail demandé - flows.yaml

Ajouter un flux court :

```yaml
web_render_poc_deployment_flow:
  owner: Procfile and app/web.py
  status: poc_deployment
  steps:
    - install Python dependencies from requirements.txt
    - start app.web:app through gunicorn
    - bind to Render PORT
    - keep one web worker for process-local jobs
    - use WEB_ACCESS_TOKEN for shared-link access
    - use WEB_OUTPUTS_ROOT and WEB_JOBS_ROOT on persistent disk
    - expose /healthz for service healthcheck
  limitations:
    - no full authentication
    - no user accounts
    - no distributed job queue
    - no horizontal scaling
    - POC audit deployment only
```

Adapter si `/healthz` ou les variables de stockage n'ont pas encore été
implémentées, mais ne pas documenter un comportement faux.

## Travail demandé - rules.yaml

Ajouter ou vérifier une règle courte dans `web_rules`, par exemple :

```yaml
- Keep the Render deployment as a single-process POC unless a real external
  queue and shared job store are introduced.
```

Ne pas placer cette règle dans `prompt_rules`.

## Vérification du périmètre

Avant de finir, vérifier que le lot n'a pas :

- réécrit largement le README ;
- modifié les prompts ;
- modifié les contrats blackboard ;
- documenté une authentification complète ;
- promis une scalabilité horizontale ;
- documenté une génération automatique sans brief utilisateur.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; print(app.test_client().get('/healthz').status_code if 'healthz' in [rule.endpoint for rule in app.url_map.iter_rules()] else 'no healthz')"
git diff -- README.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml TODO.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle recommandée avant audit :

1. Lancer l'app localement avec `WEB_ACCESS_TOKEN`.
2. Vérifier que `/healthz` répond.
3. Vérifier que `/` est refusé sans token.
4. Vérifier que `/?access_token=<token>` donne accès.
5. Vérifier que les runs existants sont listés.
6. Vérifier qu'un job peut être créé sans lancer de génération réelle si un fake
   runner est utilisé dans un test.

## Critères d'acceptation

- README cohérent avec l'état réel du POC.
- Mémoire `docs/ai` à jour pour les futurs agents.
- Règles web placées dans `web_rules`.
- Aucun contrat blackboard modifié.
- Aucun prompt modifié.
- Aucun output généré modifié.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs courtes, factuelles et alignées avec le code.
- Ne pas mélanger documentation Render et refonte applicative.
- Ne pas introduire de déploiement grand public.
- Ne pas modifier l'historique généré.
