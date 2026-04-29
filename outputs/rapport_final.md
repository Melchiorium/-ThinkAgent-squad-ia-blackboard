# Histoire du projet d'agents - Version 2

## Pourquoi ce document existe

Ce document raconte la construction du projet `squad-ia-blackboard` : un prototype de système multi-agents capable de transformer un brief projet en dossier de cadrage startup.

L'objectif n'était pas seulement de "passer l'exercice". L'objectif personnel était plus ambitieux :
- faire le maximum en moins de 48h
- construire un POC réellement exécutable
- tester, comparer, explorer
- comprendre ce qui améliore vraiment la qualité d'un système agentique

Le projet a été développé sous contraintes :
- temps limité
- tokens limités
- travail fragmenté
- nombreux essais successifs
- changements fréquents de prompts, modèles et workflow

Un avertissement de traçabilité est nécessaire : une grande partie des anciennes instances de test a été perdue lors d'un nettoyage d'historique. Les grandes étapes de développement et le workflow ont été conservés et documentés, mais certaines comparaisons anciennes ne sont plus vérifiables fichier par fichier. L'incident est détaillé en annexe.

## Genèse technique : choisir une architecture

Avant d'écrire le workflow, il fallait choisir une approche technique.

Plusieurs options étaient possibles.

### Option no-code / workflow automation

Une première piste aurait été d'utiliser un outil de workflow visuel, par exemple n8n.

Cette approche avait des avantages évidents :
- montage rapide
- interface visuelle
- chaînage simple d'APIs
- bon outil pour prototyper des automatisations linéaires

Mais elle semblait moins adaptée à l'objectif du projet.

Les limites principales étaient :
- mémoire partagée limitée
- logique conditionnelle vite difficile à maintenir
- collaboration agentique peu naturelle
- traçabilité fine des décisions plus compliquée

Cette piste a donc été écartée assez tôt. Le projet n'avait pas seulement besoin de chaîner des appels. Il devait faire collaborer plusieurs rôles autour d'un état commun.

### Option frameworks agents

Une autre piste était d'utiliser un framework spécialisé comme LangChain, CrewAI ou AutoGen.

Ces frameworks ont de vrais avantages :
- ils accélèrent certains patterns agentiques
- ils proposent déjà des briques d'orchestration
- ils donnent accès à des abstractions prêtes à l'emploi

Mais pour ce projet, ils posaient aussi un risque.

Le but était de comprendre précisément ce qui était construit : mémoire, handoffs, arbitrage, traces, limites. Un framework aurait pu accélérer le départ, mais aussi cacher une partie du fonctionnement derrière ses propres abstractions.

Le risque était de tomber dans un design guidé par le framework plutôt que par le besoin réel du prototype.

### Option Python custom + blackboard

L'option retenue a donc été une architecture Python custom, très simple, centrée sur un `blackboard`.

Ce choix avait plusieurs avantages :
- architecture explicable
- faible coût
- contrôle complet du workflow
- flexibilité pour modifier les prompts, les agents et l'ordre d'exécution
- traçabilité directe de ce que chaque agent lit, produit et transmet

C'est dans ce choix qu'est apparu le concept central du projet : une mémoire commune.

Chaque agent :
- lit un état partagé
- produit une contribution spécialisée
- écrit ses recommandations, risques ou décisions dans le blackboard
- laisse une trace relisible par l'orchestrateur et par un humain

L'orchestrateur garde le contrôle du déroulé. Les agents ne discutent pas librement entre eux dans une boucle ouverte. Ils interviennent à un moment précis, avec un rôle précis, puis passent le relais.

Ce point était volontaire.

Le projet ne cherchait pas à simuler un faux "swarm autonome". Ce type d'approche peut sembler plus intelligent sur le papier, mais il devient vite opaque, coûteux en tokens, difficile à debugger et parfois inutilement bavard.

Le besoin était différent : construire un système traçable, contrôlable et améliorable.

L'orchestration explicite permet cela :
- Product intervient d'abord
- Growth challenge un cadrage existant
- Tech challenge ensuite la faisabilité
- Product revient pour arbitrer
- le blackboard garde la mémoire de chaque passage

