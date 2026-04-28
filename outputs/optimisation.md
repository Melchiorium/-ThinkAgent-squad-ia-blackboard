# Optimisation Du Système Squad Agentique (Hors Seconde Passe)

Ce document détaille les améliorations prioritaires du système actuel, en se concentrant sur le workflow principal (premier passage), sans traiter la logique de second pass.

L'objectif n'est pas de "faire plus de texte", mais de rendre le système plus fiable sur trois axes :
- meilleure convergence des agents sur les vrais gaps
- meilleure qualité d'arbitrage Product
- meilleure lisibilité décisionnelle pour un humain

---

## 1) Renforcer La Boucle De Correction Ciblée

## Ce Que Ça Implique

Aujourd'hui, la boucle de correction existe et se déclenche correctement, mais elle corrige souvent la forme plutôt que le fond.  
Le problème principal est la perte d'information entre la planification des tâches et l'exécution :
- l'orchestrateur construit des tâches riches (`owner`, `task`, `source_gap`, `expected_output`, `contributors`)
- mais les agents reçoivent surtout une liste de tâches textuelles simplifiées

Résultat :
- corrections trop génériques
- répétition des mêmes gaps
- difficulté à faire évoluer un `LIMITED` vers un statut plus net

## Pourquoi C'est Critique

La boucle est le coeur de la valeur "agentique" après le premier tour.  
Si cette boucle n'est pas transformationnelle, le système reste un bon générateur d'analyses, mais pas un bon moteur de progression.

## Pistes

- **Piste A (recommandée)**: transmettre aux agents des tâches structurées complètes
  - inclure systématiquement `source_gap`, `expected_output`, et `contributors`
  - forcer chaque agent à répondre en mode "gap closure", pas "nouvelle suggestion"
- **Piste B**: garder le format texte actuel, mais ajouter un protocole de réponse strict
  - exiger : "Gap traité / preuve / ce qui reste bloquant"
  - moins intrusif, mais moins robuste

## Implémentation Proposée

- Dans `app/orchestrator.py`:
  - modifier `_group_correction_tasks_by_owner` pour renvoyer des objets (dict) plutôt que des strings
  - conserver la granularité par boucle et par owner
- Dans `app/agents/tech_agent.py` et `app/agents/growth_agent.py`:
  - faire accepter `correction_tasks: list[dict]`
  - injecter chaque tâche dans le prompt avec ce format :
    - Task
    - Source Gap
    - Expected Output
    - Contributors
- Dans `app/agents/product_agent.py`:
  - même logique pour les gaps Product
  - exiger un mini-bilan de fermeture des gaps dans la réponse (section dédiée)
- Ajouter une règle de post-check dans l'orchestrateur :
  - si les mêmes gaps reviennent textuellement deux fois de suite, stopper la boucle plus tôt avec justification explicite

---

## 2) Remplacer L'Arbitrage Product Heuristique Par Un Arbitrage Déclaratif

## Ce Que Ça Implique

Le système infère actuellement `retained/deferred/rejected` en cherchant des fragments de recommandations dans le PRD final.  
Cette méthode est fragile :
- faux négatifs fréquents (la décision est prise mais reformulée différemment)
- faux positifs possibles (match lexical sans vraie décision)
- champs "Retained Decisions" souvent vides ou peu fiables

## Pourquoi C'est Critique

Sans arbitrage fiable, la collaboration multi-agent perd sa traçabilité réelle.  
On lit des recommandations, mais on ne sait pas bien ce qui a été décidé et pourquoi.

## Pistes

- **Piste A (recommandée)**: arbitrage explicite produit par Product
  - Product renvoie une section structurée avec :
    - Retained
    - Deferred
    - Rejected
    - Rationale courte
- **Piste B**: sortie JSON stricte en plus du PRD
  - plus robuste côté parsing
  - un peu plus sensible aux erreurs de format du modèle

## Implémentation Proposée

- Dans `app/prompts V2/product_prompt.md`:
  - ajouter une contrainte de sortie duale :
    - document PRD propre
    - bloc d'arbitrage structuré en fin de réponse (ou section séparée)
- Dans `app/agents/product_agent.py`:
  - supprimer progressivement `_recommendation_is_retained` et les heuristiques associées
  - parser le bloc d'arbitrage fourni par le modèle
  - hydrater `retained_decisions`, `deferred_decisions`, `rejected_changes`, `open_points` depuis ce bloc
- Ajouter une validation défensive :
  - si section arbitrage absente/mal formée, fallback minimal + log d'erreur explicite dans `activity_log`

---

## 3) Dédupliquer Et Compresser Le Blackboard Pour Améliorer Le Signal Décisionnel

