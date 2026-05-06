# Lot 48 - Documentation finale production auditable

## Objectif

Aligner README, mémoire agent et runbook après validation de la production
durable.

Ce lot ferme la phase mise en prod durable et doit laisser le projet clair pour
un audit humain comme pour un futur agent.

## Contexte projet utile

- Supabase est le backend durable recommandé.
- Render gratuit sans Supabase reste un mode éphémère de smoke test.
- `/healthz` est public.
- `/readyz` est protégé par token et sert au contrôle manuel.
- La production reste un POC : pas d'auth complète, pas de comptes, pas de
  scaling horizontal, pas de SLA.

## Fichiers autorisés à modifier

- `README.md`
- `docs/production-audit-runbook.md`
- `docs/render-poc-deployment.md`
- `docs/supabase-poc-storage.md`
- `docs/ai/00-index.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `TODO.md` seulement pour retirer ou classer des éléments devenus faux

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis toutes les entrées de mémoire liées au
   web, Render, Supabase et runbook.
2. Vérifier que README contient :
   - comment tester le viewer ;
   - mode durable Supabase ;
   - lien vers le runbook ;
   - limites POC.
3. Vérifier que `docs/production-audit-runbook.md` est la source courte pour
   l'audit production.
4. Vérifier que `docs/render-poc-deployment.md` ne mélange plus disque Render
   payant et Supabase gratuit.
5. Vérifier que `docs/supabase-poc-storage.md` reste opérationnel.
6. Mettre à jour `docs/ai` pour que les futurs agents trouvent :
   - `web_storage` ;
   - `/readyz` ;
   - `production_audit_runbook` ;
   - `web_supabase_persistence_flow`.
7. Ajuster `TODO.md` uniquement si un item est clairement clos ou faux.
8. Ne pas faire de refactor runtime.

## Comportements attendus

- Un humain sait où cliquer/lire pour auditer la prod.
- Un agent sait quels fichiers lire avant de modifier la prod.
- La documentation ne contient aucun secret.
- La documentation ne promet pas plus que le POC ne fournit.

## Critères d'acceptation

- README, docs Render, docs Supabase, runbook et docs/ai sont cohérents.
- Les limites POC restent explicites.
- Aucun code runtime n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- README.md docs/production-audit-runbook.md docs/render-poc-deployment.md docs/supabase-poc-storage.md docs/ai/00-index.yaml docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml TODO.md
git diff -- app
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs concises et exactes.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
