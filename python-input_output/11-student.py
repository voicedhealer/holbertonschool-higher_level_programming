#!/usr/bin/python3
"""
module etudiant
"""


class Student:
    """
classe étudiant
    """
    def __init__(self, first_name, last_name, age):
        """
        initialisation de irst name , last name et age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        conversion en format json
        """
        if (
                isinstance(attrs, list)
                and all(isinstance(item, str) for item in attrs)
        ):
            return {
                k: self.__dict__[k]
                for k in attrs if k in self.__dict__
                    }
        return self.__dict__

    def reload_from_json(self, json):
        """
        remplace tous les attributs de l'instance
        Student par ceux du dictionnaire json
        """
        for key, value in json.items():
            setattr(self, key, value)
