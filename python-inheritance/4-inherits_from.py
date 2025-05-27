#!/usr/bin/python3
def inherits_from(obj, a_class):

    """
    Ce module définit la fonction inherits_from.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
