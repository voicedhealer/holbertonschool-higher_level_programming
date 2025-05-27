# Python - Classes de Base Abstraites (abc)

## Description du Projet

Ce projet a pour objectif d'explorer et de comprendre le concept des classes de base abstraites (ABC) en Python, en utilisant le module `abc`. Les classes de base abstraites fournissent un moyen de définir des "interfaces" ou des "contrats" que les classes dérivées (concrètes) doivent respecter. Elles sont un outil puissant pour construire des hiérarchies de classes robustes et maintenables, en s'assurant que certaines méthodes sont implémentées par les sous-classes.

## Concepts Clés Abordés

*   **Classes de Base Abstraites (ABC)** : Ce qu'elles sont et pourquoi elles sont utiles.
*   **Module `abc`** : Utilisation de `ABC` (ou `ABCMeta`) et du décorateur `@abstractmethod`.
*   **Méthodes abstraites** : Méthodes déclarées dans une ABC qui doivent être implémentées par les sous-classes concrètes.
*   **Instanciation** : Pourquoi une ABC avec des méthodes abstraites non implémentées ne peut pas être instanciée directement.
*   **Héritage et Polymorphisme** : Comment les ABC s'intègrent dans ces concepts.
*   **Conception de l'interface** : Forcer les sous-classes à implémenter une interface spécifique.

## Composants du module `abc`

Le module `abc` fournit l'infrastructure pour définir les classes de base abstraites (ABC) en Python [1, 2]. Les principaux composants que nous utiliserons sont :

*   **`ABC`** : Une classe d'aide qui a `ABCMeta` comme métaclasse. Créer une ABC en héritant simplement de `ABC` est une manière courante d'éviter une utilisation parfois confuse des métaclasses [1, 5].
*   **`ABCMeta`** : La métaclasse pour définir les ABC. On peut aussi définir une ABC en utilisant `metaclass=ABCMeta` dans la définition de la classe [1, 9].
*   **`@abstractmethod`** : Un décorateur pour indiquer les méthodes abstraites. Une classe qui a une métaclasse dérivée de `ABCMeta` ne peut pas être instanciée à moins que toutes ses méthodes abstraites aient été surchargées (implémentées) [5, 6].

## Avantages des ABC

*   **Contrat clair** : Elles définissent un ensemble clair de méthodes que les sous-classes doivent implémenter [5].
*   **Cohérence du code** : Assurent que différentes classes partagent une interface commune, ce qui est utile pour le polymorphisme.
*   **Prévention des erreurs** : Empêchent l'instanciation de classes qui n'ont pas implémenté des fonctionnalités cruciales.
*   **Meilleure conception** : Encouragent une meilleure réflexion sur la hiérarchie des classes et les interfaces [5].

## Structure du Projet (Exemple)

Ce projet sera probablement structuré avec plusieurs fichiers Python, chacun correspondant à une tâche spécifique explorant un aspect des ABC.

*   `0-abc.py` (ou un nom similaire pour la première tâche)
*   `1-task.py`
*   ...
*   `tests/` (répertoire optionnel contenant des fichiers de test, par exemple pour `doctest`)
*   `README.md` (ce fichier)

## Exigences

*   Python 3 (généralement Python 3.8.x pour les projets Holberton)
*   Éditeur de code (VSCode, Vim, Emacs, etc.)
*   Accès à un terminal
*   Le module `abc` fait partie de la bibliothèque standard de Python, donc aucune installation supplémentaire n'est requise.

## Tâches

*   **Tâche 0 : Ma première classe abstraite**
    *   Fichier : `0-animal.py`
    *   Description : Créez une classe abstraite `Animal` avec une méthode abstraite `sound`.
*   **Tâche 1 : Classes concrètes**
    *   Fichier : `1-domestic.py`
    *   Description : Créez deux classes concrètes, `Dog` et `Cat`, qui héritent de `Animal` et implémentent la méthode `sound`.
*   ... (Autres tâches du projet)

## Auteur

Bernardot Vivien

---