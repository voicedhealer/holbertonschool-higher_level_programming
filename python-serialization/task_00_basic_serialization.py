#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise le dictionnaire Python 'data'
    et l'enregistre dans un fichier JSON 'filename'.
    Si le fichier existe déjà, il est remplacé.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge et désérialise les données JSON du fichier
    'filename' et retourne un dictionnaire Python.
    """
    with open(filename, 'r') as f:
        return json.load(f)
