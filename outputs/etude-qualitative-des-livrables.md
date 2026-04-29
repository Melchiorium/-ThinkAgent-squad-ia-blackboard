# Etude qualitative des livrables

## Pourquoi cette note

Cette page rassemble une lecture qualitative de l'historique des livrables produits par le systeme multi-agents.

Elle ne cherche pas a juger si chaque startup "va marcher".
Elle cherche a repondre a une autre question :

- est-ce que les livrables produits sont de bonne qualite ?
- est-ce qu'ils deviennent plus clairs, plus concrets, plus decisionnels ?
- est-ce que les iterations ameliorent vraiment le dossier, ou seulement sa forme ?

## Perimetre et limite importante

Une partie des versions de tests a ete perdue lors d'un nettoyage destructif mal securise de `outputs/tests`.

Cette synthese repose donc sur :
- l'historique conserve dans [agent-project-history.md](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/agent-project-history.md)
- les evaluations encore presentes
- les reevaluations refaites sur les V1
- les notes comparatives conservees dans le suivi de travail

Conclusion importante :
- la tendance generale reste exploitable
- mais la tracabilite fine run par run est incomplete

## Grille de lecture

Les livrables ont ete juges selon cinq axes :
- qualite produit
- qualite technique
- qualite growth / GTM
- qualite de collaboration entre agents
- qualite globale des livrables

Le systeme n'a pas ete note sur "la probabilite de faire un unicorn".
Il a ete note sur sa capacite a produire un cadrage serieux, critique et exploitable.

## Resume executif

Le constat global est plutot bon.

Le systeme ne produit plus seulement des documents plausibles. Dans ses meilleurs etats, il produit :
- un wedge MVP clair
- une architecture proportionnee au vrai sujet
- un GTM plus concret
- des desaccords visibles
- une synthese finale assez proche d'un document de travail interne credible

En revanche, le systeme n'a pas encore atteint un niveau "strong" stable.
Son plafond actuel est plutot :
- de bons livrables `ACCEPTABLE`
- souvent compris entre 7.0 et 7.6/10
- avec des limites recurrentes sur les decisions que seuls des humains, du terrain ou de la recherche externe peuvent vraiment fermer

Autrement dit :
- il aide bien a cadrer
- il aide bien a identifier les vrais trous
- il aide bien a eviter les faux MVP trop larges
- mais il ne remplace pas une vraie decision humaine quand il manque du contexte, de la preuve terrain ou une validation legale

## Ce qui s'est vraiment ameliore avec le temps

### 1. Le wedge MVP est devenu nettement meilleur

Au debut, les projets avaient tendance a rester trop larges ou trop abstraits.
Avec les iterations, surtout via les prompts V3, les meilleurs dossiers ont appris a :
- choisir une cible plus etroite
- choisir un usage de preuve plus concret
- repousser les expansions non necessaires
- distinguer ce qui doit etre construit de ce qui peut rester manuel

C'est probablement le progres le plus visible du systeme.

### 2. L'architecture est devenue plus juste

Le systeme a cesse de surproduire des architectures trop lourdes.
Les meilleures versions techniques ont appris a :
- rester macro
- cibler la vraie contrainte
- expliciter les etats, gates, audit trails et control points
- faire apparaitre les vraies dependances MVP

Le passage au couple `architecture-diagram.mmd + png` a aussi apporte un gain qualitatif.
Pas seulement en lisibilite :
- le format Mermaid semble avoir pousse l'agent Tech vers des decisions plus structurees
- le schema est devenu un vrai artefact technique source
- le PDF etait plus passif, moins maintenable, moins utile

### 3. Le GTM est devenu plus credible

Les premiers GTM avaient tendance a rester trop generiques.
Les meilleurs runs ont ensuite mieux formule :
- qui on essaie de convaincre d'abord
- quel est le vrai goulot initial
- quel signal de preuve doit etre observe
- ce qui doit etre manuel au debut

Le systeme est devenu meilleur quand Growth a ete pousse a chercher le vrai bottleneck, pas a raconter un plan marketing large.

### 4. La sortie finale est devenue plus decisionnelle

Le point important n'est pas seulement que les agents ecrivent mieux.
C'est qu'ils arbitrent mieux.

Les meilleurs livrables finaux montrent :
- ce qui est retenu
- ce qui est differe
- ce qui est rejete
- ce qui reste ouvert

C'est un vrai progres par rapport a un simple "texte collaboratif".

