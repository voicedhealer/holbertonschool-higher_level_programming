#!/usr/bin/python3
"""
Script qui ajoute un objet State « Louisiana » à la base de données
hbtn_0e_6_usa via SQLAlchemy ORM et affiche son identifiant.
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: ./11-model_state_insert.py "
            "<mysql_username> <mysql_password> <database_name>"
        )
        sys.exit(1)

    mysql_username, mysql_password, database_name = sys.argv[1], \
        sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Création du nouvel objet State
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        # Affichage de l'ID du nouvel enregistrement
        print(new_state.id)
    except Exception as e:
        session.rollback()
        print(f"Erreur : {e}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
