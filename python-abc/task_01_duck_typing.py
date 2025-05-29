#!/usr/bin/python3
"""
Module illustrant les classes de base abstraites
avec Shape, area, perimeter et la fonction shape_info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe de base abstraite pour les formes géométriques.
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
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape_object):
    """
    Affiche l'aire et le périmètre d'un objet forme donné.
    L'objet doit avoir des méthodes area() et perimeter().
    """
    resultat_de_area = shape_object.area()
    resultat_de_perimeter = shape_object.perimeter()
    print(f"Area: {resultat_de_area}")
    print(f"Perimeter: {resultat_de_perimeter}")