Cette sobriété technique a été un choix structurant. Elle a permis de tester rapidement, de comprendre les limites du système, puis de faire évoluer les prompts et le workflow sans dépendre d'une boîte noire.

### Note sur le système Architecte-Dev

Pour construire ce projet, j'ai aussi utilisé un système agentique complémentaire : une collaboration séparée entre un agent `Architecte` et un agent `Developer`.

Ce mécanisme est presque un projet à part. Il ne fait pas partie du périmètre initial de `squad-ia-blackboard`, qui porte sur la production de dossiers par des agents Product, Growth et Tech. En revanche, il a été indispensable pour développer le prototype dans de bonnes conditions : cadrer les étapes, protéger l'architecture, préparer des handoffs d'implémentation et éviter que le code évolue de façon trop désordonnée.

Je ne détaille pas ce fonctionnement ici pour ne pas mélanger deux sujets. Il est documenté séparément dans [outputs/architecte-dev.md].

## Résumé court

Le projet a commencé comme un simple générateur de document à partir d'un brief.

Il est devenu progressivement un système de cadrage multi-agents avec :
- une mémoire centrale partagée, le `blackboard`
- des rôles spécialisés : Product, Growth, Tech
- des handoffs explicites entre agents
- une phase d'arbitrage Product
- des livrables séparés : PRD, architecture, GTM, blackboard
- un évaluateur externe pour juger la qualité des sorties
- une logique de readiness pour dire si un dossier est exploitable ou encore limité

La leçon principale n'est pas "plus d'agents donne forcément de meilleurs résultats".

La leçon principale est plutôt :

> Un système agentique utile dépend surtout du bon équilibre entre rôles clairs, mémoire partagée lisible, prompts sobres, handoffs bien placés, et capacité à reconnaître quand une idée reste insuffisamment prouvée.

## Ce qu'est un agent dans ce projet

Dans ce projet, un agent n'est pas un robot autonome complexe.

Un agent est plutôt :
- un rôle clair
- un prompt dédié
- un accès à une partie du contexte
- une responsabilité précise dans le workflow
- une contribution écrite dans une mémoire centrale

Les agents ne travaillent pas dans le vide. Ils collaborent par deux mécanismes essentiels :

### 1. Une mémoire centrale

Le `blackboard` sert de mémoire commune.

Il conserve :
- le brief
- le PRD en cours
- les notes techniques
- les notes GTM
- les recommandations
- les risques
- les questions ouvertes
- les décisions retenues, différées ou rejetées
- les résultats de readiness

Sans cette mémoire centrale, les agents produiraient seulement des textes séparés. Avec elle, le système peut garder une trace de ce qui a été dit, demandé, refusé ou arbitré.

### 2. Des handoffs entre agents

Le workflow organise des passages de relais :
- Product pose un premier cadrage
- Growth challenge la demande, le marché et la stratégie de lancement
- Tech challenge la faisabilité et l'architecture
- Product reprend les contributions et arbitre

Ces handoffs sont importants parce qu'ils donnent une forme au raisonnement collectif. Le système ne cherche pas à faire parler trois agents en parallèle sans synthèse. Il cherche à produire une décision finale lisible.

## Phase 1 - Le squelette initial

Le premier objectif était modeste :
- lire un brief
- appeler un modèle
- écrire un premier résultat
- sauvegarder un fichier

À ce stade, le projet n'était pas encore vraiment multi-agent.

Il s'agissait surtout de valider la tuyauterie :
- chargement du brief
- appel LLM
- écriture dans une structure partagée
- export Markdown

Le choix initial a été de travailler avec un modèle local via Ollama.

Ce choix était volontaire :
- valider le workflow avant de consommer des appels API limités
- pouvoir itérer librement sur les prompts
- tester rapidement plusieurs variantes sans coût direct
- séparer les problèmes de pipeline des problèmes de qualité modèle

Autrement dit, Ollama a servi de banc d'essai local. Le but n'était pas de prouver que le modèle local donnerait les meilleurs livrables finaux, mais de construire et stabiliser la mécanique agentique avant de passer à des modèles en ligne plus performants, plus coûteux ou plus limités.

