#!/usr/bin/python3
""" List States """
from sys import argv
import MySQLdb


def connect_db():
    """Connects to the database"""

    db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                         database=argv[3], port=3306)

    return db


def list_states():
    """Lists all states ordered by id"""

    db = connect_db()
    cr = db.cursor()
    cr.execute("""SELECT * FROM states
            ORDER BY states.id;""")
    # iterate over the result
    for row in cr:
        print(row)


if __name__ == '__main__':
    list_states()
