#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Boucle externe pour chaque ligne de la matrice
    for row in matrix:
        # Initialiser une liste pour stocker les versions 'chaîne' des nombres
        # de la ligne actuelle. Ceci doit être fait pour CHAQUE nouvelle ligne.
        numbers_string_for_this_row = []

        # Boucle interne pour chaque nombre dans la ligne actuelle
        # Cette boucle DOIT être indentée pour être à l'intérieur de la boucle "for row in matrix"
        for number_element in row:
            # Formater le nombre en chaîne
            numbers_format = "{:d}".format(number_element)
            # Ajouter le nombre formaté à notre liste temporaire
            numbers_string_for_this_row.append(numbers_format)

        # Joindre toutes les chaînes de nombres de la ligne avec un ESPACE
        # Cette opération DOIT être indentée pour être à l'intérieur de la boucle "for row in matrix"
        line_to_print = " ".join(numbers_string_for_this_row)

        # Afficher la ligne construite
        # Cette opération DOIT être indentée pour être à l'intérieur de la boucle "for row in matrix"
        print(line_to_print)
