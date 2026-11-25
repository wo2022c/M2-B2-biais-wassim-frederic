# Note de risques

| Risque | Usage concerné | Chiffre à l'appui | Personnes touchées | Mesure proposée | Risque restant |
| --- | --- | --- | --- | --- | --- |
| Acompte demandé à tort selon le pays | Annulation : acompte | Fausses alertes : 43,8 % (Portugal) contre 11,7 % (autres) | 1 137 clients portugais fiables en 4 mois | Acompte remboursable, validation humaine, analyse d'impact | Avance de trésorerie inégale entre groupes |
| Le pays se devine sans `country` | Les deux usages d'annulation | AUC 0,83 ; 2 425 des 2 426 réservations « Non Refund » sont portugaises | Tous les clients | Faire expliquer `deposit_type` par l'hôtel avant toute correction | Biais indirect par `market_segment` |
| Retirer `country` déplace l'écart | Les deux usages d'annulation | Fausses alertes des autres pays : 11,7 % → 34,8 % ; précision globale : 72 % → 60 % | 3 329 clients fiables d'autres pays, au lieu de 1 114 | Ne pas retirer `country` seul | Écart inversé, non supprimé |
| Relances plus fréquentes pour les Portugais | Annulation : relance | Taux d'alertes : 74,4 % contre 22,3 % | 5 076 réservations portugaises signalées | Message identique pour tous, suivi par groupe | Gêne limitée à un message |
