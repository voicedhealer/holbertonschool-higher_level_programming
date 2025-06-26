#!/usr/bin/python3
"""
Ce module filtre et liste les états commençant par 'N' (majuscule)
depuis une base de données MySQL.
"""
import sys
import MySQLdb


def main():
    """
    Fonction principale qui se connecte à la base de données, filtre
    les états et affiche les résultats.
    """
    # Connexion à la base de données avec les arguments fournis
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création du curseur pour exécuter des requêtes
    cur = db.cursor()

    # Exécution de la requête avec un filtre binaire sensible à la casse
    query = ("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    cur.execute(query)

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture des connexions
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
