#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    cles_triees = sorted(a_dictionary)
    for cle in cles_triees:
        valeur = a_dictionary[cle]
        print("{}: {}".format(cle, valeur))
