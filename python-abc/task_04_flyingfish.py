#!/usr/bin/python3
"""
Module illustrant l'héritage multiple et l'ordre de résolution
des méthodes (MRO) en Python.

Ce module définit trois classes : `Fish`, `Bird`, et `FlyingFish`.
`FlyingFish` hérite à la fois de `Fish` et de `Bird`, démontrant
comment les méthodes sont résolues et peuvent être surchargées
dans un contexte d'héritage multiple.
"""


class Fish:
    """
    Représente un poisson avec des comportements aquatiques de base.
    Fournit des méthodes pour nager et décrire son habitat.
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Représente un oiseau avec des comportements aériens de base.
    Fournit des méthodes pour voler et décrire son habitat.
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Représente un poisson volant, un animal qui combine des caractéristiques
    des poissons et des oiseaux.

    Cette classe hérite de `Fish` et `Bird` et surcharge les méthodes
    `fly`, `swim`, et `habitat` pour refléter son comportement unique.
    L'ordre de résolution des méthodes (MRO) dictera quelle version
    d'une méthode est appelée si elle n'est pas surchargée ici.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
