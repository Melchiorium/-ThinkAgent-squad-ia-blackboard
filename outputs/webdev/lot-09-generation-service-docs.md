# Lot 09 - Documentation du service de generation

## Objectif

Documenter l'etape 2 dans la memoire projet et le README, sans annoncer encore
de generation depuis l'interface web.

Le service existe pour preparer l'etape suivante, mais le viewer web reste en
lecture seule a ce stade.

## Contexte projet utile

- Les lots 06 a 08 doivent avoir ajoute :
  - `app/artifact_writer.py`
  - `app/generation_service.py`
  - l'utilisation du service par le chemin CLI standard.
- Le viewer web ne doit pas encore lancer de generation.
- La memoire `docs/ai` doit permettre aux futurs agents de trouver le service
  sans scanner le repo.

## Fichiers autorises a modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`

## Fichiers a ne pas modifier

- `app/`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`, sauf nouvelle regle vraiment necessaire
- `app/prompts V3/`
- `outputs/tests/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`
- `requirements.txt`

## Travail demande - README

Ajouter une courte note dans la section d'execution ou pres du `Viewer Web POC`.

La note doit dire :

- le CLI standard continue de fonctionner avec `python3 app/main.py` ;
- la logique de generation standard est maintenant exposee par
  `app/generation_service.py` pour reuse interne ;
- le viewer web reste en lecture seule dans cette etape ;
- aucune generation depuis le navigateur n'est encore disponible.

Ne pas reecrire le README complet.

## Travail demande - modules.yaml

Ajouter deux modules :

```yaml
- name: artifact_writer
  path: app/artifact_writer.py
  role: >
    Writes run artifacts from a completed blackboard into an output directory:
    project brief, PRD, architecture, Mermaid artifacts, GTM, blackboard, and
    activity log.
  read_when:
    - changing generated artifact files
    - changing blackboard.md rendering
    - debugging Mermaid artifact writing
  key_functions:
    - write_run_artifacts

- name: generation_service
  path: app/generation_service.py
  role: >
    Reusable standard-generation service. Runs the validated standard workflow
    from an in-memory brief and writes a new outputs/tests/<Project>/version X/
    directory.
  read_when:
    - adding non-CLI generation entrypoints
    - changing standard run creation from in-memory briefs
    - debugging output version directory creation
  key_functions:
    - run_generation_from_brief
    - extract_project_name
    - next_project_version_outputs_dir
```

Si les fonctions finales ont des noms legerement differents, documenter les noms
reels.

Mettre a jour l'entree `main` si elle ne reflete plus son role apres refactor :

- elle selectionne le brief CLI ;
- elle delegue le chemin standard a `generation_service` ;
- elle conserve le second pass experimental.

## Travail demande - flows.yaml

Ajouter un flux :

```yaml
standard_generation_service_flow:
  owner: app/generation_service.py
  status: internal_service
  steps:
    - receive an in-memory project brief
    - extract or receive the project name
    - create the next outputs/tests/<Project>/version X/ directory
    - run the validated standard workflow
    - write run artifacts through app/artifact_writer.py
  limitations:
    - no web form integration yet
    - no background jobs
    - no authentication
    - no second-pass handling
```

Ne pas modifier `web_viewer_flow` pour annoncer une generation web.

## Comportements attendus

- La documentation distingue clairement :
  - CLI standard ;
  - service interne reutilisable ;
  - viewer web toujours read-only.
- La memoire projet pointe vers les bons modules.
- Aucun contrat blackboard ne change.
- Aucun prompt ne change.

## Validation

Executer :

```bash
python3 -m compileall app
git diff -- README.md docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Attendus :

- compile OK ;
- README modifie de facon courte et ciblee ;
- `modules.yaml` contient `artifact_writer` et `generation_service` ;
- `flows.yaml` contient `standard_generation_service_flow` ;
- aucun diff sur `contracts.yaml` ;
- aucun diff sur les prompts V3.

## Criteres d'acceptation

- Les nouveaux modules sont documentes dans `docs/ai/modules.yaml`.
- Le nouveau flux interne est documente dans `docs/ai/flows.yaml`.
- Le README ne promet pas encore de generation depuis le navigateur.
- Le viewer web reste decrit comme lecture seule.
- Aucun code applicatif n'est modifie par ce lot.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Mettre a jour la memoire projet quand modules/flux changent.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs generes.
- Garder la documentation factuelle et limitee a l'etat reel.
