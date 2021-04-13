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
                    if relation[x][y] == 1 and relation[y][z] and (relation[x][z] != 1 and relation[z][w] != 1):
                        return x, y, z, w
    return True


def negtransitive(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                if relation[x][y] == 0 and relation[y][z] == 0 and relation[x][z] == 1:
                    return x, y, z
    return True


def ferrer(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            for z in range(len(relation)):
                for w in range(len(relation)):
                    if relation[x][y] == 1 and relation[y][z] == 1 and (relation[x][w] == 0 and relation[w][z] == 0):
                        return x, y, z, w
    return True


def complete(relation):
    for x in range(len(relation)):
        for y in range(len(relation)):
            # au moins l'un des deux doit etre 1 pour que ce soit complet
            if relation[x][y] != 0 and relation[y][x] != 0:
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



def main():
    # nom_fichier = input("entrez le nom du fichier (extention comprise) où se trouve la relation: ")
    nom_fichier = 'antisym_comp.txt'
    r = lecture_fichier(nom_fichier)
    print(r)
    print("comp:", complete(r))
    print("sym:", symetrie(r))
    print("asym:", asymetrique(r))
    print("trans:", transitive(r))
    print("negtran", negtransitive(r))


main()
