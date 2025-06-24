#!/usr/bin/python3
"""4-cities_by_state.py: Lists all cities with their state name from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
