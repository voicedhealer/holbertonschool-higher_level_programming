#!/usr/bin/python3
# Ce script additionne tous les arguments passés en ligne de commande.

# Importer le module nécessaire pour les arguments.
import sys

if __name__ == "__main__":
    total_sum = 0
    # sys.argv[0] est le nom du script.
    # sys.argv[1:] contient tous les arguments suivants.
    # La boucle for itère directement sur ces arguments.
    for arg_str in sys.argv[1:]:
        total_sum += int(arg_str)

    print(total_sum)
