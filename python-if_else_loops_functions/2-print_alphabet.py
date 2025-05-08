#!/usr/bin/python3

# Boucle pour itérer sur les codes ASCII des lettres minuscules de 'a' à 'z'.
# Les codes ASCII pour 'a' à 'z' vont de 97 à 122 inclusivement.
# range(97, 123) génère les nombres de 97 jusqu'à 122 (123 étant exclu).
for i in range(97, 123):  # Renommer 'alpha' en 'i' est une convention courante
                          # pour un simple compteur d'itération si 'alpha'
                          # n'est pas utilisé de manière plus sémantique ailleurs.
                          # Garder 'alpha' est aussi acceptable.

    # Convertit le code ASCII (entier) en son caractère correspondant.
    # Par exemple, chr(97) donne 'a'.
    # La méthode .format() est utilisée ici, bien qu'une f-string (Python 3.6+)
    # ou une simple conversion en chaîne serait aussi possible :
    # print(f"{chr(i)}", end="") ou print(chr(i), end="")
    # L'utilisation de "{}" avec .format() est simple et claire.
    print("{}".format(chr(i)), end="")

# Assurez-vous que cette ligne est la dernière ligne du fichier
# et qu'elle est suivie d'un seul caractère de nouvelle ligne (saut de ligne).
# Pour cela, après cette ligne de commentaire (ou la dernière ligne de code),
# appuyez une fois sur "Entrée" dans votre éditeur.
# Ceci évite l'erreur W292 "no newline at end of file".
# Aussi, vérifiez qu'il n'y a pas d'espaces en fin de ligne (W291)
# ni sur les lignes vides (W293).
