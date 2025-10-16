PLAN DE TESTS – Système de notation patinage artistique

TODO : Compléter le plan de tests suivants : 

| # | Description du test          | vbase | notes                         | Résultat attendu | Résultat obtenu |
|---|------------------------------|-------|-------------------------------|------------------|-----------------|
| 1 | Cas normal                   | 3.2   | [3,2,1,2,3,3,2,2,3]           | 5.63             | 5.63            |
| 2 | Plusieurs max/min identiques | 2.5   | [0,0,0,0,0,0,0,0,0]           | 2.5              | 2.5             |
| 3 | Notes négatives              | 1.0   | [-1,-2,-1,-3,-2,-1,-3,-2,-3]  | -1               | -1              |
| 4 | Liste invalide (taille)      | 3.0   | [1,2,1,2,3,4,2,3,2,2,3,2,3,2] | Erreur           | Erreur          |
| 5 | Valeurs hors bornes          | 2.5   | [4,5,3,1,2,3,6,7,9,5,5,4,-5]  | Erreur           | Erreur          |

