#!/usr/bin/python3
"""
Module fournissant une fonction pour convertir une chaîne de caractères
représentant un objet JSON en un objet Python.

Ce module contient une unique fonction, `from_json_string`, qui utilise
le module `json` de Python pour la désérialisation.
"""
import json


def from_json_string(my_str):
    """
    Retourne un objet Python (structure de données) à partir de sa
    représentation sous forme de chaîne JSON.

    Cette fonction prend une chaîne de caractères qui est supposée être
    au format JSON valide et la convertit en l'objet Python correspondant
    (par exemple, un dictionnaire, une liste, une chaîne, un nombre,
    un booléen, ou None). Si la chaîne n'est pas un JSON valide,
    la fonction `json.loads()` lèvera une exception (typiquement
    `json.JSONDecodeError`).

    Args:
        my_str (str): Une chaîne de caractères contenant la représentation
                      JSON d'un objet.

    Returns:
        any: L'objet Python correspondant à la chaîne JSON fournie.
             Le type exact de l'objet retourné dépendra de la structure
             de la chaîne JSON d'entrée.
    """
    return json.loads(my_str)
