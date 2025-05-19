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

    def __init__(self, size):
        """
        Initialise ube nouvelle intance de Square

        Args:
        size (int): La taille du coté du carré
        """
        self.__size = size
