# Python - Exceptions

Ce dépôt contient une série d'exercices de programmation en Python axés sur la gestion des exceptions. Les exceptions sont un mécanisme essentiel pour gérer les erreurs de manière propre et robuste dans un programme, permettant de prévoir et de réagir aux situations imprévues.

## Objectifs d'apprentissage

À travers ces exercices, vous allez :

*   Comprendre ce que sont les **exceptions** et pourquoi elles sont importantes.
*   Apprendre à **lever des exceptions** de manière appropriée pour signaler des erreurs.
*   Maîtriser l'utilisation des blocs `try`, `except`, `else`, et `finally` pour **capturer et gérer les exceptions**.
*   Savoir comment **gérer différents types d'exceptions** (par exemple, `TypeError`, `ValueError`, `IndexError`, `FileNotFoundError`, etc.) de manière spécifique.
*   Créer des **exceptions personnalisées** pour des situations d'erreur spécifiques à votre application.
*   Développer des compétences pour écrire du code **robuste et fiable** qui gère les erreurs avec élégance.

## Structure du Projet

Le dépôt est organisé en scripts Python individuels, chacun correspondant à une tâche ou un problème spécifique lié à la gestion des exceptions.

*   Chaque fichier `.py` (par exemple, `0-safe_print_list.py`, `1-safe_function.py`, etc.) contient la solution à un exercice donné.
*   Des fichiers `main.py` correspondants peuvent être fournis pour tester la fonctionnalité de chaque script d'exercice.

## Prérequis

*   **Python 3.x**
*   Un éditeur de texte ou un IDE (comme VS Code, PyCharm, etc.)
*   Aucune bibliothèque externe n'est requise pour les scripts d'exercices principaux.

## Comment utiliser

Chaque script d'exercice peut généralement être exécuté directement depuis la ligne de commande.

1.  **Cloner le dépôt (si ce n'est pas déjà fait) :**
    ```
    git clone [URL_de_votre_depot_git]
    cd python-exceptions
    ```

2.  **Rendre un script exécutable (si un shebang `#!/usr/bin/python3` est présent) :**
    ```
    chmod +x <nom_du_script.py>
    ```

3.  **Exécuter un script :**
    ```
    ./<nom_du_script.py>
    ```
    ou
    ```
    python3 <nom_du_script.py>
    ```

    Si un fichier `main.py` est fourni pour tester un exercice spécifique (par exemple, `0-main.py` pour `0-exercise.py`), vous exécuterez généralement le fichier `main` :
    ```
    ./0-main.py
    ```

## Liste des Tâches / Fichiers

*(Cette section doit être mise à jour au fur et à mesure que vous complétez les exercices. Voici un exemple de comment la structurer.)*

*   **0. Safe list printing** (`0-safe_print_list.py`)
    *   Write a function that prints x elements of a list.
*   **1. Safe printing of an integers list** (`1-safe_print_integer.py`)
    *   Write a function that prints an integer with "{:d}".format().
*   **... (et ainsi de suite pour chaque exercice)**

*(Ici, tu ajouteras une description concise pour chaque fichier/exercice de ton projet)*

## Auteur

*   **[Votre Nom ou Pseudo GitHub]**

## Remerciements (Optionnel)

Ce projet fait partie de [mentionnez le cursus, par exemple, "programme d'ingénierie logicielle ALX", "cursus Holberton School", "mon parcours d'apprentissage personnel en Python", etc.].

## Licence (Optionnel)

Si vous souhaitez rendre votre travail open source, vous pouvez ajouter une licence. Par exemple :
Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.
