#!/usr/bin/python3
"""
Ce module contient une fonction pour écrire une
chaîne de caractères dans un fichier.
"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF-8)
    et retourne le nombre de caractères écrits.

    Args:
        filename (str): Le nom du fichier dans lequel écrire.
                        Le fichier sera créé s'il n'existe pas,
                        et son contenu sera écrasé s'il existe.
        text (str): La chaîne de caractères à écrire dans le fichier.

    Returns:
        int: Le nombre de caractères écrits.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        nb_characters_written = f.write(text)
        return nb_characters_written
