# TODO

## Viewer Web POC

- Decide how to handle absolute filesystem paths already present inside generated
  `blackboard.md` files before sharing the viewer outside a trusted audit
  context. The viewer currently displays `blackboard.md` as requested, and those
  generated files may include local paths such as Mermaid source/image paths.

## Ajouter les fichiers outputs dans la réponse au challenge

## Web App And Workflow Evolution

- Nettoyer la terminologie côté interface et documentation humaine : garder
  `job` et `run` comme termes techniques internes, mais utiliser `génération`,
  `dossier généré` et `résultat` dans l'expérience utilisateur.
- Ajouter plus de granularité dans les étapes visibles et/ou persistées pendant
  une génération.
- Pouvoir lancer Growth et Tech en parallèle quand le workflow le permet.
- Pouvoir manipuler les noeuds et les prompts depuis une interface dédiée.

## Passation minimale

- Vérifier périodiquement `/healthz` et `/readyz?access_token=<token>` sur
  Render.
- Garder un run existant lisible comme preuve de persistance après redeploy.
- Surveiller les erreurs Render/Supabase avant toute nouvelle génération.

## Hors lot suivant

- Auth complète.
- Comptes utilisateurs.
- Queue distribuée.
- Migration Astro.
- Archivage automatique.
