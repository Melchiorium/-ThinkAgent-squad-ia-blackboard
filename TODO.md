# TODO

## Viewer Web POC

- Decide how to handle absolute filesystem paths already present inside generated
  `blackboard.md` files before sharing the viewer outside a trusted audit
  context. The viewer currently displays `blackboard.md` as requested, and those
  generated files may include local paths such as Mermaid source/image paths.

  

## Web App And Workflow Evolution

- Nettoyer la terminologie côté interface et documentation humaine : garder
  `job` et `run` comme termes techniques internes, mais utiliser `génération`,
  `dossier généré` et `résultat` dans l'expérience utilisateur.
- Ajouter plus de granularité dans les étapes visibles et/ou persistées pendant
  une génération.
- Pouvoir lancer Growth et Tech en parallèle quand le workflow le permet.
- Pouvoir manipuler les noeuds et les prompts depuis une interface dédiée.
