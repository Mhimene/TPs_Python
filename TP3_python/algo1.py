def somme_nulle_deux(tab):
    vus = set()
    resultats = []

    for x in tab:
        if -x in vus:
            resultats.append((x, -x))
        vus.add(x)

    return resultats


# Exemple
tab = [1, 20, 15, 3, 5, -20, 41]
print(somme_nulle_deux(tab))