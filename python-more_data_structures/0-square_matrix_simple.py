#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # 1. Initialiser la nouvelle matrice
    new_matrix = []

    # 2. Parcourir chaque 'row' dans la 'matrix' d'entrée
    for original_row in matrix:
        # 3. Pour chaque 'original_row', créer une nouvelle liste vide.
        #    Cette liste ('squared_elements_in_row')
        # contiendra les carrés des éléments de 'original_row'.
        squared_elements_in_row = []

        # 4. Parcourir chaque 'number' (entier) dans 'original_row'
        for number in original_row:
            # 5. Calculer le carré du 'number' actuel
            squared_number = number ** 2
            # 6. Ajouter ce 'squared_number' à la liste des éléments
            #  de la ligne en cours de construction
            squared_elements_in_row.append(squared_number)

        # 7. Une fois que tous les nombres de 'original_row' ont été traités et
        #    leurs carrés ajoutés à 'squared_elements_in_row',
        #    cette 'squared_elements_in_row' est complète.
        #    Ajouter cette ligne complète à notre 'new_matrix'.
        new_matrix.append(squared_elements_in_row)

    # 8. Une fois que toutes les lignes de
    #    la 'matrix' d'origine ont été traitées,
    #    'new_matrix' contient toutes les nouvelles lignes avec les carrés.
    #    Retourner 'new_matrix'.
    return new_matrix
