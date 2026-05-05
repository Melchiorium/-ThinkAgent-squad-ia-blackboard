# Lot 39 - Documentation Supabase et Render

## Objectif

Aligner la documentation humaine et la mémoire agent avec la stratégie de
mémoire persistante Supabase Postgres.

Ce lot documente le mode long terme recommandé sans introduire de secrets.

## Contexte projet utile

- Render gratuit fonctionne pour un smoke test, mais le filesystem est
  éphémère.
- Supabase Postgres est retenu comme mémoire persistante recommandée.
- Render persistent disk est une option payante et n'est pas retenue pour ce
  POC gratuit.
- Supabase est utilisé uniquement via Postgres, avec `psycopg[binary]`.
- Pas de Supabase Auth, pas de Supabase Storage, pas d'archivage automatique.

## Fichiers autorisés à modifier

- `README.md`
- `docs/render-poc-deployment.md`
- `docs/supabase-poc-storage.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une règle courte est utile

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules`, `flows` et
   `rules`.
2. Mettre à jour `README.md` avec une section courte sur la mémoire persistante
   Supabase.
3. Corriger `docs/render-poc-deployment.md` pour distinguer :
   - Render gratuit éphémère ;
   - Render gratuit + Supabase persistant ;
   - Render persistent disk payant.
4. Compléter `docs/supabase-poc-storage.md` avec la procédure opérationnelle.
5. Mettre à jour `docs/ai/modules.yaml` pour référencer le backend storage
   Supabase et les modules modifiés.
6. Mettre à jour `docs/ai/flows.yaml` pour ajouter ou ajuster le flux
   `web_supabase_persistence_flow`.
7. Ajouter une règle dans `docs/ai/rules.yaml` seulement si elle prévient un
   risque concret, par exemple ne pas committer de connection string.

## Comportements/documentation attendus

- La doc explique que `/tmp` est un fallback de smoke test éphémère.
- La doc explique que Supabase Postgres est la mémoire persistante recommandée.
- La doc explique que Render persistent disk est payant et non retenu pour ce
  POC gratuit.
- Les variables Render recommandées sont :
  - `OPENAI_API_KEY`
  - `BLACKBOARD_PROMPT_VERSION=V3`
  - `WEB_ACCESS_TOKEN`
  - `WEB_STORAGE_BACKEND=supabase`
  - `SUPABASE_DATABASE_URL`
- La doc ne demande pas `WEB_OUTPUTS_ROOT` ni `WEB_JOBS_ROOT` pour Render
  gratuit + Supabase.
- La procédure indique :
  - créer un projet Supabase ;
  - ouvrir SQL Editor ;
  - exécuter `docs/supabase-schema.sql` ;
  - récupérer la connection string Session Pooler ;
  - configurer Render ;
  - redeploy ;
  - tester une génération ;
  - redeploy à nouveau pour vérifier la persistance.

## Critères d'acceptation

- README est cohérent avec le mode Supabase.
- `docs/render-poc-deployment.md` ne mélange plus disque persistant payant et
  Render gratuit + Supabase.
- `docs/supabase-poc-storage.md` permet à un humain modérément expérimenté de
  configurer Supabase.
- `docs/ai` aide un futur agent à retrouver la logique storage.
- Aucune vraie clé ou connection string n'est écrite.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- README.md docs/render-poc-deployment.md docs/supabase-poc-storage.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs courtes, factuelles et utiles.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Préserver les outputs générés.
