#!/usr/bin/python3
"""
Select Cities module
"""
import MySQLdb
import sys


def find_cities():
    """Finds cities with the given state name in database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_term = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %(search_state)s\
                ORDER BY cities.id ASC",
                {'search_state': search_term})

    rows = cur.fetchall()
    inc = 1
    for row in rows:
        if inc < len(rows):
            print(row[0], end=',')
            inc += 1
        else:
            print(row[0])
    cur.close()
    db.close()


if __name__ == "__main__":
    find_cities()
