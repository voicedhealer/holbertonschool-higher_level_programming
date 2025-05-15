#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed_count = 0

    # Boucler 'x' fois au maximum
    for i in range(x):
        try:
            # Essayer d'accéder à l'élément et de l'afficher
            element_to_print = my_list[i]
            print(element_to_print, end="")
            elements_printed_count += 1
        except IndexError:
            # Si on essaie d'accéder à un indice 
            # qui n'existe pas dans my_list,
            # une IndexError est levée. On l'attrape ici.
            # Cela signifie qu'on a atteint la fin de la liste
            # (ou que x est trop grand).
            # On doit donc arrêter d'essayer d'afficher.
            break  # Sortir de la boucle for

    # Après la boucle (soit parce qu'on a affiché 'x'
    # éléments, soit parce qu'on a 'break' à cause d'une IndexError),
    # afficher un retour à la ligne final.
    print() # Un print vide fait un retour à la ligne

    # Retourner le nombre d'éléments qui 
    # ont été effectivement affichés.
    return elements_printed_count
