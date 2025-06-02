#!/usr/bin/python3
"""
Ce module contient une fonction pour ajouter une chaîne de caractères
à la fin d'un fichier.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF-8)
    et retourne le nombre de caractères ajoutés.
    Si le fichier n'existe pas, il est créé.

    Args:
        filename (str): Le nom du fichier auquel ajouter le texte.
        text (str): La chaîne de caractères à ajouter au fichier.

    Returns:
        int: Le nombre de caractères ajoutés.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        nb_characters_added = f.write(text)
        return nb_characters_added