Le choix du `blackboard` est arrivé très tôt. Même dans une version simple, il fallait une mémoire centrale pour éviter que le projet devienne une suite opaque d'appels modèle.

## Phase 2 - Premiers rôles : Product, Growth, Tech

Le système a ensuite été découpé en trois rôles :
- `Product`, responsable du besoin, du MVP et du PRD
- `Growth`, responsable de l'adoption, du lancement et du GTM
- `Tech`, responsable de la faisabilité, de l'architecture et des contraintes techniques

Cette séparation répondait à une faiblesse classique des réponses LLM uniques : elles mélangent souvent produit, marché, technique et business dans un même texte plausible mais peu décidable.

En séparant les rôles, on cherchait à obtenir :
- plus de spécialisation
- plus de contradiction utile
- plus de lisibilité
- moins de synthèse molle

Le premier workflow réellement multi-agent ressemblait à ceci :
1. Product rédige un premier cadrage
2. Growth challenge le cadrage
3. Tech challenge le cadrage
4. Product reprend et arbitre

Le point important n'est pas seulement l'existence de plusieurs agents. C'est le fait que Product revienne à la fin pour transformer les avis séparés en décision.

## Phase 3 - Rendre le travail lisible

Un problème est rapidement apparu : les agents travaillaient, mais un humain avait du mal à comprendre ce qui avait réellement changé.

Le blackboard brut était utile pour la machine, mais pas suffisant pour relire le raisonnement.

Le projet a donc ajouté une double lecture :
- une mémoire structurée pour les agents
- un rendu Markdown pour l'humain

Plusieurs éléments ont été introduits :
- conservation du PRD initial avant révision
- stockage des changements demandés par Growth et Tech
- synthèses de revue
- listes de décisions retenues, différées ou rejetées
- points ouverts
- tensions non résolues

Cette étape a été importante parce qu'un système agentique ne doit pas seulement produire un résultat. Il doit aussi permettre de comprendre :
- qui a recommandé quoi
- ce qui a été retenu
- ce qui a été rejeté
- ce qui reste incertain

## Phase 4 - Les premières limites

Les premiers runs ont montré plusieurs limites.

### Agents trop descriptifs

Les agents produisaient des documents plausibles, mais pas toujours décisionnels.

Ils expliquaient souvent une idée possible, sans assez dire :
- ce qu'il faut croire pour avancer
- ce qui rend le projet dangereux
- ce qui doit être testé vite
- ce qui doit être exclu du MVP

### Suggestions trop générales

Growth et Tech pouvaient réagir comme des consultants prudents :
- beaucoup de remarques
- beaucoup de risques
- peu de choix concrets

### Product absorbait trop

Product avait parfois tendance à réintégrer trop directement les retours des autres agents.

Le PRD final pouvait alors devenir trop large, trop lourd, ou contaminé par des notes de revue qui auraient dû rester dans le blackboard.

### Le modèle local montrait ses limites

Avec `qwen2.5-coder:7b`, les sorties étaient utiles pour prototyper, mais limitées :
- dérives hors brief
- qualité inégale
- mélange de langues
- difficulté à tenir un rôle strict
- décisions parfois arbitraires

Cette phase a clarifié un point important : la qualité ne dépendait pas seulement du code. Elle dépendait aussi du modèle, du prompt, du workflow et de la répartition des responsabilités.

## Phase 5 - Modèles : Ollama, Gemini, OpenAI

Le projet a d'abord privilégié Ollama pour des raisons pratiques.

Mais la qualité du modèle local est devenue une limite. Le projet a alors testé Gemini via une API compatible OpenAI, puis OpenAI avec `gpt-5.4-mini`.

Ce changement a amélioré :
- la cohérence des documents
- la capacité de synthèse
- la stabilité du rôle des agents
- la qualité des arbitrages

Un choix technique important a été conservé : la couche LLM reste configurable. Le projet n'est pas verrouillé sur un seul fournisseur.

## Phase 6 - Les évaluateurs externes

Une brique indépendante a pris de plus en plus d'importance : l'évaluation externe.

Deux postures d'évaluation ont été utilisées.

