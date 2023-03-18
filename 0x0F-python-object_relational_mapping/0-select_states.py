#!/usr/bin/python3
""" List States """
from connect import connect_db
import MySQLdb

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
