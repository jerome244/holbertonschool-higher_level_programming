#!/usr/bin/python3
"""Lists all cities by state passed by user"""

import MySQLdb
from sys import argv

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    charset="utf8",
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)
cur = conn.cursor()
cur.execute("""
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """, (argv[4],))
rows = cur.fetchall()
print(", ".join([row[0] for row in rows]))
cur.close()
conn.close()
