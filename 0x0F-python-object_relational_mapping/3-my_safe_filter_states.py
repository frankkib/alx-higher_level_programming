#!/usr/bin/python3
"""A script that takes argument and displays the states"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
            (state_name,))
 
    for city in cur.fetchall():
        print(city)
    cur.close()
    db.close()
