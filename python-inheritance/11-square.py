#!/usr/bin/python3
"""
Ce module définit la classe Square qui hérite de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Représente un carré.
    Hérite de Rectangle et est initialisé avec une taille unique.
    """
    def __init__(self, size):
        """
        Initialise un nouveau Carré.

        Args:
            size (int): La taille du côté du carré.
            Doit être un entier positif.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est <= 0.
        """

        self.integer_validator("size", size)

        # Appelle le constructeur de la classe parente (Rectangle)
        super().__init__(size, size)

        # Stocke la taille dans un attribut privé avec __
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Retourne la représentation en chaîne de caractères du Square.

        Returns:
            str: La description formatée du carré avec f
        """
        return f"[Square] {self.__size}/{self.__size}"
