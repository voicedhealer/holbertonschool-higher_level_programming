# Python - L'Héritage (Inheritance)

Ce projet explore les concepts fondamentaux de l'héritage en Programmation Orientée Objet (POO) avec Python. L'héritage permet à une classe (appelée classe enfant ou sous-classe) d'hériter des attributs et des méthodes d'une autre classe (appelée classe parente ou super-classe). Cela favorise la réutilisation du code, la création de hiérarchies de classes logiques et une meilleure organisation du code [5][7].

## Concepts Clés Abordés

Au travers des exercices de ce projet, les concepts suivants sont mis en pratique :

1.  **Classe Parente (Super-classe) :**
    La classe de base dont les fonctionnalités sont héritées [5]. Dans nos exemples, la classe `Base` sert souvent de point de départ.

2.  **Classe Enfant (Sous-classe) :**
    La classe qui hérite de la classe parente. Elle peut utiliser et étendre les fonctionnalités de sa parente [2][5].
    Syntaxe : `class ChildClass(ParentClass):` [4][6].

3.  **Héritage Simple :**
    Une classe enfant hérite d'une seule classe parente [4][5]. C'est le type d'héritage le plus couramment utilisé dans les premiers exercices.

4.  **Méthode `__init__` et Héritage :**
    *   Si une classe enfant ne définit pas sa propre méthode `__init__`, elle hérite automatiquement de celle de sa classe parente [2].
    *   Si une classe enfant définit sa propre méthode `__init__`, elle **remplace** (override) celle de la parente. Pour exécuter également le `__init__` de la classe parente, il faut l'appeler explicitement [2].

5.  **Fonction `super()` :**
    Un moyen propre et recommandé pour appeler les méthodes de la classe parente (notamment `__init__`) depuis la classe enfant. `super()` permet de rendre le code plus maintenable, surtout en cas d'héritage multiple [2].
    Exemple : `super().__init__(arguments_parent)`

6.  **Attributs de Classe et Attributs d'Instance :**
    *   **Attributs de classe :** Partagés par toutes les instances d'une classe. Utiles pour des compteurs globaux (comme `number_of_instances`) ou des configurations par défaut (comme `print_symbol`).
    *   **Attributs d'instance :** Spécifiques à chaque objet créé. Initialisés dans `__init__` avec `self.nom_attribut`.

7.  **Méthodes Magiques (Dunder Methods) :**
    *   `__str__(self)` : Définit la représentation "lisible par l'humain" d'un objet, utilisée par `print()` et `str()` [1].
    *   `__repr__(self)` : Définit la représentation "officielle" et non ambiguë d'un objet, idéalement permettant de recréer l'objet avec `eval(repr(objet))` [1].
    *   `__del__(self)` : Méthode appelée juste avant qu'un objet ne soit détruit par le garbage collector. Utile pour des messages de "nettoyage" ou de notification.

8.  **Méthodes Statiques (`@staticmethod`) :**
    Méthodes liées à une classe mais qui n'opèrent pas sur une instance spécifique (pas de `self`) ni sur la classe elle-même de manière implicite (pas de `cls`). Elles sont souvent des fonctions utilitaires regroupées logiquement dans la classe.

9.  **Méthodes de Classe (`@classmethod`) :**
    Méthodes qui reçoivent la classe elle-même comme premier argument (conventionnellement `cls`). Souvent utilisées comme des "fabriques" alternatives pour créer des instances de la classe d'une manière spécifique.

10. **Ordre de Résolution des Méthodes (MRO) :**
    Python suit un ordre spécifique pour rechercher les méthodes dans une hiérarchie de classes, surtout en cas d'héritage multiple. Toutes les classes héritent implicitement de la classe `object` [1][3].

## Structure du Projet

Ce projet est constitué d'une série de fichiers Python, chacun construisant sur les concepts du précédent :

*   **`0-lookup.py`**: (Probablement une fonction pour lister les attributs et méthodes disponibles d'un objet, utile pour comprendre ce qui est hérité.)
*   **`1-my_list.py`**: (Probablement une classe `MyList` qui hérite de la classe `list` intégrée et ajoute une fonctionnalité.)
*   **`2-is_same_class.py`**: (Probablement une fonction pour vérifier si un objet est exactement une instance d'une classe donnée.)
*   **`3-is_kind_of_class.py`**: (Probablement une fonction pour vérifier si un objet est une instance d'une classe donnée ou d'une classe qui en hérite.)
*   **`4-inherits_from.py`**: (Probablement une fonction pour vérifier si un objet est une instance d'une classe qui a hérité (directement ou indirectement) d'une classe spécifiée, mais n'est pas une instance de la classe spécifiée elle-même.)
*   **`5-base_geometry.py`**: (Introduction à une classe de base `BaseGeometry`, peut-être vide ou avec des exceptions.)
*   **`6-base_geometry.py`**: (Ajout d'une méthode `area` qui lève une exception, forçant les sous-classes à l'implémenter.)
*   **`7-base_geometry.py`**: (Ajout d'une méthode `integer_validator` pour valider les entrées.)
*   **`8-rectangle.py`**: (Création d'une classe `Rectangle` qui hérite de `BaseGeometry` et implémente `__init__` avec validation.)
*   **`9-rectangle.py`**: (Ajout des méthodes `area` et `__str__` à `Rectangle`.)
*   **`10-square.py`**: (Création d'une classe `Square` qui hérite de `Rectangle`.)
*   **`11-square.py`**: (Surcharge de la méthode `__str__` pour `Square`.)
*   *(Et potentiellement d'autres fichiers explorant des concepts plus avancés comme l'héritage multiple ou les classes abstraites [4][7].)*

## Comment Exécuter les Exemples

Chaque fichier d'exercice `X-nom_fichier.py` est généralement accompagné d'un fichier `X-main.py` qui contient le code pour tester la fonctionnalité implémentée.

Pour tester un exercice :
* python3 X-main.py

Assurez-vous que le fichier de la classe et le fichier main sont dans le même répertoire.

## Apprentissages

Ce projet vise à solidifier la compréhension de :
*   Comment définir des relations parent-enfant entre les classes.
*   Comment les attributs et méthodes sont hérités.
*   Comment surcharger (override) les méthodes des classes parentes.
*   L'utilisation de `super()` pour appeler les méthodes des parents.
*   La différence et l'utilisation des attributs/méthodes d'instance, de classe, et statiques.
*   L'implémentation de méthodes magiques pour un comportement d'objet personnalisé.

L'héritage est un outil puissant pour créer du code modulaire, réutilisable et facile à maintenir en Python.