# ============================================================
# Exercice 1 : Contient-il des doublons ?
# ============================================================

def contient_doublon(t):
    # un set enlève les doublons automatiquement
    # si la taille change, c'est qu'il y en avait
    return len(t) != len(set(t))

print("=== Doublons ===")
print(contient_doublon([1, 2, 3, 1]))  # True
print(contient_doublon([1, 2, 3, 4]))  # False


# ============================================================
# Exercice 2 : Des anagrammes ?
# ============================================================

def est_anagramme(s, t):
    # on trie les lettres des deux mots et on compare
    return sorted(s.lower()) == sorted(t.lower())

print("\n=== Anagrammes ===")
print(est_anagramme("python", "onhtyp"))  # True
print(est_anagramme("tp", "tps"))         # False