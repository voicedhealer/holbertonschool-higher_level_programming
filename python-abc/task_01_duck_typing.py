#!/usr/bin/python3
"""
Module illustrant les classes de base abstraites
avec Shape, area, perimeter
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    classe Shape
    """

    @abstractmethod
    def area(self):
        """
        area: methode pour le calcul de l'air
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter: calcul du périmetre
        """
        pass


class Circle(Shape):
    """
    Class cercle calcul de la surface d'un cercle avec pi
    """
    pass


class Rectangle(Shape):
    """
    Class Rectangle
    """
    pass
