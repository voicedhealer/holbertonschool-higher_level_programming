#!/usr/bin/python3
"""
Module pour la construction de la class rectangle
"""


class Rectangle:
    """
    definit un rectangle avec width et height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        initialise widht and height
        les setters sont appelés
        args : widht et height à 0 par default
        ajout de count pour incrémenter de 1
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def area(self):
        """
        calcul de l'air aera
        """
        rectangle_aera = self.width * self.height
        return rectangle_aera

    def perimeter(self):
        """
        calcul du périmtre
        """
        if self.width == 0 or self.height == 0:
            return 0
        rectangle_perimeter = 2 * (self.width + self.height)
        return rectangle_perimeter

    @property
    def width(self):
        """
        int: définit la largeur du rectangle.
        Attention: la largeur doit être un entier positif ou nul.
        """
        return self.__width   # retourne l'attribut de stockage privé

    @property
    def height(self):
        """
        int: définit la hauteur du rectangle.
        De même la hauteur doit être un entier positif ou nul.
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        return une reprenésentation en chaine de caractères avec '#'
        ou vide si width ou height vaut 0
        """
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            repr_string = []
            for _ in range(self.height):
                current_line = "#" * self.width
                repr_string.append(current_line)
            return "\n".join(repr_string)

    def __repr__(self):
        """
        return une reprensentation en chaine de caractère du rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Méthode del pour la suppréssion d'une instance de la Classe Rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