### Évaluation CEO

L'évaluateur CEO a une posture de décideur business :
- est-ce que j'y vais ou non ?
- est-ce que ce projet mérite d'être porté ?
- décision froide, sévère, orientée potentiel concret

Il ne cherche pas à encourager l'équipe. Il juge :
- la viabilité business
- le potentiel de profit
- la complexité d'exécution
- le réalisme GTM
- le risque concurrentiel
- la décision d'investissement : `APPROVE`, `REVISE` ou `REJECT`

Cette posture est utile, mais très dure. Les premiers résultats pouvaient être très bas, parfois sous 4/10, avec des verdicts négatifs.

Dans les derniers tests V1, le CEO evaluator donne une lecture intéressante :
- CareSync est `APPROVE` avec 7/10, sous conditions strictes de pilote
- LocalLoop est `REVISE` avec 6/10
- Melody est `REVISE` avec 5/10
- SkillBridge est `REVISE` avec 6/10

Ce n'est pas une évaluation de beauté documentaire. C'est une lecture d'investissement : est-ce que le projet mérite du temps, du budget, et sous quelles conditions ?

### Évaluation qualité

Le projet a ensuite utilisé un évaluateur davantage orienté "qualité des livrables" :
- est-ce que le PRD est bon ?
- est-ce que l'architecture est utile ?
- est-ce que le GTM est crédible ?
- pourquoi le dossier est-il qualitatif ou non ?

Cette évaluation ne juge pas si la startup doit être financée. Elle juge si l'équipe Product, Tech et Growth a produit de bons livrables stratégiques.

Elle regarde notamment :
- la qualité produit
- la qualité technique
- la qualité growth
- la collaboration entre agents
- la clarté et l'utilité des documents

Dans les séries de tests précédentes, cette évaluation qualité était souvent plus favorable, notamment parce qu'elle s'appuyait sur un historique de versions et pouvait mesurer une progression relative.

Les évaluations V1 actuelles sont davantage des évaluations "one shot" : elles ne comparent pas une trajectoire d'amélioration, elles jugent le dossier produit tel quel. Il est donc normal qu'elles paraissent moins encourageantes.

### Pourquoi garder les deux lectures ?

Les deux évaluateurs ne répondent pas à la même question.

L'évaluation qualité demande :
- est-ce que les livrables sont bons ?
- est-ce que le système multi-agents travaille correctement ?
- est-ce que les documents sont clairs, actionnables et cohérents ?

L'évaluation CEO demande :
- est-ce que ce projet mérite un investissement ?
- est-ce que le risque est acceptable ?
- est-ce que le potentiel business justifie d'aller plus loin ?

Le point important : les évaluateurs ne sont pas des agents de plus dans la collaboration. Ce sont des instruments de mesure externes.

Ils ont aidé à éviter une illusion fréquente : croire qu'un workflow plus sophistiqué est meilleur simplement parce qu'il produit plus de traces internes.

### Second pass à partir d'une évaluation

Une expérimentation importante a consisté à utiliser une évaluation externe comme point de départ d'une nouvelle passe.

Le principe :
1. une version du dossier existe déjà
2. un évaluateur externe produit une critique
3. Product réoriente le cadrage
4. Growth et Tech rechallengent
5. Product arbitre une nouvelle version

Cette logique rapprochait le système d'un cycle réel de travail : produire, recevoir un retour, réviser, consolider.

Mais elle a aussi révélé une limite importante : une deuxième version n'est pas automatiquement meilleure qu'une première. Certains runs devenaient plus propres, plus complets, mais perdaient des décisions fortes de la version précédente.

Cette expérience a préparé une leçon centrale du projet : il ne suffit pas d'ajouter une boucle de révision. Il faut aussi protéger les bons arbitrages déjà obtenus.

Cette piste mériterait d'être creusée, même si elle a été abandonnée faute de temps.

## Phase 7 - Le travail sur les prompts

Une grande partie du gain de qualité est venue des prompts.

### Première approche

Les premiers prompts demandaient surtout :
- des sections fixes
- des listes courtes
- des risques
- des questions ouvertes
- des demandes de changement

