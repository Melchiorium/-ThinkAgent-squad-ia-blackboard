# Logique De Travail Architecte-Dev

## Pourquoi ce document

Ce document décrit la méthode de développement utilisée dans ce projet quand tu travailles avec :
- un agent `Architecte`
- un agent `Developer`

L'objectif est de rendre explicite la logique de collaboration, les responsabilités de chacun, les artefacts produits, et la façon dont une idée devient une implémentation concrète.

Ce fonctionnement est construit à partir de :
- [dev-agents/architect.md]
- [dev-agents/architect-context.md]
- [dev-agents/developer.md]
- [dev-agents/developer-context.md]
- [dev-agents/current-task.md]
## Intention générale

La logique n'est pas :
- un agent qui pense et code tout
- ni un agent dev totalement autonome

La logique est plutôt :
- un agent `Architecte` qui pense la structure, découpe le travail, protège l'architecture et prépare des handoffs précis
- un agent `Developer` qui implémente seulement la partie demandée, de façon simple et contrôlée

Autrement dit :
- l'architecture est séparée de l'exécution
- le cadrage est séparé du code
- les décisions structurelles ne sont pas laissées au hasard pendant l'implémentation

## Rôle de l'Architecte

L'Architecte est défini comme un `Senior Python Architect`.

Sa mission est de :
- définir, protéger et affiner l'architecture d'implémentation
- préparer des handoffs précis pour le Developer
- maintenir l'historique d'implémentation via des fichiers de step dans `outputs/`

Il ne doit pas :
- coder tout le système lui-même
- redesign le projet sans nécessité claire
- ouvrir plusieurs pistes d'architecture en parallèle si ce n'est pas utile
- produire de grands handoffs flous ou trop larges

En pratique, l'Architecte :
- choisit le plus petit incrément utile
- détermine les fichiers concernés
- fixe les contraintes
- définit les critères d'acceptation
- précise ce qui est hors scope
- arbitre les ambiguïtés remontées par le Developer

## Rôle du Developer

Le Developer est défini comme un `Senior Python Developer`.

Sa mission est de :
- implémenter uniquement la partie demandée
- suivre le handoff courant
- préserver l'architecture existante
- garder le code simple, lisible et explicite

Il ne doit pas :
- redéfinir l'architecture de son côté
- élargir le scope
- restructurer le projet seul
- modifier des fichiers non concernés
- ajouter des abstractions ou dépendances inutiles

En pratique, le Developer :
- lit le step courant
- implémente le plus simplement possible
- remonte les vrais problèmes structurels
- ne force pas une mauvaise solution juste pour "faire avancer"

## Sources de vérité

Le fonctionnement repose sur une hiérarchie de sources très claire.

### Côté Architecte

Ordre de priorité :
1. `architect-context.md`
2. architecture existante / code existant
3. demande utilisateur courante
4. dernier step file

### Côté Developer

Ordre de priorité :
1. dernier step file actif
2. `developer-context.md`
3. code existant

Cette asymétrie est volontaire :
- l'Architecte protège la vision d'ensemble
- le Developer protège l'exécution du step courant

## Le step file comme contrat central

Le coeur du système `architecte-dev`, c'est le `step file`.

Chaque itération de travail repose sur un fichier dans `outputs/`, par exemple :
- `outputs/step-1.md`
- `outputs/step-2.md`
- `outputs/step-20.md`
- ou un correctif comme `outputs/step-correctif-v12.md`

Ce fichier est à la fois :
- le contrat d'implémentation courant
- la surface d'échange entre Architecte et Developer
- la mémoire de la décision prise pour cette étape

Le step file remplace un échange flou de type :
- "tu peux faire ça vite fait"

par un cadre beaucoup plus propre :
- objectif clair
- fichiers concernés
- comportement attendu
- contraintes
- critères d'acceptation
- hors-scope
- feedback dev
- décision architecte

## Structure d'un step file

Le format attendu côté Architecte est stable :

- `Status`
- `Objective`
- `Files concerned`
- `Required behavior`
- `Constraints`
- `Acceptance criteria`
- `Out of scope`
- `Open questions`
- `Developer feedback`
- `Developer status`
- `Architect decision`
- `Completion check`
- `Notes`

Cette structure sert à éviter deux dérives :
- des handoffs trop vagues
- des implémentations qui partent dans une autre direction

## Cycle de travail normal

Le cycle attendu est le suivant :

1. l'Architecte analyse le besoin
2. il crée ou met à jour un step file dans `outputs/`
3. le Developer prend ce step comme contrat d'implémentation
4. il code uniquement ce qui est demandé
5. s'il découvre un problème réel, il le remonte dans `Developer feedback`
6. l'Architecte arbitre dans `Architect decision`
7. on reste sur le même step tant qu'il n'est pas résolu
8. on ne crée le step suivant qu'une fois le précédent fini

Cette logique force un avancement séquentiel et maîtrisé.

