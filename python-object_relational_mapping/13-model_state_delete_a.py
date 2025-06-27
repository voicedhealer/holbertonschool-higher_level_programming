#!/usr/bin/python3
"""
Script to delete a state in the database.
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage = "Usage: {} <mysql username> <mysql password> <database name>"
        print(usage.format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.ilike("%a%"))\
        .delete(synchronize_session=False)

    session.commit()
    session.close()
