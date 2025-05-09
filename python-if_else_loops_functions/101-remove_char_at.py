#!/usr/bin/python3
"""
Fonction qui crée une copie de la chaîne,
en supprimant le caractère à la position n.
"""


def remove_char_at(str_input, n): # Si le proto impose 'str', utilisez 'str'
    """Crée une copie de str_input sans le caractère à l'index n."""
    if n < 0 or n >= len(str_input):
        return str_input  # Retourne la chaîne originale si n est invalide

    new_string = ""
    for i in range(len(str_input)):
        if i != n:  # Si l'index actuel n'est pas celui à supprimer
            new_string = new_string + str_input[i]  # Ajouter le caractère
    return new_string
