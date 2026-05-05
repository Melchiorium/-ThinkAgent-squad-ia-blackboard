# Lot 26 - Correctif terminologie UI et fichiers runtime

## Objectif

Corriger deux findings d'audit sur l'interface de génération unifiée :

1. ne jamais committer le stockage runtime `outputs/web-jobs/` ;
2. retirer la terminologie interne `job` de l'interface utilisateur.

Ce lot est correctif et doit rester strictement ciblé.

## Contexte projet utile

- `app/web_jobs.py` persiste les tâches de génération en JSON.
- Ces fichiers contiennent le `brief_text` complet et peuvent contenir des
  erreurs runtime.
- Ils sont utiles à l'exécution locale, mais ne sont pas des artefacts source.
- Côté code, le terme `job` peut rester.
- Côté interface humaine, utiliser plutôt :
  - `génération`
  - `résultat`
  - `dossier généré`

## Findings à corriger

### Finding 1 - `.gitignore`

Ajouter `outputs/web-jobs/` dans `.gitignore`.

Supprimer du working tree les fichiers générés sous `outputs/web-jobs/` avant
staging.

Ne pas supprimer le dossier si l'application en a besoin localement ; il sera
recréé automatiquement. Le point important est qu'aucun JSON runtime ne soit
committable.

### Finding 2 - `app/templates/index.html`

Retirer les libellés visibles :

- `Mes jobs`
- `job`
- `jobs`
- raw `job_id` comme titre principal d'une carte

Remplacer par des libellés utilisateur :

- `Mes générations`
- `génération`
- `générations`
- `Ouvrir le suivi`
- `Ouvrir le résultat`

Le `job_id` peut rester visible en petit texte secondaire si utile pour le debug,
par exemple :

```html
<p class="technical-id">ID technique : {{ job.job_id }}</p>
```

Mais il ne doit plus être le titre principal de la carte.

## Fichiers autorisés à modifier

- `.gitignore`
- `app/templates/index.html`
- `app/templates/job_status.html` si le `job_id` y est trop proéminent
- `app/static/web.css` si une classe secondaire est nécessaire pour l'ID technique
- `README.md` seulement si le terme `job` est exposé dans la documentation humaine
- `TODO.md` seulement si nécessaire pour retirer un TODO devenu obsolète

## Fichiers à ne pas modifier

- `app/web_jobs.py`
- `app/generation_service.py`
- `app/orchestrator.py`
- `app/agents/`
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/*.json` ne doit pas être modifié ou committé ; il doit être
  supprimé du working tree si présent

## Étapes de développement

1. Lire `docs/ai/00-index.yaml`.
2. Lire `app/templates/index.html`, `app/templates/job_status.html`,
   `app/static/web.css` et `.gitignore`.
3. Ajouter `outputs/web-jobs/` dans `.gitignore`.
4. Supprimer les fichiers JSON runtime présents sous `outputs/web-jobs/` du
   working tree.
5. Remplacer les libellés UI `job/jobs` par `génération/générations`.
6. Si `job_id` reste visible, le rendre secondaire et clairement technique.
7. Vérifier qu'aucune route backend ne change.
8. Vérifier qu'aucun prompt ou contrat blackboard ne change.

## Comportements attendus

- Les fichiers runtime de jobs web ne sont plus proposés au commit.
- L'interface utilisateur ne demande pas à l'utilisateur de comprendre le terme
  `job`.
- Le code Python peut continuer à utiliser `job`.
- Le stockage runtime continue de fonctionner localement.
- Les générations existantes dans la session restent affichées.

## Critères d'acceptation

- `.gitignore` contient `outputs/web-jobs/`.
- `git status --short` ne montre plus `outputs/web-jobs/`.
- La home affiche `Mes générations`, pas `Mes jobs`.
- La home n'affiche plus `job(s)` dans les phrases utilisateur.
- Le titre principal d'une carte n'est plus le raw `job_id`.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Commandes de validation

```bash
python3 -m compileall app
python3 -c "from app.web import app; c=app.test_client(); r=c.get('/'); text=r.get_data(as_text=True); print(r.status_code); print('Mes générations' in text); print('Mes jobs' in text); print(' job' in text.lower())"
git status --short
git diff -- .gitignore app/templates/index.html app/templates/job_status.html app/static/web.css README.md TODO.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Vérification manuelle :

1. Lancer l'app.
2. Ouvrir la home.
3. Vérifier que l'interface parle de génération/résultat/dossier généré.
4. Créer une génération de test si besoin.
5. Vérifier que `outputs/web-jobs/` peut être recréé localement, mais reste
   ignoré par git.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder le correctif ciblé.
- Ne pas modifier la logique métier.
- Ne pas exposer de brief utilisateur dans git.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux runs générés sous `outputs/tests/`.

