#!/usr/bin/python3
"""
Ce module définit une classe de base pour la géométrie, BaseGeometry.
"""


class BaseGeometry:

    """
    Une classe de base pour représenter des formes géométriques.
    Contient une méthode 'area' et un validateur d'entiers.
    """
    def area(self):
        """
        Méthode non implémentée pour calculer l'aire.
        Doit être surchargée dans les classes dérivées.
        Raises:
            Exception: Indique que la méthode area() n'est pas implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide si 'value' est un entier et est strictement positif.

        Args:
            name (str): Le nom de la valeur (supposé être une chaîne).
            value (any): La valeur à valider.

        Raises:
            TypeError: Si 'value' n'est pas un entier.
                       Le message est "{name} must be an integer".
            ValueError: Si 'value' est un entier mais est inférieur
            ou égal à 0.
                        Le message est "{name} must be greater than 0".
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


