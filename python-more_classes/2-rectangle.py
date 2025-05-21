#!/usr/bin/python3
"""
Module pour la construction de la class rectangle
"""


class Rectangle:
    """
    definit un rectangle avec width et height
    """

    def __init__(self, width=0, height=0):
        """
        initialise widht and height
        les setters sont appelés
        args : widht et height à 0 par default
        """

        self.width = width
        self.height = height
    def area(self):
        """
        
        """
        rectangle_aera =  self.width * self.height
        return rectangle_aera
    
    def perimeter(self):
        """
        
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
