# Python - Input/Output

## Description

Ce projet (ou ensemble d'exercices) est dédié à l'apprentissage et à la pratique des opérations d'Entrée/Sortie (Input/Output ou I/O) en Python. Les opérations d'I/O sont fondamentales en programmation, car elles permettent aux programmes d'interagir avec le monde extérieur, que ce soit en lisant des données depuis des fichiers, en écrivant des données vers des fichiers, en interagissant avec l'utilisateur via la console, ou en travaillant avec des flux de données.

Ce projet couvre divers aspects des I/O en Python, notamment :

*   La lecture et l'écriture de fichiers texte.
*   La gestion des fichiers avec le gestionnaire de contexte (`with`).
*   La manipulation des modes d'ouverture de fichiers (`r`, `w`, `a`, `r+`, etc.).
*   Le travail avec l'encodage des caractères (ex: UTF-8).
*   La sérialisation et la désérialisation d'objets Python en utilisant le format JSON.
*   La gestion des exceptions liées aux opérations de fichiers.
*   La redirection des entrées/sorties standard (stdin, stdout, stderr) dans certains contextes.

## Objectifs d'Apprentissage

À la fin de ce projet/module, vous devriez être capable de :

*   Ouvrir, lire, écrire et fermer des fichiers en Python de manière sécurisée et efficace.
*   Comprendre et utiliser correctement les différents modes d'ouverture de fichiers.
*   Gérer les encodages de caractères pour éviter les problèmes de compatibilité.
*   Utiliser le module `json` pour sauvegarder et charger des structures de données Python.
*   Structurer votre code pour gérer proprement les erreurs potentielles lors des opérations d'I/O.
*   Comprendre le rôle du gestionnaire de contexte `with` pour la gestion des ressources.

## Contexte

Les opérations d'Entrée/Sortie sont essentielles dans de nombreuses applications :
*   **Manipulation de données** : Chargement de jeux de données, sauvegarde de résultats.
*   **Configuration** : Lecture de fichiers de configuration.
*   **Journalisation (Logging)** : Écriture d'événements et d'erreurs dans des fichiers logs.
*   **Communication inter-processus** : Échange de données entre différents programmes.
*   **Applications Web** : Gestion des requêtes et des réponses, manipulation de fichiers uploadés.

## Structure du Projet / Liste des Tâches (Exemple)

Ce projet peut être structuré autour des tâches suivantes (à adapter selon vos exercices spécifiques) :

1.  **0. Lire un fichier (`0-read_file.py`)**
    *   Écrire une fonction qui lit un fichier texte (UTF-8) et imprime son contenu sur stdout.
    *   Doit utiliser l'instruction `with`.
2.  **1. Écrire dans un fichier (`1-write_file.py`)**
    *   Écrire une fonction qui écrit une chaîne de caractères dans un fichier texte (UTF-8) et retourne le nombre de caractères écrits.
    *   Doit utiliser l'instruction `with`.
    *   Le fichier doit être créé s'il n'existe pas, et son contenu doit être écrasé s'il existe.
3.  **2. Ajouter à un fichier (`2-append_write.py`)**
    *   Écrire une fonction qui ajoute une chaîne de caractères à la fin d'un fichier texte (UTF-8) et retourne le nombre de caractères ajoutés.
    *   Doit utiliser l'instruction `with`.
    *   Le fichier doit être créé s'il n'existe pas.
4.  **3. Objet Python vers chaîne JSON (`3-to_json_string.py`)**
    *   Écrire une fonction qui retourne la représentation JSON d'un objet (chaîne de caractères).
    *   Ne pas gérer les exceptions si l'objet ne peut pas être sérialisé.
5.  **4. Chaîne JSON vers objet Python (`4-from_json_string.py`)**
    *   Écrire une fonction qui retourne un objet Python représenté par une chaîne JSON.
6.  **5. Sauvegarder un objet dans un fichier (`5-save_to_json_file.py`)**
    *   Écrire une fonction qui écrit un Objet dans un fichier texte, en utilisant une représentation JSON.
    *   Doit utiliser l'instruction `with`.
7.  **6. Créer un objet depuis un fichier JSON (`6-load_from_json_file.py`)**
    *   Écrire une fonction qui crée un Objet Python à partir d'un fichier JSON.
    *   Doit utiliser l'instruction `with`.
    *   Si le fichier JSON n'existe pas, ou si la chaîne ne représente pas un JSON valide, la gestion des exceptions n'est pas requise pour cette tâche (ou peut être spécifiée).
... (Adaptez et ajoutez d'autres tâches comme `7-add_item.py`, `8-class_to_json.py`, etc., en fonction de votre curriculum)

## Prérequis

*   Connaissances de base de Python 3.
*   Un environnement Python 3 configuré (par exemple, Ubuntu 20.04 avec Python 3.8+).
*   Éditeur de texte ou IDE (VSCode, PyCharm, Vim, Emacs, etc.).

## Comment Exécuter (Exemple)

Pour chaque tâche, un fichier `main.py` (ex: `0-main.py`, `1-main.py`) est généralement fourni pour tester la fonction que vous avez écrite.

1.  Assurez-vous que vos fichiers de script Python (ex: `0-read_file.py`) sont exécutables :
    ```
    chmod +x 0-read_file.py
    ```
2.  Exécutez le fichier `main` correspondant :
    ```
    ./0-main.py
    ```

## Ressources

*   [Documentation Python sur les opérations d'Input et Output](https://docs.python.org/3/tutorial/inputoutput.html)
*   [Documentation Python sur le module `json`](https://docs.python.org/3/library/json.html)

## Contributeurs

*   Bernardot Vivien