L'objectif était de rendre les sorties faciles à extraire et à stocker dans le blackboard.

### Prompts V2

Une deuxième famille de prompts a cherché à rendre les agents plus décisionnels.

L'intention était bonne :
- moins de texte générique
- plus d'hypothèses critiques
- plus de verdicts
- plus de structure

Mais cette version a révélé un risque : à force de corriger chaque mauvais comportement, les prompts devenaient trop chargés. Les agents étaient parfois plus scolaires, moins naturels, et perdaient en netteté.

### Prompts V3

La V3 a marqué un tournant.

La philosophie a changé :
- moins micro-piloter
- mieux définir le rôle
- clarifier le périmètre
- garder une structure de sortie utile
- laisser l'agent raisonner dans son domaine

Cette version a produit un des meilleurs gains du projet.

Product tenait mieux le wedge MVP. Growth identifiait mieux le goulot de lancement. Tech restait plus macro, plus proportionné, plus utile.

La leçon est simple :

> Un bon prompt d'agent n'est pas forcément le plus long. C'est celui qui donne le bon rôle, le bon niveau d'ambition et le bon type de décision.

## Phase 8 - Readiness et correction ciblée

Le système a ensuite ajouté une logique de `readiness`.

Chaque agent peut qualifier son domaine :
- `READY`
- `LIMITED`
- `INSUFFICIENT`

Puis l'orchestrateur agrège ces jugements en une readiness globale.

Cette étape a changé la nature du projet :
- avant, il produisait seulement des documents
- maintenant, il disait aussi si ces documents étaient suffisamment mûrs

Une boucle de correction ciblée a ensuite été ajoutée.

Si le dossier reste `LIMITED`, le système peut lancer une courte correction sur les points les plus bloquants.

Le but n'est pas de réécrire tout le dossier. Le but est de corriger quelques faiblesses prioritaires :
- cible initiale trop vague
- motion GTM imprécise
- contrôles de données sensibles insuffisants
- hypothèse de business model mal cadrée

Les résultats ont été mitigés.

La boucle fonctionne :
- elle se déclenche
- elle est bornée
- elle est traçable

Mais elle ne transforme pas toujours profondément la qualité du dossier. Certains gaps reviennent. Certains sujets restent `LIMITED`.

Ce n'est pas forcément un échec. Cela peut indiquer que la réponse manquante n'est pas dans le texte, mais dans le terrain, la légalité, le marketing ou la preuve utilisateur.

## Phase 9 - Une question centrale : idée faible ou système faible ?

Les tests ont fait apparaître une question importante.

Quand un dossier reste `LIMITED`, est-ce que cela signifie :
- que le workflow est insuffisant ?
- que les prompts sont mauvais ?
- que le modèle n'est pas assez bon ?
- ou que l'idée elle-même manque encore de preuves ?

La réponse varie selon les projets.

Un bon système agentique ne doit pas forcer artificiellement tous les projets à devenir `READY`. Il doit aussi pouvoir dire :
- cette idée reste floue
- cette preuve manque
- ce risque est réel
- cette décision demande une enquête ou une décision humaine

C'est une limite saine. Un système qui rend tout `READY` serait probablement trop complaisant.

## Phase 10 - Trop de workflow peut dégrader les résultats

Après les gains obtenus par les prompts, le projet a tenté d'améliorer davantage le workflow.

Plusieurs idées ont été testées :
- ownership des gaps par domaine
- tagging plus fin des problèmes
- réconciliation entre arbitrage interne et livrables
- verrouillage de décisions
- règles de conservation
- boucles plus orientées solution

Sur le papier, ces idées semblaient prometteuses.

En pratique, beaucoup ont dégradé les livrables finaux :
- PRD plus lourd
- wedge moins net
- arbitrages plus laborieux
- documents plus bavards
- agents plus contraints
- qualité finale parfois inférieure malgré un blackboard plus sophistiqué

Cette phase a été décisive.

Elle a montré que le meilleur système n'est pas toujours le plus complexe. Trop de workflow peut étouffer le jugement des agents.

## Phase 11 - Retour au baseline V12-like

