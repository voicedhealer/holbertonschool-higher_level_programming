# 0x0F. Python - Mappage Objet-Relationnel (ORM)

## Description du Projet

Ce projet marque une étape importante dans notre parcours de développement backend en introduisant le concept de **Mappage Objet-Relationnel (ORM)**. Nous explorons comment utiliser des classes Python pour interagir avec des bases de données relationnelles, en évitant d'écrire directement des requêtes SQL pour les opérations CRUD (Create, Read, Update, Delete).

L'objectif principal est de comprendre le rôle et les avantages des ORM, et d'appliquer ces connaissances pour manipuler des données de base de données à travers du code Python orienté objet.

## Qu'est-ce qu'un ORM ?

Un **Object-Relational Mapper (ORM)** est une bibliothèque de code qui automatise le transfert de données entre un programme orienté objet (comme une application Python) et une base de données relationnelle (comme MySQL).

Au lieu d'écrire du SQL (`SELECT * FROM USERS WHERE zip_code=94107;`), un développeur peut utiliser du code Python pour effectuer les mêmes opérations (`users = Users.objects.filter(zip_code=94107)` avec un ORM comme Django ORM).

**Avantages principaux :**

* **Rapidité de développement :** Permet de rester dans un seul langage (Python) pour interagir avec la base de données, accélérant ainsi le développement, notamment pour les prototypes.
* **Abstraction :** Masque les détails SQL sous-jacents, permettant aux développeurs de travailler avec des objets Python familiers.
* **Portabilité :** Certains ORM permettent de changer de système de gestion de base de données (SGBD) avec un minimum de modifications du code applicatif.


## Concepts Abordés

À travers ce projet, nous abordons les concepts et technologies suivants :

* **ORM (Object-Relational Mapping)** : Compréhension de son fonctionnement et de ses avantages.
* **SQLAlchemy** : Introduction à SQLAlchemy, une boîte à outils SQL et un ORM puissant pour Python.
    * Le **langage d'expression SQL d'SQLAlchemy** pour des requêtes plus directes.
    * La composante **ORM d'SQLAlchemy** pour le mappage objet.
* **Interaction Python-MySQL** : Utilisation de `mysqlclient` (ou `MySQLdb`) pour établir la connexion.
* **Programmation Orientée Objet (POO)** : Application des principes de POO à la manipulation de données.
* **Manipulation de données (CRUD)** : Comment créer, lire, mettre à jour et supprimer des données en utilisant un ORM.


## Description des Fichiers

Chaque fichier de ce répertoire contient une tâche spécifique, démontrant l'utilisation des ORM et des interactions avec la base de données.

* **`0-select_states.py`** : Script Python qui se connecte à une base de données MySQL et liste tous les États.
* **`1-filter_states.py`** : Script Python qui filtre les États commençant par la lettre 'N'.
* **`2-my_filter_states.py`** : Script Python qui prend un argument et filtre les États en toute sécurité.
* **`3-states_id_names.py`** : Script Python qui liste les États et leurs villes.
* **`4-cities_by_state.py`** : Script Python qui liste les villes par État.
* **`5-filter_cities.py`** : Script Python qui filtre les villes par nom d'État.
* **`6-model_state.py`** : Définition de la classe `State` mappée à une table MySQL.
* **`7-model_state_fetch_all.py`** : Utilisation de `State` pour récupérer tous les États.
* **`8-model_state_fetch_first.py`** : Utilisation de `State` pour récupérer le premier État.
* **`9-model_state_filter_a.py`** : Utilisation de `State` pour filtrer les États contenant 'a'.
* **`10-model_state_my_get.py`** : Utilisation de `State` pour récupérer un État par son nom.
* **`11-model_state_update_id_2.py`** : Mise à jour d'un État via l'ORM.
* **`12-model_state_delete_id_2.py`** : Suppression d'un État via l'ORM.
* **`13-model_state_add_un.py`** : Ajout de nouveaux États à la base de données.
* **`14-model_state_add_many.py`** : Ajout de plusieurs États simultanément.
* **`15-model_state_delete_all.py`** : Suppression de tous les États dont le nom contient 'a'.

*(Cette liste est un exemple et doit être complétée avec les fichiers réels de votre projet.)*

## Configuration et Utilisation

### Prérequis

* Python 3
* MySQL 8.0
* `mysqlclient` (pour la connexion Python-MySQL)
* `SQLAlchemy`
* Base de données `hbtn_0d_usa` et `hbtn_0d_cities` (avec la structure et les données fournies par Holberton/ALX).

Vous pouvez installer les dépendances Python avec `pip` :

```bash
pip install SQLAlchemy mysqlclient
```


### Exécution des Scripts

Chaque script est un programme Python qui doit être exécuté depuis la ligne de commande. La plupart des scripts nécessiteront des arguments de connexion à la base de données : `mysql_username`, `mysql_password`, `database_name`.

**Syntaxe générale d'exécution :**

```bash
./<nom_du_script.py> <mysql_username> <mysql_password> <database_name>
```

**Exemple pour `0-select_states.py` :**

```bash
./0-select_states.py root votre_mot_de_passe hbtn_0d_usa
```


### Règles de Code et Style (Holberton/ALX)

* Tous les fichiers Python doivent être exécutables (`chmod +x`).
* Le code doit respecter les conventions de style `pycodestyle` (anciennement `PEP 8`).
* Les scripts doivent utiliser la shebang `#!/usr/bin/python3`.
* Le code ne doit pas être importé (il doit s'exécuter seulement quand il est appelé directement).


## Auteur

* Vivien Bernardot

---