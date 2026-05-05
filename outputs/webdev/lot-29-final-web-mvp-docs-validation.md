# Lot 29 - Documentation et validation finale du MVP web

## Objectif

Aligner la documentation et la mémoire projet après les lots 27 et 28.

Ce lot doit confirmer que le besoin utilisateur est couvert :

```text
accéder à l'app web -> saisir titre + brief -> lancer -> lire le résultat
```

## Contexte projet utile

- Le vocabulaire technique `job`, `run`, `outputs/tests` peut rester dans la
  documentation technique quand il aide un agent ou un développeur.
- L'interface utilisateur doit rester claire et parler de génération/résultat.
- Le lancement local se fait via un script qui charge `.env`.
- Le déploiement Render utilise des variables d'environnement configurées en
  ligne, pas le `.env` local.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une règle courte est utile
- `docs/ai/00-index.yaml` seulement si un nouveau chemin clé doit être ajouté
- `TODO.md`

## Fichiers à ne pas modifier

- `app/` sauf correction mineure découverte pendant validation
- `app/prompts V3/`
- `docs/ai/contracts.yaml`
- `outputs/tests/`
- `outputs/web-jobs/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`

## Travail README

Mettre à jour la section `Viewer Web POC` pour expliquer :

- lancement local avec `./scripts/run_web.sh` ;
- saisie d'un titre projet ;
- saisie d'un brief ;
- suivi de génération ;
- lecture des résultats dans l'interface ;
- les runs existants restent consultables ;
- Render doit avoir ses variables d'environnement configurées dans le dashboard.

Ne pas bannir les mots `job` ou `run` de la documentation technique.

## Travail docs/ai

Mettre à jour :

- `docs/ai/modules.yaml`
  - `web` : mentionner le champ titre projet ;
  - `web_jobs` : mentionner `project_title` dans le JSON job ;
  - éventuellement `scripts/run_web.sh` si `modules.yaml` suit les scripts.

- `docs/ai/flows.yaml`
  - `web_unified_generation_ui_flow` doit inclure titre + brief ;
  - ajouter ou préciser le flux local web env si utile.

- `docs/ai/00-index.yaml`
  - ajouter `web_local_launcher: scripts/run_web.sh` dans `key_paths` si le
    script existe.

- `docs/ai/rules.yaml`
  - ne pas ajouter de règle si rien de nouveau n'est nécessaire.

## Travail TODO

Mettre à jour `TODO.md` :

- garder les suites futures :
  - granularité des étapes ;
  - Growth et Tech en parallèle ;
  - manipulation noeuds/prompts ;
- retirer ou adapter le TODO terminologie seulement si l'UI est effectivement
  suffisamment claire.

## Validation finale

Exécuter :

```bash
python3 -m compileall app
zsh -n scripts/run_web.sh
python3 -c "from app.web import app; c=app.test_client(); r=c.get('/'); text=r.get_data(as_text=True); print(r.status_code); print('Titre du projet' in text); print('Lancer la génération' in text)"
git status --short outputs/web-jobs
git diff -- README.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml docs/ai/00-index.yaml TODO.md
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Validation fake runner recommandée :

- poster `project_title=Yoyo` et un brief ;
- vérifier un job `done` ;
- vérifier que le run pointe vers `Yoyo/version X` ;
- vérifier que PRD, Architecture, GTM sont visibles dans `/jobs/<job_id>`.

Validation réelle recommandée seulement si `.env` contient une clé valide :

```bash
./scripts/run_web.sh
```

Puis ouvrir l'URL affichée et lancer une génération courte.

## Critères d'acceptation

- L'utilisateur peut saisir un titre et un brief.
- Le titre contrôle le nom du run généré.
- Le lancement local charge `.env`.
- La documentation distingue local et Render.
- `outputs/web-jobs/` reste ignoré.
- Aucun prompt n'est modifié.
- Aucun contrat blackboard n'est modifié.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder les docs courtes et factuelles.
- Ne pas modifier les prompts.
- Ne pas modifier les contrats blackboard.
- Ne pas toucher aux runs générés existants.

