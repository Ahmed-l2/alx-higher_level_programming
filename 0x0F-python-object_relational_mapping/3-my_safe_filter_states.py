#!/usr/bin/python3
"""
Lists all states from the database `hbtn_0e_0_usa` that starts
with N
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    state_name = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s",
                (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)