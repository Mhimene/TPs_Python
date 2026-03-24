def somme_nulle_trois(tab):
    tab.sort()  # tri du tableau
    n = len(tab)
    resultats = []

    for i in range(n):
        gauche = i + 1
        droite = n - 1

        while gauche < droite:
            somme = tab[i] + tab[gauche] + tab[droite]

            if somme == 0:
                resultats.append((tab[i], tab[gauche], tab[droite]))
                gauche += 1
                droite -= 1

            elif somme < 0:
                gauche += 1

            else:
                droite -= 1

    return resultats


# Exemple
tab = [1, 20, 15, 3, 5, -4, 41]
print(somme_nulle_trois(tab))