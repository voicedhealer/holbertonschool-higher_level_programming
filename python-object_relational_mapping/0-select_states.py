#!/usr/bin/python3
"""
Script qui liste tous les États de
la base de données hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
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
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()

    for id, name in rows:
        print(id, name)
    cursor.close()
    db.close()
