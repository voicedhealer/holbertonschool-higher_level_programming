#!/usr/bin/python3
"""
Script qui se connecte à une base de données MySQL et filtre
les entrées de la table 'states' en fonction d'un nom d'état.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments en ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    try:
        # Établir une connexion à la base de données MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Créer un objet curseur pour exécuter des requêtes SQL
        cursor = db.cursor()

        # Construire la requête SQL avec un paramètre
        # pour éviter les injections SQL
        # La méthode .execute() de MySQLdb échappe
        # automatiquement les paramètres
        query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name_searched,))

        # Récupérer tous les résultats de la requête
        results = cursor.fetchall()

        # Afficher les résultats
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Erreur de connexion ou de requête : {e}")
    finally:
        # Fermer le curseur et la connexion à la base de données
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
