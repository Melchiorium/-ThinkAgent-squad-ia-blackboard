# Histoire De Construction Du Projet D'Agents

## Pourquoi ce document

Ce document raconte, de façon simple, comment le projet a été construit pas à pas.

L'idée de départ était de créer un petit système multi-agents capable de :
- faire travailler plusieurs rôles spécialisés sur un même projet
- les faire challenger une idée sous plusieurs angles
- produire un cadrage final plus solide qu'une réponse unique

Ici, le mot "agent" ne désigne pas un robot autonome complexe. Dans ce projet, un agent est surtout :
- un rôle clair
- un prompt dédié
- un accès à un état partagé
- une place précise dans un workflow

Le projet a donc évolué comme un produit logiciel classique :
- premiers prototypes très simples
- ajout progressif de briques
- changements de stack
- amélioration des prompts
- amélioration du workflow
- amélioration de la lisibilité pour l'humain

## Le point de départ

Le premier objectif n'était pas de construire "une vraie intelligence collective" d'un seul coup.

Le but était plus modeste :
- tester un flux minimum
- vérifier qu'un agent peut lire un brief
- produire un premier document
- garder une trace de ce qui s'est passé

Le projet a donc commencé avec un objet central très simple : le `blackboard`.

## Étape 1 : le blackboard partagé

La première brique a été un `blackboard` commun.

Concrètement, c'est une structure de données Python partagée entre les agents. Elle sert de mémoire commune.  
Au début, elle contenait surtout :
- le brief projet
- un brouillon de PRD
- des notes d'architecture
- des notes GTM
- des listes de risques, questions, décisions

Pourquoi commencer par là ?

Parce qu'un système multi-agents sans mémoire partagée devient vite flou :
- on ne sait plus qui a produit quoi
- on ne sait plus ce qui a été retenu
- on ne sait plus comment relire le raisonnement

Le blackboard a donc servi de colonne vertébrale du projet.

## Étapes 2 et 3 : premier appel LLM et premier flux de bout en bout

Une fois le blackboard posé, l'étape suivante a été de créer un appel LLM partagé, puis un flux très simple :
- un brief en entrée
- un agent test
- un texte en sortie

Ce premier prototype servait surtout à valider la tuyauterie :
- chargement du brief
- appel modèle
- écriture dans le blackboard
- export d'un fichier résultat

À ce moment-là, le projet n'était pas encore vraiment "multi-agent".  
Il s'agissait d'un squelette exécutable.

## Premier changement technique important : abandon du plan OpenAI direct au profit d'Ollama

Au départ, le contexte imaginait un usage plus direct d'API externes.  
Mais rapidement, le projet a bifurqué vers un usage local avec Ollama via une API compatible OpenAI.

Pourquoi ce changement ?

Plusieurs raisons pratiques :
- coût nul
- tests plus libres
- dépendance réduite à une clé externe
- possibilité d'itérer vite sur les prompts

Le compromis était clair :
- moins de coût
- plus de contrôle
- mais qualité et stabilité du modèle plus variables

Cette étape a été importante parce qu'elle a forcé à garder une couche LLM commune et configurable, au lieu de lier tout le projet à un fournisseur unique.

## Étapes 4 et 5 : apparition des vrais rôles

Après les premiers tests, le système a été structuré autour de trois rôles :
- `Product`
- `Tech`
- `Growth`

L'idée était simple :
- `Product` cadre le besoin, le MVP, le PRD
- `Tech` challenge la faisabilité et propose une architecture
- `Growth` challenge le go-to-market et l'acquisition

À ce stade, le projet devient vraiment un système multi-agents, mais encore linéaire :
1. Product écrit
2. Tech réagit
3. Growth réagit

Pourquoi cette séparation ?

Parce qu'une seule réponse LLM mélange souvent plusieurs couches à la fois :
- vision produit
- choix techniques
- acquisition
- contraintes business

En séparant les rôles, on espérait obtenir :
- plus de clarté
- plus de spécialisation
- plus de contradiction utile

