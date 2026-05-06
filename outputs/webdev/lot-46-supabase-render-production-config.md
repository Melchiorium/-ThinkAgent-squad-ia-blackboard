# Lot 46 - Configuration production Render + Supabase

## Objectif

Guider la configuration réelle de Render et Supabase pour passer du code prêt
à une instance durable.

Ce lot est principalement opérationnel et documentaire. Il ne doit pas ajouter
de secret au repo.

## Contexte projet utile

- Les lots 41 à 45 doivent être terminés avant celui-ci.
- `docs/supabase-schema.sql` existe et doit être appliqué dans Supabase.
- `WEB_STORAGE_BACKEND=supabase` est le mode durable.
- `/healthz` reste public.
- `/readyz` doit être protégé par `WEB_ACCESS_TOKEN` et utilisé manuellement.
- Le mode Render gratuit + Supabase ne doit pas utiliser `WEB_OUTPUTS_ROOT` ni
  `WEB_JOBS_ROOT`.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md`
- `docs/supabase-poc-storage.md`
- `docs/production-audit-runbook.md`
- `README.md`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`

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

1. Lire `docs/ai/00-index.yaml`, puis les entrées liées à Render, Supabase et
   au runbook production.
2. Vérifier que la documentation donne l'ordre exact :
   - créer projet Supabase ;
   - ouvrir Supabase SQL Editor ;
   - exécuter `docs/supabase-schema.sql` ;
   - récupérer la connection string Session Pooler ;
   - configurer Render ;
   - redeploy.
3. Vérifier que les variables Render listées sont exactement :
   - `OPENAI_API_KEY`
   - `BLACKBOARD_PROMPT_VERSION=V3`
   - `WEB_ACCESS_TOKEN`
   - `WEB_STORAGE_BACKEND=supabase`
   - `SUPABASE_DATABASE_URL`
4. Vérifier que la doc indique explicitement de supprimer/ne pas définir :
   - `WEB_OUTPUTS_ROOT`
   - `WEB_JOBS_ROOT`
5. Ajouter une checklist “avant redeploy” et “après redeploy”.
6. Ne pas écrire de vraie URL de DB, clé OpenAI ou token.

## Comportements attendus

- Un humain peut configurer Supabase et Render sans revenir poser de question.
- Le mode durable est clairement séparé du mode smoke test éphémère.
- Le runbook renvoie vers les bons documents.
- La documentation ne promet pas d'auth complète, de compte utilisateur ou de
  scalabilité.

## Critères d'acceptation

- La checklist de configuration production est décision-complète.
- Aucune variable de disque Render n'est requise dans le mode Supabase.
- Aucun secret n'est présent.
- Aucun code runtime n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/render-poc-deployment.md docs/supabase-poc-storage.md docs/production-audit-runbook.md README.md docs/ai/flows.yaml docs/ai/modules.yaml
git diff -- app
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas écrire de secrets.
- Garder la documentation simple et actionnable.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
