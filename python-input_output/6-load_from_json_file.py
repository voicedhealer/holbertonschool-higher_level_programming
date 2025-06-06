#!/usr/bin/python3
"""
Module qui permet de créer un objet Python
à partir d’un fichier contenant du JSON.

Ce module fournit la fonction load_from_json_file qui lit un fichier texte,
interprète son contenu JSON et retourne l’objet Python correspondant.
"""
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
