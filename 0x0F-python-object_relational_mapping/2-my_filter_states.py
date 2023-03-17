#!/usr/bin/python3
""" Filter States """
from connect import connect_db


def filter_states():
    """Filters all states ordered by id"""

    db = connect_db()
    cr = db.cursor()
    query = "SELECT * FROM states \
             WHERE name='{}' ORDER BY states.id;".format(argv[4])
    cr.execute(query)
    # iterate over the result
    for row in cr:
        print(row)


if __name__ == '__main__':
    filter_states()
