def remove_char_at(str_input, n): # Respectez le prototype si c'est `str`
    # Étape 1: Gérer les index n hors limites
    if n < 0 or n >= len(str_input):
        return str_input # Retourner la chaîne originale si n est invalide

    # Étape 2: Construire la nouvelle chaîne si n est valide
    new_string = ""
    for i in range(len(str_input)):
        if i != n: # Si l'index actuel n'est pas celui à supprimer
            new_string = new_string + str_input[i] # Ajouter le caractère

    return new_string
