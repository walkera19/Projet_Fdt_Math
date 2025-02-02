def degres_sommets(relation):
    n = len(relation)
    deg_plus = [0] * n
    deg_moins = [0] * n
    for i in range(n):
        for j in range(n):
            deg_plus[i] += relation[i][j]
            deg_moins[j] -= relation[i][j]
    deg = [sum(x) for x in zip(deg_plus, deg_moins)]
    deg_moins = list(map(lambda x: -x, deg_moins))
    return deg, deg_plus, deg_moins


# associe un indice à chaque élément de la liste puis la tri
def tri_tuples(relation):
    n = len(relation)
    liste_moins = []
    liste_plus = []
    # calcul du nombre de precedents pour chaque sommet
    deg_moins = list(map(lambda x: n - x, degres_sommets(relation)[2]))
    # calcul du nombre de suivants pour chaque sommet
    deg_plus = list(map(lambda x: x - 1, degres_sommets(relation)[1]))
    # on associe l'indice du sommet pour ne pas perdre la correspondance lors du tri
    for i in range(n):
        liste_moins.append((i, deg_moins[i]))
        liste_plus.append((i, deg_plus[i]))
    # on tri par nombre de suivants / precedants
    liste_moins.sort(key = lambda tup: tup[1])
    liste_plus.sort(key = lambda tup: tup[1])
    return liste_moins, liste_plus


# Renvoie la début et la fin de chaque intervalle pour les élements de la relation
# Le début est 0 si on n'a pas de precedant
# sinon c'est le plus grand début des precedants + 1
# La fin est le plus grand début si on n'a pas de suivant
# sinon c'est le plus grand fin des suivants - 1
def representation_graphique(relation, liste_moins, liste_plus):
    n = len(relation)
    debut = [-1]*n
    # on prend les elements dans l'ordre des degres
    for i,_ in liste_moins:
        # si on n'a pas de precedent on prend 0
        precedent_max = 0
        for j in range(n):
            # si on a un precedent, on prend de début du plus grand + 1
            if i != j and relation[i][j] == 1 and relation[j][i] == 0:
                precedent_max = max(precedent_max, debut[j] + 1)
        debut[i] = precedent_max

    fin = [max(debut) + 1]*n
    for i,_ in liste_plus:
        suivant_max = max(debut) + 1
        for j in range(n):
            if i != j and relation[i][j] == 0 and relation[j][i] == 1:
                suivant_max = min(suivant_max, debut[j])
        fin[i] = suivant_max

    return debut, fin


def affichage_intervalles(debut, fin):
    ascii_a = ord('a')
    for i in range(len(debut)):
        print(chr(ascii_a + i), ': [', debut[i] + 0.1, ', ', fin[i] - 0.1, ']', sep='')
        # print(chr(ascii_a + i), ': [', debut[i], ', ', fin[i], ']', sep='')
