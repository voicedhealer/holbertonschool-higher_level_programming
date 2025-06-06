#!/usr/bin/python3
"""
Ce script ajoute tous les arguments de la ligne de commande à une liste Python,
puis sauvegarde cette liste dans un fichier JSON nommé 'add_item.json'.

- Si le fichier existe, il charge la liste existante avec load_from_json_file.
- Si le fichier n'existe pas, il commence avec une liste vide.
- Les nouveaux arguments sont ajoutés à la liste.
- La liste finale est sauvegardée avec save_to_json_file.

Fonctions utilisées :
- save_to_json_file (importée de save_to_json_file.py)
- load_from_json_file (importée de load_from_json_file.py)
"""
import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
"""
import module
"""

filename = "add_item.json"
"""
utilisation de if et else
"""

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
