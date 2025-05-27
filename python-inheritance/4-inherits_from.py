#!/usr/bin/python3
"""
Module pour la fonction inherits_from.
Vérifie l'héritage strict d'une classe.
"""

def inherits_from(obj, a_class):
    """
    Retourne True si obj est une instance d'une classe héritant de a_class
    (directement ou indirectement), mais pas de a_class elle-même.

    Args:
        obj (any): L'objet à vérifier.
        a_class (type): La classe de référence.

    Returns:
        bool: True si la condition d'héritage strict est remplie, sinon False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
