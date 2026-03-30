# Conversion chiffres romains --> entier


# Tableau de correspondance symbole --> valeur
valeurs = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# On demande un nombre romain à l'utilisateur
nombre_romain = input("Entrez un nombre romain : ").upper()

total = 0

for i in range(len(nombre_romain)):
    valeur_actuelle = valeurs[nombre_romain[i]]

    # Si le symbole suivant est plus grand, on soustrait (ex: IV = 5-1 = 4)
    if i + 1 < len(nombre_romain) and valeur_actuelle < valeurs[nombre_romain[i + 1]]:
        total -= valeur_actuelle
    else:
        total += valeur_actuelle

print("Résultat :", total)


# Partie BONUS : entier --> chiffres romains


# Table dans l'ordre décroissant (on inclut les cas spéciaux comme IV, IX...)
table = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
    (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
    (1, 'I')
]

nombre = int(input("\nEntrez un entier à convertir en romain : "))

resultat = ""

for valeur, symbole in table:
    # Tant que le nombre est >= à la valeur, on ajoute le symbole
    while nombre >= valeur:
        resultat += symbole
        nombre -= valeur

print("Résultat :", resultat)