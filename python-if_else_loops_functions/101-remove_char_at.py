#!/usr/bin/python3

def remove_char_at(str_input, n): # J'utilise str_input pour éviter de masquer la fonction intégrée str
    # Gérer les cas où n est hors limites (optionnel, mais bonne pratique)
    # Si n < 0 ou n >= longueur de str_input:
    #     retourner str_input (ou une copie)

    new_string = ""  # Initialiser une chaîne vide pour le résultat

    # Boucler sur les index de la chaîne d'entrée
    # pour chaque index 'i' de 0 à longueur_de_str_input - 1:
        # SI l'index actuel 'i' est DIFFERENT de 'n':
            # Ajouter le caractère str_input[i] à nouvelle_chaine
        # (SINON, si i == n, on ne fait rien, on saute ce caractère)

    return new_string
