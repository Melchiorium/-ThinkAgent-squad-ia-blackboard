# Lot 16 - Documentation et validation du lien secret

## Objectif

Documenter l'étape 4 : accès au POC par lien secret via `WEB_ACCESS_TOKEN`.

Ce lot est strictement documentaire. Il ne doit pas modifier le code applicatif.

## Contexte projet utile

- Le lot 15 ajoute la protection par lien secret.
- Il ne s'agit pas d'une authentification complète.
- Le POC reste sans comptes utilisateurs.
- Les sessions navigateur `web_session_id` restent séparées du contrôle d'accès.
- Le mécanisme sert seulement à limiter l'accès accidentel à une URL publique ou
  partagée.

## Fichiers autorisés à modifier

- `README.md`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml` seulement si une règle courte est utile

## Fichiers à ne pas modifier

- `app/`
- `docs/ai/contracts.yaml`
- `app/prompts V3/`
- `outputs/tests/`
- `outputs/rapport_final.md`
- `outputs/workflow.md`
- `requirements.txt`

## Travail demandé - README

Mettre à jour la section `Viewer Web POC`.

Ajouter une sous-section courte ou quelques lignes expliquant :

- si `WEB_ACCESS_TOKEN` est défini, il faut ouvrir :

```text
https://<host>/?access_token=<token>
```

- après validation du token, l'app pose un cookie local ;
- si `WEB_ACCESS_TOKEN` n'est pas défini, l'app reste ouverte ;
- ce mécanisme n'est pas une authentification complète ;
- ne pas partager le lien publiquement.

Ne pas réécrire le README complet.

## Travail demandé - modules.yaml

Mettre à jour l'entrée `web` pour mentionner :

- contrôle d'accès POC par `WEB_ACCESS_TOKEN` ;
- cookie `web_access_granted` ;
- protection des routes applicatives ;
- route `static` laissée accessible pour le CSS.

Ne pas ajouter un nouveau module si toute la logique est dans `app/web.py`.

## Travail demandé - flows.yaml

Ajouter un flux :

```yaml
web_secret_link_access_flow:
  owner: app/web.py
  status: poc_access_control
  steps:
    - read WEB_ACCESS_TOKEN
    - allow all requests when the token is unset
    - allow static assets
    - accept access_token query parameter when it matches the configured token
    - store a non-raw-token access cookie after successful validation
    - allow later requests with a valid access cookie
    - reject other application requests with 403
  limitations:
    - not full authentication
    - no user accounts
    - no roles or permissions
    - shared-token POC only
```

Ne pas modifier `web_generation_job_flow` sauf si nécessaire pour mentionner que
les routes sont désormais behind the POC access gate.

## Travail demandé - rules.yaml

Ajouter une règle seulement si elle aide vraiment les futurs agents.

Règle acceptable :

```yaml
- The web access token is a POC shared-link guard. Do not expand it into full
  auth, accounts, roles, or OAuth unless explicitly requested.
```

Si `rules.yaml` semble déjà assez clair, ne pas le modifier.

## Validation

Exécuter :

```bash
python3 -m compileall app
git diff -- README.md docs/ai/modules.yaml docs/ai/flows.yaml docs/ai/rules.yaml
git diff -- docs/ai/contracts.yaml
git diff -- "app/prompts V3"
```

Attendus :

- compile OK ;
- README modifié de façon ciblée ;
- `modules.yaml` mentionne `WEB_ACCESS_TOKEN` et `web_access_granted` ;
- `flows.yaml` contient `web_secret_link_access_flow` ;
- aucun diff sur `contracts.yaml` ;
- aucun diff sur les prompts V3.

## Vérification manuelle recommandée

Après implémentation du lot 15 :

```bash
WEB_ACCESS_TOKEN=secret-test python3 app/web.py
```

Puis vérifier :

1. `/` sans token retourne une page refusée ou `403` ;
2. `/?access_token=secret-test` donne accès ;
3. une navigation suivante sans query token fonctionne grâce au cookie ;
4. `POST /jobs` reste inaccessible sans token/cookie ;
5. `POST /jobs` fonctionne après accès valide.

Ne pas lancer une vraie génération LLM dans cette vérification sauf accord du
mainteneur.

## Critères d'acceptation

- La documentation correspond au comportement réel.
- Elle ne promet pas de login ou de comptes.
- Elle explique clairement le lien secret.
- Elle ne modifie pas les contrats blackboard.
- Elle ne modifie pas les prompts.

## Contraintes AGENTS.md

- Commencer par lire `docs/ai/00-index.yaml`.
- Garder la documentation courte et factuelle.
- Ne pas transformer le POC en architecture auth complète.
- Ne pas modifier les outputs générés.
- Ne pas modifier les prompts.
