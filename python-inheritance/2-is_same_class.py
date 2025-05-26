#!/usr/bin/python3
"""
la fonction retourne Vrai si elle exactememnt une instance de classe
"""


def is_same_class(obj, a_class):
    """
    Méthode is_same_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