## Ce Que Ça Implique

Les champs `risks`, `open_questions`, `unresolved_tensions`, `remaining_open_points` accumulent des doublons inter-agents et inter-boucles.  
Le blackboard devient vite long, redondant, et plus difficile à exploiter.

Effets visibles :
- fatigue de lecture
- perte de hiérarchie (les risques critiques sont noyés)
- difficulté à comparer deux runs

## Pourquoi C'est Critique

Le blackboard est censé être une mémoire utile.  
S'il devient un dump brut, il ne joue plus son rôle de support à la décision.

## Pistes

- **Piste A (recommandée)**: normalisation + déduplication + priorisation
  - normaliser les textes (casefold, ponctuation, espaces)
  - fusionner entrées proches
  - conserver top N par criticité
- **Piste B**: séparation "raw log" vs "executive view"
  - stocker le brut, mais rendre la vue exportée plus compacte
  - très utile si tu veux garder toute la matière pour debug

## Implémentation Proposée

- Créer un utilitaire dédié (ex: `app/normalization.py`):
  - `normalize_text()`
  - `dedupe_semanticish()` (version simple par règles lexicales)
  - `rank_items()` selon source, fréquence, et nature (`blocking_gap` > `improvement` > `question`)
- Dans `tech_agent.py` et `growth_agent.py`:
  - limiter la collecte initiale (déjà partiellement fait avec `limit=3`/`limit=5`)
  - tagger chaque item avec sa source
- Dans `main.py` (formatage `blackboard.md`):
  - afficher version compacte en priorité
  - optionnel: section "Raw Extract (appendix)" pour debug

---

## 4) Fiabiliser La Génération Du Diagramme D'Architecture

## Ce Que Ça Implique

Les évaluations montrent des incohérences entre `architecture.md` et `architecture.pdf` (ex: "No explicit flow captured").  
La cause probable est un format de blueprint trop libre et un parseur qui dépend fortement de labels textuels.

Résultat :
- le PDF peut paraître pauvre alors que l'analyse Tech contient de la matière
- perte de crédibilité du livrable architecture

## Pourquoi C'est Critique

Le diagramme est un artefact de confiance.  
S'il est incomplet alors que le document est bon, il dégrade la perception globale de la qualité du système.

## Pistes

- **Piste A (recommandée)**: contrat de format strict pour le `Diagram Blueprint`
  - sections obligatoires, headings fixes, listes courtes
  - parseur simplifié et robuste
- **Piste B**: extraction assistée par fallback intelligent
  - si blueprint absent, extraire depuis sections techniques proches
  - déjà partiellement présent, à renforcer

## Implémentation Proposée

- Dans `app/prompts V2/tech_prompt.md`:
  - imposer un sous-format exact pour "Diagram Blueprint" :
    - Main system blocks
    - Main flows between blocks
    - External actors or systems
    - Admin or operations control points
- Dans `app/agents/tech_agent.py`:
  - valider la présence de ces 4 sous-sections
  - si manquantes, logguer un warning structuré
- Dans `app/architecture_render.py`:
  - rendre le parsing plus tolérant aux variantes mineures
  - ajouter un "quality flag" dans le blackboard (ex: `diagram_quality: complete|partial|fallback`)

---

## 5) Introduire Une Grille D'Évaluation Commune Inter-Agents

## Ce Que Ça Implique

Chaque agent produit aujourd'hui ses analyses avec une bonne structure, mais les critères de jugement restent parfois hétérogènes.  
Conséquence :
- gaps parfois vagues ou non comparables
- difficulté à savoir si les trois agents convergent vraiment

Une scorecard commune améliorerait :
- la cohérence des verdicts locaux
- la qualité de l'agrégation globale
- la comparabilité entre projets/runs

## Pourquoi C'est Critique

Sans référentiel commun, tu as trois "bons avis" qui ne parlent pas exactement de la même chose.  
Avec référentiel, tu obtiens un diagnostic systémique, pas juste trois opinions.

## Pistes

- **Piste A (recommandée)**: scorecard minimale commune (4-6 dimensions)
  - preuve de demande
  - preuve de faisabilité
  - preuve de launchability
  - confiance/compliance/safety
  - viabilité économique initiale
- **Piste B**: scorecard par rôle + noyau commun
  - noyau partagé + dimensions spécifiques Product/Tech/Growth
  - plus riche mais plus complexe à maintenir

## Implémentation Proposée

- Ajouter un schéma d'évaluation dans les prompts V2 :
  - chaque agent doit noter les dimensions communes (échelle simple 1-5 ou faible/moyen/fort)
  - puis ajouter ses dimensions spécifiques
