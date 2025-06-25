#!/usr/bin/python3
"""
Script qui liste tous les États dont le nom commence par 'N' (majuscule)
depuis la base de données hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupère les arguments de la ligne de commande.
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Établir la connexion à la base de données MySQL.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Créer un objet curseur pour exécuter des requêtes SQL.
    cursor = db.cursor()

    # Définir la requête SQL avec le filtre LIKE BINARY.
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"

    # Exécuter la requête SQL.
    cursor.execute(query)

    # Récupérer toutes les lignes du résultat de la requête.
    rows = cursor.fetchall()

    # Afficher chaque état.
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion.
    cursor.close()
    db.close()
