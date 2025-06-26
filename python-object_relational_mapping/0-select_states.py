#!/usr/bin/python3
"""
Script qui liste tous les États de
la base de données hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Fonction principale qui exécute la connexion,
    la requête et l'affichage.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
