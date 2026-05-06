# Lot 50 - Correctif statut production et warning RLS Supabase

## Objectif

Corriger la documentation des derniers lots de mise en production pour :

1. ne pas présenter le smoke test durable Supabase comme validé tant qu'il ne
   l'est pas ;
2. clarifier que la base de données à ne pas créer est une base managée Render,
   pas le projet Supabase requis ;
3. documenter l'avertissement Supabase “New tables will not have Row Level
   Security enabled” sans modifier le schéma à l'aveugle.

## Contexte projet utile

- Le mode durable attendu est `WEB_STORAGE_BACKEND=supabase`.
- Le smoke test réellement observé à date indique encore `backend: file` sur
  `/readyz`.
- Supabase est utilisé comme Postgres serveur via `SUPABASE_DATABASE_URL` et
  `psycopg`.
- L'application ne doit jamais exposer `SUPABASE_DATABASE_URL` côté navigateur.
- Le repo ne doit pas contenir de clé OpenAI, token d'accès ou connection
  string Supabase.
- Le warning RLS Supabase concerne surtout l'exposition via l'API Supabase avec
  les clés `anon` ou `authenticated`.
- Le POC actuel ne prévoit pas Supabase Auth, Supabase Storage, ni accès direct
  frontend aux tables.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md`
- `docs/supabase-poc-storage.md`
- `docs/production-audit-runbook.md`
- `README.md` seulement si une phrase courte évite une contradiction
- `docs/ai/flows.yaml` seulement si le statut du smoke test durable doit être
  clarifié pour les futurs agents
- `docs/ai/rules.yaml` seulement si un garde-fou RLS/secrets manque

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `docs/supabase-schema.sql`, sauf décision explicite de modifier la stratégie
  RLS après validation du rôle Postgres utilisé par Render
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`, sauf demande explicite utilisateur

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées liées à Render, Supabase,
   web storage et runbook production.
2. Dans `docs/render-poc-deployment.md`, remplacer la formulation
   “ne pas créer de base de données” par une formulation non ambiguë :
   - “ne pas créer de base de données Render managée” ;
   - ou “ne pas ajouter de base Render, Supabase est le Postgres retenu”.
3. Dans la section smoke test, séparer clairement :
   - le smoke test éphémère déjà réalisé avec `backend: file` ;
   - le smoke test durable Supabase encore non validé ;
   - les critères exacts à remplir pour le marquer validé.
4. Ne pas écrire que le lot 47 est terminé tant que :
   - `/readyz?access_token=<token>` ne répond pas `backend: supabase` ;
   - une génération réelle n'est pas terminée ;
   - le run n'est pas encore visible après redeploy Render.
5. Dans `docs/supabase-poc-storage.md`, ajouter une section courte sur le
   warning RLS Supabase :
   - expliquer que le warning est attendu après création des tables ;
   - expliquer que l'app utilise une connexion Postgres serveur, pas les clés
     frontend `anon` / `authenticated` ;
   - rappeler de ne jamais exposer `SUPABASE_DATABASE_URL` au navigateur ;
   - indiquer qu'il ne faut pas activer/modifier RLS sans lot dédié et test
     `/readyz` + `scripts/check_web_storage.py`.
6. Dans `docs/production-audit-runbook.md`, ajouter le diagnostic :
   - si `/readyz` renvoie `backend: file`, la production durable n'est pas
     active ;
   - si Supabase affiche le warning RLS, vérifier qu'aucune clé frontend
     Supabase n'est utilisée par l'application avant de changer le schéma.
7. Vérifier qu'aucun secret ou token réel n'a été ajouté.

## Comportements attendus

- La documentation ne confond plus :
  - Render éphémère ;
  - Render + Supabase durable ;
  - Render avec disque payant.
- Un humain comprend que Supabase doit bien être créé et configuré.
- Un humain comprend que le warning RLS n'empêche pas forcément d'exécuter le
  schéma pour ce POC backend-only.
- Un futur agent ne doit pas activer RLS ou ajouter des policies sans lot dédié.
- Le statut de production durable reste “non validé” tant que le smoke test
  Supabase + redeploy n'a pas été prouvé.

## Critères d'acceptation

- `docs/render-poc-deployment.md` ne prétend pas que le smoke test durable est
  validé.
- `docs/render-poc-deployment.md` ne dit plus simplement “ne pas créer de base
  de données” sans qualifier Render.
- `docs/supabase-poc-storage.md` explique le warning RLS et la posture retenue.
- `docs/production-audit-runbook.md` indique quoi faire si `/readyz` reste en
  backend `file`.
- Aucun code runtime n'est modifié.
- Aucun schéma SQL n'est modifié sans décision explicite.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun secret n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/render-poc-deployment.md docs/supabase-poc-storage.md docs/production-audit-runbook.md README.md docs/ai/flows.yaml docs/ai/rules.yaml
git diff -- app
git diff -- docs/supabase-schema.sql
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Vérification manuelle attendue

- Relire la section Render et vérifier que Supabase est clairement présenté
  comme la mémoire durable recommandée.
- Relire la section smoke test et vérifier que le test durable est marqué
  bloqué / non validé tant que `/readyz` reste en `backend: file`.
- Relire la note RLS et vérifier qu'elle ne demande pas de désactiver une
  sécurité ni de publier des clés Supabase côté client.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les corrections documentaires simples et factuelles.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
