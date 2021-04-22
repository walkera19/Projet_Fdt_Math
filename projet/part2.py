def degres_sommets(relation):
    n = len(relation)
    deg_plus = [0]*n
    deg_moins = [0] * n
    for i in range(n):
        for j in range(n):
            deg_plus[i] += relation[i][j]
            deg_moins[j] -= relation[i][j]
    deg = [sum(x) for x in zip(deg_plus, deg_moins)]
    deg_moins = list(map(lambda x: -x, deg_moins))
    return deg, deg_plus, deg_moins


# associe un indice à chaque élément de la liste puis on la tri
# si i = 1 ca donne les degres plus, si i = 2 ca donne les degres moins
def tri_tuples(relation):
    n = len(relation)
    liste_moins = []
    liste_plus = []
    deg_moins = list(map(lambda x: n - x, degres_sommets(relation)[2]))
    deg_plus = list(map(lambda x: x - 1, degres_sommets(relation)[1]))
    for i in range(n):
        liste_moins.append((i, deg_moins[i]))
        liste_plus.append((i, deg_plus[i]))
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
    for i,_ in liste_moins:
        precedent_max = 0
        for j in range(n):
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

    debut =
    return debut, fin


###############


def parcours_profondeur_topo(relation, liste_sommets, etats_sommets, i):
    n = len(relation)
    for j in range(n):
        if i != j and relation[i][j] == 1 and relation[j][i] == 0 and etats_sommets[j] == 0:
            parcours_profondeur_topo(relation, liste_sommets, etats_sommets, j)
    etats_sommets[i] = 1
    liste_sommets.append(i)


def tri_topologique(relation):
    n = len(relation)
    liste_sommets = []
    # non traités à 0, traités à 1
    etats_sommets = [0]*n
    for i in range(n):
        if etats_sommets[i] == 0:
            parcours_profondeur_topo(relation, liste_sommets, etats_sommets, i)
    return liste_sommets

