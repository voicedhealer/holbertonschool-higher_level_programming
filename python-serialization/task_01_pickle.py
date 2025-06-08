#!/usr/bin/python3
"""
CustomObject class for pickling and unpickling.
"""
import pickle


class CustomObject:
    """
    Classe représentant un objet personnalisable avec sérialisation pickle.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet au format demandé.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance courante dans le fichier donné avec pickle.
        Retourne None en cas d'erreur.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise et retourne une instance
        de CustomObject depuis le fichier donné.
        Retourne None si le fichier n'existe pas ou est mal formé.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
