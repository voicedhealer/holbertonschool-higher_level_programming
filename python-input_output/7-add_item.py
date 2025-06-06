#!/usr/bin/python3
"""
Script qui ajoute tous les arguments de la ligne de commande à une liste Python
et les sauvegarde dans un fichier JSON ('add_item.json').

- Utilise save_to_json_file pour la sérialisation.
- Utilise load_from_json_file pour la désérialisation.
- Crée le fichier s'il n'existe pas.
"""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
