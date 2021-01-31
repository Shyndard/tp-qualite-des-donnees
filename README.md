# Tp qualité des données

## Introduction

> TP dans le cadre de la formation sur la qualité des données

> Ce TP a été réalisée via Jupyter Notebook avec Python 3.8.6

> Groupe constitué de Maël C. et Clément F.

## Traitement

Ce README contient les réponses contenues dans le fichier [Traitement.ipynb](https://github.com/Shyndard/tp-qualite-des-donnees/blob/master/Traitement.ipynb) en expliquant nos choix. Rendez-vous dans ce fichier pour consulter les graphiques. Pour intéragir avec certains graphiques, il est nécessaire d'exécuter le script.

### Traitement du SI en erreur

Pour traiter les données en erreurs, nous avons divisé le traitement en deux étapes :

#### 1. Traiter les données qui ne sont pas des nombres

Lors de la lecture du fichier, lorsqu’une valeur lue n’est pas un nombre alors elle est remplacée par la moyenne de la température du jour précédent et du jour suivant. Cela permet d’avoir un nombre cohérent pour le contexte de température.

#### 2. Traiter les données aberrantes

Une fois les températures lues, les calculs de la moyenne et de l’écart type par mois sont réalisés.
Un traitement repasse sur chaque température et effectue les opérations suivantes :
-  Une température est considérée comme atypique si elle est en dehors de l’intervalle [moyenne - écart type du mois ; moyenne + écart type du mois]. Cela nous permet d’avoir toutes les valeurs qui « sortent du lot ».
- Une température atypique est considérée comme fausse si la valeur absolue de la température actuelle et du jour précédent et/ou jour suivant est supérieure à l’écart type du mois de la température. Cela permet de vérifier qu’une valeur en dehors de l’intervalle s’inscrit dans un contexte cohérent avec le jour précédent et/ou suivant. Le problème de cette correction intervient dans le cas où les températures sont fausses pendant au moins 2 jours consécutifs.

#### 3. Résultats

En appliquant ces traitements sur les températures, nous obtenons les résultats suivants :

| Température initiale | Mois | n° du jour | Cohérence avec premier SI |
| :-----------: |:----:|:----:| :-----------------------------------------:|
| 5 | Février | 6 | NOK |
| -6 | Juillet | 15 | OK |
| 48 | Aout | 14 | OK |
| 1 | Octobre | 15 | NOK |
| -33 | Décembre | 20 | OK |

On observe que 5 valeurs ont été considérées comme fausses alors qu’elles sont vraies selon le premier SI.

Dans l'export ci-dessous, vous trouverez :
- En vert les valeurs (non modifiées) considérées comme fausses par le premier traitement
- En jaune les valeurs (non modifiées) considérées comme fausses par le second traitement
- En rouge les valeurs (non modifiées) considérées comme fausses par le second traitement mais pourtant vraies selon le premier SI

![alt text](https://zupimages.net/up/21/04/5003.png)

### Traitement des données de Savukoski kirkonkyla

Nous avons comparé les valeurs entre les données du SI erreur et Savukoski kirkonkyla. 

Données aquises en divisant les valeurs d'un SI par un autre
|  | Janvier | Février | Mars | Avril | Mai | Juin | Juillet | Aout | Septembre | Octobre | Novembre | Décembre | 
| :- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Moyenne de témpérature | 0.824 | 0.381 | 0.116 | 13.598 | 1.274 | 1.601 | 0.947 | 1.368 | 1.376 | 5.502 | 0.389 | 0.854 |
| Ecart type | 0.732 | 0.625 | 0.744 | 0.979 | 0.916 | 0.852 | 1.357 | 0.829 | 0.609 | 0.353 | 0.982 | 0.361 |
| Température minimale | 0.878 | 0.441 | 0.387 | 0.252 | 2.273 | 2.268 | 0.867 | 1.697 | 4.615 | 0.09 | 0.705 | 0.444 |
| Température maximale | 0.896 | 1.277 | 2.692 | 2.645 | 1.053 | 1.358 | 1.053 | 1.221 | 1.208 | 0.683 | 1.299 | 1.277 |

On observe des écarts importants, il ne s'agit donc pas de la même ville.

> Selon les données, on est dans un pays du nord de l'europe ayant des températures en moyenne en dessous de 0°C en hiver. La capitale européenne qui se rapproche le plus est helsinki (cf. https://www.infoclimat.fr/climatologie/annee/2018/helsinki-vantaa/valeurs/02974.html)