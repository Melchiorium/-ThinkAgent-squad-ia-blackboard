# Lot 40 - Validation storage Supabase

## Objectif

Créer une validation reproductible du backend de stockage web, sans appel LLM.

Le script doit vérifier le backend actif (`file` ou `supabase`) et permettre de
confirmer que les jobs et artefacts peuvent être créés, relus et listés.

## Contexte projet utile

- Le backend fichier doit rester disponible pour le local.
- Le backend Supabase doit être testable uniquement si `SUPABASE_DATABASE_URL`
  est disponible.
- Le script ne doit jamais appeler OpenAI ni lancer le workflow
  Product/Growth/Tech.
- Les données de test peuvent rester en base : pas d'archivage automatique dans
  cette phase.

## Fichiers autorisés à modifier

- `scripts/check_web_storage.py`
- `docs/supabase-poc-storage.md` seulement pour documenter le script
- `README.md` seulement pour référencer brièvement la validation
- storage module uniquement si une petite correction est nécessaire pour rendre
  le script testable

## Fichiers à ne pas modifier

- `app/generation_service.py`
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules` et `flows`
   concernant le viewer web et le storage Supabase.
2. Créer `scripts/check_web_storage.py`.
3. Faire détecter le backend actif via `WEB_STORAGE_BACKEND`.
4. En mode `file`, utiliser un répertoire temporaire contrôlé pour ne pas
   polluer les outputs générés.
5. En mode `supabase`, exiger `SUPABASE_DATABASE_URL`.
6. Créer un job de test pour le projet `Storage Check`.
7. Mettre à jour le job en `running`, puis `done`.
8. Sauvegarder des artefacts fake sans appel LLM.
9. Relire le job, lister les jobs, lister les runs et relire au moins un
   artefact.
10. Ne pas afficher de secret.

## Données fake attendues

Projet :

```text
Storage Check
```

Version :

```text
version 1
```

Artefacts fake minimaux :

```text
project-brief.md
prd.md
architecture.md
architecture-diagram.mmd
gtm.md
blackboard.md
activity_log.txt
```

Le PNG est optionnel et ne doit pas être requis pour valider le script.

## Comportements attendus

- Le script n'appelle aucun LLM.
- Le script indique clairement le backend testé.
- Le script échoue clairement si `WEB_STORAGE_BACKEND=supabase` sans
  `SUPABASE_DATABASE_URL`.
- Le script ne masque pas une erreur réelle de connexion Supabase.
- Le script ne supprime pas automatiquement les données Supabase créées.
- Le script ne crée pas d'outputs générés à committer.

## Critères d'acceptation

- `python3 scripts/check_web_storage.py` fonctionne en mode défaut `file`.
- `WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py` fonctionne.
- En mode Supabase sans `SUPABASE_DATABASE_URL`, le message d'erreur est clair.
- En mode Supabase avec variable configurée et schéma appliqué, le script valide
  jobs et artefacts.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun secret n'est affiché.

## Commandes de validation

```bash
python3 -m compileall app
python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=supabase python3 scripts/check_web_storage.py
```

La dernière commande doit échouer proprement si `SUPABASE_DATABASE_URL` est
absent.

Validation Supabase réelle seulement si configurée :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 scripts/check_web_storage.py
```

Smoke test Render manuel après implémentation complète :

```text
1. Déployer avec WEB_STORAGE_BACKEND=supabase.
2. Générer un run court.
3. Vérifier le résultat inline.
4. Redéployer Render.
5. Vérifier que le run reste visible.
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas appeler de LLM dans le script.
- Ne pas écrire de secrets.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
