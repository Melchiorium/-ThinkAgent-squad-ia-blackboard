# Lot 44 - Runbook audit production

## Objectif

Créer un runbook court pour auditer la mise en production durable du POC web.

Ce runbook doit permettre à un humain ou à un futur agent de comprendre l'état
de production, les limites, les preuves de test et les actions de diagnostic
sans fouiller le repo.

## Contexte projet utile

- Le POC web est déployé sur Render.
- La mémoire persistante durable repose sur Supabase Postgres.
- L'accès reste un guardrail de POC via `WEB_ACCESS_TOKEN`.
- Il n'y a pas de compte utilisateur, pas d'auth complète, pas de queue
  distribuée.
- La génération utilise les agents Product/Growth/Tech existants.

## Fichiers autorisés à modifier

- `docs/production-audit-runbook.md`
- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si un garde-fou d'audit manque

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

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules`, `flows` et
   `rules` liées au web, Render et Supabase.
2. Créer `docs/production-audit-runbook.md`.
3. Le runbook doit contenir :
   - URL Render à renseigner sans token ;
   - variables requises, sans valeurs secrètes ;
   - endpoints de contrôle ;
   - scénario de test utilisateur ;
   - scénario de persistance après redeploy ;
   - limites assumées ;
   - diagnostic rapide des pannes fréquentes.
4. Ajouter dans `README.md` un lien court vers le runbook.
5. Mettre à jour `docs/ai/modules.yaml` ou `docs/ai/flows.yaml` pour référencer
   le runbook si utile.
6. Ne pas ajouter de promesse d'auth complète, de scalabilité ou de SLA.

## Contenu attendu du runbook

Sections minimales :

- `État cible`
- `Variables d'environnement`
- `Endpoints de contrôle`
- `Smoke test`
- `Vérification de persistance`
- `Limites POC`
- `Diagnostic rapide`

Diagnostics à couvrir :

- `/healthz` échoue ;
- `/readyz` échoue ;
- accès sans token refusé ;
- génération en échec OpenAI ;
- Supabase schema absent ;
- résultat visible avant redeploy mais absent après redeploy ;
- PNG Mermaid absent mais `.mmd` présent.

## Critères d'acceptation

- Le runbook permet un audit humain sans lire toute la codebase.
- Aucun secret n'est documenté.
- Les limites POC sont explicites.
- Les preuves de smoke test peuvent être ajoutées sans exposer de token.
- Aucun code runtime n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/production-audit-runbook.md README.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml
git diff -- app
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la documentation courte, factuelle et actionnable.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
