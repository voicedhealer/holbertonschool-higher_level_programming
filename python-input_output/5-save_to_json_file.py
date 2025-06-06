#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet Python dans un fichier texte en utilisant une représentation JSON.

    Args:
        my_obj: L'objet Python à sérialiser et enregistrer dans le fichier.
        filename (str): Le chemin du fichier dans lequel écrire l'objet JSON.

    Cette fonction utilise le module json pour convertir l'objet en chaîne JSON
    et l'enregistre dans le fichier spécifié. Les exceptions de sérialisation et 
    de permissions ne sont pas gérées explicitement.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
