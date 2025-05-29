#!/usr/bin/python3
"""
Module définissant un itérateur qui compte les éléments.
"""


class CountedIterator:
    """
    Un itérateur qui enveloppe un autre itérable et compte
    le nombre d'éléments récupérés.
    """

    def __init__(self, iterable_source):
        """
        Initialise l'itérateur avec l'itérable source et un compteur.
        """
        self.iterator = iter(iterable_source)
        self.count = 0

    def get_count(self):
        """
        Retourne le nombre actuel d'éléments qui ont été récupérés.
        """
        return self.count

    def __next__(self):
        """
        itère de + 1
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """
        Retourne l'itérateur lui-même
        """
        return self
