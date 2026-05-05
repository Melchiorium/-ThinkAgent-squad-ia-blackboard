# Lot 23 - Résultat généré affiché dans l'interface

## Objectif

Afficher directement le dossier généré dans l'interface de génération quand un
job est terminé.

L'utilisateur ne doit plus devoir comprendre la navigation technique
`jobs -> runs -> artifacts` pour voir le résultat.

## Contexte projet utile

- `run_detail.html` sait déjà afficher les sections d'un run.
- `job_status.html` affiche actuellement seulement un lien `Open generated run`.
- `app/web.py` contient déjà `_build_detail_sections(...)`.
- Les artefacts disponibles sont :
  - `project-brief.md`
  - `prd.md`
  - `architecture.md`
  - `architecture-diagram.mmd`
  - `architecture-diagram.png`
  - `gtm.md`
  - `blackboard.md`
  - `activity_log.txt`

## Fichiers autorisés à modifier

- `app/web.py`
- `app/templates/job_status.html`
- `app/templates/run_detail.html`
- `app/templates/_run_result.html`
- `app/static/web.css`
- `app/static/web.js` seulement si nécessaire pour intégrer le résultat après
  polling

## Fichiers à ne pas modifier

- `app/web_runs.py` sauf bug bloquant
- `app/generation_service.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Travail demandé

Créer un partial Jinja réutilisable :

```text
app/templates/_run_result.html
```

Ce partial doit afficher les sections principales :

- Brief
- PRD
- Architecture
- Diagramme Mermaid
- GTM
- Blackboard
- Activity Log

Puis :

1. utiliser ce partial dans `run_detail.html` ;
2. utiliser ce partial dans `job_status.html` quand le job est `done` ;
3. garder le lien vers la page run comme lien secondaire ;
4. afficher une mention simple si un fichier manque.

## Priorité d'affichage

Sur la page job terminée, mettre en avant :

1. PRD ;
2. Architecture ;
3. Diagramme Mermaid PNG si présent ;
4. GTM ;
5. Brief, Blackboard et Activity Log en sections moins proéminentes.

Implémentation simple acceptable :

- sections en accordéons HTML `<details>` ;
- ou sections empilées avec titres clairs ;
- `<pre>` conservé pour rester simple.

Ne pas convertir le Markdown en HTML dans ce lot.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `app/web.py`, `run_detail.html`, `job_status.html`.
3. Extraire le rendu commun dans `_run_result.html`.
4. Modifier `run_detail.html` pour utiliser le partial sans régression.
5. Modifier `job_status.html` pour inclure le résultat quand le job est `done`.
6. Dans `app/web.py`, fournir `sections` au template job quand un `run_url`
   existe.
7. Ne pas changer les routes d'artefacts.

## Comportements attendus

- Après génération terminée, la page `/jobs/<job_id>` montre directement les
  contenus générés.
- Le lien vers `/runs/<project>/<version>` reste disponible.
- La page `/runs/<project>/<version>` continue de fonctionner.
- Le PNG Mermaid s'affiche si présent.
- Les fichiers manquants ont une mention claire.

## Critères d'acceptation

- Le résultat généré est visible dans la page statut du job terminé.
- `run_detail.html` et `job_status.html` partagent le même rendu de sections.
- Aucun chemin filesystem n'est affiché.
- Les artefacts restent servis par la route allowlist existante.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); print(c.get('/').status_code)"
git diff -- app/web.py app/templates/job_status.html app/templates/run_detail.html app/templates/_run_result.html app/static/web.css app/static/web.js
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle recommandée :

1. Utiliser un job déjà `done` ou un fake runner.
2. Ouvrir `/jobs/<job_id>`.
3. Vérifier que PRD, Architecture, Mermaid, GTM sont visibles sur la page.
4. Ouvrir le lien run et vérifier que le rendu reste cohérent.

Ne pas lancer de vraie génération LLM sauf accord explicite.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Réutiliser le rendu existant au lieu de le dupliquer.
- Garder `<pre>` si c'est le plus simple.
- Ne pas exposer de chemin serveur.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.

