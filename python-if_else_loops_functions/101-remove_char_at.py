#!/usr/bin/python3
"""
Ce module contient une fonction pour supprimer un caractère d'une chaîne.
"""
# (Deux lignes vides ici si le docstring de module est présent)

def remove_char_at(str_input, n):
    """Crée une copie de str_input sans le caractère à l'index n.

    Args:
        str_input (str): La chaîne d'entrée.
        n (int): L'index du caractère à supprimer.

    Returns:
        str: La nouvelle chaîne avec le caractère supprimé, ou la
             chaîne originale si n est hors limites.
    """
    # (Une ligne vide ici si le docstring de fonction est multi-lignes
    #  et avant le code de la fonction, mais ce n'est pas une règle E302)
    if n < 0 or n >= len(str_input):
        return str_input  # Exemple de commentaire en ligne bien espacé

    new_string = ""
    # ... (reste de votre code) ...
    return new_string
