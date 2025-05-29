#!/usr/bin/python3
"""
Module illustrant les classes de base abstraites
avec Shape, area, perimeter
"""
from abc import ABC, abstractmethod
import math


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
