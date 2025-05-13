#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Étape 1: Vérifier si l'indice est négatif
    if idx < 0:
        return my_list

    # Étape 2: Obtenir la longueur de la liste
    longueur_liste = len(my_list) # Correction ici

    # Étape 3: Vérifier si l'indice est hors limites (trop grand OU si la liste est vide)
    # Cette condition gère aussi le cas où my_list est vide, car longueur_liste sera 0.
    # Si idx=0 (valeur par défaut) et longueur_liste=0, alors 0 >= 0 est vrai.
    if idx >= longueur_liste:
        return my_list

    # Étape 4: Si on arrive ici, l'indice est valide et la liste n'est pas vide à cet indice.
    # Supprimer l'élément.
    del my_list[idx] # Correction ici

    # Étape 5: Retourner la liste (qui a été modifiée si la suppression a eu lieu)
    return my_list
