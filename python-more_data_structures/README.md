# Python - More Data Structures

Ce dépôt contient une série d'exercices de programmation en Python axés sur les structures de données avancées et leurs applications pratiques. Il explore le travail avec les ensembles (sets), les dictionnaires, ainsi que des manipulations plus complexes de listes et de tuples, souvent en mettant l'accent sur la compréhension et l'implémentation de la logique sans dépendre de fonctions intégrées spécifiques ou de modules externes.

## Objectifs d'apprentissage

À travers ces exercices, vous allez :
*   Comprendre et utiliser efficacement les **ensembles (sets)** et leurs opérations.
*   Maîtriser la création, l'accès, l'itération et les méthodes des **dictionnaires**.
*   Appliquer des techniques avancées de manipulation pour les **listes** et les **tuples**.
*   Utiliser les fonctions **lambda**, ainsi que les fonctions d'ordre supérieur comme `map` et `filter` (si couvertes par les exercices).
*   Développer une compréhension approfondie de la gestion des **cas limites** (listes vides, tuples vides, indices hors limites, etc.).
*   Apprendre à implémenter des fonctionnalités spécifiques **sans utiliser certains modules ou fonctions Python intégrées** (par exemple, `max()`, `pop()`, `replace()`), pour renforcer la compréhension des algorithmes sous-jacents.

## Structure du Projet

Le dépôt est organisé en scripts Python individuels, chacun correspondant à une tâche ou un problème spécifique lié aux structures de données plus avancées.

*   Chaque fichier `.py` (par exemple, `0-square_matrix_simple.py`, `1-search_replace.py`, etc.) contient la solution à un exercice donné.
*   Des fichiers `main.py` correspondants peuvent être fournis pour tester la fonctionnalité de chaque script d'exercice.

## Prérequis

*   **Python 3.x**
*   Un éditeur de texte ou un IDE (comme VS Code, PyCharm, etc.)
*   Aucune bibliothèque externe n'est requise pour les scripts d'exercices principaux, conformément aux contraintes des tâches.

## Comment utiliser

Chaque script d'exercice peut généralement être exécuté directement depuis la ligne de commande.

1.  **Cloner le dépôt (si ce n'est pas déjà fait) :**
    ```
    git clone [URL_de_votre_depot_git]
    cd python-more_data_structures
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

*   **0. Nom de l'exercice 0** (`0-nom_fichier.py`)
    *   Description brève de la tâche.
*   **1. Nom de l'exercice 1** (`1-nom_fichier.py`)
    *   Description brève de la tâche.
*   **... (et ainsi de suite pour chaque exercice)**
*   `7-add_tuple.py`: Fonction qui additionne 2 tuples, en gérant les tailles variables.
*   `8-multiple_returns.py`: Fonction qui retourne un tuple avec la longueur d'une chaîne et son premier caractère.
*   `9-max_integer.py`: Fonction qui trouve le plus grand entier d'une liste sans utiliser `max()`.
*   `10-divisible_by_2.py`: Fonction qui trouve tous les multiples de 2 dans une liste.
*   `11-delete_at.py`: Fonction qui supprime l'élément à une position spécifique dans une liste sans utiliser `pop()`.
*   `12-switch.py`: Script qui échange les valeurs de deux variables en une seule ligne.
*   *(Ajoutez ici les autres exercices comme celui sur `no_c` et `print_matrix_integer`)*

## Auteur

*   ** Bernardot Vivien **

## Remerciements (Optionnel)

Ce projet fait partie de [mentionnez le cursus, par exemple, "programme d'ingénierie logicielle ALX", "cursus Holberton School", "mon parcours d'apprentissage personnel en Python", etc.].

## Licence (Optionnel)

Si vous souhaitez rendre votre travail open source, vous pouvez ajouter une licence. Par exemple :
Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.
