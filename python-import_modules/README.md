# Python - Import & Modules

![Image Représentant Python Imports et Modules](URL_DE_VOTRE_IMAGE_ICI)
*Remplacez `URL_DE_VOTRE_IMAGE_ICI` par le lien direct vers une image pertinente (par exemple, un diagramme illustrant l'importation, le logo Python, ou un extrait de code illustratif).*

## Description du Projet

Ce projet, inscrit dans le cursus "Programmation de Plus Haut Niveau" de Holberton School, explore les mécanismes d'importation de modules et de fonctions en Python. L'objectif est de comprendre comment structurer son code en plusieurs fichiers pour une meilleure organisation, réutilisabilité et maintenabilité. Nous apprendrons à créer nos propres modules, à importer des fonctions spécifiques, des modules entiers, et à utiliser des alias pour simplifier leur usage. Ce projet abordera également l'utilisation de la fonction intégrée `dir()` et le concept de garde d'exécution avec `if __name__ == "__main__":`.

## Objectifs d'Apprentissage

À la fin de ce projet, vous devriez être capable de :

*   Comprendre pourquoi Python est considéré comme un langage de programmation interprété.
*   Expliquer comment utiliser l'interpréteur Python.
*   Comprendre ce qu'est un module en Python et comment il favorise la modularité.
*   Savoir comment créer un module Python.
*   Maîtriser les différentes manières d'importer des fonctions depuis un autre fichier :
    *   Importer des fonctions spécifiques (`from nom_module import fonction`).
    *   Importer un module entier (`import nom_module`).
    *   Utiliser des alias pour les modules importés (`import nom_module as alias`).
*   Comprendre et utiliser la fonction intégrée `dir()` pour inspecter les objets et les modules.
*   Comprendre comment empêcher l'exécution de code lors de l'importation d'un module en utilisant la construction `if __name__ == "__main__":`.
*   Savoir comment utiliser les arguments de la ligne de commande avec Python en utilisant le module `sys`.

## Fichiers dans ce Dossier

Ce projet comprendra une série de fichiers `.py` illustrant les concepts d'importation et de modularité. Voici une liste indicative des types de tâches :

*   **`0-add.py`**:
    *   `add_0.py` (ou un nom similaire) : Fichier contenant une fonction `add(a, b)` qui retourne la somme de deux entiers.
    *   `0-add.py` : Script principal qui importe la fonction `add` depuis `add_0.py`, l'utilise avec des valeurs prédéfinies (par exemple, `a = 1`, `b = 2`), et affiche le résultat formaté.
*   **`1-calculation.py`**:
    *   `calculator_1.py` : Fichier contenant plusieurs fonctions mathématiques de base (`add`, `sub`, `mul`, `div`).
    *   `1-calculation.py` : Script principal qui importe toutes les fonctions de `calculator_1.py` et les utilise pour effectuer et afficher plusieurs calculs.
*   **`2-args.py`**:
    *   Script qui importe le module `sys` et affiche le nombre d'arguments passés en ligne de commande ainsi que la liste de ces arguments.
*   **`3-infinite_add.py`**:
    *   Script qui importe le module `sys` et additionne tous les arguments passés en ligne de commande (qui sont supposés être des entiers).
*   **`4-hidden_discovery.py`**:
    *   Un module compilé `hidden_4.pyc` (fourni).
    *   Script qui charge le module `hidden_4`, et en utilisant `dir()`, trouve et affiche tous les noms définis dans ce module qui ne commencent pas par `__`.
*   **`5-variable_load.py`**:
    *   `variable_load_5.py` : Fichier contenant une variable simple (par exemple, `a = 98`).
    *   `5-variable_load.py` : Script principal qui importe la variable `a` depuis `variable_load_5.py` et l'affiche.
*   **`100-safe_calculator.py` (Avancé)**:
    *
