#!/usr/bin/python3
"""
Script qui se connecte à une base de données MySQL et affiche
toutes les villes d'un état spécifique.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments en ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

        # Requête SQL sécurisée avec jointure et filtrage
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        cursor.execute(query, (state_name,))

        # Récupérer tous les résultats de la requête
        results = cursor.fetchall()

        # Afficher les résultats dans le format requis
        city_names = [row[0] for row in results]
        if city_names:
            print(", ".join(city_names))

    except MySQLdb.Error as e:
        print(f"Erreur de connexion ou de requête : {e}")
    finally:
        # Fermer le curseur et la connexion à la base de données
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
