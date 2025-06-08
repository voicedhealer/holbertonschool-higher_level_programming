python-serialization
Projet Holberton School : Sérialisation et désérialisation en Python

Description
Ce projet porte sur la sérialisation et la désérialisation d’objets en Python, principalement à l’aide du format JSON.
Tu apprendras à :

Convertir des objets Python (ex : instances de classes) en dictionnaires ou en JSON.

Recharger des objets à partir de données sérialisées.

Manipuler des fichiers pour sauvegarder et restaurer des structures de données.

Implémenter des méthodes personnalisées comme to_json() et reload_from_json() dans tes propres classes.

Exemples de fonctionnalités
Classe Student : Sérialisation d’une instance en dictionnaire, filtrage des attributs, rechargement depuis un dictionnaire.

Triangle de Pascal : Génération d’une structure de données en liste de listes, exportable en JSON.

Fichiers principaux
10-student.py : Classe Student avec méthode to_json(attrs=None).

11-student.py : Ajout de la méthode reload_from_json(json).

12-pascal_triangle.py : Fonction qui retourne le triangle de Pascal sous forme de liste de listes.

main.py : Fichiers de test pour chaque exercice.

Utilisation
Exemple pour sérialiser un objet Student :
from 10-student import Student

student = Student("John", "Doe", 23)
print(student.to_json())
# {'first_name': 'John', 'last_name': 'Doe', 'age': 23}
from 10-student import Student

Exemple pour générer le triangle de Pascal :
from 12-pascal_triangle import pascal_triangle

print(pascal_triangle(5))
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Contraintes
Aucun import de module non autorisé (ex : pas d’import de json, pickle, etc. sauf indication).

Respect strict de la PEP 8 (pycodestyle).

Première ligne de chaque fichier exécuté :
#!/usr/bin/python3

Auteur : Vivien Bernardot
Projet réalisé dans le cadre du cursus Holberton School.