Après plusieurs régressions, le projet est revenu vers un état plus sobre, appelé `V12-like`.

Ce baseline conserve :
- prompts V3
- Product comme arbitre final
- Growth et Tech comme challengers spécialisés
- readiness
- correction ciblée bornée
- Product locking
- blackboard lisible

Il retire ou évite :
- les surcouches expérimentales trop contraignantes
- les prompts d'équipe génériques
- les boucles qui forcent artificiellement les agents à trancher

Ce retour en arrière n'a pas été un échec. C'est une maturité du projet.

La conclusion provisoire est :

> La bonne version n'est pas celle qui maximise le contrôle. C'est celle qui garde le meilleur équilibre entre spécialisation, sobriété, lisibilité et qualité finale.

## Phase 12 - Prompt d'équipe : bonne idée, mauvais effet

Un `team_prompt.md` générique a été testé.

L'idée était raisonnable :
- rappeler que les agents travaillent ensemble
- clarifier les rôles Product, Growth, Tech
- renforcer l'objectif commun

Mais les résultats ont suggéré un effet négatif.

Même générique, ce prompt pouvait ramollir la posture individuelle des agents. Ils semblaient parfois chercher davantage une synthèse consensuelle qu'un jugement strict dans leur domaine.

Une variante intégrée directement dans chaque prompt agent a aussi été testée, puis retirée.

Leçon :
- la collaboration doit être portée par le workflow et le blackboard
- les prompts doivent rester centrés sur le rôle propre de chaque agent
- trop rappeler "l'équipe" peut réduire la tension utile entre rôles

## Phase 13 - Passage à Mermaid

Le système produisait d'abord un `Diagram Blueprint`, transformé ensuite en `architecture.pdf`.

Cette approche avait des limites :
- le blueprint était une description intermédiaire
- le PDF était peu maintenable
- le diagramme était difficile à versionner

Le contrat Tech a donc évolué vers Mermaid :
- suppression du `Diagram Blueprint`
- ajout d'une section `Mermaid Diagram`
- extraction vers `architecture-diagram.mmd`
- génération possible de `architecture-diagram.png`
- suppression du PDF d'architecture dans les nouveaux runs

Ce changement n'a pas seulement amélioré l'artefact visuel. Il semble aussi avoir mieux orienté l'agent Tech.

Le fait de demander un diagramme Mermaid oblige Tech à penser en composants, flux et responsabilités. Sans changer profondément son rôle, le formalisme l'a poussé vers des décisions plus structurées, plus pertinentes et plus construites.

C'est une conclusion importante :

> Le format de sortie n'est pas neutre. Un bon artefact peut améliorer le raisonnement de l'agent, pas seulement la présentation du résultat.

## Phase 14 - Contexte Paris / France

Une phrase générique a été ajoutée aux prompts V3 :

`The projects will be implemented in France, in the city of Paris.`

Ce n'est pas une optimisation spécifique à un projet. C'est une hypothèse d'environnement.

Pourquoi l'ajouter ?

Beaucoup de gaps concernaient :
- la géographie
- le droit
- les données personnelles
- la densité locale
- les canaux de lancement
- les opérations terrain

Les agents ne pouvaient pas deviner ce contexte. Sans lui, ils laissaient souvent ouverts les mêmes sujets.

L'ajout Paris / France a amélioré les livrables :
- CareSync devient plus clair sur confiance, données, consentement et posture France/EU
- LocalLoop redevient plus local, plus neighborhood-specific
- Melody gagne en concrétude avec une scène musicale parisienne
- SkillBridge se protège mieux contre la dérive marketplace générique

Le dernier batch comparatif documenté a obtenu :
- CareSync V38 : 7.6/10, `ACCEPTABLE`
- LocalLoop V38 : 7.6/10, `ACCEPTABLE`
- Melody V8 : 7.4/10, `ACCEPTABLE`
- SkillBridge V6 : 7.4/10, `ACCEPTABLE`

La leçon :

> Certains flous ne demandent pas plus de workflow. Ils demandent une hypothèse de contexte réaliste.

## Ce que le projet produit aujourd'hui