## Principe clé : un petit incrément à la fois

Les deux prompts insistent sur le même point :
- livrer petit
- livrer clair
- éviter les gros changements multi-fichiers si ce n'est pas nécessaire

Cela donne une logique très proche d'un développement par micro-étapes :
- une responsabilité bien bornée
- un nombre minimal de fichiers touchés
- une validation plus facile
- moins de régressions involontaires

Le but n'est pas d'aller vite "sur le papier".
Le but est d'avancer proprement sans casser l'ensemble.

## Gestion de l'ambiguïté

Le système prévoit explicitement deux niveaux d'ambiguïté.

### Ambiguïté mineure

Si l'ambiguïté est locale et sans impact structurel :
- le plus simple choix valide est autorisé

### Ambiguïté structurelle

Si l'ambiguïté touche :
- l'architecture
- la structure du projet
- la propriété des fichiers
- le périmètre réel de la tâche

alors :
- le Developer ne doit pas inventer
- il doit remonter le sujet
- l'Architecte doit décider explicitement

Cette règle évite qu'un détail ambigu devienne un changement d'architecture non assumé.

## Gestion du feedback Developer

Le Developer a le droit, et même le devoir, de remonter quand il voit :
- un problème structurel
- une contradiction
- une dépendance cachée
- une contrainte irréaliste
- une meilleure option minimale qui change réellement le scope

Mais il ne doit pas :
- redéfinir silencieusement la tâche
- corriger le step dans son coin
- forcer une implémentation mauvaise

Le format attendu est :
- `issue:`
- `impact:`
- `minimal suggested resolution:`

Puis l'Architecte tranche.

## Logique de statut

Le Developer manipule un petit set de statuts :
- `pending`
- `blocked`
- `ready_for_review`
- `done`

Cela permet de distinguer clairement :
- ce qui n'a pas commencé
- ce qui est bloqué
- ce qui est fini mais demande revue
- ce qui est réellement terminé

Un step ne doit pas avancer tant que :
- l'implémentation n'est pas faite
- les critères d'acceptation ne sont pas atteints
- le Developer est encore `blocked`

## Philosophie technique sous-jacente

Les deux rôles partagent la même philosophie :
- Python simple
- architecture explicite
- lisibilité avant sophistication
- pas de GUI
- pas de frontend
- pas de dépendances inutiles
- pas d'overengineering

Le projet valorise :
- l'orchestration explicite
- les responsabilités claires
- la compréhension par un développeur junior
- la facilité de modification dans le temps

Cette méthode est donc cohérente avec le projet lui-même :
- un système transparent
- modulaire mais minimal
- piloté par états et contrats, pas par magie

## Ce que cette méthode apporte

La logique `architecte-dev` apporte surtout :

- une séparation nette entre conception et implémentation
- une réduction du scope creep
- une meilleure traçabilité des décisions
- une meilleure qualité de handoff
- un rythme d'itération plus sûr
- moins de dérive implicite dans le code

Elle est particulièrement utile quand :
- le projet évolue beaucoup
- plusieurs essais sont tentés
- il faut revenir à un état antérieur sain
- on veut documenter pourquoi une décision a été prise

## Limites et vigilance

Cette méthode a aussi ses limites.

Si elle est mal utilisée, elle peut devenir :
- trop procédurale
- trop lourde
- ou trop dépendante des step files

Elle marche bien si :
- les steps restent petits
- l'Architecte ne sur-prescrit pas
- le Developer ne sous-interprète pas tout
- chacun respecte vraiment son rôle

Le point d'équilibre important est :
- assez de structure pour éviter la dérive
- pas trop de structure au point de ralentir inutilement

## Note Sur Les Dernières Optimisations

Les dernières optimisations du projet ont été menées avec une logique volontairement plus simple :
- un seul agent de travail principal
- un modèle `OpenAI 5.4` utilisé avec un niveau de raisonnement élevé

L'objectif de ce choix était de :
- repartir sur des bases plus saines
- réduire l'effet de confusion lié à un historique trop lourd
- éviter d'empiler trop de couches de coordination ou de prompts secondaires
- retrouver plus facilement ce qui améliore réellement le système

Cette phase doit être comprise comme un recentrage méthodologique :
- moins de complexité de pilotage
- moins de bruit hérité
- plus de lisibilité sur les vraies causes d'amélioration ou de régression

## Résumé simple

Le modèle `architecte-dev` utilisé ici repose sur 4 idées :

1. l'Architecte pense et cadre, mais ne code pas tout
2. le Developer implémente, mais ne redéfinit pas l'architecture
3. le step file est le contrat central de chaque itération
4. on avance par petits incréments, avec arbitrage explicite quand un vrai problème apparaît

En pratique, c'est une méthode de développement assisté qui cherche moins à maximiser l'autonomie qu'à maximiser :
- la clarté
- la stabilité
- la qualité des décisions
- et la capacité à reprendre le projet proprement plus tard
