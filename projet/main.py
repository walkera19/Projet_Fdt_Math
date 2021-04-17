from itertools import permutations
import copy
import proprietes as prop


# prend en argument le nom du fichier a lire
# renvoie un tableau d'entier représentant la relation
def lecture_fichier(nom_fichier):
    fichier = open(nom_fichier, encoding='utf-8-sig')
    lignes = fichier.readlines()

    # on stock les valeurs dans un tableau
    relation = []
    i, j = 0, 0
    for ligne in lignes:
        relation.append([])
        for char in ligne:
            if char == '1' or char == '0':
                relation[i].append(int(char))
            j += 1
        i += 1
    if [] in relation:
        relation.remove([])

    # verification de la taille de la matrice:
    n = len(relation)
    for i in range(n):
        if len(relation[i]) != n:
            print('La matrice n\'est pas de la forme attendue')
            exit(1)

    return relation


def transforme_ordre_total_2(relation):
    n = len(relation)
    nb_perm = int((n * (n - 1)) / 2)

    distance_min = n**2
    meilleurS = []

    # on génère les permutations possibles de nb_perm 0 et 1
    for p in range(2**nb_perm):
        # on met sous forme de liste les nombres binaires
        perm = [int(d) for d in str(bin(p))[2:]]
        # on ajoute des 0 au début pour qu'ils aient tous la bonne longueur
        perm = [0]*(nb_perm - len(perm)) + perm

        # cree une matrice de taille n x n remplie de 1
        # on ne modifiera pas la diagonale pour conserver la réflexivité
        S = [[1 for col in range(n)] for row in range(n)]
        distance_kemeney = 0

        for i in range(n):
            for j in range(i + 1, n):
                # on met les permutations trouvées dans la partie triangulaire supérieure de la matrice
                cellule = perm[bijection(i, j, n - 1)]
                S[i][j] = cellule
                # la matrice est symétrique
                if cellule == 0:
                    S[j][i] = 1
                else:
                    S[j][i] = 0

        if not prop.transitive(S) and not prop.complete(S):
            continue

        # On calcul la distance de Kemeney de la matrice
        for i in range(n):
            for j in range(n):
                if S[i][j] == relation[i][j]: distance_kemeney += 1

        if distance_min > distance_kemeney:
            distance_min = distance_kemeney
            meilleurS = copy.deepcopy(S)
    return meilleurS, distance_min


# on génère toute les matrices réflexives, transitives, complètes et antisymétriques possibles
# on calcul la distance entre ces matrices et la relation donnée
def transforme_ordre_total_3(relation):
    n = len(relation)
    nb_perm = int((n * (n - 1)) / 2)
    perm = []  # contient toutes les combinaisons de n 0 et 1

    for i in range(nb_perm + 1):
        # on cree une liste avec i fois 1 et n-1 fois 0
        liste = [1] * i + [0] * (nb_perm - i)
        # on prend les permutations de la liste sans les doublons (enlevés par set())
        perm += list(set(permutations(liste)))

    # a chaque permutation on associe une matrice
    distance_min = n ** 2
    meilleurS = []
    for tuple_perm in perm:
        # cree une matrice de taille n x n remplie de 1
        # on ne modifiera pas la diagonale pour conserver la réflexivité
        distance_kemeney = 0
        S = [[1 for col in range(n)] for row in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                # on met les permutations trouvées dans la partie triangulaire supérieure de la matrice
                cellule = tuple_perm[bijection(i, j, n - 1)]
                S[i][j] = cellule
                # la matrice est symétrique
                if cellule == 0:
                    S[j][i] = 1
                else:
                    S[j][i] = 0
                # On calcul la distance de Kemeney de la matrice
                if S[i][j] == relation[i][j]: distance_kemeney += 1
                if S[j][i] == relation[j][i]: distance_kemeney += 1
        # si S est transitive et complète
        # si S est la meilleure matrice trouvée on la garde
        if prop.transitive(S) and prop.complete(S) and distance_min > distance_kemeney:
            distance_min = distance_kemeney
            meilleurS = S
    return meilleurS, distance_min


def affiche_matrix(mat):
    for ligne in mat:
        print(ligne)


# fonction bijective qui associe à chaque couple d'indice un entier entre 1 et n
# permet d'associer à chaque case de la matrice un indice des permutations
def bijection(i, j, n):
    return int(j - 1 + (n * (n - 1)) / 2 - ((n - i) * (n - i - 1)) / 2)


# GERER LES AFFICHAGES
def main():
    # nom_fichier = input("Entrez le nom du fichier (extension comprise) où se trouve la relation: ")
    nom_fichier = '1.txt'

    relation = lecture_fichier(nom_fichier)
    # affiche_prop(relation)

    # on obligé de mettre '!= True' car la valeur retournées n'est pas toujours un bool
    if prop.ordre_total(relation) != True:
        s, d = transforme_ordre_total_2(relation)
        print("\n\nL'ordre total le plus proche de la relation donnée est : ")
        affiche_matrix(s)
        print("\nLa distance de Kemeney est de", d)

        s, d = transforme_ordre_total_3(relation)
        print("\n\nL'ordre total le plus proche de la relation donnée est : ")
        affiche_matrix(s)
        print("\nLa distance de Kemeney est de", d)


main()
