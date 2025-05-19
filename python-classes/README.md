# Python - Classes et Programmation Orientée Objet

Bienvenue dans le dépôt du projet `python-classes` ! Ce projet est conçu pour explorer et maîtriser les concepts fondamentaux de la **Programmation Orientée Objet (POO)** en Python. Les classes sont un moyen puissant de structurer le code en regroupant des données (attributs) et des fonctionnalités (méthodes) [1, 9].

## Objectifs d'apprentissage

À travers les exercices de ce projet, vous allez :

*   Comprendre la différence fondamentale entre une **classe** (un modèle) et un **objet/instance** (une réalisation concrète de ce modèle).
*   Savoir définir une classe simple en Python.
*   Maîtriser l'utilisation de la méthode spéciale `__init__` pour initialiser les attributs d'une instance.
*   Comprendre le rôle du paramètre `self` pour faire référence à l'instance actuelle.
*   Différencier et utiliser correctement les **attributs d'instance** (uniques à chaque objet) et les **attributs de classe** (partagés par toutes les instances de la classe) [6, 8, 12].
*   Définir et utiliser des **méthodes d'instance** pour ajouter des comportements à vos objets.
*   Apprendre l'importance de la documentation et comment écrire des **docstrings** claires pour les classes et les méthodes [7, 11].
*   Explorer des concepts plus avancés comme les propriétés (`@property`), les getters, les setters, et la notion d'attributs "protégés" ou "privés" par convention (usage du `_` ou `__`).
*   Écrire du code plus modulaire, réutilisable et organisé.

## Concepts Clés

### Classe
Un modèle ou un plan pour créer des objets. Elle définit un ensemble d'attributs et de méthodes que tous les objets créés à partir d'elle posséderont [1, 9].

### Objet (ou Instance)
Une instance spécifique d'une classe. Chaque objet a son propre état (valeurs de ses attributs d'instance) mais partage le comportement (méthodes) défini par sa classe [14].

### `__init__(self, ...)`
Une méthode spéciale (constructeur) appelée automatiquement lors de la création d'une nouvelle instance. Elle sert à initialiser les attributs de l'instance [9, 10].

### `self`
Une référence à l'instance actuelle de la classe. C'est le premier argument de toute méthode d'instance et est utilisé pour accéder aux attributs et méthodes de cette instance [10].

### Attributs d'Instance
Variables qui appartiennent à une instance spécifique d'une classe. Elles sont généralement définies dans `__init__` en utilisant `self.nom_attribut` et sont uniques à chaque objet [6, 8].

### Attributs de Classe
Variables qui appartiennent à la classe elle-même et sont partagées par toutes les instances de cette classe. Elles sont définies directement sous la déclaration de la classe [6, 12, 17].

### Méthodes
Fonctions définies à l'intérieur d'une classe qui opèrent sur les instances de cette classe (méthodes d'instance) ou sur la classe elle-même (méthodes de classe, méthodes statiques) [1].

### Docstrings
Chaînes de documentation utilisées pour expliquer le but et le fonctionnement des classes, méthodes, et modules. Elles sont accessibles via l'attribut `__doc__` [7].

## Structure du Projet

Le dépôt contiendra une série de fichiers Python, chacun se concentrant sur un aspect particulier des classes ou un exercice spécifique.

*   Chaque fichier `.py` (par exemple, `0-square.py`, `1-square.py`, etc.) contiendra l'implémentation d'une ou plusieurs classes selon les exigences de l'exercice.
*   Des fichiers de test (souvent dans un dossier `tests/` ou intégrés comme doctests) pourront accompagner certains exercices pour valider leur fonctionnalité.

## Prérequis

*   **Python 3.x**
*   Un éditeur de texte ou un IDE (comme VS Code, PyCharm, etc.).
*   Compréhension des bases de la syntaxe Python.

## Comment utiliser

Chaque fichier d'exercice peut généralement être exécuté directement ou importé dans un interpréteur Python pour interagir avec les classes et objets définis.
1.  **Naviguez vers le répertoire du projet.**
2.  **Examinez le code** dans les fichiers d'exercice `.py`.
3.  **Exécutez un script (si applicable) :**
    ```
    python3 <nom_du_fichier.py>
    ```
4.  **Ou ouvrez un interpréteur Python** pour importer et tester les classes :
    ```
    python3
    >>> from nom_du_module import NomDeLaClasse
    >>> mon_objet = NomDeLaClasse(...)
    >>> # Interagissez avec mon_objet
    ```

## Liste des Tâches / Fichiers

*(Cette section doit être mise à jour au fur et à mesure que vous complétez les exercices. Voici un exemple.)*

*   **0. Ma première classe Carré** (`0-square.py`)
    *   Définition d'une classe `Square` vide.
*   **1. Carré avec taille** (`1-square.py`)
    *   Ajout d'un attribut de taille à la classe `Square` via `__init__`.
*   **2. Validation de la taille** (`2-square.py`)
    *   Ajout de la validation du type et
