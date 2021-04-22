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

def tri_topologique(relation):
    n = len(relation)
    liste_sommets = []
    # non traités à 0, traités à 1
    etats_sommets = [0]*n
    for i in range(n):
        if etats_sommets[i] == 0:
            parcours_profondeur_topo(relation, liste_sommets, etats_sommets, i)
    return liste_sommets


def parcours_profondeur_topo(relation, liste_sommets, etats_sommets, i):
    n = len(relation)
    for j in range(n):
        if i != j and relation[i][j] == 1 and relation[j][i] == 0 and etats_sommets[j] == 0:
            parcours_profondeur_topo(relation, liste_sommets, etats_sommets, j)
    etats_sommets[i] = 1
    liste_sommets.append(i)

