#!/usr/bin/python3
"""
Fonction qui retourne la description d'un objet pour la sérialisation JSON.
"""


def class_to_json(obj):
    """
    Retourne le dictionnaire des attributs de l'objet.
    """
    return obj.__dict__
