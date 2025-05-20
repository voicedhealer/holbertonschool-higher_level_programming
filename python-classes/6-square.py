#!/usr/bin/python3
"""
Ce module définit une classe Square.

La classe Square permet de créer des objets carrés avec une taille
et une position spécifiques, et inclut des méthodes pour calculer l'aire
et afficher le carré.
"""


class Square:
    """
    Représente un carré géométrique.

    Cette classe permet de définir un carré par sa taille et sa position
    dans un plan 2D. Elle fournit des méthodes pour calculer son aire
    et pour l'afficher en utilisant des caractères '#'.

    Attributes:
        size (int): La longueur du côté du carré.
        position (tuple): Un tuple de deux entiers positifs indiquant
                          les coordonnées (x, y) du coin supérieur gauche
                          du carré pour l'affichage.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int, optional): La taille du côté du carré.
                                  Doit être un entier positif ou nul.
                                  Par défaut à 0.
            position (tuple, optional): Un tuple de deux entiers positifs (x, y)
                                        indiquant le décalage pour l'impression.
                                        Par défaut à (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        int: Obtient ou définit la taille du côté du carré.

        La taille doit être un entier supérieur ou égal à 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré avec validation.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        tuple: Obtient ou définit la position du carré.

        La position est un tuple de deux entiers positifs (x, y)
        indiquant le décalage pour l'impression du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré avec validation.

        Args:
            value (tuple): Le nouveau tuple de position (x, y).

        Raises:
            TypeError: Si `value` n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule et renvoie l'aire du carré.

        Returns:
            int: L'aire du carré (taille * taille).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime le carré à la console avec le caractère '#'.

        Prend en compte la position pour décaler l'affichage du carré.
        Si la taille est 0, imprime une ligne vide.
        L'impression est décalée verticalement par `position[1]` lignes vides
        et horizontalement par `position[0]` espaces.
        """
        if self.__size == 0:
            print()
            return

        # Ajoute les sauts de ligne verticaux avant d'imprimer le carré
        print("\n" * self.__position[1], end="")
        # Imprime chaque ligne du carré
        for _ in range(self.__size):
            # Ajoute les espaces horizontaux et les '#'
            print(" " * self.__position[0] + "#" * self.__size)

