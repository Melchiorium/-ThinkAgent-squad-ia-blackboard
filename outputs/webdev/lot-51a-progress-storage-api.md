# Lot 51A - Socle stockage et API progression

## Objectif

Préparer le socle technique pour afficher une progression détaillée pendant une
génération web, sans encore instrumenter le workflow Product/Growth/Tech et
sans modifier l'UI finale.

Ce lot doit ajouter aux jobs web les champs nécessaires à une progression par
blocs métier, puis les exposer dans `GET /api/jobs/<job_id>`.

## Contexte projet utile

- `app/web.py` expose `GET /api/jobs/<job_id>`.
- `app/web_presenters.py` construit le payload JSON de statut.
- `app/web_storage.py` gère les jobs en backend `file` et `supabase`.
- `app/web_jobs.py` réexporte les helpers de job.
- `docs/supabase-schema.sql` définit la table `web_jobs`.
- Le lot 51B utilisera ces champs pour remplir la progression.
- Le lot 51C affichera ensuite ces champs dans la page d'attente.

## Fichiers autorisés à modifier

- `app/web_storage.py`
- `app/web_jobs.py` seulement si nécessaire
- `app/web_presenters.py`
- `scripts/check_web_storage.py`
- `docs/supabase-schema.sql`
- `docs/supabase-poc-storage.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`

## Fichiers à ne pas modifier

- `app/web.py`, sauf ajout strictement nécessaire pour exposer le payload
- `app/orchestrator.py`
- `app/generation_service.py`
- `app/templates/`
- `app/static/`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `TODO.md`

## Contrat de progression à stocker

Ajouter ces champs au job :

```python
progress_stage: str
progress_label: str
progress_detail: str
progress_order: int
progress_total: int
progress_blocks: list[dict]
progress_events: list[dict]
progress_started_at: str
progress_last_event_at: str
progress_timeout_seconds: int
progress_error_type: str
progress_error_message: str
```

Statuts de bloc autorisés :

```text
pending
active
done
skipped
failed
```

Un bloc a au minimum :

```python
{
    "id": "product_problem",
    "group": "Product",
    "label": "Problème cible",
    "status": "pending",
}
```

Un événement a au minimum :

```python
{
    "timestamp": "2026-05-06T09:41:02Z",
    "stage": "product_initial",
    "label": "Product démarre le cadrage initial",
    "detail": "Le brief est analysé avant rédaction du PRD.",
}
```

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`, puis les entrées liées à `web_jobs`,
   `web_storage`, `web_presenters` et `web_storage_validation_script`.
2. Ajouter des valeurs par défaut aux jobs nouvellement créés :
   - `progress_stage=""`
   - `progress_label=""`
   - `progress_detail=""`
   - `progress_order=0`
   - `progress_total=0`
   - `progress_blocks=[]`
   - `progress_events=[]`
3. En backend file :
   - persister ces champs dans les JSON jobs ;
   - accepter leur mise à jour via `update_job(...)` ;
   - garder la compatibilité avec les anciens jobs sans ces champs.
4. En backend Supabase :
   - ajouter les colonnes au `create table` de `docs/supabase-schema.sql` ;
   - ajouter aussi les `alter table ... add column if not exists ...` pour les
     bases déjà créées ;
   - inclure les colonnes dans `insert`, `select`, `update`.
5. Préférer `jsonb` pour `progress_blocks` et `progress_events` :

   ```sql
   progress_blocks jsonb not null default '[]'::jsonb,
   progress_events jsonb not null default '[]'::jsonb
   ```

6. Limiter côté code `progress_events` à 100 entrées maximum.
7. Ne jamais stocker de brief complet, prompt brut, token, clé ou connection
   string dans `progress_events`.
8. Ajouter les champs nécessaires aux retours d'erreur et de blocage :
   - `progress_started_at` ;
   - `progress_last_event_at` ;
   - `progress_timeout_seconds`, défaut `600` ;
   - `progress_error_type`, par exemple `timeout`, `network`, `llm`, `storage`,
     `unknown` ;
   - `progress_error_message`, message court sans secret.
9. Mettre à jour `build_job_status_payload(...)` pour exposer les champs.
10. Mettre à jour `scripts/check_web_storage.py` pour créer un job fake, écrire
   deux blocs et deux événements, puis les relire.
11. Mettre à jour `docs/supabase-poc-storage.md` pour documenter la migration
    additive.
12. Mettre à jour `docs/ai/modules.yaml` et `docs/ai/flows.yaml` si nécessaire.

## Comportements attendus

- Un job existant sans progression reste lisible.
- Un nouveau job contient les champs de progression vides.
- `GET /api/jobs/<job_id>` retourne toujours les champs de progression.
- `GET /api/jobs/<job_id>` retourne les champs d'erreur/timeout de progression.
- Les backends `file` et `supabase` exposent le même contrat.
- Aucun affichage UI avancé n'est requis dans ce lot.
- Aucune instrumentation Product/Growth/Tech n'est requise dans ce lot.

## Critères d'acceptation

- `python3 scripts/check_web_storage.py` valide les champs de progression en
  backend file.
- `WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py` passe.
- La migration Supabase est additive et ne supprime aucune donnée.
- Les champs de timeout/erreur sont disponibles en backend `file` et
  `supabase`.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.
- Aucun output généré n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -m gunicorn --check-config app.web:app
python3 scripts/check_web_storage.py
WEB_STORAGE_BACKEND=file python3 scripts/check_web_storage.py
git diff -- app/web_storage.py app/web_jobs.py app/web_presenters.py scripts/check_web_storage.py docs/supabase-schema.sql docs/supabase-poc-storage.md docs/ai/modules.yaml docs/ai/flows.yaml
git diff -- app/orchestrator.py app/generation_service.py app/agents "app/prompts V3" docs/ai/contracts.yaml
git status --short outputs/tests outputs/web-jobs
```

Migration Supabase additive attendue pour les champs d'erreur :

```sql
alter table web_jobs add column if not exists progress_started_at text not null default '';
alter table web_jobs add column if not exists progress_last_event_at text not null default '';
alter table web_jobs add column if not exists progress_timeout_seconds integer not null default 600;
alter table web_jobs add column if not exists progress_error_type text not null default '';
alter table web_jobs add column if not exists progress_error_message text not null default '';
```

Validation Supabase réelle seulement si configurée :

```bash
WEB_STORAGE_BACKEND=supabase SUPABASE_DATABASE_URL="..." python3 scripts/check_web_storage.py
```

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder l'implémentation simple et lisible.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas modifier les outputs générés.
- Ne jamais stocker de secrets ou prompts bruts dans la progression.