## Étape 6 : ajout de la boucle de révision Product

Une limite est vite apparue :
- si Product écrit une première version
- puis Tech et Growth répondent
- mais que personne ne consolide vraiment

... alors on obtient juste trois textes côte à côte.

La réponse a été d'ajouter une deuxième passe Product :
1. Product rédige un premier cadrage
2. Tech challenge
3. Growth challenge
4. Product réécrit une version finale

Pourquoi c'était important ?

Parce qu'un système de collaboration ne vaut pas grand-chose si personne n'arbitre à la fin.  
Cette étape a transformé le pipeline d'une simple juxtaposition en une première forme de synthèse.

## Étapes 7 à 9 : rendre les échanges lisibles pour un humain

Un problème est alors apparu dans les résultats :
- les agents "travaillaient"
- mais un humain comprenait mal ce qui avait réellement changé

Le blackboard brut était utile pour la machine, moins pour le lecteur.

Le projet a donc évolué vers deux vues :
- une vue interne, structurée, pour les agents
- une vue Markdown, plus narrative, pour l'humain

Cela a entraîné plusieurs améliorations :
- conservation du PRD initial avant révision
- stockage des demandes de changement par agent
- résumé de revue
- liste de changements appliqués ou non

Pourquoi ce travail de présentation comptait ?

Parce qu'un bon système multi-agents ne doit pas seulement produire un bon résultat.  
Il doit aussi permettre de comprendre :
- qui a recommandé quoi
- ce qui a été retenu
- ce qui reste incertain

## Les premières limites constatées

À ce stade, plusieurs faiblesses sont apparues dans les sorties :

### 1. Les agents restaient trop descriptifs

Ils produisaient des documents plausibles, mais pas toujours décisionnels.  
Autrement dit :
- ils racontaient une bonne idée
- mais aidaient encore mal à décider s'il fallait investir

### 2. Tech et Growth faisaient trop de suggestions générales

Ils réagissaient souvent comme des consultants prudents :
- beaucoup de remarques
- pas assez de choix concrets

### 3. Product réintégrait parfois les retours trop "brut"

Le PRD final pouvait se retrouver pollué par :
- des résumés de revue
- des notes techniques
- des artefacts de prompts

### 4. Le modèle local montrait ses limites

Avec `qwen2.5-coder:7b`, plusieurs symptômes sont apparus :
- dérive hors brief
- choix arbitraires
- qualité inégale
- mélange de langues
- difficulté à tenir un rôle propre jusqu'au bout

Cette phase a été précieuse parce qu'elle a montré que :
- le problème ne venait pas seulement du code
- mais aussi du modèle
- et surtout de la façon de distribuer les responsabilités entre agents

## Étapes 9.x : gros travail sur les prompts

Une grande partie du projet a ensuite consisté à retoucher les prompts.

Ce travail a beaucoup évolué :

### Première phase

On a d'abord demandé aux agents d'être plus clairs et plus structurés :
- sections fixes
- listes courtes
- risques
- questions ouvertes
- demandes de changement

But :
- faciliter l'extraction
- rendre le blackboard exploitable

### Deuxième phase

On a ensuite demandé aux agents de proposer de vraies solutions :
- Tech devait produire une architecture réelle
- Growth un vrai plan GTM
- Product un vrai PRD consolidé

But :
- éviter des sorties trop faibles ou purement consultatives

### Troisième phase

On a alors découvert un autre excès :
- Tech pouvait surprescrire
- Product pouvait trop absorber
- les documents pouvaient devenir trop lourds

Les prompts ont donc été resserrés pour :
- rester proportionnés à un MVP
- éviter les architectures trop ambitieuses
- empêcher la fuite de métadonnées de revue dans le PRD final

Cette période a montré une chose très importante pour un public non expert :

Un agent n'est pas "intelligent tout seul".  
Une grande partie de sa qualité dépend :
- de son rôle
- de ses consignes
- de ce qu'on lui demande de produire
- de ce qu'on lui interdit de faire

