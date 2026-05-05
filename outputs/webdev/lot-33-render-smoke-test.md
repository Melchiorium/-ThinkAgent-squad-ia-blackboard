# Lot 33 - Smoke test web déployé

## Objectif

Définir et exécuter le test d'acceptation final sur l'URL Render.

Ce lot suppose que le service Render existe et que les variables/disk ont été
configurés selon les lots 31 et 32.

## Contexte projet utile

- Le service Render est protégé par `WEB_ACCESS_TOKEN`.
- `/healthz` doit rester accessible sans token.
- Le formulaire web demande un titre projet et un brief.
- Le résultat doit s'afficher inline dans la page de suivi de génération.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md` pour ajouter les résultats du smoke test
- `README.md` seulement pour une note courte si le test révèle une précision
  utile
- `TODO.md` seulement pour noter un risque constaté

## Fichiers à ne pas modifier

- `app/` sauf correction bloquante explicitement justifiée
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `render.yaml`

## Préconditions

Avant d'exécuter ce lot, vérifier :

- l'URL Render existe ;
- `OPENAI_API_KEY` est configuré côté Render ;
- `BLACKBOARD_PROMPT_VERSION=V3` est configuré ;
- `WEB_ACCESS_TOKEN` est configuré ;
- `WEB_OUTPUTS_ROOT=/var/data/outputs` est configuré ;
- `WEB_JOBS_ROOT=/var/data/web-jobs` est configuré ;
- le disque persistant est monté sur `/var/data`.

## Scénario smoke test

Utiliser :

```text
Titre du projet: Yoyo Web Test
```

Brief court recommandé :

```text
Créer un dossier MVP pour virtualiser l'expérience d'un jouet yo-yo dans une
application web simple. Le produit doit aider un utilisateur à comprendre les
principes physiques du yo-yo, tester quelques paramètres, et obtenir une
visualisation simple.
```

Étapes :

1. ouvrir `https://<render-host>/healthz` ;
2. vérifier `200` ;
3. ouvrir `https://<render-host>/` sans token ;
4. vérifier que l'accès est refusé ;
5. ouvrir `https://<render-host>/?access_token=<token>` ;
6. vérifier que la home est visible ;
7. saisir le titre projet ;
8. saisir le brief ;
9. lancer la génération ;
10. suivre le statut ;
11. attendre `Terminé` ;
12. vérifier le résultat inline :
    - PRD visible ;
    - Architecture visible ;
    - Mermaid visible ou message clair si PNG absent ;
    - GTM visible ;
13. revenir à la home ;
14. vérifier que le run apparaît dans les runs existants.

## Critères d'acceptation

- `/healthz` retourne `200`.
- `/` sans token est refusé.
- `/?access_token=<token>` donne accès.
- La génération réelle se termine.
- Le run est nommé selon le titre `Yoyo Web Test`.
- Le résultat est lisible par un auditeur non technique.
- Aucun secret n'est écrit dans la doc.

## Vérification persistance

Après le smoke test :

1. redémarrer ou redeployer le service Render ;
2. rouvrir la home avec token ;
3. vérifier que `Yoyo Web Test` reste listé ;
4. rouvrir le run ;
5. vérifier que les sections principales restent visibles.

## Documentation des résultats

Dans `docs/render-poc-deployment.md`, ajouter une courte section :

```text
Smoke test
```

Elle doit contenir :

- date du test ;
- URL Render sans token secret complet ;
- résultat `/healthz` ;
- résultat accès sans token ;
- nom du run généré ;
- statut final ;
- notes éventuelles.

Ne jamais écrire `OPENAI_API_KEY` ou le token complet.

## Commandes utiles

```bash
curl -i https://<render-host>/healthz
curl -i https://<render-host>/
```

Les étapes de formulaire peuvent être faites manuellement dans le navigateur.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés depuis Render.
- Ne pas écrire de secrets dans la documentation.

