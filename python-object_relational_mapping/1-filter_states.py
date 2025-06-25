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

    # Connexion à la base de données.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Création du curseur.
    cursor = db.cursor()

    # Exécution de la requête avec le filtre
    # BINARY pour la sensibilité à la casse.
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Récupération et affichage des résultats.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture des connexions.
    cursor.close()
    db.close()