## Ce qui reste structurellement faible

### 1. Les memes gaps reviennent souvent

Quand un projet reste `LIMITED`, ce n'est pas forcement parce que le systeme est mauvais.
Tres souvent, les gaps restants sont reels :
- choix geographique exact
- seuil minimal de supply ou de densite
- valeur de preuve precise
- regles exactes de consentement ou de retention
- cadre legal valide
- arbitrage business qui depend d'un terrain reel

Le systeme sait souvent bien les nommer.
Il sait moins bien les fermer sans contexte supplementaire.

### 2. Le workflow trop complexe a souvent degrade les resultats

C'est une des lecons les plus fortes du projet.

Ajouter :
- plus de boucles
- plus de contraintes intermediaires
- plus de mecanismes de reconciliation
- plus de sophistication d'orchestration

... n'a pas automatiquement ameliore les livrables.

Dans plusieurs cas, cela a au contraire produit :
- plus de verbosite
- des wedges moins nets
- des arbitrages plus mous
- plus de structure interne, sans gain clair dans les documents finaux

Le meilleur equilibre observe reste un baseline sobre :
- prompts V3
- roles bien separes
- workflow relativement direct
- boucle de correction simple
- locking Product final

### 3. Les agents ne doivent pas inventer une precision qu'ils n'ont pas

Dans les projets les plus difficiles, une mauvaise correction serait de "faire semblant de savoir".

Exemples typiques :
- inventer un quartier sans raison
- inventer une posture legale trop sure
- fixer une metrique de preuve artificielle
- trancher une hypothese terrain sans aucune base

Le systeme est utile quand il resiste a cette fausse precision.
Il est moins bon quand il essaie de fermer un trou qui devrait en fait etre remonte a un humain.

## Ce que les projets racontent

## CareSync

### Impression generale

CareSync est l'un des projets les plus solides en termes de cadrage produit.
Le systeme comprend bien le coeur du probleme :
- coordination familiale
- information fragmentee
- confiance
- permissions
- documents sensibles

### Forces recurrentes
- bon wedge "un proche / un coordinateur / une routine"
- bon recentrage sur la coordination plutot que sur un "care OS"
- bonne sensibilite aux risques de permissions, d'audit, de boundaries et de support
- GTM generalement credible en concierge pilot

### Faiblesses recurrentes
- privacy/compliance France ou EU souvent laissee partiellement ouverte
- policy documents / consent / deletion / retention rarement fermee jusqu'au bout
- canal de reminder et fallback parfois encore flous
- permissions exactes parfois pas suffisamment verrouillees

### Lecture qualitative

CareSync produit souvent de bons livrables.
Sa limite n'est pas un manque d'intelligence produit.
Sa limite est que le projet touche vite a des zones ou la qualite depend d'un vrai choix de posture de confiance et de cadre legal minimal.

## LocalLoop

### Impression generale

LocalLoop est probablement le projet qui a le plus clairement montre quand le systeme etait bon... et quand il regressait.

Quand le systeme est bien regle, LocalLoop devient tres net :
- quartier precis
- categorie etroite
- une offre
- une boucle de visite / redemption / loyalty
- une obsession pour la qualite de supply

Quand le systeme se relache, LocalLoop regresse tres vite vers :
- app locale generique
- discovery trop large
- social / reviews / restaurants / loyalty sans wedge clair

### Forces recurrentes
- excellente identification du vrai sujet : densite et quality control
- bonnes architectures de gating, stale control, token lifecycle, dispute handling
- bon GTM supply-first
- projet tres sensible a la clarte du wedge, donc bon test de qualite du systeme

### Faiblesses recurrentes
- quartier exact souvent non choisi
- seuil minimum de marchands souvent non fixe
- methode de redemption parfois encore partiellement ouverte
- risque permanent de retour vers un marketplace local trop large

### Lecture qualitative

LocalLoop est le meilleur thermometre du systeme.
Quand les prompts et le workflow sont bons, le projet devient excellentement cadre.
Quand ils se degradent, LocalLoop part vite dans le flou.
Son historique raconte tres bien la difference entre un systeme qui tranche et un systeme qui brode.

## Melody

### Impression generale

Melody a beaucoup progresse lorsque le systeme a appris a lui imposer une promesse plus etroite :
- Paris only
- une scene
- concert companion
- musique comme signal

