#!/usr/bin/python3
"""
Ce module se connecte à une base de données MySQL et liste tous les états
de la table 'states', triés par ID en ordre croissant.
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Se connecte à la base de données MySQL et affiche les états.

    Args:
        username (str): Le nom d'utilisateur MySQL.
        password (str): Le mot de passe de l'utilisateur.
        db_name (str): Le nom de la base de données.
    """
    db = None
    try:
        # Établir la connexion à la base de données.
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Créer un objet curseur pour exécuter des requêtes.
        cursor = db.cursor()

        # Exécuter la requête SQL.
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Récupérer tous les résultats.
        states = cursor.fetchall()

        # Afficher chaque état.
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        # Gérer les erreurs MySQL.
        print(f"Erreur MySQL: {e}")
    finally:
        # Fermer la connexion en toute sécurité.
        if db:
            db.close()


if __name__ == "__main__":
    """
    Point d'entrée du script. Récupère les arguments et appelle la fonction
    principale.
    """
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
