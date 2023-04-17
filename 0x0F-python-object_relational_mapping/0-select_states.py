#!/usr/bin/python3
"""
a script for printing all states in the database
hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list():

    """connecting to the database"""

    db = MySQLdb.connect(
            host='localhost', port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ = "__main__":
    list()
