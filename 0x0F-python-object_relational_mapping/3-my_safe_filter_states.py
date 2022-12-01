#!/usr/bin/python3
"""script to take an argument that is safe"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    cont = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], database=argv[3])
    cursor = cont.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
            (argv[4],)
            )
    db =  cursor.fetchall()
    for i in db:
        print(i)
