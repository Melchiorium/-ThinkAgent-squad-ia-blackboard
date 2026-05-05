# Lot 05b - Correction du scope documentation

## Objectif

Corriger les deux findings d'audit du lot 05 sans élargir le périmètre :

1. Le README a été réécrit trop largement alors que le lot 05 demandait seulement
   une courte section `Viewer Web POC`.
2. L'entrée `web` dans `docs/ai/modules.yaml` ne décrit pas assez les routes
   réellement implémentées : liste des runs, détail d'un run et service
   d'artefacts allowlistés.

Ce lot ne doit pas modifier l'implémentation Flask.

## Contexte projet utile

- Le viewer web POC existe déjà.
- Les lots 1 à 4 ont ajouté :
  - `app/web_runs.py`
  - `app/web.py`
  - `app/templates/index.html`
  - `app/templates/run_detail.html`
  - `app/static/web.css`
- Le lot 05 est strictement documentaire.
- Le README doit rester centré sur le contenu déjà validé du projet, avec un
  ajout minimal pour le viewer.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`

## Fichiers à ne pas modifier

- `app/web.py`
- `app/web_runs.py`
- `app/templates/`
- `app/static/`
- `app/main.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`, sauf si une incohérence évidente est découverte avec
  `web_viewer_flow`.
- `outputs/tests/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`

## Finding 1 a corriger - README trop largement réécrit

### Problème

Le lot 05 a remplacé une grande partie du README : introduction, périmètre,
architecture, livrables, preuve, exécution et guides de lecture.

Ce n'était pas demandé. Cela augmente le risque de supprimer ou modifier du
contexte utile à l'audit humain.

### Travail demandé

1. Restaurer le contenu README hors section web à l'état antérieur au lot 05.
2. Conserver uniquement un ajout documentaire court pour le viewer.
3. Ajouter la section `## Viewer Web POC` à un endroit logique, idéalement après
   les instructions d'exécution ou après la présentation des livrables.
4. La section doit rester courte et factuelle.

### Contenu attendu de la section

La section doit expliquer uniquement :

```markdown
## Viewer Web POC

Le viewer web POC permet de consulter les runs existants sous
`outputs/tests/<Project>/version X/` depuis un navigateur.

Il ne lance aucune génération, aucun appel LLM et aucun formulaire de brief.

Pour le démarrer localement :

```bash
python3 app/web.py
```

Par défaut, le serveur écoute sur `http://127.0.0.1:8000`.
Pour un POC contrôlé sur le réseau local, utiliser :

```bash
WEB_HOST=0.0.0.0 python3 app/web.py
```
```

Adapter légèrement la formulation si nécessaire, mais ne pas ajouter de promesse
sur la génération web, les jobs, Render, l'authentification ou les comptes.

## Finding 2 a corriger - mémoire `web` incomplète

### Problème

Dans `docs/ai/modules.yaml`, l'entrée `web` décrit surtout la page d'accueil,
alors que l'implémentation actuelle couvre aussi :

- la page détail d'un run ;
- la lecture des artefacts texte ;
- l'affichage du PNG Mermaid ;
- le service d'artefacts allowlistés.

### Travail demandé

Mettre à jour uniquement l'entrée `web` dans `docs/ai/modules.yaml`.

Le rôle doit mentionner explicitement :

- serveur Flask du viewer POC ;
- liste des runs sur `/` ;
- détail d'un run sur `/runs/<project>/<version>` ;
- service des artefacts allowlistés sur
  `/runs/<project>/<version>/artifacts/<filename>`.

Le `read_when` doit couvrir :

- changement des routes Flask ;
- changement des templates ;
- changement de l'affichage des artefacts ;
- changement des garde-fous de service fichier.

Le `key_functions` peut lister au minimum :

- `app`
- `index`
- `run_detail`
- `run_artifact`

Ne pas modifier l'entrée `web_runs` sauf si une incohérence évidente est liée à
ce finding.

## Comportements attendus

- Le diff README doit être minimal et limité à l'ajout de la section viewer.
- La mémoire `docs/ai/modules.yaml` doit orienter correctement un futur agent
  vers `app/web.py` pour les routes, les templates et les artefacts.
- Aucun code applicatif ne doit changer.
- Aucun contrat blackboard ne doit changer.
- Aucun prompt ne doit changer.

## Critères d'acceptation

- `git diff README.md` ne montre plus une refonte complète du document.
- `README.md` contient une section `Viewer Web POC`.
- `docs/ai/modules.yaml` décrit clairement les routes et responsabilités du
  module `web`.
- `docs/ai/contracts.yaml` reste inchangé.
- `app/prompts V3/` reste inchangé.

## Validation

Exécuter :

```bash
python3 -m compileall app
```

Puis vérifier :

```bash
git diff -- README.md docs/ai/modules.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Attendus :

- le diff README est limité à l'ajout de la section viewer ;
- le diff `modules.yaml` est limité à l'amélioration de l'entrée `web` ;
- aucun diff sur `contracts.yaml` ;
- aucun diff sur les prompts V3.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Respecter le périmètre du lot.
- Garder les modifications documentaires minimales.
- Ne pas modifier les outputs générés.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
