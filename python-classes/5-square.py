#!/usr/bin/python3
"""
Ce module définit une classe Square.
La classe Square définit un carré par sa taille,
avec accès et modification contrôlés via des propriétés.
"""


class Square:
    """
    Représente un carré.

    Attributs privés:
        __size (int): La taille du côté du carré.
    """

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de Square.
        La validation de la taille se fait via le setter.

        Args:
            size (int, optional): La taille du côté du carré. Défaut à 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter pour l'attribut size.
        Retourne la valeur actuelle de la taille.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut size.
        Valide que la valeur est un entier et >= 0 avant de l'assigner.

        Args:
            value (int): La nouvelle valeur pour la taille.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est un entier mais inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        # Si tout est OK, on assigne à l'attribut privé
        self.__size = value

    def area(self):
        """
        Calcule et retourne l'aire actuelle du carré.

        Returns:
            int: L'aire du carré (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime le carré avec des caractères '#' sur stdout
        Si la taille est 0, imprime une ligne vide
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
