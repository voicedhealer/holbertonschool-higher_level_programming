#!/usr/bin/python3
"""
Ce module définit une classe Square.
La classe Square définit un carré par sa taille.
"""


class Square:
    """
    Représente un carré

    Attributs privés:
    __size (int): La taille du cotédu carré
    """

    def __init__(self, size=0):
        """
        Initialise ube nouvelle intance de Square
        Args:
        size (int): La taille du coté du carré
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
