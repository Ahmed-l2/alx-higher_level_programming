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
    cur.execute("SELECT cities.name \
                FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY %s \
                ORDER BY cities.id ASC", (state_name,))
    rows = cur.fetchall()

    if rows:
        print(", ".join(row[0] for row in rows[:-1]) + ", " + rows[-1][0])
    else:
        print("")