Le système produit un dossier composé de plusieurs livrables :
- `prd.md`
- `architecture.md`
- `architecture-diagram.mmd`
- `architecture-diagram.png`
- `gtm.md`
- `blackboard.md`
- `activity_log.txt`

Ces documents ne sont pas tous destinés au même usage.

Le PRD, l'architecture et le GTM sont les livrables principaux.

Le blackboard est la mémoire lisible :
- il montre les décisions
- les tensions
- les gaps
- les arbitrages
- les traces du workflow

L'activity log sert surtout à comprendre ce qui s'est passé dans le run.

## Est-ce que ces documents aident vraiment ?

Oui, mais avec une nuance importante.

Les documents ne remplacent pas une enquête terrain, un vrai travail juridique, des interviews utilisateurs ou une analyse marché sérieuse.

En revanche, ils aident à :
- formuler une première version crédible d'un projet
- identifier les hypothèses critiques
- voir les risques de scope
- distinguer MVP et extensions
- rendre visibles les tensions produit, marché et tech
- poser de meilleures questions avant d'investir davantage

Les derniers runs évalués en V1 sont des lectures plus "one shot" : ils ne bénéficient pas du même historique de comparaison active que certaines séries précédentes.

Cela change surtout l'interprétation de l'évaluation qualité. Dans les suites de tests précédentes, l'évaluateur qualité pouvait s'appuyer sur l'historique, constater une progression, et donc paraître plus favorable. Sur une version isolée, il juge davantage le dossier comme un livrable autonome, sans récompenser explicitement le chemin parcouru.

La posture froide, directe et sceptique appartient plutôt à l'évaluateur CEO. Lui ne mesure pas seulement la qualité des documents : il demande si le projet mérite un investissement, avec une logique go/no-go ou revise.

Mais même dans ce cadre, les résultats restent utiles :
- les questions soulevées sont pertinentes
- le cadrage est souvent crédible
- les livrables donnent une bonne base de discussion
- le système évite une partie de la complaisance naturelle d'un générateur unique

Pour rendre l'outil plus efficace, il faudrait probablement l'utiliser sur plusieurs itérations plus fines, avec des réponses humaines, des données terrain et des validations progressives.

Une comparaison simple resterait intéressante :
- demander le même travail à un agent unique, sans système multi-agents
- comparer la qualité, la profondeur des contradictions et la netteté des décisions

À minima, le système aide déjà à se poser de meilleures questions.

## Ce que le projet est devenu

Le projet n'est plus seulement un générateur de documents.

C'est un système expérimental de cadrage multi-agents avec :
- mémoire centrale
- handoffs
- rôles spécialisés
- arbitrage Product
- readiness
- évaluateur externe
- versioning
- livrables séparés

Il ne transforme pas automatiquement une idée faible en projet fort.

Il aide plutôt à voir :
- ce qui est solide
- ce qui est flou
- ce qui manque
- ce qui doit être testé
- ce qui devrait rester hors scope

## Grandes leçons

### 1. La mémoire centrale est indispensable

Sans blackboard, les agents produisent des textes séparés. Avec une mémoire centrale lisible, le système peut garder une trace des décisions et des handoffs.

### 2. Les handoffs doivent être sobres

Le passage de relais entre agents donne de la structure, mais chaque handoff supplémentaire peut aussi ajouter du bruit.

### 3. Product doit arbitrer

Tech et Growth challengent. Product tranche. Sans arbitrage final, on obtient une juxtaposition d'avis.

### 4. Le prompt est une pièce de design

Un prompt n'est pas une simple instruction. Il définit un rôle, une posture, un niveau d'ambition et un type de sortie.

### 5. Le format de sortie influence le raisonnement

Mermaid en est un bon exemple : demander un diagramme structuré peut améliorer la pensée technique elle-même.

### 6. L'évaluateur externe est précieux

Il permet de sortir de l'auto-satisfaction du système.

L'évaluateur qualité aide à savoir si les livrables Product, Tech et Growth sont clairs, cohérents et actionnables.

L'évaluateur CEO ajoute un regard plus froid : est-ce que le projet mérite vraiment un investissement, ou seulement une révision sous conditions ?

### 7. `LIMITED` n'est pas forcément un échec

