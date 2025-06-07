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

    def to_json(self):
        """
        conversion en format json
        """
        return self.__dict__
