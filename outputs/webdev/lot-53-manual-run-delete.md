# Lot 53 - Suppression manuelle des runs historiques

## Objectif

Permettre à l'utilisateur de supprimer manuellement un run historique depuis
l'interface web, avec une icône corbeille et une confirmation.

Le besoin est de nettoyer l'historique visible dans le viewer POC, notamment
les générations de test.

## Contexte projet utile

- La home liste les runs via `list_runs(...)`.
- Le détail d'un run est disponible sur `/runs/<project>/<version>`.
- Les artefacts sont servis via
  `/runs/<project>/<version>/artifacts/<filename>`.
- Le stockage peut être :
  - `file` : `outputs/tests/<Project>/version X/` ;
  - `supabase` : table `web_run_artifacts`.
- Le guard `WEB_ACCESS_TOKEN` protège déjà l'application quand configuré.
- Il n'y a pas de comptes utilisateurs ni de rôles.
- Cette action est destructive et doit être volontaire.

## Fichiers autorisés à modifier

- `app/web.py`
- `app/web_storage.py`
- `app/web_runs.py` seulement si nécessaire
- `app/web_presenters.py`
- `app/templates/index.html`
- `app/templates/run_detail.html` si suppression depuis le détail souhaitée
- `app/static/web.css`
- `app/static/web.js` seulement si confirmation JS personnalisée nécessaire
- `scripts/check_web_storage.py`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` si ajout d'un garde-fou suppression
- `README.md` seulement si une phrase courte est utile

## Fichiers à ne pas modifier

- `app/orchestrator.py`
- `app/generation_service.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `docs/supabase-schema.sql`, sauf si une contrainte mineure est strictement
  nécessaire
- `outputs/tests/` sauf via test manuel explicitement contrôlé
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`, sauf demande explicite utilisateur

## Règles de sécurité et UX

- Suppression uniquement en `POST`.
- Pas de suppression via `GET`.
- Utiliser les paramètres `project` et `version` validés par l'inventaire :
  ne jamais supprimer depuis un chemin brut fourni par l'utilisateur.
- Refuser les valeurs contenant `/`, `\` ou `..`.
- Demander confirmation avant suppression :
  - confirmation navigateur simple acceptable ;
  - ou formulaire avec bouton “Supprimer” + texte clair.
- Afficher une icône corbeille ou un bouton corbeille dans la liste des runs.
- Le bouton doit rester compréhensible avec ou sans icône.
- Après suppression, rediriger vers `/` avec un message court si possible.
- Si le run n'existe pas, répondre `404`.
- Si la suppression échoue, afficher une erreur claire sans stacktrace.
- Ne pas supprimer les jobs par défaut dans ce lot, sauf si une relation directe
  au run est explicitement gérée et documentée.

## Comportement attendu en backend file

- Supprimer uniquement le dossier :

```text
outputs/tests/<Project>/<version>/
```

- Ne pas supprimer le dossier projet parent sauf s'il est vide après suppression.
- Si le dossier projet parent devient vide, il peut être supprimé pour garder
  l'historique propre.
- Ne jamais supprimer ailleurs que sous `outputs/tests/`.
- Utiliser `Path.resolve()` et vérifier que le chemin final reste sous la racine
  attendue avant suppression.

## Comportement attendu en backend Supabase

- Supprimer les lignes de `web_run_artifacts` correspondant à :

```sql
run_project = <project>
run_version = <version>
```

- Ne pas toucher aux autres runs du même projet.
- Ne pas toucher aux jobs par défaut.
- Après suppression, `list_runs(...)` ne doit plus retourner ce run.
- `GET /runs/<project>/<version>` doit répondre `404`.

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées liées à `web`, `web_runs`,
   `web_storage`, `web_viewer_flow` et `web_rules`.
2. Ajouter une fonction storage claire, par exemple :

```python
delete_run(project: str, version: str, outputs_root: Path | None = None, backend: str | None = None) -> bool
```

3. Implémenter le backend `file` avec validation de chemin stricte.
4. Implémenter le backend `supabase` avec `delete from web_run_artifacts ...`.
5. Ajouter une route Flask :

```text
POST /runs/<project>/<version>/delete
```

6. La route doit :
   - retrouver le run via `get_run(...)` ;
   - répondre `404` s'il n'existe pas ;
   - appeler `delete_run(...)` ;
   - rediriger vers `/`.
7. Ajouter dans `index.html` un bouton corbeille pour chaque run.
8. Ajouter un `confirm(...)` simple ou une confirmation HTML explicite.
9. Ajouter éventuellement le même bouton sur `run_detail.html`.
10. Ajouter le style CSS pour un bouton corbeille discret.
11. Mettre à jour `scripts/check_web_storage.py` pour tester un run fake :
    - créer/persister un run fake ;
    - vérifier qu'il est listé ;
    - le supprimer ;
    - vérifier qu'il n'est plus listé.
12. Mettre à jour `docs/ai/modules.yaml` et `docs/ai/flows.yaml`.
13. Ajouter une règle courte dans `docs/ai/rules.yaml` si nécessaire :
    “les suppressions de runs web doivent passer par l'inventaire et jamais par
    un chemin brut utilisateur”.

## Comportements attendus

- L'utilisateur voit une corbeille sur les runs historiques.
- Cliquer sur la corbeille demande confirmation.
- Après confirmation, le run disparaît de la home.
- Le détail du run supprimé devient inaccessible.
- Les autres runs du même projet restent visibles.
- Les jobs existants ne sont pas supprimés par surprise.
- La suppression fonctionne en backend `file`.
- La suppression fonctionne en backend `supabase`.
- Une tentative de suppression avec chemin invalide échoue.

## Critères d'acceptation

- `POST /runs/<project>/<version>/delete` supprime un run existant.
- `GET /runs/<project>/<version>` répond `404` après suppression.
- La home ne liste plus le run supprimé.
- Aucun accès `GET` destructif n'existe.
- Les chemins avec `/`, `\`, `..` sont refusés.
- Backend `file` validé.
- Backend `supabase` validé si `SUPABASE_DATABASE_URL` est configuré.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré réel n'est committé.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py
git diff -- app/web.py app/web_storage.py app/web_runs.py app/web_presenters.py app/templates/index.html app/templates/run_detail.html app/static/web.css app/static/web.js scripts/check_web_storage.py docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml README.md
git diff -- app/orchestrator.py app/generation_service.py app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

Validation Supabase réelle seulement si configurée :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 scripts/check_web_storage.py
```

Validation manuelle web :

1. ouvrir `/` ;
2. repérer un run de test ;
3. cliquer sur la corbeille ;
4. annuler et vérifier que rien n'est supprimé ;
5. recommencer et confirmer ;
6. vérifier que le run disparaît ;
7. ouvrir l'ancien détail et vérifier `404`.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la suppression explicite et sûre.
- Ne jamais supprimer depuis un chemin brut utilisateur.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas committer d'outputs générés.
