# Lot 24 - UI simple, claire et légèrement animée

## Objectif

Rendre l'interface de génération plus lisible et plus agréable sans changer de
stack.

Ce lot porte sur l'expérience utilisateur : libellés, hiérarchie visuelle,
états, animations CSS légères.

## Contexte projet utile

- Le POC utilise Flask, Jinja, CSS statique et éventuellement `web.js`.
- L'objectif utilisateur est :

```text
écrire un brief -> lancer -> voir la génération avancer -> lire le dossier généré
```

- L'interface ne doit pas devenir une landing page marketing.
- Le POC reste un outil de travail pour audit humain.

## Fichiers autorisés à modifier

- `app/templates/index.html`
- `app/templates/job_status.html`
- `app/templates/run_detail.html`
- `app/templates/_run_result.html`
- `app/static/web.css`
- `app/static/web.js`

## Fichiers à ne pas modifier

- `app/web.py` sauf mini-ajustement de variable de template réellement utile
- `app/generation_service.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `requirements.txt`

## Travail demandé

Améliorer l'interface autour de ces éléments :

- titre clair : `Générer un dossier projet`
- zone brief large, lisible, première dans la page ;
- bouton principal clair ;
- badge de statut visible ;
- état `queued`, `running`, `done`, `failed` distinct ;
- résultat généré lisible par sections ;
- anciens runs placés en zone secondaire ;
- animation CSS légère sur :
  - apparition des panels ;
  - changement visuel du statut ;
  - spinner ou indicateur pendant `queued/running`.

## Contraintes UI

- Ne pas ajouter de framework CSS.
- Ne pas ajouter de dépendance JavaScript.
- Ne pas utiliser de grosses animations.
- Ne pas cacher les informations importantes derrière trop d'interactions.
- Ne pas faire une page marketing.
- Ne pas mettre de texte d'explication long dans l'interface.
- Garder une interface utilisable sur mobile.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire les templates web existants et `app/static/web.css`.
3. Mettre les libellés principaux en français cohérent.
4. Ajouter les classes CSS nécessaires.
5. Ajouter des animations CSS courtes et non bloquantes.
6. Vérifier que les textes longs ne débordent pas.
7. Vérifier que l'interface reste utilisable sans JS.

## Comportements attendus

- L'action principale est évidente.
- Le statut d'un job est lisible immédiatement.
- Un job en cours donne une impression d'activité.
- Un job terminé montre clairement où lire le résultat.
- Les anciens runs restent consultables sans prendre toute la place.

## Critères d'acceptation

- L'interface ne ressemble plus à un inventaire technique.
- Le flux de génération est compréhensible sans documentation.
- Les animations restent sobres.
- Aucun comportement backend n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); r=c.get('/'); print(r.status_code); print('Générer un dossier projet' in r.get_data(as_text=True))"
git diff -- app/templates/index.html app/templates/job_status.html app/templates/run_detail.html app/templates/_run_result.html app/static/web.css app/static/web.js
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle :

1. Ouvrir la home.
2. Vérifier desktop et largeur mobile.
3. Créer un job avec un fake runner ou un brief réel si autorisé.
4. Vérifier les états `queued/running/done/failed`.
5. Vérifier que le résultat reste lisible.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'UI simple pour un développeur/auditeur humain.
- Ne pas introduire de build frontend.
- Ne pas modifier la logique métier.
- Ne pas modifier les prompts ou contrats blackboard.
- Ne pas toucher aux outputs générés.

