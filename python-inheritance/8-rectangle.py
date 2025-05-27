#!/usr/bin/python3
"""
Ce module définit une classe Rectangle qui hérite de BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Représente un rectangle.

    Hérite de BaseGeometry et utilise integer_validator pour
    valider la largeur et la hauteur.
    """
    def __init__(self, width, height):
        """
        Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle. Doit être un entier positif.
            height (int): La hauteur du rectangle. Doit être un entier positif.

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est <= 0.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
