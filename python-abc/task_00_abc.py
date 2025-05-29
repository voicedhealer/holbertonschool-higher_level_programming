#!/usr/bin/python3
"""
Module illustrant les classes de base abstraites avec Animal, Dog et Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe de base abstraite représentant un animal.
    Définit une méthode abstraite 'sound' que les
    sous-classes doivent implémenter.
    """
    @abstractmethod
    def sound(self):
        """
        Méthode abstraite que les sous-classes doivent implémenter
        pour retourner le son de l'animal.
        """
        pass


class Dog(Animal):
    """
    Représente un chien, une sous-classe d'Animal.
    """
    def sound(self):
        """
        Retourne le son caractéristique du chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Représente un chat, une sous-classe d'Animal.
    """
    def sound(self):
        """
        Retourne le son caractéristique du chat.
        """
        return "Meow"
