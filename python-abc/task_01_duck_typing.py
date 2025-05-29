#!/usr/bin/python3
"""
Module illustrant les classes de base abstraites
avec Shape, area, perimeter
"""
from abc import ABC, abstractmethod
import math


def shape_info(shape_object):
    """
    fonction shape info
    L'objet doit avoir des méthodes area() et perimeter()
    """

    resultat_de_aera = shape_object.aera()
    resultat_de_peremeter = shape_object.perimeter()
    print(f"Area: {resultat_de_area}")
    print(f"Perimeter: {resultat_de_perimeter}")


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
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and Height cannot be negative")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    if __name__ == "__main__":
        # Par exemple, avec un rayon de 5
        mon_cercle = Circle(radius=5)

        # Crée une instance de Rectangle
        mon_rectangle = Rectangle(width=4, height=7)

        # Teste shape_info avec le cercle
        print("Info pour le cercle :")
        shape_info(mon_cercle)

        # Teste shape_info avec le rectangle
        print("\nInfo pour le rectangle :")
        shape_info(mon_rectangle)
