# Projet_Fondements_Math

## Strucutre générale:
  1. Lecture du fichier
  2. Liste des propriétés satisfaites ou non par la relation
  3. Liste de structures de préférances vérifiées par la relation
  4. Ordre total le plus proche en distance de Kemeney

<br><br>

### 1. Lecture du fichier
L'utilisateur doit saisir le nom du fichier (avec extention) dans l'invite de commande. 
Le fichier doit contenir une matrice carrée de 0 et de 1.<br>
Le programme ne retiendra que les caratères 0 et 1 donc un fichier de la forme:<br>
1 a 0<br>
0 1<br>
ne fera pas d'erreur et donnera la matrice [[1, 0], [0, 1]]. 
Il n'est cependant pas conseillé de mettre autre chose que 0, 1, \n et espaces pour éviter les erreurs.<br>
On vérifie aussi si le nombre d'éléments par ligne est bien le même dans tout le fichier et s'il est égal au nombre de ligne
(c'est-à-dire qu'on vérifie si la matrice est bien carrée).

<br><br>

### 2. Liste des propriétés satisfaites ou non par la relation
Les propriétés étudiées sont:
  - réflexive
  - symétrique
  - antisymétrique
  - transitive
  - semi-transitive
  - negativement transitive
  - ferrer
  -complète
<br>Pour chacune de ces relations, on affichera un message indiquant si elle est vérifiée ou non par la relation lue dans le fichier.
Si elle ne l'est pas, on donnera des éléments qui violent cette propriété.

<br>
<br>

### 3. Liste des structures de préférances vérifiées par la relation
Les structures de préférances étudiées sont:
  - ordre total
  - ordre partiel
  - préordre partiel
  - préordre total
  - semi-ordre
  - ordre d'intervalle
<br>
Pour chacune de ces relations, on affichera un message indiquant si elle est vérifiée ou non par la relation.

<br>
<br>

### 4. Ordre total le plus proche en distance de Kemeney
<br>**Si la relation n'est pas un ordre total, on donne l'ordre total le plus proche en distance de Kemeney**<br>
D'après nous recherches, ce problème est np_complet. <br>
Nous avons donc choisi de générer toutes les matrices symétriques et réflexives de la même taille que la relation,
puis de filtrer celle qui étaient transitives et completes.
Enfin, on calcul la distance de Kemeney entre la relation et les matrices obtenues et on garde la matrice ayant la plus petite distance.<br>
Remarque: pour optimiser le stockage, on ne gardera en mémoire que la meilleure matrice.
<br><br>
**Création des matrices symétriques et réflexives de la même taille que la relation:**
<br>On pose n la taille de la relation. <br>
Du fait de la réflexivité, on sait que la diagonale sera entièrement composée de 1.
De plus étant symétriques, on peut faire toutes les combinaires possibles sur les cellules strictement au dessus de la diagonale
puis compléter de la même façon sous la diagonale. <br>
On génère donc des permutations de taille n*(n-1)/2 composées de 0 et 1.
On construit aussi une bijection qui associe a chaque couple d'indice un entier entre 0 et n*(n-1)/2.
Grace à cette bijection, on peut construire une matrice par permutation.

