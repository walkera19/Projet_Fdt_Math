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



