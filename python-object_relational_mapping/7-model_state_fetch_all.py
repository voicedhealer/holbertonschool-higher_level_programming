#!/usr/bin/python3
"""
Script qui se connecte à une base de données MySQL via SQLAlchemy ORM
et liste tous les objets State de la base de données.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupérer les arguments en ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Créer l'engine SQLAlchemy avec la chaîne de connexion MySQL
    engine = create_engine(
        f'mysql+mysqldb: // {mysql_username}: {
            mysql_password}@localhost: 3306/{database_name}',
        pool_pre_ping=True
    )

    # Créer une session factory liée à l'engine
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Exécuter la requête pour récupérer tous les états, triés par id
        states = session.query(State).order_by(State.id).all()

        # Afficher les résultats dans le format requis
        for state in states:
            print(f"{state.id}: {state.name}")

    finally:
        # Fermer la session
        session.close()
