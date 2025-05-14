#!/usr/bin/python3
def roman_to_int(roman_string):
    # Étape 1: Valider l'entrée
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    # Étape 2: Définir le dictionnaire des valeurs romaines
    # (si ce n'est pas déjà fait globalement)
    valeurs_romaines = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Étape 3: Initialiser le total et l'index
    total_entier = 0
    i = 0
    longueur_chaine = len(roman_string)

    # Étape 4: Boucle de conversion
    while i < longueur_chaine:
        val_actuelle = valeurs_romaines.get(roman_string[i], 0)

        # S'il y a un caractère suivant
        if i + 1 < longueur_chaine:
            val_suivante = valeurs_romaines.get(roman_string[i+1], 0)

            if val_actuelle < val_suivante:
                total_entier += (val_suivante - val_actuelle)
                i += 2
            else:
                total_entier += val_actuelle
                i += 1
        else:
            total_entier += val_actuelle
            i += 1

    # Étape 5: Retourner le total
    return total_entier
