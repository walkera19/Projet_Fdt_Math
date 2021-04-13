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
    relation.remove([])

    # verification de la taille de la matrice:
    n = len(relation)
    for i in range(n):
        if len(relation[i]) != n:
            return 'La matrice n\'est pas carrée'

    return relation


def symetrie(relation):
    for i in range(len(relation)):
        for j in range(len(relation)):
            if relation[i][j] != relation[j][i]:
                return False
    return True


def asymetrique(relation):
    for i in range(len(relation)):
        # 0 sur la diagonale
        if relation[i][i] != 0: return False
        for j in range(len(relation)):
            # aij = 1 => aji = 0
            if relation[i][j] == 1 and relation[j][i] == 1:
                return False
    return True


def transitive(relation):
    for i in range(len(relation)):
        for j in range(len(relation)):
            for k in range(len(relation)):
                if relation[i][j] == 1 and relation[j][k] == 1 and relation[i][k] == 0:
                    return False
    return True


def negtransitive(relation):
    for i in range(len(relation)):
        for j in range(len(relation)):
            for k in range(len(relation)):
                if relation[i][j] == 0 and relation[j][k] == 0 and relation[i][k] == 1:
                    return False
    return True


def complete(relation):
    for i in range(len(relation)):
        for j in range(len(relation)):
            # au moins l'un des deux doit etre 1 pour que ce soit complet
            if relation[i][j] != 0 and relation[j][i] != 0:
                return False
    return True


def main():
    # nom_fichier = input("entrez le nom du fichier (extention comprise) où se trouve la relation: ")
    nom_fichier = 'exemple.txt'
    r = lecture_fichier(nom_fichier)


main()
