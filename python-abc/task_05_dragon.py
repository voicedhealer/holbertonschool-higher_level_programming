#!/usr/bin/python3
"""
Module démontrant l'utilisation des classes Mixin en Python.

Les Mixins sont des classes qui fournissent des fonctionnalités spécifiques
pour être héritées par d'autres classes, sans être elles-mêmes des classes
parentes "complètes" ou destinées à être instanciées seules.
Ce module définit `SwimMixin` et `FlyMixin`, puis une classe `Dragon`
qui utilise ces mixins pour acquérir des capacités de nage et de vol.
"""


class SwimMixin:
    """
    Un Mixin qui fournit la capacité de nager.

    Cette classe est destinée à être héritée par d'autres classes pour leur
    ajouter une méthode `swim()`, sans affecter leur hiérarchie principale.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Un Mixin qui fournit la capacité de voler.

    Cette classe est destinée à être héritée par d'autres classes pour leur
    ajouter une méthode `fly()`, sans affecter leur hiérarchie principale.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Représente un dragon qui peut nager, voler et rugir.

    Cette classe hérite de `SwimMixin` et `FlyMixin` pour acquérir
    les méthodes `swim()` et `fly()`. Elle définit également sa propre
    méthode `roar()`. Cela illustre comment les mixins peuvent être utilisés
    pour composer des fonctionnalités.
    """
    def roar(self):
        print("The dragon roars!")
