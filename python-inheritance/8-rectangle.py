#!/usr/bin/python3
"""
Ce module définit une classe Rectangle.
"""


def __init__(self, width, height):
    """
    Initialise un rectangle avec une largeur et une hauteur.

    Args:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.

    Raises:
        TypeError: Si 'width' ou 'height' n'est pas un entier.
        ValueError: Si 'width' ou 'height' est inférieur ou égal à 0.
    """
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height
