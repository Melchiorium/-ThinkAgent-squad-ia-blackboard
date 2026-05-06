# Runbook d'audit production

Runbook court pour vérifier le viewer web en production durable sans relire la
codebase.

## État cible

- service Render actif ;
- `WEB_ACCESS_TOKEN` configuré ;
- `BLACKBOARD_PROMPT_VERSION=V3` ;
- `WEB_STORAGE_BACKEND=supabase` ;
- `SUPABASE_DATABASE_URL` configurée ;
- `/healthz` reste léger ;
- `/readyz` vérifie la persistance durable et suit le même token que
  l'application si un token est configuré ;
- un seul worker Render ;
- pas de compte utilisateur ;
- pas de queue distribuée.

## Variables d'environnement

Requises :

- `OPENAI_API_KEY`
- `BLACKBOARD_PROMPT_VERSION=V3`
- `WEB_ACCESS_TOKEN`
- `WEB_STORAGE_BACKEND=supabase`
- `SUPABASE_DATABASE_URL`

À ne pas utiliser pour le chemin durable recommandé :

- `WEB_OUTPUTS_ROOT`
- `WEB_JOBS_ROOT`

## Endpoints de contrôle

- `/healthz` : santé du service ;
- `/readyz` : readiness stockage ;
- `/?access_token=<token>` : accès partagé ;
- `/jobs/<job_id>` : suivi d'une génération ;
- `/runs/<project>/<version>` : résultat final ;
- `/runs/<project>/<version>/artifacts/<filename>` : artefacts allowlistés.

## Smoke test

1. ouvrir `/healthz` et confirmer `200` ;
2. ouvrir `/readyz` avec le token configuré et confirmer `200` avec backend
   `supabase` ;
3. ouvrir `/` sans token et confirmer le refus `403` ;
4. ouvrir `/?access_token=<token>` ;
5. saisir un titre de projet ;
6. saisir un brief court ;
7. lancer la génération ;
8. attendre `Terminé` ;
9. vérifier PRD, Architecture, Mermaid, GTM et logs inline ;
10. vérifier l'URL du run complet ;
11. redeployer Render ;
12. rouvrir `/readyz` ;
13. rouvrir la home ;
14. confirmer que le run reste listé et lisible.

## Vérification de persistance

- le job reste lisible après redeploy ;
- le run reste présent dans la liste ;
- les artefacts restent lisibles ;
- si le PNG Mermaid manque mais que `.mmd` est présent, le résultat reste
  acceptable si la source Mermaid est affichée clairement.

## Limites POC

- pas d'authentification complète ;
- pas de comptes ;
- pas de rôles ;
- pas de queue distribuée ;
- pas de scalabilité horizontale ;
- pas de SLA ;
- pas d'archivage automatique.

## Diagnostic rapide

- `/healthz` échoue : vérifier le process Render, le `Procfile` et les logs de
  démarrage ;
- `/readyz` échoue : vérifier `WEB_STORAGE_BACKEND`, `SUPABASE_DATABASE_URL`
  et l'existence / accessibilité des tables `web_jobs` / `web_run_artifacts` ;
- accès sans token refusé : attendu ;
- génération en échec OpenAI : vérifier `OPENAI_API_KEY` et les logs du job ;
- schéma Supabase absent : exécuter `docs/supabase-schema.sql` ;
- résultat visible avant redeploy mais absent après : vérifier le backend
  Supabase et l'URL de connexion ;
- PNG Mermaid absent mais `.mmd` présent : acceptable si la source Mermaid est
  disponible.

## Opérations minimales

- vérifier `/healthz` ;
- vérifier `/readyz?access_token=<token>` ;
- vérifier qu'un run existant reste lisible ;
- vérifier les variables Render si une génération échoue ;
- conserver le même couple `WEB_STORAGE_BACKEND=supabase` et
  `SUPABASE_DATABASE_URL` pour le mode durable.

## Pannes fréquentes

- clé OpenAI invalide ;
- modèle invalide ou indisponible ;
- URL Supabase invalide ;
- schéma Supabase absent ;
- redeploy Render pendant une génération ;
- PNG Mermaid absent alors que `.mmd` est présent.

## À ne pas faire sans nouveau lot

- auth complète ;
- comptes utilisateurs ;
- queue distribuée ;
- migration Astro ;
- archivage automatique ;
- stockage de secrets dans le repo.
