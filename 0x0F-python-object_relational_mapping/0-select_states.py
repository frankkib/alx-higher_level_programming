#!/usr/bin/env python3
import MySQLdb
import sys
"""a script for printing all states in the database"""

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
