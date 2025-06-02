#!/usr/bin/python3
"""
Module fournissant une fonction pour convertir des objets Python
en leur représentation sous forme de chaîne de caractères JSON.
"""
import json


def to_json_string(my_obj):
    """
    Retourne la représentation JSON d'un objet Python (chaîne de caractères).

    Cette fonction prend un objet Python en entrée et utilise le module `json`
    pour le sérialiser en une chaîne de caractères respectant le format JSON.
    Les types d'objets qui ne sont pas nativement sérialisables par le module
    `json` (comme les sets, ou des classes personnalisées sans traitement
    spécifique) lèveront une exception `TypeError`, conformément aux
    instructions de l'exercice qui ne demandent pas de gérer ces cas.

    Args:
        my_obj: L'objet Python à convertir en chaîne JSON.
                Types courants incluent listes, dictionnaires, chaînes,
                nombres (int, float), booléens et None.

    Returns:
        str: La représentation de `my_obj` sous forme de chaîne JSON.
    """
    return json.dumps(my_obj)
