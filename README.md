# Squad IA Blackboard

Projet Python local qui simule une petite équipe de 3 agents IA qui collaborent via un `blackboard` partagé.

## Contexte

L’idée est de transformer un brief projet en trois livrables distincts:

- `PRD`
- notes d’architecture
- notes go-to-market

Les agents ne se parlent pas directement. Ils lisent et écrivent dans un état partagé, puis l’orchestrateur décide de l’ordre d’exécution.

## Architecture

- `app/main.py` charge le brief initial et lance le flux
- `app/orchestrator.py` pilote l’ordre des agents
- `app/blackboard.py` crée l’état partagé
- `app/agents/*.py` contient les agents métier
- `app/llm.py` encapsule l’appel au modèle local
- `app/prompts/*.md` contient les prompts des agents
- `outputs/` contient les artefacts générés

## Étapes du projet

Le projet a été construit par incréments:

1. `blackboard` initial
2. utilitaire LLM partagé
3. flux V0 avec agent temporaire
4. vrai `product_agent`
5. ajout des agents `tech` et `growth`
6. passe de révision produit
7. séparation entre état interne et rendu humain
8. chargement du brief depuis `dev-agents/architect-context.md`

Les fichiers de suivi des étapes sont maintenant dans `outputs/dev-steps/`.

## Où on en est

L’application fonctionne en local avec:

- un brief chargé depuis `outputs/project-brief.md`
- un flux à 4 passes: product, tech, growth, puis révision product
- des sorties générées dans `outputs/`
- un `blackboard.md` lisible pour les humains

## Exécution

```bash
python3 app/main.py
```

## Sorties

- `outputs/prd.md`
- `outputs/architecture.md`
- `outputs/gtm.md`
- `outputs/blackboard.md`
- `outputs/activity_log.txt`

## Notes

- Le brief source éditable est `outputs/project-brief.md`
- Le modèle local est configuré via les variables d’environnement lues dans `app/llm.py`
