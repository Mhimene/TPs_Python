
# EXERCICE 1 : NOMBRE DE BITS À 1

def count_bits(n):
    count = 0
    while n > 0:
        count += n & 1   # récupère le dernier bit
        n = n >> 1       # décale à droite
    return count



# EXERCICE 2 : SWAP BITS

def swap_bits(n, i, j):
    # récupérer les bits i et j
    bit_i = (n >> i) & 1
    bit_j = (n >> j) & 1

    # si différents → on les swap
    if bit_i != bit_j:
        mask = (1 << i) | (1 << j)
        n = n ^ mask

    return n



# MAIN

if __name__ == "__main__":

    print("=== Exercice 1 : Nombre de bits à 1 ===")
    n1 = int(input("Entrer un nombre : "))
    print("Résultat :", count_bits(n1))

    print("\n=== Exercice 2 : Swap bits ===")
    n2 = int(input("Entrer un nombre : "))
    i = int(input("Index i : "))
    j = int(input("Index j : "))
    print("Résultat :", swap_bits(n2, i, j))