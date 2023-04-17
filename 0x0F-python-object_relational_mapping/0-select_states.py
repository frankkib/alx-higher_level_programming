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
    """creating cursor object"""
    cursor = db.cursor()
    """excute all sql commands"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """fect all the states"""
    states = cursor.fetchall()

    for state in states:
        print(state)
        """close the cursor and the databse connection"""
    cursor.close()
    db.close()


if __name__ = "__main__":
    list()
