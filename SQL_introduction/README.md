# 0x0D. SQL - Introduction

## Description du Projet

Ce projet est notre première incursion dans le monde des bases de données relationnelles avec **SQL (Structured Query Language)**. L'objectif est de comprendre et de maîtriser les commandes fondamentales de SQL pour interagir avec un serveur de base de données, en l'occurrence **MySQL**.

À travers une série de tâches simples et progressives, nous apprenons à créer, gérer et interroger des bases de données et des tables. Ce projet jette les bases essentielles qui seront nécessaires pour tous les projets de développement backend et de manipulation de données à venir.

## Concepts Abordés

Au cours de ce projet, nous avons appris et mis en pratique les concepts suivants :

* Qu'est-ce qu'une **base de données relationnelle**.
* Qu'est-ce que le langage **SQL**.
* Ce qu'est **MySQL** et comment l'utiliser depuis la ligne de commande.
* Comment créer et supprimer une base de données (`CREATE DATABASE`, `DROP DATABASE`).
* Comment lister les bases de données et les tables (`SHOW`).
* Comment sélectionner une base de données (`USE`).
* Comment créer une table (`CREATE TABLE`) avec des colonnes, des types de données (`INT`, `VARCHAR`, etc.) et des contraintes (`NOT NULL`).
* Comment insérer des données dans une table (`INSERT INTO`).
* Comment sélectionner des données spécifiques depuis une table (`SELECT`, `WHERE`, `ORDER BY`).
* Comment mettre à jour des enregistrements existants (`UPDATE`).
* Comment supprimer des enregistrements (`DELETE`).
* L'utilisation des fonctions d'agrégation de base (`COUNT`, `AVG`, `SUM`, `MAX`, `MIN`).
* La différence entre un guillemet simple (`'`) et un guillemet double (`"`) en SQL.


## Description des Fichiers

Chaque fichier `.sql` de ce répertoire correspond à une tâche spécifique visant à mettre en pratique les concepts ci-dessus.

* **`0-list_databases.sql`** : Script qui liste toutes les bases de données présentes sur le serveur MySQL.
* **`1-create_database_if_missing.sql`** : Script qui crée la base de données `hbtn_0c_0` sans échouer si elle existe déjà.
* **`2-remove_database.sql`** : Script qui supprime la base de données `hbtn_0c_0` sans échouer si elle n'existe pas.
* **`3-list_tables.sql`** : Script qui liste toutes les tables d'une base de données spécifiée.
* **`4-first_table.sql`** : Script qui crée une table nommée `first_table` avec deux colonnes (`id` et `name`).
* **`5-full_table.sql`** : Script qui affiche la description complète de la table `first_table`.
* **`6-list_values.sql`** : Script qui liste toutes les lignes de la table `first_table`.
* **`7-insert_a_row.sql`** : Script qui insère une nouvelle ligne dans la table `first_table`.
* **`8-count_89.sql`** : Script qui compte le nombre d'enregistrements où `id = 89`.
* **`9-full_creation.sql`** : Script qui crée une table `second_table` et y insère plusieurs enregistrements.
* **`10-top_score.sql`** : Script qui liste les enregistrements avec un score >= 10, triés par score décroissant.
* **`11-best_score.sql`** : Script qui liste les enregistrements par score (top 3) de la table `second_table`.
* **`12-no_cheating.sql`** : Script qui met à jour le score de "Bob" à 10 en utilisant `UPDATE`.
* **`13-change_class.sql`** : Script qui supprime tous les enregistrements avec un score <= 5 en utilisant `DELETE`.
* **`14-average.sql`** : Script qui calcule le score moyen de tous les enregistrements et le nomme `average`.
* **`15-groups.sql`** : Script qui liste le nombre d'enregistrements ayant le même score, trié par nombre décroissant.
* **`16-no_link.sql`** : Script qui liste tous les enregistrements de la table `second_table` sans nom.


## Comment Utiliser les Scripts

Tous les scripts SQL de ce projet sont conçus pour être exécutés via la ligne de commande en utilisant une redirection (`|`) vers le client `mysql`. Le nom de la base de données est souvent passé en argument lors de l'exécution.

### Syntaxe générale

```bash
cat <nom_du_script.sql> | mysql -hlocalhost -uroot -p [nom_de_la_base_de_donnees]
```


### Exemple concret

Pour exécuter le script qui crée la table `first_table` dans la base de données `hbtn_0c_0` :

```bash
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

Après avoir lancé cette commande, vous serez invité à entrer le mot de passe de votre utilisateur `root` MySQL.

## Auteur

* Vivien Bernardot