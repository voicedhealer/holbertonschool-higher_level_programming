# Projet Python : Hello, World

![Image Représentant Python Hello World](https://github.com/voicedhealer/holbertonschool-higher_level_programming/blob/main/python-hello_world/assets_task_01jszk0ex8e6manstat6hrhwpd_1745890688_img_0.webp)

## Description du Projet

Ce projet est la première introduction au langage de programmation Python dans le cadre du cursus "Programmation de Plus Haut Niveau" de Holberton School. L'objectif principal est de se familiariser avec l'environnement Python, la syntaxe de base pour afficher du texte, et la manière d'exécuter des scripts Python.

## Objectifs d'Apprentissage

À la fin de ce projet, vous devriez être capable de :

*   Comprendre et expliquer pourquoi Python est un langage adapté à la programmation de haut niveau.
*   Utiliser l'interpréteur Python.
*   Écrire et exécuter un script Python simple.
*   Comprendre l'importance du "shebang" (`#!/usr/bin/python3`) dans les scripts Python.
*   Utiliser la fonction `print` pour afficher des chaînes de caractères.
*   Comprendre le concept de chaînes de caractères (strings) et comment les manipuler basiquement.
*   Vérifier la conformité de votre code avec le guide de style PEP 8 en utilisant `pycodestyle`.

## Fichiers dans ce Dossier

*   **`0-run` (ou un nom similaire pour un script shell)** : Un script shell qui exécute un code Python.
*   **`1-run_inline` (ou un nom similaire)** : Un script shell qui exécute du code Python directement en ligne de commande.
*   **`2-print.py` (ou un nom similaire)** : Un script Python qui affiche une chaîne de caractères spécifique en utilisant la fonction `print`.
    ```
    print("\"Programming is like building a multilingual puzzle")
    ```
*   **`3-print_number.py` (ou un nom similaire)** : Un script Python qui affiche un entier suivi d'une chaîne de caractères, en utilisant les f-strings pour le formatage.
    ```
    number = 98
    print(f"{number:d} Battery street")
    ```
*   **`4-print_float.py` (ou un nom similaire)** : Un script Python qui affiche un nombre à virgule flottante avec une précision de deux décimales.
*   **`5-print_string.py` (ou un nom similaire)** : Un script Python qui affiche une chaîne de caractères plusieurs fois et sa sous-chaîne.
*   **`6-concat.py` (ou un nom similaire)** : Un script Python qui concatène deux chaînes de caractères.
*   **`7-edges.py` (ou un nom similaire)** : Un script Python qui manipule une chaîne pour en extraire des parties spécifiques.
*   **`8-concat_edges.py` (ou un nom similaire)** : Un script Python qui effectue des opérations de découpage et de concaténation de chaînes.
*   **`10-check_cycle.c`, `list.h` (si un lien avec C est fait pour des structures de données comme les listes chaînées)** : Fichiers C si le projet inclut une tâche sur la détection de cycle dans une liste chaînée (parfois lié aux premiers modules Python).
*   **`main.py` ou fichiers `main_*.py`** : Fichiers principaux utilisés pour tester vos scripts.
*   **`README.md`** : Ce fichier d'information.

*(Adaptez la liste des fichiers ci-dessus aux fichiers réels présents dans votre dossier `python-hello_world`.)*

## Exigences

*   Python 3 (généralement une version spécifique comme Python 3.4.3, 3.8.5, etc., est précisée par Holberton School).
*   L'outil `pycodestyle` (anciennement `pep8`) pour vérifier la conformité au style PEP 8.
*   Tous les fichiers doivent être exécutables.
*   Le code doit utiliser un "shebang" : `#!/usr/bin/python3` au début de chaque script Python.

## Comment Exécuter les Scripts

1.  **Assurez-vous que Python 3 est installé.**
2.  **Clonez le dépôt parent si ce n'est pas déjà fait :**
    ```
    git clone https://github.com/voicedhealer/holbertonschool-higher_level_programming.git
    ```
3.  **Naviguez vers le dossier du projet :**
    ```
    cd holbertonschool-higher_level_programming/python-hello_world
    ```
4.  **Rendez les scripts exécutables (si nécessaire) :**
    Par exemple, pour un fichier nommé `2-print.py` :
    ```
    chmod +x 2-print.py
    ```
5.  **Exécutez un script :**
    ```
    ./2-print.py
    ```
    ou pour les scripts shell :
    ```
    ./0-run
    ```

## Vérification du Style

Pour vérifier la conformité de votre code Python avec PEP 8, utilisez `pycodestyle` :
