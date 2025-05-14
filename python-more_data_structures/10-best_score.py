#!/usr/bin/python3
def best_score(a_dictionary):
    # Gérer le cas du dictionnaire vide
    if not a_dictionary:
        return None

    # Initialiser les variables
    best_key = None
    max_score = None

    # Parcourir chaque paire (clé, valeur) dans le dictionnaire
    for key, score_value in a_dictionary.items():
        # Comparer et mettre à jour si un meilleur score est trouvé
        if max_score is None or score_value > max_score:
            max_score = score_value
            best_key = key

    # Une fois la boucle terminée
    # (tous les éléments ont été vérifiés),
    # retourner la clé du meilleur score trouvé.
    return best_key
