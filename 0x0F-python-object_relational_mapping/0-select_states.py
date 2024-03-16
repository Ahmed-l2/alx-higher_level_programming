#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(host='localhost', port=3306,  user=argv[1], passwd=argv[2],
                     db=argv[3])

cur = db.cursor()
cur.execute('SELECT * FROM STATES')
rows = cur.fetchall()

for row in rows:
    print(row)
