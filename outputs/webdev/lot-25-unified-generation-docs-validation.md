# Lot 25 - Documentation et validation de l'interface de génération unifiée

## Objectif

Documenter le nouvel usage réel de l'app web :

```text
écrire un brief dans l'interface -> lancer la génération -> lire les résultats dans l'interface
```

Ce lot ne doit pas réécrire largement la documentation. Il doit aligner README
et mémoire projet avec le comportement livré.

## Contexte projet utile

- Les lots 21 à 24 transforment l'expérience web.
- Le backend de génération reste celui des étapes précédentes.
- Le POC reste sans comptes utilisateurs.
- Le stockage reste fichier.
- Render reste un déploiement POC.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une règle courte est utile
- `TODO.md` seulement pour ajuster un risque ou une suite explicitement liée

## Fichiers à ne pas modifier

- `app/` sauf correction mineure découverte pendant validation
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`

## Travail demandé - README

Mettre à jour la section `Viewer Web POC` pour ne plus décrire seulement un
viewer.

La section doit expliquer brièvement :

- ouvrir la home ;
- coller un brief ;
- lancer la génération ;
- suivre le statut ;
- lire PRD, Architecture, Mermaid, GTM et logs dans l'interface ;
- les anciens runs restent consultables ;
- le lien secret `WEB_ACCESS_TOKEN` reste un garde POC.

Ne pas réécrire tout le README.

## Travail demandé - modules.yaml

Mettre à jour l'entrée `web` pour mentionner :

- interface de génération depuis un brief ;
- statut de job ;
- résultat généré affiché dans l'interface ;
- route JSON de statut si le lot 22 l'a ajoutée ;
- partial `_run_result.html` si le lot 23 l'a ajouté ;
- `web.js` si le lot 22 ou 24 l'a ajouté.

Ne pas ajouter de nouveau module sauf si un nouveau fichier Python significatif
a été créé, ce qui n'est pas attendu.

## Travail demandé - flows.yaml

Ajouter ou mettre à jour un flux :

```yaml
web_unified_generation_ui_flow:
  owner: app/web.py and app/templates/
  status: poc_ui
  steps:
    - render generation-first home page
    - accept a brief from the user
    - create a session-scoped generation job
    - show queued/running/done/failed status
    - poll job status when JavaScript is available
    - display generated artifacts inline when the job is done
    - keep existing run detail pages available
  limitations:
    - no full authentication
    - no multi-user accounts
    - no distributed queue
    - no fine-grained agent step telemetry yet
```

Adapter le flux à ce qui a vraiment été implémenté.

## Travail demandé - rules.yaml

Ajouter une règle uniquement si nécessaire, par exemple :

```yaml
- Keep the web UI generation-first: users should be able to submit a brief and
  read the generated dossier without understanding internal run/job paths.
```

Si `rules.yaml` est déjà suffisant, ne pas le modifier.

## Vérification du périmètre

Avant de finir, vérifier que la documentation ne promet pas :

- une authentification complète ;
- des comptes utilisateurs ;
- une queue distribuée ;
- une progression fine par agent si elle n'existe pas ;
- la manipulation de prompts/noeuds si elle n'existe pas encore.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); print(c.get('/').status_code); print(c.get('/healthz').status_code)"
git diff -- README.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml TODO.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle recommandée :

1. Lancer l'app localement avec `WEB_ACCESS_TOKEN`.
2. Ouvrir `/?access_token=<token>`.
3. Coller un brief.
4. Lancer la génération.
5. Vérifier que le statut évolue dans l'interface.
6. Vérifier que le résultat généré est lisible dans l'interface.
7. Vérifier que les anciens runs restent accessibles.

Ne pas lancer une vraie génération LLM sauf accord explicite du mainteneur.

## Critères d'acceptation

- README décrit le flux utilisateur réel.
- `docs/ai/modules.yaml` aide un futur agent à trouver les fichiers UI.
- `docs/ai/flows.yaml` contient le flux unifié.
- La documentation reste alignée avec le comportement réel.
- Aucun contrat blackboard n'est modifié.
- Aucun prompt n'est modifié.
- Aucun output généré n'est modifié.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs courtes et factuelles.
- Ne pas documenter des fonctionnalités non livrées.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux outputs générés.

