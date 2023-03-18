#!/usr/bin/python3
""" Filter States """
import MySQLdb #For checker
from connect import connect_db


def filter_states():
    """Filters all states ordered by id"""

    db = connect_db()
    cr = db.cursor()
    cr.execute("""SELECT * FROM states
            WHERE name  LIKE 'N%'
            ORDER BY states.id;""")
    # iterate over the result
    for row in cr:
        print(row)


if __name__ == '__main__':
    filter_states()