- Étendre `readiness.py`:
  - parser un bloc "Evidence Scorecard" commun
  - permettre une agrégation pondérée (optionnelle) en plus du statut READY/LIMITED/INSUFFICIENT
- Dans `main.py` / `blackboard.md`:
  - afficher synthèse courte :
    - dimensions les plus faibles
    - dimensions améliorées après correction

---

## Roadmap D'Implémentation (Pragmatique)

- **Sprint 1 (impact immédiat)**:
  - arbitrage déclaratif Product
  - tâches de correction enrichies transmises aux agents
- **Sprint 2 (qualité de sortie)**:
  - déduplication/compactage blackboard
  - format strict Diagram Blueprint + robustesse render
- **Sprint 3 (maturité système)**:
  - scorecard commune
  - métriques de convergence multi-runs

---

## Définition De Succès (Mesurable)

Après optimisation, tu devrais observer :
- baisse du taux de duplicats dans `risks/open_questions`
- augmentation de la part de décisions `retained/deferred/rejected` correctement renseignées
- moins de runs où le PDF architecture est jugé incohérent avec le Markdown
- correction loop qui modifie réellement les gaps prioritaires (pas seulement reformulation)
- meilleure stabilité des verdicts entre projets comparables

En bref : l'objectif n'est pas d'obtenir plus de `READY`, mais d'obtenir des verdicts plus fiables, plus explicites, et plus actionnables.

---

## Journal D'Implémentation - Solution 1.A

Cette section documente ce qui a été effectivement implémenté dans le code pour la solution `1.A` (transmission de tâches structurées complètes aux agents).

## Portée

- Incluse:
  - passage des tâches de correction en format structuré côté orchestrateur
  - consommation des tâches structurées par Tech, Growth et Product
  - enrichissement des prompts utilisateur envoyés aux agents pendant la correction loop
- Non incluse:
  - arrêt anticipé automatique si mêmes gaps sur deux boucles
  - modifications de format de sortie final des agents (hors prompt de tasking)

## Fichiers Modifiés

- `app/orchestrator.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/agents/product_agent.py`

## Détails Des Changements

### 1) `app/orchestrator.py`

- `_group_correction_tasks_by_owner` renvoie désormais `dict[str, list[dict]]` au lieu de `dict[str, list[str]]`.
- Chaque owner reçoit l'objet de tâche complet (pas seulement `task`):
  - `task`
  - `source_gap`
  - `expected_output`
  - `contributors`
- Impact:
  - aucune perte d'information entre planification et exécution
  - les agents peuvent corriger en contexte, pas "à l'aveugle"

### 2) `app/agents/tech_agent.py`

- Signature de `run_tech_agent` mise à jour:
  - de `correction_tasks: list[str] | None`
  - vers `correction_tasks: list[dict] | None`
- `_format_correction_tasks` formatte maintenant chaque tâche de manière structurée.
- Le prompt inclut explicitement:
  - la tâche à résoudre
  - le gap source
  - la sortie attendue
  - les contributeurs
- Ajout d'une consigne explicite "gap-closure assignment".

### 3) `app/agents/growth_agent.py`

- Même changement que Tech:
  - `run_growth_agent` accepte `list[dict]`
  - `_format_correction_tasks` rend les champs structurés
  - consigne explicite de fermeture de gap
- Impact:
  - meilleurs signaux de correction actionnable dans la passe Growth

### 4) `app/agents/product_agent.py`

- `_build_revision_user_prompt` et `run_product_revision` passent à `list[dict]`.
- `_format_correction_tasks` produit un bloc structuré complet.
- Ajout d'une contrainte opérationnelle Product dans le prompt:
  - "resolve concretely or state a credible reduction path"
- Impact:
  - Product reçoit des instructions de correction plus opérationnelles
  - meilleure discipline de résolution des gaps Product-owned

## Pourquoi Cette Implémentation Est Utile

- Elle réduit la dérive "reformulation vague" des boucles LIMITED.
- Elle aligne les agents sur des attentes vérifiables (`expected_output`).
- Elle garde la trace de collaboration via `contributors`, ce qui améliore la cohérence inter-rôles.

## Vérification Recommandée

Pour valider que la 1.A apporte le gain attendu:
- lancer 2 à 3 runs comparables
- inspecter `blackboard.md`:
  - qualité des sections de correction
  - diminution des gaps répétés tels quels
  - meilleure correspondance entre gaps initiaux et changements produits

Critère pragmatique de succès:
- au moins 1 gap prioritaire est réellement transformé par boucle (et pas seulement reformulé).
