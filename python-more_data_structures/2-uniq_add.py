#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Utilise un set pour obtenir les éléments uniques de la liste
    unique_elements = set(my_list)

    # Calcule la somme des éléments uniques
    total = 0
    for num in unique_elements:
        total += num

    # Retourne le résultat
    return total
