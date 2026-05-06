# Lot 47 - Preuve de smoke test production durable

## Objectif

Documenter le résultat du smoke test réel Render + Supabase après
configuration production.

Ce lot ne doit pas modifier le fonctionnement applicatif. Il sert à produire
une preuve d'audit sans exposer de secrets.

## Contexte projet utile

- Render est configuré avec `WEB_STORAGE_BACKEND=supabase`.
- Supabase contient les tables `web_jobs` et `web_run_artifacts`.
- `/readyz` est protégé par token et doit confirmer le backend durable.
- Le smoke test doit vérifier la persistance après redeploy.

## Fichiers autorisés à modifier

- `docs/render-poc-deployment.md`
- `docs/production-audit-runbook.md`
- `README.md` seulement si un statut court doit être ajouté
- `docs/ai/flows.yaml` seulement si le résultat du flow doit être précisé

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

1. Lire `docs/ai/00-index.yaml`, puis la doc Render/Supabase/runbook.
2. Exécuter ou faire exécuter le smoke test réel :
   - `/healthz` -> `200` ;
   - `/readyz?access_token=<token>` -> `200`, backend `supabase` ;
   - `/` sans token -> `403` ;
   - `/?access_token=<token>` -> home visible ;
   - génération courte avec titre explicite ;
   - statut final `Terminé` ;
   - PRD, Architecture, Mermaid, GTM et logs visibles inline ;
   - redeploy Render ;
   - `/readyz?access_token=<token>` toujours OK ;
   - run toujours visible et lisible.
3. Documenter le résultat avec :
   - date ;
   - URL du service sans token ;
   - titre du projet de test ;
   - job id si non sensible ;
   - statut final ;
   - vérification post-redeploy.
4. Ne jamais documenter le token, la clé OpenAI ou la connection string.
5. Si le PNG Mermaid est absent mais `.mmd` visible, documenter que c'est
   acceptable pour ce POC.

## Comportements attendus

- La preuve est lisible par un auditeur humain.
- La preuve montre explicitement que la persistance survit au redeploy.
- Les secrets ne sont pas exposés.
- Les limites POC restent visibles.

## Critères d'acceptation

- Le smoke test durable est documenté.
- Le résultat post-redeploy est documenté.
- Aucun code runtime n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/render-poc-deployment.md docs/production-audit-runbook.md README.md docs/ai/flows.yaml
git diff -- app
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

Smoke test manuel :

```text
/healthz -> 200
/readyz?access_token=<token> -> 200 backend supabase
/ sans token -> 403
génération courte -> Terminé
redeploy Render
run toujours visible
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
