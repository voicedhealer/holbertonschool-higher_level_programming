#!/usr/bin/python3
def max_integer(my_list=[]):
    # Étape 1: Gérer le cas où la liste est vide
    if not my_list:  # ou if len(my_list) == 0:
        return None

    # Étape 2: Si la liste n'est pas vide, trouver le maximum
    # Initialiser 'plus_grand' avec le premier élément de la liste
    # (on sait maintenant que la liste a au moins un élément)
    plus_grand = my_list[0]

    # Parcourir la liste à partir du DEUXIÈME élément (si elle en a)
    # ou parcourir toute la liste et comparer. Parcourir toute la liste est plus simple.
    for nombre in my_list: # Renommer la variable de boucle
        if nombre > plus_grand:
            plus_grand = nombre

    # Étape 3: Retourner la plus grande valeur trouvée
    return plus_grand
