#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """
    Crée un objet Python à partir d’un fichier contenant du JSON.

    Args:
        filename (str): Le chemin du fichier JSON à lire.

    Returns:
        L’objet Python désérialisé depuis le fichier.
    """
    with open(filename, 'r') as f:
        return json.load(f)
