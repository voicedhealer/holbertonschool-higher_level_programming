#!/usr/bin/python3
"""
Ce module définit une classe MyList qui hérite de list
"""
class Mylist(list):
    """
    Classe Mylist qui hérite de la calsse list
    """
    def print_sorted(self):
        """
        Méthode publique print_stored qui affiche
        les éléments de la liste
        """
        liste_triee_pour_impression = sorted(self)
        """
        print la list for impression
        """
        print(liste_triee_pour_impression)
