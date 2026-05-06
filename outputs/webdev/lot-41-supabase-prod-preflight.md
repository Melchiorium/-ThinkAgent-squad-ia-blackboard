# Lot 41 - Préflight Supabase production

## Objectif

Vérifier que le backend Supabase est prêt pour une mise en production durable
sur Render, sans lancer de génération LLM.

Ce lot doit permettre de détecter tôt les erreurs de dépendance, de schéma,
de variable d'environnement ou de connexion Supabase.

## Contexte projet utile

- Le backend Supabase est implémenté dans `app/web_storage.py`.
- Le schéma SQL est dans `docs/supabase-schema.sql`.
- Le script de validation sans LLM est `scripts/check_web_storage.py`.
- Le mode production durable retenu est :
  - `WEB_STORAGE_BACKEND=supabase`
  - `SUPABASE_DATABASE_URL=<Session Pooler connection string>`
- Le backend `file` reste le défaut local.
- `TODO.md` peut être déjà modifié localement par l'utilisateur : ne pas y
  toucher dans ce lot.

## Fichiers autorisés à modifier

- `scripts/check_web_storage.py`
- `app/web_storage.py`
- `docs/supabase-poc-storage.md`
- `docs/render-poc-deployment.md`
- `README.md` seulement si une précision de préflight est nécessaire

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées `modules`, `flows` et
   `rules` liées à `web_storage`.
2. Vérifier que `scripts/check_web_storage.py` teste clairement :
   - backend actif ;
   - présence de `SUPABASE_DATABASE_URL` en mode Supabase ;
   - création job ;
   - update job ;
   - persistance artefacts ;
   - lecture runs ;
   - lecture artefact.
3. Si nécessaire, améliorer les messages d'erreur du script pour distinguer :
   - dépendance `psycopg` absente ;
   - `SUPABASE_DATABASE_URL` absente ;
   - schéma Supabase absent ;
   - erreur de connexion Supabase.
4. Ne jamais afficher la connection string ou le mot de passe.
5. Ajouter à la doc Supabase une section courte “Préflight production”.
6. Ne pas lancer de génération LLM.

## Comportements attendus

- En mode `file`, le script passe sans Supabase.
- En mode `supabase` sans `SUPABASE_DATABASE_URL`, le script échoue proprement.
- En mode `supabase` avec `SUPABASE_DATABASE_URL`, le script valide réellement
  la base si le schéma est appliqué.
- Les données de test peuvent rester en base, comme décidé précédemment.
- Aucune vraie clé n'est écrite dans le repo.

## Critères d'acceptation

- Les erreurs de préflight sont actionnables pour un humain.
- Le script ne masque pas une erreur Supabase réelle.
- Le script n'appelle aucun LLM.
- Le backend `file` reste inchangé.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=supabase python3 scripts/check_web_storage.py
```

La dernière commande doit échouer proprement si `SUPABASE_DATABASE_URL` est
absent.

Si Supabase est configuré localement ou dans l'environnement de test :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 scripts/check_web_storage.py
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Ne pas demander de secret pour implémenter.
- Ne pas committer de secret.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
