#!/usr/bin/python3
"""
Convertit un fichier CSV en fichier JSON (data.json).
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Lit le fichier CSV 'filename', convertit
    les données en JSON et les écrit dans 'data.json'.
    Retourne True si la conversion réussit,
    False sinon (ex: fichier non trouvé).
    """
    try:
        with open(filename, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
