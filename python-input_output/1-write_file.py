#!/usr/bin/python3
"""
fonction read file
"""


def write_file(filename="", text=""):
    """
    definition de filename en écriture
    """

    with open(filename, 'w', encoding="utf8") as f:
        contenu = f.write
        print(contenu, end="")
