#!/usr/bin/python3
"""
fonction read file
"""


def read_file(filename=""):
    """
    definition de le fonction read file
    """
    with open('filename', 'r', encoding="utf8") as f:
        contenu = f.read()
        print(contenu, end="")
