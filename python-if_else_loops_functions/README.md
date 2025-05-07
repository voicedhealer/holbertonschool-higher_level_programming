# Python - if/else, loops, functions

![Image Représentant Python if/else, loops, functions](URL_DE_VOTRE_IMAGE_ICI)
*Remplacez `URL_DE_VOTRE_IMAGE_ICI` par le lien direct vers une image pertinente (par exemple, un diagramme de flux, un extrait de code illustratif, ou le logo Python).*

## Description du Projet

Ce projet fait partie du cursus "Programmation de Plus Haut Niveau" de Holberton School et se concentre sur les structures de contrôle fondamentales en Python : les instructions conditionnelles (`if`, `else`, `elif`), les boucles (`for`, `while`), et la définition et l'utilisation de fonctions. La maîtrise de ces concepts est essentielle pour écrire des programmes Python logiques et efficaces.

## Objectifs d'Apprentissage

À la fin de ce projet, vous devriez être capable de :

*   Comprendre et utiliser les instructions conditionnelles `if`, `else`, et `elif`.
*   Comprendre et utiliser les boucles `while` et `for`.
*   Comprendre la différence entre les boucles `for` en Python et dans d'autres langages comme le C.
*   Utiliser les instructions `break` et `continue` pour contrôler le flux des boucles.
*   Utiliser les clauses `else` avec les boucles.
*   Comprendre ce que fait la fonction `range()` et comment l'utiliser.
*   Définir et appeler des fonctions en Python.
*   Comprendre le concept de portée (scope) des variables.
*   Comprendre ce qu'est une trace d'erreur (traceback) et comment l'interpréter.
*   Appliquer les principes arithmétiques de base.
*   Respecter les conventions de style PEP 8.

## Fichiers dans ce Dossier

Ce projet comprendra une série de fichiers `.py` et potentiellement des scripts shell pour les exécuter ou les tester. Voici une liste indicative des types de tâches que l'on pourrait y trouver :

*   **`0-positive_or_negative.py`**: Script qui assigne un nombre aléatoire à une variable et affiche si ce nombre est positif, négatif ou nul.
*   **`1-last_digit.py`**: Script qui assigne un nombre aléatoire à une variable et affiche le dernier chiffre de ce nombre avec des conditions spécifiques.
*   **`2-print_alphabet.py`**: Script qui affiche l'alphabet ASCII en minuscules, sans saut de ligne entre les lettres.
*   **`3-print_alphabt.py`**: Script qui affiche l'alphabet ASCII en minuscules, en excluant certaines lettres.
*   **`4-print_hexa.py`**: Script qui affiche tous les nombres de 0 à 98 en décimal et en hexadécimal.
*   **`5-print_comb2.py`**: Script qui affiche les nombres de 00 à 99, séparés par une virgule et un espace.
*   **`6-print_comb3.py`**: Script qui affiche toutes les combinaisons différentes de deux chiffres.
*   **`7-islower.py`**: Fonction qui vérifie si un caractère est une minuscule.
*   **`8-uppercase.py`**: Fonction qui affiche une chaîne de caractères en majuscules.
*   **`9-print_last_digit.py`**: Fonction qui affiche le dernier chiffre d'un nombre.
*   **`10-add.py`**: Fonction qui additionne deux entiers.
*   **`11-pow.py`**: Fonction qui calcule `a` à la puissance `b`.
*   **`12-fizzbuzz.py`**: Fonction qui implémente le jeu FizzBuzz (affiche les nombres de 1 à 100, remplaçant les multiples de 3 par "Fizz", les multiples de 5 par "Buzz", et les multiples des deux par "FizzBuzz").
*   **`13-insert_number.c`, `list.h` (si lié à des listes chaînées en C)**: Tâche optionnelle ou avancée sur l'insertion d'un nombre dans une liste chaînée triée en C.
*   **`100-print_tebahpla.py`**: Script qui affiche l'alphabet ASCII en sens inverse, en alternant minuscules et majuscules.
*   **`101-remove_char_at.py`**: Fonction qui crée une copie d'une chaîne en supprimant le caractère à une position donnée.
*   **`102-magic_calculation.py`**: Tâche de décompilation de bytecode Python pour reproduire une fonction.

*(Adaptez cette liste avec les noms et descriptions exacts de vos fichiers d'exercices.)*

## Exigences

*   Python 3 (version spécifique précisée par Holberton School, par exemple Python 3.4.3 ou 3.8.5).
*   L'outil `pycodestyle` pour la vérification du style PEP 8.
*   Tous les fichiers doivent être exécutables.
*   Le "shebang" `#!/usr/bin/python3` doit être présent au début de tous les scripts Python.
*   Un fichier `README.md` à la racine du dossier du projet est obligatoire.

## Comment Exécuter et Tester

1.  **Clonez le dépôt principal si ce n'est pas déjà fait.**
2.  **Naviguez vers le dossier du projet :**
    ```
    cd chemin/vers/votre/depot/python-if_else_loops_functions
    ```
3.  **Rendez les scripts exécutables (si nécessaire) :**
    Par exemple, pour un fichier nommé `0-positive_or_negative.py` :
    ```
    chmod +x 0-positive_or_negative.py
    ```
4.  **Exécutez un script :**
    ```
    ./0-positive_or_negative.py
    ```
    Certains scripts pourraient nécessiter des fichiers `main.py` fournis pour les tester (surtout ceux qui définissent des fonctions). Par exemple :
    ```
    ./main_files/7-main.py # (si le fichier de test est dans un sous-dossier main_files)
    ```