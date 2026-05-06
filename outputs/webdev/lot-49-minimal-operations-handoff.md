# Lot 49 - Passation opérations minimale

## Objectif

Préparer une passation minimale pour garder le projet accessible dans le temps
sans maintenance active.

Ce lot documente quoi vérifier périodiquement, quoi faire en cas de panne et
quelles évolutions reporter.

## Contexte projet utile

- Le projet est un POC durable, pas un service grand public.
- Render héberge l'app.
- Supabase conserve jobs et artefacts.
- OpenAI reste une dépendance externe pour les nouvelles générations.
- Les résultats déjà générés doivent rester lisibles même si une nouvelle
  génération échoue.

## Fichiers autorisés à modifier

- `docs/production-audit-runbook.md`
- `README.md`
- `TODO.md`
- `docs/ai/rules.yaml` seulement si un garde-fou opérations manque

## Fichiers à ne pas modifier

- `app/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis `docs/production-audit-runbook.md`.
2. Ajouter une section courte “Opérations minimales” :
   - vérifier `/healthz` ;
   - vérifier `/readyz?access_token=<token>` ;
   - vérifier qu'un run existant reste lisible ;
   - vérifier les variables Render si une génération échoue.
3. Ajouter une section “Pannes fréquentes” :
   - OpenAI key invalide ;
   - modèle invalide ;
   - Supabase URL invalide ;
   - schema Supabase absent ;
   - Render redeploy ;
   - PNG Mermaid absent.
4. Ajouter une section “À ne pas faire sans nouveau lot” :
   - full auth ;
   - comptes utilisateurs ;
   - queue distribuée ;
   - migration Astro ;
   - archivage automatique.
5. Mettre à jour `TODO.md` avec les suites hors prod minimale si nécessaire.
6. Ne pas modifier le runtime.

## Comportements attendus

- La passation est compréhensible par un humain modérément expérimenté.
- Elle indique les checks les plus utiles sans créer une fausse promesse de SLA.
- Elle distingue résultats déjà persistés et nouvelles générations.

## Critères d'acceptation

- Le runbook explique quoi vérifier à froid.
- Le README renvoie vers le runbook.
- TODO ne contient que des suites utiles et non bloquantes.
- Aucun code runtime n'est modifié.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- docs/production-audit-runbook.md README.md TODO.md docs/ai/rules.yaml
git diff -- app
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la passation courte et pratique.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