## Étape 10 : migration vers Gemini, puis test OpenAI

Après les limites du modèle local, le projet a tenté une migration vers l'API Gemini via une interface compatible OpenAI.

Pourquoi ?

Parce que la qualité de fond devenait un frein :
- meilleure cohérence attendue
- meilleure capacité de synthèse
- moins d'artefacts bizarres

Les résultats se sont globalement améliorés :
- documents plus crédibles
- architecture mieux calibrée
- meilleur respect du brief

Ensuite, le projet a aussi testé OpenAI avec `gpt-5.4-mini`, toujours via une couche compatible.

Pourquoi ce point est important ?

Parce qu'il montre que l'architecture du projet n'était pas pensée pour un seul fournisseur.  
La couche LLM a été conçue pour permettre des essais comparatifs sans devoir réécrire tout le pipeline.

## Étapes 11 à 13 : du "texte collaboratif" à l'arbitrage

Le projet a alors changé de nature.

Avant :
- les agents produisaient surtout des textes spécialisés

Après :
- les agents ont commencé à produire des contributions plus structurées
- Product a pris un vrai rôle d'arbitre final

Des notions ont été ajoutées au blackboard :
- décisions retenues
- décisions différées
- recommandations rejetées
- points ouverts
- tensions non résolues

Pourquoi ce changement ?

Parce qu'une collaboration utile ne consiste pas seulement à produire plus de texte.  
Elle consiste à rendre visible la décision.

À partir de là, on ne voulait plus seulement savoir :
- ce que Tech pense
- ce que Growth pense

On voulait aussi savoir :
- ce que Product garde
- ce que Product repousse
- ce qui reste dangereux

## Étape 14 : introduction d'un second pass à partir d'une évaluation externe

Une nouvelle idée a ensuite été testée :
- prendre une version déjà produite
- y ajouter un rapport d'évaluation "CEO"
- faire une nouvelle passe de révision

Le workflow est devenu :
1. une première version existe
2. une évaluation externe critique cette version
3. Product réoriente le cadrage
4. Tech et Growth rechallengent
5. Product arbitre une `v2`

Pourquoi c'était intéressant ?

Parce que cela rapprochait le système d'un vrai cycle de travail en entreprise :
- première proposition
- retour d'un décideur
- révision
- consolidation

Mais cela a aussi révélé une limite :
- une v2 n'est pas forcément meilleure qu'une v1

Dans certains cas, la v2 est devenue plus "propre", mais moins solide.  
Cela a montré que le système savait encore mal protéger les acquis forts d'une version précédente.

## Nouvelle phase : travail intensif sur les prompts

À partir de là, le projet a cessé d'évoluer seulement par le code.  
Une grande partie de la progression est venue d'un travail beaucoup plus fin sur les prompts.

Deux idées importantes se sont imposées :
- il ne faut pas écraser trop vite les prompts existants
- il faut pouvoir comparer plusieurs philosophies d'agents

Une première famille de prompts plus "décisionnels" a donc été créée en parallèle de la base historique :
- `prompts V2`

L'intention était bonne :
- moins de texte générique
- plus d'hypothèses critiques
- plus de verdicts explicites

Mais un effet secondaire est apparu :
- à force de vouloir corriger les agents point par point
- les prompts sont parfois devenus trop précis, trop scolaires, trop chargés

Autrement dit :
- on expliquait parfois trop le métier aux agents
- au lieu de leur donner un rôle fort et une direction claire

## Le tournant V3 : revenir à des rôles plus nets

Une nouvelle famille de prompts a alors été créée :
- `app/prompts V3/product_prompt.md`
- `app/prompts V3/tech_prompt.md`
- `app/prompts V3/growth_prompt.md`

Cette fois, la philosophie a changé.

L'idée n'était plus :
- de corriger chaque mauvais comportement un par un

