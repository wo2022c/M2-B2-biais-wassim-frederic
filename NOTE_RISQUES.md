# Note de risques

<!-- toc -->
## Sommaire

- [Risques, du plus grave au moins grave](#risques-du-plus-grave-au-moins-grave)
- [Cadre réglementaire](#cadre-réglementaire)
- [Désaccord au sein du binôme](#désaccord-au-sein-du-binôme)
<!-- /toc -->

## Risques, du plus grave au moins grave

| Risque | Usage concerné | Chiffre à l'appui | Personnes touchées | Mesure proposée | Risque restant |
| --- | --- | --- | --- | --- | --- |
| Acompte demandé à tort selon le pays | Annulation : acompte | Fausses alertes : 43,8 % (Portugal) contre 11,7 % (autres) | 1 137 clients portugais fiables en 4 mois | Ne pas mettre l'acompte en service | Aucun tant que l'acompte reste écarté |
| Le pays se devine sans `country` | Les deux usages d'annulation | AUC 0,83 ; 2 425 des 2 426 réservations « Non Refund » sont portugaises | Tous les clients | Faire expliquer `deposit_type` par l'hôtel avant toute correction | Biais indirect par `market_segment` |
| Retirer `country` déplace l'écart | Les deux usages d'annulation | Fausses alertes des autres pays : 11,7 % → 34,8 % ; précision globale : 72 % → 60 % | 3 329 clients fiables d'autres pays, au lieu de 1 114 | Retirer `country` pour la relance seulement, suivre les fausses alertes par groupe | Écart inversé, non supprimé ; plus de relances à tort |
| Relances plus fréquentes pour les Portugais | Annulation : relance | Taux d'alertes : 74,4 % contre 22,3 % | 5 076 réservations portugaises signalées | Message identique pour tous, suivi par groupe | Gêne limitée à un message |

## Cadre réglementaire

Classement établi avec l'aide d'un assistant IA, à vérifier sur les textes (EUR-Lex, CNIL). Ce n'est pas un avis juridique.

| Usage | Base légale envisagée | Principe en tension | Niveau AI Act et justification |
| --- | --- | --- | --- |
| Annulation : relance | Intérêt légitime (RGPD art. 6), avec mise en balance | Minimisation et information (art. 5 et 13) : le pays est-il nécessaire, le client sait-il qu'un score est calculé ? | Risque minimal : la réservation hôtelière ne figure pas dans l'annexe III. Pas d'obligation spécifique, hors maîtrise de l'IA (art. 4). |
| Annulation : acompte | Intérêt légitime, plus difficile à justifier ; à défaut, clause du contrat | Décision automatisée (art. 22) si l'acompte est exigé sans intervention humaine. Non-discrimination : Code pénal art. 225-2, règlement (UE) 2018/302. Analyse d'impact (art. 35). | Risque minimal au sens de l'annexe III : l'hôtel n'est pas un service privé essentiel. Le risque porte sur le RGPD et la discrimination, pas sur le classement. |

## Désaccord au sein du binôme

**Point discuté :** l'écart d'alertes est-il injuste alors que les Portugais annulent plus (62 % contre 26 %) ?

- **Pour l'accepter :** le modèle reflète la réalité, il est plus précis pour les Portugais (78 % contre 61 %) et une relance coûte peu.
- **Contre :** il juge la personne selon son groupe. Parmi les clients qui viennent, l'écart de fausses alertes (43,8 % contre 11,7 %, soit ×3,7) dépasse celui des annulations (62 % contre 26 %, soit ×2,4). La vraie cause semble être le type de tarif, pas la nationalité.

**Décision :** relance acceptée sans le pays. Acompte refusé, car l'effet sur le client est trop fort pour un écart qu'on ne sait pas expliquer.

**Coût assumé :** sans le pays, l'écart de taux d'alertes se resserre (55 % contre 44 %, au lieu de 74 % contre 22 %). En contrepartie, les fausses alertes passent de 18,5 % à 31,3 % sur l'ensemble des clients. Ce coût est acceptable pour une relance, qui se limite à un message.
