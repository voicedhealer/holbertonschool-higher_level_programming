# 0x0E. SQL - Requêtes Avancées

## Description du Projet

Ce projet est la suite de notre apprentissage de SQL. Il vise à approfondir nos compétences en se concentrant sur des requêtes plus complexes, la gestion des utilisateurs et de leurs permissions, et l'utilisation des clés et des contraintes pour garantir l'intégrité des données dans une base de données relationnelle.

Les scripts de ce répertoire sont conçus pour être exécutés dans un environnement MySQL.

## Concepts Abordés

À travers ce projet, nous avons exploré les concepts suivants :

* Comment créer un nouvel utilisateur MySQL.
* Comment gérer les privilèges d'un utilisateur sur une base de données ou une table spécifique.
* Ce qu'est une **Clé Primaire (PRIMARY KEY)** et comment l'utiliser.
* Ce qu'est une **Clé Étrangère (FOREIGN KEY)** et son rôle dans l'établissement de relations.
* Comment utiliser les contraintes `NOT NULL` et `UNIQUE` pour garantir la qualité des données.
* Comment récupérer des données depuis plusieurs tables en une seule requête.
* L'utilisation des **sous-requêtes (subqueries)**.
* La différence et l'utilisation des jointures **`JOIN`** et de l'opérateur **`UNION`**.


## Description des Fichiers

Chaque fichier `.sql` de ce répertoire correspond à une tâche spécifique visant à mettre en pratique les concepts ci-dessus.

* **`0-privileges.sql`** : Script qui liste tous les privilèges des utilisateurs MySQL `user_0d_1` et `user_0d_2`.
* **`1-create_user.sql`** : Script qui crée l'utilisateur `user_0d_1` et lui accorde tous les privilèges.
* **`2-create_read_user.sql`** : Script qui crée une base de données `hbtn_0d_2` et un utilisateur `user_0d_2` ayant uniquement le privilège `SELECT`.
* **`3-force_name.sql`** : Script qui crée la table `force_name` avec une contrainte `NOT NULL` sur la colonne `name`.
* **`4-first_add.sql`** : Script qui insère une nouvelle ligne dans la table `first_table`.
* **`5-full_table.sql`** : Script qui affiche la description complète de la table `first_table`.
* **`6-states.sql`** : Script qui crée une base de données et une table `states` avec une clé primaire auto-incrémentée.
* **`7-cities.sql`** : Script qui crée la table `cities` avec une clé étrangère faisant référence à la table `states`.
* **`8-count_89.sql`** : Script qui compte le nombre d'enregistrements où `id = 89`.
* **`9-full_creation.sql`** : Script qui crée une seconde table `second_table` et y insère plusieurs lignes.
* **`10-top_score.sql`** : Script qui liste les enregistrements par score décroissant.
* **`11-best_score.sql`** : Script qui liste les enregistrements avec un score >= 10.
* **`12-no_cheating.sql`** : Script qui met à jour le score d'un enregistrement en utilisant `UPDATE`.
* **`13-change_class.sql`** : Script qui supprime des enregistrements en utilisant `DELETE`.
* **`14-average.sql`** : Script qui calcule le score moyen en utilisant la fonction d'agrégation `AVG()`.
* **`15-groups.sql`** : Script qui groupe les enregistrements par score en utilisant `GROUP BY`.
* **`16-shows_by_genre.sql`** : Script qui utilise une `JOIN` pour lister les émissions TV par genre.

*(La liste peut être complétée avec les autres fichiers du projet.)*

## Comment Utiliser les Scripts

Tous les scripts SQL sont conçus pour être exécutés directement depuis la ligne de commande en utilisant une redirection (pipe `|`) vers le client `mysql`. Le nom de la base de données est souvent passé en argument.

### Syntaxe générale

```bash
cat <nom_du_script.sql> | mysql -hlocalhost -uroot -p [nom_de_la_base_de_donnees]
```


### Exemple concret

Pour exécuter le script `3-force_name.sql` sur la base de données `hbtn_0d_2` :

```bash
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
```

Après avoir exécuté cette commande, vous serez invité à entrer le mot de passe de votre utilisateur `root` MySQL.

### Bases de Données Requises

Pour certains exercices, des bases de données de test sont nécessaires. Vous devrez les importer avant de lancer les scripts correspondants :

* Les tâches `3` à `101` utilisent la base de données `hbtn_0d_tvshows`.
* Les tâches `102` à `103` utilisent la base de données `hbtn_0d_tvshows_rate`.


## Auteur

* **[Vivien Bernardot]** -