Mais plutôt :
- de mieux incarner le rôle général de chaque agent
- de les guider vers l'essentiel
- de réduire les consignes trop professorales
- de garder des structures de sortie utiles, sans micro-piloter tout le raisonnement

Ce changement a produit un des meilleurs gains du projet.

Pourquoi ?

Parce que les agents se sont remis à raisonner de façon plus naturelle :
- `Product` a mieux tenu le wedge MVP
- `Tech` a été meilleur quand il restait macro et focalisé sur la vraie contrainte
- `Growth` a été meilleur quand on lui demandait surtout de voir le vrai goulot de marché

L'enseignement majeur a été le suivant :

Un bon prompt d'agent ne doit pas seulement être plus détaillé.  
Il doit surtout être plus juste sur :
- le rôle
- le périmètre
- la responsabilité
- le type de décision attendu

## Ajout de la readiness et de la boucle de correction

Une nouvelle évolution importante a ensuite été introduite :
- ne plus seulement générer un dossier
- mais aussi qualifier son niveau de maturité

Le système a donc ajouté une couche de `readiness` avec trois statuts simples :
- `READY`
- `LIMITED`
- `INSUFFICIENT`

Chaque agent produit désormais son propre jugement :
- `Product Readiness`
- `Technical Readiness`
- `GTM Readiness`

Puis l’orchestrateur les agrège en un statut global.

Pourquoi cette évolution est importante ?

Parce qu’elle change la nature du système :
- avant, il écrivait un dossier
- maintenant, il dit aussi si ce dossier est assez bon pour avancer

Ensuite, une étape supplémentaire a été ajoutée :
- si le dossier est `LIMITED`
- le système lance une courte boucle de correction ciblée

Le but n’est pas de tout réécrire.
Le but est de corriger les points les plus bloquants.

Par exemple :
- clarifier une cible initiale
- préciser une motion GTM trop vague
- expliciter des contrôles minimums sur des données sensibles
- formuler plus clairement une hypothèse de business model

Cette évolution a fait passer le projet :
- d’un système de génération
- à un système de génération + qualification + tentative de correction

## Ce que les premiers tests de correction ont montré

Les premiers résultats ont été instructifs.

Bonne nouvelle :
- le mécanisme fonctionne
- la boucle se déclenche bien
- elle est bornée
- elle est traçable dans le blackboard

Mais une limite est apparue :
- la qualité du dossier n’augmente pas toujours beaucoup après correction

En pratique, on a vu des cas où :
- les mêmes gaps revenaient
- la readiness restait `LIMITED`
- les corrections amélioraient un peu la forme, mais pas profondément le fond

Et c’est là qu’une interrogation importante est apparue.

## Nouvelle question centrale : idée faible ou workflow à améliorer ?

Pendant longtemps, il était naturel de penser :
- si le résultat n’est pas assez bon, il faut améliorer le workflow
- ou les prompts
- ou le modèle

Mais les derniers tests ont montré qu’une autre hypothèse est parfois plus juste :
- certaines idées de départ sont simplement encore trop faibles, trop floues ou trop peu prouvées

Autrement dit :
- le système n’échoue pas forcément
- il peut au contraire signaler correctement qu’un projet n’est pas encore prêt

C’est un point très important.

Un bon système agentique ne doit pas forcer artificiellement toutes les idées à devenir `READY`.  
Il doit aussi pouvoir dire :
- cette idée reste `LIMITED`
- les questions restantes ne sont pas rédactionnelles
- elles sont réelles : terrain, marché, confiance, usage, conformité, adoption

## L'autre grande phase : essayer d'améliorer le workflow

Après les gains obtenus sur les prompts, le projet a naturellement tenté une autre voie :
- mieux structurer le workflow
- mieux tracer les décisions
- mieux réconcilier le blackboard avec les livrables finaux
- mieux forcer les agents à résoudre les problèmes identifiés

Plusieurs idées ont été testées :
- readiness globale et locale
- boucle de correction ciblée
- ownership des tâches de correction
- tagging des gaps
- passe finale de verrouillage Product
- réconciliation entre arbitrage interne et livrables finaux
- tentatives de boucle orientée "solutions"

