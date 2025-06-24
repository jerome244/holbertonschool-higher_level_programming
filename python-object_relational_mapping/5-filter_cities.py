#!/usr/bin/python3
"""5-filter_cities.py: Lists all cities of a given state from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 5:
        exit(1)
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (argv[4],)
    )
    rows = cur.fetchall()
    if rows:
        print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
