# Python - Structures de Données (python-data_structures)

Bienvenue dans le dépôt `python-data_structures` ! Ce projet a pour objectif de fournir une collection claire et concise d'exemples, d'explications et d'exercices sur les structures de données fondamentales en Python.

## Table des matières

1.  [Introduction](#introduction)
2.  [Pourquoi les structures de données sont-elles importantes ?](#pourquoi-les-structures-de-données-sont-elles-importantes-)
3.  [Structures de données couvertes](#structures-de-données-couvertes)
4.  [Comment utiliser ce dépôt](#comment-utiliser-ce-dépôt)
5.  [Prérequis](#prérequis)
6.  [Organisation du dépôt](#organisation-du-dépôt)
7.  [Contributions](#contributions)
8.  [Ressources supplémentaires](#ressources-supplémentaires)
9.  [Licence](#licence)

## Introduction

Les structures de données sont un concept fondamental en informatique. Elles permettent d'organiser, de stocker et de gérer des données de manière efficace afin de pouvoir y accéder et les modifier de façon performante. Python, avec sa syntaxe expressive, offre plusieurs structures de données intégrées puissantes et flexibles.

Ce dépôt vise à :
*   Expliquer le fonctionnement des structures de données courantes en Python.
*   Illustrer leur utilisation à travers des exemples pratiques.
*   Mettre en évidence leurs avantages, inconvénients et cas d'usage typiques.

## Pourquoi les structures de données sont-elles importantes ?

Comprendre et savoir utiliser les bonnes structures de données est crucial pour tout développeur car :
*   Cela permet d'écrire du code plus **efficace** en termes de temps d'exécution et d'utilisation de la mémoire.
*   Cela aide à choisir le **bon outil** pour résoudre un problème algorithmique spécifique.
*   Cela améliore la **lisibilité**, la **maintenance** et la **robustesse** du code.
*   C'est une compétence clé souvent évaluée lors d'**entretiens techniques**.

## Structures de données couvertes

Ce dépôt explorera (ou contient déjà des exemples pour) les structures de données suivantes :

### Structures de données intégrées (Built-in)
*   **Listes (`list`)**:
    *   Description : Collections ordonnées, modifiables (mutables) et hétérogènes.
    *   Exemples : création, accès, modification, méthodes courantes (`append`, `insert`, `remove`, `pop`, `sort`, etc.), slicing, compréhension de listes.
*   **Tuples (`tuple`)**:
    *   Description : Collections ordonnées, non modifiables (immutables) et hétérogènes.
    *   Exemples : création, accès, slicing, empaquetage et déballage (packing/unpacking).
*   **Dictionnaires (`dict`)**:
    *   Description : Collections non ordonnées (ordonnées depuis Python 3.7+) de paires clé-valeur, modifiables. Les clés doivent être uniques et immutables.
    *   Exemples : création, accès, modification, suppression d'éléments, méthodes courantes (`keys`, `values`, `items`), itération.
*   **Ensembles (`set`, `frozenset`)**:
    *   Description : Collections non ordonnées d'éléments uniques. `set` est modifiable, `frozenset` est immutable.
    *   Exemples : création, opérations sur les ensembles (union, intersection, différence), tests d'appartenance.
*   **Chaînes de caractères (`str`)**:
    *   Description : Séquences ordonnées et immuables de caractères Unicode.
    *   Exemples : création, slicing, méthodes de manipulation de chaînes.

### Structures de données plus avancées (ou implémentations basées sur les types intégrés)
*   **(Optionnel) Piles (Stacks)**
    *   Description : Structure LIFO (Last-In, First-Out).
    *   Implémentation : Souvent avec des listes (`append()` et `pop()`).
*   **(Optionnel) Files d'attente (Queues)**
    *   Description : Structure FIFO (First-In, First-Out).
    *   Implémentation : Souvent avec `collections.deque`.
*   **(Optionnel) Listes Chaînées (Linked Lists)**
    *   Description : Séquence d'éléments où chaque élément pointe vers le suivant.
*   **(Optionnel) Arbres (Trees)**
    *   Description : Structure hiérarchique.
*   **(Optionnel) Graphes (Graphs)**
    *   Description : Ensemble de nœuds et d'arêtes.
