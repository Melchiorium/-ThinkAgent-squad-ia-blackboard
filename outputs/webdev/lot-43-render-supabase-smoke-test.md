# Lot 43 - Smoke test Render Supabase persistant

## Objectif

Définir et documenter le smoke test réel de production durable sur Render avec
Supabase.

Ce lot valide le comportement utilisateur final : titre + brief, génération,
résultat inline, redeploy, résultat toujours visible.

## Contexte projet utile

- Le mode Render gratuit sans Supabase est éphémère.
- Le mode durable attendu utilise Supabase Postgres.
- Le service Render doit être configuré manuellement.
- Le test peut appeler le LLM uniquement pour la génération finale courte.
- Aucune vraie clé ne doit être écrite dans le repo.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md`
- `docs/supabase-poc-storage.md`
- `README.md`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml` seulement si une référence manque

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `flows` et `modules`
   liées à Render et Supabase.
2. Documenter une checklist de configuration Render :
   - `OPENAI_API_KEY`
   - `BLACKBOARD_PROMPT_VERSION=V3`
   - `WEB_ACCESS_TOKEN`
   - `WEB_STORAGE_BACKEND=supabase`
   - `SUPABASE_DATABASE_URL`
3. Documenter les variables à ne pas mettre en mode Supabase gratuit :
   - `WEB_OUTPUTS_ROOT`
   - `WEB_JOBS_ROOT`
4. Documenter l'ordre exact du smoke test :
   - ouvrir `/healthz` ;
   - ouvrir `/readyz` ;
   - ouvrir `/` sans token et vérifier le refus ;
   - ouvrir `/?access_token=<token>` ;
   - saisir un titre de test ;
   - saisir un brief court ;
   - lancer la génération ;
   - attendre `Terminé` ;
   - vérifier PRD, Architecture, Mermaid, GTM et logs inline ;
   - redeploy Render ;
   - rouvrir `/readyz` ;
   - rouvrir la home ;
   - vérifier que le run reste listé et lisible.
5. Après exécution réelle par l'humain ou l'agent autorisé, documenter le
   résultat du test sans secret.

## Comportements attendus

- La doc distingue clairement :
  - smoke test éphémère ;
  - production durable Supabase ;
  - disque Render payant non retenu.
- Le résultat du smoke test ne contient ni token, ni connection string, ni clé
  OpenAI.
- Si le PNG Mermaid est absent, le test accepte le message clair déjà prévu.

## Critères d'acceptation

- La checklist suffit à refaire le test sans décision restante.
- La persistance après redeploy est explicitement vérifiée.
- Les secrets restent hors repo.
- Aucun code runtime n'est modifié dans ce lot.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/render-poc-deployment.md docs/supabase-poc-storage.md README.md docs/ai/flows.yaml docs/ai/modules.yaml
git diff -- app
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Smoke test manuel Render :

```text
1. /healthz -> 200
2. /readyz -> 200 avec backend supabase
3. / sans token -> 403
4. /?access_token=<token> -> home
5. Génération courte -> Terminé
6. Résultat inline lisible
7. Redeploy
8. Run toujours visible
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
