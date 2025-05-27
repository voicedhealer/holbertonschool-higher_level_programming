#!/usr/bin/python3
"""
Ce module définit la fonction is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):

    """
    Retourne True si l'objet est une instance de la classe spécifiée,
    ou une instance d'une classe qui a hérité de la classe spécifiée,
    sinon False.
    """
    return isinstance(obj, a_class)