Sur le papier, ces idées semblaient très prometteuses.  
Dans la pratique, elles ont révélé une limite importante.

## Le constat clé : trop contraindre par le workflow a souvent dégradé les résultats

L'un des apprentissages majeurs du projet a été contre-intuitif.

On aurait pu penser :
- plus le workflow est sophistiqué
- plus les résultats seront bons

Mais les tests ont montré l'inverse dans plusieurs cas.

À partir du meilleur état connu autour de :
- `CareSync version 12`
- `LocalLoop version 12`

chaque nouvelle couche de workflow a souvent apporté :
- plus de traçabilité
- plus de structure interne
- plus de sophistication

... mais pas forcément de meilleurs livrables finaux.

Au contraire, plusieurs essais ont dégradé la qualité :
- scope moins bien tenu
- wedge plus flou
- arbitrages plus lourds
- documents plus bavards
- blackboard plus complexe sans gain clair côté PRD / architecture / GTM

Le système devenait parfois plus intelligent "sur le papier", mais moins bon dans ses résultats utiles.

## Pourquoi ce point est important

Ce constat a changé la façon de voir le projet.

Le risque n'était plus seulement :
- un système trop faible

Mais aussi :
- un système trop médié
- trop instrumenté
- trop contraint par des couches intermédiaires

En clair :
- plus de workflow ne veut pas forcément dire plus de qualité
- plus de logique d'orchestration peut affaiblir la netteté du jugement des agents

Cela a conduit à une conclusion provisoire forte :

Le meilleur équilibre obtenu jusqu'ici vient de :
- prompts `V3`
- workflow relativement sobre
- boucle de correction existante mais simple
- locking pass Product conservée
- sans les surcouches expérimentales ajoutées après le meilleur baseline

## Le retour à un baseline V12-like

Après plusieurs essais d'amélioration du workflow, le projet a donc volontairement fait marche arrière.

Un correctif a été appliqué pour revenir vers un état `V12-like` :
- conservation des prompts `V3`
- suppression des couches expérimentales postérieures qui n'amélioraient pas les résultats
- retour à un workflow plus lisible et plus direct

Ce retour en arrière n'a pas été un échec.  
Au contraire, il a été une étape de maturité.

Il a permis de comprendre une chose essentielle :

Dans un système agentique, il faut parfois résister à la tentation d'ajouter toujours plus de contrôle.  
La bonne version n'est pas toujours la plus complexe.  
C'est celle qui garde le meilleur équilibre entre :
- spécialisation des rôles
- qualité des prompts
- sobriété du workflow
- lisibilité des décisions

## La bonne suite : tester sur plus de projets

La conclusion provisoire n’est donc pas :
- “il faut forcément encore boucler plus”

La conclusion la plus saine est :
- il faut tester le système sur davantage de projets

Pourquoi ?

Parce que c’est la seule façon de distinguer clairement :

### Cas 1 : le workflow est le vrai problème

Si beaucoup de projets restent bloqués pour les mêmes raisons, cela suggère :
- une boucle de correction trop faible
- des tâches de correction mal formulées
- une logique d’arbitrage encore insuffisante

### Cas 2 : l’idée est le vrai problème

Si certains projets progressent bien mais qu’un projet précis reste `LIMITED`, cela suggère plutôt :
- un problème de qualité intrinsèque du projet
- une hypothèse business non prouvée
- un manque de wedge
- une trop forte dépendance à des validations terrain

Autrement dit, la prochaine phase du projet doit être comparative :
- plusieurs briefs
- plusieurs types de produits
- plusieurs niveaux de clarté

Cela permettra de mieux comprendre si le plafond actuel vient :
- du système agentique
- ou des idées qu’on lui demande d’évaluer

## Ce que l'évaluateur a apporté

Les retours d'évaluation ont servi de tournant.

Ils ont poussé le projet vers une idée forte :

