# python-everything_is_object

## Description

Ce projet a pour objectif d’illustrer le principe fondamental que **tout en Python est un objet**.  
À travers une série d’exercices progressifs, tu apprendras à manipuler les objets, leurs attributs et méthodes, et comprendras mieux le modèle objet en Python.

## Fonctionnalités

- Exercices couvrant les concepts clés des objets en Python (types, attributs, méthodes)
- Manipulation avancée des objets et compréhension approfondie du modèle objet Python
- Code prêt à être testé avec `pytest` pour assurer la robustesse et la fiabilité
- Respect des bonnes pratiques Python (PEP8, fin de fichier avec une ligne vide)

## Installation

1. Cloner le repository :

```
git clone 
cd python-everything_is_object
```

2. (Optionnel mais recommandé) Créer un environnement virtuel :

```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Installer les dépendances si nécessaire (aucune dépendance externe obligatoire pour ce projet de base) :

```
pip install -r requirements.txt
```

## Utilisation

Exécuter les scripts Python correspondant aux exercices dans le dossier `exercises/`. Exemple :

```
python exercises/exercice_1.py
```

Pour lancer les tests unitaires, utiliser :

```
pytest tests/
```

## Structure du projet

```
python-everything_is_object/
│
├── exercises/             # Exercices à réaliser
│   ├── exercice_1.py
│   ├── exercice_2.py
│   └── ...
│
├── tests/                 # Tests unitaires pour les exercices
│   ├── test_exercice_1.py
│   └── ...
│
├── README.md              # Description du projet
├── requirements.txt       # Dépendances (vide ou minimale)
└── .gitignore             # Fichiers/dossiers ignorés par git (ex: venv/, __pycache__)
```

## Contribution

Les contributions sont les bienvenues !  
Merci de forker le projet et de soumettre une pull request en respectant les normes de codage Python et en ajoutant des tests si possible.

## Licence

Ce projet est sous licence MIT — voir le fichier [LICENSE](LICENSE) pour plus d’informations.

---------------------------------------------------------------------------------------------------------------------------------------------