from itertools import permutations


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
            return 'La matrice n\'est pas carrée'

    return relation


# toutes les fonctions ci dessous renvoient True si la relation vérifie cette propriété
# et l'indice / les indices d'un contre exemple si la relation ne vérifie pas cette propriété

def reflexive(relation):
    for x in range(len(relation)):
        if relation[x][x] != 1:
            print("La relation n'est pas reflexive: à l'indice", x, "sur la diagonale, on a un 0")
            return x
    print("La relation est reflexive")
    return True


def symetrie(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            if relation[x][y] != relation[y][x]:
                print("La relation n'est pas symétrique: R(", x, y, ") != R(", y, x,")")
                return x, y
    print("La relation est symétrique")
    return True


def asymetrique(relation):
    for x in range(len(relation)):
        # 0 sur la diagonale
        if relation[x][x] != 0:
            print("La relation n'est pas asymétrique: à l'indice", x, "sur la diagonale, on a un 0")
            return x
        for y in range(len(relation)):
            # aij = 1 => aji = 0
            if relation[x][y] == 1 and relation[y][x] == 1:
                print("La relation n'est pas asymétrique: R(", x, y, ") = 1 mais R(", y, x, ") != 0")
                return x, y
    print("La relation est asymétrique")
    return True


def transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 1 and relation[y][z] == 1 and relation[x][z] == 0:
                    print("La relation n'est pas transitive: R(", x, y, ") = 1  and R(", y, z, ") = 1, pourtant R(", x, z, ") != 1")
                    return x, y, z
    print("La relation est transitive")
    return True


def semi_transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[y][z] == 1 and (relation[x][z] == 0 and relation[z][w] == 0):
                        print("La relation n'est pas semi-transitive: R(", x, y, ") = 1  and R(", y, z, ") = 1, pourtant R(", x, z, ") != 1 et R(", z, w, ") != 1")
                        return x, y, z, w
    print("La relation est semi-transitive")
    return True


def negtransitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 0 and relation[y][z] == 0 and relation[x][z] == 1:
                    print("La relation n'est pas transitive: R(", x, y, ") = 0  and R(", y, z, ") = 0, pourtant R(", x, z, ") != 0")
                    return x, y, z
    return True


def ferrer(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[y][z] == 1 and (relation[x][w] == 0 and relation[z][w] == 0):
                        print("La relation n'est pas ferrer: R(", x, y, ") = 1  and R(", y, z, ") = 1, pourtant R(",
                              x, w, ") != 1 et R(", z, w, ") != 1")
                        return x, y, z, w
    print("La relation est ferrer")
    return True


def complete(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            # au moins l'un des deux doit etre 1 pour que ce soit complet
            if relation[x][y] == 0 and relation[y][x] == 0:
                print("La relation n'est pas complete: R(", x, y, ") = 0 et R(", y, x, ") = 0")
                return x, y
    print("La relation est complete")
    return True


def ordre_total(relation):
    if reflexive(relation) and transitive(relation) and complete(relation) and not symetrie(relation):
        print("La relation est un ordre total")
        return True
    print("La relation n'est pas un ordre total")
    return False


def ordre_partiel(relation):
    if reflexive(relation) and transitive(relation) and not symetrie(relation):
        print("La relation est un ordre partiel")
        return True
    print("La relation n'est pas un ordre partiel")
    return False


def preodre_partiel(relation):
    if reflexive(relation) and transitive(relation):
        print("la relation est un préordre partiel")
        return True
    print("La relation n'est pas un préordre partiel")
    return False


def preordre_total(relation):
    if reflexive(relation) and transitive(relation) and complete(relation):
        print("la relation est un préordre total")
        return True
    print("La relation n'est pas un préordre total")
    return False


def semi_ordre(relation):
    if reflexive(relation) and complete(relation) and semi_transitive(relation) and ferrer(relation):
        print("La relation est un semi-ordre")
        return True
    print("La relation n'est pas un semi-ordre")
    return False


def ordre_intervalle(relation):
    if reflexive(relation) and complete(relation) and ferrer(relation):
        print("La relation est pas un ordre d'intervalle")
        return True
    print("La relation n'est pas un ordre d'intervalle")
    return False


# on génère toute les matrices réflexives, transitives, complètes et antisymétriques possibles
# on calcul la distance entre ces matrices et la relation donnée
def transforme_ordre_total(relation):
    n = len(relation)
    nb_perm = int((n*(n-1))/2)
    perm = []  # contient toutes les combinaisons de n 0 et 1
    for i in range(nb_perm + 1):
        # on cree une liste avec i fois 1 et n-1 fois 0
        liste = [1]*i + [0]*(nb_perm-i)
        # on prend les permutations de la liste sans les doublons (enlevés par set())
        perm += list(set(permutations(liste)))

    # a chaque permutation on associe une matrice
    distance_min = n**2
    meilleurS = []
    for tuple_perm in perm:
        # cree une matrice de taille n x n remplie de 1
        # on ne modifiera pas la diagonale pour conserver la réflexivité
        distance_Kemeney = 0
        S = [[1 for col in range(n)] for row in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                # on met les permutations trouvées dans la partie triangulaire supérieure de la matrice
                cellule = tuple_perm[bijection(i, j, n-1)]
                S[i][j] = cellule
                # la matrice est symétrique
                if cellule == 0: S[j][i] = 1
                else: S[j][i] = 0
                # On calcul la distance de Kemeney de la matrice
                if S[i][j] == relation[i][j]: distance_Kemeney += 1
                if S[j][i] == relation[j][i]: distance_Kemeney += 1
        # si S est transitive et complète et
        # si S est la meilleure matrice trouvée on la garde
        print(distance_Kemeney)
        affiche_matrix(S)
        if transitive(S) and complete(S) and distance_min > distance_Kemeney:
            distance_min = distance_Kemeney
            meilleurS = S
    print(meilleurS)
    return meilleurS


def affiche_matrix(mat):
    for ligne in mat:
        print(ligne)
    print('\n')


# fonction bijective qui associe à chaque couple d'indice un entier entre 1 et n
# permet d'associer à chaque case de la matrice un indice des permutations
def bijection(i, j, n):
    return int(j - 1 + (n * (n - 1))/2 - ((n - i) * (n - i - 1))/2)


# GERER LES AFFICHAGES
def main():
    # nom_fichier = input("entrez le nom du fichier (extension comprise) où se trouve la relation: ")
    """
    nom_fichier = 'antisym_comp.txt'
    relation = lecture_fichier(nom_fichier)
    reflexive(relation)
    symetrie(relation)
    asymetrique(relation)
    transitive(relation)
    semi_transitive(relation)
    negtransitive(relation)
    ferrer(relation)
    complete(relation)
    ordre_total(relation)
    ordre_partiel(relation)
    preodre_partiel(relation)
    preordre_total(relation)
    semi_ordre(relation)
    ordre_intervalle(relation)
    """
    transforme_ordre_total([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


main()

"""
n = 5
for i in range(0, 6):
    for j in range(0,6):
        print(j - 1 + ((n*(n-1)) / 2 - ((n - i)*(n-i-1)) / 2), end = ' ')
    print('\n')
"""
