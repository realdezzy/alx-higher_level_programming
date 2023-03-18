#!/usr/bin/python3
""" Connects to the database"""
from sys import argv
import MySQLdb


def connect_db():
    """ Connects to the database

        Raises:
            ValueError: if number of args is incorrect
    """
    if len(argv) < 4:
        raise ValueError("Incorrect number of arguments")

    db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                         database=argv[3], port=3306)

    return db


if __name__ == "__main__":
    pass
