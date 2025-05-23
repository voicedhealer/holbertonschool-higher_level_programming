#!/usr/bin/python3
"""
Module pour la construction de la class rectangle
"""


class Rectangle:
    """
    definit un rectangle avec width et height
    """
    number_of_instances = 0
    print_symbol = '#'

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
                current_line = str(self.print_symbol) * self.width
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Méthod static, retourne le plus grand rectangle basé sur l'aire
        retourne rect-1 si les aires sont égales
        Raises:
        TypeError: Si rect_1 ou rect_2 n'est pas une instance de Rectangle.
        Returns:
        Rectangle: Le rectangle avec la plus grande aire,
        ou rect_1 si aires égales.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        aire_rect_1 = rect_1.area()
        aire_rect_2 = rect_2.area()
        if aire_rect_1 >= aire_rect_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Crée et retourne une nouvelle instance de Rectangle
        width et height sont égaux à size faisant un carré

        Returns:
            Rectangle: Une nouvelle instance de Rectangle
            avec width = size et height = size.
        """
        return cls(size, size)
