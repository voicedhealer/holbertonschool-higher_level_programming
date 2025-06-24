#!/usr/bin/python3
"""
Script qui liste tous les États de la base de données hbtn_0e_0_usa.
Prend 3 arguments : mysql username, mysql password, database name.
Utilise le module MySQLdb et se connecte à localhost:3306.
Les résultats sont triés par states.id en ordre croissant.
"""

import MySQLdb
import sys

# Le code ne doit s'exécuter que lorsqu'il est appelé directement,
# pas lorsqu'il est importé.
if __name__ == "__main__":
    # Récupère les arguments de la ligne de commande.
    # sys.argv[0] est le nom du script lui-même.
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = None  # Initialisation à None pour la gestion des erreurs

    try:
        # Établir la connexion à la base de données MySQL.
        # Le port par défaut de MySQL est 3306.
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Créer un objet curseur pour exécuter des requêtes SQL.
        cursor = db.cursor()

        # Exécuter la requête SQL pour sélectionner tous les états, triés par ID.
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Récupérer toutes les lignes du résultat de la requête.
        states = cursor.fetchall()

        # Afficher chaque état au format requis (ID, 'Nom de l'État').
        for state in states:
            print(state) # state est déjà un tuple (id, name)

    except MySQLdb.Error as e:
        # Gérer les erreurs de connexion ou de requête MySQL.
        print(f"Erreur MySQL: {e}")
    finally:
        # S'assurer que la connexion est fermée, même en cas d'erreur.
        if db:
            cursor.close()
            db.close()
