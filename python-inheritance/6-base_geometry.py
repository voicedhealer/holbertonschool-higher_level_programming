#!/usr/bin/python3
"""
Ce module définit une classe de base pour la géométrie, BaseGeometry.
"""


class BaseGeometry:

    """
    Une classe de base pour représenter des formes géométriques.
    Contient une méthode 'area' qui doit être implémentée par les sous-classes.
    """
    def area(self):
        raise Exception("area() is not implemented")
