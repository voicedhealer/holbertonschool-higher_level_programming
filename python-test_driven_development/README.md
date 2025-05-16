# Python - Test-Driven Development

Ce dépôt est dédié à l'apprentissage et à la pratique du **Test-Driven Development (TDD)** en Python. Le TDD est une méthodologie de développement logiciel où les tests sont écrits *avant* le code de production. Cela permet de s'assurer que le code répond aux exigences spécifiées et aide à concevoir des logiciels plus robustes et mieux structurés [6, 7, 8].

## Objectifs d'apprentissage

À travers ces exercices, vous allez :
*   Comprendre les principes fondamentaux du Test-Driven Development [6].
*   Apprendre le cycle TDD : **Rouge** (écrire un test qui échoue) -> **Vert** (écrire le code minimal pour faire passer le test) -> **Refactor** (améliorer le code sans changer son comportement) [6].
*   Rédiger des cas de test efficaces qui définissent le comportement attendu des fonctionnalités.
*   Utiliser des modules de test Python comme `unittest` ou `doctest` pour automatiser les tests [3, 4, 5].
*   Développer des fonctions et des modules en suivant une approche "test-first" [6].
*   Gagner en confiance sur la qualité et la fiabilité de votre code grâce à une suite de tests complète.
*   Utiliser les tests comme une forme de documentation et de spécification du comportement du code [5].

## Le Cycle TDD

Le Test-Driven Development suit un cycle court et itératif :
1.  **Écrire un test (Rouge)** : Définissez une nouvelle fonctionnalité et écrivez un test automatisé qui la vérifie. Ce test doit échouer initialement car la fonctionnalité n'est pas encore implémentée.
2.  **Écrire le code minimal (Vert)** : Écrivez juste assez de code de production pour que le test (et tous les tests précédents) passe.
3.  **Refactoriser (Bleu/Optionnel)** : Améliorez la structure et la lisibilité du code de production et/ou des tests, sans en altérer le comportement externe. Assurez-vous que tous les tests continuent de passer.
4.  Répétez le cycle pour la prochaine fonctionnalité.

## Structure du Projet

Le dépôt sera généralement organisé avec :
*   Des fichiers Python contenant l'implémentation des fonctionnalités.
*   Un dossier séparé (par exemple, `tests/`) contenant les fichiers de test.
*   Chaque fichier d'exercice (`.py`) sera accompagné de ses tests correspondants.

## Exemple de structure [5] :
nom_du_projet/
module_principal/
init.py
fichier_source.py
tests/
init.py
test_fichier_source.py
README.md


## Prérequis

*   **Python 3.x**
*   Compréhension de base de Python.
*   Un éditeur de texte ou un IDE (comme VS Code, PyCharm, etc.).
*   Connaissance des modules de test Python qui seront utilisés (par exemple, `unittest`, `doctest`).

## Comment utiliser

Les instructions spécifiques pour chaque exercice seront fournies dans les fichiers correspondants. En général :
1.  **Lisez la description de la tâche** pour comprendre la fonctionnalité à implémenter.
2.  **Écrivez les tests** dans le fichier de test approprié (par exemple, en utilisant `unittest.TestCase` ou le format `doctest`). Ces tests doivent initialement échouer.
3.  **Exécutez les tests** pour confirmer qu'ils échouent (phase Rouge).
    *   Pour `unittest` : `python3 -m unittest discover tests` ou `python3 -m unittest tests.test_fichier.py`
    *   Pour `doctest` : `python3 -m doctest -v fichier_avec_doctests.py` ou `python3 -m doctest -v tests/fichier_texte_avec_doctests.txt`
4.  **Écrivez le code de production minimal** dans le fichier source pour faire passer les tests (phase Verte).
5.  **Exécutez à nouveau les tests** pour confirmer qu'ils passent.
6.  **Refactorisez** votre code si nécessaire, en vous assurant que les tests continuent de passer.

## Liste des Tâches / Fichiers

*(Cette section doit être mise à jour au fur et à mesure que vous complétez les exercices. Voici un exemple de comment la structurer.)*

*   **0. Nom de l'exercice 0** (`0-nom_fichier.py`, `tests/test_0-nom_fichier.py`)
    *   Description brève de la tâche et des concepts TDD appliqués.
*   **1. Addition d'entiers** (`add_integer.py`, `tests/0-add_integer.txt`)
    *   Écrire une fonction qui additionne deux entiers, avec gestion des types et casting, en suivant une approche TDD. Tests utilisant `doctest`.
*   **... (et ainsi de suite pour chaque exercice)**

## Auteur

*   **[Votre Nom ou Pseudo GitHub]**

## Remerciements (Optionnel)

Ce projet fait partie de [mentionnez le cursus, par exemple, "programme d'ingénierie logicielle ALX", "cursus Holberton School", "mon parcours d'apprentissage personnel en Python", etc.]. Ce README s'inspire d'exemples de projets TDD disponibles sur GitHub [1, 2, 3].

## Licence (Optionnel)

Si vous souhaitez rendre votre travail open source, vous pouvez ajouter une licence. Par exemple :
Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.
