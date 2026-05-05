# TODO

## Viewer Web POC

- Decide how to handle absolute filesystem paths already present inside generated
  `blackboard.md` files before sharing the viewer outside a trusted audit
  context. The viewer currently displays `blackboard.md` as requested, and those
  generated files may include local paths such as Mermaid source/image paths.
