# fusion de deux tableaux triés
def fusion(nums1, nums2):
    resultat = []
    i = 0
    j = 0

    # comparer les éléments des deux tableaux
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            resultat.append(nums1[i])
            i += 1
        else:
            resultat.append(nums2[j])
            j += 1

    # ajouter les éléments restants
    resultat.extend(nums1[i:])
    resultat.extend(nums2[j:])

    return resultat


# test
nums1 = [1, 2, 3]
nums2 = [2, 5, 6]

print(fusion(nums1, nums2))