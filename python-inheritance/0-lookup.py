#!/usr/bin/python3
"""
Fonction qui retourne une liste des attributs
et methode disponible par objet
"""


def lookup(obj):
    """
    Méthode qui retoourne une liste
    """
    return dir(obj)
