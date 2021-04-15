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
            return x
    return True


def symetrie(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            if relation[x][y] != relation[y][x]:
                return x, y
    return True


def asymetrique(relation):
    for x in range(len(relation)):
        # 0 sur la diagonale
        if relation[x][x] != 0:
            return x, x
        for y in range(len(relation)):
            # aij = 1 => aji = 0
            if relation[x][y] == 1 and relation[y][x] == 1:
                return x, y
    return True


def transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 1 and relation[y][z] == 1 and relation[x][z] == 0:
                    return x, y, z
    return True


def semi_transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[y][z] == 1 and relation[x][z] == 0 and relation[z][w] == 0:
                        return x, y, z, w
    return True


def negativement_transitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 0 and relation[y][z] == 0 and relation[x][z] == 1:
                    print("La relation n'est pas transitive: R(", x, y, ") = 0  and R(", y, z, ") = 0, pourtant R(", x,
                          z, ") != 0")
                    return x, y, z
    return True


def ferrer(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[y][z] == 1 and (relation[x][w] == 0 or relation[z][w] == 0):
                        return x, y, z, w
    return True


def complete(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            # au moins l'un des deux doit etre 1 pour que ce soit complet
            if x != y and relation[x][y] == 0 and relation[y][x] == 0:
                return x, y
    return True


def ordre_total(relation):
    if reflexive(relation) and transitive(relation) and complete(relation) and not symetrie(relation):
        return True
    return False


def ordre_partiel(relation):
    if reflexive(relation) and transitive(relation) and not symetrie(relation):
        return True
    return False


def preodre_partiel(relation):
    if reflexive(relation) and transitive(relation):
        return True
    return False


def preordre_total(relation):
    if reflexive(relation) and transitive(relation) and complete(relation):
        return True
    return False


def semi_ordre(relation):
    if reflexive(relation) and complete(relation) and semi_transitive(relation) and ferrer(relation):
        return True
    return False


def ordre_intervalle(relation):
    if reflexive(relation) and complete(relation) and ferrer(relation):
        return True
    return False


# on génère toute les matrices réflexives, transitives, complètes et antisymétriques possibles
# on calcul la distance entre ces matrices et la relation donnée
def transforme_ordre_total(relation):
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
        distance_Kemeney = 0
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
    return int(j - 1 + (n * (n - 1)) / 2 - ((n - i) * (n - i - 1)) / 2)


def affiche_prop(relation):
    ref = reflexive(relation)
    sym = symetrie(relation)
    asym = asymetrique(relation)
    trans = transitive(relation)
    semi_t = semi_transitive(relation)
    neg_t = negativement_transitive(relation)
    fer = ferrer(relation)
    comp = complete(relation)
    ot = ordre_total(relation)
    op = ordre_partiel(relation)
    pp = preodre_partiel(relation)
    pt = preordre_total(relation)
    so = semi_ordre(relation)
    oi = ordre_intervalle(relation)

    print("Propriétés: ")
    if ref ==  True:
        print("La relation est reflexive")
    else:
        print("La relation n'est pas reflexive: R(", ref, ", ", ref, ") = 0", sep='')

    if sym == True:
        print("La relation est symétrique")
    else:
        print("La relation n'est pas symétrique: R(", sym[0], ", ", sym[1], ") != R(", sym[1], ", ", sym[0], ")",
              sep='')

    if asym == True:
        print("La relation est asymétrique")
    elif (asym[0] == asym[1]):
        print("La relation n'est pas asymétrique: R(", asym[0], ', ', asym[1], ") = 1", sep='')
    else:
        print("La relation n'est pas asymétrique: R(", asym[0], ', ', asym[1], ") = 1 mais R(", asym[1], ', ', asym[0],
              ") != 0",
              sep='')

    if trans == True:
        print("La relation est transitive")
    else:
        print("La relation n'est pas transitive: R(", trans[0], ', ', trans[1], ") = 1 et R(", trans[1], ', ', trans[0],
              ") = 1, pourtant R(", trans[0], ', ', trans[2], ") = 0 ", sep='')

    if semi_t == True:
        print("La relation est semi-transitive")
    else:
        print("La relation n'est pas semi-transitive: R(", semi_t[0], ', ', semi_t[1], ") = 1  and R(", semi_t[1], ', ',
              semi_t[2],
              ") = 1, pourtant R(", semi_t[0], ', ', semi_t[2], ") != 1 et R(", semi_t[2], ', ', semi_t[3], ") != 1",
              sep='')

    if neg_t == True:
        print("La relation est négativement transitive")
    else:
        print("La relation n'est pas négativement-transitive: R(", neg_t[0], ', ', neg_t[1], ") = 0  et R(", neg_t[1],
              ', ', neg_t[2], ") = 0, pourtant R(", neg_t[1],
              ', ', neg_t[2], ") != 0", sep='')

    if fer == True:
        print("La relation est ferrer")
    else:
        print("La relation n'est pas ferrer: R(", fer[0], ', ', fer[1], ") = 1  et R(", fer[1], ', ', fer[2],
              ") = 1, pourtant R(",
              fer[0], ', ', fer[2], ") == 0 ou R(", fer[2], ', ', fer[3], ") == 0", sep='')

    if comp == True:
        print("La relation est complète")
    else:
        print("La relation n'est pas complète: R(", comp[0], ', ', comp[1], ") = 0 et R(", comp[1], ', ', comp[0],
              ") = 0", sep='')

    print("\n\nOrdres :")

    if ot:
        print("La relation est un ordre total")
    else:
        print("La relation n'est pas un ordre total")

    if op:
        print("La relation est un ordre partiel")
    else:
        print("La relation n'est pas un ordre partiel")

    if pp:
        print("La relation est un préordre partiel")
    else:
        print("La relation n'est pas un préordre partiel")

    if pt:
        print("La relation est un préordre total")
    else:
        print("La relation n'est pas un préordre total")

    if so:
        print("La relation est un semi-ordre")
    else:
        print("La relation n'est pas un semi-ordre")

    if oi:
        print("La relation est un ordre d'intervalle")
    else:
        print("La relation n'est pas un ordre d'intervalle")

    # transforme_ordre_total([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


# GERER LES AFFICHAGES
def main():
    # nom_fichier = input("entrez le nom du fichier (extension comprise) où se trouve la relation: ")
    nom_fichier = 'transitive.txt'

    relation = lecture_fichier(nom_fichier)

    affiche_prop(relation)


main()