Une bonne proposition ne doit pas seulement dire :
- "voici un produit possible"

Elle doit surtout dire :
- "qu'est-ce qu'il faut croire pour investir ?"
- "qu'est-ce qui pourrait faire échouer ce projet ?"
- "qu'est-ce qu'on peut tester vite et à faible coût ?"

Cela a entraîné un recadrage important :
- Product doit définir un wedge clair
- Growth doit identifier le vrai goulot de départ
- Tech doit juger ce qu'il faut réellement construire
- les désaccords doivent être visibles
- la sortie finale doit assumer un verdict

## Ce que le projet est devenu

Aujourd'hui, le projet n'est plus un simple générateur de documents.

Il est devenu un système expérimental de cadrage multi-agents avec :
- un état partagé
- des rôles distincts
- des sorties spécialisées
- une logique d'arbitrage
- une mémoire des désaccords
- des versions archivées

Mais surtout, il est devenu un projet qui a appris une leçon importante sur l'agentique appliquée :

Le progrès ne vient pas seulement de "plus d'agents", "plus de boucles" ou "plus de workflow".  
Il vient souvent d'un meilleur équilibre entre :
- la qualité du rôle donné à chaque agent
- la simplicité du pipeline
- la capacité à trancher
- et l'humilité de reconnaître qu'une idée peut rester faible même avec un bon système autour.

Autrement dit, on est passé :

de :
- "un LLM écrit un texte"

à :
- "plusieurs rôles spécialisés examinent un projet, se contredisent partiellement, puis produisent une synthèse arbitrée"

## Les grandes leçons apprises

### 1. Le workflow compte autant que le modèle, mais il doit rester sobre

Un bon modèle seul ne suffit pas.  
Si le workflow est flou, les sorties le seront aussi.

Mais l'expérience a montré l'inverse aussi :
- un workflow trop chargé
- trop contraint
- trop instrumenté

... peut dégrader les résultats.

Le bon enjeu n'est donc pas seulement d'ajouter du workflow.  
C'est de trouver le bon niveau de structure.

### 2. Le prompt est une pièce de design, pas juste une consigne

Le prompt définit :
- le rôle
- le niveau d'ambition
- le style de raisonnement
- ce qui est attendu
- ce qui est interdit

### 3. Le blackboard est utile, mais seulement s'il est lisible

Une mémoire partagée brute ne suffit pas.  
Il faut aussi une traduction humaine compréhensible.

### 4. La collaboration doit déboucher sur une décision

Trois avis séparés ne valent pas encore une décision.  
Il faut une phase finale d'arbitrage.

### 5. Les versions doivent être traçables

Dès qu'on compare plusieurs runs, ou plusieurs briefs, ou plusieurs révisions, le versioning devient indispensable.

### 6. Un bon système doit aussi savoir dire qu’une idée n’est pas prête

Le but n’est pas d’obtenir `READY` à tout prix.  
Le but est de produire un jugement fiable.

Si un projet reste `LIMITED` après correction, ce n’est pas toujours un échec du système.  
Cela peut être un bon signal sur la faiblesse réelle de l’idée.

## Ce qu'il reste à explorer

Le projet a déjà beaucoup mûri, mais plusieurs pistes restent ouvertes :
- mieux comparer les performances entre prompts V2 et V3
- rendre les verdicts encore plus explicites
- mieux protéger les acquis forts d'une version précédente pendant les révisions
- rendre les sorties encore plus utiles pour une vraie décision d'investissement
- mieux distinguer ce qui doit être construit de ce qui peut rester manuel au début
- comparer le comportement du système sur un ensemble plus large de projets pour distinguer les limites du workflow des limites des idées testées

## Résumé en une phrase

Le projet a commencé comme un prototype simple de génération de documents, puis a progressivement évolué vers un système multi-agents plus structuré, plus traçable et plus orienté décision, grâce à une suite d'ajustements sur la mémoire partagée, les prompts, les modèles utilisés et le workflow d'arbitrage.