### Forces recurrentes
- bonne reduction de scope quand le systeme est bien regle
- trust layer utile pour un produit de matching
- bonne discipline sur la moderation, l'activation gate et l'etat des profils

### Faiblesses recurrentes
- these centrale encore fragile : la musique seule suffit-elle ?
- densite locale difficile a prouver
- risque de devenir un dating app re-skinne
- scene exacte et seuils de preuve souvent encore ouverts

### Lecture qualitative

Melody montre une bonne capacite du systeme a resserrer un concept ambigu.
Mais il montre aussi que certains projets peuvent rester intelligents sans devenir vraiment convaincants.
Le systeme aide bien a poser la bonne question ; il ne peut pas, seul, prouver que le signal est assez fort.

## SkillBridge

### Impression generale

SkillBridge est fort quand il reste une plateforme tres contrainte de missions bornees, et faible quand il glisse vers un faux marketplace freelance.

### Forces recurrentes
- bonne protection contre la derive marketplace
- bonne architecture de moderation, taxonomie, et proof issuance
- bonne distinction entre mission bornee et travail ouvert

### Faiblesses recurrentes
- legal framing France tres sensible
- valeur reelle du proof-of-work encore a prouver
- tensions ethiques sur compensation / travail gratuit / exploitation percue
- GTM parfois moins net que le PRD sur le premier segment exact

### Lecture qualitative

SkillBridge est un bon projet de stress test sur les sujets trust / legal / proof credibility.
Les livrables sont souvent solides, mais le projet touche rapidement des questions qui demandent autre chose qu'un bon raisonnement interne.

## Evolution globale de la qualite

En simplifiant fortement, on peut lire l'historique comme quatre phases.

### Phase 1 - Premiers livrables credibles mais encore descriptifs
- bonnes intuitions
- trop de texte consultant
- pas assez de choix fermes

### Phase 2 - Gain net via roles plus clairs et prompts V3
- meilleurs wedges
- meilleures architectures
- meilleure capacite a dire non
- sorties beaucoup plus credibles

### Phase 3 - Tentation de complexifier le workflow
- plus de traceabilite
- plus de sophistication
- mais souvent moins de nettete dans les livrables

### Phase 4 - Retour a un baseline plus sobre + contexte Paris / France + Mermaid
- regain qualitatif
- meilleurs dossiers transverses
- meilleures decisions structurelles sans inflation de workflow

## Ce qu'on peut conclure honnetement

### Oui, les livrables aident vraiment

Ils aident au minimum a :
- poser les bonnes questions
- resserrer un MVP
- faire remonter les dependances critiques
- distinguer build maintenant vs manuel au debut
- voir les angles morts que beaucoup de briefs cachent

Dans les meilleurs cas, ils aident plus que cela :
- ils produisent un vrai dossier de cadrage interne credible
- ils permettent de comparer des versions
- ils donnent une bonne base de discussion pour une vraie decision humaine

### Non, ils ne remplacent pas encore un jugement complet

Ils ne suffisent pas, seuls, a fermer :
- les choix terrain
- la preuve d'usage
- la validation legale
- certains arbitrages business

Leur vraie valeur aujourd'hui est :
- de structurer la pensee
- de rendre les tensions visibles
- de ne pas laisser passer un faux dossier "propre mais creux"

## Ma lecture finale

La qualite generale des livrables a reelement progresse.
Le systeme est passe :
- d'un generateur de documents plausibles
- a un outil de cadrage critique, multi-angle, globalement serieux

Son meilleur niveau actuel n'est pas encore "decision finale autonome".
Mais il est deja utile comme :
- machine a clarifier
- machine a resserrer
- machine a challenger
- machine a expliciter pourquoi un projet reste encore incomplet

La lecon la plus importante est peut-etre la suivante :

le systeme devient meilleur non pas quand on lui ajoute toujours plus de workflow, mais quand on lui donne :
- des roles nets
- un contexte d'execution utile
- une structure sobre
- et le droit de dire qu'un projet n'est pas encore pret.

## Repere rapide sur les derniers runs

Dernier batch qualitatif documente dans l'historique :

| Projet | Version | Note | Verdict |
|---|---:|---:|---|
| CareSync | V38 | 7.6 | ACCEPTABLE |
| LocalLoop | V38 | 7.6 | ACCEPTABLE |
| Melody | V8 | 7.4 | ACCEPTABLE |
| SkillBridge | V6 | 7.4 | ACCEPTABLE |

