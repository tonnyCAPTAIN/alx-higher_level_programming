#!/usr/bin/python3
"""Script that lists all states from a database"""

from sys import agrv
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
