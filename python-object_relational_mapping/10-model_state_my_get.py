#!/usr/bin/python3
"""
Script qui se connecte à une base de données MySQL via SQLAlchemy ORM
et affiche l’ID du State dont le nom est passé en argument.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        print(
            "Usage: ./10-model_state_my_get.py "
            "<username> <password> <database> <state_name>"
        )
        sys.exit(1)

    mysql_username, mysql_password, database_name, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}",
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = (
            session.query(State)
            .filter(State.name == state_name)
            .first()
        )
        if state:
            print(state.id)
        else:
            print("Not found")
    finally:
        session.close()


if __name__ == "__main__":
    main()
