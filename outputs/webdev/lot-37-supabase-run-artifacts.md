# Lot 37 - Persistance Supabase des artefacts de run

## Objectif

Sauvegarder les artefacts d'un run terminé dans Supabase Postgres quand
`WEB_STORAGE_BACKEND=supabase`.

Le backend fichier doit rester inchangé.

## Contexte projet utile

- `app/generation_service.py` écrit déjà un dossier de run via
  `app/artifact_writer.py`.
- `app/web.py` lance la génération web et marque le job `done` quand elle
  réussit.
- Les artefacts attendus sont les fichiers déjà listés par `app/web_runs.py`.
- En mode Supabase, le dossier local généré peut être temporaire ou éphémère.
  La source de vérité long terme doit devenir la table `web_run_artifacts`.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_storage.py`
- `app/web_runs.py` seulement si nécessaire pour partager la liste des fichiers
  attendus ou les métadonnées d'artefacts
- `docs/supabase-poc-storage.md` seulement si nécessaire

## Fichiers à ne pas modifier

- `app/generation_service.py` sauf nécessité technique explicitement justifiée
- `app/artifact_writer.py` sauf nécessité technique explicitement justifiée
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules` et `flows`
   concernant `web`, `web_runs`, `artifact_writer` et `generation_service`.
2. Ajouter dans le storage Supabase une opération pour sauvegarder les artefacts
   d'un run terminé.
3. Après une génération web réussie, lire les fichiers présents dans le dossier
   de sortie local.
4. En mode Supabase, insérer ou mettre à jour les artefacts dans
   `web_run_artifacts`.
5. En mode fichier, ne rien changer au flux actuel.
6. Ne pas faire échouer un run uniquement parce que le PNG Mermaid est absent.
7. Ne pas exposer les chemins locaux comme source de vérité Supabase.

## Artefacts à persister

```text
project-brief.md          text/markdown
prd.md                    text/markdown
architecture.md           text/markdown
architecture-diagram.mmd  text/plain
architecture-diagram.png  image/png, bytea, optionnel
gtm.md                    text/markdown
blackboard.md             text/markdown
activity_log.txt          text/plain
```

## Comportements attendus

- Les fichiers Markdown, TXT et MMD sont stockés dans `content_text`.
- Le PNG, s'il existe, est stocké dans `content_bytes`.
- `content_type` est toujours renseigné.
- `version_number` est extrait de `version X`.
- Les artefacts peuvent être réécrits proprement pour le même
  `(run_project, run_version, filename)`.
- Si un fichier texte attendu manque, il n'est pas sauvegardé et sera affiché
  comme absent par les lots suivants.
- Si `architecture-diagram.png` manque, ce n'est pas une erreur.

## Critères d'acceptation

- Un job web terminé en mode Supabase sauvegarde ses artefacts présents.
- Un run sans PNG termine quand même en `done`.
- Le backend `file` reste inchangé.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
git diff -- app/web.py app/web_storage.py app/web_runs.py docs/supabase-poc-storage.md
git diff -- app/generation_service.py app/artifact_writer.py
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Prévoir ou exécuter un test avec fake runner sans appel LLM si le projet a déjà
une convention de test manuel web.

Validation Supabase réelle seulement si la variable est disponible :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 -m gunicorn --check-config app.web:app
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le flux Product/Growth/Tech inchangé.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
- Ne pas écrire ou afficher de secret.
