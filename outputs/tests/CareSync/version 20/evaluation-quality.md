# Evaluation qualite - CareSync - Version 20

Sources lues: `prd.md`, `architecture.md`, `architecture.pdf`, `gtm.md`, `blackboard.md`.

## Scores
- Product: 6/10
- Tech: 5/10
- Growth: 5/10
- Collaboration: 3/10
- Qualite des livrables: 5/10

Note finale: 4.8/10

Verdict final: WEAK

## Evaluation

La V20 corrige certains defauts visibles de la V19. Le wedge est plus lisible: coordonner les rendez-vous medicaux et les rappels medicaments pour des parents ages, avec des familles a distance. Le PRD ajoute aussi deux elements importants qui manquaient ou etaient incoherents auparavant: user permission management dans le MVP et support manuel pendant le pilote. C'est une amelioration de surface utile.

Le probleme reste bien identifie, mais le scenario de preuve manque encore de precision. Le workflow parle de profils d'elderly relatives, de rendez-vous, de rappels, de notifications et de partage de taches. Pourtant le scope exclut l'advanced task management, ce qui cree une ambiguite: partage-t-on vraiment des taches, ou seulement des rappels et rendez-vous? Le messaging reste dans le MVP alors que la proposition de valeur principale est la coordination structuree, pas une nouvelle messagerie familiale.

La qualite produit est donc moyenne. Les criteres d'acceptation sont plus concrets que V19, mais encore insuffisants pour une decision de pilote: "3 family members active", "80% satisfaction", "10 appointments/reminders tracked" ne disent pas combien de familles participent, sur quelle duree, avec quel seuil de retention ou quelle preuve que l'outil remplace vraiment les alternatives existantes. Le MVP est comprehensible, mais pas encore decision-ready.

La partie technique identifie les bons sujets: RBAC, consentement, audit logs, notification service, chiffrement, admin/support, compliance tracking. Mais elle reste trop generique. Le choix d'une architecture microservices cloud est lourd pour un MVP qui devrait surtout tester usage, confiance et fiabilite de rappels. Le document ne fixe pas le pays de lancement, les exigences reglementaires, la matrice exacte des roles, la politique de retention/suppression, ni les regles d'acces support/admin. Les mentions de chiffrement et compliance restent des intentions, pas un design executable.

La GTM est correcte mais peu tranchee. Elle identifie l'inertie des familles, propose un positionnement complementaire aux outils existants, et prevoit onboarding manuel + data entry assistance. C'est mieux que V19. Mais le premier canal reste flou: social media, forums, educational content, partenariats elder care, referrals. Rien n'est vraiment choisi. Le plan ne dit pas comment recruter les premieres familles, combien en recruter, combien de temps dure le pilote, ni quel signal prouve que l'inertie est depassee.

Le plus gros probleme est la collaboration. Le blackboard indique que le product arbitration est en heuristic fallback, avec "aucun element retenu", "aucun changement applique", puis un scope quand meme verrouille. Pire: des recommandations critiques comme RBAC, compliance checklist, audit logs et onboarding workflow sont marquees comme rejetees dans l'arbitrage, alors qu'elles reapparaissent ensuite dans le PRD ou l'architecture comme si elles etaient acceptees. Ce n'est pas une tension mineure: c'est une incoherence de gouvernance des livrables.

## Angles morts majeurs
- Pays de lancement et cadre reglementaire non fixes.
- Consentement, retention, suppression et breach process non definis.
- Permission matrix concrete absente malgre "user permission management" en scope.
- Contradiction entre task sharing dans le workflow et advanced task management hors scope.
- Messaging inclus sans justification claire face au risque de recreer WhatsApp.
- Architecture microservices trop lourde pour le stade MVP.
- Aucun protocole pilote complet: taille cohorte, duree, recrutement, retention, seuil proceed/revise/stop.
- Product arbitration incoherent: recommandations critiques rejetees/deferrees mais reutilisees ailleurs.

## Conclusion

Livrable faible, mais legerement plus prometteur que V19 sur le cadrage produit. La V20 remet permission management et support manuel dans la conversation, ce qui va dans le bon sens. Elle reste toutefois non decision-ready a cause d'un arbitrage tres faible, d'une architecture trop generique, d'un plan GTM peu tranche et de blocages compliance toujours ouverts. Avant build, il faut verrouiller un pays, une matrice d'acces, un protocole pilote et nettoyer les contradictions du blackboard.