Même quand la qualité augmente, beaucoup de dossiers restent `LIMITED`.

C'est normal si les questions restantes demandent :
- enquête terrain
- validation juridique
- preuve marketing
- choix stratégique humain
- données réelles

Un système agentique mature doit savoir signaler cette limite au lieu d'inventer une certitude.

### 8. La sobriété a souvent gagné

Les meilleurs résultats récents ne viennent pas du workflow le plus complexe. Ils viennent d'un équilibre plus simple :
- prompts V3
- pas de prompt d'équipe
- contexte Paris / France
- Product arbitre
- Growth et Tech challengent
- Mermaid pour structurer l'architecture
- readiness sans obsession du `READY`

## Pistes non retenues ou à creuser

### Clarification humaine

Une piste intéressante consiste à générer une petite liste de questions humaines à la fin d'un run.

Exemples :
- quel quartier exact viser ?
- quel seuil de supply minimum ?
- quelle métrique principale de preuve ?
- quelle posture légale validée ?
- quelles règles de consentement, rétention ou compensation ?

Cette piste est prometteuse, car elle traite un vrai manque de contexte sans ajouter une boucle agentique artificielle.

Elle a été laissée hors scope :
- elle demande un nouveau workflow utilisateur
- elle nécessite des tests dédiés
- elle dépasse le temps limite prévu pour finaliser le projet

### Comparaison avec un agent unique

Une autre piste simple serait de demander les mêmes livrables à un agent unique, puis de comparer :
- qualité du PRD
- pertinence des risques
- qualité des contradictions
- précision du GTM
- réalisme technique

Ce test permettrait de mieux mesurer ce que l'agentique apporte vraiment.

### Retour CEO

La version "CEO evaluator" reste intéressante.

Elle ne cherche pas à être encourageante. Elle cherche à répondre :
- est-ce que je porte ce projet ?
- est-ce que j'investis du temps ?
- est-ce que le potentiel est suffisant ?

Ce regard est plus dur que l'évaluateur qualité, mais complémentaire. Il peut donner un verdict go/no-go plus concret.

## Conclusion

Le projet montre qu'un système multi-agents peut améliorer un travail de cadrage, mais seulement s'il reste discipliné.

Les gains ne viennent pas seulement :
- du nombre d'agents
- de la longueur des prompts
- du nombre de boucles
- de la sophistication du blackboard

Ils viennent surtout de l'équilibre entre :
- rôles spécialisés
- mémoire centrale
- handoffs clairs
- prompts sobres
- arbitrage final
- évaluation externe
- acceptation des limites réelles d'un projet

Au final, les documents produits ne donnent pas une vérité définitive.

Ils donnent quelque chose de plus utile pour un POC : une base crédible pour décider quoi creuser, quoi tester, quoi couper, et quelles questions poser ensuite.

## Annexe - Incident de perte d'instances de test

Un incident important s'est produit pendant une tentative de nettoyage manuel des dossiers `outputs/tests`.

L'objectif était de :
- garder seulement quelques versions utiles par projet
- supprimer les versions redondantes
- réduire un historique devenu trop lourd

Ce qui s'est mal passé :
- une suppression automatisée a été lancée trop tôt
- la logique de sélection des dossiers à conserver était fragile
- la commande a supprimé plus que prévu
- Git n'a pu restaurer que les fichiers déjà versionnés
- plusieurs sorties récentes non poussées ont été perdues

Pourquoi l'erreur est arrivée :
- suppression destructive avant validation complète
- absence de manifeste clair des dossiers à garder et à supprimer
- absence d'étape de déplacement en archive temporaire
- confiance excessive dans la capacité de Git à tout restaurer

Leçon opérationnelle :
- pousser régulièrement les versions utiles
- faire un snapshot avant tout nettoyage massif
- générer une liste explicite des chemins conservés et supprimés
- déplacer d'abord en archive
- supprimer seulement après validation

Cet incident limite une partie de la traçabilité fine des anciens runs, mais il n'efface pas les apprentissages principaux du projet : le workflow, les prompts, les comparaisons majeures et les conclusions de conception restent documentés.
