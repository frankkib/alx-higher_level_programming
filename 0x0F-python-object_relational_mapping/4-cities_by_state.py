#!/usr/bin/python3
"""A script that filters the database"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=db_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    db.close()
